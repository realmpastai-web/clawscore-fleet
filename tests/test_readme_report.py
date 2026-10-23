"""README.md stays a render of evidence/verify-report.json."""

from __future__ import annotations

import json
import unittest

from clawscore_fleet.render_readme import ROOT, readme_drift


class ReadmeReportTest(unittest.TestCase):
    def test_committed_readme_matches_report(self) -> None:
        report = json.loads((ROOT / "evidence" / "verify-report.json").read_text())
        readme = (ROOT / "README.md").read_text()
        self.assertEqual(readme_drift(readme, report), "")

    def test_scratch_figure_does_not_match(self) -> None:
        report = json.loads((ROOT / "evidence" / "verify-report.json").read_text())
        readme = (ROOT / "README.md").read_text()
        scratch = readme.replace("116 of 116", "115 of 115", 1)
        self.assertNotEqual(scratch, readme)
        drift = readme_drift(scratch, report)
        self.assertNotEqual(drift, "")
        self.assertIn("115 of 115", drift)
