#!/usr/bin/env bash
# Hark repro for CURSOR_TASK_clawscore-v0.2.2. Usage: bash run_repro.sh <clawscore-fleet checkout @ cc29565 or 6ccf7f6> <hark landscape dir (v0.2 inputs)>
set -euo pipefail
R=$1; L=$2; H=$(cd "$(dirname "$0")" && pwd)
echo "== 1. v0.2 log re-judged (5,267 DISAGREE lines, commas stripped, includePrerelease=true)"; python3 $H/repro_crosscheck.py "$R"
echo "== 2. full 39,476 decisions, v0.2 grammar"; python3 $H/repro_full.py "$R" | grep -v '^OTHER' ; python3 $H/repro_full.py "$R" | grep -c '^OTHER'
echo "== 3. full decisions, alpha/rc fix only"; python3 $H/repro_full.py "$R" --fixed-key | grep -v '^OTHER'
echo "== 4. full decisions, alpha/rc + glued betaN fix"; python3 $H/repro_full.py "$R" --fixed-key --glued
echo "== 5. version-vulns regen"; python3 $H/regen_version_vulns.py "$L" --old | sha256sum; sha256sum "$L/version-vulns.json"; python3 $H/regen_version_vulns.py "$L" | sha256sum
