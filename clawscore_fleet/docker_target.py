"""Read lab container filesystems. Targets stay inside the labeled lab."""

from __future__ import annotations

import json
import re
import subprocess

CONTAINER_RE = re.compile(r"^claw-\d{2}$")

DISCOVER_JS = r"""
const fs = require("fs");
const roots = ["/srv", "/home", "/opt", "/var", "/app", "/workspace", "/usr"];
const marks = [
  "dist/cli.runtime.js",
  "dist/abort.runtime.js",
  "dist/.buildstamp",
  "dist/version.js",
  "dist/build-info.json",
  "openclaw.mjs",
  "package.json"
];
const hits = [];
function looksLike(pkg) {
  for (const rel of marks) {
    try { fs.accessSync(pkg + "/" + rel); return true; } catch {}
  }
  return false;
}
function walk(dir, depth) {
  if (depth > 5) return;
  let ents;
  try { ents = fs.readdirSync(dir, { withFileTypes: true }); }
  catch { return; }
  for (const ent of ents) {
    if (ent.name === "proc" || ent.name === "sys" || ent.name === "dev") continue;
    const full = dir + "/" + ent.name;
    let isDir = ent.isDirectory();
    if (ent.isSymbolicLink()) {
      try { isDir = fs.statSync(full).isDirectory(); } catch { isDir = false; }
    }
    if (!isDir) continue;
    if (ent.name === "node_modules") {
      const pkg = full + "/openclaw";
      if (looksLike(pkg)) hits.push(pkg);
      continue;
    }
    walk(full, depth + 1);
  }
}
for (const root of roots) walk(root, 0);
process.stdout.write(JSON.stringify(hits));
"""

LIST_JS = r"""
const fs = require("fs");
const path = require("path");
const root = process.argv[2];
const rootReal = fs.realpathSync(root);
const out = [];
const seen = new Set();
function inside(real) {
  return real === rootReal || real.startsWith(rootReal + path.sep);
}
function walk(dir) {
  let ents;
  try { ents = fs.readdirSync(dir, { withFileTypes: true }); }
  catch { return; }
  for (const ent of ents) {
    const full = path.join(dir, ent.name);
    let real = full;
    let stat;
    try {
      real = fs.realpathSync(full);
      stat = fs.statSync(real);
    } catch { continue; }
    if (!inside(real)) continue;
    if (seen.has(real)) continue;
    seen.add(real);
    if (stat.isDirectory()) walk(real);
    else if (stat.isFile()) out.push(path.relative(rootReal, real));
  }
}
walk(rootReal);
process.stdout.write(JSON.stringify(out));
"""

HASH_JS = r"""
const fs = require("fs");
const path = require("path");
const crypto = require("crypto");
const spec = JSON.parse(process.argv[2]);
const out = {};
for (const rel of spec.rels) {
  if (!rel || rel.includes("..") || path.isAbsolute(rel)) {
    out[rel] = null;
    continue;
  }
  const full = path.join(spec.root, rel);
  try {
    const data = fs.readFileSync(full);
    out[rel] = crypto.createHash("sha256").update(data).digest("hex");
  } catch (err) {
    if (err && err.code === "ENOENT") out[rel] = null;
    else throw err;
  }
}
process.stdout.write(JSON.stringify(out));
"""


class TargetError(RuntimeError):
    pass


def _run(cmd: list[str], timeout: int = 60, stdin: bytes | None = None) -> subprocess.CompletedProcess:
    return subprocess.run(
        cmd,
        input=stdin,
        capture_output=True,
        timeout=timeout,
        check=False,
    )


def lab_container_names() -> set[str]:
    proc = _run(
        [
            "docker",
            "ps",
            "-a",
            "--filter",
            "label=clawscore.lab=1",
            "--format",
            "{{.Names}}",
        ]
    )
    if proc.returncode != 0:
        raise TargetError(proc.stderr.decode()[:2000] or "docker ps failed")
    return {line.strip() for line in proc.stdout.decode().splitlines() if line.strip()}


def assert_lab_target(name: str, allowed: set[str]) -> None:
    if not CONTAINER_RE.fullmatch(name):
        raise TargetError(f"refusing target outside the lab name pattern: {name}")
    if name not in allowed:
        raise TargetError(f"refusing target that is not a labeled lab container: {name}")


def discover_install_root(container: str) -> str | None:
    proc = _run(
        ["docker", "exec", "-i", container, "node", "-"],
        timeout=60,
        stdin=DISCOVER_JS.encode(),
    )
    if proc.returncode != 0:
        raise TargetError(f"{container} discover failed: {proc.stderr.decode()[:2000]}")
    try:
        hits = json.loads(proc.stdout.decode() or "[]")
    except json.JSONDecodeError as exc:
        raise TargetError(f"{container} discover returned non-json") from exc
    preferred = [hit for hit in hits if "/opt/openclaw/" not in hit]
    pool = preferred or hits
    if not pool:
        return None
    return sorted(pool)[0]


def list_paths(container: str, root: str) -> list[str]:
    proc = _run(
        ["docker", "exec", "-i", container, "node", "-", root],
        timeout=120,
        stdin=LIST_JS.encode(),
    )
    if proc.returncode != 0:
        raise TargetError(f"{container} list failed: {proc.stderr.decode()[:2000]}")
    try:
        found = json.loads(proc.stdout.decode() or "[]")
    except json.JSONDecodeError as exc:
        raise TargetError(f"{container} list returned non-json") from exc
    if not isinstance(found, list):
        raise TargetError(f"{container} list returned {type(found).__name__}")
    return [str(item) for item in found]


def hash_paths(container: str, root: str, rels: list[str]) -> dict[str, str | None]:
    spec = json.dumps({"root": root, "rels": rels})
    proc = _run(
        ["docker", "exec", "-i", container, "node", "-", spec],
        timeout=60,
        stdin=HASH_JS.encode(),
    )
    if proc.returncode != 0:
        raise TargetError(f"{container} hash failed: {proc.stderr.decode()[:2000]}")
    try:
        found = json.loads(proc.stdout.decode() or "{}")
    except json.JSONDecodeError as exc:
        raise TargetError(f"{container} hash returned non-json") from exc
    return {rel: found.get(rel) for rel in rels}


def work_dir_from_root(root: str) -> str:
    parent, leaf = root.rstrip("/").rsplit("/", 1)
    base, mid = parent.rsplit("/", 1)
    if leaf == "openclaw" and mid == "node_modules":
        return base
    return parent
