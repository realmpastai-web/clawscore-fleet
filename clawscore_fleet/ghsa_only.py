"""GHSA-only OpenClaw advisories for one installed version.

An advisory is GHSA-only when the OSV record has no CVE- alias and the
landscape row has cve_id null. `affected` means some openclaw
vulnerable_version_range in the landscape covers the version
(`cves.in_range`). `possibly_affected` means that range does not, but an
OSV SEMVER introduced/fixed/last_affected range does.

Ordering is `versions.hark_key`. A numeric suffix is a post-release:
2026.4.7 < 2026.4.7-1 < 2026.4.8. OSV SEMVER would treat 2026.4.7-1 as a
prerelease of 2026.4.7 and sort it first. Range checks here follow
hark_key, so 2026.4.7-1 stays inside an OSV window fixed at 2026.4.8 and
outside a GitHub range of `<= 2026.4.2`.

The same version window also contains advisories this module does not
fold into ghsa_ids. `follow_up_text` records that count. It does not
change the report.
"""

from __future__ import annotations

import hashlib
import json
import re
from functools import lru_cache
from pathlib import Path

from clawscore_fleet.cves import in_range
from clawscore_fleet.pkgmatch import is_openclaw_npm
from clawscore_fleet.versions import ROOT, hark_key, parse_comparators

INPUTS = ROOT / "inputs" / "clawscore-ghsa-only"
OSV_PATH = INPUTS / "sources" / "osv" / "osv-query-openclaw-npm.json"
SNAPSHOT_PATH = INPUTS / "OSV_SNAPSHOT.json"
LANDSCAPE_PATH = ROOT / "evidence" / "landscape" / "ghsa-all.json"
TASK_PATH = INPUTS / "CURSOR_TASK_clawscore-ghsa-only.md"
DEFENDER_README = ROOT / "inputs" / "rea-defender-ghsa-only" / "README.md"
_PLAIN = re.compile(r"(\d+)\.(\d+)\.(\d+)")


def load_snapshot(osv_path: Path, snapshot_path: Path) -> tuple[dict, list]:
    """Load an OSV document. Refuse when its sha256 is not the pinned snapshot."""
    snap = json.loads(snapshot_path.read_text())
    digest = hashlib.sha256(osv_path.read_bytes()).hexdigest()
    pinned = snap.get("sha256")
    if digest != pinned:
        raise SystemExit(
            f"OSV snapshot sha256 mismatch: {osv_path} is {digest} "
            f"OSV_SNAPSHOT.json says {pinned}"
        )
    payload = json.loads(osv_path.read_text())
    if not isinstance(payload, list):
        raise SystemExit(f"OSV snapshot is not a list: {osv_path}")
    return snap, payload


def _cmp(left: str, right: str) -> int:
    lk = hark_key(left)
    rk = hark_key(right)
    if lk is None or rk is None:
        missing = left if lk is None else right
        raise SystemExit(f"unparseable version {missing}")
    if lk < rk:
        return -1
    if lk > rk:
        return 1
    return 0


def semver_events_cover(version: str, events: list) -> bool:
    """True when hark_key places version inside one introduced..end event pair.

    `fixed` is exclusive. `last_affected` is inclusive. An introduced value
    of `0` has no lower bound. 2026.4.7-1 is after 2026.4.7, so a range
    fixed at 2026.4.7 does not cover it.
    """
    lo = None
    for event in events:
        if not isinstance(event, dict):
            continue
        if "introduced" in event:
            lo = str(event["introduced"])
            continue
        if "fixed" in event:
            end, inclusive = str(event["fixed"]), False
        elif "last_affected" in event:
            end, inclusive = str(event["last_affected"]), True
        else:
            lo = None
            continue
        if lo is not None and _between(version, lo, end, inclusive):
            return True
        lo = None
    return lo is not None and (lo == "0" or _cmp(version, lo) >= 0)


def _between(version: str, lo: str, end: str, inclusive: bool) -> bool:
    if lo != "0" and _cmp(version, lo) < 0:
        return False
    order = _cmp(version, end)
    return order <= 0 if inclusive else order < 0


def _osv_semver_covers(advisory: dict, version: str) -> bool:
    for affected in advisory.get("affected") or []:
        package = (affected.get("package") or {}) if isinstance(affected, dict) else {}
        if not is_openclaw_npm(package, advisory.get("id")):
            continue
        for rng in affected.get("ranges") or []:
            if not isinstance(rng, dict) or rng.get("type") != "SEMVER":
                continue
            if semver_events_cover(version, rng.get("events") or []):
                return True
    return False


def _github_ranges(row: dict) -> list[str]:
    found = []
    for entry in row.get("vulnerabilities") or []:
        package = entry.get("package") or {}
        if not is_openclaw_npm(package, row.get("ghsa_id")):
            continue
        rng = entry.get("vulnerable_version_range")
        if rng:
            found.append(str(rng))
    return found


def _github_covers(row: dict | None, version: str) -> bool:
    if not row:
        return False
    return any(in_range(version, rng) for rng in _github_ranges(row))


def _is_nocve(advisory: dict, landscape: dict) -> bool:
    aliases = advisory.get("aliases") or []
    if any(str(alias).startswith("CVE-") for alias in aliases):
        return False
    row = landscape.get(advisory.get("id"))
    return bool(row) and row.get("cve_id") is None


def _rows(version: str, advisories: list, landscape: dict, nocve_only: bool) -> list[dict]:
    rows = []
    for advisory in advisories:
        if nocve_only and not _is_nocve(advisory, landscape):
            continue
        covered = _osv_semver_covers(advisory, version)
        if not covered:
            continue
        row = landscape.get(advisory.get("id"))
        if row is not None and row.get("withdrawn_at") is not None:
            continue
        status = "affected" if _github_covers(row, version) else "possibly_affected"
        rows.append({"id": advisory["id"], "status": status})
    rows.sort(key=lambda item: item["id"])
    return rows


@lru_cache(maxsize=1)
def _bundle() -> tuple[dict, list, dict]:
    snap, osv = load_snapshot(OSV_PATH, SNAPSHOT_PATH)
    payload = json.loads(LANDSCAPE_PATH.read_text())
    if not isinstance(payload, list):
        raise SystemExit(f"landscape is not a list: {LANDSCAPE_PATH}")
    landscape = {item.get("ghsa_id"): item for item in payload}
    return snap, osv, landscape


def snapshot_sha256() -> str:
    snap, _osv, _landscape = _bundle()
    return str(snap["sha256"])


def for_version(version: str) -> list[dict]:
    """Sorted `{id, status}` rows for one OpenClaw version."""
    _snap, osv, landscape = _bundle()
    return _rows(version, osv, landscape, True)


def rows_for_install(version: str | None, candidates: list[str] | None, verdict: str) -> list[dict]:
    """GHSA-only rows for one scan install.

    An exact verdict uses the identified version. A range unions the
    candidate versions and keeps `affected` when the candidates disagree.
    Unknown installs get an empty list. This does not change ghsa_ids.
    """
    if verdict == "unknown":
        return []
    versions = [version] if version else [item for item in (candidates or []) if item]
    rank = {"possibly_affected": 1, "affected": 2}
    merged: dict[str, dict] = {}
    for item in versions:
        for row in for_version(item):
            current = merged.get(row["id"])
            if current is None or rank[row["status"]] > rank[current["status"]]:
                merged[row["id"]] = {"id": row["id"], "status": row["status"]}
    return [merged[key] for key in sorted(merged)]


def _step_patch(version: str, delta: int) -> str:
    match = _PLAIN.fullmatch(version)
    if not match:
        raise SystemExit(f"cannot step patch of {version}")
    major, minor, patch = (int(part) for part in match.groups())
    patch += delta
    if patch < 0:
        raise SystemExit(f"patch step left {version} below 0")
    return f"{major}.{minor}.{patch}"


def _osv_fixed_versions(advisory: dict) -> list[str]:
    found = []
    for affected in advisory.get("affected") or []:
        package = (affected.get("package") or {}) if isinstance(affected, dict) else {}
        if not is_openclaw_npm(package, advisory.get("id")):
            continue
        for rng in affected.get("ranges") or []:
            if not isinstance(rng, dict) or rng.get("type") != "SEMVER":
                continue
            for event in rng.get("events") or []:
                if isinstance(event, dict) and "fixed" in event:
                    found.append(str(event["fixed"]))
    return found


def _window_for(advisory_id: str) -> tuple[str, str]:
    _snap, osv, landscape = _bundle()
    advisory = next(item for item in osv if item.get("id") == advisory_id)
    row = landscape.get(advisory_id)
    ranges = _github_ranges(row or {})
    fixed = _osv_fixed_versions(advisory)
    if len(ranges) != 1 or len(fixed) != 1:
        raise SystemExit(
            f"cannot derive a window for {advisory_id}: ranges={ranges} fixed={fixed}"
        )
    parsed = parse_comparators(ranges[0])
    if len(parsed) != 1 or parsed[0][0] != "<=":
        raise SystemExit(f"cannot derive a window for {advisory_id}: range {ranges[0]!r}")
    return _step_patch(parsed[0][1], 1), _step_patch(fixed[0], -1)


def gap_window() -> tuple[str, str]:
    """Patch window derived from fixture versions that are possibly_affected."""
    hosts = json.loads((INPUTS / "expected-ghsa-only.json").read_text())["fixture_hosts"]
    windows: dict[tuple[str, str], list[str]] = {}
    for host in hosts:
        version = host["version"]
        for row in for_version(version):
            if row["status"] != "possibly_affected":
                continue
            window = _window_for(row["id"])
            windows.setdefault(window, []).append(f"{version} {row['id']}")
    if len(windows) != 1:
        raise SystemExit("gap windows:\n" + json.dumps({str(key): value for key, value in windows.items()}, indent=2))
    return next(iter(windows))


def measured_readme_claim() -> str:
    snap, osv, landscape = _bundle()
    count = sum(1 for advisory in osv if _is_nocve(advisory, landscape))
    fetched = str(snap.get("fetched") or "")
    date = fetched.split()[0] if fetched else ""
    low, high = gap_window()
    return (
        "Lists the OpenClaw advisories that have no CVE id "
        f"({count} in the OSV snapshot of {date}) per install, marking the "
        f"{low} to {high} window as possibly affected where GitHub's range stops early."
    )


def frozen_task_claim() -> str:
    text = TASK_PATH.read_text()
    match = re.search(r"README claim, and only while the gate passes:\*\* \"([^\"]+)\"", text)
    if not match:
        raise SystemExit(f"frozen README claim not found in {TASK_PATH}")
    return match.group(1)


def defender_claim() -> str:
    """The one Defender sentence the frozen REA allows, copied from that file."""
    text = DEFENDER_README.read_text()
    match = re.search(r"\*\*README claim allowed:\*\* \"([^\"]+)\"", text)
    if not match:
        raise SystemExit(f"frozen Defender claim not found in {DEFENDER_README}")
    claim = match.group(1)
    lowered = claim.lower()
    if "container" in lowered or "agent 365" in lowered or "can't show non-cve" in lowered or "can’t show non-cve" in lowered:
        raise SystemExit(f"frozen Defender claim contains forbidden wording: {claim}")
    return claim


def _patches(start: str, end: str) -> list[str]:
    versions = []
    current = start
    while True:
        versions.append(current)
        if current == end:
            return versions
        current = _step_patch(current, 1)
        if hark_key(current) > hark_key(end):
            raise SystemExit(f"patch walk from {start} did not reach {end}")


def follow_up_text() -> str:
    """Record the CVE-window follow-up. Do not fold it into ghsa_ids."""
    _snap, osv, landscape = _bundle()
    low, high = gap_window()
    versions = _patches(low, high)
    nocve_ids = []
    cve_ids = []
    for advisory in osv:
        outside = False
        for version in versions:
            if _osv_semver_covers(advisory, version) and not _github_covers(landscape.get(advisory.get("id")), version):
                outside = True
                break
        if not outside:
            continue
        if _is_nocve(advisory, landscape):
            nocve_ids.append(advisory["id"])
        else:
            cve_ids.append(advisory["id"])
    return (
        "Follow-up, not changed here. The task says the same gap window also exists for "
        "advisories that have CVEs: 13 in the landscape, 10 of them no-CVE. "
        f"Measured on the pinned OSV snapshot against evidence/landscape/ghsa-all.json for patches "
        f"{low} through {high}: {len(nocve_ids) + len(cve_ids)} advisories are inside an OSV SEMVER "
        f"range and outside every landscape vulnerable_version_range "
        f"({len(nocve_ids)} with no CVE alias and cve_id null, {len(cve_ids)} otherwise). "
        "possibly_affected is not folded into ghsa_ids or the counts."
    )
