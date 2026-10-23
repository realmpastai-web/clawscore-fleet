"""v0.2.3 gates. Actuals are read from evidence files and frozen inputs, not typed in."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

from clawscore_fleet.cves import in_range
from clawscore_fleet.pkgmatch import is_openclaw_npm
from clawscore_fleet.feed_check import evaluate
from clawscore_fleet.versions import (
    FEED_NEWEST,
    ROOT,
    RangeSyntaxError,
    hark_key,
    parse_comparators,
)

EVIDENCE = ROOT / "evidence"
STAGE = EVIDENCE / "v0.2.2-stage"
LANDSCAPE = EVIDENCE / "landscape"
EXPECTED_LANDSCAPE = ROOT / "inputs/clawscore-feed-csv-2026-10-17/expected-landscape.json"
EXPECTED_V023 = ROOT / "inputs/clawscore-v0.2.3-gate/expected-v023.json"


def _load(path: Path):
    return json.loads(path.read_text())


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _sums_hash(directory: Path, name: str) -> str:
    for line in (directory / "SHA256SUMS").read_text().splitlines():
        digest, filename = line.split(None, 1)
        if filename == name:
            return digest
    raise SystemExit(f"{name} is not listed in {directory / 'SHA256SUMS'}")


def _section_lines(text: str, start: str, stop_prefixes: tuple[str, ...]) -> list[str]:
    lines = text.splitlines()
    began = False
    found = []
    for line in lines:
        if line.startswith(start):
            began = True
            found.append(line)
            continue
        if not began:
            continue
        if any(line.startswith(prefix) for prefix in stop_prefixes):
            break
        found.append(line)
    return found


def _pairs(lines: list[str]) -> dict[str, str]:
    found = {}
    for line in lines:
        if "\t" not in line:
            continue
        key, value = line.split("\t", 1)
        found[key] = value
    return found


def _openclaw_ranges(advisories: list) -> list[str]:
    found = []
    seen = set()
    for advisory in advisories:
        for entry in advisory.get("vulnerabilities") or []:
            package = entry.get("package") or {}
            rng = entry.get("vulnerable_version_range")
            if not is_openclaw_npm(package, advisory.get("ghsa_id")) or not rng or rng in seen:
                continue
            seen.add(rng)
            found.append(rng)
    return found


def _exec_defs(path: Path, start: str, until: str) -> dict:
    text = path.read_text()
    namespace = {"re": re, "json": json}
    exec(text[text.index(start) : text.index(until)], namespace)
    return namespace


def semver_comma_normalized(semver: dict) -> dict:
    log_path = EVIDENCE / "semver-crosscheck.log"
    log = log_path.read_text() if log_path.is_file() else ""
    grammar_lines = sum(1 for line in log.splitlines() if "hark-grammar" in line)
    ours = _pairs(_section_lines((EVIDENCE / "v0.2.2-repro.log").read_text(), "== 1.", ("== 2.",)))
    frozen = _pairs(
        _section_lines(
            (ROOT / "inputs/clawscore-v0.2.2/repro/repro.log").read_text(),
            "== 1.",
            ("== 2.",),
        )
    )
    keys = ("agree_after_norm", "post_release", "parser_diff", "mislabeled_grammar")
    match = all(ours.get(key) == frozen.get(key) and ours.get(key) for key in keys)
    comma = semver.get("comma_ranges_sent")
    return {
        "pass": comma == 0 and grammar_lines == 0 and match,
        "comma_ranges_sent": comma,
        "hark_grammar_lines": grammar_lines,
        "agree_after_norm": int(ours["agree_after_norm"]) if ours.get("agree_after_norm") else None,
        "post_release": int(ours["post_release"]) if ours.get("post_release") else None,
        "parser_diff": int(ours["parser_diff"]) if ours.get("parser_diff") else None,
        "mislabeled_grammar": int(ours["mislabeled_grammar"]) if ours.get("mislabeled_grammar") else None,
    }


def prerelease_order() -> dict:
    published = _load(STAGE / "landscape/versions.json")
    advisories = _load(STAGE / "landscape/ghsa-all.json")
    ranges = _openclaw_ranges(advisories)
    bounds = [bound for rng in ranges for _op, bound in parse_comparators(rng)]
    unparsed_versions = [version for version in published if hark_key(version) is None]
    unparsed_bounds = [bound for bound in bounds if hark_key(bound) is None]
    oracle = _exec_defs(
        ROOT / "inputs/clawscore-v0.2.2/landscape-v0.2.2/recompute.py",
        "def key(",
        "def inrange(",
    )["key"]
    key_mismatch = [
        item
        for item in list(published) + bounds
        if hark_key(item) != oracle(item)
    ]
    order = ["2026.5.19-alpha.1", "2026.5.19-beta.2", "2026.5.19", "2026.5.19-1"]
    keys = [hark_key(item) for item in order]
    ordered = all(item is not None for item in keys) and keys == sorted(keys)
    glued = hark_key("2026.1.29-beta3") == hark_key("2026.1.29-beta.3")
    alpha = in_range("2026.5.19-alpha.1", "<= 2026.5.19-beta.2")
    summary = (STAGE / "semver-check.out").read_text().strip()
    repro = _pairs(_section_lines((EVIDENCE / "v0.2.2-repro.log").read_text(), "== 4.", ("== 5.",)))
    frozen = _pairs(
        _section_lines((ROOT / "inputs/clawscore-v0.2.2/repro/repro.log").read_text(), "== 4.", ("== 5.",))
    )
    decisions = disagreements = unexplained = None
    match = re.search(
        r"decisions (\d+) disagreements (\d+) unexplained (\d+)",
        summary,
    )
    if match:
        decisions, disagreements, unexplained = (int(item) for item in match.groups())
    post = int(repro["disagree_norm_pre:post_release"]) if "disagree_norm_pre:post_release" in repro else None
    other = int(repro.get("disagree_norm_pre:other") or 0)
    frozen_decisions = int(frozen["decisions"])
    frozen_post = int(frozen["disagree_norm_pre:post_release"])
    passed = (
        not unparsed_versions
        and not unparsed_bounds
        and not key_mismatch
        and ordered
        and glued
        and alpha
        and decisions == frozen_decisions
        and disagreements == frozen_post
        and unexplained == 0
        and post == frozen_post
        and other == 0
        and "disagree_norm_pre:other" not in frozen
    )
    return {
        "pass": passed,
        "catalog_versions": len(published),
        "catalog_parsed": len(published) - len(unparsed_versions),
        "ranges": len(ranges),
        "bounds": len(bounds),
        "bounds_parsed": len(bounds) - len(unparsed_bounds),
        "key_mismatches": len(key_mismatch),
        "order_ok": ordered and glued and alpha,
        "decisions": decisions,
        "disagreements": disagreements,
        "post_release_suffix": post,
        "parser_diff": other,
        "unexplained": unexplained,
    }


def _clearing_version(rows: list) -> str | None:
    def weight(row: dict) -> int:
        return row["critical"] + row["high"]

    parsed = [{"version": row[0], **row[3]} for row in rows]
    for index, row in enumerate(parsed):
        if all(weight(later) == 0 for later in parsed[index:]):
            return row["version"]
    return None


def glued_bound_effect() -> dict:
    old_rows = _load(ROOT / "inputs/landscape/version-vulns.json")
    new_rows = _load(STAGE / "landscape/version-vulns.json")
    old = {row[0]: row for row in old_rows}
    new = {row[0]: row for row in new_rows}
    changed = []
    for version, row in new.items():
        previous = old[version]
        if previous[2] != row[2] or previous[3] != row[3]:
            changed.append(
                {
                    "version": version,
                    "before": previous[2],
                    "after": row[2],
                    "delta": row[2] - previous[2],
                    "severity_delta": {
                        name: row[3][name] - previous[3][name] for name in ("critical", "high", "medium", "low")
                    },
                }
            )
    advisories = _load(STAGE / "landscape/ghsa-all.json")
    ranges = []
    for advisory in advisories:
        for entry in advisory.get("vulnerabilities") or []:
            package = entry.get("package") or {}
            rng = entry.get("vulnerable_version_range")
            if is_openclaw_npm(package, advisory.get("ghsa_id")) and rng:
                ranges.append((advisory.get("ghsa_id"), rng))
    old_ns = _exec_defs(ROOT / "inputs/landscape/recompute.py", "def key(", "def hits(")
    added: dict[str, int] = {}
    removed: dict[str, int] = {}
    for version in new:
        old_ids = {gid for gid, rng in ranges if old_ns["inrange"](version, rng)}
        new_ids = {gid for gid, rng in ranges if in_range(version, rng)}
        for gid in sorted(new_ids - old_ids):
            added[gid] = added.get(gid, 0) + 1
        for gid in sorted(old_ids - new_ids):
            removed[gid] = removed.get(gid, 0) + 1
    digest = _sha(STAGE / "landscape/version-vulns.json")
    listed = _sums_hash(STAGE / "landscape", "version-vulns.json")
    diff_path = STAGE / "cve-map-diff.txt"
    diff_bytes = diff_path.stat().st_size if diff_path.is_file() else None
    focus = _load(EXPECTED_V023)["fix_target"]["focus_version"]
    cited = old_rows[0][0]
    focus_same = old[focus][2:] == new[focus][2:]
    passed = digest == listed and diff_bytes == 0 and not removed and focus_same and bool(changed)
    return {
        "pass": passed,
        "version_vulns_sha256": digest,
        "cve_map_diff_bytes": diff_bytes,
        "releases_changed": len(changed),
        "advisories_added": sum(item["delta"] for item in changed),
        "critical_added": sum(item["severity_delta"]["critical"] for item in changed),
        "changed": changed,
        "added_ghsa": added,
        "removed_ghsa": removed,
        "cited_version": cited,
        "cited_before": old[cited][2],
        "cited_after": new[cited][2],
        "cited_critical": new[cited][3]["critical"],
        "cited_high": new[cited][3]["high"],
        "focus_version": focus,
        "focus_unchanged": focus_same,
        "focus_advisories": new[focus][2],
        "min_clearing_version": _clearing_version(new_rows),
    }


def feed_pinned() -> dict:
    expected = _load(EXPECTED_V023)
    digest = _sha(LANDSCAPE / "ghsa-all.json")
    wanted = expected["sha256"]["evidence/landscape/ghsa-all.json"]
    newest = FEED_NEWEST == expected["feed_newest"]
    present = any(
        item.get("ghsa_id") == "GHSA-xx9p-hc9w-6p5h" for item in _load(LANDSCAPE / "ghsa-all.json")
    )
    return {
        "pass": digest == wanted and newest and present,
        "ghsa_sha256": digest,
        "feed_newest": FEED_NEWEST,
        "ghsa_xx9p_present": present,
    }


def landscape_constants(landscape: dict) -> dict:
    expected = _load(EXPECTED_LANDSCAPE)
    keys = (
        "total_advisories",
        "with_cve_id",
        "without_cve_id",
        "without_cve_id_critical_or_high",
    )
    actual = {key: landscape.get(key) for key in keys}
    wanted = {key: expected[key] for key in keys}
    return {
        "pass": landscape.get("pass") is True and actual == wanted and FEED_NEWEST == expected["feed_newest"],
        **actual,
        "feed_newest": expected["feed_newest"],
    }


def feed_check_same() -> dict:
    result = evaluate()
    log = EVIDENCE / "feed-check.log"
    log.write_text(result["text"])
    if result["status"] == "offline":
        print("SKIP feed_check_same (offline)", flush=True)
    return {
        "pass": result["pass"],
        "status": result["status"],
        "newer": result["newer"],
    }


def semver_crosscheck_894(semver: dict) -> dict:
    expected = _load(EXPECTED_V023)["semver_crosscheck"]
    log = (EVIDENCE / "semver-crosscheck.log").read_text() if (EVIDENCE / "semver-crosscheck.log").is_file() else ""
    grammar_lines = sum(1 for line in log.splitlines() if "hark-grammar" in line)
    post_lines = sum(1 for line in log.splitlines() if line.startswith("  explanation: post-release-suffix:"))
    published = _load(LANDSCAPE / "versions.json")
    ranges = _openclaw_ranges(_load(LANDSCAPE / "ghsa-all.json"))
    unparsed_versions = [version for version in published if hark_key(version) is None]
    unparsed_bounds = []
    unparsed_ranges = []
    for rng in ranges:
        try:
            for _op, bound in parse_comparators(rng):
                if hark_key(bound) is None:
                    unparsed_bounds.append(bound)
        except RangeSyntaxError:
            unparsed_ranges.append(rng)
    numbers = all(semver.get(key) == expected[key] for key in expected)
    passed = (
        numbers
        and semver.get("pass") is True
        and grammar_lines == 0
        and semver.get("comma_ranges_sent") == 0
        and not unparsed_versions
        and not unparsed_bounds
        and not unparsed_ranges
        and post_lines == semver.get("disagreements")
    )
    return {
        "pass": passed,
        "semver": semver.get("semver"),
        "decisions": semver.get("decisions"),
        "disagreements": semver.get("disagreements"),
        "unexplained": semver.get("unexplained"),
        "post_release_suffix": post_lines,
        "comma_ranges_sent": semver.get("comma_ranges_sent"),
        "hark_grammar_lines": grammar_lines,
        "catalog_unparsed": len(unparsed_versions),
        "bounds_unparsed": len(unparsed_bounds),
        "ranges_unparsed": len(unparsed_ranges),
    }


def extra_offline_gates(semver: dict, landscape: dict) -> dict:
    return {
        "semver_comma_normalized": semver_comma_normalized(semver),
        "prerelease_order": prerelease_order(),
        "glued_bound_effect": glued_bound_effect(),
        "feed_pinned": feed_pinned(),
        "landscape_constants": landscape_constants(landscape),
        "feed_check_same": feed_check_same(),
        "semver_crosscheck_894": semver_crosscheck_894(semver),
    }


def _extra_listing_count() -> int:
    """Store rows that are not landscape stable releases. The frozen base counted only that set."""
    from clawscore_fleet.versions import stable_releases

    payload = json.loads((ROOT / "evidence" / "matrix" / "releases.json").read_text())
    stable = set(stable_releases())
    return sum(1 for row in payload["releases"] if row["version"] not in stable)


def no_regression(gates: dict) -> dict:
    base = json.loads((ROOT / "inputs/clawscore-v0.2.3-gate/base-verify-report-58d4925.json").read_text())
    names = _load(EXPECTED_V023)["unchanged_gates_vs_base"]
    extra = _extra_listing_count()
    expected_exact = dict(base["gates"]["matrix_exact"])
    expected_exact["correct"] += extra
    expected_exact["non_colliding"] += extra
    expected_exact["total"] += extra
    expected_dir = dict(base["gates"]["dirlist_metric"])
    expected_dir["correct"] += extra
    expected_dir["total"] += extra
    differ = []
    for name in names:
        actual = gates.get(name)
        if name == "matrix_exact":
            wanted = expected_exact
        elif name == "dirlist_metric":
            wanted = expected_dir
        else:
            wanted = base["gates"].get(name)
        if actual != wanted:
            differ.append(name)
    accuracy = gates.get("version_accuracy") or {}
    ranges = gates.get("range_verdicts") or {}
    stripped = gates.get("stripped") or {}
    exact = gates.get("matrix_exact") or {}
    coverage = gates.get("matrix_coverage") or {}
    figures = {
        "version_accuracy": [accuracy.get("correct"), accuracy.get("total")],
        "version_accuracy_pre": [accuracy.get("pre_correct"), accuracy.get("pre_total")],
        "range_verdicts": [ranges.get("ok"), ranges.get("total")],
        "stripped": [stripped.get("ok"), stripped.get("total")],
        "matrix_exact": [exact.get("correct"), exact.get("non_colliding")],
        "matrix_coverage": [coverage.get("have"), coverage.get("total")],
    }
    base_accuracy = base["gates"]["version_accuracy"]
    base_figures = {
        "version_accuracy": [base_accuracy["correct"], base_accuracy["total"]],
        "version_accuracy_pre": [base_accuracy["pre_correct"], base_accuracy["pre_total"]],
        "range_verdicts": [base["gates"]["range_verdicts"]["ok"], base["gates"]["range_verdicts"]["total"]],
        "stripped": [base["gates"]["stripped"]["ok"], base["gates"]["stripped"]["total"]],
        "matrix_exact": [expected_exact["correct"], expected_exact["non_colliding"]],
        "matrix_coverage": [base["gates"]["matrix_coverage"]["have"], base["gates"]["matrix_coverage"]["total"]],
    }
    return {
        "pass": not differ and figures == base_figures,
        "unchanged_gates": len(names) - len(differ),
        "unchanged_total": len(names),
        "differ": differ,
        "figures": figures,
    }


def readme_facts() -> dict:
    expected = _load(EXPECTED_LANDSCAPE)
    sources = expected["sources"]
    old_rows = _load(ROOT / "inputs/landscape/version-vulns.json")
    stage_rows = _load(STAGE / "landscape/version-vulns.json")
    base = json.loads((ROOT / "inputs/clawscore-v0.2.3-gate/base-verify-report-58d4925.json").read_text())
    oracle = (ROOT / "inputs/clawscore-feed-csv-2026-10-17/csv/escape_reference.py").read_text()
    rfc = re.search(r"RFC (\d+)", oracle)
    return {
        "advisory_total": expected["total_advisories"],
        "advisory_global": sources["global_db"],
        "advisory_repo_only": sources["repo_only"],
        "advisory_repo_already": sources["repo_only_on_or_before_2026_07_02"],
        "previous_feed_newest": base["feed_newest"],
        "cited_version": old_rows[0][0],
        "grammar_before": old_rows[0][2],
        "grammar_after": stage_rows[0][2],
        "csv_standard": f"RFC {rfc.group(1)}" if rfc else "",
    }


def _ghsa_steps() -> list[tuple[str, list[str]]]:
    import sys

    return [
        (
            "inputs",
            [
                "bash",
                "-lc",
                "cd inputs/clawscore-ghsa-only && sha256sum -c SHA256SUMS && python3 gate_ghsa_only.py | diff - gate-output.txt",
            ],
        ),
        (
            "fixtures",
            [sys.executable, "-m", "clawscore_fleet.ghsa_only_fixtures", "--out", "evidence/ghsa-only"],
        ),
        (
            "report",
            [
                sys.executable,
                "inputs/clawscore-ghsa-only/gate_ghsa_only.py",
                "--report",
                "evidence/ghsa-only/report.json",
            ],
        ),
    ]


def ghsa_only() -> dict:
    """Run the ghsa-only acceptance steps 1 to 3. Fail on any non-zero exit."""
    import subprocess

    from clawscore_fleet.ghsa_only import defender_claim, follow_up_text, frozen_task_claim, measured_readme_claim

    logs = []
    for name, cmd in _ghsa_steps():
        proc = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
        logs.append({"step": name, "exit": proc.returncode, "stdout": proc.stdout, "stderr": proc.stderr})
        if proc.returncode != 0:
            return {
                "pass": False,
                "steps": [{"step": item["step"], "exit": item["exit"]} for item in logs],
                "detail": f"{name} exit {proc.returncode}\n{proc.stdout}{proc.stderr}",
                "readme_claim": "",
                "defender_claim": "",
                "follow_up": "",
            }
    try:
        computed = measured_readme_claim()
        frozen = frozen_task_claim()
        defender = defender_claim()
        follow = follow_up_text()
    except SystemExit as exc:
        return {
            "pass": False,
            "steps": [{"step": item["step"], "exit": item["exit"]} for item in logs],
            "detail": str(exc),
            "readme_claim": "",
            "defender_claim": "",
            "follow_up": "",
        }
    exits = " ".join(f"{item['step']}={item['exit']}" for item in logs)
    if computed != frozen:
        return {
            "pass": False,
            "steps": [{"step": item["step"], "exit": item["exit"]} for item in logs],
            "detail": exits + "\nREADME claim mismatch\nCOMPUTED:\n" + computed + "\nFROZEN:\n" + frozen,
            "readme_claim": "",
            "defender_claim": "",
            "follow_up": follow,
        }
    return {
        "pass": True,
        "steps": [{"step": item["step"], "exit": item["exit"]} for item in logs],
        "detail": exits,
        "readme_claim": computed,
        "defender_claim": defender,
        "follow_up": follow,
    }


def main() -> int:
    result = ghsa_only()
    status = "PASS" if result["pass"] else "FAIL"
    if not result["pass"]:
        print(result["detail"], flush=True)
    print(f"{status}\tghsa_only\t{result['detail'] if result['pass'] else result['steps']}", flush=True)
    if result.get("follow_up"):
        print(result["follow_up"], flush=True)
    failed = [] if result["pass"] else ["ghsa_only"]
    print(
        f"SUMMARY pass={1 if result['pass'] else 0} fail={len(failed)} report=0 failed={failed}",
        flush=True,
    )
    return 0 if result["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
