"""npm audit section: frozen brief replay, disjoint parts, wording, tamper refusal."""

from __future__ import annotations

import hashlib
import json
import re
import shutil
import tempfile
import unittest
from pathlib import Path

from clawscore_fleet.npm_audit import (
    ENDPOINT,
    classify,
    clawscore_ids,
    distinct_versions,
    lab_versions,
    load_context,
    load_npm_section,
    load_response,
    parse_npm_ids,
    report_lines,
    request_body,
    score_versions,
    sentence_for,
)
from clawscore_fleet.report import build_report, feed_sha256, fleet_name, load_observed_at, render_markdown, render_npm_audit, tool_commit
from clawscore_fleet.versions import FEED_NEWEST, ROOT

BRIEF = ROOT / "inputs" / "rea-brief-npm-audit-gap"
RAW = BRIEF / "live" / "raw"
FROZEN_SPLIT = "17a37df397c2c8d9cc0039a5650ad3740738ecd11fd9bfd7294eae63a0257037"
BRIEF_VERSIONS = ["2026.4.22", "2026.6.10", "2026.1.29"]
SECTION_BANNED = [
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
    r"\bwrong\b",
    r"\bmisses\b",
    r"\bmissed\b",
    r"\bfails\b",
    r"\bfailed\b",
    r"\bbroken\b",
    r"\bblind\b",
    r"\bincorrect\b",
    r"\bbecause\b",
    r"\bcause[ds]?\b",
    r"\bdue to\b",
]
SENTENCE_RE = re.compile(
    r"^npm audit returned \d+ advisories for openclaw@\S+ on \d{4}-\d{2}-\d{2}; "
    r"(?:the maker's repository lists|the GitHub advisory database and the maker's repository list) "
    r"\d+ \(feed newest \d{4}-\d{2}-\d{2}\)\.$"
)


def section_banned(text: str) -> list[str]:
    hits = []
    for pattern in SECTION_BANNED:
        hits.extend(match.group(0) for match in re.finditer(pattern, text, re.I))
    return hits


class NpmAuditTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.frozen = json.loads((BRIEF / "live" / "split.json").read_text())
        cls.scored, cls.source_log = score_versions(RAW, BRIEF_VERSIONS)

    def test_frozen_split_sha256(self) -> None:
        digest = hashlib.sha256((BRIEF / "live" / "split.json").read_bytes()).hexdigest()
        self.assertEqual(digest, FROZEN_SPLIT)

    def test_endpoint_and_request_body(self) -> None:
        self.assertEqual(ENDPOINT, "https://registry.npmjs.org/-/npm/v1/security/advisories/bulk")
        for version in BRIEF_VERSIONS:
            self.assertEqual(request_body(version), (RAW / f"req-{version}.json").read_bytes())

    def test_brief_replay_matches_frozen_split(self) -> None:
        self.assertEqual(FEED_NEWEST, "2026-09-11")
        by_version = {row["version"]: row for row in self.frozen["versions"]}
        lines = []
        for row in self.scored["versions"]:
            want = by_version[row["version"]]
            self.assertEqual(row["npm_audit"], want["npm_audit"])
            self.assertEqual(row["clawscore"], want["clawscore"])
            self.assertEqual(row["overlap"], want["overlap"])
            self.assertEqual(row["db_not_npm"], want["db_not_npm"])
            self.assertEqual(row["repo_only"], want["repo_only"])
            self.assertEqual(row["npm_only"], want["npm_only"])
            self.assertEqual(row["npm_audit_rows"], want["npm_audit_rows"])
            self.assertEqual(row["sentence"], want["sentence"])
            self.assertEqual(row["response_sha256"], want["response_sha256"])
            lines.extend(report_lines(row))
        text = "\n".join(lines)
        self.assertIn(
            "2026.4.22: 67 / 148 = 67 + 1 (GHSA-2j8v-hwgc-x698) + 80, npm-only 0.",
            text,
        )
        self.assertIn("2026.6.10: 0 / 58 = 0 + 0 + 58, npm-only 0.", text)
        self.assertIn("2026.1.29: 555 / 627 = 555 + 2 + 70, npm-only 0.", text)

    def test_m3_parts_sum(self) -> None:
        ctx = load_context()
        for version in BRIEF_VERSIONS:
            data, _meta = load_response(RAW, version)
            npm, _nrows = parse_npm_ids(data)
            ids = clawscore_ids(ctx.oracle, ctx.feed, version)
            overlap, db_not_npm, repo_only, _npm_only = classify(ids, npm, ctx.global_db)
            self.assertEqual(len(overlap) + len(db_not_npm) + len(repo_only), len(ids), version)

    def test_brief_sources_keep_maker_sentence(self) -> None:
        for line in self.source_log.splitlines():
            self.assertIn("not_openclaw 0", line)
        for row in self.scored["versions"]:
            self.assertEqual(row["foreign_source_count"], 0)
            self.assertIn("the maker's repository lists", row["sentence"])
            self.assertNotIn("GitHub advisory database and the maker's repository list", row["sentence"])

    def test_offline_refuses_tampered_response(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            raw = Path(tmp) / "raw"
            raw.mkdir()
            for name in ("req-2026.6.10.json", "resp-2026.6.10.json", "meta-2026.6.10.json"):
                shutil.copy(RAW / name, raw / name)
            resp = raw / "resp-2026.6.10.json"
            resp.write_bytes(resp.read_bytes() + b" ")
            with self.assertRaises(SystemExit) as caught:
                score_versions(raw, ["2026.6.10"])
            self.assertIn("does not match", str(caught.exception))

    def test_sentence_has_fetched_date(self) -> None:
        for row in self.scored["versions"]:
            sentence = sentence_for(row, FEED_NEWEST)
            self.assertEqual(sentence, row["sentence"])
            self.assertIsNotNone(SENTENCE_RE.fullmatch(sentence), sentence)
            self.assertIn(str(row["npm_audit_date_utc"])[:10], sentence)
            self.assertIn(f"feed newest {FEED_NEWEST}", sentence)
            self.assertIn(f"openclaw@{row['version']} on ", sentence)

    def test_npm_section_banned_words(self) -> None:
        section = {
            "feed_newest": FEED_NEWEST,
            "rows": self.scored["versions"],
        }
        text = "\n".join(render_npm_audit(section))
        self.assertEqual(section_banned(text), [])
        self.assertIn("## npm audit comparison", text)
        for row in self.scored["versions"]:
            self.assertIn(sentence_for(row, FEED_NEWEST), text)
            self.assertIn(str(row["npm_audit_date_utc"])[:10], text)
            self.assertIn(FEED_NEWEST, text)

    def test_foreign_source_rewords_sentence(self) -> None:
        row = dict(self.scored["versions"][0])
        row["foreign_source_count"] = 1
        sentence = sentence_for(row, FEED_NEWEST)
        self.assertIn("the GitHub advisory database and the maker's repository list", sentence)
        self.assertNotIn("the maker's repository lists", sentence)
        self.assertIsNotNone(SENTENCE_RE.fullmatch(sentence), sentence)

    def test_section_absent_when_split_missing(self) -> None:
        scan = {"installs": [{"candidates": ["2026.4.22"]}]}
        missing = Path("/tmp/clawscore-npm-audit-split-missing.json")
        self.assertIsNone(load_npm_section(scan, missing))

    def test_section_absent_when_a_fleet_version_is_missing(self) -> None:
        row = self.scored["versions"][0]
        payload = {"feed_newest": FEED_NEWEST, "versions": [row]}
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "split.json"
            path.write_text(json.dumps(payload))
            scan = {"installs": [{"candidates": ["2026.4.22", "2026.6.10"]}]}
            self.assertIsNone(load_npm_section(scan, path))

    def test_section_follows_distinct_scan_versions(self) -> None:
        payload = {"feed_newest": FEED_NEWEST, "versions": self.scored["versions"]}
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "split.json"
            path.write_text(json.dumps(payload))
            scan = {"installs": [{"candidates": ["2026.1.29"]}, {"candidates": ["2026.4.22", "2026.6.10"]}]}
            section = load_npm_section(scan, path)
        self.assertIsNotNone(section)
        assert section is not None
        self.assertEqual([row["version"] for row in section["rows"]], ["2026.1.29", "2026.4.22", "2026.6.10"])
        self.assertEqual(distinct_versions(scan), ["2026.1.29", "2026.4.22", "2026.6.10"])

    def test_lab_versions_are_the_scan(self) -> None:
        scan = json.loads((ROOT / "evidence" / "scan.json").read_text())
        self.assertEqual(lab_versions(), distinct_versions(scan))
        self.assertEqual(
            lab_versions(),
            [
                "2026.1.29",
                "2026.2.14",
                "2026.3.28",
                "2026.4.7-1",
                "2026.4.8",
                "2026.4.15",
                "2026.4.20",
                "2026.4.21",
                "2026.4.22",
                "2026.4.23",
                "2026.10.4",
            ],
        )

    def test_lab_report_section_matches_committed_split(self) -> None:
        path = ROOT / "evidence" / "npm-audit" / "split.json"
        self.assertTrue(path.is_file(), "evidence/npm-audit/split.json is missing")
        scan = json.loads((ROOT / "evidence" / "scan.json").read_text())
        observed = load_observed_at(ROOT / "evidence" / "lab-scan-observed-at.txt")
        data = build_report(
            scan,
            observed_at=observed,
            commit=tool_commit(),
            feed_sha=feed_sha256(),
            fleet=fleet_name(),
        )
        markdown = render_markdown(data)
        self.assertEqual(markdown.count("## npm audit comparison"), 1)
        self.assertLess(markdown.index("## Fleet summary"), markdown.index("## npm audit comparison"))
        self.assertLess(markdown.index("## npm audit comparison"), markdown.index("## Fix order"))
        split = json.loads(path.read_text())
        by_version = {row["version"]: row for row in split["versions"]}
        self.assertEqual([row["version"] for row in data["npm_audit"]["rows"]], lab_versions())
        for row in data["npm_audit"]["rows"]:
            source = by_version[row["version"]]
            self.assertEqual(row["npm_audit"], source["npm_audit"])
            self.assertEqual(row["clawscore"], source["clawscore"])
            self.assertEqual(row["overlap"], source["overlap"])
            self.assertEqual(row["db_not_npm"], source["db_not_npm"])
            self.assertEqual(row["repo_only"], source["repo_only"])
            self.assertEqual(row["npm_only"], source["npm_only"])
            self.assertEqual(row["overlap"] + len(row["db_not_npm"]) + row["repo_only"], row["clawscore"])
            self.assertIn(row["sentence"], markdown)
            self.assertEqual(row["sentence"], sentence_for(row, data["npm_audit"]["feed_newest"]))
            self.assertEqual(section_banned(row["sentence"]), [])


if __name__ == "__main__":
    unittest.main()
