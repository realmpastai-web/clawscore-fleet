# clawscore-host-mode inputs (frozen by Hark 2026-10-18, base main 026f719; internal)
- CURSOR_TASK_clawscore-host-mode.md: the task.
- gate_host_mode.py + build_host_fixture.py: gate S0-S10 on a 5-install host root built from 4 sha512-pinned npm tarballs (sources/npm-openclaw-pins.json).
- gate-output-main-026f719.txt: main fails S0 (no scan-host), exit 1.
- controls/: synthetic-good-scan.json passes (gate-logic fixture, not scan-host output); mutant-trust-package-json and mutant-unknown-clean fail, exit 1 (logs).
- Reverse: static-reverse.txt, registry-coverage.txt, identify-main-026f719.txt, main-026f719-idle_linux.{json,table,exit,stderr}, main-026f719-code-lines.txt, rea/ (REA attempts; full run is A0).
- expected-advisories-026f719.json: lab truth for 2026.1.29 / 2026.4.15 / 2026.10.4 from main evidence/scan.json (sha256 inside).
