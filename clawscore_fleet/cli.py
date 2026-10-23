"""clawscore-fleet scan command."""

from __future__ import annotations

import csv
import json
from pathlib import Path

from clawscore_fleet.blast import analyze_container
from clawscore_fleet.cves import report_for_versions
from clawscore_fleet.ghsa_only import rows_for_install, snapshot_sha256
from clawscore_fleet.docker_target import (
    assert_lab_target,
    discover_install_root,
    hash_paths,
    lab_container_names,
    list_paths,
    work_dir_from_root,
)
from clawscore_fleet.fingerprint import identify, load_db
from clawscore_fleet.fixorder import fix_order
from clawscore_fleet.scan_host import merge_host, scan_host
from clawscore_fleet.summary import summary_from_scan
from clawscore_fleet.idle_linux import evaluate as evaluate_idle_linux
from clawscore_fleet.versions import FEED_NEWEST

ROOT = Path(__file__).resolve().parents[1]


def _read_targets(path: Path) -> list[str]:
    names = []
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        names.append(line)
    return names


def _read_agent365(path: Path) -> list[dict]:
    with path.open(newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames is None:
            raise SystemExit(f"agent365 export has no header: {path}")
        lowered = [name.lower() for name in reader.fieldnames]
        if any("risk" in name for name in lowered):
            raise SystemExit("agent365 export includes a risk column; this mock must not")
        rows = []
        for row in reader:
            mcp_raw = row.get("mcpServers") or ""
            mcp = [part for part in mcp_raw.split("|") if part]
            rows.append(
                {
                    "name": row.get("name") or "",
                    "version": row.get("version") or "",
                    "process": row.get("process") or "",
                    "device": row.get("device") or "",
                    "user": row.get("user") or "",
                    "autoApprove": row.get("autoApprove") or "",
                    "mcpServers": mcp,
                }
            )
        return rows


def _unknown_report() -> dict:
    report = report_for_versions([])
    report["note"] = "version was not identified"
    report["vulnerable"] = False
    return report


def scan(targets: Path, agent365: Path, out_dir: Path) -> dict:
    db = load_db()
    names = _read_targets(targets)
    allowed = lab_container_names()
    rows = _read_agent365(agent365)
    by_device = {row["device"]: row for row in rows}
    installs = []
    log_lines = []
    for name in names:
        assert_lab_target(name, allowed)
        root = discover_install_root(name)
        files_read_abs: list[str] = []
        if root is None:
            ident = {
                "version": None,
                "verdict": "unknown",
                "candidates": [],
                "family": "",
                "matched_files": [],
                "files_read": [],
            }
            blast = {"credentials": [], "mcp_servers": [], "auto_approve": None, "config_paths": []}
            report = _unknown_report()
        else:
            listed = list_paths(name, root)

            def fetch(rels, container=name, install_root=root):
                return hash_paths(container, install_root, rels)

            ident = identify(listed, fetch, db)
            files_read_abs = [f"{root}/{rel}" for rel in ident["files_read"]]
            for abs_path in files_read_abs:
                log_lines.append(f"{name}\t{abs_path}")
            blast = analyze_container(name, work_dir_from_root(root))
            if ident["verdict"] == "unknown":
                report = _unknown_report()
            else:
                report = report_for_versions(ident["candidates"])
        installs.append(
            {
                "id": name,
                "install_root": root,
                "version": ident["version"],
                "verdict": ident["verdict"],
                "candidates": ident["candidates"],
                "family": ident["family"],
                "method": ident["family"] if ident["verdict"] != "unknown" else "none",
                "matched_files": ident["matched_files"],
                "files_read": files_read_abs,
                "cves": report["cve_ids"],
                "ghsa_ids": report["ghsa_ids"],
                "ghsa_only": rows_for_install(ident["version"], ident["candidates"], ident["verdict"]),
                "advisory_count": report["advisories"],
                "advisory_critical": report["critical"],
                "advisory_high": report["high"],
                "advisory_note": report["note"],
                "vulnerable": report["vulnerable"],
                "feed_newest": FEED_NEWEST,
                "credentials": blast["credentials"],
                "mcp_servers": blast["mcp_servers"],
                "auto_approve": blast["auto_approve"],
                "config_paths": blast["config_paths"],
                "agent365": by_device.get(name),
            }
        )
    order = fix_order(installs)
    document = {
        "feed_newest": FEED_NEWEST,
        "osv_snapshot_sha256": snapshot_sha256(),
        "installs": installs,
        "fix_order": order,
        "agent365_rows": rows,
        "agent365_row_count": len(rows),
    }
    document["summary"] = summary_from_scan(document)
    document["idle_linux"] = [evaluate_idle_linux()["row"]]
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "scan.json").write_text(json.dumps(document, indent=2, sort_keys=True) + "\n")
    (out_dir / "files-read.log").write_text("\n".join(log_lines) + ("\n" if log_lines else ""))
    return document


def main(argv: list[str] | None = None) -> int:
    import argparse

    parser = argparse.ArgumentParser(prog="clawscore")
    sub = parser.add_subparsers(dest="cmd", required=True)
    scan_parser = sub.add_parser("scan")
    scan_parser.add_argument("--targets", required=True)
    scan_parser.add_argument("--agent365", required=True)
    scan_parser.add_argument("--out", required=True)
    host_parser = sub.add_parser("scan-host")
    host_parser.add_argument("--root", required=True)
    host_parser.add_argument("--out", required=True)
    merge_parser = sub.add_parser("merge")
    merge_parser.add_argument("--in", dest="inputs", nargs="+", required=True)
    merge_parser.add_argument("--defender")
    merge_parser.add_argument("--out", required=True)
    export_parser = sub.add_parser("export-osv")
    export_parser.add_argument("--package", required=True)
    export_parser.add_argument("--out")
    args = parser.parse_args(argv)
    if args.cmd == "scan":
        document = scan(Path(args.targets), Path(args.agent365), Path(args.out))
        print(f"wrote {args.out} installs={len(document['installs'])}")
        print(document["summary"]["sentence"])
        return 0
    if args.cmd == "scan-host":
        document = scan_host(Path(args.root), Path(args.out))
        print(f"wrote {args.out} installs={len(document['installs'])} unidentified={len(document['unidentified'])}")
        return 0
    if args.cmd == "merge":
        defender = Path(args.defender) if args.defender else None
        document = merge_host([Path(item) for item in args.inputs], Path(args.out), defender)
        print(f"wrote {args.out} installs={len(document['installs'])} unidentified={len(document['unidentified'])}")
        return 0
    if args.cmd == "export-osv":
        if args.package != "openclaw":
            print("export-osv only writes package openclaw")
            return 1
        from clawscore_fleet.export_osv import write_export

        out = Path(args.out) if args.out else None
        written = write_export(out)
        print(f"wrote {args.out or 'evidence/scanner-feed-gap/osv'} files={len(written)}")
        return 0
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
