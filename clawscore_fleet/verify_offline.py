"""Offline gates: landscape, matrix, fingerprints, CVE map, semver, wording."""

from __future__ import annotations

import csv
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

from clawscore_fleet.build_fingerprints import _dirlist, _lookup_hash
from clawscore_fleet.idle_linux import evaluate as evaluate_idle_linux
from clawscore_fleet.idle_linux import write_scan_artifacts
from clawscore_fleet.listings_store import is_listing_blob, listings_present, load_listings
from clawscore_fleet.cves import diff_text, version_counts, write_outputs
from clawscore_fleet.fingerprint import collision_groups, identify, load_db
from clawscore_fleet.gates_v023 import extra_offline_gates
from clawscore_fleet.semver_check import run as semver_run
from clawscore_fleet.versions import (
    FEED_NEWEST,
    FILE_READ_LIMIT,
    LANDSCAPE,
    MATRIX_RELEASE_COUNT,
    ROOT,
    SEED_TABLE,
    contains_word_safe,
    hark_key,
    stable_releases,
)

EVIDENCE = ROOT / "evidence"
MATRIX = EVIDENCE / "matrix"
CACHE = ROOT / ".cache" / "tarballs"
HEX = re.compile(r"^[0-9a-f]{64}$")
# Upstream dist basenames. Chunk filenames are an artifact listing, the same
# class as the matrix listings, and some basenames contain the banned wording
# token. Every other evidence file and the README stay in the wording scan.
REA_DIRLIST_NAMES = EVIDENCE / "rea" / "idle-linux" / "dist-names-2026.4.15.txt"
COUNT_RE = {
    "total_advisories": re.compile(r"total_advisories:\s*(\d+)"),
    "with_cve_id": re.compile(r"with_cve_id:\s*(\d+)"),
    "without_cve_id": re.compile(r"without_cve_id:\s*(\d+)"),
    "without_cve_id_critical_or_high": re.compile(r"without_cve_id_critical_or_high:\s*(\d+)"),
}


def percent_display(numerator: int, denominator: int) -> str:
    if denominator <= 0:
        return "0.0"
    scaled = (numerator * 1000) // denominator
    return f"{scaled // 10}.{scaled % 10}"


def _run(cmd: list[str], cwd: Path) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, check=False)


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _parse_counts(text: str) -> dict[str, int]:
    found = {}
    for name, pattern in COUNT_RE.items():
        match = pattern.search(text)
        if not match:
            raise ValueError(f"count_nocve.py did not print {name}")
        found[name] = int(match.group(1))
    return found


def landscape_gate() -> dict:
    sha = _run(["sha256sum", "-c", "SHA256SUMS"], LANDSCAPE)
    counted = _run([sys.executable, "count_nocve.py"], LANDSCAPE)
    recomputed = _run([sys.executable, "recompute.py"], LANDSCAPE)
    log = "\n".join(
        [
            "command: sha256sum -c SHA256SUMS",
            sha.stdout,
            sha.stderr,
            f"exit {sha.returncode}",
            "",
            f"command: {sys.executable} count_nocve.py",
            counted.stdout,
            counted.stderr,
            f"exit {counted.returncode}",
            "",
            f"command: {sys.executable} recompute.py",
            recomputed.stdout,
            recomputed.stderr,
            f"exit {recomputed.returncode}",
            "",
        ]
    )
    EVIDENCE.mkdir(parents=True, exist_ok=True)
    (EVIDENCE / "landscape-check.log").write_text(log)
    counts = {}
    parse_error = ""
    try:
        counts = _parse_counts(counted.stdout)
    except ValueError as exc:
        parse_error = str(exc)
    expected_doc = json.loads(
        (ROOT / "inputs/clawscore-feed-csv-2026-10-17/expected-landscape.json").read_text()
    )
    expected = {
        "total_advisories": expected_doc["total_advisories"],
        "with_cve_id": expected_doc["with_cve_id"],
        "without_cve_id": expected_doc["without_cve_id"],
        "without_cve_id_critical_or_high": expected_doc["without_cve_id_critical_or_high"],
    }
    sha_ok = sha.returncode == 0 and "FAILED" not in sha.stdout
    numbers_ok = counts == expected
    recompute_ok = (
        recomputed.returncode == 0
        and f"advisories {expected_doc['total_advisories']}" in recomputed.stdout
        and "stable releases 117" in recomputed.stdout
    )
    return {
        "pass": sha_ok and numbers_ok and recompute_ok and not parse_error,
        "sha256sum_exit": sha.returncode,
        "total_advisories": counts.get("total_advisories"),
        "with_cve_id": counts.get("with_cve_id"),
        "without_cve_id": counts.get("without_cve_id"),
        "without_cve_id_critical_or_high": counts.get("without_cve_id_critical_or_high"),
        "parse_error": parse_error,
        "recompute_exit": recomputed.returncode,
    }


def _load_listings() -> dict:
    return load_listings()


def _load_releases() -> list[dict]:
    payload = json.loads((MATRIX / "releases.json").read_text())
    return list(payload["releases"])


def matrix_gate(listings: dict, stable: list[str]) -> dict:
    releases = _load_releases() if (MATRIX / "releases.json").is_file() else []
    sha_text = (MATRIX / "tarballs.sha256").read_text() if (MATRIX / "tarballs.sha256").is_file() else ""
    sha_rows = {}
    for line in sha_text.splitlines():
        if not line.strip():
            continue
        digest, filename = line.split(None, 1)
        sha_rows[filename] = digest
    by_version = {row["version"]: row for row in releases}
    missing = []
    bad_hash = []
    for version in stable:
        row = by_version.get(version)
        files = listings.get(version)
        if row is None or not files or row.get("tarball") not in sha_rows:
            missing.append(version)
            continue
        if not HEX.fullmatch(row.get("sha256") or "") or sha_rows[row["tarball"]] != row["sha256"]:
            bad_hash.append(version)
            continue
        for path, digest in files:
            if not path or not HEX.fullmatch(digest):
                bad_hash.append(version)
                break
    cache_checked = 0
    cache_mismatch = []
    if CACHE.is_dir():
        for row in releases:
            path = CACHE / row["tarball"]
            if not path.is_file():
                continue
            cache_checked += 1
            if _sha256_file(path) != row["sha256"]:
                cache_mismatch.append(row["version"])
    have = len(stable) - len(missing)
    return {
        "pass": have == len(stable) == MATRIX_RELEASE_COUNT and not bad_hash and not cache_mismatch,
        "have": have,
        "total": len(stable),
        "expected": MATRIX_RELEASE_COUNT,
        "bad_hash": len(bad_hash),
        "cache_checked": cache_checked,
        "cache_mismatch": cache_mismatch,
        "missing": missing,
    }


def _classify(listings: dict, db: dict) -> list[dict]:
    rows = []
    for version in sorted(listings, key=lambda item: hark_key(item) or (0,)):
        files = listings[version]
        result = identify(
            [pair[0] for pair in files],
            lambda rels, stored=files: {rel: _lookup_hash(stored, rel) for rel in rels},
            db,
        )
        rows.append(
            {
                "version": version,
                "predicted": result["version"] or "",
                "verdict": result["verdict"],
                "candidates": "|".join(result["candidates"]),
                "reads": str(result["reads"]),
            }
        )
    return rows


def _read_confusion() -> list[dict]:
    with (EVIDENCE / "matrix-confusion.csv").open(newline="") as handle:
        return list(csv.DictReader(handle))


def fingerprint_gates(listings: dict, db: dict) -> dict:
    fresh = _classify(listings, db)
    saved = _read_confusion()
    saved_key = [(row["version"], row["predicted"], row["verdict"], row["candidates"], str(row["reads"])) for row in saved]
    fresh_key = [(row["version"], row["predicted"], row["verdict"], row["candidates"], row["reads"]) for row in fresh]
    groups = collision_groups(db)
    colliding = {version for group in groups for version in group}
    non = [row for row in fresh if row["version"] not in colliding]
    correct = sum(1 for row in non if row["verdict"] == "exact" and row["predicted"] == row["version"])
    pair = ["2026.4.7-1", "2026.4.8"]
    pair_group = next((group for group in groups if set(pair) <= set(group)), None)
    range_bad = []
    for row in fresh:
        if row["version"] not in colliding:
            continue
        wanted = next(group for group in groups if row["version"] in group)
        got = row["candidates"].split("|") if row["candidates"] else []
        if row["verdict"] != "range" or got != wanted:
            range_bad.append(row["version"])
    reads = [int(row["reads"]) for row in fresh]
    matrix_max = max(reads) if reads else 0
    dirlist = _dirlist(listings, list(listings))
    saved_dir = json.loads((EVIDENCE / "dirlist-metric.json").read_text())
    saved_groups = json.loads((EVIDENCE / "collisions.json").read_text())
    confusion_match = saved_key == fresh_key
    listing_count = len(listings)
    return {
        "matrix_exact": {
            "pass": correct == len(non) and len(non) + len(colliding) == len(fresh) and confusion_match and len(fresh) == listing_count,
            "correct": correct,
            "non_colliding": len(non),
            "total": len(fresh),
            "percent_display": percent_display(correct, len(non)),
            "confusion_match": confusion_match,
        },
        "collisions": {
            "pass": pair_group is not None and not range_bad and saved_groups.get("groups") == groups and saved_groups.get("count") == len(groups),
            "count": len(groups),
            "groups": groups,
            "includes_pair": pair_group,
            "range_bad": range_bad,
        },
        "dirlist_metric": {
            "pass": dirlist["total"] == listing_count and saved_dir.get("correct") == dirlist["correct"] and saved_dir.get("total") == dirlist["total"],
            "correct": dirlist["correct"],
            "total": dirlist["total"],
            "accuracy_display": dirlist["accuracy_display"],
            "listing_collision_groups": dirlist["listing_collision_groups"],
        },
        "matrix_reads_max": matrix_max,
        "matrix_reads_ok": matrix_max <= FILE_READ_LIMIT,
    }


def seed_gate(listings: dict) -> dict:
    matched = 0
    total = 0
    mismatches = []
    for version, files in SEED_TABLE.items():
        stored = {path: digest for path, digest in listings.get(version, [])}
        for rel, expected in files.items():
            total += 1
            got = stored.get(rel)
            if got == expected:
                matched += 1
            else:
                mismatches.append(f"{version} {rel}")
    return {
        "pass": matched == total == 9 and not mismatches,
        "matched": matched,
        "total": total,
        "mismatches": mismatches,
    }


def cve_gate() -> dict:
    written = write_outputs()
    diff = written["diff"]
    lines = 0 if not diff else len(diff.splitlines())
    pinned = json.loads((ROOT / "inputs/clawscore-v0.2.3-gate/expected-v023.json").read_text())["fix_target"]
    focus_version = pinned["focus_version"]
    focus = version_counts(focus_version)
    clearing = written["fixorder"]["min_clearing_version"]
    published_rows = {
        row[0]: row for row in json.loads((LANDSCAPE / "version-vulns.json").read_text())
    }
    published = published_rows[focus_version]
    version_row = (written["cve_map"]["versions"].get(focus_version) or {})
    counted_ids = set(version_row.get("ghsa_ids") or [])
    withdrawn_ids = set(version_row.get("withdrawn_not_counted") or [])
    actual = {
        "min_clearing_version": clearing,
        "focus_version": focus_version,
        "advisories": focus["advisories"],
        "critical": focus["critical"],
        "high": focus["high"],
        "medium": focus["medium"],
        "low": focus["low"],
    }
    # Advisory totals come from the regenerated landscape. The pinned file still
    # names the focus release and the clearing release; its advisory totals counted
    # withdrawn rows.
    expected = {
        "min_clearing_version": pinned["min_clearing_version"],
        "focus_version": focus_version,
        "advisories": published[2],
        "critical": published[3]["critical"],
        "high": published[3]["high"],
        "medium": published[3]["medium"],
        "low": published[3]["low"],
    }
    return {
        "cve_mapping": {"pass": lines == 0, "diff_lines": lines},
        "fix_target": {
            "pass": actual == expected and not (counted_ids & withdrawn_ids),
            **actual,
            "withdrawn_not_counted": len(withdrawn_ids),
        },
        "diff": diff,
    }


def freshness_gate(extra_paths: list[Path] | None = None) -> dict:
    reports = [
        EVIDENCE / "cve-map.json",
        EVIDENCE / "fixorder.json",
        EVIDENCE / "collisions.json",
        EVIDENCE / "dirlist-metric.json",
        EVIDENCE / "fingerprint-set.json",
        MATRIX / "releases.json",
    ]
    if extra_paths:
        reports.extend(extra_paths)
    missing_feed = []
    for path in reports:
        if not path.is_file():
            missing_feed.append(str(path.relative_to(ROOT)))
            continue
        payload = json.loads(path.read_text())
        if payload.get("feed_newest") != FEED_NEWEST:
            missing_feed.append(str(path.relative_to(ROOT)))
    skip = {
        EVIDENCE / "landscape",
        EVIDENCE / "matrix" / "listings.json",
        EVIDENCE / "SHA256SUMS",
    }
    hits = []
    scan_roots = [EVIDENCE, ROOT / "README.md"]
    for root in scan_roots:
        paths = [root] if root.is_file() else list(root.rglob("*"))
        for path in paths:
            if not path.is_file():
                continue
            if is_listing_blob(path):
                continue
            if path.resolve() == REA_DIRLIST_NAMES.resolve():
                continue
            if "landscape" in path.parts:
                continue
            # Captured registry bodies. Their titles are not this repo's wording,
            # and the gate's token occurs inside those titles.
            if path.parent.name == "raw" and path.parent.parent.name == "npm-audit" and path.name.startswith("resp-"):
                continue
            if path.stat().st_size > 20_000_000:
                continue
            text = path.read_text(errors="replace")
            if contains_word_safe(text):
                hits.append(str(path.relative_to(ROOT)))
    return {
        "pass": not missing_feed and not hits,
        "feed_newest": FEED_NEWEST,
        "missing_feed": missing_feed,
        "word_hits": hits,
        "skipped": [
            "evidence/landscape",
            "evidence/matrix/listings.json",
            "evidence/rea/idle-linux/dist-names-2026.4.15.txt",
        ],
    }


def _refresh_verify_report(gates: dict) -> None:
    """Copy the offline matrix and dirlist figures into the committed report.

    Lab-only gates stay as they were. A missing report is left missing.
    """
    path = EVIDENCE / "verify-report.json"
    if not path.is_file():
        return
    from clawscore_fleet.gates_v023 import no_regression

    report = json.loads(path.read_text())
    exact = gates["matrix_exact"]
    dirlist = gates["dirlist_metric"]
    report_gates = report.setdefault("gates", {})
    report_gates["matrix_exact"] = exact
    report_gates["dirlist_metric"] = dirlist
    display = report.setdefault("display", {})
    display["matrix_correct"] = exact["correct"]
    display["matrix_non_colliding"] = exact["non_colliding"]
    display["matrix_percent"] = exact["percent_display"]
    display["dirlist_correct"] = dirlist["correct"]
    display["dirlist_total"] = dirlist["total"]
    display["dirlist_percent"] = dirlist["accuracy_display"]
    report_gates["no_regression"] = no_regression(report_gates)
    path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")


def run() -> dict:
    stable = stable_releases()
    landscape = landscape_gate()
    listings = _load_listings()
    coverage = matrix_gate(listings, stable)
    db = load_db()
    fingerprints = fingerprint_gates(listings, db)
    seeds = seed_gate(listings)
    cves = cve_gate()
    semver = semver_run()
    idle = evaluate_idle_linux()
    write_scan_artifacts(idle["row"])
    freshness = freshness_gate()
    gates = {
        "landscape_hashes": {key: value for key, value in landscape.items()},
        "matrix_coverage": {key: value for key, value in coverage.items() if key != "missing"},
        "matrix_exact": fingerprints["matrix_exact"],
        "collisions": {
            "pass": fingerprints["collisions"]["pass"],
            "count": fingerprints["collisions"]["count"],
            "includes_pair": fingerprints["collisions"]["includes_pair"],
        },
        "dirlist_metric": fingerprints["dirlist_metric"],
        "cve_mapping": cves["cve_mapping"],
        "semver_crosscheck": {
            "pass": semver["pass"],
            "disagreements": semver["disagreements"],
            "unexplained": semver["unexplained"],
            "semver": semver["semver"],
            "decisions": semver["decisions"],
        },
        "freshness": freshness,
        "fix_target": cves["fix_target"],
        "v01_regression": {key: value for key, value in seeds.items() if key != "mismatches"},
    }
    gates.update(extra_offline_gates(semver, landscape))
    gates.update(idle["gates"])
    offline_names = [
        "landscape_hashes",
        "matrix_coverage",
        "matrix_exact",
        "collisions",
        "dirlist_metric",
        "cve_mapping",
        "semver_crosscheck",
        "freshness",
        "fix_target",
        "v01_regression",
        "semver_comma_normalized",
        "prerelease_order",
        "glued_bound_effect",
        "feed_pinned",
        "landscape_constants",
        "feed_check_same",
        "semver_crosscheck_894",
        "idle_linux_discovered",
        "idle_linux_version_recovered",
        "changelog_ghsa_30",
        "agent365_published_schema",
        "changelog_not_in_feed",
    ]
    failures = []
    for name in offline_names:
        if gates[name].get("pass") is not True:
            failures.append(f"{name} failed")
    if not fingerprints["matrix_reads_ok"]:
        failures.append(f"matrix reads max {fingerprints['matrix_reads_max']} exceeds {FILE_READ_LIMIT}")
    _refresh_verify_report(gates)
    drift = ""
    report_path = EVIDENCE / "verify-report.json"
    if not report_path.is_file():
        drift = "evidence/verify-report.json is missing"
    else:
        from clawscore_fleet.render_readme import readme_drift

        report = json.loads(report_path.read_text())
        readme_path = ROOT / "README.md"
        readme_text = readme_path.read_text() if readme_path.is_file() else ""
        drift = readme_drift(readme_text, report)
    gates["readme_matches_report"] = {"pass": drift == "", "drift": drift}
    offline_names.append("readme_matches_report")
    if drift and "readme_matches_report failed" not in failures:
        failures.append("readme_matches_report failed")
    print(json.dumps({"offline_failures": failures, "gates": {name: gates[name]["pass"] for name in offline_names}}, indent=2), flush=True)
    return {
        "gates": gates,
        "failures": failures,
        "groups": fingerprints["collisions"]["groups"],
        "matrix_reads_max": fingerprints["matrix_reads_max"],
        "stable": stable,
        "listings_count": len(listings),
    }


def main() -> int:
    if not listings_present():
        raise SystemExit("evidence/matrix/listings shards are missing")
    result = run()
    return 0 if not result["failures"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
