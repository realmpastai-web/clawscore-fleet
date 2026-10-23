"""Holdout lab targets. The main lab files are not written."""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

from clawscore_fleet.blast import analyze_container
from clawscore_fleet.cves import report_for_versions
from clawscore_fleet.docker_target import (
    discover_install_root,
    hash_paths,
    list_paths,
    work_dir_from_root,
)
from clawscore_fleet.fingerprint import identify, load_db
from clawscore_fleet.fixorder import fix_order
from clawscore_fleet.ghsa_only import rows_for_install, snapshot_sha256
from clawscore_fleet.report import write_report
from clawscore_fleet.summary import summary_from_scan
from clawscore_fleet.versions import FEED_NEWEST, ROOT

NAME_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_.-]{0,63}$")
OUT = ROOT / "fleet-holdout"
EVIDENCE = ROOT / "evidence" / "holdout"
COMPOSE = OUT / "compose.yaml"
NETWORK = "clawscore-holdout"
ENV_JS = """
const fs = require("fs");
const buf = fs.readFileSync("/proc/1/environ");
const names = [];
for (const part of buf.toString("utf8").split("\\0")) {
  if (!part) continue;
  const idx = part.indexOf("=");
  if (idx > 0) names.push(part.slice(0, idx));
}
process.stdout.write(names.sort().join("\\n"));
"""


def git_head() -> str:
    proc = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    if proc.returncode != 0:
        raise SystemExit(proc.stderr.strip() or "git rev-parse HEAD failed")
    return proc.stdout.strip()


def git_porcelain() -> str:
    proc = subprocess.run(
        ["git", "status", "--porcelain"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    if proc.returncode != 0:
        raise SystemExit(proc.stderr.strip() or "git status failed")
    return proc.stdout


def report_or_refuse(head: str, porcelain: str) -> str:
    """Print HEAD. Refuse when porcelain is non-empty."""
    print(head, flush=True)
    if porcelain.strip():
        print(porcelain, end="" if porcelain.endswith("\n") else "\n", flush=True)
        raise SystemExit("holdout-report refuses a dirty tree")
    return head


def _run(cmd: list[str], **kwargs) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, capture_output=True, text=True, check=False, **kwargs)


def _ps_text() -> str:
    proc = _run(
        [
            "docker",
            "ps",
            "-a",
            "--filter",
            "label=clawscore.holdout=1",
            "--format",
            "{{.Names}}\t{{.Status}}\t{{.Ports}}",
        ]
    )
    if proc.returncode != 0:
        return (proc.stderr or "") + (proc.stdout or "")
    lines = sorted(line for line in proc.stdout.splitlines() if line.strip())
    return "\n".join(lines) + ("\n" if lines else "")


def _holdout_names() -> set[str]:
    proc = _run(
        [
            "docker",
            "ps",
            "-a",
            "--filter",
            "label=clawscore.holdout=1",
            "--format",
            "{{.Names}}",
        ]
    )
    if proc.returncode != 0:
        raise SystemExit(proc.stderr.strip() or "docker ps failed")
    return {line.strip() for line in proc.stdout.splitlines() if line.strip()}


def _versions() -> list[str]:
    seen: list[str] = []
    images = OUT / "images"
    for path in sorted(images.glob("Dockerfile.*")):
        version = path.name[len("Dockerfile.") :]
        if version not in seen:
            seen.append(version)
    return seen


def _build() -> None:
    context = Path("/tmp/clawscore-empty-ctx")
    context.mkdir(parents=True, exist_ok=True)
    env = os.environ.copy()
    env["DOCKER_BUILDKIT"] = "1"
    for version in _versions():
        dockerfile = OUT / "images" / f"Dockerfile.{version}"
        tag = f"clawscore-openclaw:{version}"
        print(f"docker build -f {dockerfile} -t {tag}", flush=True)
        rc = subprocess.call(
            ["docker", "build", "--progress=quiet", "-f", str(dockerfile), "-t", tag, str(context)],
            env=env,
        )
        if rc != 0:
            print(f"docker build failed for {tag}; rerunning with plain progress", flush=True)
            rc = subprocess.call(
                ["docker", "build", "--progress=plain", "-f", str(dockerfile), "-t", tag, str(context)],
                env=env,
            )
            raise SystemExit(rc)


def _up() -> None:
    print("docker compose up -d --no-build --force-recreate", flush=True)
    rc = subprocess.call(
        [
            "docker",
            "compose",
            "-f",
            str(COMPOSE),
            "up",
            "-d",
            "--no-build",
            "--force-recreate",
            "--remove-orphans",
        ]
    )
    if rc != 0:
        raise SystemExit(rc)


def _expected_count() -> int:
    hosts = (OUT / "hosts.txt").read_text().splitlines()
    return len([line for line in hosts if line.strip()])


def _rows() -> list[tuple[str, str, str]]:
    rows = []
    for line in _ps_text().splitlines():
        parts = line.split("\t")
        while len(parts) < 3:
            parts.append("")
        rows.append((parts[0].strip(), parts[1].strip(), parts[2].strip()))
    return rows


def _wait_running() -> list[tuple[str, str, str]]:
    expected = _expected_count()
    deadline = time.time() + 90
    last: list[tuple[str, str, str]] = []
    while time.time() < deadline:
        last = _rows()
        up = [row for row in last if row[1].startswith("Up")]
        if len(last) == expected and len(up) == expected:
            return last
        time.sleep(1)
    print(f"holdout did not reach {expected} running containers", flush=True)
    raise SystemExit(1)


def _assert_network() -> None:
    proc = _run(["docker", "network", "inspect", NETWORK, "--format", "{{.Internal}}"])
    value = proc.stdout.strip()
    print(f"network {NETWORK} internal={value}", flush=True)
    if proc.returncode != 0 or value != "true":
        print(proc.stderr, end="")
        raise SystemExit(f"network {NETWORK} is not internal")


def _assert_no_ports(rows: list[tuple[str, str, str]]) -> None:
    for name, _status, ports in rows:
        if ports:
            raise SystemExit(f"{name} published ports: {ports}")
        proc = _run(["docker", "inspect", "--format", "{{json .HostConfig.PortBindings}}", name])
        if proc.returncode != 0:
            raise SystemExit(f"inspect failed for {name}")
        bindings = proc.stdout.strip()
        if bindings not in {"null", "{}", ""}:
            raise SystemExit(f"{name} port bindings {bindings}")


def _assert_env_names() -> None:
    count = 0
    for path in sorted((OUT / "plants").glob("*.json")):
        plant = json.loads(path.read_text())
        expected = set(plant["env_names"]) | {"OPENCLAW_STATE_DIR", "OPENCLAW_CONFIG_PATH"}
        proc = subprocess.run(
            ["docker", "exec", "-i", plant["id"], "node", "-"],
            input=ENV_JS.encode(),
            capture_output=True,
            check=False,
        )
        if proc.returncode != 0:
            raise SystemExit(f"env read failed for {plant['id']}")
        present = set(proc.stdout.decode().splitlines())
        missing = sorted(expected - present)
        if missing:
            print(f"{plant['id']} missing env names: {', '.join(missing)}", flush=True)
            raise SystemExit(1)
        comm = _run(["docker", "exec", plant["id"], "cat", "/proc/1/comm"])
        if comm.stdout.strip() != "sleep":
            raise SystemExit(f"{plant['id']} pid 1 is {comm.stdout.strip()!r}")
        count += 1
    print(f"pid 1 is sleep on {count} holdout containers", flush=True)


def _remove_labeled() -> None:
    proc = _run(["docker", "ps", "-aq", "--filter", "label=clawscore.holdout=1"])
    ids = [line.strip() for line in proc.stdout.splitlines() if line.strip()]
    if not ids:
        return
    print("docker rm -f " + " ".join(ids), flush=True)
    rc = subprocess.call(["docker", "rm", "-f", *ids])
    if rc != 0:
        raise SystemExit(rc)


def up(manifest: Path) -> None:
    EVIDENCE.mkdir(parents=True, exist_ok=True)
    rc = subprocess.call(
        [sys.executable, str(ROOT / "fleet" / "gen_lab.py"), "--holdout", str(manifest), "--out", str(OUT)]
    )
    if rc != 0:
        raise SystemExit(rc)
    down(remove_only=False, quiet_missing=True)
    _build()
    _up()
    rows = _wait_running()
    _assert_network()
    _assert_no_ports(rows)
    _assert_env_names()
    print("holdout-lab-up ok", flush=True)


def down(remove_only: bool = False, quiet_missing: bool = False) -> None:
    if COMPOSE.is_file():
        print("docker compose down", flush=True)
        rc = subprocess.call(["docker", "compose", "-f", str(COMPOSE), "down", "--remove-orphans"])
        if rc != 0 and not quiet_missing:
            raise SystemExit(rc)
    elif not quiet_missing and not remove_only:
        print("no fleet-holdout/compose.yaml", flush=True)
    _remove_labeled()


def _agent_rows(view: dict) -> list[dict]:
    rows = []
    for agent in view.get("agents") or []:
        rows.append(
            {
                "name": agent.get("name") or "",
                "version": agent.get("version") or "",
                "process": agent.get("process") or "",
                "device": agent.get("device") or "",
                "user": agent.get("user") or "",
                "autoApprove": agent.get("autoApprove") or "",
                "mcpServers": list(agent.get("mcpServers") or []),
            }
        )
    return rows


def _ensure_observed_at() -> None:
    path = EVIDENCE / "observed-at.txt"
    if path.is_file() and path.read_text().strip():
        return
    moment = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    EVIDENCE.mkdir(parents=True, exist_ok=True)
    path.write_text(moment + "\n")


def scan() -> dict:
    hosts = OUT / "hosts.txt"
    view_path = OUT / "defender_view.json"
    if not hosts.is_file() or not view_path.is_file():
        raise SystemExit("fleet-holdout is missing; run holdout-lab-up first")
    allowed = _holdout_names()
    names = [line.strip() for line in hosts.read_text().splitlines() if line.strip()]
    view = json.loads(view_path.read_text())
    rows = _agent_rows(view)
    by_device = {row["device"]: row for row in rows}
    db = load_db()
    installs = []
    log_lines = []
    for name in names:
        if not NAME_RE.fullmatch(name):
            raise SystemExit(f"refusing holdout target name: {name}")
        if name not in allowed:
            raise SystemExit(f"refusing target that is not a labeled holdout container: {name}")
        root = discover_install_root(name)
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
            mapped = report_for_versions([])
            mapped["note"] = "version was not identified"
            mapped["vulnerable"] = False
        else:
            listed = list_paths(name, root)

            def fetch(rels, container=name, install_root=root):
                return hash_paths(container, install_root, rels)

            ident = identify(listed, fetch, db)
            files_read_abs = [f"{root}/{rel}" for rel in ident["files_read"]]
            for abs_path in files_read_abs:
                log_lines.append(f"{name}\t{abs_path}")
            ident["files_read"] = files_read_abs
            blast = analyze_container(name, work_dir_from_root(root))
            if ident["verdict"] == "unknown":
                mapped = report_for_versions([])
                mapped["note"] = "version was not identified"
                mapped["vulnerable"] = False
            else:
                mapped = report_for_versions(ident["candidates"])
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
                "files_read": ident["files_read"],
                "cves": mapped["cve_ids"],
                "ghsa_ids": mapped["ghsa_ids"],
                "ghsa_only": rows_for_install(ident["version"], ident["candidates"], ident["verdict"]),
                "advisory_count": mapped["advisories"],
                "advisory_critical": mapped["critical"],
                "advisory_high": mapped["high"],
                "advisory_note": mapped["note"],
                "vulnerable": mapped["vulnerable"],
                "feed_newest": FEED_NEWEST,
                "credentials": blast["credentials"],
                "mcp_servers": blast["mcp_servers"],
                "auto_approve": blast["auto_approve"],
                "config_paths": blast["config_paths"],
                "agent365": by_device.get(name),
            }
        )
    document = {
        "feed_newest": FEED_NEWEST,
        "osv_snapshot_sha256": snapshot_sha256(),
        "installs": installs,
        "fix_order": fix_order(installs),
        "agent365_rows": rows,
        "agent365_row_count": len(rows),
    }
    document["summary"] = summary_from_scan(document)
    EVIDENCE.mkdir(parents=True, exist_ok=True)
    (EVIDENCE / "scan.json").write_text(json.dumps(document, indent=2, sort_keys=True) + "\n")
    (EVIDENCE / "files-read.log").write_text("\n".join(log_lines) + ("\n" if log_lines else ""))
    _ensure_observed_at()
    (EVIDENCE / "ps.txt").write_text(_ps_text())
    print(f"wrote {EVIDENCE / 'scan.json'} installs={len(installs)}", flush=True)
    return document


def report() -> int:
    report_or_refuse(git_head(), git_porcelain())
    scan_path = EVIDENCE / "scan.json"
    observed = EVIDENCE / "observed-at.txt"
    if not scan_path.is_file():
        raise SystemExit("evidence/holdout/scan.json is missing")
    if not observed.is_file():
        raise SystemExit("evidence/holdout/observed-at.txt is missing")
    data = write_report(scan_path, EVIDENCE / "report", observed)
    print(f"wrote {EVIDENCE / 'report'} installs={len(data['installs'])}", flush=True)
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="python3 -m clawscore_fleet.holdout_lab")
    sub = parser.add_subparsers(dest="cmd", required=True)
    up_parser = sub.add_parser("up")
    up_parser.add_argument("--manifest", required=True)
    sub.add_parser("down")
    sub.add_parser("scan")
    sub.add_parser("report")
    args = parser.parse_args(argv)
    if args.cmd == "up":
        up(Path(args.manifest))
        return 0
    if args.cmd == "down":
        down()
        return 0
    if args.cmd == "scan":
        scan()
        return 0
    if args.cmd == "report":
        return report()
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
