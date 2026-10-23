#!/bin/bash
# Controls on main 3439300 (or any checkout before the withdrawn fix). Run from the repo root.
# C0 main + post-withdrawn expectations -> exit 1 (main still counts withdrawn)
# C1 scratch fix (skip withdrawn_at in cves.build_index) + post-withdrawn expectations -> exit 0
# M1 scratch fix + OLD 026f719 expectations (the original gate) -> exit 1 (proves re-pin is required)
# C2 scratch fix + checkout expected re-pinned IN PLACE to the post-withdrawn set -> exit 0
# M2 scratch fix + checkout expected re-pinned in place to a wrong set (2026.1.29 count 630) -> exit 2 (P2)
set -u
W=inputs/clawscore-host-mode-post-withdrawn/gate_host_mode_post_withdrawn.py
C=${CACHE:-$HOME/.cache/clawscore-host-fixture}
T=$(mktemp -d); git archive HEAD | tar -x -C "$T"; cp -r inputs/clawscore-host-mode-post-withdrawn inputs/clawscore-withdrawn-gate inputs/clawscore-withdrawn-reconcile "$T/inputs/"
echo "== C0 HEAD $(git rev-parse --short HEAD) as-is: expect exit 1"; python3 $W --checkout . --cache "$C"; c0=$?; echo "exit=$c0"
python3 - "$T" <<'P'
import sys, pathlib
p = pathlib.Path(sys.argv[1]) / "clawscore_fleet/cves.py"; s = p.read_text()
old = "    for advisory in advisories:\n        ranges = _openclaw_ranges(advisory)\n"; assert old in s
p.write_text(s.replace(old, "    for advisory in advisories:\n        if advisory.get(\"withdrawn_at\"):\n            continue\n        ranges = _openclaw_ranges(advisory)\n"))
P
echo "== C1 scratch fix + post-withdrawn expectations: expect exit 0"; python3 "$T/$W" --checkout "$T" --cache "$C"; c1=$?; echo "exit=$c1"
echo "== M1 scratch fix + original gate (026f719 expectations): expect exit 1"; python3 "$T/inputs/clawscore-host-mode/gate_host_mode.py" --checkout "$T" --cache "$C"; m1=$?; echo "exit=$m1"
E="$T/inputs/clawscore-host-mode/expected-advisories-026f719.json"
cp inputs/clawscore-host-mode-post-withdrawn/expected-advisories-post-withdrawn.json "$E"
echo "== C2 scratch fix + in-place re-pin to post-withdrawn set: expect exit 0"; python3 "$T/$W" --checkout "$T" --cache "$C"; c2=$?; echo "exit=$c2"
python3 -c "import json,sys;d=json.load(open(sys.argv[1]));d['by_version']['2026.1.29']['advisory_count']+=1;open(sys.argv[1],'w').write(json.dumps(d,indent=2,sort_keys=True)+chr(10))" "$E"
echo "== M2 scratch fix + in-place re-pin to a wrong set: expect exit 2"; python3 "$T/$W" --checkout "$T" --cache "$C"; m2=$?; echo "exit=$m2"
rm -rf "$T"
[ $c0 -eq 1 ] && [ $c1 -eq 0 ] && [ $m1 -eq 1 ] && [ $c2 -eq 0 ] && [ $m2 -eq 2 ] && { echo "CONTROLS OK"; exit 0; }; echo "CONTROLS BROKEN c0=$c0 c1=$c1 m1=$m1 c2=$c2 m2=$m2"; exit 1
