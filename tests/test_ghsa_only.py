"""Unit tests for GHSA-only matching, post-release order, and snapshot refusal."""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from clawscore_fleet.cves import in_range
from clawscore_fleet.fixtures.idle_linux import LAYOUTS, build_global_layout
from clawscore_fleet.ghsa_only import (
    defender_claim,
    for_version,
    frozen_task_claim,
    load_snapshot,
    measured_readme_claim,
    semver_events_cover,
)
from clawscore_fleet.idle_linux import discover_all
from clawscore_fleet.versions import ROOT, hark_key


class GhsaOnlyTest(unittest.TestCase):
    def test_sha_mismatch_refuses(self) -> None:
        with tempfile.TemporaryDirectory(prefix="clawscore-ghsa-sha-") as tmp:
            osv = Path(tmp) / "osv.json"
            snap = Path(tmp) / "OSV_SNAPSHOT.json"
            osv.write_text("[]\n")
            snap.write_text(json.dumps({"sha256": "0" * 64}) + "\n")
            with self.assertRaises(SystemExit) as caught:
                load_snapshot(osv, snap)
        self.assertIn("sha256 mismatch", str(caught.exception))

    def test_2026_4_7_gap_ids(self) -> None:
        self.assertFalse(in_range("2026.4.7", "<= 2026.4.2"))
        rows = {item["id"]: item["status"] for item in for_version("2026.4.7")}
        self.assertEqual(rows["GHSA-gfmx-pph7-g46x"], "possibly_affected")
        self.assertEqual(rows["GHSA-jf56-mccx-5f3f"], "possibly_affected")
        self.assertEqual(rows["GHSA-w9j9-w4cp-6wgr"], "affected")
        ids = [item["id"] for item in for_version("2026.4.7")]
        self.assertEqual(ids, sorted(ids))

    def test_2026_4_7_1_orders_as_post_release(self) -> None:
        self.assertLess(hark_key("2026.4.7"), hark_key("2026.4.7-1"))
        self.assertLess(hark_key("2026.4.7-1"), hark_key("2026.4.8"))
        # OSV SEMVER would call 2026.4.7-1 a prerelease and include it below the fix.
        events = [{"introduced": "0"}, {"fixed": "2026.4.7"}]
        self.assertFalse(semver_events_cover("2026.4.7-1", events))
        self.assertTrue(semver_events_cover("2026.4.6", events))
        rows = {item["id"]: item["status"] for item in for_version("2026.4.7-1")}
        self.assertEqual(rows["GHSA-gfmx-pph7-g46x"], "possibly_affected")
        self.assertEqual(rows["GHSA-jf56-mccx-5f3f"], "possibly_affected")
        self.assertEqual(rows["GHSA-w9j9-w4cp-6wgr"], "affected")

    def test_fixture_versions_match_pinned_expected(self) -> None:
        expected = json.loads((ROOT / "inputs" / "clawscore-ghsa-only" / "expected-ghsa-only.json").read_text())
        for host in expected["fixture_hosts"]:
            got = {item["id"]: item["status"] for item in for_version(host["version"])}
            self.assertEqual(got, host["expected"], host["version"])

    def test_global_layout_version_comes_from_discovery(self) -> None:
        with tempfile.TemporaryDirectory(prefix="clawscore-ghsa-fx-") as tmp:
            root = Path(tmp) / "host"
            build_global_layout(root, "2026.4.7")
            found = [row for row in discover_all(root) if row.get("install") == LAYOUTS["L1"]]
        self.assertEqual(len(found), 1)
        self.assertEqual(found[0]["resolved_version"], "2026.4.7")
        self.assertEqual(found[0]["version_source"], "package.json")

    def test_defender_claim_avoids_forbidden_wording(self) -> None:
        claim = defender_claim()
        lowered = claim.lower()
        self.assertNotIn("container", lowered)
        self.assertNotIn("agent 365", lowered)
        self.assertNotIn("can't show non-cve", lowered)
        self.assertIn("tvm-software-inventory", claim)

    def test_measured_claim_matches_frozen_task_sentence(self) -> None:
        self.assertEqual(measured_readme_claim(), frozen_task_claim())


if __name__ == "__main__":
    unittest.main()
