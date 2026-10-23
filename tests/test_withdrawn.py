"""Withdrawn advisories are listed and not counted.

The reconciliation check compares the fleet count for one release with Hark's
repo-advisory counter. It does not require the two counts to be equal. A row
that cannot be explained from the two snapshots fails the check.
"""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from clawscore_fleet.cves import (
    affecting_advisories,
    withdrawn_covering,
)

VERSION = "2026.4.22"


class WithdrawnTests(unittest.TestCase):
    def test_withdrawn_fixture_is_not_counted(self) -> None:
        withdrawn = {
            "ghsa_id": "GHSA-test-withdrawn",
            "severity": "critical",
            "withdrawn_at": "2026-05-01T00:00:00Z",
            "vulnerabilities": [
                {
                    "package": {"ecosystem": "npm", "name": "openclaw"},
                    "vulnerable_version_range": "<= 2026.4.22",
                }
            ],
        }
        active = {
            "ghsa_id": "GHSA-test-active",
            "severity": "high",
            "withdrawn_at": None,
            "vulnerabilities": [
                {
                    "package": {"ecosystem": "npm", "name": "openclaw"},
                    "vulnerable_version_range": "<= 2026.4.22",
                }
            ],
        }
        advisories = [withdrawn, active]
        counted = affecting_advisories(advisories, VERSION)
        listed = withdrawn_covering(advisories, VERSION)
        self.assertEqual([item["ghsa_id"] for item in counted], ["GHSA-test-active"])
        self.assertEqual([item["ghsa_id"] for item in listed], ["GHSA-test-withdrawn"])
        self.assertNotIn("GHSA-test-withdrawn", [item["ghsa_id"] for item in counted])


if __name__ == "__main__":
    unittest.main()
