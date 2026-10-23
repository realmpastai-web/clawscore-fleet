"""Written report: oracle agreement, wording, provenance, and the holdout fixture."""

from __future__ import annotations

import filecmp
import hashlib
import json
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import yaml

from clawscore_fleet.lab_key import build_lab_key, load_feed, score_lab
from clawscore_fleet.oracle_check import check_report
from clawscore_fleet.holdout_lab import report_or_refuse
from clawscore_fleet.report import (
    MIN_CLEAR_DEFINITION,
    _cell,
    advisories_for,
    build_report,
    feed_sha256,
    fleet_name,
    load_observed_at,
    min_clear_sentence,
    render_markdown,
    tool_commit,
    write_report,
)
from clawscore_fleet.summary import summary_from_scan
from clawscore_fleet.versions import NO_ADVISORY_WORDING, ROOT

BANNED = [
    r"\bsafe\b",
    r"not vulnerable",
    r"\bsecure[ds]?\b",
    r"no vulnerabilit",
    r"known vulnerabilit",
    r"\bclean\b",
    r"\bprotected\b",
    r"guarantee",
    r"risk[- ]free",
    r"fully patched",
    r"\bimmune\b",
]
SCAN = ROOT / "evidence" / "scan.json"
OBSERVED = ROOT / "evidence" / "lab-scan-observed-at.txt"
MANIFEST = ROOT / "fixtures" / "holdout-example.json"


def _report():
    scan = json.loads(SCAN.read_text())
    data = build_report(
        scan,
        observed_at=load_observed_at(OBSERVED),
        commit=tool_commit(),
        feed_sha=feed_sha256(),
        fleet=fleet_name(),
    )
    return scan, data, render_markdown(data)


def _banned(text: str) -> list[str]:
    hits = []
    for pattern in BANNED:
        hits.extend(match.group(0) for match in re.finditer(pattern, text, re.I))
    return hits


class ReportTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.scan, cls.data, cls.markdown = _report()
        cls.feed = load_feed()

    def test_a1_oracle_agreement(self) -> None:
        lines, failures = check_report(self.data, self.feed)
        self.assertEqual(failures, [], "\n".join(lines))
        joined = "\n".join(lines)
        self.assertIn("oracle-check 30/30 range=222", joined)
        for ident in ("claw-10", "claw-11", "claw-12", "claw-13"):
            row = next(item for item in self.data["installs"] if item["id"] == ident)
            self.assertEqual(row["candidates"], ["2026.4.7-1", "2026.4.8"])
            self.assertEqual(len(row["advisories"]), 222)
            partial = [item for item in row["advisories"] if item["applies_to"]]
            self.assertEqual(len(partial), 20)
            self.assertTrue(all(item["applies_to"] == ["2026.4.7-1"] for item in partial))

    def test_banned_words(self) -> None:
        self.assertEqual(_banned(self.markdown), [])
        zeros = [item for item in self.data["installs"] if item["advisory_count"] == 0]
        self.assertGreaterEqual(len(zeros), 1)
        for item in zeros:
            self.assertEqual(item["advisory_note"], NO_ADVISORY_WORDING)
            self.assertIn(item["advisory_note"], self.markdown)
        self.assertIn("credential reach is lab-tested only", self.markdown)
        self.assertIn("This Agent 365 comparison is a local mock", self.markdown)
        self.assertIn("inputs/rea-narrower-gap/CLAIMS.md", self.markdown)

    def test_no_credential_values(self) -> None:
        pool = json.loads((ROOT / "fleet" / "secrets-pool.json").read_text())
        blob = self.markdown + json.dumps(self.data)
        leaked = [name for name, value in pool.items() if value and value in blob]
        self.assertEqual(leaked, [])

    def test_report_numbers(self) -> None:
        blob = json.dumps(self.data)
        for token in re.findall(r"\d+", self.markdown):
            self.assertIn(token, blob, token)
        for token in re.findall(r"GHSA-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}", self.markdown):
            self.assertIn(token, blob)
        mutated = json.loads(blob)
        mutated["installs"][0]["advisory_count"] += 1
        self.assertNotEqual(render_markdown(mutated), self.markdown)

    def test_determinism(self) -> None:
        _scan, again, markdown = _report()
        self.assertEqual(again, self.data)
        self.assertEqual(markdown, self.markdown)
        with tempfile.TemporaryDirectory() as tmp:
            left = Path(tmp) / "a"
            right = Path(tmp) / "b"
            write_report(SCAN, left, OBSERVED)
            write_report(SCAN, right, OBSERVED)
            self.assertTrue(filecmp.cmp(left / "report-data.json", right / "report-data.json", shallow=False))
            self.assertTrue(filecmp.cmp(left / "report.md", right / "report.md", shallow=False))

    def test_lab_key_scores_pass(self) -> None:
        manifest = yaml.safe_load((ROOT / "fleet" / "manifest.yaml").read_text())
        key = build_lab_key(manifest, self.feed)
        with tempfile.TemporaryDirectory() as tmp:
            directory = Path(tmp)
            key_path = directory / "lab-key.json"
            data_path = directory / "report-data.json"
            markdown_path = directory / "report.md"
            key_path.write_text(json.dumps(key, indent=2, sort_keys=True) + "\n")
            data_path.write_text(json.dumps(self.data, indent=2, sort_keys=True) + "\n")
            markdown_path.write_text(self.markdown)
            proc = score_lab(key_path, data_path, markdown_path, ROOT / "fleet" / "secrets-pool.json")
        self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)
        self.assertIn("RESULT PASS", proc.stdout)

    def test_mock_counts_come_from_the_scan(self) -> None:
        mock = summary_from_scan(self.scan)
        self.assertEqual(self.data["summary"]["mock_registry_rows"], mock["registry_sees"])
        self.assertEqual(self.data["summary"]["mock_blank_or_stale"], mock["no_usable_version"])
        self.assertEqual(self.data["header"]["feed_sha256"], "27b020df70c9896d7b94280ad0646dc69ef4d27e504d81bc6719dedcb6446034")
        self.assertEqual(self.data["fix_order"]["min_clear_release"], "2026.8.1")
        self.assertEqual(self.data["summary"]["install_count"], 30)
        self.assertEqual(self.data["summary"]["range_count"], 4)

    def test_min_clear_sentence_uses_medium_count_from_data(self) -> None:
        order = self.data["fix_order"]
        sentence = min_clear_sentence(order, self.data["header"]["feed_newest"])
        self.assertIn(sentence, self.markdown)
        self.assertIn(MIN_CLEAR_DEFINITION, sentence)
        self.assertIn(f"as of {self.data['header']['feed_newest']}", sentence)
        self.assertIn(f"is {order['min_clear_release']}", sentence)
        self.assertIn(f"it still matches {order['min_clear_medium_count']} medium advisories.", sentence)
        rows = advisories_for([order["min_clear_release"]])
        medium = [row["ghsa_id"] for row in rows if row.get("severity") == "medium"]
        self.assertEqual(order["min_clear_medium_count"], len(medium))
        self.assertEqual(order["min_clear_medium_ids"], medium)
        self.assertEqual(sum(1 for row in rows if row.get("severity") == "critical"), 0)
        self.assertEqual(sum(1 for row in rows if row.get("severity") == "high"), 0)

    def test_summary_table_uses_count_columns(self) -> None:
        header = (
            "| id | verdict | version | candidates | advisory_count | critical | high | "
            "credential_count | auto_approve | mcp_count |"
        )
        self.assertIn(header, self.markdown)
        self.assertNotIn("| credential_names |", self.markdown)
        self.assertNotIn("| mcp_servers |", self.markdown)
        for install in self.data["installs"]:
            self.assertEqual(install["credential_count"], len(install["credential_names"]))
            self.assertEqual(install["mcp_count"], len(install["mcp_servers"]))
            row = (
                f"| {install['id']} | {_cell(install['verdict'])} | {_cell(install['version'])} | "
                f"{_cell(install['candidates'])} | {install['advisory_count']} | {install['critical']} | "
                f"{install['high']} | {install['credential_count']} | {_cell(install['auto_approve'])} | "
                f"{install['mcp_count']} |"
            )
            self.assertIn(row, self.markdown)

    def test_holdout_report_refuses_dirty_tree(self) -> None:
        with self.assertRaises(SystemExit) as caught:
            report_or_refuse("abc123", " M fleet/gen_lab.py\n")
        self.assertIn("dirty", str(caught.exception))
        self.assertEqual(report_or_refuse("abc123", ""), "abc123")
        self.assertEqual(report_or_refuse("abc123", "\n"), "abc123")

    def test_holdout_example_builds_three_installs(self) -> None:
        fleet = ROOT / "fleet"
        before = _dir_digest(fleet)
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "fleet-holdout"
            proc = subprocess.run(
                [
                    sys.executable,
                    str(fleet / "gen_lab.py"),
                    "--holdout",
                    str(MANIFEST),
                    "--out",
                    str(out),
                ],
                cwd=ROOT,
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(proc.returncode, 0, proc.stderr + proc.stdout)
            plants = sorted(path.name for path in (out / "plants").glob("*.json"))
            self.assertEqual(plants, ["hold-01.json", "hold-02.json", "hold-03.json"])
            compose = yaml.safe_load((out / "compose.yaml").read_text())
            self.assertEqual(compose["name"], "clawscore-holdout")
            self.assertEqual(list(compose["services"]), ["hold-01", "hold-02", "hold-03"])
            self.assertEqual(compose["networks"]["holdnet"]["name"], "clawscore-holdout")
            self.assertTrue(compose["networks"]["holdnet"]["internal"])
            self.assertNotIn("clawscore.lab", (out / "compose.yaml").read_text())
            dockerfiles = sorted(path.name for path in (out / "images").glob("Dockerfile.*"))
            self.assertEqual(
                dockerfiles,
                ["Dockerfile.2026.1.29", "Dockerfile.2026.10.4", "Dockerfile.2026.4.22"],
            )
            for path in (out / "images").glob("Dockerfile.*"):
                text = path.read_text()
                self.assertIn("--ignore-scripts", text)
                self.assertIn("sleep", (ROOT / "fleet" / "entrypoint.sh").read_text())
            self.assertIn("../fleet/entrypoint.sh", (out / "compose.yaml").read_text())
            pool = json.loads((ROOT / "fleet" / "secrets-pool.json").read_text())
            planted = "\n".join(path.read_text() for path in (out / "plants").glob("*.json"))
            planted += (out / "compose.yaml").read_text()
            leaked = [name for name, value in pool.items() if value and value in planted]
            self.assertEqual(leaked, [])
            hold_01 = json.loads((out / "plants" / "hold-01.json").read_text())
            self.assertEqual(hold_01["stripped"], "removed")
            self.assertEqual(hold_01["env_names"], ["OPENAI_API_KEY"])
            hold_03 = json.loads((out / "plants" / "hold-03.json").read_text())
            self.assertEqual(hold_03["stripped"], "false-version")
            self.assertEqual(hold_03["false_version"], "2026.4.15")
        self.assertEqual(_dir_digest(fleet), before)


def _dir_digest(root: Path) -> str:
    digest = hashlib.sha256()
    for path in sorted(item for item in root.rglob("*") if item.is_file()):
        if "__pycache__" in path.parts or path.suffix == ".pyc":
            continue
        digest.update(path.relative_to(root).as_posix().encode())
        digest.update(path.read_bytes())
    return digest.hexdigest()


if __name__ == "__main__":
    unittest.main()
