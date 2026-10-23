"""Idle-Linux openclaw filesystem fixture.

Writes the four install layouts from the shipped OpenClaw installers
(static read of inputs/clawscore-idle-paths/sources). L3s keeps the
stripped package.json from the idle-Linux fingerprint and the exact
dist/build-info.json and dist bytes. The output directory is replaced
on every run so the file count does not grow when the manifest from a
previous run is still on disk.
"""

from __future__ import annotations

import json
import os
import shutil
from pathlib import Path

from clawscore_fleet.versions import ROOT

GATE = ROOT / "inputs" / "rea-gate-idle-linux"
NAMES_FILE = GATE / "dist-names-2026.4.15.txt"
CHANGELOG_IDS = GATE / "changelog-ghsa-2026.4.15.txt"
# install-cli.sh DEFAULT_NODE_VERSION (sources/openclaw-install-cli.sh.txt:684).
NODE_VERSION = "24.21.0"
PACKAGE_VERSION = "2026.4.15"
# Paths match gate_idle_paths.LAYOUTS. Home layouts keep that user.
# Installs outside home/<user> use build_fixture's system_owner (default claw1).
LAYOUTS = {
    "L1": "usr/lib/node_modules/openclaw",
    "L2": "home/claw2/.npm-global/lib/node_modules/openclaw",
    "L3": f"home/claw3/.openclaw/tools/node-v{NODE_VERSION}/lib/node_modules/openclaw",
    "L3s": f"home/claw4/.openclaw/tools/node-v{NODE_VERSION}/lib/node_modules/openclaw",
}

# Exact bytes of dist/build-info.json and dist/.buildstamp from the
# openclaw@2026.4.15 tarball (static read). recon.log truncates builtAt.
BUILD_INFO_TEXT = (
    '{\n  "version": "2026.4.15",\n'
    '  "commit": "041266a6699cac3baef8ef39db41fa26f29f9db3",\n'
    '  "builtAt": "2026-04-16T22:07:24.387Z"\n}\n'
)
BUILDSTAMP_TEXT = '{"builtAt":1776377226517,"head":"041266a6699cac3baef8ef39db41fa26f29f9db3"}\n'

# Unconditional lines from the systemd unit renderer in dist/systemd-D3GGnU7N.js.
# WorkingDirectory and Environment lines are omitted because that renderer
# emits them only when those values are present.
UNIT_TEMPLATE = """[Unit]
Description=OpenClaw Gateway
After=network-online.target
Wants=network-online.target
StartLimitBurst=5
StartLimitIntervalSec=60

[Service]
ExecStart={exec_start}
Restart=always
RestartSec=5
RestartPreventExitStatus=78
TimeoutStopSec=30
TimeoutStartSec=30
SuccessExitStatus=0 143
KillMode=control-group

[Install]
WantedBy=default.target
"""


def _refuse(out: Path) -> Path:
    resolved = out.resolve()
    if resolved == Path("/") or resolved == ROOT or resolved in ROOT.parents:
        raise SystemExit(f"refusing to replace {resolved}")
    return resolved


def _write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)


def _dist_names() -> list[str]:
    if not NAMES_FILE.is_file():
        raise SystemExit(f"missing dist name list: {NAMES_FILE}")
    return [line.strip() for line in NAMES_FILE.read_text().splitlines() if line.strip()]


def _changelog_text() -> str:
    if not CHANGELOG_IDS.is_file():
        raise SystemExit(f"missing changelog GHSA list: {CHANGELOG_IDS}")
    ids = [line.strip() for line in CHANGELOG_IDS.read_text().splitlines() if line.strip()]
    return "\n".join(ids) + "\n"


def owner_name(rel: str, system_owner: str = "claw1") -> str:
    """Account that owns an install path.

    Layouts under home/<user> belong to that user. Every other layout
    belongs to system_owner. The default is the split gate_idle_paths.build()
    uses.
    """
    parts = Path(rel).parts
    if len(parts) >= 2 and parts[0] == "home":
        return parts[1]
    return system_owner


def _package_json(keep_version: bool) -> dict:
    body = {"name": "openclaw", "bin": {"openclaw": "openclaw.mjs"}, "main": "dist/index.js"}
    if keep_version:
        body = {
            "name": "openclaw",
            "version": PACKAGE_VERSION,
            "bin": body["bin"],
            "main": body["main"],
        }
    return body


def _home_config(home: Path) -> None:
    _write(
        home / ".openclaw" / "openclaw.json",
        json.dumps({"gateway": {"auth": {"token": ""}}}, indent=1) + "\n",
    )
    _write(
        home / ".openclaw" / ".env",
        "# key names only, no values\nOPENCLAW_GATEWAY_TOKEN=\nANTHROPIC_API_KEY=\n",
    )
    _write(
        home / ".openclaw" / "exec-approvals.json",
        json.dumps({"version": 1, "agents": {}}, indent=1) + "\n",
    )
    (home / ".openclaw" / "memory").mkdir(parents=True, exist_ok=True)
    (home / ".openclaw" / "workspace").mkdir(parents=True, exist_ok=True)
    _write(home / ".openclaw" / "workspace" / "IDENTITY.md", "# IDENTITY.md - Agent Identity\n")


def build_fixture(out: Path, system_owner: str = "claw1") -> dict:
    """Build the fixture into a fresh directory and return the measured counts.

    system_owner is the account written for installs that are not under
    home/<user>. Home layouts keep the user in their path.
    """
    resolved = _refuse(out)
    if resolved.exists():
        shutil.rmtree(resolved)
    resolved.mkdir(parents=True)
    names = _dist_names()
    for layout_id, rel in LAYOUTS.items():
        package = resolved / rel
        keep_version = layout_id != "L3s"
        _write(package / "package.json", json.dumps(_package_json(keep_version), indent=1) + "\n")
        _write(package / "dist" / "build-info.json", BUILD_INFO_TEXT)
        if layout_id == "L3s":
            _write(package / "dist" / ".buildstamp", BUILDSTAMP_TEXT)
            for name in names:
                _write(package / "dist" / name, "// shipped chunk\n")
            _write(package / "CHANGELOG.md", _changelog_text())
        user = owner_name(rel, system_owner)
        home = resolved / "home" / user
        unit = home / ".config" / "systemd" / "user" / "openclaw-gateway.service"
        _write(unit, UNIT_TEMPLATE.format(exec_start=f"/{rel}/openclaw.mjs gateway"))
        link = home / ".config" / "systemd" / "user" / "default.target.wants" / "openclaw-gateway.service"
        link.parent.mkdir(parents=True, exist_ok=True)
        if not link.exists():
            os.symlink("../openclaw-gateway.service", link)
        _write(resolved / "var" / "lib" / "systemd" / "linger" / user, "")
        _home_config(home)
    files = sorted(str(path.relative_to(resolved)) for path in resolved.rglob("*") if path.is_file())
    (resolved / "FIXTURE_MANIFEST.txt").write_text("\n".join(files) + "\n")
    loaded = json.loads((resolved / LAYOUTS["L3s"] / "package.json").read_text())
    return {
        "out": str(resolved),
        "files": len(files),
        "dist_js": len(names),
        "version_in_package_json": "version" in loaded,
        "git_head_in_package_json": "gitHead" in loaded,
    }


def build_global_layout(out: Path, version: str) -> dict:
    """Write one idle-paths host using the default global layout (L1).

    L1 is /usr/lib/node_modules/openclaw, the system prefix from install.sh
    `install -g`. `version` is written into that install's package.json and
    dist/build-info.json. Callers must read the version back from discovery.
    """
    resolved = _refuse(out)
    if resolved.exists():
        shutil.rmtree(resolved)
    resolved.mkdir(parents=True)
    rel = LAYOUTS["L1"]
    package = resolved / rel
    body = {
        "name": "openclaw",
        "version": version,
        "bin": {"openclaw": "openclaw.mjs"},
        "main": "dist/index.js",
    }
    _write(package / "package.json", json.dumps(body, indent=1) + "\n")
    _write(
        package / "dist" / "build-info.json",
        json.dumps({"version": version}, indent=1) + "\n",
    )
    user = owner_name(rel)
    home = resolved / "home" / user
    unit = home / ".config" / "systemd" / "user" / "openclaw-gateway.service"
    _write(unit, UNIT_TEMPLATE.format(exec_start=f"/{rel}/openclaw.mjs gateway"))
    link = home / ".config" / "systemd" / "user" / "default.target.wants" / "openclaw-gateway.service"
    link.parent.mkdir(parents=True, exist_ok=True)
    if not link.exists():
        os.symlink("../openclaw-gateway.service", link)
    _write(resolved / "var" / "lib" / "systemd" / "linger" / user, "")
    _home_config(home)
    return {"out": str(resolved), "layout": rel, "planted_version": version}


def main(argv: list[str] | None = None) -> int:
    import sys

    args = list(sys.argv[1:] if argv is None else argv)
    out = Path(args[0] if args else "fixture")
    print(json.dumps(build_fixture(out)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
