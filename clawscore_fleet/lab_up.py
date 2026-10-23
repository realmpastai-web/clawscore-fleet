"""make lab-up / lab-down. Images build one version at a time."""

from __future__ import annotations

import json
import os
import subprocess
import sys
import time
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
COMPOSE = ROOT / "fleet" / "compose.yaml"
EVIDENCE = ROOT / "evidence"
NETWORK = "clawscore-lab"
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


def _ps_text() -> str:
    proc = subprocess.run(
        [
            "docker",
            "ps",
            "-a",
            "--filter",
            "label=clawscore.lab=1",
            "--format",
            "{{.Names}}\t{{.Status}}\t{{.Ports}}",
        ],
        capture_output=True,
        text=True,
        check=False,
    )
    if proc.returncode != 0:
        return (proc.stderr or "") + (proc.stdout or "")
    lines = sorted(line for line in proc.stdout.splitlines() if line.strip())
    return "\n".join(lines) + ("\n" if lines else "")


def _write_ps() -> None:
    EVIDENCE.mkdir(parents=True, exist_ok=True)
    text = _ps_text()
    (EVIDENCE / "ps.txt").write_text(text)
    print(text, end="" if text.endswith("\n") or text == "" else "\n", flush=True)


def _lab_versions() -> list[str]:
    manifest = yaml.safe_load((ROOT / "fleet" / "manifest.yaml").read_text())
    seen: list[str] = []
    for item in manifest["installs"]:
        version = item["version"]
        if version not in seen:
            seen.append(version)
    return seen


def _remove_labeled() -> None:
    proc = subprocess.run(
        ["docker", "ps", "-aq", "--filter", "label=clawscore.lab=1"],
        capture_output=True,
        text=True,
        check=False,
    )
    ids = [line.strip() for line in proc.stdout.splitlines() if line.strip()]
    if not ids:
        return
    print("docker rm -f " + " ".join(ids), flush=True)
    rc = subprocess.call(["docker", "rm", "-f", *ids])
    if rc != 0:
        raise SystemExit(rc)


def _build() -> None:
    context = Path("/tmp/clawscore-empty-ctx")
    context.mkdir(parents=True, exist_ok=True)
    env = os.environ.copy()
    env["DOCKER_BUILDKIT"] = "1"
    for version in _lab_versions():
        dockerfile = ROOT / "fleet" / "images" / f"Dockerfile.{version}"
        tag = f"clawscore-openclaw:{version}"
        print(f"docker build -f {dockerfile} -t {tag}", flush=True)
        rc = subprocess.call(
            [
                "docker",
                "build",
                "--progress=quiet",
                "-f",
                str(dockerfile),
                "-t",
                tag,
                str(context),
            ],
            env=env,
        )
        if rc != 0:
            print(f"docker build failed for {tag}; rerunning with plain progress", flush=True)
            rc = subprocess.call(
                [
                    "docker",
                    "build",
                    "--progress=plain",
                    "-f",
                    str(dockerfile),
                    "-t",
                    tag,
                    str(context),
                ],
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


def _rows() -> list[tuple[str, str, str]]:
    rows = []
    for line in _ps_text().splitlines():
        parts = line.split("\t")
        while len(parts) < 3:
            parts.append("")
        rows.append((parts[0].strip(), parts[1].strip(), parts[2].strip()))
    return rows


def _wait_running() -> list[tuple[str, str, str]]:
    deadline = time.time() + 90
    last: list[tuple[str, str, str]] = []
    while time.time() < deadline:
        last = _rows()
        up = [row for row in last if row[1].startswith("Up")]
        if len(last) == 30 and len(up) == 30:
            return last
        time.sleep(1)
    print("lab did not reach 30 running containers", flush=True)
    for name, status, _ports in last:
        if not status.startswith("Up"):
            print(f"logs {name} status={status}", flush=True)
            logs = subprocess.run(
                ["docker", "logs", "--tail", "80", name],
                capture_output=True,
                text=True,
                check=False,
            )
            if logs.stdout:
                print(logs.stdout, end="" if logs.stdout.endswith("\n") else "\n")
            if logs.stderr:
                print(logs.stderr, end="" if logs.stderr.endswith("\n") else "\n")
    raise SystemExit(1)


def _assert_network() -> None:
    proc = subprocess.run(
        ["docker", "network", "inspect", NETWORK, "--format", "{{.Internal}}"],
        capture_output=True,
        text=True,
        check=False,
    )
    value = proc.stdout.strip()
    print(f"network {NETWORK} internal={value}", flush=True)
    if proc.returncode != 0 or value != "true":
        print(proc.stderr, end="")
        raise SystemExit(f"network {NETWORK} is not internal")


def _assert_no_ports(rows: list[tuple[str, str, str]]) -> None:
    for name, _status, ports in rows:
        if ports:
            raise SystemExit(f"{name} published ports: {ports}")
        proc = subprocess.run(
            ["docker", "inspect", "--format", "{{json .HostConfig.PortBindings}}", name],
            capture_output=True,
            text=True,
            check=False,
        )
        if proc.returncode != 0:
            print(proc.stderr, end="")
            raise SystemExit(f"inspect failed for {name}")
        bindings = proc.stdout.strip()
        if bindings not in {"null", "{}", ""}:
            raise SystemExit(f"{name} port bindings {bindings}")


def _assert_env_names() -> None:
    for path in sorted((ROOT / "fleet" / "plants").glob("claw-*.json")):
        plant = json.loads(path.read_text())
        expected = set(plant["env_names"]) | {"OPENCLAW_STATE_DIR", "OPENCLAW_CONFIG_PATH"}
        proc = subprocess.run(
            ["docker", "exec", "-i", plant["id"], "node", "-"],
            input=ENV_JS.encode(),
            capture_output=True,
            check=False,
        )
        if proc.returncode != 0:
            print(proc.stderr.decode()[:2000])
            raise SystemExit(f"env read failed for {plant['id']}")
        present = set(proc.stdout.decode().splitlines())
        missing = sorted(expected - present)
        if missing:
            print(f"{plant['id']} missing env names: {', '.join(missing)}", flush=True)
            raise SystemExit(1)
        comm = subprocess.run(
            ["docker", "exec", plant["id"], "cat", "/proc/1/comm"],
            capture_output=True,
            text=True,
            check=False,
        )
        if comm.stdout.strip() != "sleep":
            raise SystemExit(f"{plant['id']} pid 1 is {comm.stdout.strip()!r}")
    print("pid 1 env names present on 30 containers", flush=True)


def up() -> None:
    down()
    print("generate lab", flush=True)
    rc = subprocess.call([sys.executable, str(ROOT / "fleet" / "gen_lab.py")])
    if rc != 0:
        raise SystemExit(rc)
    _build()
    _up()
    rows = _wait_running()
    _assert_network()
    _assert_no_ports(rows)
    _assert_env_names()
    print("lab-up ok", flush=True)


def down() -> None:
    print("docker compose down", flush=True)
    rc = subprocess.call(
        ["docker", "compose", "-f", str(COMPOSE), "down", "--remove-orphans"]
    )
    _remove_labeled()
    if rc != 0:
        raise SystemExit(rc)


def main() -> int:
    EVIDENCE.mkdir(parents=True, exist_ok=True)
    try:
        if len(sys.argv) > 1 and sys.argv[1] == "down":
            down()
        else:
            up()
        return 0
    finally:
        _write_ps()


if __name__ == "__main__":
    raise SystemExit(main())
