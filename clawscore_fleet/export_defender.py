"""Defender-shaped export of the v0.2 lab scan.

File A and File B are built from evidence already on disk: scan.json,
version-confusion.csv, cve-map.json, fixorder.json, ps.txt, files-read.log,
and the passing gates in verify-report.json. Cells with no evidence stay empty.

Device ID is a sha256 of device fields recorded on each scan.json install
(docs/defender-export-lab-fields.md). It is lab-derived, Defender format UNPROVEN.
The lab scan has no observation clock, so make export and make verify record one
UTC time in evidence/lab-scan-observed-at.txt and later runs read that line.
PublishedStatus is JSON null.
"""

from __future__ import annotations

import csv
import hashlib
import io
import json
import re
import uuid
from datetime import datetime, timezone
from pathlib import Path

from clawscore_fleet.versions import ROOT, contains_word_safe

EVIDENCE = ROOT / "evidence"
EXPORT_DIR = EVIDENCE / "export"
SPEC_PATH = ROOT / "docs" / "inputs" / "export-spec-v0.2.1.md"
QUOTES_PATH = ROOT / "docs" / "inputs" / "export-spec-quotes.tsv"
CSV_PATH = EXPORT_DIR / "defender_local_agents.csv"
JSONL_PATH = EXPORT_DIR / "agentsinfo_local.jsonl"
SCAN_OBSERVED_AT = EVIDENCE / "lab-scan-observed-at.txt"
SPEC_SHA256 = "ceb33179dda3ac307653d8bece6c13510c9188e60622246d7dc49d8f7e941769"
QUOTES_SHA256 = "b619b766378fd5028771cef2571c73329e5ffc8e3dbb3d4866a4dac0e6e6c4f2"

# Names in spec order. column_names() re-reads the spec and refuses a mismatch.
DEFENDER_COLUMNS = (
    "Agent name",
    "Version",
    "Device name",
    "Device ID",
    "OS platform",
    "Device type",
    "Account name",
    "Account domain",
    "Risk level",
    "Risk indicators",
    "Recommendations",
    "MCP servers",
    "Local MCPs",
    "First seen",
)
CS_COLUMNS = (
    "cs_build_verdict",
    "cs_candidates",
    "cs_reads",
    "cs_stripped",
    "cs_ghsa_ids",
    "cs_cve_ids",
    "cs_ghsa_only_count",
    "cs_crit_high_count",
    "cs_readable_secret_classes",
    "cs_fix_target",
    "cs_feed_newest",
)
# Spec: each cs_ column traces to a passing verify-report gate.
COLUMN_GATES = {
    "cs_build_verdict": ("version_accuracy", "range_verdicts"),
    "cs_candidates": ("version_accuracy", "range_verdicts"),
    "cs_reads": ("reads",),
    "cs_stripped": ("stripped",),
    "cs_ghsa_ids": ("cve_mapping",),
    "cs_cve_ids": ("cve_mapping",),
    "cs_ghsa_only_count": ("cve_mapping",),
    "cs_crit_high_count": ("cve_mapping",),
    "cs_readable_secret_classes": ("blast_recall",),
    "cs_fix_target": ("fix_target",),
    "cs_feed_newest": ("freshness",),
}
SPEC_GATE_NAMES = (
    "stripped",
    "range_verdicts",
    "cve_mapping",
    "blast_recall",
    "fix_target",
    "freshness",
)
JSON_KEYS = (
    "Timestamp",
    "AgentId",
    "Name",
    "AgentName",
    "Platform",
    "Version",
    "PublishedStatus",
    "LifecycleStatus",
    "LastUpdatedDateTime",
    "McpServers",
    "DeclaredTools",
    "RawAgentInfo",
    *CS_COLUMNS,
)
METADATA_KEYS = (
    "vendor",
    "relatedProcess",
    "trustedProcess",
    "autoApprove",
    "deviceName",
    "aadDeviceId",
    "accountName",
    "accountDomain",
    "accountSid",
    "localMcps",
)
CLOUD_KEYS = ("Owners", "Model", "Instructions")
GUID_RE = re.compile(r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$")
ISO_RE = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?Z$")
INT_RE = re.compile(r"\d+")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
VENDOR = "OpenClaw Foundation"
PLATFORM = "LocalAgents"
# Formula triggers from the frozen escape reference. A leading quote is included so unescape is reversible.
DANGER_PREFIX = ("=", "+", "-", "@", "\t", "\r", "\n", "\uff1d", "\uff0b", "\uff0d", "\uff20", "'")
INT_COLUMNS = frozenset(
    {"MCP servers", "Local MCPs", "cs_reads", "cs_ghsa_only_count", "cs_crit_high_count"}
)
PLANTED_SOURCE = ROOT / "inputs/clawscore-feed-csv-2026-10-17/csv/planted-row.source.json"
PLANTED_CSV = EXPORT_DIR / "planted-row.csv"


def escape_cell(value: str) -> str:
    """Prefix a text cell whose first character would start a spreadsheet formula."""
    if value[:1] in DANGER_PREFIX:
        return "'" + value
    return value


def unescape_cell(value: str) -> str:
    """Drop one leading quote added by escape_cell."""
    if value[:1] == "'":
        return value[1:]
    return value


def _csv_shown(column: str, cell: str) -> str:
    if column in INT_COLUMNS:
        return cell
    return unescape_cell(cell)


class SpecError(ValueError):
    pass


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def assert_spec_bytes() -> None:
    if not SPEC_PATH.is_file() or not QUOTES_PATH.is_file():
        raise SpecError("frozen export spec inputs are missing")
    spec_hash = _sha256(SPEC_PATH)
    quotes_hash = _sha256(QUOTES_PATH)
    if spec_hash != SPEC_SHA256 or quotes_hash != QUOTES_SHA256:
        raise SpecError("frozen export spec inputs do not match the pinned sha256")


def _spec_text() -> str:
    assert_spec_bytes()
    return SPEC_PATH.read_text()


def defender_columns_from_spec(text: str) -> list[str]:
    names: list[str] = []
    in_file_a = False
    for line in text.splitlines():
        if line.startswith("FILE A:"):
            in_file_a = True
            continue
        if in_file_a and line.startswith("FILE B:"):
            break
        if not in_file_a or " | " not in line:
            continue
        left = line.split(" | ", 1)[0].strip()
        if left == "col":
            continue
        names.append(left)
    return names


def cs_columns_from_spec(text: str) -> list[str]:
    for line in text.splitlines():
        if not line.startswith("cs_build_verdict "):
            continue
        return [part.split()[0] for part in line.split(" | ") if part.split()]
    raise SpecError("export spec is missing the cs_ column line")


def column_names() -> list[str]:
    text = _spec_text()
    parsed = defender_columns_from_spec(text) + cs_columns_from_spec(text)
    expected = list(DEFENDER_COLUMNS) + list(CS_COLUMNS)
    if parsed != expected:
        raise SpecError("parsed export columns do not match the spec order")
    return expected


def verbatim_flag_lines(text: str | None = None) -> list[str]:
    """UNPROVEN lines, both CONFLICT lines, and the global UNPROVEN section."""
    body = text if text is not None else _spec_text()
    lines = body.splitlines()
    collected: list[str] = []
    in_global = False
    for line in lines:
        if line.startswith("GLOBAL UNPROVENS"):
            in_global = True
        if not in_global:
            continue
        if line.startswith("FILE A:"):
            break
        if line.strip():
            collected.append(line.rstrip())
    for line in lines:
        if line.startswith("ACCEPTANCE"):
            break
        if "UNPROVEN" not in line and "CONFLICT" not in line:
            continue
        item = line.rstrip()
        if item not in collected:
            collected.append(item)
    conflicts = [line for line in collected if "CONFLICT" in line]
    unprovens = [line for line in collected if "UNPROVEN" in line]
    if len(conflicts) != 2 or len(unprovens) < 2:
        raise SpecError("export spec did not yield both CONFLICT lines and the UNPROVEN lines")
    return collected


def iso8601_utc(moment: datetime) -> str:
    """Format an aware datetime as ISO 8601 UTC with second precision."""
    if moment.tzinfo is None:
        raise SpecError("discovery time must be timezone-aware")
    return moment.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def lab_scan_observed_at() -> str:
    """Observation time for First seen, Timestamp, and LastUpdatedDateTime.

    scan.json, scan.log, ps.txt, and verify-report.json do not record a lab
    scan clock. Advisory publish times are feed times, so they are not used.
    The first make export or make verify writes evidence/lab-scan-observed-at.txt.
    Later runs read that committed line and do not consult file mtimes.
    """
    if SCAN_OBSERVED_AT.is_file():
        text = SCAN_OBSERVED_AT.read_text()
        first = text.splitlines()[0].strip() if text.strip() else ""
        if not ISO_RE.fullmatch(first):
            raise SpecError("evidence/lab-scan-observed-at.txt is not ISO 8601 UTC")
        return first
    moment = iso8601_utc(datetime.now(timezone.utc))
    EVIDENCE.mkdir(parents=True, exist_ok=True)
    SCAN_OBSERVED_AT.write_text(moment + "\n")
    return moment


def lab_device_id(install: dict) -> str:
    """sha256 of device fields already recorded for this install.

    The v0.2 lab scan does not record a host or container id. The hash is
    lab-derived, Defender format UNPROVEN. See docs/defender-export-lab-fields.md.
    """
    ident = install.get("id")
    if not isinstance(ident, str) or not ident:
        raise SpecError("install id is missing from scan.json")
    agent = install.get("agent365") or {}
    device = agent.get("device")
    install_root = install.get("install_root")
    config_paths = install.get("config_paths")
    if not isinstance(device, str) or not device:
        raise SpecError(f"{ident} device is missing from scan.json")
    if not isinstance(install_root, str) or not install_root:
        raise SpecError(f"{ident} install_root is missing from scan.json")
    if not isinstance(config_paths, list) or not all(isinstance(item, str) and item for item in config_paths):
        raise SpecError(f"{ident} config_paths are missing from scan.json")
    if not config_paths:
        raise SpecError(f"{ident} config_paths are missing from scan.json")
    payload = {
        "config_paths": sorted(config_paths),
        "device": device,
        "id": ident,
        "install_root": install_root,
    }
    raw = json.dumps(payload, ensure_ascii=True, separators=(",", ":"), sort_keys=True)
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()


def agent_guid(install_id: str) -> str:
    return str(uuid.uuid5(uuid.NAMESPACE_URL, "clawscore-fleet:" + install_id))


def _load_json(path: Path) -> dict:
    if not path.is_file():
        raise SpecError(f"missing {path.relative_to(ROOT)}")
    return json.loads(path.read_text())


def _stripped_by_id() -> dict[str, str]:
    path = EVIDENCE / "version-confusion.csv"
    if not path.is_file():
        raise SpecError("missing evidence/version-confusion.csv")
    with path.open(newline="") as handle:
        rows = list(csv.DictReader(handle))
    found = {}
    for row in rows:
        found[row["install_id"]] = row["stripped"]
    return found


def _read_counts() -> dict[str, int]:
    path = EVIDENCE / "files-read.log"
    if not path.is_file():
        raise SpecError("missing evidence/files-read.log")
    counts: dict[str, int] = {}
    for line in path.read_text().splitlines():
        if not line.strip() or "\t" not in line:
            continue
        ident, _path = line.split("\t", 1)
        counts[ident] = counts.get(ident, 0) + 1
    return counts


def _lifecycle(install_id: str) -> str:
    path = EVIDENCE / "ps.txt"
    if not path.is_file():
        raise SpecError("missing evidence/ps.txt")
    for line in path.read_text().splitlines():
        if not line.strip():
            continue
        parts = line.split("\t")
        if parts[0].strip() != install_id:
            continue
        status = parts[1].strip() if len(parts) > 1 else ""
        if status.startswith("Up"):
            return "Active"
        return ""
    return ""


def _advisory_facts(install: dict, advisories: dict) -> tuple[int, int]:
    ghsa_ids = list(install["ghsa_ids"])
    cve_ids = list(install["cves"])
    only = 0
    critical = 0
    high = 0
    mapped: list[str] = []
    for ghsa_id in ghsa_ids:
        record = advisories.get(ghsa_id)
        if not isinstance(record, dict):
            raise SpecError(f"{install['id']} {ghsa_id} is not in evidence/cve-map.json")
        cve_id = record.get("cve_id")
        if cve_id:
            mapped.append(str(cve_id))
        else:
            only += 1
        severity = record.get("severity")
        if severity == "critical":
            critical += 1
        elif severity == "high":
            high += 1
    if sorted(set(mapped)) != sorted(set(cve_ids)):
        raise SpecError(f"{install['id']} cve ids do not match evidence/cve-map.json")
    if critical != install["advisory_critical"] or high != install["advisory_high"]:
        raise SpecError(f"{install['id']} severity counts do not match evidence/scan.json")
    if len(ghsa_ids) != install["advisory_count"]:
        raise SpecError(f"{install['id']} advisory_count does not match ghsa_ids")
    return only, critical + high


def _gate_value(report: dict, gate_name: str, field: str) -> str:
    gate = (report.get("gates") or {}).get(gate_name) or {}
    if not gate.get("pass"):
        raise SpecError(f"{gate_name} is not passing; refusing cs_ values that trace to it")
    value = gate.get(field)
    if not isinstance(value, str) or not value:
        raise SpecError(f"{gate_name} has no {field}")
    return value


def _shared_cs(report: dict, scan: dict) -> tuple[str, str]:
    fix_target = _gate_value(report, "fix_target", "min_clearing_version")
    feed_newest = _gate_value(report, "freshness", "feed_newest")
    fixorder = _load_json(EVIDENCE / "fixorder.json")
    if fixorder.get("min_clearing_version") != fix_target:
        raise SpecError("evidence/fixorder.json does not match the fix_target gate")
    if scan.get("feed_newest") != feed_newest or report.get("feed_newest") != feed_newest:
        raise SpecError("feed_newest does not match the freshness gate")
    for name in SPEC_GATE_NAMES:
        gate = (report.get("gates") or {}).get(name) or {}
        if not gate.get("pass"):
            raise SpecError(f"{name} is not passing; refusing cs_ values")
    return fix_target, feed_newest


def _cs_for_install(
    install: dict,
    stripped: str,
    read_counts: dict[str, int],
    advisories: dict,
    fix_target: str,
    feed_newest: str,
) -> dict:
    logged = read_counts.get(install["id"], 0)
    reads = len(install.get("files_read") or [])
    if logged != reads:
        raise SpecError(f"{install['id']} files-read.log does not match scan.json")
    only, crit_high = _advisory_facts(install, advisories)
    verdict = install.get("verdict")
    if verdict not in {"exact", "range", "unknown"}:
        raise SpecError(f"{install['id']} verdict is not exact, range, or unknown")
    return {
        "cs_build_verdict": verdict,
        "cs_candidates": [str(item) for item in (install.get("candidates") or [])],
        "cs_reads": reads,
        "cs_stripped": stripped != "none",
        "cs_ghsa_ids": [str(item) for item in install.get("ghsa_ids") or []],
        "cs_cve_ids": [str(item) for item in install.get("cves") or []],
        "cs_ghsa_only_count": only,
        "cs_crit_high_count": crit_high,
        "cs_readable_secret_classes": [str(item) for item in install.get("credentials") or []],
        "cs_fix_target": fix_target,
        "cs_feed_newest": feed_newest,
    }


def _bool_string(value: bool) -> str:
    if value is True:
        return "true"
    if value is False:
        return "false"
    raise SpecError("expected a boolean from the scan")


def build_rows(report: dict) -> list[dict]:
    scan = _load_json(EVIDENCE / "scan.json")
    advisories = (_load_json(EVIDENCE / "cve-map.json").get("advisories") or {})
    stripped = _stripped_by_id()
    read_counts = _read_counts()
    fix_target, feed_newest = _shared_cs(report, scan)
    observed_at = lab_scan_observed_at()
    installs = scan.get("installs") or []
    if not installs:
        raise SpecError("scan.json has no installs")
    rows = []
    for install in installs:
        ident = install["id"]
        if ident not in stripped:
            raise SpecError(f"{ident} is missing from evidence/version-confusion.csv")
        agent = install.get("agent365") or {}
        if not isinstance(install.get("auto_approve"), bool):
            raise SpecError(f"{ident} auto_approve is missing from scan.json")
        agent_auto = agent.get("autoApprove")
        if agent_auto != _bool_string(install["auto_approve"]):
            raise SpecError(f"{ident} autoApprove does not match between scan fields")
        name = str(agent.get("name") or "")
        if not name:
            raise SpecError(f"{ident} agent name is missing from scan.json")
        version = ""
        if install.get("verdict") == "exact":
            version = str(install.get("version") or "")
            if not version:
                raise SpecError(f"{ident} exact verdict has no version in scan.json")
        local_names = [str(item) for item in (install.get("mcp_servers") or [])]
        # Scan records names from local config files and no remote endpoint.
        local_mcps = [
            {"name": item, "transportType": "", "commandName": ""} for item in local_names
        ]
        cs_values = _cs_for_install(install, stripped[ident], read_counts, advisories, fix_target, feed_newest)
        row = {
            "Timestamp": observed_at,
            "AgentId": agent_guid(ident),
            "Name": name,
            "AgentName": name,
            "Platform": PLATFORM,
            "Version": version,
            "PublishedStatus": None,
            "LifecycleStatus": _lifecycle(ident),
            "LastUpdatedDateTime": observed_at,
            "McpServers": [],
            "DeclaredTools": [],
            "RawAgentInfo": {
                "localAgentMetadata": {
                    "vendor": VENDOR,
                    "relatedProcess": str(agent.get("process") or ""),
                    "trustedProcess": "false",
                    "autoApprove": _bool_string(install["auto_approve"]),
                    "deviceName": str(agent.get("device") or ident),
                    "aadDeviceId": "",
                    "accountName": str(agent.get("user") or ""),
                    "accountDomain": "",
                    "accountSid": "",
                    "localMcps": local_mcps,
                }
            },
        }
        row.update(cs_values)
        row["_install_id"] = ident
        row["_device_id"] = lab_device_id(install)
        rows.append(row)
    return rows


def _join_list(items: list[str]) -> str:
    for item in items:
        if "|" in item or "\n" in item or "\r" in item:
            raise SpecError("a cs_ list item contains a separator")
    return "|".join(items)


def _csv_field(column: str, row: dict) -> str:
    meta = row["RawAgentInfo"]["localAgentMetadata"]
    if column == "Agent name":
        return row["Name"]
    if column == "Version":
        return row["Version"]
    if column == "Device name":
        return meta["deviceName"]
    if column == "Device ID":
        return row["_device_id"]
    if column == "OS platform":
        return ""
    if column == "Device type":
        return ""
    if column == "Account name":
        return meta["accountName"]
    if column == "Account domain":
        return meta["accountDomain"]
    if column == "Risk level":
        return ""
    if column == "Risk indicators":
        return ""
    if column == "Recommendations":
        return ""
    if column == "MCP servers":
        return str(len(row["McpServers"]))
    if column == "Local MCPs":
        return str(len(meta["localMcps"]))
    if column == "First seen":
        return row["Timestamp"]
    if column in {"cs_candidates", "cs_ghsa_ids", "cs_cve_ids", "cs_readable_secret_classes"}:
        return _join_list(list(row[column]))
    if column == "cs_stripped":
        return _bool_string(row[column])
    if column in {"cs_reads", "cs_ghsa_only_count", "cs_crit_high_count"}:
        return str(row[column])
    return str(row[column])


def _export_cell(column: str, row: dict) -> str:
    value = _csv_field(column, row)
    if column in INT_COLUMNS:
        return value
    return escape_cell(value)


def _csv_text(rows: list[dict]) -> str:
    headers = column_names()
    buffer = io.StringIO(newline="")
    writer = csv.writer(buffer, lineterminator="\n")
    writer.writerow(headers)
    for row in rows:
        writer.writerow([_export_cell(column, row) for column in headers])
    text = buffer.getvalue()
    if text.splitlines()[0] != ",".join(headers):
        raise SpecError("csv header was quoted and no longer matches the spec list")
    return text


def _jsonl_text(rows: list[dict]) -> str:
    lines = []
    for row in rows:
        body = {key: row[key] for key in JSON_KEYS}
        lines.append(json.dumps(body, ensure_ascii=True))
    return "\n".join(lines) + "\n"


def _reject_planted(text: str) -> None:
    pool = json.loads((ROOT / "fleet" / "secrets-pool.json").read_text())
    for value in pool.values():
        if isinstance(value, str) and value and value in text:
            raise SpecError("export output contains a planted credential value")
    if contains_word_safe(text):
        raise SpecError("export output contains a banned wording token")


def write_exports(report: dict | None = None) -> list[dict]:
    if report is None:
        report = _load_json(EVIDENCE / "verify-report.json")
    rows = build_rows(report)
    csv_body = _csv_text(rows)
    jsonl_body = _jsonl_text(rows)
    _reject_planted(csv_body)
    _reject_planted(jsonl_body)
    EXPORT_DIR.mkdir(parents=True, exist_ok=True)
    CSV_PATH.write_text(csv_body)
    JSONL_PATH.write_text(jsonl_body)
    write_planted_row()
    print(f"wrote {CSV_PATH.relative_to(ROOT)} rows={len(rows)}", flush=True)
    print(f"wrote {JSONL_PATH.relative_to(ROOT)} rows={len(rows)}", flush=True)
    return rows


def write_planted_row(source: Path | None = None, dest: Path | None = None) -> Path:
    """Write one planted CSV row with the same quoter the lab export uses."""
    source = source or PLANTED_SOURCE
    dest = dest or PLANTED_CSV
    payload = json.loads(source.read_text())
    headers = column_names()
    buffer = io.StringIO(newline="")
    writer = csv.writer(buffer, lineterminator="\n")
    writer.writerow(headers)
    cells = []
    for column in headers:
        raw = payload.get(column)
        value = "" if raw is None else str(raw)
        if column not in INT_COLUMNS:
            value = escape_cell(value)
        cells.append(value)
    writer.writerow(cells)
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(buffer.getvalue())
    return dest


def _split_list(cell: str) -> list[str]:
    if cell == "":
        return []
    return cell.split("|")


def _parse_csv_cs(column: str, cell: str):
    if column in {"cs_candidates", "cs_ghsa_ids", "cs_cve_ids", "cs_readable_secret_classes"}:
        return _split_list(cell)
    if column == "cs_stripped":
        if cell == "true":
            return True
        if cell == "false":
            return False
        raise SpecError(f"{column} is not true or false")
    if column in {"cs_reads", "cs_ghsa_only_count", "cs_crit_high_count"}:
        if not cell.isdigit():
            raise SpecError(f"{column} is not an integer")
        return int(cell)
    return cell


def _is_int(value: object) -> bool:
    return isinstance(value, int) and not isinstance(value, bool)


def _string_object(value: object, keys: tuple[str, ...], label: str, errors: list[str]) -> None:
    if not isinstance(value, dict) or tuple(value.keys()) != keys:
        errors.append(f"{label} keys")
        return
    for key in keys:
        if not isinstance(value[key], str):
            errors.append(f"{label}.{key} type")


def _schema_errors(rows: list[dict], scan_count: int) -> list[str]:
    errors: list[str] = []
    if len(rows) != scan_count:
        errors.append(f"jsonl rows {len(rows)} scan installs {scan_count}")
    for index, row in enumerate(rows):
        prefix = f"row {index}"
        if tuple(row.keys()) != JSON_KEYS:
            errors.append(f"{prefix} keys")
            continue
        for banned in CLOUD_KEYS:
            if banned in row:
                errors.append(f"{prefix} cloud column {banned}")
        if not isinstance(row["Timestamp"], str) or not ISO_RE.fullmatch(row["Timestamp"]):
            errors.append(f"{prefix} Timestamp")
        if not isinstance(row["LastUpdatedDateTime"], str) or not ISO_RE.fullmatch(row["LastUpdatedDateTime"]):
            errors.append(f"{prefix} LastUpdatedDateTime")
        if not isinstance(row["AgentId"], str) or not GUID_RE.match(row["AgentId"]):
            errors.append(f"{prefix} AgentId")
        if not isinstance(row["Name"], str) or not isinstance(row["AgentName"], str) or row["Name"] != row["AgentName"]:
            errors.append(f"{prefix} Name")
        if row["Platform"] != PLATFORM:
            errors.append(f"{prefix} Platform")
        if not isinstance(row["Version"], str):
            errors.append(f"{prefix} Version")
        if row["PublishedStatus"] not in {"Draft", "Published", None}:
            errors.append(f"{prefix} PublishedStatus")
        if row["LifecycleStatus"] not in {"Active", "Blocked", "Uninstalled", "Deleted"}:
            errors.append(f"{prefix} LifecycleStatus")
        for key in ("McpServers", "DeclaredTools"):
            items = row[key]
            if not isinstance(items, list):
                errors.append(f"{prefix} {key}")
                continue
            for item in items:
                _string_object(item, ("name", "type", "endpoint"), f"{prefix} {key}", errors)
        raw = row["RawAgentInfo"]
        if not isinstance(raw, dict) or tuple(raw.keys()) != ("localAgentMetadata",):
            errors.append(f"{prefix} RawAgentInfo")
            continue
        meta = raw["localAgentMetadata"]
        if not isinstance(meta, dict) or tuple(meta.keys()) != METADATA_KEYS:
            errors.append(f"{prefix} localAgentMetadata")
            continue
        for key in METADATA_KEYS:
            if key == "localMcps":
                continue
            if not isinstance(meta[key], str):
                errors.append(f"{prefix} {key} type")
        if meta["trustedProcess"] not in {"true", "false"} or meta["autoApprove"] not in {"true", "false"}:
            errors.append(f"{prefix} trustedProcess/autoApprove")
        if not isinstance(meta["localMcps"], list):
            errors.append(f"{prefix} localMcps")
        else:
            for item in meta["localMcps"]:
                _string_object(item, ("name", "transportType", "commandName"), f"{prefix} localMcps", errors)
        device = meta["deviceName"]
        if isinstance(device, str) and device and row["AgentId"] != agent_guid(device):
            errors.append(f"{prefix} AgentId does not match deviceName")
        if row["cs_build_verdict"] not in {"exact", "range", "unknown"}:
            errors.append(f"{prefix} cs_build_verdict")
        for key in ("cs_candidates", "cs_ghsa_ids", "cs_cve_ids", "cs_readable_secret_classes"):
            items = row[key]
            if not isinstance(items, list) or not all(isinstance(item, str) for item in items):
                errors.append(f"{prefix} {key}")
        if not isinstance(row["cs_stripped"], bool):
            errors.append(f"{prefix} cs_stripped")
        for key in ("cs_reads", "cs_ghsa_only_count", "cs_crit_high_count"):
            if not _is_int(row[key]):
                errors.append(f"{prefix} {key}")
        if not isinstance(row["cs_fix_target"], str) or not row["cs_fix_target"]:
            errors.append(f"{prefix} cs_fix_target")
        if not isinstance(row["cs_feed_newest"], str) or not DATE_RE.match(row["cs_feed_newest"]):
            errors.append(f"{prefix} cs_feed_newest")
    return errors


def _load_jsonl(path: Path) -> list[dict]:
    rows = []
    for line in path.read_text().splitlines():
        if not line.strip():
            continue
        rows.append(json.loads(line))
    return rows


def _trace_errors(report: dict) -> list[str]:
    errors: list[str] = []
    gates = report.get("gates") or {}
    for column, needed in COLUMN_GATES.items():
        for name in needed:
            gate = gates.get(name) or {}
            if not gate.get("pass"):
                errors.append(f"{column} gate {name} is not passing")
    for name in SPEC_GATE_NAMES:
        gate = gates.get(name) or {}
        if not gate.get("pass"):
            errors.append(f"spec gate {name} is not passing")
    if not CSV_PATH.is_file() or not JSONL_PATH.is_file():
        errors.append("export files are missing")
        return errors
    try:
        expected_rows = build_rows(report)
        csv_text = CSV_PATH.read_text()
        parsed = list(csv.DictReader(io.StringIO(csv_text)))
        json_rows = _load_jsonl(JSONL_PATH)
    except (SpecError, json.JSONDecodeError, csv.Error, OSError) as exc:
        errors.append(f"export could not be read against evidence: {exc}")
        return errors
    if len(parsed) != len(expected_rows) or len(json_rows) != len(expected_rows):
        errors.append("export row count does not match scan.json")
        return errors
    for expected, csv_row, json_row in zip(expected_rows, parsed, json_rows):
        ident = expected["_install_id"]
        for column in CS_COLUMNS:
            try:
                got = _parse_csv_cs(column, _csv_shown(column, csv_row.get(column, "")))
            except SpecError as exc:
                errors.append(f"{ident} {column} csv {exc}")
                continue
            if got != expected[column]:
                errors.append(f"{ident} {column} csv does not match evidence")
            if json_row.get(column) != expected[column]:
                errors.append(f"{ident} {column} jsonl does not match evidence")
        if csv_row.get("Risk level", None) not in {""}:
            errors.append(f"{ident} Risk level is not empty")
        if _csv_shown("Agent name", csv_row.get("Agent name", "")) != expected["Name"] or json_row.get("Name") != expected["Name"]:
            errors.append(f"{ident} Agent name does not match scan.json")
        if _csv_shown("Version", csv_row.get("Version", "")) != expected["Version"]:
            errors.append(f"{ident} Version does not match scan.json")
        meta = expected["RawAgentInfo"]["localAgentMetadata"]
        if _csv_shown("Device name", csv_row.get("Device name", "")) != meta["deviceName"]:
            errors.append(f"{ident} Device name does not match scan.json")
        if _csv_shown("Device ID", csv_row.get("Device ID", "")) != expected["_device_id"]:
            errors.append(f"{ident} Device ID does not match the recorded device fields")
        if _csv_shown("First seen", csv_row.get("First seen", "")) != expected["Timestamp"]:
            errors.append(f"{ident} First seen does not match the recorded observation time")
        if json_row.get("Timestamp") != expected["Timestamp"]:
            errors.append(f"{ident} Timestamp does not match the recorded observation time")
        if json_row.get("LastUpdatedDateTime") != expected["LastUpdatedDateTime"]:
            errors.append(f"{ident} LastUpdatedDateTime does not match the recorded observation time")
        if json_row.get("PublishedStatus") != expected["PublishedStatus"]:
            errors.append(f"{ident} PublishedStatus does not match the local-agent null")
        if csv_row.get("Local MCPs") != str(len(meta["localMcps"])):
            errors.append(f"{ident} Local MCPs does not match scan.json")
        if csv_row.get("MCP servers") != str(len(expected["McpServers"])):
            errors.append(f"{ident} MCP servers does not match scan.json")
        if json_row.get("AgentId") != expected["AgentId"]:
            errors.append(f"{ident} AgentId does not match the install id")
    return errors


def _csv_type_errors(text: str) -> list[str]:
    """Fail empty strings where Hark's G1.types requires a datetime or a string."""
    errors: list[str] = []
    try:
        parsed = list(csv.DictReader(io.StringIO(text)))
    except csv.Error as exc:
        return [f"csv {exc}"]
    for row in parsed:
        device = row.get("Device name") or "?"
        if row.get("Agent name") != "OpenClaw":
            errors.append(f"{device} Agent name")
        if not row.get("Device ID"):
            errors.append(f"{device} Device ID empty")
        if row.get("Risk level") != "":
            errors.append(f"{device} Risk level")
        for column in ("MCP servers", "Local MCPs"):
            if not INT_RE.fullmatch(row.get(column) or ""):
                errors.append(f"{device} {column}")
        if not ISO_RE.fullmatch(row.get("First seen") or ""):
            errors.append(f"{device} First seen")
    return errors


def export_gates(report: dict) -> dict:
    header_gate: dict = {"pass": False, "error": ""}
    try:
        expected_header = ",".join(column_names())
        if not CSV_PATH.is_file():
            header_gate["error"] = "missing evidence/export/defender_local_agents.csv"
        else:
            text = CSV_PATH.read_text()
            actual = text.splitlines()[0] if text else ""
            header_gate["actual"] = actual
            header_gate["expected"] = expected_header
            problems: list[str] = []
            if actual != expected_header:
                problems.append("header does not match the spec list")
            problems.extend(_csv_type_errors(text))
            header_gate["pass"] = not problems
            header_gate["error"] = "; ".join(problems)
    except SpecError as exc:
        header_gate["error"] = str(exc)

    schema_gate: dict = {"pass": False, "rows": 0, "errors": []}
    try:
        scan_count = len(_load_json(EVIDENCE / "scan.json").get("installs") or [])
        if not JSONL_PATH.is_file():
            schema_gate["errors"] = ["missing evidence/export/agentsinfo_local.jsonl"]
        else:
            json_rows = _load_jsonl(JSONL_PATH)
            schema_gate["rows"] = len(json_rows)
            schema_gate["errors"] = _schema_errors(json_rows, scan_count)
            schema_gate["pass"] = not schema_gate["errors"]
    except (SpecError, json.JSONDecodeError, OSError) as exc:
        schema_gate["errors"] = [str(exc)]

    trace_gate: dict = {
        "pass": False,
        "untraceable": [],
        "mapped_gates": {column: list(names) for column, names in COLUMN_GATES.items()},
    }
    try:
        trace_gate["untraceable"] = _trace_errors(report)
        trace_gate["pass"] = not trace_gate["untraceable"]
    except SpecError as exc:
        trace_gate["untraceable"] = [str(exc)]

    readme_gate: dict = {"pass": False, "missing": [], "checked": 0}
    try:
        required = verbatim_flag_lines()
        readme = (ROOT / "README.md").read_text() if (ROOT / "README.md").is_file() else ""
        missing = [line for line in required if line not in readme]
        readme_gate["checked"] = len(required)
        readme_gate["missing"] = missing
        readme_gate["pass"] = not missing and len(required) > 0
    except (SpecError, OSError) as exc:
        readme_gate["missing"] = [str(exc)]

    return {
        "export_header": header_gate,
        "export_traceable": trace_gate,
        "export_jsonl_schema": schema_gate,
        "readme_unprovens": readme_gate,
        "csv_escape": csv_escape_gate(),
    }


def csv_escape_gate() -> dict:
    """Score the exporter against the frozen vectors, the planted row, and the lab CSV."""
    vector_path = ROOT / "inputs/clawscore-feed-csv-2026-10-17/csv/formula-escape-vectors.tsv"
    expected_planted = ROOT / "inputs/clawscore-feed-csv-2026-10-17/csv/planted-row.expected.csv"
    oracle_path = ROOT / "inputs/clawscore-feed-csv-2026-10-17/csv/escape_reference.py"
    oracle: dict = {}
    exec(oracle_path.read_text().split("if __name__")[0], oracle)
    rows = list(
        csv.DictReader(vector_path.open(encoding="utf-8"), delimiter="\t", quoting=csv.QUOTE_NONE)
    )
    failed = []
    for row in rows:
        raw = json.loads(row["input_json"])
        escaped = escape_cell(raw)
        field = oracle["csv_field"](escaped)
        if not (
            escaped == json.loads(row["expected_cell_json"])
            and field == json.loads(row["expected_csv_field_json"])
            and unescape_cell(escaped) == raw
        ):
            failed.append(row["id"])
    planted_ok = False
    planted_error = ""
    try:
        produced = write_planted_row()
        planted_ok = produced.read_bytes() == expected_planted.read_bytes()
    except (OSError, SpecError, json.JSONDecodeError, csv.Error) as exc:
        planted_error = str(exc)
    bare = []
    round_trip = []
    text_cells = 0
    scan_mismatch = []
    if CSV_PATH.is_file():
        parsed = list(csv.DictReader(CSV_PATH.open(encoding="utf-8", newline="")))
        scan = {item["id"]: item for item in _load_json(EVIDENCE / "scan.json").get("installs") or []}
        for record in parsed:
            device = record.get("Device name") or ""
            install = scan.get(device) or {}
            for column, cell in record.items():
                if column in INT_COLUMNS or cell == "":
                    continue
                text_cells += 1
                if cell[:1] in oracle["DANGER"]:
                    bare.append((device, column))
                if escape_cell(unescape_cell(cell)) != cell:
                    round_trip.append((device, column))
            if install:
                for column, wanted in _scan_text_values(install).items():
                    if column in INT_COLUMNS:
                        continue
                    if unescape_cell(record.get(column, "")) != wanted:
                        scan_mismatch.append((device, column))
    passed = not failed and planted_ok and not bare and not round_trip and not scan_mismatch and text_cells > 0
    return {
        "pass": passed,
        "vectors_ok": len(rows) - len(failed),
        "vectors_total": len(rows),
        "vector_failures": failed,
        "planted_byte_equal": planted_ok,
        "planted_error": planted_error,
        "text_cells": text_cells,
        "bare_danger": bare[:8],
        "round_trip_failures": round_trip[:8],
        "scan_round_trip_failures": scan_mismatch[:8],
    }


def _scan_text_values(install: dict) -> dict[str, str]:
    """CSV text cells copied from one scan install, before formula escaping."""
    agent = install.get("agent365") or {}
    verdict = str(install.get("verdict") or "")
    version = str(install.get("version") or "") if verdict == "exact" else ""
    return {
        "Agent name": str(agent.get("name") or ""),
        "Version": version,
        "Device name": str(agent.get("device") or install.get("id") or ""),
        "cs_build_verdict": verdict,
        "cs_candidates": "|".join(str(item) for item in (install.get("candidates") or [])),
        "cs_ghsa_ids": "|".join(str(item) for item in (install.get("ghsa_ids") or [])),
        "cs_cve_ids": "|".join(str(item) for item in (install.get("cves") or [])),
        "cs_readable_secret_classes": "|".join(str(item) for item in (install.get("credentials") or [])),
        "cs_feed_newest": str(install.get("feed_newest") or ""),
    }


def main() -> int:
    try:
        write_exports()
    except SpecError as exc:
        print(str(exc), flush=True)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
