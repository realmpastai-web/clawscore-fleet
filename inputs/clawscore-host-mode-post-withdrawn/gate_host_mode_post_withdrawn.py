#!/usr/bin/env python3
"""Run the frozen host-mode gate (ab18b4e) with post-withdrawn expectations (Hark, 2026-10-18).
  python3 inputs/clawscore-host-mode-post-withdrawn/gate_host_mode_post_withdrawn.py --checkout <repo> [--cache DIR] [--expected FILE]
P0 the checkout's gate code is ab18b4e's: gate_host_mode.py, build_host_fixture.py, sources/npm-openclaw-pins.json (sha256 pinned).
P1 the Hark expected-advisories-post-withdrawn.json matches its pin.
P2 the checkout's own inputs/clawscore-host-mode/expected-advisories-026f719.json is either the original 026f719 file
   or byte-equal to the post-withdrawn set (a PR that re-pins it in place must re-pin to exactly this set).
Then copies inputs/clawscore-host-mode to a temp dir, swaps in the post-withdrawn expected file under the gate's
fixed name, and runs gate_host_mode.py --checkout unchanged. Exit = the gate's exit (0 PASS, 1 FAIL), 2 on a P0/P1/P2 failure.
"""
import argparse, hashlib, shutil, subprocess, sys, tempfile
from pathlib import Path
H = Path(__file__).resolve().parent
GATE_CODE = {"gate_host_mode.py": "4db1ff928a876182899b219aabb8dc0aecd3886488425fc2a8f099ad866fa9bf",
             "build_host_fixture.py": "9c4d675975406802d4c92bc80a59028a51ebaed502c0400fbd8c702532eeff08",
             "sources/npm-openclaw-pins.json": "659dbd18c49618e1fb56b91490b4371026aa401926def38c50af9f00486cbed4"}
OLD_EXP_SHA = "14b77eefd897ee450fa32e2a2b4d497aef0dd42aa529f776dd771722ddc8cc37"
POST_SHA = "7c7642a14d362454a079e198c6e574dcfc5a34016a469dd1451f322ace17139a"
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
ap = argparse.ArgumentParser(); ap.add_argument("--checkout", required=True)
ap.add_argument("--cache", default=str(Path.home() / ".cache" / "clawscore-host-fixture"))
ap.add_argument("--expected", default=str(H / "expected-advisories-post-withdrawn.json"))
a = ap.parse_args(); co = Path(a.checkout).resolve(); host = co / "inputs/clawscore-host-mode"
bad = [f"{n}={sha(host / n)[:16] if (host / n).exists() else 'MISSING'}" for n, h in GATE_CODE.items() if not (host / n).exists() or sha(host / n) != h]
p0 = not bad
print(f"{'PASS' if p0 else 'FAIL'}\tP0.gate_code_is_ab18b4e\tbad={bad}")
e = sha(a.expected); p1 = e == POST_SHA
print(f"{'PASS' if p1 else 'FAIL'}\tP1.expected_pin\t{Path(a.expected).name}={e[:16]}{'' if p1 else ' (not the frozen post-withdrawn set)'}")
ce = sha(host / "expected-advisories-026f719.json")
p2 = ce in (OLD_EXP_SHA, POST_SHA)
print(f"{'PASS' if p2 else 'FAIL'}\tP2.checkout_expected_is_original_or_post\t{ce[:16]} ({'original 026f719' if ce == OLD_EXP_SHA else 'post-withdrawn' if ce == POST_SHA else 'OTHER'})")
if not (p0 and p1 and p2):
    print("GATE FAIL [P0/P1/P2]"); sys.exit(2)
with tempfile.TemporaryDirectory() as t:
    g = Path(t) / "clawscore-host-mode"; shutil.copytree(host, g)
    shutil.copyfile(a.expected, g / "expected-advisories-026f719.json")
    print(f"INFO\tgate inputs/clawscore-host-mode from checkout, expected swapped to {Path(a.expected).name}")
    sys.stdout.flush()
    r = subprocess.run([sys.executable, str(g / "gate_host_mode.py"), "--checkout", str(co), "--cache", a.cache])
sys.exit(r.returncode)
