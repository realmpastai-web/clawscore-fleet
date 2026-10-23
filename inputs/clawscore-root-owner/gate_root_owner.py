#!/usr/bin/env python3
"""Root-owned gateway idle gate (frozen by Hark 2026-10-18 against clawscore-fleet 4294427).
Usage: python3 gate_root_owner.py <clawscore-fleet checkout>
Builds 4 fixtures in temp dirs and calls the scanner's discover_all/idle_ok.
R1/R2 must be idle (root's user unit names the install, enabled symlink, linger/root).
C1/C2 are controls that must stay NOT idle so a fix can't just mark /root idle."""
import json, sys, tempfile
from pathlib import Path
repo = Path(sys.argv[1]).resolve(); sys.path.insert(0, str(repo))
from clawscore_fleet.idle_linux import discover_all, idle_ok

UNIT = "[Service]\nExecStart={exe} gateway\n"
def build(root, rel, unit_exec, *, linger=True, enable=True):
    pkg = root / rel; pkg.mkdir(parents=True)
    (pkg / "package.json").write_text(json.dumps({"name": "openclaw", "version": "2026.4.15", "bin": {"openclaw": "openclaw.mjs"}}))
    u = root / "root/.config/systemd/user"; u.mkdir(parents=True)
    (u / "openclaw-gateway.service").write_text(UNIT.format(exe=unit_exec))
    if enable:
        w = u / "default.target.wants"; w.mkdir(); (w / "openclaw-gateway.service").symlink_to("../openclaw-gateway.service")
    if linger:
        l = root / "var/lib/systemd/linger"; l.mkdir(parents=True); (l / "root").write_text("")

CASES = [  # id, install rel, ExecStart, linger, expected idle_ok, expected linger_markers
    ("R1.system_install_root_unit", "usr/lib/node_modules/openclaw", "/usr/lib/node_modules/openclaw/openclaw.mjs", True, True, ["root"]),
    ("R2.root_home_install", "root/.npm-global/lib/node_modules/openclaw", "/root/.npm-global/lib/node_modules/openclaw/openclaw.mjs", True, True, ["root"]),
    ("C1.root_unit_no_linger", "usr/lib/node_modules/openclaw", "/usr/lib/node_modules/openclaw/openclaw.mjs", False, False, []),
    ("C2.root_unit_other_path", "usr/lib/node_modules/openclaw", "/usr/lib/node_modules/openclaw-extra/openclaw.mjs", True, False, []),
]
fails = []
for cid, rel, exe, linger, want_idle, want_markers in CASES:
    with tempfile.TemporaryDirectory() as t:
        root = Path(t); build(root, rel, exe, linger=linger)
        rows = {r["install"]: r for r in discover_all(root)}
        if rel not in rows:
            print(f"FAIL\t{cid}\tinstall not discovered: {sorted(rows)}"); fails.append(cid); continue
        f = rows[rel]; got = (idle_ok(f), f["idle"]["linger_markers"])
        ok = got == (want_idle, want_markers)
        print(f"{'PASS' if ok else 'FAIL'}\t{cid}\twant idle_ok={want_idle} markers={want_markers}\tgot idle_ok={got[0]} idle={json.dumps(f['idle'], sort_keys=True)}")
        ok or fails.append(cid)
print("SUMMARY", f"pass={len(CASES)-len(fails)} fail={len(fails)}", fails); sys.exit(1 if fails else 0)
