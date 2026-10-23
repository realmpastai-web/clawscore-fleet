"""Reader-facing written report. See docs/written-report.md."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

import yaml

from clawscore_fleet.cves import _rows_for_version, build_index, min_clearing_version
from clawscore_fleet.fixorder import fix_order
from clawscore_fleet.npm_audit import load_npm_section, sentence_for
from clawscore_fleet.summary import summary_from_scan
from clawscore_fleet.versions import FEED_NEWEST, ROOT

OBSERVED_AT_RE = re.compile(r"\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ")
RULE = (
    "package name casefold equals openclaw and ecosystem npm, "
    "or the ghsa_id is a data row in data/non-npm-keep.tsv; "
    "rows with withdrawn_at set are excluded"
)


def feed_sha256() -> str:
    path = ROOT / "evidence" / "landscape" / "ghsa-all.json"
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fleet_name() -> str:
    manifest = yaml.safe_load((ROOT / "fleet" / "manifest.yaml").read_text())
    return str(manifest["lab"])


def tool_commit() -> str:
    proc = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    if proc.returncode != 0:
        raise SystemExit(proc.stderr.strip() or "git rev-parse HEAD failed")
    return proc.stdout.strip()


def load_observed_at(path: Path) -> str:
    text = path.read_text() if path.is_file() else ""
    line = text.splitlines()[0].strip() if text.strip() else ""
    if not OBSERVED_AT_RE.fullmatch(line):
        raise SystemExit(f"observed-at file is not ISO 8601 UTC: {path}")
    return line


def zero_note(feed_newest: str) -> str:
    return "no published advisory as of " + feed_newest


def advisories_for(candidates: list[str]) -> list[dict]:
    """Union of non-withdrawn npm openclaw advisories across candidates."""
    index = build_index()
    chosen: dict[str, dict] = {}
    covered: dict[str, list[str]] = {}
    for version in candidates:
        rows, _withdrawn = _rows_for_version(index, version)
        for advisory in rows:
            ghsa_id = advisory.get("ghsa_id")
            if not isinstance(ghsa_id, str) or not ghsa_id:
                continue
            chosen.setdefault(ghsa_id, advisory)
            hits = covered.setdefault(ghsa_id, [])
            if version not in hits:
                hits.append(version)
    listed = []
    for ghsa_id in sorted(chosen):
        hits = covered[ghsa_id]
        applies = None if len(hits) == len(candidates) else hits
        listed.append(
            {
                "applies_to": applies,
                "ghsa_id": ghsa_id,
                "severity": chosen[ghsa_id].get("severity"),
                "url": "https://github.com/advisories/" + ghsa_id,
            }
        )
    return listed


def _severity_count(advisories: list[dict], severity: str) -> int:
    return sum(1 for advisory in advisories if advisory.get("severity") == severity)


MIN_CLEAR_DEFINITION = (
    "earliest release from which no critical or high published advisory matches"
)


def build_report(
    scan: dict,
    *,
    observed_at: str,
    commit: str,
    feed_sha: str,
    fleet: str,
) -> dict:
    feed_newest = FEED_NEWEST
    installs = []
    for item in scan["installs"]:
        candidates = [str(version) for version in (item.get("candidates") or [])]
        advisories = advisories_for(candidates)
        critical = _severity_count(advisories, "critical")
        high = _severity_count(advisories, "high")
        count = len(advisories)
        version = item.get("version")
        credential_names = sorted(str(name) for name in (item.get("credentials") or []))
        mcp_servers = [str(name) for name in (item.get("mcp_servers") or [])]
        installs.append(
            {
                "advisories": advisories,
                "advisory_count": count,
                "advisory_note": "" if count else zero_note(feed_newest),
                "auto_approve": item.get("auto_approve"),
                "candidates": candidates,
                "credential_count": len(credential_names),
                "credential_names": credential_names,
                "credential_sources": [str(path) for path in (item.get("config_paths") or [])],
                "critical": critical,
                "files_read": [str(path) for path in (item.get("files_read") or [])],
                "high": high,
                "id": item["id"],
                "matched_files": [str(path) for path in (item.get("matched_files") or [])],
                "mcp_count": len(mcp_servers),
                "mcp_servers": mcp_servers,
                "verdict": item.get("verdict"),
                "version": version if version else None,
            }
        )
    clearing = min_clearing_version()
    if not clearing:
        raise SystemExit("min_clearing_version is empty")
    clearing_rows = advisories_for([clearing])
    if _severity_count(clearing_rows, "critical") or _severity_count(clearing_rows, "high"):
        raise SystemExit("min_clear_release still matches a critical or high advisory")
    medium_ids = [row["ghsa_id"] for row in clearing_rows if row.get("severity") == "medium"]
    by_id = {item["id"]: item for item in installs}
    projected = [
        {
            "id": item["id"],
            "version": item["version"],
            "vulnerable": item["critical"] + item["high"] > 0,
            "credentials": list(item["credential_names"]),
            "auto_approve": bool(item["auto_approve"]),
            "cves": [],
        }
        for item in installs
    ]
    steps = fix_order(projected)
    patch = []
    rotate = []
    for step in steps:
        if step["action"] == "patch":
            source = by_id[step["install"]]
            patch.append(
                {
                    "auto_approve": source["auto_approve"],
                    "candidates": list(source["candidates"]),
                    "credential_count": step["credential_count"],
                    "install": step["install"],
                    "min_clear_release": clearing,
                    "version": source["version"],
                }
            )
        elif step["action"] == "rotate":
            rotate.append(
                {
                    "credential": step["credential"],
                    "installs": list(step["installs"]),
                    "reach": step["reach"],
                }
            )
    mock = summary_from_scan(scan)
    data = {
        "fix_order": {
            "min_clear_medium_count": len(medium_ids),
            "min_clear_medium_ids": medium_ids,
            "min_clear_release": clearing,
            "patch": patch,
            "rotate": rotate,
        },
        "header": {
            "feed_newest": feed_newest,
            "feed_sha256": feed_sha,
            "fleet": fleet,
            "observed_at": observed_at,
            "rule": RULE,
            "tool_commit": commit,
        },
        "installs": installs,
        "summary": {
            "agent365_label": "Agent 365",
            "critical_or_high_count": sum(1 for item in installs if item["critical"] + item["high"] > 0),
            "exact_count": sum(1 for item in installs if item["verdict"] == "exact"),
            "install_count": len(installs),
            "mock_blank_or_stale": mock["no_usable_version"],
            "mock_registry_rows": mock["registry_sees"],
            "range_count": sum(1 for item in installs if item["verdict"] == "range"),
            "unknown_count": sum(1 for item in installs if item["verdict"] == "unknown"),
            "zero_advisory_count": sum(1 for item in installs if item["advisory_count"] == 0),
        },
    }
    section = load_npm_section(scan)
    if section is not None:
        data["npm_audit"] = section
    return data


def _id_cell(ids: list) -> str:
    if not ids:
        return "0"
    return f"{len(ids)} ({', '.join(str(item) for item in ids)})"


def _cell(value: object) -> str:
    if value is None:
        return ""
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, list):
        return ", ".join(str(item) for item in value)
    return str(value)


def min_clear_sentence(order: dict, feed_newest: str) -> str:
    """Numbers come from report-data.json. The definition names the critical/high cutoff."""
    return (
        f"min_clear_release ({MIN_CLEAR_DEFINITION}, as of {feed_newest}) "
        f"is {order['min_clear_release']}; "
        f"it still matches {order['min_clear_medium_count']} medium advisories."
    )


def _match_sentence(install: dict, feed_newest: str) -> str:
    if install["advisory_count"] == 0:
        return str(install["advisory_note"])
    return (
        f"matches {install['advisory_count']} published advisories "
        f"({install['critical']} critical, {install['high']} high) as of {feed_newest}"
    )


def render_npm_audit(section: dict) -> list[str]:
    """Optional comparison. Counts and the two dates only."""
    lines = [
        "## npm audit comparison",
        "",
        "| version | npm query date | feed newest | npm audit | ClawScore | overlap | GitHub-DB-not-returned | repo-only | npm-only |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    feed_newest = section["feed_newest"]
    for row in section["rows"]:
        lines.append(
            "| {version} | {day} | {feed} | {npm} | {claw} | {overlap} | {db} | {repo} | {npm_only} |".format(
                version=row["version"],
                day=str(row["npm_audit_date_utc"])[:10],
                feed=feed_newest,
                npm=row["npm_audit"],
                claw=row["clawscore"],
                overlap=row["overlap"],
                db=_id_cell(row["db_not_npm"]),
                repo=row["repo_only"],
                npm_only=_id_cell(row["npm_only"]),
            )
        )
    lines.append("")
    for row in section["rows"]:
        lines.append(sentence_for(row, feed_newest))
        lines.append("")
    return lines


def render_markdown(data: dict) -> str:
    header = data["header"]
    summary = data["summary"]
    order = data["fix_order"]
    lines: list[str] = []
    lines.append("# ClawScore fleet report")
    lines.append("")
    lines.append("## Header")
    lines.append("")
    lines.append(f"Fleet: {header['fleet']}")
    lines.append(f"Observed at: {header['observed_at']}")
    lines.append(f"Feed newest: {header['feed_newest']}")
    lines.append(f"Feed sha256: {header['feed_sha256']}")
    lines.append(f"Tool commit: {header['tool_commit']}")
    lines.append(f"Rule: {header['rule']}")
    lines.append("")
    lines.append("## Fleet summary")
    lines.append("")
    lines.append(
        f"Installs: {summary['install_count']}. "
        f"Exact: {summary['exact_count']}. "
        f"Range: {summary['range_count']}. "
        f"Unknown: {summary['unknown_count']}. "
        f"Critical or high: {summary['critical_or_high_count']}. "
        f"Zero advisory: {summary['zero_advisory_count']}."
    )
    lines.append("")
    label = summary["agent365_label"]
    lines.append(
        f"This {label} comparison is a local mock: "
        f"the local mock registry lists {summary['mock_registry_rows']} rows, "
        f"of which {summary['mock_blank_or_stale']} have a blank or stale mock version."
    )
    lines.append("")
    lines.append(
        "| id | verdict | version | candidates | advisory_count | critical | high | credential_count | auto_approve | mcp_count |"
    )
    lines.append("| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |")
    for install in data["installs"]:
        lines.append(
            "| {id} | {verdict} | {version} | {candidates} | {advisory_count} | {critical} | {high} | {names} | {auto} | {mcp} |".format(
                id=install["id"],
                verdict=_cell(install["verdict"]),
                version=_cell(install["version"]),
                candidates=_cell(install["candidates"]),
                advisory_count=install["advisory_count"],
                critical=install["critical"],
                high=install["high"],
                names=install["credential_count"],
                auto=_cell(install["auto_approve"]),
                mcp=install["mcp_count"],
            )
        )
    lines.append("")
    if data.get("npm_audit"):
        lines.extend(render_npm_audit(data["npm_audit"]))
    lines.append("## Fix order")
    lines.append("")
    lines.append(
        "Patch installs that match at least one critical or high advisory, "
        "then rotate credential names ordered by reach. "
        + min_clear_sentence(order, header["feed_newest"])
    )
    lines.append("")
    lines.append("| install | version | candidates | min_clear_release | credential_count | auto_approve |")
    lines.append("| --- | --- | --- | --- | --- | --- |")
    for row in order["patch"]:
        lines.append(
            "| {install} | {version} | {candidates} | {release} | {count} | {auto} |".format(
                install=row["install"],
                version=_cell(row["version"]),
                candidates=_cell(row["candidates"]),
                release=row["min_clear_release"],
                count=row["credential_count"],
                auto=_cell(row["auto_approve"]),
            )
        )
    lines.append("")
    lines.append("| credential | reach | installs |")
    lines.append("| --- | --- | --- |")
    for row in order["rotate"]:
        lines.append(
            f"| {row['credential']} | {row['reach']} | {_cell(row['installs'])} |"
        )
    lines.append("")
    lines.append("## Per-install detail")
    lines.append("")
    for install in data["installs"]:
        lines.append(f"### {install['id']}")
        lines.append("")
        lines.append(f"Verdict: { _cell(install['verdict']) }")
        lines.append(f"Version: {_cell(install['version'])}")
        lines.append(f"Candidates: {_cell(install['candidates'])}")
        lines.append(f"Files read: {_cell(install['files_read'])}")
        lines.append(f"Matched files: {_cell(install['matched_files'])}")
        lines.append("")
        lines.append(_match_sentence(install, header["feed_newest"]))
        lines.append("")
        names = _cell(install["credential_names"]) or "(none)"
        sources = _cell(install["credential_sources"]) or "(none)"
        lines.append(
            f"Credential names: {names}. credential reach is lab-tested only. Sources: {sources}."
        )
        lines.append(f"auto_approve: {_cell(install['auto_approve'])}")
        lines.append(f"mcp_servers: {_cell(install['mcp_servers']) or '(none)'}")
        lines.append("")
        lines.append("Critical and high advisories:")
        lines.append("")
        shown = [
            advisory
            for advisory in install["advisories"]
            if advisory.get("severity") in {"critical", "high"}
        ]
        if not shown:
            lines.append("(none)")
        for advisory in shown:
            extra = ""
            if advisory.get("applies_to"):
                extra = " applies_to " + _cell(advisory["applies_to"])
            lines.append(
                f"- {advisory['ghsa_id']} severity {advisory['severity']} {advisory['url']}{extra}"
            )
        lines.append("")
    lines.append("## Method and limits")
    lines.append("")
    lines.append(
        "An install with matches is described as matches N published advisories "
        "(C critical, H high) as of the header feed_newest, using that install's "
        "advisory_count, critical, and high fields. An install with zero matches "
        "uses its advisory_note."
    )
    lines.append("")
    lines.append(
        "Credential reach is lab-tested only. The names were read from the planted "
        "lab paths listed in credential_sources. This report does not measure customer hosts."
    )
    lines.append("")
    lines.append(
        f"This {summary['agent365_label']} comparison is a local mock, and published-schema limits are "
        "cited in inputs/rea-narrower-gap/CLAIMS.md."
    )
    lines.append("")
    lines.append("## Appendix")
    lines.append("")
    for install in data["installs"]:
        lines.append(f"### {install['id']} advisory ids")
        lines.append("")
        if not install["advisories"]:
            lines.append("(none)")
        for advisory in install["advisories"]:
            lines.append(advisory["ghsa_id"])
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def write_pdf(out_dir: Path) -> None:
    status = out_dir / "pdf-status.txt"
    pdf_path = out_dir / "report.pdf"
    pandoc = shutil.which("pandoc")
    if not pandoc:
        if pdf_path.exists():
            pdf_path.unlink()
        status.write_text("pandoc not available; report.pdf not written\n")
        return
    proc = subprocess.run(
        [pandoc, str(out_dir / "report.md"), "-o", str(pdf_path)],
        capture_output=True,
        text=True,
        check=False,
    )
    if proc.returncode != 0 or not pdf_path.is_file():
        if pdf_path.exists():
            pdf_path.unlink()
        status.write_text("pandoc failed; report.pdf not written\n")
        return
    digest = hashlib.sha256(pdf_path.read_bytes()).hexdigest()
    status.write_text(f"report.pdf sha256 {digest}\n")


def write_report(scan_path: Path, out_dir: Path, observed_at_path: Path | None = None) -> dict:
    observed_path = observed_at_path or (ROOT / "evidence" / "lab-scan-observed-at.txt")
    scan = json.loads(scan_path.read_text())
    data = build_report(
        scan,
        observed_at=load_observed_at(observed_path),
        commit=tool_commit(),
        feed_sha=feed_sha256(),
        fleet=fleet_name(),
    )
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "report-data.json").write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    markdown = render_markdown(data)
    (out_dir / "report.md").write_text(markdown)
    if out_dir.resolve() == (ROOT / "evidence" / "report").resolve():
        (out_dir / "sample-report.md").write_text(markdown)
    write_pdf(out_dir)
    return data


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="python3 -m clawscore_fleet.report")
    parser.add_argument("--scan", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--observed-at")
    args = parser.parse_args(argv)
    observed = Path(args.observed_at) if args.observed_at else None
    data = write_report(Path(args.scan), Path(args.out), observed)
    print(f"wrote {args.out} installs={len(data['installs'])}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
