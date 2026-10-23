#!/usr/bin/env python3
"""Build evidence/host-mode/rea-beta-summary.json from a REA JSON file.

The summary is computed from the file on disk: sha256, byte size, the Evidence
ID, the provider version and operation recorded in the file, and the
file-inventory nodes for dist/abort.runtime.js and dist/build-info.json.
Those nodes are copied from the parsed document, not rewritten by hand.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "evidence" / "host-mode" / "rea-beta.json"
DEFAULT_OUTPUT = ROOT / "evidence" / "host-mode" / "rea-beta-summary.json"
INVENTORY_PATHS = ("dist/abort.runtime.js", "dist/build-info.json")
INVENTORY_OPERATION = "inventory-relevant-file"


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _observation_nodes(doc: dict) -> tuple[dict, dict, list]:
    """Return (observation, normalized_result, graph nodes) from a REA document.

    A finished analysis stores the graph on the document. A resource-constraint
    failure stores it under details.partial_observation.normalized_result.
    """
    if not isinstance(doc, dict):
        return {}, {}, []
    if isinstance(doc.get("graph"), dict):
        observation = doc
        normalized = doc
    else:
        details = doc.get("details") if isinstance(doc.get("details"), dict) else {}
        observation = details.get("partial_observation") if isinstance(details.get("partial_observation"), dict) else {}
        normalized = observation.get("normalized_result") if isinstance(observation.get("normalized_result"), dict) else {}
    graph = normalized.get("graph") if isinstance(normalized.get("graph"), dict) else {}
    nodes = graph.get("nodes") if isinstance(graph.get("nodes"), list) else []
    return observation, normalized, nodes


def file_inventory_entries(doc: dict) -> dict[str, list]:
    """Graph nodes whose inventory-relevant-file observation names each path."""
    _observation, _normalized, nodes = _observation_nodes(doc)
    found = {path: [] for path in INVENTORY_PATHS}
    for node in nodes:
        if not isinstance(node, dict):
            continue
        observations = node.get("observations")
        if not isinstance(observations, list):
            continue
        for item in observations:
            if not isinstance(item, dict):
                continue
            properties = item.get("properties") if isinstance(item.get("properties"), dict) else {}
            evidence = item.get("evidence") if isinstance(item.get("evidence"), dict) else {}
            extractor = evidence.get("extractor") if isinstance(evidence.get("extractor"), dict) else {}
            path = properties.get("path")
            if path in found and extractor.get("operation") == INVENTORY_OPERATION:
                found[path].append(node)
                break
    return found


def summarize(path: Path) -> dict:
    """Read one REA JSON file and return the committable summary object."""
    raw_size = path.stat().st_size
    digest = sha256_file(path)
    document = json.loads(path.read_text())
    observation, _normalized, _nodes = _observation_nodes(document)
    provider = observation.get("provider") if isinstance(observation.get("provider"), dict) else {}
    parameters = observation.get("parameters") if isinstance(observation.get("parameters"), dict) else {}
    operation = observation.get("operation")
    if not isinstance(operation, str) or not operation:
        details = document.get("details") if isinstance(document, dict) and isinstance(document.get("details"), dict) else {}
        operation = details.get("operation") if isinstance(details.get("operation"), str) else ""
    evidence = observation.get("evidence_id") if isinstance(observation.get("evidence_id"), str) else ""
    analysis = {}
    if isinstance(document, dict) and isinstance(document.get("error"), str):
        analysis = {
            "error": document.get("error"),
            "code": document.get("code"),
            "category": document.get("category"),
            "message": document.get("message"),
            "retryable": document.get("retryable"),
        }
    summary = {
        "source_file": "evidence/host-mode/rea-beta.json",
        "sha256": digest,
        "bytes": raw_size,
        "evidence_id": evidence,
        "rea_version": provider.get("version"),
        "rea_command": operation,
        "provider": provider,
        "parameters": parameters,
        "analysis": analysis,
        "file_inventory": file_inventory_entries(document),
    }
    return summary


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Summarize a REA analyze-javascript-application JSON file")
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args(argv)
    if not args.input.is_file():
        print(f"missing {args.input}", file=sys.stderr)
        return 1
    summary = summarize(args.input)
    missing = [path for path, nodes in summary["file_inventory"].items() if not nodes]
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(summary, indent=2) + "\n")
    print(f"wrote {args.output}")
    print(f"sha256 {summary['sha256']}")
    print(f"bytes {summary['bytes']}")
    print(f"evidence_id {summary['evidence_id']}")
    print(f"rea_version {summary['rea_version']}")
    print(f"rea_command {summary['rea_command']}")
    for path, nodes in summary["file_inventory"].items():
        print(f"inventory {path} nodes={len(nodes)}")
    if missing:
        print("missing inventory entries: " + ", ".join(missing), file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
