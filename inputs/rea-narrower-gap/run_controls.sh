#!/bin/bash
# usage: bash run_controls.sh <clawscore-fleet checkout @756cd2a, e.g. a codeload of 756cd2a>. Expect G0=0, M1=1, M2=1.
C=$1; r(){ python3 -B gate_narrower_gap.py --checkout "$C" "$@" | grep -E "^(FAIL|GATE)"; return ${PIPESTATUS[0]}; }
echo "== G0 real: expect 0"; r; g=$?; echo "exit=$g"
echo "== M1 fabricated Microsoft quote: expect 1"; r --quotes controls/mutant-quotes-fabricated.tsv; m1=$?; echo "exit=$m1"
echo "== M2 weakened verify-report (stripped 2/4, blast 30/42): expect 1"; r --report controls/mutant-verify-report.json; m2=$?; echo "exit=$m2"
[ $g -eq 0 ] && [ $m1 -eq 1 ] && [ $m2 -eq 1 ] && { echo CONTROLS OK; exit 0; }; echo CONTROLS BROKEN; exit 1
