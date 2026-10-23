"""2026.10.5 fingerprint gap and the re-pinned feed counts."""

from __future__ import annotations

import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from clawscore_fleet.feed_check import source_counts
from clawscore_fleet.fingerprint import identify, load_db
from clawscore_fleet.scan_host import scan_host
from clawscore_fleet.versions import ROOT

SIG = ROOT / "inputs" / "rea-openclaw-latest-evidence" / "sig"
MARKS = (
    "dist/cli.runtime.js",
    "dist/abort.runtime.js",
    "dist/.buildstamp",
    "dist/build-info.json",
)


def _present(base: Path) -> tuple[list[str], object]:
    rels = [rel for rel in MARKS if (base / rel).is_file()]

    def fetch(wanted: list[str]) -> dict[str, str | None]:
        found: dict[str, str | None] = {}
        for rel in wanted:
            path = base / rel
            if not path.is_file():
                found[rel] = None
                continue
            digest = hashlib.sha256()
            with path.open("rb") as handle:
                for chunk in iter(lambda: handle.read(1024 * 1024), b""):
                    digest.update(chunk)
            found[rel] = digest.hexdigest()
        return found

    return rels, fetch


def _identify(version: str, db: dict) -> dict:
    rels, fetch = _present(SIG / version)
    return identify(rels, fetch, db)


def _scan(version: str) -> dict:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        dest = root / "home" / "pilot" / ".npm-global" / "lib" / "node_modules" / "openclaw"
        (dest / "dist").mkdir(parents=True)
        (dest / "package.json").write_text(json.dumps({"name": "openclaw", "version": version}) + "\n")
        for name in ("abort.runtime.js", "cli.runtime.js", "build-info.json"):
            source = SIG / version / "dist" / name
            (dest / "dist" / name).write_bytes(source.read_bytes())
        document = scan_host(root, root / "out")
    return document["installs"][0]


class Latest2026105Test(unittest.TestCase):
    def test_t1_main_db_unknown(self) -> None:
        db = load_db(ROOT / "fixtures" / "db-d733a8c.json")
        result = _identify("2026.10.5", db)
        self.assertEqual(result["verdict"], "unknown")
        self.assertIsNone(result["version"])
        self.assertEqual(result["candidates"], [])

    def test_t2_new_db_exact(self) -> None:
        result = _identify("2026.10.5", load_db())
        self.assertEqual(result["verdict"], "exact")
        self.assertEqual(result["version"], "2026.10.5")
        self.assertEqual(result["candidates"], ["2026.10.5"])

    def test_t3_previous_release_still_exact(self) -> None:
        result = _identify("2026.10.4", load_db())
        self.assertEqual(result["verdict"], "exact")
        self.assertEqual(result["version"], "2026.10.4")

    def test_t4_beta_unidentified_vulnerable_null(self) -> None:
        row = _scan("2026.10.10-beta.2")
        self.assertEqual(row["verdict"], "unknown")
        self.assertIsNone(row["version"])
        self.assertIsNone(row["vulnerable"])
        self.assertIsNot(row["vulnerable"], False)

    def test_t5_scan_matches_repinned_feed(self) -> None:
        row = _scan("2026.10.5")
        counts = {item["version"]: item for item in source_counts()}
        expected = counts["2026.10.5"]["github_db"] + counts["2026.10.5"]["repo_only"]
        self.assertEqual(row["verdict"], "exact")
        self.assertEqual(row["version"], "2026.10.5")
        self.assertEqual(row["advisory_count"], expected)

    def test_t6_unindexed_fallback_nonzero(self) -> None:
        """Unindexed 2026.6.7 is scored by the feed fallback, and that count is 61."""
        from clawscore_fleet.cves import build_index, report_for_versions

        version = "2026.6.7"
        index = build_index()
        self.assertNotIn(version, index["per_version"])
        report = report_for_versions([version])
        self.assertEqual(report["advisories"], 61)
        self.assertGreater(report["advisories"], 0)
