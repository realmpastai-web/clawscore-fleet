"""Lab answer key for score_holdout.py, from the manifest and Hark's oracle."""

from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
from pathlib import Path

import yaml

from clawscore_fleet.fingerprint import collision_groups, load_db
from clawscore_fleet.versions import NO_ADVISORY_WORDING, ROOT

ORACLE_PATH = ROOT / "inputs" / "rea-brief-sample-report" / "report-brief" / "oracle.py"
SCORER_PATH = ROOT / "inputs" / "rea-brief-sample-report" / "report-brief" / "score_holdout.py"
FEED_PATH = ROOT / "evidence" / "landscape" / "ghsa-all.json"


def load_oracle():
    spec = importlib.util.spec_from_file_location("hark_oracle", ORACLE_PATH)
    if spec is None or spec.loader is None:
        raise SystemExit(f"cannot load {ORACLE_PATH}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_feed() -> list:
    payload = json.loads(FEED_PATH.read_text())
    if not isinstance(payload, list):
        raise SystemExit("ghsa-all.json is not a list")
    return payload


def build_lab_key(manifest: dict, feed: list, db: dict | None = None) -> dict:
    oracle = load_oracle()
    groups = collision_groups(db or load_db())
    by_version: dict[str, list[str]] = {}
    for group in groups:
        for version in group:
            by_version[version] = list(group)
    rows = []
    for item in manifest["installs"]:
        version = item["version"]
        if version in by_version:
            verdict = "range"
            candidates = list(by_version[version])
        else:
            verdict = "exact"
            candidates = [version]
        chosen: dict[str, str] = {}
        for candidate in candidates:
            for ghsa_id, severity in oracle.advisories(feed, candidate):
                chosen.setdefault(ghsa_id, severity)
        ids = sorted(chosen)
        critical = sum(1 for ghsa_id in ids if chosen[ghsa_id] == "critical")
        high = sum(1 for ghsa_id in ids if chosen[ghsa_id] == "high")
        rows.append(
            {
                "advisory_count": len(ids),
                "advisory_ids": ids,
                "auto_approve": bool(item["auto_approve"]),
                "candidates": candidates,
                "credential_names": sorted(item.get("credentials") or []),
                "critical": critical,
                "high": high,
                "id": item["id"],
                "verdict": verdict,
                "zero_wording": "" if ids else NO_ADVISORY_WORDING,
            }
        )
    return {"key": rows}


def score_lab(key_path: Path, data_path: Path, markdown_path: Path, pool_path: Path) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(SCORER_PATH), str(key_path), str(data_path), str(markdown_path), str(pool_path)],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )


def main(argv: list[str] | None = None) -> int:
    manifest = yaml.safe_load((ROOT / "fleet" / "manifest.yaml").read_text())
    key = build_lab_key(manifest, load_feed())
    out = ROOT / "evidence" / "report"
    out.mkdir(parents=True, exist_ok=True)
    key_path = out / "lab-key.json"
    key_path.write_text(json.dumps(key, indent=2, sort_keys=True) + "\n")
    data_path = out / "report-data.json"
    markdown_path = out / "report.md"
    pool_path = ROOT / "fleet" / "secrets-pool.json"
    proc = score_lab(key_path, data_path, markdown_path, pool_path)
    log = (proc.stdout or "") + (proc.stderr or "")
    (out / "lab-score.log").write_text(log if log.endswith("\n") or log == "" else log + "\n")
    sys.stdout.write(log)
    return proc.returncode


if __name__ == "__main__":
    raise SystemExit(main())
