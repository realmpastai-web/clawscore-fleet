# clawscore-root-owner (frozen 2026-10-18, Hark)
Follow-up from the PR #6 review. Run: `python3 gate_root_owner.py <clawscore-fleet checkout>`.
On main 4294427: SUMMARY pass=2 fail=2 (R1, R2 fail; controls C1, C2 pass), see gate-output-4294427.txt.
Expected after the fix: pass=4 fail=0. Cause and line numbers: CURSOR_TASK_clawscore-root-owner.md.
sources/: systemd.unit man page (user unit search path ~/.config/systemd/user/*), loginctl man page (enable-linger), getent passwd root from the freeze host (home /root).
