"""make verify: offline gates plus the lab gates, then the report and README."""

from __future__ import annotations

import csv
import json
import re
import tempfile
from pathlib import Path

import yaml

from clawscore_fleet import __version__
from clawscore_fleet.blast import selftest
from clawscore_fleet.fixtures.idle_linux import LAYOUTS, build_fixture
from clawscore_fleet.idle_linux import VERSION_SOURCE, discover_all, idle_ok
from clawscore_fleet.listings_store import is_listing_blob
from clawscore_fleet.cves import _first_patched, _openclaw_ranges, build_index, has_critical_or_high, report_for_versions
from clawscore_fleet.fixorder import fix_order
from clawscore_fleet.export_defender import SpecError, export_gates, verbatim_flag_lines, write_exports
from clawscore_fleet.gates_v023 import ghsa_only as ghsa_only_gate
from clawscore_fleet.gates_v023 import no_regression, readme_facts
from clawscore_fleet.render_readme import write_readme
from clawscore_fleet.summary import summary_from_scan
from clawscore_fleet.verify_offline import freshness_gate, percent_display, run as offline_run
from clawscore_fleet.versions import (
    ACCURACY_TARGET_PERCENT,
    FEED_NEWEST,
    FILE_READ_LIMIT,
    NO_ADVISORY_WORDING,
    OLD_BUILD_CUTOFF,
    PATCH_BOUNDARY,
    RECALL_TARGET_PERCENT,
    ROOT,
    contains_word_safe,
    is_before,
    load_published,
)

EVIDENCE = ROOT / "evidence"
CHAIN_IDS = [
    "GHSA-wppj-c6mr-83jj",
    "GHSA-5h3g-6xhh-rg6p",
    "GHSA-x3h8-jrgh-p8jx",
    "GHSA-r6xh-pqhr-v4xh",
]
SCANNER_FILES = [
    "clawscore_fleet/fingerprint.py",
    "clawscore_fleet/cli.py",
    "clawscore_fleet/blast.py",
    "clawscore_fleet/blast.js",
    "clawscore_fleet/cves.py",
    "clawscore_fleet/fixorder.py",
    "clawscore_fleet/docker_target.py",
    "clawscore_fleet/scan_lab.py",
    "clawscore_fleet/summary.py",
]
BANNED = ["manifest.yaml", "secrets-pool.json", "defender_view.json", "docker inspect"]
NUMBER_RE = re.compile(r"\d+(?:\.\d+)*")


def _meets(numerator: int, denominator: int, target: int) -> bool:
    return denominator > 0 and numerator * 100 >= target * denominator


def _mean(total: int, count: int) -> str:
    if count <= 0:
        return "0.00"
    scaled = total * 100
    quotient, remainder = divmod(scaled, count)
    if remainder * 2 >= count:
        quotient += 1
    whole, frac = divmod(quotient, 100)
    return f"{whole}.{frac:02d}"


def _load_scan() -> dict:
    return json.loads((EVIDENCE / "scan.json").read_text())


def _load_manifest() -> dict:
    return yaml.safe_load((ROOT / "fleet" / "manifest.yaml").read_text())


def _pool_values() -> list[str]:
    pool = json.loads((ROOT / "fleet" / "secrets-pool.json").read_text())
    return [value for value in pool.values() if isinstance(value, str) and value]


def _secret_hits(paths: list[Path], values: list[str]) -> list[str]:
    hits = []
    for path in paths:
        if not path.is_file() or path.stat().st_size > 20_000_000:
            continue
        text = path.read_text(errors="replace")
        if any(value in text for value in values):
            hits.append(f"{path.relative_to(ROOT)} contains a planted credential value")
    return hits


def _chain() -> list[dict]:
    index = build_index()
    by_id = {item.get("ghsa_id"): item for item in index["advisories"]}
    rows = []
    for ghsa_id in CHAIN_IDS:
        advisory = by_id.get(ghsa_id)
        if not advisory:
            continue
        ranges = _openclaw_ranges(advisory)
        title = str(advisory.get("summary") or ghsa_id)
        if contains_word_safe(title):
            title = ghsa_id
        cve_id = advisory.get("cve_id")
        sources = [advisory.get("html_url")]
        if cve_id:
            sources.append(f"https://nvd.nist.gov/vuln/detail/{cve_id}")
        rows.append(
            {
                "id": cve_id or ghsa_id,
                "ghsa_id": ghsa_id,
                "title": title,
                "affected": ranges[0] if ranges else "",
                "fixed_in": _first_patched(advisory) or "",
                "sources": [source for source in sources if source],
            }
        )
    return rows


def _ps_failures() -> list[str]:
    path = EVIDENCE / "ps.txt"
    if not path.is_file():
        return ["evidence/ps.txt is missing"]
    failures = []
    seen = []
    for line in path.read_text().splitlines():
        if not line.strip():
            continue
        parts = line.split("\t")
        while len(parts) < 3:
            parts.append("")
        name, status, ports = parts[0].strip(), parts[1].strip(), parts[2].strip()
        seen.append(name)
        if not status.startswith("Up"):
            failures.append(f"{name} status is {status}")
        if ports:
            failures.append(f"{name} has published ports")
    expected = [f"claw-{index:02d}" for index in range(1, 31)]
    if sorted(seen) != expected:
        failures.append(f"ps.txt containers {len(seen)} expected 30")
    return failures


def _network_failure() -> list[str]:
    path = EVIDENCE / "lab-up.log"
    if not path.is_file():
        return ["evidence/lab-up.log is missing"]
    if "network clawscore-lab internal=true" not in path.read_text():
        return ["lab-up.log does not record an internal network"]
    return []


def _scanner_banned() -> list[str]:
    hits = []
    for rel in SCANNER_FILES:
        text = (ROOT / rel).read_text()
        for banned in BANNED:
            if banned in text:
                hits.append(f"{rel} contains {banned}")
    return hits


def _readme_missing(readme: str, corpus: str) -> list[str]:
    missing = []
    for token in NUMBER_RE.findall(readme):
        if token not in corpus and token not in missing:
            missing.append(token)
    return missing


def _score_lab(scan: dict, manifest: dict, groups: list[list[str]]) -> dict:
    colliding = {version for group in groups for version in group}
    by_scan = {item["id"]: item for item in scan["installs"]}
    truth = manifest["installs"]
    published = load_published()
    failures: list[str] = []
    if len(truth) != 30 or len(by_scan) != 30:
        failures.append(f"install count scan={len(by_scan)} manifest={len(truth)}")
    overall_bits = []
    pre_bits = []
    range_ok = 0
    range_total = 0
    stripped_ok = 0
    stripped_total = 0
    confusion = []
    planted_pairs = 0
    found_pairs = 0
    extra_names = []
    auto_ok = 0
    mcp_ok = 0
    advisory_bad = []
    for item in truth:
        got = by_scan.get(item["id"])
        if got is None:
            failures.append(f"scan missing {item['id']}")
            continue
        is_collision = item["version"] in colliding
        exact = got.get("verdict") == "exact" and got.get("version") == item["version"]
        ranged = got.get("verdict") == "range" and item["version"] in (got.get("candidates") or [])
        if is_collision:
            range_total += 1
            if ranged:
                range_ok += 1
        else:
            overall_bits.append(exact)
            if is_before(item["version"], OLD_BUILD_CUTOFF):
                pre_bits.append(exact)
        if item["stripped"] != "none":
            stripped_total += 1
            if (is_collision and ranged) or (not is_collision and exact):
                stripped_ok += 1
        if got.get("verdict") == "exact":
            expected = report_for_versions([item["version"]])
            if got.get("advisory_count") != expected["advisories"] or got.get("vulnerable") != expected["vulnerable"]:
                advisory_bad.append(item["id"])
        elif got.get("verdict") == "range":
            expected = report_for_versions(list(got.get("candidates") or []))
            if got.get("ghsa_ids") != expected["ghsa_ids"] or got.get("vulnerable") != expected["vulnerable"]:
                advisory_bad.append(item["id"])
        if bool(got.get("auto_approve")) != bool(item["auto_approve"]):
            failures.append(f"{item['id']} autoApprove mismatch")
        else:
            auto_ok += 1
        if set(got.get("mcp_servers") or []) != set(item["mcp_servers"]):
            failures.append(f"{item['id']} mcp mismatch")
        else:
            mcp_ok += 1
        planted = set(item["credentials"])
        found = set(got.get("credentials") or [])
        planted_pairs += len(planted)
        found_pairs += len(planted & found)
        unexpected = sorted(found - planted)
        if unexpected:
            extra_names.append(f"{item['id']} unexpected credential names")
        pre = is_before(item["version"], OLD_BUILD_CUTOFF)
        confusion.append(
            {
                "install_id": item["id"],
                "true": item["version"],
                "predicted": got.get("version") or "",
                "verdict": got.get("verdict") or "",
                "candidates": "|".join(got.get("candidates") or []),
                "stripped": item["stripped"],
                "pre_2026_3_31": "yes" if pre else "no",
            }
        )
    pre_installs = [item for item in truth if is_before(item["version"], OLD_BUILD_CUTOFF)]
    months = sorted({published[item["version"]][:7] for item in pre_installs})
    present = {item["version"] for item in truth}
    old_pass = (
        len(pre_installs) >= 8
        and {"2026-01", "2026-02", "2026-03"} <= set(months)
        and "2026.1.29" in present
        and "2026.3.28" in present
    )
    acc_correct = sum(1 for bit in overall_bits if bit)
    pre_correct = sum(1 for bit in pre_bits if bit)
    accuracy_pass = _meets(acc_correct, len(overall_bits), ACCURACY_TARGET_PERCENT) and _meets(
        pre_correct, len(pre_bits), ACCURACY_TARGET_PERCENT
    )
    recall_pass = _meets(found_pairs, planted_pairs, RECALL_TARGET_PERCENT) and not extra_names
    log_text = (EVIDENCE / "files-read.log").read_text() if (EVIDENCE / "files-read.log").is_file() else ""
    counts: dict[str, int] = {}
    logged: dict[str, list[str]] = {}
    for line in log_text.splitlines():
        if not line.strip() or "\t" not in line:
            continue
        ident, fpath = line.split("\t", 1)
        counts[ident] = counts.get(ident, 0) + 1
        logged.setdefault(ident, []).append(fpath)
    read_values = []
    for item in scan["installs"]:
        read_values.append(len(item.get("files_read") or []))
        if logged.get(item["id"], []) != item.get("files_read"):
            failures.append(f"{item['id']} files-read.log does not match scan.json")
        if len(item.get("files_read") or []) > FILE_READ_LIMIT:
            failures.append(f"{item['id']} read more than {FILE_READ_LIMIT} files")
    files_max = max(read_values) if read_values else 0
    files_total = sum(read_values)
    truth_order = fix_order(
        [
            {
                "id": item["id"],
                "version": item["version"],
                "vulnerable": has_critical_or_high(item["version"]),
                "credentials": list(item["credentials"]),
                "auto_approve": bool(item["auto_approve"]),
                "cves": report_for_versions([item["version"]])["cve_ids"],
            }
            for item in truth
        ]
    )
    scan_patch = [step.get("install") for step in scan.get("fix_order") or [] if step.get("action") == "patch"]
    truth_patch = [step.get("install") for step in truth_order if step.get("action") == "patch"]
    scan_rotate = [step for step in scan.get("fix_order") or [] if step.get("action") == "rotate"]
    truth_rotate = [step for step in truth_order if step.get("action") == "rotate"]
    if scan_patch != truth_patch or scan_rotate != truth_rotate:
        failures.append("fix order does not match the answer key")
    if advisory_bad:
        failures.append("advisory union mismatch " + ",".join(advisory_bad))
    failures.extend(extra_names)
    failures.extend(_ps_failures())
    failures.extend(_network_failure())
    failures.extend(_scanner_banned())
    values = _pool_values()
    evidence_paths = [
        path
        for path in EVIDENCE.rglob("*")
        if path.is_file() and "landscape" not in path.parts and not is_listing_blob(path)
    ]
    source_paths = [
        path
        for path in list((ROOT / "fleet").rglob("*"))
        + list((ROOT / "clawscore_fleet").rglob("*"))
        + list((ROOT / "mock_agent365").rglob("*"))
        if path.is_file() and path.name != "secrets-pool.json" and "__pycache__" not in path.parts and path.suffix != ".pyc"
    ]
    failures.extend(_secret_hits(evidence_paths, values))
    failures.extend(_secret_hits(source_paths, values))
    if auto_ok != len(truth):
        failures.append(f"autoApprove matched {auto_ok} of {len(truth)}")
    if mcp_ok != len(truth):
        failures.append(f"mcp servers matched {mcp_ok} of {len(truth)}")
    summary = summary_from_scan(scan)
    if summary["sentence"] != (scan.get("summary") or {}).get("sentence"):
        failures.append("scan summary sentence was not computed from the scan body")
    if scan.get("feed_newest") != FEED_NEWEST:
        failures.append("scan.json feed_newest mismatch")
    return {
        "failures": failures,
        "confusion": confusion,
        "summary": summary,
        "old_builds": {
            "pass": old_pass,
            "count": len(pre_installs),
            "minimum": 8,
            "months": months,
            "cutoff": OLD_BUILD_CUTOFF,
            "includes_2026.1.29": "2026.1.29" in present,
            "includes_2026.3.28": "2026.3.28" in present,
        },
        "version_accuracy": {
            "pass": accuracy_pass,
            "correct": acc_correct,
            "total": len(overall_bits),
            "percent_display": percent_display(acc_correct, len(overall_bits)),
            "pre_correct": pre_correct,
            "pre_total": len(pre_bits),
            "pre_percent_display": percent_display(pre_correct, len(pre_bits)),
            "target_percent": ACCURACY_TARGET_PERCENT,
        },
        "range_verdicts": {"pass": range_ok == range_total, "ok": range_ok, "total": range_total},
        "stripped": {
            "pass": stripped_total >= 3 and stripped_ok == stripped_total,
            "ok": stripped_ok,
            "total": stripped_total,
            "minimum": 3,
        },
        "reads": {
            "max": files_max,
            "total_reads": files_total,
            "installs": len(read_values),
            "mean": _mean(files_total, len(read_values)),
        },
        "blast_recall": {
            "pass": recall_pass,
            "found": found_pairs,
            "planted": planted_pairs,
            "percent_display": percent_display(found_pairs, planted_pairs),
            "target_percent": RECALL_TARGET_PERCENT,
        },
        "installs": len(truth),
    }


def _display(report_gates: dict, stable: list[str], installs: int) -> dict:
    coverage = report_gates["matrix_coverage"]
    exact = report_gates["matrix_exact"]
    collisions = report_gates["collisions"]
    dirlist = report_gates["dirlist_metric"]
    reads = report_gates["reads"]
    old = report_gates["old_builds"]
    accuracy = report_gates["version_accuracy"]
    ranges = report_gates["range_verdicts"]
    stripped = report_gates["stripped"]
    cve = report_gates["cve_mapping"]
    semver = report_gates["semver_crosscheck"]
    fix = report_gates["fix_target"]
    blast = report_gates["blast_recall"]
    seeds = report_gates["v01_regression"]
    pair = collisions.get("includes_pair") or []
    return {
        "matrix_have": coverage["have"],
        "matrix_total": coverage["total"],
        "matrix_first": stable[0] if stable else "",
        "matrix_last": stable[-1] if stable else "",
        "matrix_correct": exact["correct"],
        "matrix_non_colliding": exact["non_colliding"],
        "matrix_percent": exact["percent_display"],
        "collision_count": collisions["count"],
        "collision_group": ", ".join(pair),
        "dirlist_correct": dirlist["correct"],
        "dirlist_total": dirlist["total"],
        "dirlist_percent": dirlist["accuracy_display"],
        "reads_max": reads["max"],
        "reads_mean": reads["mean"],
        "read_limit": reads["limit"],
        "old_count": old["count"],
        "old_minimum": old["minimum"],
        "old_cutoff": old["cutoff"],
        "old_months": ", ".join(old["months"]),
        "install_count": installs,
        "acc_correct": accuracy["correct"],
        "acc_total": accuracy["total"],
        "acc_percent": accuracy["percent_display"],
        "acc_target": accuracy["target_percent"],
        "pre_correct": accuracy["pre_correct"],
        "pre_total": accuracy["pre_total"],
        "pre_percent": accuracy["pre_percent_display"],
        "range_ok": ranges["ok"],
        "range_total": ranges["total"],
        "stripped_ok": stripped["ok"],
        "stripped_total": stripped["total"],
        "diff_lines": cve["diff_lines"],
        "semver_disagreements": semver["disagreements"],
        "semver_unexplained": semver["unexplained"],
        "focus_version": fix["focus_version"],
        "focus_advisories": fix["advisories"],
        "focus_critical": fix["critical"],
        "focus_high": fix["high"],
        "blast_found": blast["found"],
        "blast_planted": blast["planted"],
        "blast_percent": blast["percent_display"],
        "blast_target": blast["target_percent"],
        "seed_label": "v0.1",
        "seed_matched": seeds["matched"],
        "seed_total": seeds["total"],
    }


def _publish_date(version: str) -> str:
    published = load_published().get(version, "")
    return published[:10]


def idle_paths_gate() -> dict:
    """Four installer layouts on a fresh fixture, each idle at 2026.4.15."""
    expected = {name: LAYOUTS[name] for name in ("L1", "L2", "L3", "L3s")}
    with tempfile.TemporaryDirectory(prefix="clawscore-idle-paths-") as tmp:
        root = Path(tmp)
        build_fixture(root)
        rows = discover_all(root)
    by_install = {row["install"]: row for row in rows}
    versions = {name: (by_install.get(path) or {}).get("resolved_version") for name, path in expected.items()}
    sources = {name: (by_install.get(path) or {}).get("version_source") for name, path in expected.items()}
    idle_flags = {name: idle_ok(by_install[path]) if path in by_install else False for name, path in expected.items()}
    paths_ok = set(by_install) == set(expected.values()) and len(rows) == len(expected)
    versions_ok = set(versions.values()) == {"2026.4.15"} and len(versions) == len(expected)
    sources_ok = sources.get("L3s") == VERSION_SOURCE and all(
        sources.get(name) == "package.json" for name in ("L1", "L2", "L3")
    )
    idle_all = all(idle_flags.values()) and len(idle_flags) == len(expected)
    return {
        "pass": bool(paths_ok and versions_ok and sources_ok and idle_all),
        "actuals": {
            "installs": [row["install"] for row in rows],
            "expected": expected,
            "versions": versions,
            "version_sources": sources,
            "idle": idle_flags,
        },
    }


def main() -> int:
    selftest()
    offline = offline_run()
    scan = _load_scan()
    manifest = _load_manifest()
    lab = _score_lab(scan, manifest, offline["groups"])
    gates = dict(offline["gates"])
    gates["idle_paths"] = idle_paths_gate()
    gates["ghsa_only"] = ghsa_only_gate()
    gates["old_builds"] = lab["old_builds"]
    gates["version_accuracy"] = lab["version_accuracy"]
    gates["range_verdicts"] = lab["range_verdicts"]
    gates["stripped"] = lab["stripped"]
    gates["blast_recall"] = lab["blast_recall"]
    gates["reads"] = {
        "pass": lab["reads"]["max"] <= FILE_READ_LIMIT and offline["matrix_reads_max"] <= FILE_READ_LIMIT and not any(
            "files-read" in item for item in lab["failures"]
        ),
        "max": lab["reads"]["max"],
        "mean": lab["reads"]["mean"],
        "limit": FILE_READ_LIMIT,
        "total_reads": lab["reads"]["total_reads"],
        "installs": lab["reads"]["installs"],
        "matrix_max": offline["matrix_reads_max"],
    }
    published_patch = _publish_date(PATCH_BOUNDARY)
    facts = readme_facts()
    report = {
        "release": __version__,
        "base": "58d4925c3f83a0fae5ed947bd285cbc3d32f72f7",
        "feed_newest": FEED_NEWEST,
        **facts,
        "no_advisory_wording": NO_ADVISORY_WORDING,
        "agent_product": "Agent 365",
        "patch_boundary": PATCH_BOUNDARY,
        "patch_released": published_patch,
        "fix_version": gates["fix_target"]["min_clearing_version"],
        "python_requirement": "3.11",
        "chain_url": "https://www.cyera.com/blog/claw-chain-cyera-research-unveil-four-chainable-vulnerabilities-in-openclaw",
        "defender_url": "https://learn.microsoft.com/en-us/defender-endpoint/discover-local-ai-agents",
        "xdr_url": "https://learn.microsoft.com/en-us/defender-xdr/security-for-ai/ai-agent-inventory",
        "summary": lab["summary"],
        "cves": _chain(),
        "failures": [],
        "gates": gates,
    }
    report["display"] = _display(gates, offline["stable"], lab["installs"])
    failures = list(lab["failures"])
    for name, gate in gates.items():
        if not gate.get("pass"):
            failures.append(f"{name} failed")
    # Drop duplicate strings while keeping order.
    deduped = []
    for failure in failures:
        if failure not in deduped:
            deduped.append(failure)
    failures = deduped
    report["failures"] = failures
    report["ok"] = not failures
    report["gate_status"] = "pass" if report["ok"] else "fail"
    try:
        report["spec_unprovens"] = verbatim_flag_lines()
    except SpecError as exc:
        report["spec_unprovens"] = []
        print(str(exc), flush=True)
    EVIDENCE.mkdir(parents=True, exist_ok=True)
    with (EVIDENCE / "version-confusion.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=["install_id", "true", "predicted", "verdict", "candidates", "stripped", "pre_2026_3_31"],
        )
        writer.writeheader()
        writer.writerows(lab["confusion"])
    report_path = EVIDENCE / "verify-report.json"
    report_path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    write_readme(report)
    fresh = freshness_gate([report_path, EVIDENCE / "scan.json"])
    gates["freshness"] = fresh
    report["gates"] = gates
    failures = [item for item in failures if item != "freshness failed"]
    if not fresh["pass"] and "freshness failed" not in failures:
        failures.append("freshness failed")
    report["failures"] = failures
    report["ok"] = not failures and all(gate.get("pass") for gate in gates.values())
    report["gate_status"] = "pass" if report["ok"] else "fail"
    report["display"] = _display(gates, offline["stable"], lab["installs"])
    try:
        write_exports(report)
    except SpecError as exc:
        print(str(exc), flush=True)
        if "export write failed" not in failures:
            failures.append("export write failed")
        report["failures"] = failures
        report["ok"] = False
        report["gate_status"] = "fail"
    extra = export_gates(report)
    for name, gate in extra.items():
        gates[name] = gate
        if gate.get("pass") is not True and f"{name} failed" not in failures:
            failures.append(f"{name} failed")
    regression = no_regression(gates)
    gates["no_regression"] = regression
    if regression.get("pass") is not True and "no_regression failed" not in failures:
        failures.append("no_regression failed")
    report["gates"] = gates
    report["failures"] = failures
    report["ok"] = not failures and all(gate.get("pass") for gate in gates.values())
    report["gate_status"] = "pass" if report["ok"] else "fail"
    report["display"] = _display(gates, offline["stable"], lab["installs"])
    report_path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    write_readme(report)
    corpus = report_path.read_text()
    missing = _readme_missing((ROOT / "README.md").read_text(), corpus)
    if missing:
        print("README numbers missing from the report: " + ", ".join(missing), flush=True)
        if "readme number check failed" not in failures:
            failures.append("readme number check failed")
        report["failures"] = failures
        report["ok"] = False
        report["gate_status"] = "fail"
        report_path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
        write_readme(report)
    print(json.dumps({"ok": report["ok"], "failures": report["failures"]}, indent=2), flush=True)
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
