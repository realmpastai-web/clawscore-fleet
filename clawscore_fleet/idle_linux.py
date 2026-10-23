"""Idle-Linux discovery and offline version recovery.

Finds every installed gateway under usr, opt, root, and home, confirms each
one is idle (that owner's user unit, enable symlink, linger marker, and no
process evidence), and recovers the version from dist/build-info.json when
package.json has no version string. The hashed dist listing must meet the
Jaccard threshold against the reversed openclaw@2026.4.15 names.
"""

from __future__ import annotations

import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

from clawscore_fleet.fixtures.idle_linux import LAYOUTS, build_fixture
from clawscore_fleet.versions import ROOT

GATE = ROOT / "inputs" / "rea-gate-idle-linux"
SCHEMA = ROOT / "inputs" / "rea-agent365-schema"
FEED = ROOT / "inputs" / "clawscore-feed-csv-2026-10-17" / "ghsa-all.json"
EVIDENCE_REA = ROOT / "evidence" / "rea" / "idle-linux"
# The frozen idle-Linux reference script still reads mock-agent365-export.json.
# make verify does not. Published-schema verdicts replace that comparison.
_VERDICT_A = re.compile(r"^VERDICT A idle host not exposed: (\S+) \((.*)\)\s*$")
_VERDICT_B = re.compile(r"^VERDICT B per-build GHSA list not exposed: (\S+) \((.*)\)\s*$")
_SCOPE = re.compile(r"^SCOPE (.+)$")
_VERSION_LINE = re.compile(r"^PASS\tG2\.agentsinfo_has_version\t(.*)$")
# Threshold from inputs/rea-gate-idle-linux/discover_recover.py and the task spec.
JACCARD_MIN = 0.99
# G3 in inputs/rea-gate-idle-linux/gate_idle_linux.py.
CHANGELOG_GHSA_LEN = 30
HOST_ID = "idle-linux"
VERSION_SOURCE = "build-info+dirlist"
# clawscore() in inputs/clawscore-idle-paths/gate_idle_paths.py walks these
# four tops and ignores relative paths longer than 9 parts.
WALK_TOPS = ("usr", "opt", "root", "home")
MAX_REL_PARTS = 9


def _fingerprint() -> dict:
    return json.loads((GATE / "dirlist_fingerprint.json").read_text())


def _expected_names() -> list[str]:
    fingerprint = _fingerprint()
    path = GATE / fingerprint["names_file"]
    return [line.strip() for line in path.read_text().splitlines() if line.strip()]


def _blank_version(fingerprint_version: str) -> dict:
    return {
        "package_json_has_version": False,
        "from_build_info": None,
        "buildstamp_head": None,
        "dirlist_jaccard": 0.0,
        "dirlist_match": False,
        "recovered": None,
        "fingerprint_version": fingerprint_version,
    }


def _blank_found(fingerprint_version: str) -> dict:
    return {
        "install": None,
        "idle": {
            "user_unit": False,
            "enabled_symlink": False,
            "linger_markers": [],
            "running_process_evidence": 0,
        },
        "version": _blank_version(fingerprint_version),
        "recovered_without_package_version": False,
        "resolved_version": None,
        "version_source": "",
    }


def _process_evidence(root: Path) -> int:
    """Count proc cmdline files and pid files. The fixture has neither."""
    count = 0
    proc = root / "proc"
    if proc.is_dir():
        for child in proc.iterdir():
            if (child / "cmdline").is_file():
                count += 1
    for dirpath, dirnames, filenames in os.walk(root):
        if Path(dirpath) == proc:
            dirnames.clear()
            continue
        count += sum(1 for name in filenames if name.endswith(".pid"))
    return count


_UNIT_KEYS = {"ExecStart", "WorkingDirectory"}
_EXEC_PREFIXES = ("!!", "!", "-", "@", ":", "+")


def _path_owner(rel: str) -> str | None:
    """User named by a home/<user> or root/ install path. Other installs have none.

    The scanned root/ directory is /root, the home of user root.
    """
    parts = Path(rel).parts
    if len(parts) >= 2 and parts[0] == "home" and parts[1] not in {".", ".."}:
        return parts[1]
    if parts and parts[0] == "root" and (len(parts) == 1 or parts[1] not in {".", ".."}):
        return "root"
    return None


def _owner_home(scan_root: Path, owner: str) -> Path:
    """Home of owner inside a scanned tree. root's home is the root/ directory."""
    if owner == "root":
        return scan_root / "root"
    return scan_root / "home" / owner


def _rooted(rel: str) -> str:
    return "/" + rel.strip("/")


def _strip_exec_prefix(token: str) -> str:
    while token:
        for prefix in _EXEC_PREFIXES:
            rest = token[len(prefix) :]
            if token.startswith(prefix) and rest.startswith("/"):
                token = rest
                break
        else:
            break
    return token


def _systemd_tokens(value: str) -> list[str]:
    tokens: list[str] = []
    buf: list[str] = []
    quote: str | None = None
    for char in value:
        if quote is not None:
            if char == quote:
                quote = None
            else:
                buf.append(char)
            continue
        if char in "\"'":
            quote = char
            continue
        if char.isspace():
            if buf:
                tokens.append("".join(buf))
                buf = []
            continue
        buf.append(char)
    if buf:
        tokens.append("".join(buf))
    return tokens


def _openclaw_bin_paths(install_dir: Path, install_abs: str) -> list[str]:
    """Absolute paths of the openclaw bin declared by package.json."""
    package = install_dir / "package.json"
    try:
        payload = json.loads(package.read_text())
    except (OSError, UnicodeError, json.JSONDecodeError):
        return []
    if not isinstance(payload, dict):
        return []
    bin_field = payload.get("bin")
    relatives: list[str] = []
    if isinstance(bin_field, str):
        relatives.append(bin_field)
    elif isinstance(bin_field, dict):
        for value in bin_field.values():
            if isinstance(value, str) and value:
                relatives.append(value)
    paths: list[str] = []
    for relative in relatives:
        if relative.startswith("/"):
            paths.append(relative.rstrip("/") or relative)
        else:
            cleaned = relative.lstrip("./")
            if cleaned:
                paths.append(f"{install_abs}/{cleaned}")
    return paths


def _same_or_under(path: str, root_path: str) -> bool:
    if path == root_path:
        return True
    prefix = root_path.rstrip("/")
    if not prefix:
        return False
    return path.startswith(prefix + "/")


def _token_matches(token: str, install_abs: str, bins: list[str]) -> bool:
    path = _strip_exec_prefix(token)
    if len(path) > 1:
        path = path.rstrip("/")
    if not path.startswith("/") and "/" not in path:
        return False
    if _same_or_under(path, install_abs) or _same_or_under(path, install_abs.lstrip("/")):
        return True
    for bin_path in bins:
        if _same_or_under(path, bin_path) or _same_or_under(path, bin_path.lstrip("/")):
            return True
    return False


def _unit_references(text: str, install_abs: str, bins: list[str]) -> bool:
    for raw in text.splitlines():
        line = raw.split("#", 1)[0].strip()
        if not line or line.startswith("[") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        if key.strip() not in _UNIT_KEYS:
            continue
        for token in _systemd_tokens(value.strip()):
            if _token_matches(token, install_abs, bins):
                return True
    return False


def _read_text_inside(root: Path, path: Path) -> str:
    try:
        resolved_root = root.resolve()
        resolved = path.resolve()
    except OSError:
        return ""
    if resolved != resolved_root and resolved_root not in resolved.parents:
        return ""
    if not resolved.is_file():
        return ""
    try:
        return resolved.read_text(errors="replace")
    except OSError:
        return ""


def _user_dirs(root: Path) -> list[Path]:
    """home/* plus the scanned root/ directory, which is user root's home."""
    dirs: list[Path] = []
    home = root / "home"
    if home.is_dir():
        dirs.extend(sorted((item for item in home.iterdir() if item.is_dir()), key=lambda item: item.name))
    root_home = root / "root"
    if root_home.is_dir():
        dirs.append(root_home)
    return dirs


def _idle_for_system(root: Path, rel: str, process_count: int) -> dict:
    """Owners are home users and root whose units name this install, paired with linger.

    Scans home/*/.config/systemd/user/*.service and root/.config/systemd/user/*.service,
    and the enable symlinks under *.target.wants. A unit matches when ExecStart or
    WorkingDirectory is the install directory or its openclaw bin. Linger markers are
    those users who also have var/lib/systemd/linger/<user>. No match is not idle.
    """
    install_abs = _rooted(rel)
    bins = _openclaw_bin_paths(root / rel, install_abs)
    user_unit = False
    enabled_symlink = False
    linger_markers: list[str] = []
    for user_dir in _user_dirs(root):
        unit_dir = user_dir / ".config" / "systemd" / "user"
        if not unit_dir.is_dir():
            continue
        service_hit = False
        for service in sorted(unit_dir.glob("*.service"), key=lambda item: item.name):
            if not service.is_file():
                continue
            if _unit_references(_read_text_inside(root, service), install_abs, bins):
                service_hit = True
                break
        symlink_hit = False
        for wants_dir in sorted(unit_dir.glob("*.target.wants"), key=lambda item: item.name):
            if not wants_dir.is_dir():
                continue
            for entry in sorted(wants_dir.iterdir(), key=lambda item: item.name):
                if not entry.is_symlink():
                    continue
                if _unit_references(_read_text_inside(root, entry), install_abs, bins):
                    symlink_hit = True
                    break
            if symlink_hit:
                break
        if service_hit:
            user_unit = True
        if symlink_hit:
            enabled_symlink = True
        linger = root / "var" / "lib" / "systemd" / "linger" / user_dir.name
        if (service_hit or symlink_hit) and linger.is_file() and user_dir.name not in linger_markers:
            linger_markers.append(user_dir.name)
    linger_markers.sort()
    return {
        "user_unit": user_unit,
        "enabled_symlink": enabled_symlink,
        "linger_markers": linger_markers,
        "running_process_evidence": process_count,
    }


def _idle_for(root: Path, rel: str, process_count: int) -> dict:
    owner = _path_owner(rel)
    if owner is None:
        return _idle_for_system(root, rel, process_count)
    unit_dir = _owner_home(root, owner) / ".config" / "systemd" / "user"
    unit = unit_dir / "openclaw-gateway.service"
    wants = unit_dir / "default.target.wants" / "openclaw-gateway.service"
    linger = root / "var" / "lib" / "systemd" / "linger" / owner
    return {
        "user_unit": unit.is_file(),
        "enabled_symlink": wants.is_symlink(),
        "linger_markers": [owner] if linger.is_file() else [],
        "running_process_evidence": process_count,
    }


def _measure(install: Path, expected: list[str], fingerprint_version: str) -> tuple[dict, bool, str | None, str]:
    package_json = json.loads((install / "package.json").read_text())
    build_info = install / "dist" / "build-info.json"
    buildstamp = install / "dist" / ".buildstamp"
    from_build_info = json.loads(build_info.read_text()).get("version") if build_info.is_file() else None
    head = json.loads(buildstamp.read_text()).get("head") if buildstamp.is_file() else None
    dist = install / "dist"
    got_names = sorted(path.name for path in dist.glob("*.js")) if dist.is_dir() else []
    if got_names:
        jaccard = len(set(got_names) & set(expected)) / len(set(got_names) | set(expected))
    else:
        jaccard = 0.0
    rounded = round(jaccard, 4)
    match = jaccard >= JACCARD_MIN
    recovered = from_build_info if (not package_json.get("version") and from_build_info) else None
    version = {
        "package_json_has_version": "version" in package_json,
        "from_build_info": from_build_info,
        "buildstamp_head": head,
        "dirlist_jaccard": rounded,
        "dirlist_match": match,
        "recovered": recovered,
        "fingerprint_version": fingerprint_version,
    }
    recovered_ok = bool(recovered) and match and recovered == fingerprint_version
    package_version = package_json.get("version")
    if package_version:
        return version, recovered_ok, package_version, "package.json"
    if recovered_ok:
        return version, recovered_ok, recovered, VERSION_SOURCE
    return version, recovered_ok, recovered or from_build_info, ""


def discover_all(root: Path) -> list[dict]:
    """Discover every openclaw install under the four walk roots.

    A match is a directory named openclaw whose parent is node_modules and
    which contains package.json. Descent stops at the first match, and a
    relative path of more than 9 parts is not searched. Version comes from
    package.json when that field is set, otherwise from dist/build-info.json.
    """
    expected = _expected_names()
    fingerprint_version = _fingerprint()["version"]
    process_count = _process_evidence(root)
    found: list[dict] = []
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
            matched = (
                current.name == "openclaw"
                and current.parent.name == "node_modules"
                and (current / "package.json").is_file()
            )
            if not matched:
                continue
            version, recovered_ok, resolved, source = _measure(current, expected, fingerprint_version)
            install = rel.as_posix()
            found.append(
                {
                    "install": install,
                    "idle": _idle_for(root, install, process_count),
                    "version": version,
                    "recovered_without_package_version": recovered_ok,
                    "resolved_version": resolved,
                    "version_source": source,
                }
            )
            dirnames.clear()
    found.sort(key=lambda item: item["install"])
    return found


def idle_ok(found: dict) -> bool:
    idle = found["idle"]
    return bool(idle["user_unit"]) and bool(idle["enabled_symlink"]) and bool(idle["linger_markers"]) and idle["running_process_evidence"] == 0


def scan_row(found: dict) -> dict:
    """One scan row. state and version_source are set only when recovery holds."""
    recovered = bool(found.get("recovered_without_package_version"))
    version = found["version"]
    return {
        "id": HOST_ID,
        "state": "idle" if idle_ok(found) else "not-idle",
        "version": version.get("recovered") if recovered else None,
        "version_source": VERSION_SOURCE if recovered else "",
        "install": found.get("install"),
        "package_json_has_version": version.get("package_json_has_version"),
        "from_build_info": version.get("from_build_info"),
        "buildstamp_head": version.get("buildstamp_head"),
        "dirlist_jaccard": version.get("dirlist_jaccard"),
        "dirlist_match": version.get("dirlist_match"),
        "idle": found.get("idle"),
    }


def _changelog_ids() -> set[str]:
    return {line.strip() for line in (GATE / "changelog-ghsa-2026.4.15.txt").read_text().splitlines() if line.strip()}


def _parse_schema_stdout(text: str) -> dict:
    """Pull verdict A, verdict B, the scope line, and the Version column note."""
    found = {
        "verdict_a": "",
        "verdict_a_detail": "",
        "verdict_b": "",
        "verdict_b_detail": "",
        "scope": "",
        "agentsinfo_version_line": "",
    }
    for line in text.splitlines():
        match = _VERDICT_A.match(line)
        if match:
            found["verdict_a"] = match.group(1)
            found["verdict_a_detail"] = match.group(2)
            continue
        match = _VERDICT_B.match(line)
        if match:
            found["verdict_b"] = match.group(1)
            found["verdict_b_detail"] = match.group(2)
            continue
        match = _SCOPE.match(line)
        if match:
            found["scope"] = match.group(1).strip()
            continue
        match = _VERSION_LINE.match(line)
        if match:
            found["agentsinfo_version_line"] = match.group(1)
    return found


def published_schema_gate() -> dict:
    """Run the frozen schema script and report the verdicts it prints."""
    script = SCHEMA / "gate_agent365_schema.py"
    frozen_path = SCHEMA / "gate-output.txt"
    actuals = {
        "script": "inputs/rea-agent365-schema/gate_agent365_schema.py",
        "frozen_output": "inputs/rea-agent365-schema/gate-output.txt",
        "exit_code": None,
        "output_matches_frozen": False,
        "verdict_a": "",
        "verdict_a_detail": "",
        "verdict_b": "",
        "verdict_b_detail": "",
        "scope": "",
        "agentsinfo_version_line": "",
    }
    try:
        frozen = frozen_path.read_bytes()
        proc = subprocess.run(
            [sys.executable, script.name],
            cwd=SCHEMA,
            capture_output=True,
            check=False,
            timeout=60,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        actuals["error"] = str(exc)
        return {"pass": False, "actuals": actuals}
    parsed = _parse_schema_stdout(proc.stdout.decode("utf-8", errors="replace"))
    actuals.update(parsed)
    actuals["exit_code"] = proc.returncode
    actuals["output_matches_frozen"] = proc.stdout == frozen
    stderr = proc.stderr.decode("utf-8", errors="replace")
    if stderr:
        actuals["stderr"] = stderr
    ok = (
        proc.returncode == 0
        and actuals["output_matches_frozen"]
        and actuals["verdict_a"] != ""
        and actuals["verdict_b"] != ""
        and actuals["scope"] != ""
    )
    return {"pass": ok, "actuals": actuals}


def _feed_ids() -> set[str]:
    payload = json.loads(FEED.read_text())
    return {item["ghsa_id"] for item in payload}


def _read_sha() -> str:
    path = EVIDENCE_REA / "tarball.sha256"
    if not path.is_file():
        return ""
    parts = path.read_text().split()
    return parts[0] if parts else ""


def _tarball_has_version() -> str:
    path = EVIDENCE_REA / "package-json-version.txt"
    if not path.is_file():
        return ""
    for line in path.read_text().splitlines():
        if line.startswith("has_version_field:"):
            return line.split(":", 1)[1].strip()
    return ""


def _diff_empty(name: str) -> bool:
    path = EVIDENCE_REA / name
    return path.is_file() and path.read_text() == ""


def _expected_sha() -> str:
    payload = json.loads((GATE / "expected-idle-linux.json").read_text())
    return str(payload.get("tarball_sha256") or "")


def evaluate() -> dict:
    """Build a fresh fixture, discover it, and measure the changelog gates."""
    with tempfile.TemporaryDirectory(prefix="clawscore-idle-linux-") as tmp:
        built = build_fixture(Path(tmp))
        rows = discover_all(Path(tmp))
    l3s = next((row for row in rows if row["install"] == LAYOUTS["L3s"]), None)
    found = l3s if l3s is not None else _blank_found(_fingerprint()["version"])
    row = scan_row(found)
    ids = _changelog_ids()
    feed = _feed_ids()
    missing_feed = sorted(ids - feed)
    evidence_ids_path = EVIDENCE_REA / "changelog-ghsa-2026.4.15.txt"
    evidence_ids = set()
    if evidence_ids_path.is_file():
        evidence_ids = {line.strip() for line in evidence_ids_path.read_text().splitlines() if line.strip()}
    sha = _read_sha()
    expected_sha = _expected_sha()
    version = found["version"]
    discovered_pass = idle_ok(found) and row["state"] == "idle" and row["id"] == HOST_ID
    recovered_pass = (
        row["version_source"] == VERSION_SOURCE
        and row["state"] == "idle"
        and version.get("package_json_has_version") is False
        and version.get("recovered") == version.get("from_build_info") == version.get("fingerprint_version")
        and bool(version.get("dirlist_match"))
        and float(version.get("dirlist_jaccard") or 0) >= JACCARD_MIN
        and sha != ""
        and sha == expected_sha
        and _diff_empty("dist-names.diff")
        and _diff_empty("changelog-ghsa.diff")
    )
    changelog_pass = len(ids) == CHANGELOG_GHSA_LEN and (not evidence_ids or evidence_ids == ids)
    gates = {
        "idle_linux_discovered": {
            "pass": discovered_pass,
            "actuals": {
                "id": row["id"],
                "state": row["state"],
                "user_unit": found["idle"]["user_unit"],
                "enabled_symlink": found["idle"]["enabled_symlink"],
                "linger_markers": found["idle"]["linger_markers"],
                "running_process_evidence": found["idle"]["running_process_evidence"],
                "fixture_files": built["files"],
                "dist_js": built["dist_js"],
                "version_in_package_json": built["version_in_package_json"],
            },
        },
        "idle_linux_version_recovered": {
            "pass": recovered_pass,
            "actuals": {
                "version": version.get("recovered"),
                "version_source": row["version_source"],
                "package_json_has_version": version.get("package_json_has_version"),
                "from_build_info": version.get("from_build_info"),
                "buildstamp_head": version.get("buildstamp_head"),
                "dirlist_jaccard": version.get("dirlist_jaccard"),
                "dirlist_match": version.get("dirlist_match"),
                "jaccard_min": JACCARD_MIN,
                "fingerprint_version": version.get("fingerprint_version"),
                "tarball_sha256": sha,
                "tarball_package_json_has_version": _tarball_has_version(),
                "dist_names_diff_empty": _diff_empty("dist-names.diff"),
                "changelog_diff_empty": _diff_empty("changelog-ghsa.diff"),
            },
        },
        "changelog_ghsa_30": {
            "pass": changelog_pass,
            "actuals": {
                "count": len(ids),
                "threshold": CHANGELOG_GHSA_LEN,
                "source": "inputs/rea-gate-idle-linux/changelog-ghsa-2026.4.15.txt",
                "evidence_matches": (not evidence_ids) or evidence_ids == ids,
            },
        },
        "agent365_published_schema": published_schema_gate(),
        "changelog_not_in_feed": {
            "pass": len(missing_feed) >= 1,
            "actuals": {
                "label": "feed_vs_changelog",
                "about": "pinned feed versus on-disk CHANGELOG GHSA ids; not an Agent 365 result",
                "changelog_ids": len(ids),
                "feed_file": "inputs/clawscore-feed-csv-2026-10-17/ghsa-all.json",
                "missing": len(missing_feed),
                "missing_ids_sample": missing_feed[:3],
            },
        },
    }
    return {"gates": gates, "row": row, "fixture": built}


def write_scan_artifacts(row: dict) -> None:
    """Record the idle-Linux scan row and attach it to an existing lab scan."""
    evidence = ROOT / "evidence"
    evidence.mkdir(parents=True, exist_ok=True)
    (evidence / "idle-linux-host.json").write_text(json.dumps(row, indent=2, sort_keys=True) + "\n")
    scan_path = evidence / "scan.json"
    if not scan_path.is_file():
        return
    document = json.loads(scan_path.read_text())
    document["idle_linux"] = [row]
    scan_path.write_text(json.dumps(document, indent=2, sort_keys=True) + "\n")


def main(argv: list[str] | None = None) -> int:
    args = list(sys.argv if argv is None else argv)
    if len(args) < 2:
        print("usage: python -m clawscore_fleet.idle_linux <root>", file=sys.stderr)
        return 2
    rows = discover_all(Path(args[1]))
    print(json.dumps(rows, indent=1))
    ok = bool(rows) and all(idle_ok(row) and row.get("resolved_version") for row in rows)
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
