"""Trivy bbolt extraction for npm openclaw. Rules are BRIEF.md.

Ecosystem is the bucket-name prefix before '::'. Only prefix casefold 'npm' is npm.
Package name must casefold to openclaw.
Advisory IDs on a record are the leaf key and each VendorIDs string. ClawScore's
ids are GHSA strings; this DB stores many of them in VendorIDs under a CVE key.
Hold decision is Form A on each VulnerableVersions string (parse_comparators +
in_range). A record is held for V when any of those strings includes V.
PatchedVersions is not a second constraint: VulnerableVersions is already Form A.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(ROOT))

from bbolt import BUCKET_LEAF, BoltDB
from clawscore_fleet.cves import in_range
from clawscore_fleet.versions import RangeSyntaxError, parse_comparators

VERSIONS = ("2026.6.10", "2026.4.22")
TRIVY_DB = HERE / "frozen" / "trivy" / "trivy.db"


def label(value: str) -> str:
    text = value.casefold()
    found = []
    if "nvd" in text:
        found.append("NVD")
    if "ghsa" in text or "github" in text:
        found.append("GHSA")
    if "osv" in text:
        found.append("OSV")
    return "+".join(found) if found else "UNCLASSIFIED"


def _form_a(text: str) -> bool:
    try:
        parse_comparators(text)
    except RangeSyntaxError:
        return False
    return True


def load(db_path: Path | None = None) -> dict:
    db = BoltDB(str(db_path or TRIVY_DB))
    try:
        return _load(db)
    finally:
        db.close()


def _load(db: BoltDB) -> dict:
    sources = []
    npm_buckets = []
    for key, _value, flags in db.root_entries():
        if not flags & BUCKET_LEAF:
            continue
        name = key.decode("utf-8", "replace")
        prefix, sep, _rest = name.partition("::")
        if sep and prefix.casefold() == "npm":
            npm_buckets.append(name)
    for key, value, flags in db.bucket(b"data-source"):
        if flags & BUCKET_LEAF:
            continue
        name = key.decode("utf-8", "replace")
        if "npm" not in name.casefold():
            continue
        try:
            meta = json.loads(value.decode("utf-8"))
        except json.JSONDecodeError:
            meta = {}
        sources.append(("data-source-key", name, label(name), "npm-key"))
        for field in ("ID", "Name", "URL"):
            raw = meta.get(field)
            if isinstance(raw, str) and raw:
                sources.append((f"data-source-{field}", raw, label(raw), name))

    held: dict[str, dict[str, dict]] = {version: {} for version in VERSIONS}
    present: dict[str, dict] = {}
    unresolved = []
    for bucket_name in sorted(npm_buckets):
        bucket_key = bucket_name.encode()
        for pkg_key, pkg_value, pkg_flags in db.bucket(bucket_key):
            pkg_name = pkg_key.decode("utf-8", "replace")
            if pkg_name.casefold() != "openclaw":
                continue
            sources.append(("openclaw-bucket", bucket_name, label(bucket_name), pkg_name))
            if not pkg_flags & BUCKET_LEAF:
                unresolved.append((pkg_name, bucket_name, "package entry is not a bucket"))
                continue
            for adv_key, adv_value, adv_flags in db.bucket(bucket_key, pkg_key):
                adv_id = adv_key.decode("utf-8", "replace")
                if adv_flags & BUCKET_LEAF:
                    unresolved.append((adv_id, bucket_name, "nested bucket under package"))
                    continue
                try:
                    record = json.loads(adv_value.decode("utf-8"))
                except json.JSONDecodeError:
                    unresolved.append((adv_id, bucket_name, "value is not JSON"))
                    continue
                _consume(record, adv_id, bucket_name, held, present, unresolved)
    return {"sources": sources, "held": held, "present": present, "unresolved": unresolved, "npm_buckets": npm_buckets}


def _consume(record: dict, adv_id: str, bucket_name: str, held, present, unresolved) -> None:
    versions = record.get("VulnerableVersions")
    vendor = record.get("VendorIDs") or []
    ids = [adv_id]
    if isinstance(vendor, list):
        for item in vendor:
            if isinstance(item, str) and item and item not in ids:
                ids.append(item)
    else:
        unresolved.append((adv_id, bucket_name, "VendorIDs is not a list"))
        return
    if not isinstance(versions, list) or not versions or not all(isinstance(item, str) for item in versions):
        for item_id in ids:
            unresolved.append((item_id, bucket_name, "VulnerableVersions is not a list of strings"))
        return
    bad = [item for item in versions if not _form_a(item)]
    good = [item for item in versions if _form_a(item)]
    constraint = " | ".join(versions)
    if not good:
        for item_id in ids:
            unresolved.append((item_id, bucket_name, f"unparsed {bad!r}"))
        return
    for item_id in ids:
        present[item_id] = {"source": bucket_name, "constraint": constraint}
        for version in VERSIONS:
            if any(in_range(version, item) for item in good):
                slot = held[version].setdefault(
                    item_id,
                    {"source": bucket_name, "status": "", "constraint": constraint},
                )
                if bucket_name not in slot["source"].split(" | "):
                    slot["source"] = " | ".join(sorted(set(slot["source"].split(" | ")) | {bucket_name}))


def render_sources(payload: dict) -> str:
    lines = ["source_field\tsource_value\tlabel\tscope"]
    rows = sorted(set(payload["sources"]))
    for field, value, lab, scope in rows:
        lines.append(f"{field}\t{value}\t{lab}\t{scope}")
    return "\n".join(lines) + "\n"


def render_held(payload: dict, version: str) -> str:
    lines = ["advisory_id\tversion\tsource\tstatus\tconstraint"]
    for adv_id in sorted(payload["held"][version]):
        row = payload["held"][version][adv_id]
        lines.append(f"{adv_id}\t{version}\t{row['source']}\t{row['status']}\t{row['constraint']}")
    return "\n".join(lines) + "\n"


def render_unresolved(payload: dict) -> str:
    lines = ["advisory_id\tsource\treason"]
    rows = sorted(set(payload["unresolved"]))
    for adv_id, source, reason in rows:
        lines.append(f"{adv_id}\t{source}\t{reason}")
    return "\n".join(lines) + "\n"


def held_ids(payload: dict, version: str) -> set[str]:
    return set(payload["held"][version])
