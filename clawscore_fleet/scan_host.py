"""Read-only host scan and merge.

Walks WALK_TOPS with idle_linux.discover_all, identifies each install from
fingerprints/db.json, and reports advisories through the lab CVE and GHSA-only
path. An unknown verdict is not clean: vulnerable is null, the row is listed
in unidentified, and fixorder leaves it out.
"""

from __future__ import annotations

import csv
import hashlib
import io
import json
import os
import re
from pathlib import Path

from clawscore_fleet.cves import min_clearing_version, report_for_versions
from clawscore_fleet.export_defender import INT_COLUMNS, column_names, escape_cell
from clawscore_fleet.fingerprint import identify, load_db
from clawscore_fleet.fixorder import fix_order
from clawscore_fleet.ghsa_only import rows_for_install, snapshot_sha256
from clawscore_fleet.idle_linux import (
    MAX_REL_PARTS,
    WALK_TOPS,
    _idle_for,
    _owner_home,
    _path_owner,
    _process_evidence,
    discover_all,
)
from clawscore_fleet.summary import summary_from_scan
from clawscore_fleet.versions import FEED_NEWEST

UNKNOWN_NOTE = "version was not identified"
_SECRET = re.compile(
    r"(SECRET|TOKEN|PASSWORD|PASSWD|API_KEY|APIKEY|ACCESS_KEY|PRIVATE_KEY|CREDENTIAL)",
    re.IGNORECASE,
)
_MARKS = (
    "dist/cli.runtime.js",
    "dist/abort.runtime.js",
    "dist/.buildstamp",
    "dist/build-info.json",
    "dist/version.js",
    "openclaw.mjs",
    "package.json",
)
_BLOCKED = ("manifest.yaml", "secrets-pool", "plant.json", "defender_view")


def declared_version(install: Path) -> str | None:
    """package.json version string, or None when the field is absent."""
    path = install / "package.json"
    if not path.is_file():
        return None
    try:
        data = json.loads(path.read_text())
    except (OSError, json.JSONDecodeError):
        return None
    if not isinstance(data, dict):
        return None
    version = data.get("version")
    if isinstance(version, str) and version:
        return version
    return None


def version_mismatch(verdict: str, version: str | None, declared: str | None) -> bool:
    """True when the exact fingerprint verdict is not the declared version."""
    return verdict == "exact" and version != declared


def host_fix_order(installs: list[dict]) -> list[dict]:
    """Patch steps for truthy vulnerable rows, each carrying the install id.

    fixorder.fix_order drops rows whose vulnerable value is not truthy, so
    unknown (null) stays out. Host scan.json records those patch steps. The
    id field is the install id the host-mode gate reads.
    """
    steps = []
    for step in fix_order(installs):
        if step.get("action") != "patch":
            continue
        annotated = dict(step)
        annotated["id"] = annotated.get("install")
        steps.append(annotated)
    return steps


def _abs(rel: str) -> str:
    rel = rel.strip("/")
    return "/" + rel if rel else "/"


def _looks_like(install: Path) -> bool:
    return any((install / rel).is_file() for rel in _MARKS)


def _present_paths(install: Path) -> list[str]:
    return [rel for rel in _MARKS if (install / rel).is_file()]


def _hash_rels(install: Path, rels: list[str]) -> dict[str, str | None]:
    found: dict[str, str | None] = {}
    for rel in rels:
        path = install / rel
        if not path.is_file():
            found[rel] = None
            continue
        digest = hashlib.sha256()
        with path.open("rb") as handle:
            for chunk in iter(lambda: handle.read(1024 * 1024), b""):
                digest.update(chunk)
        found[rel] = digest.hexdigest()
    return found


def _openclaw_dirs(root: Path) -> list[str]:
    """node_modules/openclaw directories under WALK_TOPS, including ones with no package.json."""
    found: list[str] = []
    for top in WALK_TOPS:
        base = root / top
        if not base.is_dir():
            continue
        for dirpath, dirnames, _filenames in os.walk(base):
            current = Path(dirpath)
            rel = current.relative_to(root)
            if len(rel.parts) > MAX_REL_PARTS:
                dirnames.clear()
                continue
            matched = current.name == "openclaw" and current.parent.name == "node_modules"
            if not matched:
                continue
            found.append(rel.as_posix())
            dirnames.clear()
    found.sort()
    return found


def _is_secret(name: str) -> bool:
    if not name or name.startswith("LAB_"):
        return False
    return _SECRET.search(name) is not None


def _add_server(name: object, server: object, names: set[str], creds: set[str]) -> None:
    if isinstance(name, str) and name:
        names.add(name)
    if not isinstance(server, dict):
        return
    for block_name in ("env", "headers"):
        block = server.get(block_name)
        if isinstance(block, dict):
            for key in block:
                if isinstance(key, str) and _is_secret(key):
                    creds.add(key)


def _consume_document(doc: dict, names: set[str], creds: set[str], auto: dict) -> None:
    if isinstance(doc.get("autoApprove"), bool):
        auto["value"] = doc["autoApprove"]
    elif doc.get("autoApprove") == "true":
        auto["value"] = True
    elif doc.get("autoApprove") == "false":
        auto["value"] = False
    env = doc.get("env")
    if isinstance(env, dict):
        vars_ = env.get("vars")
        if isinstance(vars_, dict):
            for key in vars_:
                if isinstance(key, str) and _is_secret(key):
                    creds.add(key)
        for key, value in env.items():
            if key in {"shellEnv", "vars"}:
                continue
            if isinstance(key, str) and _is_secret(key) and isinstance(value, (str, int, float)):
                creds.add(key)
    mcp = doc.get("mcp")
    if isinstance(mcp, dict) and isinstance(mcp.get("servers"), dict):
        for name, server in mcp["servers"].items():
            _add_server(name, server, names, creds)
    if isinstance(doc.get("mcpServers"), dict):
        for name, server in doc["mcpServers"].items():
            _add_server(name, server, names, creds)
    if isinstance(doc.get("name"), str) and any(key in doc for key in ("env", "command", "url")):
        _add_server(doc["name"], doc, names, creds)


def _blocked(path: Path) -> bool:
    text = path.as_posix()
    return any(token in text for token in _BLOCKED)


def _config_files(root: Path, rel: str) -> list[Path]:
    install = root / rel
    bases = [install.parent.parent]
    owner = _path_owner(rel)
    if owner:
        bases.append(_owner_home(root, owner))
    candidates: list[Path] = []
    for base in bases:
        candidates.extend(
            [
                base / ".openclaw" / "openclaw.json",
                base / ".clawdbot" / "clawdbot.json",
                base / ".mcp.json",
                base / "mcp.json",
            ]
        )
        mcp_dir = base / ".openclaw" / "mcp"
        if mcp_dir.is_dir():
            candidates.extend(sorted(path for path in mcp_dir.glob("*.json") if path.is_file()))
    seen: set[Path] = set()
    found: list[Path] = []
    for path in candidates:
        if path in seen or _blocked(path) or not path.is_file():
            continue
        seen.add(path)
        found.append(path)
    return found


def _credentials(root: Path, rel: str) -> tuple[list[str], list[str], bool | None, list[str]]:
    """Credential names, MCP server names, autoApprove, and config paths. Values are dropped."""
    names: set[str] = set()
    creds: set[str] = set()
    auto: dict = {"value": None}
    paths: list[str] = []
    for path in _config_files(root, rel):
        try:
            data = json.loads(path.read_text())
        except (OSError, json.JSONDecodeError):
            continue
        if not isinstance(data, dict):
            continue
        _consume_document(data, names, creds, auto)
        paths.append(_abs(path.relative_to(root).as_posix()))
    return sorted(creds), sorted(names), auto["value"], paths


def _unknown_report() -> dict:
    report = report_for_versions([])
    report["note"] = UNKNOWN_NOTE
    report["vulnerable"] = None
    return report


def _idle_by_install(root: Path) -> dict[str, dict]:
    found = {row["install"]: row["idle"] for row in discover_all(root)}
    process_count = None
    for rel in _openclaw_dirs(root):
        if rel in found:
            continue
        install = root / rel
        if (install / "package.json").is_file() or not _looks_like(install):
            continue
        if process_count is None:
            process_count = _process_evidence(root)
        found[rel] = _idle_for(root, rel, process_count)
    return found


def _row(root: Path, rel: str, idle: dict, db: dict) -> dict:
    install = root / rel
    declared = declared_version(install)
    ident = identify(_present_paths(install), lambda rels: _hash_rels(install, rels), db)
    if ident["verdict"] == "unknown":
        report = _unknown_report()
    else:
        report = report_for_versions(ident["candidates"])
    credentials, mcp_servers, auto_approve, config_paths = _credentials(root, rel)
    install_root = _abs(rel)
    files_read = [f"{install_root}/{item}" for item in ident["files_read"]]
    return {
        "id": rel,
        "install_root": install_root,
        "version": ident["version"],
        "verdict": ident["verdict"],
        "candidates": ident["candidates"],
        "family": ident["family"],
        "method": ident["family"] if ident["verdict"] != "unknown" else "none",
        "matched_files": ident["matched_files"],
        "files_read": files_read,
        "cves": report["cve_ids"],
        "ghsa_ids": report["ghsa_ids"],
        "ghsa_only": rows_for_install(ident["version"], ident["candidates"], ident["verdict"]),
        "advisory_count": report["advisories"],
        "advisory_critical": report["critical"],
        "advisory_high": report["high"],
        "advisory_note": report["note"],
        "vulnerable": report["vulnerable"],
        "feed_newest": FEED_NEWEST,
        "credentials": credentials,
        "mcp_servers": mcp_servers,
        "auto_approve": auto_approve,
        "config_paths": config_paths,
        "agent365": None,
        "declared_version": declared,
        "version_mismatch": version_mismatch(ident["verdict"], ident["version"], declared),
        "idle": idle,
    }


def _document(installs: list[dict]) -> dict:
    document = {
        "feed_newest": FEED_NEWEST,
        "osv_snapshot_sha256": snapshot_sha256(),
        "fix_target": min_clearing_version(),
        "installs": installs,
        "unidentified": [item["id"] for item in installs if item.get("verdict") == "unknown"],
        "fix_order": host_fix_order(installs),
    }
    document["summary"] = summary_from_scan(document)
    return document


def _write_scan(out_dir: Path, document: dict, installs: list[dict]) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "scan.json").write_text(json.dumps(document, indent=2, sort_keys=True) + "\n")
    lines = []
    for item in installs:
        for path in item.get("files_read") or []:
            lines.append(f"{item['id']}\t{path}")
    (out_dir / "files-read.log").write_text("\n".join(lines) + ("\n" if lines else ""))


def scan_host(root: Path, out_dir: Path) -> dict:
    """Scan a Linux filesystem image rooted at root. Writes only under out_dir."""
    root = root.resolve()
    if not root.is_dir():
        raise SystemExit(f"scan root is not a directory: {root}")
    db = load_db()
    idles = _idle_by_install(root)
    installs = [_row(root, rel, idles[rel], db) for rel in sorted(idles)]
    document = _document(installs)
    _write_scan(out_dir, document, installs)
    return document


def _csv_text(rows: list[dict]) -> str:
    headers = column_names()
    buffer = io.StringIO(newline="")
    writer = csv.writer(buffer, lineterminator="\n")
    writer.writerow(headers)
    for row in rows:
        cells = []
        for column in headers:
            value = row.get(column, "")
            text = "" if value is None else str(value)
            if column not in INT_COLUMNS:
                text = escape_cell(text)
            cells.append(text)
        writer.writerow(cells)
    return buffer.getvalue()


def defender_csv(installs: list[dict]) -> str:
    """Defender CSV. Unidentified rows have an empty Version and the advisory note."""
    fix_target = min_clearing_version() or ""
    rows = []
    for item in installs:
        unknown = item.get("verdict") == "unknown"
        note = item.get("advisory_note") or ""
        if unknown and not note:
            note = UNKNOWN_NOTE
        version = "" if unknown else str(item.get("version") or "")
        rows.append(
            {
                "Agent name": item.get("id") or "",
                "Version": version,
                "Device name": item.get("id") or "",
                "Device ID": "",
                "OS platform": "linux",
                "Device type": "",
                "Account name": "",
                "Account domain": "",
                "Risk level": "",
                "Risk indicators": "",
                "Recommendations": note if unknown else "",
                "MCP servers": str(len(item.get("mcp_servers") or [])),
                "Local MCPs": str(len(item.get("mcp_servers") or [])),
                "First seen": "",
                "cs_build_verdict": item.get("verdict") or "",
                "cs_candidates": "|".join(str(part) for part in (item.get("candidates") or [])),
                "cs_reads": str(len(item.get("files_read") or [])),
                "cs_stripped": "false",
                "cs_ghsa_ids": "|".join(str(part) for part in (item.get("ghsa_ids") or [])),
                "cs_cve_ids": "|".join(str(part) for part in (item.get("cves") or [])),
                "cs_ghsa_only_count": str(len(item.get("ghsa_only") or [])),
                "cs_crit_high_count": str((item.get("advisory_critical") or 0) + (item.get("advisory_high") or 0)),
                "cs_readable_secret_classes": "|".join(str(part) for part in (item.get("credentials") or [])),
                "cs_fix_target": fix_target,
                "cs_feed_newest": str(item.get("feed_newest") or FEED_NEWEST),
            }
        )
    return _csv_text(rows)


def merge_host(in_dirs: list[Path], out_dir: Path, defender: Path | None = None) -> dict:
    """Concatenate host scan.json files, then run fixorder and write a Defender CSV."""
    installs: list[dict] = []
    for directory in in_dirs:
        path = directory / "scan.json"
        if not path.is_file():
            raise SystemExit(f"missing scan.json: {path}")
        document = json.loads(path.read_text())
        rows = document.get("installs") or []
        if not isinstance(rows, list):
            raise SystemExit(f"scan.json installs is not a list: {path}")
        installs.extend(rows)
    document = _document(installs)
    _write_scan(out_dir, document, installs)
    csv_path = defender if defender is not None else out_dir / "defender_local_agents.csv"
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    csv_path.write_text(defender_csv(installs))
    return document
