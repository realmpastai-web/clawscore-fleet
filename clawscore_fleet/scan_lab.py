"""make scan: export the mock, then fingerprint the lab containers."""

from __future__ import annotations

import subprocess
import sys
import time
import urllib.request
from pathlib import Path

from clawscore_fleet.blast import selftest
from clawscore_fleet.cli import main as cli_main

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "evidence"
BASE = "http://127.0.0.1:8765"


def _wait_mock() -> None:
    deadline = time.time() + 15
    while time.time() < deadline:
        try:
            with urllib.request.urlopen(BASE + "/agents", timeout=1) as response:
                body = response.read()
            if b"risk" in body.lower():
                raise SystemExit("mock /agents payload contains risk")
            return
        except SystemExit:
            raise
        except Exception:
            time.sleep(0.2)
    raise SystemExit("agent365 mock did not start")


def main() -> int:
    selftest()
    EVIDENCE.mkdir(parents=True, exist_ok=True)
    proc = subprocess.Popen(
        [
            sys.executable,
            "-m",
            "uvicorn",
            "mock_agent365.app:app",
            "--host",
            "127.0.0.1",
            "--port",
            "8765",
            "--log-level",
            "warning",
        ],
        cwd=ROOT,
    )
    try:
        _wait_mock()
        with urllib.request.urlopen(BASE + "/export.csv", timeout=5) as response:
            payload = response.read()
        csv_path = EVIDENCE / "agent365-export.csv"
        csv_path.write_bytes(payload if payload.endswith(b"\n") else payload + b"\n")
        print(f"wrote {csv_path}", flush=True)
        return cli_main(
            [
                "scan",
                "--targets",
                str(ROOT / "fleet" / "hosts.txt"),
                "--agent365",
                str(csv_path),
                "--out",
                str(EVIDENCE),
            ]
        )
    finally:
        proc.terminate()
        try:
            proc.wait(timeout=5)
        except subprocess.TimeoutExpired:
            proc.kill()


if __name__ == "__main__":
    raise SystemExit(main())
