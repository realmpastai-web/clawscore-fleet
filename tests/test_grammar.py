"""Grammar checks for the v0.2.2 key and the shared range parser.

Oracles are the frozen landscape recompute.py and regen_v023.py. Expected cells
are not copied into this file.
"""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path

from clawscore_fleet.cves import in_range
from clawscore_fleet.pkgmatch import is_openclaw_npm
from clawscore_fleet.versions import RangeSyntaxError, hark_key, parse_comparators

ROOT = Path(__file__).resolve().parents[1]


def _exec_function(path: Path, name: str, until: str) -> object:
    text = path.read_text()
    start = text.index(f"def {name}(")
    end = text.index(until, start)
    namespace = {"re": re, "json": json}
    exec(text[start:end], namespace)
    return namespace[name]


class GrammarTests(unittest.TestCase):
    def test_key_matches_v022_recompute_on_catalog_and_bounds(self) -> None:
        key = _exec_function(
            ROOT / "inputs/clawscore-v0.2.2/landscape-v0.2.2/recompute.py",
            "key",
            "def inrange(",
        )
        published = json.loads((ROOT / "inputs/landscape/versions.json").read_text())
        advisories = json.loads((ROOT / "inputs/landscape/ghsa-all.json").read_text())
        ranges = []
        for advisory in advisories:
            for entry in advisory.get("vulnerabilities") or []:
                package = entry.get("package") or {}
                rng = entry.get("vulnerable_version_range")
                if is_openclaw_npm(package, advisory.get("ghsa_id")) and rng:
                    ranges.append(rng)
        unique = sorted(set(ranges))
        bounds = sorted({bound for rng in unique for _op, bound in parse_comparators(rng)})
        self.assertEqual(len(published), 278)
        self.assertEqual(len(unique), 142)
        self.assertEqual(sum(len(parse_comparators(rng)) for rng in unique), 183)
        for version in published:
            self.assertEqual(hark_key(version), key(version), version)
        for bound in bounds:
            self.assertEqual(hark_key(bound), key(bound), bound)
        self.assertIsNotNone(hark_key("2.0.0-beta3"))

    def test_prerelease_order_and_alpha_membership(self) -> None:
        order = ["2026.5.19-alpha.1", "2026.5.19-beta.2", "2026.5.19", "2026.5.19-1"]
        keys = [hark_key(item) for item in order]
        self.assertTrue(all(item is not None for item in keys))
        self.assertEqual(keys, sorted(keys))
        self.assertEqual(hark_key("2026.1.29-beta3"), hark_key("2026.1.29-beta.3"))
        self.assertTrue(in_range("2026.5.19-alpha.1", "<= 2026.5.19-beta.2"))

    def test_unparsed_range_is_an_error(self) -> None:
        with self.assertRaises(RangeSyntaxError):
            parse_comparators("not-a-range")
        with self.assertRaises(RangeSyntaxError):
            in_range("2026.1.29", ">= 1.0.0 leftover")

    def test_space_and_ranges_match_regen_v023(self) -> None:
        source = (ROOT / "inputs/clawscore-v0.2.3-gate/regen_v023.py").read_text()
        start = source.index("def key(")
        end = source.index("R = [")
        namespace = {"re": re}
        exec(source[start:end], namespace)
        key = namespace["key"]
        comparators = namespace["comparators"]
        inrange = namespace["inrange"]
        advisories = json.loads(
            (ROOT / "inputs/clawscore-feed-csv-2026-10-17/ghsa-all.json").read_text()
        )
        versions = json.loads((ROOT / "inputs/landscape/versions.json").read_text())
        ranges = []
        for advisory in advisories:
            for entry in advisory.get("vulnerabilities") or []:
                package = entry.get("package") or {}
                rng = entry.get("vulnerable_version_range")
                if is_openclaw_npm(package, advisory.get("ghsa_id")) and rng:
                    ranges.append(rng)
        unique = sorted(set(ranges))
        space_and = []
        for rng in unique:
            parsed = comparators(rng)
            self.assertIsNotNone(parsed, rng)
            self.assertEqual([(op, bound) for op, bound in parse_comparators(rng)], parsed, rng)
            if len(parsed) > 1 and "," not in rng:
                space_and.append(rng)
        frozen = json.loads((ROOT / "inputs/clawscore-v0.2.3-gate/expected-v023.json").read_text())
        self.assertEqual(sorted(space_and), frozen["ranges"]["space_and_ranges"])
        mismatches = []
        for version in versions:
            self.assertEqual(hark_key(version), key(version), version)
            for rng in space_and:
                parsed = comparators(rng)
                if in_range(version, rng) != inrange(version, parsed):
                    mismatches.append((version, rng))
        self.assertEqual(mismatches, [])


if __name__ == "__main__":
    unittest.main()
