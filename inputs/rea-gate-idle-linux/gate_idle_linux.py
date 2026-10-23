#!/usr/bin/env python3
"""rea-gate-idle-linux (Hark, frozen 2026-10-18). Invention gate for the next Cursor task.
Builds the idle-Linux fixture, discovers+recovers version build-info/dirlist only (no execution), and asserts the
CHANGELOG-parsed GHSA set has at least one ID missing from the mock Agent365 export. Exit 0 iff all gates pass.
Usage: python3 gate_idle_linux.py"""
import json, subprocess, sys, hashlib
from pathlib import Path
H = Path(__file__).resolve().parent; FIX = Path("/tmp/rea-gate-fixture")
fails = []
def check(name, ok, detail): 
    print(("PASS" if ok else "FAIL") + "\t" + name + "\t" + detail); 
    (None if ok else fails.append(name))
# G1 fixture builds, idle shape, no process
r = subprocess.run([sys.executable, str(H / "build_fixture.py"), str(FIX)], capture_output=True, text=True)
check("G1.fixture_builds", r.returncode == 0, r.stdout.strip() or r.stderr.strip()[:200])
# G2 discover + recover version WITHOUT package.json version
d = subprocess.run([sys.executable, str(H / "discover_recover.py"), str(FIX)], capture_output=True, text=True)
rec = json.loads(d.stdout) if d.stdout.strip().startswith("{") else {}
check("G2.idle_no_process", d.returncode == 0 and rec.get("idle", {}).get("running_process_evidence") == 0 and rec["idle"]["linger_markers"] and rec["idle"]["user_unit"] and rec["idle"]["enabled_symlink"], json.dumps(rec.get("idle", {})))
check("G2.version_recovered_no_pkg", rec.get("recovered_without_package_version") and not rec["version"]["package_json_has_version"] and rec["version"]["recovered"] == "2026.4.15" and rec["version"]["dirlist_match"], f"recovered={rec.get('version',{}).get('recovered')} dirlist_match={rec.get('version',{}).get('dirlist_match')}")
# G3 CHANGELOG GHSA set has >=1 id missing from the mock Agent365 export
ids = {l.strip() for l in (H / "changelog-ghsa-2026.4.15.txt").read_text().splitlines() if l.strip()}
exp = set(json.loads((H / "mock-agent365-export.json").read_text())["advisories"])
missing = sorted(ids - exp)
check("G3.changelog_ids_30", len(ids) == 30, f"{len(ids)} ids")
check("G3.at_least_1_missing_from_export", len(missing) >= 1, f"{len(missing)} of {len(ids)} CHANGELOG ids absent from export; e.g. {missing[:3]}")
# G4 pinned-feed note: ClawScore's four counts still need the feed CSV (CHANGELOG != feed)
A = {a["ghsa_id"] for a in json.loads((H / "../clawscore-feed-csv-2026-10-17/ghsa-all.json").read_text())}
check("G4.changelog_not_feed", len(ids - A) >= 1, f"{len(ids - A)} CHANGELOG ids not in the pinned feed, so feed CSV stays required")
print(("GATE PASS" if not fails else "GATE FAIL: " + ",".join(fails)))
sys.exit(0 if not fails else 1)
