"""OSV 1.6 export of advisories absent from the pinned scanner DBs.

The ID list is inputs/rea-scanner-feed-gap-evidence/gap-ids.txt.
Ranges come from evidence/landscape/ghsa-all.json. This module does not open
the scanner databases.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

from clawscore_fleet.cves import _first_patched, _openclaw_ranges, in_range, is_withdrawn
from clawscore_fleet.versions import FEED_NEWEST, ROOT, hark_key, load_published, parse_comparators, stable_releases

GAP_PATH = ROOT / "inputs" / "rea-scanner-feed-gap-evidence" / "gap-ids.txt"
GHSA_PATH = ROOT / "evidence" / "landscape" / "ghsa-all.json"
SCHEMA_PATH = ROOT / "inputs" / "rea-brief-scanner-feed-gap" / "pins" / "osv-schema-1.6.0.json"
DEFAULT_OUT = ROOT / "evidence" / "scanner-feed-gap" / "osv"
SOURCE_SHA256 = "27b020df70c9896d7b94280ad0646dc69ef4d27e504d81bc6719dedcb6446034"


class ExportError(SystemExit):
    pass


def _events(rng: str) -> list[dict] | None:
    comps = parse_comparators(rng)
    ops = [op for op, _bound in comps]
    if ops == ["<"]:
        return [{"introduced": "0"}, {"fixed": comps[0][1]}]
    if ops == ["<="]:
        return [{"introduced": "0"}, {"last_affected": comps[0][1]}]
    if ops == [">=", "<"]:
        return [{"introduced": comps[0][1]}, {"fixed": comps[1][1]}]
    if ops == [">", "<"]:
        return None
    raise ExportError(f"unmapped range {rng!r}")


def _affected(advisory: dict, stable: list[str]) -> dict:
    ranges = _openclaw_ranges(advisory)
    if len(ranges) != 1:
        raise ExportError(f"{advisory.get('ghsa_id')} has {len(ranges)} openclaw ranges")
    rng = ranges[0]
    specific = {"vulnerable_version_range": rng}
    patched = _first_patched(advisory)
    if isinstance(patched, str) and patched:
        specific["first_patched_version"] = patched
    body: dict = {
        "database_specific": specific,
        "package": {"ecosystem": "npm", "name": "openclaw"},
    }
    events = _events(rng)
    if events is None:
        matched = [version for version in stable if in_range(version, rng)]
        matched.sort(key=lambda item: hark_key(item) or ())
        body["versions"] = matched
    else:
        body["ranges"] = [
            {
                "database_specific": {"vulnerable_version_range": rng},
                "events": events,
                "type": "ECOSYSTEM",
            }
        ]
    return body


def _document(advisory: dict, stable: list[str]) -> dict:
    if is_withdrawn(advisory):
        raise ExportError(f"withdrawn advisory {advisory.get('ghsa_id')} is excluded")
    doc: dict = {
        "affected": [_affected(advisory, stable)],
        "database_specific": {
            "clawscore_feed_newest": FEED_NEWEST,
            "source_sha256": SOURCE_SHA256,
        },
        "id": advisory["ghsa_id"],
        "modified": advisory["updated_at"],
        "published": advisory["published_at"],
        "schema_version": "1.6.0",
    }
    summary = advisory.get("summary")
    if isinstance(summary, str) and summary:
        doc["summary"] = summary
    details = advisory.get("description")
    if isinstance(details, str) and details:
        doc["details"] = details
    cve_id = advisory.get("cve_id")
    if isinstance(cve_id, str) and cve_id:
        doc["aliases"] = [cve_id]
    vector = ((advisory.get("cvss") or {}).get("vector_string")) if isinstance(advisory.get("cvss"), dict) else None
    if isinstance(vector, str) and vector.startswith("CVSS:3"):
        doc["severity"] = [{"score": vector, "type": "CVSS_V3"}]
    refs = []
    for url in advisory.get("references") or []:
        if not isinstance(url, str) or not url.startswith(("https://", "http://")):
            raise ExportError(f"reference is not an http(s) URL on {advisory.get('ghsa_id')}")
        refs.append({"type": "ADVISORY", "url": url})
    if refs:
        doc["references"] = refs
    return doc


def _encode(doc: dict) -> str:
    return json.dumps(doc, ensure_ascii=False, indent=2, sort_keys=True) + "\n"


def load_gap(path: Path | None = None) -> list[str]:
    text = (path or GAP_PATH).read_text().splitlines()
    return [line.strip() for line in text if line.strip()]


def write_export(out_dir: Path | None = None, gap_path: Path | None = None) -> list[Path]:
    ghsa_hash = hashlib.sha256(GHSA_PATH.read_bytes()).hexdigest()
    if ghsa_hash != SOURCE_SHA256:
        raise ExportError("ghsa-all.json sha256 does not match the pinned source")
    schema_hash = hashlib.sha256(SCHEMA_PATH.read_bytes()).hexdigest()
    if schema_hash != "b30f59611f61a5c233dc5666379b683eeca6bb42e8c5acba172415d445f4f86e":
        raise ExportError("pinned OSV schema sha256 changed")
    by_id = {item["ghsa_id"]: item for item in json.loads(GHSA_PATH.read_text())}
    stable = stable_releases(load_published())
    out = out_dir or DEFAULT_OUT
    out.mkdir(parents=True, exist_ok=True)
    written = []
    for ghsa_id in load_gap(gap_path):
        advisory = by_id.get(ghsa_id)
        if advisory is None:
            raise ExportError(f"gap id {ghsa_id} is not in ghsa-all.json")
        text = _encode(_document(advisory, stable))
        path = out / f"{ghsa_id}.json"
        path.write_text(text)
        written.append(path)
    lines = []
    for path in sorted(written, key=lambda item: item.name):
        lines.append(f"{hashlib.sha256(path.read_bytes()).hexdigest()}  {path.name}")
    (out / "SHA256SUMS").write_text("\n".join(lines) + "\n")
    return written


def validate_directory(out_dir: Path | None = None) -> None:
    import jsonschema

    schema = json.loads(SCHEMA_PATH.read_text())
    validator = jsonschema.Draft202012Validator(schema, format_checker=jsonschema.Draft202012Validator.FORMAT_CHECKER)
    out = out_dir or DEFAULT_OUT
    files = sorted(out.glob("GHSA-*.json"))
    if not files:
        raise ExportError("no OSV files to validate")
    for path in files:
        errors = list(validator.iter_errors(json.loads(path.read_text())))
        if errors:
            raise ExportError(f"{path.name} {errors[0].message}")
