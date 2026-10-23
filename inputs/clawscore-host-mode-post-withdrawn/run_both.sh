#!/bin/bash
# One pass on a withdrawn-fix PR head. Run from the checkout root after:
#   git checkout origin/hark-inputs-2026-10-18 -- inputs/clawscore-withdrawn-reconcile inputs/clawscore-withdrawn-gate inputs/clawscore-host-mode-post-withdrawn
# Both must exit 0 for APPROVE.
set -u
echo "\$ git rev-parse HEAD"; git rev-parse HEAD
for d in clawscore-withdrawn-reconcile clawscore-withdrawn-gate clawscore-host-mode-post-withdrawn; do (cd inputs/$d && sha256sum -c --quiet SHA256SUMS && echo "sums-ok $d $(wc -l < SHA256SUMS)") || exit 2; done
echo "== gate_withdrawn.py"; python3 -B inputs/clawscore-withdrawn-gate/gate_withdrawn.py; w=$?; echo "exit=$w"
echo "== gate_host_mode_post_withdrawn.py"; python3 -B inputs/clawscore-host-mode-post-withdrawn/gate_host_mode_post_withdrawn.py --checkout . ${CACHE:+--cache "$CACHE"}; h=$?; echo "exit=$h"
[ $w -eq 0 ] && [ $h -eq 0 ] && { echo "BOTH PASS"; exit 0; }; echo "BOTH FAIL withdrawn=$w host=$h"; exit 1
