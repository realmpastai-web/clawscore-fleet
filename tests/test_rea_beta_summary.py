"""The REA summary extractor copies inventory nodes from a parsed document."""

from __future__ import annotations

import unittest

from tools import rea_beta_summary as summary


def _node(path: str, operation: str) -> dict:
    return {
        "node_id": "jag_node_" + path.replace("/", "_"),
        "kind": "artifact",
        "observations": [
            {
                "label": path,
                "properties": {"path": path, "bytes": 1},
                "evidence": {"extractor": {"operation": operation}},
            }
        ],
    }


class ReaBetaSummaryTest(unittest.TestCase):
    def test_inventory_nodes_are_copied_from_a_partial_observation(self) -> None:
        abort = _node("dist/abort.runtime.js", "inventory-relevant-file")
        info = _node("dist/build-info.json", "inventory-relevant-file")
        other = _node("dist/other.js", "recover-source-module")
        document = {
            "error": "JavaScript application analysis failed",
            "details": {
                "operation": "analyze_javascript_application",
                "partial_observation": {
                    "evidence_id": "ev_test",
                    "provider": {"version": "1"},
                    "operation": "analyze_javascript_application",
                    "normalized_result": {"graph": {"nodes": [abort, other, info]}},
                },
            },
        }
        found = summary.file_inventory_entries(document)
        self.assertEqual(found["dist/abort.runtime.js"], [abort])
        self.assertEqual(found["dist/build-info.json"], [info])
        self.assertNotIn(other, found["dist/abort.runtime.js"])


if __name__ == "__main__":
    unittest.main()
