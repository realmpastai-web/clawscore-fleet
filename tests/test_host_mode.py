"""Unit tests for host-mode version fields, unknown rows, and merge."""

from __future__ import annotations

import csv
import io
import json
import tempfile
import unittest
from pathlib import Path

from clawscore_fleet.scan_host import (
    UNKNOWN_NOTE,
    declared_version,
    defender_csv,
    host_fix_order,
    merge_host,
    scan_host,
    version_mismatch,
)


def _install(root: Path, rel: str, version: str | None, config: dict | None = None) -> None:
    dest = root / rel
    dest.mkdir(parents=True)
    body = {"name": "openclaw"}
    if version is not None:
        body["version"] = version
    (dest / "package.json").write_text(json.dumps(body) + "\n")
    if config is not None:
        owner = root / "home" / "alice" / ".openclaw"
        owner.mkdir(parents=True, exist_ok=True)
        (owner / "openclaw.json").write_text(json.dumps(config) + "\n")


class VersionFieldTest(unittest.TestCase):
    def test_declared_version_reads_package_json_only(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            present = root / "with"
            present.mkdir()
            (present / "package.json").write_text(json.dumps({"name": "openclaw", "version": "2026.10.4"}) + "\n")
            missing = root / "without"
            missing.mkdir()
            (missing / "package.json").write_text(json.dumps({"name": "openclaw"}) + "\n")
            self.assertEqual(declared_version(present), "2026.10.4")
            self.assertIsNone(declared_version(missing))
            self.assertIsNone(declared_version(root / "absent"))

    def test_version_mismatch_is_exact_verdict_against_declared(self) -> None:
        self.assertTrue(version_mismatch("exact", "2026.1.29", "2026.10.4"))
        self.assertFalse(version_mismatch("exact", "2026.10.4", "2026.10.4"))
        self.assertFalse(version_mismatch("unknown", None, "2026.10.10-beta.1"))
        self.assertFalse(version_mismatch("range", None, "2026.4.7-1"))


class UnknownAndMergeTest(unittest.TestCase):
    def test_unknown_is_null_and_out_of_fix_order(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "host"
            out = Path(tmp) / "out"
            rel = "home/alice/.npm-global/lib/node_modules/openclaw"
            _install(
                root,
                rel,
                "2026.10.10-beta.1",
                {"env": {"OPENAI_API_KEY": "hark-canary-7f3e1c-NOT-A-REAL-TOKEN"}},
            )
            document = scan_host(root, out)
            self.assertEqual(len(document["installs"]), 1)
            row = document["installs"][0]
            self.assertEqual(row["declared_version"], "2026.10.10-beta.1")
            self.assertFalse(row["version_mismatch"])
            self.assertEqual(row["verdict"], "unknown")
            self.assertIsNone(row["version"])
            self.assertIsNone(row["vulnerable"])
            self.assertEqual(row["advisory_note"], UNKNOWN_NOTE)
            self.assertEqual(document["unidentified"], [row["id"]])
            self.assertEqual(document["fix_order"], [])
            self.assertEqual(row["credentials"], ["OPENAI_API_KEY"])
            text = (out / "scan.json").read_text()
            self.assertNotIn("hark-canary-7f3e1c-NOT-A-REAL-TOKEN", text)
            self.assertNotIn("hark-canary-7f3e1c-NOT-A-REAL-TOKEN", (out / "files-read.log").read_text())

    def test_fix_order_keeps_only_truthy_vulnerable(self) -> None:
        installs = [
            {"id": "known", "vulnerable": True, "credentials": [], "auto_approve": False, "version": "2026.1.29", "cves": ["CVE-1"]},
            {"id": "unknown", "vulnerable": None, "credentials": ["OPENAI_API_KEY"], "auto_approve": False, "version": None, "cves": []},
            {"id": "clean", "vulnerable": False, "credentials": [], "auto_approve": False, "version": "2026.10.4", "cves": []},
        ]
        steps = host_fix_order(installs)
        self.assertEqual([step["id"] for step in steps], ["known"])
        self.assertNotIn("unknown", [step.get("id") for step in steps])

    def test_merge_csv_gives_unidentified_an_empty_version_and_the_note(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            first = base / "a"
            second = base / "b"
            out = base / "out"
            first.mkdir()
            second.mkdir()
            (first / "scan.json").write_text(
                json.dumps(
                    {
                        "installs": [
                            {
                                "id": "beta",
                                "verdict": "unknown",
                                "version": None,
                                "vulnerable": None,
                                "advisory_note": UNKNOWN_NOTE,
                                "declared_version": "2026.10.10-beta.1",
                                "version_mismatch": False,
                                "candidates": [],
                                "cves": [],
                                "ghsa_ids": [],
                                "ghsa_only": [],
                                "files_read": [],
                                "credentials": [],
                                "mcp_servers": [],
                                "advisory_critical": 0,
                                "advisory_high": 0,
                            }
                        ]
                    }
                )
            )
            (second / "scan.json").write_text(
                json.dumps(
                    {
                        "installs": [
                            {
                                "id": "old",
                                "verdict": "exact",
                                "version": "2026.1.29",
                                "vulnerable": True,
                                "advisory_note": "",
                                "candidates": ["2026.1.29"],
                                "cves": ["CVE-2026-22168"],
                                "ghsa_ids": ["GHSA-test"],
                                "ghsa_only": [],
                                "files_read": ["/old/dist/build-info.json"],
                                "credentials": [],
                                "mcp_servers": [],
                                "advisory_critical": 1,
                                "advisory_high": 1,
                                "auto_approve": False,
                            }
                        ]
                    }
                )
            )
            csv_path = out / "defender.csv"
            document = merge_host([first, second], out, csv_path)
            self.assertEqual([item["id"] for item in document["installs"]], ["beta", "old"])
            self.assertEqual(document["unidentified"], ["beta"])
            self.assertEqual([step["id"] for step in document["fix_order"]], ["old"])
            rows = list(csv.DictReader(io.StringIO(csv_path.read_text())))
            by_name = {row["Agent name"]: row for row in rows}
            self.assertEqual(by_name["beta"]["Version"], "")
            self.assertIn(UNKNOWN_NOTE, csv_path.read_text())
            self.assertEqual(by_name["beta"]["Recommendations"], UNKNOWN_NOTE)
            self.assertEqual(by_name["old"]["Version"], "2026.1.29")
            self.assertEqual(defender_csv(document["installs"]).splitlines()[0], csv_path.read_text().splitlines()[0])


if __name__ == "__main__":
    unittest.main()
