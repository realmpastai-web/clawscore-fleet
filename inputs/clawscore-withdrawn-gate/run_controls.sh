#!/bin/bash
# Controls for gate_withdrawn.py. Run from a clawscore-fleet checkout of main 026f719 (or this branch).
# Builds a scratch copy, applies a minimal fix (skip withdrawn_at in cves.build_index + regenerate
# version-vulns.json), and checks: fixed -> exit 0; each mutant -> exit 1.
set -u
G=inputs/clawscore-withdrawn-gate/gate_withdrawn.py
T=$(mktemp -d); git archive HEAD | tar -x -C "$T"
cp -r inputs/clawscore-withdrawn-gate inputs/clawscore-withdrawn-reconcile "$T/inputs/" 2>/dev/null
run(){ (cd "$1" && python3 $G "${@:2}" > /tmp/ctl.out; e=$?; tail -1 /tmp/ctl.out; grep '^FAIL' /tmp/ctl.out | cut -f2; echo "exit=$e"; return $e); }
echo "== C0 main as-is (counts withdrawn): expect exit 1"; run . ; c0=$?
echo "== C1 scratch fix (skip withdrawn in build_index, regenerate rows): expect exit 0"
python3 - "$T" <<'P'
import sys, json, pathlib
t = pathlib.Path(sys.argv[1]); p = t / "clawscore_fleet/cves.py"; s = p.read_text()
old = "    for advisory in advisories:\n        ranges = _openclaw_ranges(advisory)\n"
assert old in s
p.write_text(s.replace(old, "    for advisory in advisories:\n        if advisory.get(\"withdrawn_at\"):\n            continue\n        ranges = _openclaw_ranges(advisory)\n"))
sys.path.insert(0, str(t)); from clawscore_fleet import cves
(t / "evidence/landscape/version-vulns.json").write_text(json.dumps(cves.version_vuln_rows(), indent=0))
P
run "$T"; c1=$?
echo "== M1 mutant: fixed code, version-vulns.json still counts withdrawn (main rows): expect exit 1"
run "$T" --version-vulns "$T/inputs/clawscore-withdrawn-gate/controls/mutant-counts-withdrawn-main-026f719.json"; m1=$?
echo "== M2 mutant: fixed rows, code counts withdrawn again (cves.py reverted): expect exit 1"
git show HEAD:clawscore_fleet/cves.py > "$T/clawscore_fleet/cves.py"; run "$T"; m2=$?
echo "== M3 mutant: fixed, one 2026.4.22 high bumped (+1): expect exit 1"
python3 - "$T" <<'P'
import sys, json, pathlib, re
t = pathlib.Path(sys.argv[1]); p = t / "clawscore_fleet/cves.py"; s = p.read_text()
p.write_text(s.replace("    for advisory in advisories:\n        ranges = _openclaw_ranges(advisory)\n", "    for advisory in advisories:\n        if advisory.get(\"withdrawn_at\"):\n            continue\n        ranges = _openclaw_ranges(advisory)\n"))
f = t / "evidence/landscape/version-vulns.json"; rows = json.loads(f.read_text())
for r in rows:
    if r[0] == "2026.4.22": r[2] += 1; r[3]["high"] += 1
f.write_text(json.dumps(rows, indent=0))
P
run "$T"; m3=$?
rm -rf "$T"
[ $c0 -eq 1 ] && [ $c1 -eq 0 ] && [ $m1 -eq 1 ] && [ $m2 -eq 1 ] && [ $m3 -eq 1 ] && echo "CONTROLS OK" && exit 0
echo "CONTROLS BROKEN c0=$c0 c1=$c1 m1=$m1 m2=$m2 m3=$m3"; exit 1
