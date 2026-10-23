"""Package matching: casefold, npm ecosystem, and the non-npm keep-list.

Expected lines and the 17/11 delta are the recount in docs/package-matching.md.
"""

from __future__ import annotations

import copy
import json
import unittest
from collections import Counter

from clawscore_fleet.cves import _openclaw_ranges, build_index, in_range, is_withdrawn
from clawscore_fleet.feed_check import version_count_lines
from clawscore_fleet.pkgmatch import KEEP_PATH, is_openclaw_npm
from clawscore_fleet.versions import LANDSCAPE

VERSION_COUNT_LINES = [
    "version_counts withdrawn_excluded=yes",
    "2026.10.5 github_db=0 repo_only=0 osv=0",
    "2026.10.4 github_db=0 repo_only=0 osv=0",
    "2026.6.10 github_db=0 repo_only=58 osv=0",
    "2026.4.22 github_db=68 repo_only=80 osv=67",
]
DROP = ("GHSA-2j9j-gf59-p4p5", "GHSA-mmpf-jwf4-h3qv")
KEEP_NPM = "GHSA-w7j5-j98m-w679"
KEEP_LIST = "GHSA-25gx-x37c-7pph"
CAPITAL = "GHSA-2j8v-hwgc-x698"


def _name_only_ids(advisories: list[dict], version: str) -> set[str]:
    """Pre-change predicate: casefolded name, no ecosystem check."""
    found = set()
    for advisory in advisories:
        if is_withdrawn(advisory):
            continue
        ghsa_id = advisory.get("ghsa_id")
        for entry in advisory.get("vulnerabilities") or []:
            package = entry.get("package") or {}
            rng = entry.get("vulnerable_version_range")
            if str(package.get("name") or "").casefold() != "openclaw" or not rng:
                continue
            if in_range(version, str(rng)):
                found.add(ghsa_id)
                break
    return found


class PackageMatchTests(unittest.TestCase):
    def test_casefold_matches_capital_o(self) -> None:
        package = {"ecosystem": "npm", "name": "Openclaw"}
        self.assertTrue(is_openclaw_npm(package, CAPITAL))
        lowered = {"ecosystem": "npm", "name": "openclaw"}
        self.assertTrue(is_openclaw_npm(lowered, CAPITAL))
        self.assertTrue(is_openclaw_npm({"ecosystem": "NPM", "name": "OpenClaw"}, None))

    def test_ecosystem_check_rejects_swift_and_other(self) -> None:
        swift = {"ecosystem": "swift", "name": "openclaw"}
        other = {"ecosystem": "other", "name": "openclaw"}
        self.assertFalse(is_openclaw_npm(swift, "GHSA-2j9j-gf59-p4p5"))
        self.assertFalse(is_openclaw_npm(other, "GHSA-mmpf-jwf4-h3qv"))
        self.assertFalse(is_openclaw_npm(other, KEEP_NPM))

    def test_keep_list_has_four_columns(self) -> None:
        lines = [
            line
            for line in KEEP_PATH.read_text().splitlines()
            if line.strip() and not line.startswith("#")
        ]
        self.assertEqual(
            lines[0].split("\t"),
            ["ghsa_id", "package/ecosystem", "decision", "evidence"],
        )
        cols = lines[1].split("\t")
        self.assertEqual(len(cols), 4)
        self.assertEqual(cols[0], KEEP_LIST)
        self.assertEqual(cols[1], "openclaw/other")
        self.assertEqual(cols[2], "keep")
        self.assertIn("ghsa-all.json:65302", cols[3])
        self.assertIn("6747882e3f2e1485695a2d4dacd73bddfccd4cd49c2e14ddc090774210f5dd31", cols[3])
        self.assertNotIn("not repeated", cols[3])

    def test_keep_list_matches_non_npm_25gx(self) -> None:
        other = {"ecosystem": "other", "name": "openclaw"}
        self.assertTrue(is_openclaw_npm(other, KEEP_LIST))
        self.assertFalse(is_openclaw_npm(other, "GHSA-not-on-keep-list"))

    def test_version_count_lines_unchanged(self) -> None:
        self.assertEqual(version_count_lines(), VERSION_COUNT_LINES)

    def test_ghsa_2j8v_covers_2026_4_22_not_2026_5_18(self) -> None:
        index = build_index()
        covered = {item.get("ghsa_id") for item in index["per_version"]["2026.4.22"]}
        later = {item.get("ghsa_id") for item in index["per_version"]["2026.5.18"]}
        self.assertIn(CAPITAL, covered)
        self.assertNotIn(CAPITAL, later)
        advisories = json.loads((LANDSCAPE / "ghsa-all.json").read_text())
        original = next(item for item in advisories if item.get("ghsa_id") == CAPITAL)
        lowered = copy.deepcopy(original)
        for entry in lowered.get("vulnerabilities") or []:
            package = entry.get("package") or {}
            if isinstance(package.get("name"), str):
                package["name"] = package["name"].casefold()
        ranges = _openclaw_ranges(lowered)
        self.assertTrue(any(in_range("2026.4.22", rng) for rng in ranges))
        self.assertFalse(any(in_range("2026.5.18", rng) for rng in ranges))
        self.assertEqual(original["vulnerabilities"][0]["package"]["name"], "Openclaw")

    def test_attachment_of_cited_ids(self) -> None:
        index = build_index()
        by_id = {record["ghsa_id"]: record for record in index["records"]}
        self.assertEqual(by_id["GHSA-2j9j-gf59-p4p5"]["versions"], [])
        self.assertEqual(by_id["GHSA-mmpf-jwf4-h3qv"]["versions"], [])
        self.assertGreater(len(by_id[KEEP_LIST]["versions"]), 0)
        self.assertGreater(len(by_id[KEEP_NPM]["versions"]), 0)
        advisories = json.loads((LANDSCAPE / "ghsa-all.json").read_text())
        w7j5 = next(item for item in advisories if item.get("ghsa_id") == KEEP_NPM)
        package = w7j5["vulnerabilities"][0]["package"]
        self.assertEqual(package["ecosystem"], "npm")
        self.assertTrue(is_openclaw_npm(package, KEEP_NPM))
        gx = next(item for item in advisories if item.get("ghsa_id") == KEEP_LIST)
        self.assertEqual(gx["vulnerabilities"][0]["package"]["ecosystem"], "npm")
        self.assertIn(KEEP_LIST, {item.get("ghsa_id") for item in index["per_version"]["2026.2.19-2"]})
        self.assertNotIn(KEEP_LIST, {item.get("ghsa_id") for item in index["per_version"]["2026.2.21"]})

    def test_version_deltas(self) -> None:
        index = build_index()
        buckets: Counter[int] = Counter()
        lines = ["version\tdelta\tlost"]
        for version in index["stable"]:
            new_ids = {item.get("ghsa_id") for item in index["per_version"][version]}
            old_ids = _name_only_ids(index["advisories"], version)
            lost = sorted(old_ids - new_ids)
            gained = sorted(new_ids - old_ids)
            if not lost and not gained:
                continue
            delta = len(new_ids) - len(old_ids)
            buckets[delta] += 1
            lines.append(f"{version}\t{delta}\t{','.join(lost)}")
            self.assertEqual(gained, [])
            self.assertTrue(set(lost) <= set(DROP))
        print("\n".join(lines))
        print(f"buckets {dict(buckets)} versions {sum(buckets.values())}")
        self.assertEqual(dict(buckets), {-2: 17, -1: 11})
        self.assertEqual(sum(buckets.values()), 28)


if __name__ == "__main__":
    unittest.main()
