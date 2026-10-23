"""Credential names reachable from MCP config and process environment.

Values are never returned. The helper script prints names only.
"""

from __future__ import annotations

import json
import subprocess
from pathlib import Path

SCRIPT = (Path(__file__).resolve().parent / "blast.js").read_bytes()


class BlastError(RuntimeError):
    pass


def _run_node(argv_tail: list[str], script: bytes = SCRIPT, timeout: int = 60) -> dict:
    proc = subprocess.run(
        ["node", "-", *argv_tail],
        input=script,
        capture_output=True,
        timeout=timeout,
        check=False,
    )
    if proc.returncode != 0:
        err = proc.stderr.decode("utf-8", "replace")[:2000]
        raise BlastError(err or "blast helper failed")
    try:
        return json.loads(proc.stdout.decode("utf-8"))
    except json.JSONDecodeError as exc:
        raise BlastError("blast helper returned non-json") from exc


def analyze_fixture(spec: dict) -> dict:
    return _run_node([json.dumps(spec)])


def analyze_container(container: str, work_dir: str) -> dict:
    spec = json.dumps({"mode": "container", "work_dir": work_dir})
    proc = subprocess.run(
        ["docker", "exec", "-i", container, "node", "-", spec],
        input=SCRIPT,
        capture_output=True,
        timeout=60,
        check=False,
    )
    if proc.returncode != 0:
        err = proc.stderr.decode("utf-8", "replace")[:2000]
        raise BlastError(f"{container}: {err or 'blast helper failed'}")
    try:
        parsed = json.loads(proc.stdout.decode("utf-8"))
    except json.JSONDecodeError as exc:
        raise BlastError(f"{container}: blast helper returned non-json") from exc
    return {
        "credentials": list(parsed.get("credentials") or []),
        "mcp_servers": list(parsed.get("mcp_servers") or []),
        "auto_approve": parsed.get("auto_approve"),
        "config_paths": list(parsed.get("config_paths") or []),
    }


def selftest() -> None:
    sentinel = "SENTINEL_VALUE_DO_NOT_LEAK"
    spec = {
        "mode": "fixture",
        "env_names": [
            "PATH",
            "AWS_ACCESS_KEY_ID",
            "LAB_PLANT",
            "OPENCLAW_STATE_DIR",
            "LOG_LEVEL",
        ],
        "documents": [
            {
                "path": "/tmp/openclaw.json",
                "body": {
                    "autoApprove": True,
                    "env": {"vars": {"LOG_LEVEL": "debug"}},
                    "mcp": {
                        "servers": {
                            "github": {
                                "command": "npx",
                                "env": {"GITHUB_PERSONAL_ACCESS_TOKEN": sentinel},
                            }
                        }
                    },
                },
            },
            {
                "path": "/tmp/.mcp.json",
                "body": {
                    "mcpServers": {
                        "slack": {
                            "command": "npx",
                            "env": {"SLACK_BOT_TOKEN": sentinel, "LOG_LEVEL": "info"},
                        }
                    }
                },
            },
            {
                "path": "/tmp/extra.json",
                "body": {
                    "name": "filesystem",
                    "command": "npx",
                    "env": {"STRIPE_SECRET_KEY": sentinel},
                },
            },
        ],
    }
    raw = subprocess.run(
        ["node", "-", json.dumps(spec)],
        input=SCRIPT,
        capture_output=True,
        timeout=30,
        check=False,
    )
    text = raw.stdout.decode("utf-8", "replace")
    if raw.returncode != 0:
        raise BlastError(raw.stderr.decode()[:2000])
    if sentinel in text:
        raise BlastError("blast helper printed a credential value")
    parsed = json.loads(text)
    creds = parsed["credentials"]
    expected = [
        "AWS_ACCESS_KEY_ID",
        "GITHUB_PERSONAL_ACCESS_TOKEN",
        "SLACK_BOT_TOKEN",
        "STRIPE_SECRET_KEY",
    ]
    if creds != expected:
        raise BlastError(f"fixture credentials {creds} != {expected}")
    if parsed["mcp_servers"] != ["filesystem", "github", "slack"]:
        raise BlastError(f"fixture servers {parsed['mcp_servers']}")
    if parsed["auto_approve"] is not True:
        raise BlastError("fixture autoApprove was not true")
