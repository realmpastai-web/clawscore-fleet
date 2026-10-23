"""Advisory mapping generated from evidence/landscape/ghsa-all.json."""

from __future__ import annotations

import difflib
import json
import re
from functools import lru_cache
from pathlib import Path

from clawscore_fleet.pkgmatch import is_openclaw_npm
from clawscore_fleet.versions import (
    FEED_NEWEST,
    LANDSCAPE,
    NO_ADVISORY_WORDING,
    ROOT,
    hark_key,
    load_published,
    parse_comparators,
    stable_releases,
)

EVIDENCE = ROOT / "evidence"
_OPS = {
    "<": lambda left, right: left < right,
    "<=": lambda left, right: left <= right,
    ">": lambda left, right: left > right,
    ">=": lambda left, right: left >= right,
    "=": lambda left, right: left == right,
}


def in_range(version: str, rng: str) -> bool:
    """AND of every comparator. A range the grammar cannot consume raises."""
    left = hark_key(version)
    if left is None:
        return False
    for operator, bound in parse_comparators(rng):
        right = hark_key(bound)
        if not _OPS[operator](left, right):
            return False
    return True


def _load_advisories() -> list[dict]:
    payload = json.loads((LANDSCAPE / "ghsa-all.json").read_text())
    if not isinstance(payload, list):
        raise SystemExit("ghsa-all.json is not a list")
    return payload


def _openclaw_ranges(advisory: dict) -> list[str]:
    ranges = []
    ghsa_id = advisory.get("ghsa_id")
    for entry in advisory.get("vulnerabilities") or []:
        package = entry.get("package") or {}
        if not is_openclaw_npm(package, ghsa_id):
            continue
        rng = entry.get("vulnerable_version_range")
        if rng:
            ranges.append(str(rng))
    return ranges


def is_withdrawn(advisory: dict) -> bool:
    """True when withdrawn_at is set. Those rows are listed, not counted."""
    return advisory.get("withdrawn_at") is not None


def _covers(advisory: dict, version: str) -> bool:
    return any(in_range(version, rng) for rng in _openclaw_ranges(advisory))


def affecting_advisories(advisories: list[dict], version: str) -> list[dict]:
    """Openclaw ranges that cover version, excluding a non-null withdrawn_at."""
    return [
        advisory
        for advisory in advisories
        if not is_withdrawn(advisory) and _covers(advisory, version)
    ]


def withdrawn_covering(advisories: list[dict], version: str) -> list[dict]:
    """Rows that cover version and are withdrawn (not counted)."""
    return [
        advisory
        for advisory in advisories
        if is_withdrawn(advisory) and _covers(advisory, version)
    ]


@lru_cache(maxsize=1)
def build_index() -> dict:
    advisories = _load_advisories()
    published = load_published()
    stable = stable_releases(published)
    per_version: dict[str, list[dict]] = {version: [] for version in stable}
    withdrawn_by_version: dict[str, list[dict]] = {version: [] for version in stable}
    records = []
    for advisory in advisories:
        ranges = _openclaw_ranges(advisory)
        withdrawn = is_withdrawn(advisory)
        matched = []
        if ranges:
            for version in stable:
                if any(in_range(version, rng) for rng in ranges):
                    matched.append(version)
                    if withdrawn:
                        withdrawn_by_version[version].append(advisory)
                    else:
                        per_version[version].append(advisory)
        records.append(
            {
                "ghsa_id": advisory.get("ghsa_id"),
                "cve_id": advisory.get("cve_id"),
                "severity": advisory.get("severity"),
                "ranges": ranges,
                "first_patched_version": _first_patched(advisory),
                "withdrawn": withdrawn,
                "versions": [] if withdrawn else matched,
            }
        )
    records.sort(key=lambda item: item["ghsa_id"] or "")
    return {
        "advisories": advisories,
        "records": records,
        "per_version": per_version,
        "withdrawn_by_version": withdrawn_by_version,
        "stable": stable,
        "published": published,
    }


def _first_patched(advisory: dict) -> str | None:
    ghsa_id = advisory.get("ghsa_id")
    for entry in advisory.get("vulnerabilities") or []:
        package = entry.get("package") or {}
        if not is_openclaw_npm(package, ghsa_id):
            continue
        patched = entry.get("first_patched_version")
        if patched:
            return str(patched)
    return None


def _severity_counts(advisories: list[dict]) -> dict[str, int]:
    counts = {"critical": 0, "high": 0, "medium": 0, "low": 0}
    for advisory in advisories:
        severity = str(advisory.get("severity") or "")
        if severity in counts:
            counts[severity] += 1
    return counts


def version_counts(version: str) -> dict[str, int]:
    index = build_index()
    advisories = index["per_version"].get(version) or []
    counts = _severity_counts(advisories)
    counts["advisories"] = len(advisories)
    return counts


def has_critical_or_high(version: str) -> bool:
    counts = version_counts(version)
    return counts["critical"] + counts["high"] > 0


def _rows_for_version(index: dict, version: str) -> tuple[list[dict], list[dict]]:
    """Indexed rows for a stable release. Any other version is scored from the feed."""
    if version in index["per_version"]:
        return index["per_version"][version], index["withdrawn_by_version"][version]
    covered: list[dict] = []
    withdrawn: list[dict] = []
    for advisory in index["advisories"]:
        if not _covers(advisory, version):
            continue
        if is_withdrawn(advisory):
            withdrawn.append(advisory)
        else:
            covered.append(advisory)
    return covered, withdrawn


def report_for_versions(versions: list[str]) -> dict:
    """Union of advisories across versions. An empty union uses the feed wording."""
    index = build_index()
    chosen: dict[str, dict] = {}
    withdrawn_ids = []
    seen_withdrawn = set()
    for version in versions:
        covered, withdrawn = _rows_for_version(index, version)
        for advisory in covered:
            ghsa_id = advisory.get("ghsa_id")
            if ghsa_id and ghsa_id not in chosen:
                chosen[ghsa_id] = advisory
        for advisory in withdrawn:
            ghsa_id = advisory.get("ghsa_id")
            if ghsa_id and ghsa_id not in seen_withdrawn:
                seen_withdrawn.add(ghsa_id)
                withdrawn_ids.append(ghsa_id)
    ordered = [chosen[key] for key in sorted(chosen)]
    counts = _severity_counts(ordered)
    cve_ids = sorted({item.get("cve_id") for item in ordered if item.get("cve_id")})
    note = ""
    if not ordered:
        note = NO_ADVISORY_WORDING
    return {
        "ghsa_ids": [item.get("ghsa_id") for item in ordered],
        "cve_ids": cve_ids,
        "advisories": len(ordered),
        "critical": counts["critical"],
        "high": counts["high"],
        "medium": counts["medium"],
        "low": counts["low"],
        "withdrawn_not_counted": sorted(withdrawn_ids),
        "note": note,
        "vulnerable": counts["critical"] + counts["high"] > 0,
        "feed_newest": FEED_NEWEST,
    }


def version_vuln_rows() -> list:
    """Per-stable-release rows in the version-vulns.json shape."""
    index = build_index()
    published = index["published"]
    rows = []
    for version in index["stable"]:
        advisories = index["per_version"][version]
        counts = _severity_counts(advisories)
        match = re.search(r"\d{4}-\d\d-\d\d", published[version])
        if not match:
            raise SystemExit(f"no publish date for {version}")
        rows.append(
            [
                version,
                match.group(0),
                len(advisories),
                {name: counts[name] for name in ("critical", "high", "medium", "low")},
            ]
        )
    return rows


def count_lines(stable: list[str] | None = None) -> list[str]:
    index = build_index()
    order = stable if stable is not None else index["stable"]
    lines = []
    for version in order:
        counts = _severity_counts(index["per_version"][version])
        total = len(index["per_version"][version])
        lines.append(
            f"{version} {total} {counts['critical']} {counts['high']} {counts['medium']} {counts['low']}"
        )
    return lines


def landscape_count_lines() -> list[str]:
    payload = json.loads((LANDSCAPE / "version-vulns.json").read_text())
    rows = []
    for version, _date, total, severity in payload:
        rows.append(
            (
                version,
                f"{version} {total} {severity['critical']} {severity['high']} {severity['medium']} {severity['low']}",
            )
        )
    rows.sort(key=lambda item: hark_key(item[0]) or (0,))
    return [line for _version, line in rows]


def diff_text() -> str:
    generated = count_lines()
    expected = landscape_count_lines()
    delta = list(
        difflib.unified_diff(
            expected,
            generated,
            fromfile="evidence/landscape/version-vulns.json",
            tofile="generated",
            lineterm="",
        )
    )
    if not delta:
        return ""
    return "\n".join(delta) + "\n"


def min_clearing_version() -> str | None:
    """Earliest stable release at which this and every later release have no critical or high advisory."""
    index = build_index()
    stable = index["stable"]
    for start, version in enumerate(stable):
        if all(
            _severity_counts(index["per_version"][later])["critical"] == 0
            and _severity_counts(index["per_version"][later])["high"] == 0
            for later in stable[start:]
        ):
            return version
    return None


def write_outputs() -> dict:
    index = build_index()
    published = index["published"]
    version_rows = {}
    for version in index["stable"]:
        advisories = index["per_version"][version]
        counts = _severity_counts(advisories)
        version_rows[version] = {
            "published": published.get(version, ""),
            "advisories": len(advisories),
            "critical": counts["critical"],
            "high": counts["high"],
            "medium": counts["medium"],
            "low": counts["low"],
            "ghsa_ids": sorted(item.get("ghsa_id") for item in advisories),
            "withdrawn_not_counted": sorted(
                item.get("ghsa_id") for item in index["withdrawn_by_version"][version]
            ),
            "note": NO_ADVISORY_WORDING if not advisories else "",
        }
    advisory_rows = {}
    for record in index["records"]:
        advisory_rows[record["ghsa_id"]] = {
            "cve_id": record["cve_id"],
            "severity": record["severity"],
            "ranges": record["ranges"],
            "first_patched_version": record["first_patched_version"],
            "versions": record["versions"],
        }
    cve_map = {
        "feed_newest": FEED_NEWEST,
        "advisory_count": len(index["advisories"]),
        "with_cve_id": sum(1 for item in index["advisories"] if item.get("cve_id")),
        "advisories": advisory_rows,
        "versions": version_rows,
    }
    clearing = min_clearing_version()
    focus = version_rows.get("2026.4.22") or {}
    fixorder = {
        "feed_newest": FEED_NEWEST,
        "cited": "evidence/landscape/CLAIMS.md",
        "clears": "critical and high",
        "min_clearing_version": clearing,
        "focus_version": "2026.4.22",
        "focus_advisories": focus.get("advisories"),
        "focus_critical": focus.get("critical"),
        "focus_high": focus.get("high"),
        "focus_withdrawn_not_counted": len(focus.get("withdrawn_not_counted") or []),
        "withdrawn_not_counted_label": "withdrawn (not counted)",
        "versions": [
            {
                "version": version,
                "advisories": version_rows[version]["advisories"],
                "critical": version_rows[version]["critical"],
                "high": version_rows[version]["high"],
                "medium": version_rows[version]["medium"],
                "low": version_rows[version]["low"],
                "clears_critical_and_high": version_rows[version]["critical"] == 0
                and version_rows[version]["high"] == 0,
            }
            for version in index["stable"]
        ],
    }
    EVIDENCE.mkdir(parents=True, exist_ok=True)
    (EVIDENCE / "cve-map.json").write_text(json.dumps(cve_map, indent=2, sort_keys=True) + "\n")
    diff = diff_text()
    (EVIDENCE / "cve-map-diff.txt").write_text(diff)
    (EVIDENCE / "fixorder.json").write_text(json.dumps(fixorder, indent=2, sort_keys=True) + "\n")
    return {"diff": diff, "fixorder": fixorder, "cve_map": cve_map}


def main() -> int:
    result = write_outputs()
    diff = result["diff"]
    focus = result["fixorder"]
    print(f"advisories {result['cve_map']['advisory_count']}", flush=True)
    print(f"with_cve_id {result['cve_map']['with_cve_id']}", flush=True)
    print(f"min_clearing_version {focus['min_clearing_version']}", flush=True)
    print(
        "2026.4.22 "
        f"{focus['focus_advisories']} critical={focus['focus_critical']} high={focus['focus_high']}",
        flush=True,
    )
    print(f"diff_lines {0 if not diff else len(diff.splitlines())}", flush=True)
    return 0 if not diff else 1


if __name__ == "__main__":
    raise SystemExit(main())
