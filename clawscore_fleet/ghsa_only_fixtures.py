"""Filesystem hosts for the GHSA-only gate.

Each host is the idle-paths default global layout (L1). Discovery reads the
version from that install. The report uses that discovered version for
`report_for_versions` and `for_version`.
"""

from __future__ import annotations

import hashlib
import json
import shutil
from pathlib import Path

from clawscore_fleet.cves import report_for_versions
from clawscore_fleet.fixtures.idle_linux import LAYOUTS, build_global_layout
from clawscore_fleet.ghsa_only import for_version, snapshot_sha256
from clawscore_fleet.idle_linux import discover_all
from clawscore_fleet.versions import ROOT

INPUTS = ROOT / "inputs" / "clawscore-ghsa-only" / "expected-ghsa-only.json"


def _replace(out: Path) -> Path:
    resolved = out.resolve()
    if resolved == Path("/") or resolved == ROOT or resolved in ROOT.parents:
        raise SystemExit(f"refusing to replace {resolved}")
    if resolved.exists():
        shutil.rmtree(resolved)
    resolved.mkdir(parents=True)
    return resolved


def _discovered(host_root: Path, planted: str, host_id: str) -> dict:
    rows = discover_all(host_root)
    found = [row for row in rows if row.get("install") == LAYOUTS["L1"]]
    if len(found) != 1:
        raise SystemExit(f"{host_id} discovery found {len(found)} global installs, want 1")
    row = found[0]
    version = row.get("resolved_version")
    source = row.get("version_source") or ""
    if version != planted:
        raise SystemExit(
            f"{host_id} discovery version {version!r} source {source!r} "
            f"install {row.get('install')!r}; package file was written as {planted!r}"
        )
    return row


def build_report(out: Path) -> dict:
    resolved = _replace(out)
    expected = json.loads(INPUTS.read_text())
    hosts = []
    for spec in expected["fixture_hosts"]:
        host_id = spec["id"]
        planted = spec["version"]
        host_root = resolved / "hosts" / host_id
        build_global_layout(host_root, planted)
        found = _discovered(host_root, planted, host_id)
        version = found["resolved_version"]
        report = report_for_versions([version])
        hosts.append(
            {
                "id": host_id,
                "version": version,
                "layout": found["install"],
                "version_source": found["version_source"],
                "cves": report["cve_ids"],
                "ghsa_ids": report["ghsa_ids"],
                "ghsa_only": for_version(version),
            }
        )
    document = {"osv_snapshot_sha256": snapshot_sha256(), "hosts": hosts}
    report_path = resolved / "report.json"
    report_path.write_text(json.dumps(document, indent=2, sort_keys=True) + "\n")
    digest = hashlib.sha256(report_path.read_bytes()).hexdigest()
    (resolved / "SHA256SUMS").write_text(f"{digest}  report.json\n")
    return document


def main(argv: list[str] | None = None) -> int:
    import argparse

    parser = argparse.ArgumentParser(prog="python -m clawscore_fleet.ghsa_only_fixtures")
    parser.add_argument("--out", required=True)
    args = parser.parse_args(argv)
    document = build_report(Path(args.out))
    print(f"wrote {args.out}/report.json hosts={len(document['hosts'])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
