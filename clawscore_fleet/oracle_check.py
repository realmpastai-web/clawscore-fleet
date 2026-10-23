"""Compare report-data.json advisory ids to Hark's oracle. See docs/written-report.md."""

from __future__ import annotations

import json
import sys
from pathlib import Path

from clawscore_fleet.lab_key import load_feed, load_oracle
from clawscore_fleet.versions import ROOT


def check_report(data: dict, feed: list) -> tuple[list[str], list[str]]:
    """Return (log lines, failure lines). Failure lines are empty when every install agrees."""
    oracle = load_oracle()
    cache: dict[str, set[str]] = {}

    def ids_for(version: str) -> set[str]:
        found = cache.get(version)
        if found is None:
            found = {ghsa_id for ghsa_id, _severity in oracle.advisories(feed, version)}
            cache[version] = found
        return found

    lines = []
    failures = []
    ok = 0
    for install in data["installs"]:
        candidates = list(install.get("candidates") or [])
        want: set[str] = set()
        for version in candidates:
            want |= ids_for(version)
        got = [advisory["ghsa_id"] for advisory in install.get("advisories") or []]
        got_set = set(got)
        extra = sorted(got_set - want)
        missing = sorted(want - got_set)
        match = got_set == want and got == sorted(got)
        applies_bad = []
        for advisory in install.get("advisories") or []:
            covered = [version for version in candidates if advisory["ghsa_id"] in ids_for(version)]
            expected = None if len(covered) == len(candidates) else covered
            if advisory.get("applies_to") != expected:
                applies_bad.append(advisory["ghsa_id"])
        if match and not applies_bad:
            ok += 1
            lines.append(f"{install['id']} ids {len(got_set)} oracle {len(want)} ok")
        else:
            lines.append(
                f"{install['id']} ids {len(got_set)} oracle {len(want)} "
                f"extra {extra[:5]} missing {missing[:5]} applies_to {applies_bad[:5]}"
            )
            failures.append(install["id"])
    range_ids = []
    for install in data["installs"]:
        if install["id"] in {"claw-10", "claw-11", "claw-12", "claw-13"}:
            range_ids.append(len(install.get("advisories") or []))
    range_value = range_ids[0] if range_ids and all(count == range_ids[0] for count in range_ids) else None
    total = len(data["installs"])
    lines.append(f"oracle-check {ok}/{total} range={range_value}")
    if ok != total or range_value != 222 or failures:
        if not failures and range_value != 222:
            failures.append("range")
    return lines, failures


def main(argv: list[str] | None = None) -> int:
    path = ROOT / "evidence" / "report" / "report-data.json"
    if argv:
        path = Path(argv[0])
    data = json.loads(path.read_text())
    lines, failures = check_report(data, load_feed())
    text = "\n".join(lines) + "\n"
    log_path = path.parent / "oracle-check.log"
    log_path.write_text(text)
    sys.stdout.write(text)
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
