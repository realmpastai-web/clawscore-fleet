#!/usr/bin/env python3
"""Build an idle-Linux openclaw FS fixture: an installed gateway with a systemd USER unit and linger enabled, no running process.
Mirrors the shipped layout evidenced from openclaw@2026.4.15 dist (recon.log). No secret values are written; credential files hold only key NAMES.
Usage: python3 build_fixture.py <outdir>   (default ./fixture)"""
import json, os, sys, hashlib
from pathlib import Path
OUT = Path(sys.argv[1] if len(sys.argv) > 1 else "fixture"); HOME = OUT / "home/claw"
VERSION, COMMIT, BUILT_MS = "2026.4.15", "041266a6699cac3baef8ef39db41fa26f29f9db3", 1776377226517
# shipped js chunk names (hashed) recovered from the real tarball dirlist; used for the dirlist-only fingerprint
NAMES = (Path(__file__).resolve().parent / "dist-names-2026.4.15.txt")
def w(p, s): p.parent.mkdir(parents=True, exist_ok=True); p.write_text(s if isinstance(s, str) else json.dumps(s, indent=1) + "\n")
# 1. installed package, version STRIPPED from package.json (name/bin kept, version/gitHead removed) -> forces build-info/dirlist recovery
pkg = HOME / ".local/share/openclaw/node_modules/openclaw"
w(pkg / "package.json", {"name": "openclaw", "bin": {"openclaw": "openclaw.mjs"}, "main": "dist/index.js"})
w(pkg / "dist/build-info.json", {"version": VERSION, "commit": COMMIT, "builtAt": "2026-04-17T03:37:06+05:30"})
w(pkg / "dist/.buildstamp", json.dumps({"builtAt": BUILT_MS, "head": COMMIT}))
names = [l.strip() for l in NAMES.read_text().splitlines() if l.strip()] if NAMES.is_file() else [f"chunk-{i:04d}.js" for i in range(2147)]
for n in names: w(pkg / "dist" / n, "// shipped chunk\n")
# 2. systemd USER unit (installed, not running) + [Install] WantedBy symlink; NO pid/process
unit = HOME / ".config/systemd/user/openclaw-gateway.service"
w(unit, "[Unit]\nDescription=OpenClaw Gateway\nAfter=network-online.target\nWants=network-online.target\n\n[Service]\n"
        f"ExecStart={pkg}/openclaw.mjs gateway\nRestart=always\nRestartSec=5\nKillMode=control-group\n\n[Install]\nWantedBy=default.target\n")
link = HOME / ".config/systemd/user/default.target.wants/openclaw-gateway.service"
link.parent.mkdir(parents=True, exist_ok=True)
if not link.exists(): os.symlink("../openclaw-gateway.service", link)
# 3. linger enabled: /var/lib/systemd/linger/<user> marker (idle persistence, no process)
w(OUT / "var/lib/systemd/linger/claw", "")
# 4. credential path templates under ~/.openclaw (NAMES ONLY, no values)
w(HOME / ".openclaw/openclaw.json", {"profile": "default", "gateway": {"auth": {"tokenRef": "env:OPENCLAW_GATEWAY_TOKEN"}}})
w(HOME / ".openclaw/.env", "# key names only, no values\nOPENCLAW_GATEWAY_TOKEN=\nANTHROPIC_API_KEY=\n")
w(HOME / ".openclaw/exec-approvals.json", {"approvals": []})
(HOME / ".openclaw/memory").mkdir(parents=True, exist_ok=True)
(HOME / ".openclaw/workspace").mkdir(parents=True, exist_ok=True)
w(HOME / ".openclaw/workspace/IDENTITY.md", "# agent identity (fixture)\n")
# 5. on-disk CHANGELOG with the 30 GHSAs (copied from the real tarball if present, else a 30-id stub)
real = Path("/tmp/rea/2026.4.15/package/CHANGELOG.md")
w(pkg / "CHANGELOG.md", real.read_text() if real.is_file() else "\n".join(f"- GHSA-aa{i:02d}-bb{i:02d}-cc{i:02d}" for i in range(30)))
# manifest hash of the fixture (deterministic, excludes mtimes)
man = sorted(str(p.relative_to(OUT)) for p in OUT.rglob("*") if p.is_file())
(OUT / "FIXTURE_MANIFEST.txt").write_text("\n".join(man) + "\n")
print(json.dumps({"out": str(OUT), "files": len(man), "dist_js": len(names), "version_in_package_json": "version" in json.loads((pkg/"package.json").read_text())}))
