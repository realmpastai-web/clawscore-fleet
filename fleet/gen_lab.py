"""Build the 30-install answer key, compose file, and Defender mock view."""

from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from clawscore_fleet.cves import has_critical_or_high  # noqa: E402
from clawscore_fleet.versions import (  # noqa: E402
    LAB_PLAN,
    OLD_BUILD_CUTOFF,
    is_before,
    load_published,
)

def _load_pool() -> dict[str, str]:
    pool = json.loads((ROOT / "fleet" / "secrets-pool.json").read_text())
    if not pool or any(not isinstance(value, str) or not value for value in pool.values()):
        raise SystemExit("secrets pool is empty")
    return pool

BASES = [
    "/srv/agents",
    "/home/node/work",
    "/opt/apps",
    "/var/lib/claw",
    "/app",
    "/workspace",
]

SERVERS = [
    ("github", ["-y", "@modelcontextprotocol/server-github"]),
    ("slack", ["-y", "@modelcontextprotocol/server-slack"]),
    ("filesystem", ["-y", "@modelcontextprotocol/server-filesystem", "/tmp"]),
]

PLAN_VERSIONS = [version for version, count in LAB_PLAN for _ in range(count)]
FIRST_STRIP = {
    "2026.1.29": ("removed", None),
    "2026.2.14": ("false-version", "2026.10.4"),
    "2026.3.28": ("removed", None),
    "2026.4.7-1": ("false-version", "2026.4.22"),
}


def _server(index: int, env_names: list[str]) -> tuple[str, dict]:
    name, args = SERVERS[index]
    return name, {"command": "npx", "args": args, "env_names": env_names}


def _install(i: int) -> dict:
    number = i + 1
    ident = f"claw-{number:02d}"
    version = PLAN_VERSIONS[i]
    base = BASES[(i * 5) % len(BASES)]
    work = f"{base}/{ident}"
    state = f"{work}/.openclaw"
    pool_names = list(POOL)
    mcp_count = i % 4
    n_secrets = (i // 4) % 4
    secrets = [pool_names[(i + k) % len(pool_names)] for k in range(n_secrets)]
    if len(set(secrets)) != len(secrets):
        raise SystemExit(f"duplicate secrets on {ident}")
    if mcp_count == 0 or n_secrets == 0:
        env_names = list(secrets)
        mcp_secrets: list[str] = []
    elif n_secrets == 1 and i % 2 == 1:
        env_names = []
        mcp_secrets = list(secrets)
    else:
        env_names = secrets[:1]
        mcp_secrets = secrets[1:]
    openclaw_servers: dict = {}
    extra_files = []
    leftover = list(mcp_secrets)
    if mcp_count >= 1:
        take = [leftover.pop(0)] if leftover else []
        name, spec = _server(0, take)
        openclaw_servers[name] = spec
    if mcp_count >= 2:
        take = [leftover.pop(0)] if leftover else []
        name, spec = _server(1, take)
        extra_files.append(
            {
                "path": f"{work}/.mcp.json",
                "format": "mcpServers",
                "servers": {name: spec},
            }
        )
    if mcp_count >= 3:
        take = [leftover.pop(0)] if leftover else []
        name, spec = _server(2, take)
        extra_files.append(
            {
                "path": f"{state}/mcp/extra.json",
                "format": "single",
                "name": name,
                "server": spec,
            }
        )
    if leftover:
        if extra_files:
            last = extra_files[-1]
            if last["format"] == "mcpServers":
                spec = next(iter(last["servers"].values()))
            else:
                spec = last["server"]
            spec["env_names"].extend(leftover)
        elif openclaw_servers:
            spec = next(iter(openclaw_servers.values()))
            spec["env_names"].extend(leftover)
        else:
            env_names.extend(leftover)
        leftover = []
    mode, false_version = "none", None
    mcp_servers = sorted(
        list(openclaw_servers)
        + [next(iter(item["servers"])) for item in extra_files if item["format"] == "mcpServers"]
        + [item["name"] for item in extra_files if item["format"] == "single"]
    )
    if i % 5 == 0:
        agent_version = ""
    elif i % 5 == 2:
        agent_version = "2026.10.4" if version != "2026.10.4" else "2026.4.15"
        if agent_version == version:
            raise SystemExit(f"stale version equals truth for {ident}")
    else:
        agent_version = version
    return {
        "id": ident,
        "version": version,
        "work_dir": work,
        "state_dir": state,
        "install_root": f"{work}/node_modules/openclaw",
        "stripped": mode,
        "false_version": false_version,
        "auto_approve": number % 2 == 1,
        "user": "root",
        "process": "sleep",
        "env_names": env_names,
        "credentials": sorted(set(env_names + mcp_secrets)),
        "mcp_servers": mcp_servers,
        "mcp_config_count": mcp_count,
        "agent365_version": agent_version,
        "openclaw_servers": openclaw_servers,
        "extra_files": extra_files,
    }


def _dockerfile(version: str) -> str:
    # Non-interactive lab image. npm may rewrite git+https -> git+ssh for libsignal;
    # insteadOf forces HTTPS so builds never wait on missing SSH keys. No ports published.
    return (
        "# syntax=docker/dockerfile:1\n"
        "FROM node:22-slim\n"
        f"# Lab image. npm install pins openclaw@{version}. No ports are published.\n"
        "ENV DEBIAN_FRONTEND=noninteractive\n"
        "ENV GIT_TERMINAL_PROMPT=0\n"
        "RUN apt-get update \\\n"
        " && apt-get install -y --no-install-recommends git openssh-client ca-certificates \\\n"
        " && rm -rf /var/lib/apt/lists/*\n"
        'RUN git config --global --add url."https://github.com/".insteadOf "ssh://git@github.com/" \\\n'
        ' && git config --global --add url."https://github.com/".insteadOf "git@github.com:" \\\n'
        ' && git config --global --add url."https://github.com/".insteadOf "git+ssh://git@github.com/"\n'
        "RUN --mount=type=cache,target=/root/.npm \\\n"
        "    npm install --omit=dev --ignore-scripts --no-audit --no-fund "
        f"--fetch-retries=5 --prefix /opt/openclaw \"openclaw@{version}\"\n"
    )


def _service(install: dict) -> dict:
    ident = install["id"]
    return {
        "image": f"clawscore-openclaw:{install['version']}",
        "pull_policy": "never",
        "container_name": ident,
        "hostname": ident,
        "entrypoint": ["/bin/sh", "/opt/lab/entrypoint.sh"],
        "environment": {"LAB_PLANT": "/opt/lab/plant.json"},
        "volumes": [
            "./entrypoint.sh:/opt/lab/entrypoint.sh:ro",
            "./apply-plant.js:/opt/lab/apply-plant.js:ro",
            "./secrets-pool.json:/opt/lab/secrets-pool.json:ro",
            f"./plants/{ident}.json:/opt/lab/plant.json:ro",
        ],
        "networks": ["labnet"],
        "labels": {"clawscore.lab": "1"},
        "restart": "no",
        "init": False,
    }


def _plant(install: dict) -> dict:
    return {
        "id": install["id"],
        "work_dir": install["work_dir"],
        "state_dir": install["state_dir"],
        "stripped": install["stripped"],
        "false_version": install["false_version"],
        "auto_approve": install["auto_approve"],
        "env_names": install["env_names"],
        "openclaw_servers": install["openclaw_servers"],
        "extra_files": install["extra_files"],
    }


def _manifest_install(install: dict) -> dict:
    return {
        "id": install["id"],
        "version": install["version"],
        "work_dir": install["work_dir"],
        "state_dir": install["state_dir"],
        "install_root": install["install_root"],
        "stripped": install["stripped"],
        "false_version": install["false_version"],
        "auto_approve": install["auto_approve"],
        "user": install["user"],
        "process": install["process"],
        "credentials": install["credentials"],
        "mcp_servers": install["mcp_servers"],
        "mcp_config_count": install["mcp_config_count"],
        "agent365_version": install["agent365_version"],
    }


def _main_lab() -> None:
    global POOL
    POOL = _load_pool()
    if len(PLAN_VERSIONS) != 30:
        raise SystemExit(f"lab plan has {len(PLAN_VERSIONS)} installs")
    installs = [_install(i) for i in range(30)]
    seen_strip: set[str] = set()
    for item in installs:
        spec = FIRST_STRIP.get(item["version"])
        if spec and item["version"] not in seen_strip:
            item["stripped"], item["false_version"] = spec
            seen_strip.add(item["version"])
    if len({item["id"] for item in installs}) != 30:
        raise SystemExit("install ids are not unique")
    counts: dict[str, int] = {}
    for item in installs:
        counts[item["version"]] = counts.get(item["version"], 0) + 1
    expected = {version: count for version, count in LAB_PLAN}
    if counts != expected:
        raise SystemExit(f"version spread {counts}")
    stripped = [item for item in installs if item["stripped"] != "none"]
    if len(stripped) < 3:
        raise SystemExit("expected at least 3 stripped installs")
    if {item["mcp_config_count"] for item in installs} != {0, 1, 2, 3}:
        raise SystemExit("mcp counts do not cover 0-3")
    planted = sum(len(item["credentials"]) for item in installs)
    if planted < 20:
        raise SystemExit(f"too few planted credentials: {planted}")
    vulnerable = [item for item in installs if has_critical_or_high(item["version"])]
    if not any(item["credentials"] for item in vulnerable):
        raise SystemExit("vulnerable installs have no credentials")
    pre = [item for item in installs if is_before(item["version"], OLD_BUILD_CUTOFF)]
    if len(pre) < 8:
        raise SystemExit(f"old installs {len(pre)}")
    published = load_published()
    months = {published[item["version"]][:7] for item in pre}
    if not {"2026-01", "2026-02", "2026-03"} <= months:
        raise SystemExit(f"old install months {sorted(months)}")
    versions_present = {item["version"] for item in installs}
    if "2026.1.29" not in versions_present or "2026.3.28" not in versions_present:
        raise SystemExit("lab is missing 2026.1.29 or 2026.3.28")
    env_only = mcp_only = False
    for item in installs:
        env_set = set(item["env_names"])
        mcp_set = set(item["credentials"]) - env_set
        if env_set and not mcp_set:
            env_only = True
        if mcp_set and not env_set:
            mcp_only = True
    if not env_only or not mcp_only:
        raise SystemExit(f"secret placement env_only={env_only} mcp_only={mcp_only}")
    blank = [item for item in installs if item["agent365_version"] == ""]
    stale = [item for item in installs if item["agent365_version"] not in {"", item["version"]}]

    fleet = ROOT / "fleet"
    plants = fleet / "plants"
    images = fleet / "images"
    plants.mkdir(parents=True, exist_ok=True)
    images.mkdir(parents=True, exist_ok=True)
    (fleet / "hosts.txt").write_text("".join(f"{item['id']}\n" for item in installs))
    keep = {version for version, _count in LAB_PLAN}
    for path in images.glob("Dockerfile.*"):
        if path.name.split(".", 1)[1] not in keep:
            path.unlink()
    for version in keep:
        (images / f"Dockerfile.{version}").write_text(_dockerfile(version))
    for item in installs:
        (plants / f"{item['id']}.json").write_text(
            json.dumps(_plant(item), indent=2, sort_keys=True) + "\n"
        )
    manifest = {
        "lab": "clawscore-fleet",
        "patch_boundary": "2026.4.22",
        "versions": [version for version, _count in LAB_PLAN],
        "installs": [_manifest_install(item) for item in installs],
    }
    manifest_path = fleet / "manifest.yaml"
    manifest_path.write_text(yaml.safe_dump(manifest, sort_keys=False))
    loaded = yaml.safe_load(manifest_path.read_text())
    for raw, item in zip(loaded["installs"], installs, strict=True):
        if raw["version"] != item["version"]:
            raise SystemExit(f"yaml changed version {item['id']} {raw['version']!r}")
    compose = {
        "name": "clawscore-lab",
        "networks": {"labnet": {"name": "clawscore-lab", "internal": True}},
        "services": {item["id"]: _service(item) for item in installs},
    }
    (fleet / "compose.yaml").write_text(yaml.safe_dump(compose, sort_keys=False))
    agents = []
    for item in installs:
        agents.append(
            {
                "name": "OpenClaw",
                "version": item["agent365_version"],
                "process": item["process"],
                "device": item["id"],
                "user": item["user"],
                "autoApprove": "true" if item["auto_approve"] else "false",
                "mcpServers": list(item["mcp_servers"]),
            }
        )
    view = {"agents": agents}
    blob = json.dumps(view)
    if "risk" in blob.lower():
        raise SystemExit("defender view contains a risk field")
    mock = ROOT / "mock_agent365"
    mock.mkdir(parents=True, exist_ok=True)
    (mock / "defender_view.json").write_text(json.dumps(view, indent=2, sort_keys=True) + "\n")
    print(f"installs {len(installs)}")
    print(f"versions {counts}")
    print(f"planted_credential_rows {planted}")
    print(f"vulnerable {len(vulnerable)}")
    print(f"blank {len(blank)} stale {len(stale)}")
    print(f"old_before_{OLD_BUILD_CUTOFF} {len(pre)} months {sorted(months)}")
    print(f"stripped {[item['id'] + ':' + item['stripped'] + ':' + item['version'] for item in stripped]}")


_HOLD_ID = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_.-]{0,63}$")
_HOLD_MCP = {
    "github": {
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-github"],
        "place": "openclaw",
    },
    "slack": {
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-slack"],
        "place": "mcpjson",
    },
    "filesystem": {
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-filesystem", "/tmp"],
        "place": "extra",
    },
}
_HOLD_BASES = [
    "/srv/holdout",
    "/opt/holdout",
    "/var/holdout",
    "/app/holdout",
    "/workspace/holdout",
    "/home/holdout",
]


def _feed_sha256() -> str:
    path = ROOT / "evidence" / "landscape" / "ghsa-all.json"
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _holdout_service(install: dict) -> dict:
    ident = install["id"]
    return {
        "image": f"clawscore-openclaw:{install['version']}",
        "pull_policy": "never",
        "container_name": ident,
        "hostname": ident,
        "entrypoint": ["/bin/sh", "/opt/lab/entrypoint.sh"],
        "environment": {"LAB_PLANT": "/opt/lab/plant.json"},
        "volumes": [
            "../fleet/entrypoint.sh:/opt/lab/entrypoint.sh:ro",
            "../fleet/apply-plant.js:/opt/lab/apply-plant.js:ro",
            "../fleet/secrets-pool.json:/opt/lab/secrets-pool.json:ro",
            f"./plants/{ident}.json:/opt/lab/plant.json:ro",
        ],
        "networks": ["holdnet"],
        "labels": {"clawscore.holdout": "1"},
        "restart": "no",
        "init": False,
    }


def _mock_version(item: dict) -> str:
    stripped = item["stripped"]
    if stripped == "removed":
        return ""
    if stripped == "false-version":
        return str(item["false_version"])
    return str(item["version"])


def build_holdout(manifest_path: Path, out_dir: Path) -> dict:
    """Write a separate compose project. Does not touch fleet/."""
    raw = json.loads(manifest_path.read_text())
    if not isinstance(raw, dict):
        raise SystemExit("holdout manifest is not an object")
    feed_sha = raw.get("feed_sha256")
    pinned = _feed_sha256()
    if feed_sha != pinned:
        raise SystemExit("holdout feed_sha256 does not match evidence/landscape/ghsa-all.json")
    salt = raw.get("salt")
    if not isinstance(salt, str) or not salt:
        raise SystemExit("holdout salt is missing")
    rows = raw.get("installs")
    if not isinstance(rows, list) or not rows:
        raise SystemExit("holdout installs are missing")
    pool = _load_pool()
    out = out_dir.resolve()
    fleet = (ROOT / "fleet").resolve()
    if out == fleet or fleet in out.parents or out == ROOT.resolve():
        raise SystemExit("holdout --out must not be fleet/ or the repo root")
    installs = []
    seen = set()
    for index, row in enumerate(rows):
        if not isinstance(row, dict):
            raise SystemExit("holdout install is not an object")
        ident = row.get("id")
        if not isinstance(ident, str) or not _HOLD_ID.fullmatch(ident):
            raise SystemExit("holdout install id is not a safe container name")
        if ident in seen:
            raise SystemExit(f"duplicate holdout id {ident}")
        seen.add(ident)
        version = row.get("version")
        if not isinstance(version, str) or not version:
            raise SystemExit(f"{ident} version is missing")
        stripped = row.get("stripped")
        if stripped not in {"none", "removed", "false-version"}:
            raise SystemExit(f"{ident} stripped must be none, removed, or false-version")
        false_version = row.get("false_version")
        if stripped == "false-version":
            if not isinstance(false_version, str) or not false_version:
                raise SystemExit(f"{ident} false_version is missing")
        elif false_version not in {None, ""}:
            raise SystemExit(f"{ident} false_version is set without false-version strip")
        else:
            false_version = None
        if not isinstance(row.get("auto_approve"), bool):
            raise SystemExit(f"{ident} auto_approve is not a boolean")
        credentials = row.get("credentials")
        servers = row.get("mcp_servers")
        if not isinstance(credentials, list) or not all(isinstance(name, str) for name in credentials):
            raise SystemExit(f"{ident} credentials must be a list of names")
        if len(set(credentials)) != len(credentials):
            raise SystemExit(f"{ident} credential names are not unique")
        unknown = sorted(set(credentials) - set(pool))
        if unknown:
            raise SystemExit(f"{ident} credential names are not in the pool: {', '.join(unknown)}")
        if not isinstance(servers, list) or not all(isinstance(name, str) for name in servers):
            raise SystemExit(f"{ident} mcp_servers must be a list of names")
        if any(name not in _HOLD_MCP for name in servers):
            raise SystemExit(f"{ident} mcp_servers must be filesystem, github, or slack")
        if len(set(servers)) != len(servers):
            raise SystemExit(f"{ident} mcp_servers are not unique")
        base = _HOLD_BASES[index % len(_HOLD_BASES)]
        work = f"{base}/{ident}"
        state = f"{work}/.openclaw"
        openclaw_servers: dict = {}
        extra_files = []
        for name in servers:
            spec = {
                "command": _HOLD_MCP[name]["command"],
                "args": list(_HOLD_MCP[name]["args"]),
                "env_names": [],
            }
            place = _HOLD_MCP[name]["place"]
            if place == "openclaw":
                openclaw_servers[name] = spec
            elif place == "mcpjson":
                extra_files.append(
                    {
                        "path": f"{work}/.mcp.json",
                        "format": "mcpServers",
                        "servers": {name: spec},
                    }
                )
            else:
                extra_files.append(
                    {
                        "path": f"{state}/mcp/extra.json",
                        "format": "single",
                        "name": name,
                        "server": spec,
                    }
                )
        installs.append(
            {
                "id": ident,
                "version": version,
                "work_dir": work,
                "state_dir": state,
                "install_root": f"{work}/node_modules/openclaw",
                "stripped": stripped,
                "false_version": false_version,
                "auto_approve": row["auto_approve"],
                "user": "root",
                "process": "sleep",
                "env_names": list(credentials),
                "credentials": sorted(credentials),
                "mcp_servers": sorted(servers),
                "openclaw_servers": openclaw_servers,
                "extra_files": extra_files,
            }
        )
    plants = out / "plants"
    images = out / "images"
    plants.mkdir(parents=True, exist_ok=True)
    images.mkdir(parents=True, exist_ok=True)
    keep_ids = {item["id"] for item in installs}
    keep_versions = {item["version"] for item in installs}
    for path in plants.glob("*.json"):
        if path.stem not in keep_ids:
            path.unlink()
    for path in images.glob("Dockerfile.*"):
        version = path.name[len("Dockerfile.") :]
        if version not in keep_versions:
            path.unlink()
    (out / "hosts.txt").write_text("".join(f"{item['id']}\n" for item in installs))
    for version in sorted(keep_versions):
        (images / f"Dockerfile.{version}").write_text(_dockerfile(version))
    for item in installs:
        (plants / f"{item['id']}.json").write_text(
            json.dumps(_plant(item), indent=2, sort_keys=True) + "\n"
        )
    record = {
        "lab": "clawscore-holdout",
        "salt": salt,
        "feed_sha256": pinned,
        "installs": [
            {
                "id": item["id"],
                "version": item["version"],
                "work_dir": item["work_dir"],
                "state_dir": item["state_dir"],
                "install_root": item["install_root"],
                "stripped": item["stripped"],
                "false_version": item["false_version"],
                "auto_approve": item["auto_approve"],
                "user": item["user"],
                "process": item["process"],
                "credentials": item["credentials"],
                "mcp_servers": item["mcp_servers"],
            }
            for item in installs
        ],
    }
    (out / "manifest.yaml").write_text(yaml.safe_dump(record, sort_keys=False))
    compose = {
        "name": "clawscore-holdout",
        "networks": {"holdnet": {"name": "clawscore-holdout", "internal": True}},
        "services": {item["id"]: _holdout_service(item) for item in installs},
    }
    (out / "compose.yaml").write_text(yaml.safe_dump(compose, sort_keys=False))
    agents = []
    for item in installs:
        agents.append(
            {
                "name": "OpenClaw",
                "version": _mock_version(item),
                "process": "sleep",
                "device": item["id"],
                "user": "root",
                "autoApprove": "true" if item["auto_approve"] else "false",
                "mcpServers": list(item["mcp_servers"]),
            }
        )
    view = {"agents": agents}
    blob = json.dumps(view)
    if "risk" in blob.lower():
        raise SystemExit("defender view contains a risk field")
    (out / "defender_view.json").write_text(json.dumps(view, indent=2, sort_keys=True) + "\n")
    print(f"holdout installs {len(installs)}", flush=True)
    print(f"holdout out {out}", flush=True)
    return record


def main(argv: list[str] | None = None) -> None:
    args = list(sys.argv[1:] if argv is None else argv)
    if not args:
        _main_lab()
        return
    if len(args) == 4 and args[0] == "--holdout" and args[2] == "--out":
        build_holdout(Path(args[1]), Path(args[3]))
        return
    raise SystemExit("usage: gen_lab.py [--holdout MANIFEST --out DIR]")


if __name__ == "__main__":
    main()
