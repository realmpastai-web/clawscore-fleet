"""OSV export replay. The files are produced from gap-ids.txt and ghsa-all.json."""

from __future__ import annotations

import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from clawscore_fleet.cli import main
from clawscore_fleet.export_osv import DEFAULT_OUT, GAP_PATH, validate_directory, write_export


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


class ExportOsvTest(unittest.TestCase):
    def test_other_package_exits(self) -> None:
        self.assertEqual(main(["export-osv", "--package", "not-openclaw"]), 1)

    def test_replay_matches_committed_sha256(self) -> None:
        gap = [line for line in GAP_PATH.read_text().splitlines() if line.strip()]
        committed = sorted(DEFAULT_OUT.glob("GHSA-*.json"))
        self.assertEqual(len(committed), len(gap))
        validate_directory(DEFAULT_OUT)
        with tempfile.TemporaryDirectory(prefix="osv-replay-") as tmp:
            written = write_export(Path(tmp))
            self.assertEqual(len(written), len(gap))
            validate_directory(Path(tmp))
            for path in committed:
                self.assertEqual(_sha(path), _sha(Path(tmp) / path.name))
            listed = (DEFAULT_OUT / "SHA256SUMS").read_text().splitlines()
            self.assertEqual(len(listed), len(gap))
            for line in listed:
                digest, name = line.split("  ", 1)
                self.assertEqual(digest, _sha(DEFAULT_OUT / name))
                doc = json.loads((DEFAULT_OUT / name).read_text())
                self.assertEqual(doc["schema_version"], "1.6.0")
                self.assertIsNone(doc.get("withdrawn"))


if __name__ == "__main__":
    unittest.main()
