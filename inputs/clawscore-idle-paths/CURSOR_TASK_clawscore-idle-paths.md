CURSOR TASK: ClawScore idle-Linux discovery on the real OpenClaw install roots (L1 /usr/lib, L2 ~/.npm-global, L3 ~/.openclaw/tools/node-v*/lib)
FROZEN 2026-10-18 by Hark. Re-frozen against main 90c2ae4 (PR #5 merged) and PR #4's code at db6e8c5.
- Start only after the rebased PR #4 is approved and merged.
- Branch feat/idle-paths from the main that contains #4. Draft PR only; Hark gates it.
EVIDENCE RULE: no claim without the file, log or command output behind it.
Reverse-first: the install roots come from the shipped installers in sources/, read statically. Never execute them.

Goal: ClawScore finds every idle OpenClaw gateway on the 3 installer roots and reports its version. When package.json has no version, it recovers the version from dist/build-info.json.

Copy this folder (inputs/clawscore-idle-paths/, unchanged) into the branch. It is the evidence for the roots.

Do NOT edit inputs/rea-gate-idle-linux/. It is frozen evidence, and #4's tests/test_idle_linux.py checks its output byte-for-byte. The old path lives in code, and that is what this task fixes.

1. Fixture: clawscore_fleet/fixtures/idle_linux.py
   - build_fixture() currently writes one install at home/<user>/.local/share/openclaw/node_modules/openclaw. No installer evidences that path, so remove it.
   - Write the 4 layouts from gate_idle_paths.py LAYOUTS / build() instead: L1, L2, L3, L3s, for users claw1 to claw4.
   - Give each layout its own systemd USER unit, a default.target.wants symlink, a var/lib/systemd/linger/<user> marker, and no /proc and no pid file.
   - L3s keeps #4's stripped package.json and the exact BUILD_INFO_TEXT and dist bytes. L1, L2 and L3 have version 2026.4.15 in package.json.
2. Discovery: clawscore_fleet/idle_linux.py
   - discover() returns one install and uses unbounded root.rglob. Replace it with discover_all(root) -> list.
   - Walk <root>/usr, /opt, /root and /home only, keeping relative paths of at most 9 parts. Match */node_modules/openclaw/package.json and stop descending once a match is found, exactly like clawscore() in gate_idle_paths.py.
   - Version order: package.json `version` first, then dist/build-info.json `version`.
   - Keep the existing `version_source` field:
     - "package.json" when the version came from package.json
     - VERSION_SOURCE ("build-info+dirlist") when it was recovered
   - Idle per install: its owner's unit + wants symlink + linger marker, with no process.
   - Keep the gates idle_linux_discovered and idle_linux_version_recovered passing. They now read the L3s row.
3. New verify gate `idle_paths` in verify_run.py. On the fixture it must hold that:
   - exactly 4 installs are found, at the 4 LAYOUTS paths
   - all 4 are version 2026.4.15
   - L3s has version_source "build-info+dirlist" and the other three have "package.json"
   - all 4 are idle
4. Do NOT emit claims about other tools. The osquery and Wazuh emulation stays in inputs/ as evidence only.

Acceptance:
- `cd inputs/clawscore-idle-paths && sha256sum -c SHA256SUMS` is OK, and `python3 gate_idle_paths.py` output equals gate-output.txt (GATE PASS, 17 PASS).
- `cd inputs/rea-gate-idle-linux && sha256sum -c SHA256SUMS` stays OK, and that folder is untouched (git diff empty).
- Pipeline: `make matrix && make fingerprints && make verify-offline && make lab-up && make scan && make verify` all exit 0.
- verify-report has idle_paths true and every existing gate still true, including no_regression, agent365_published_schema, idle_linux_discovered and idle_linux_version_recovered.
- Gates rerun on the final head:
  - gate_v023 reports SUMMARY fail=0 (`python3 inputs/clawscore-v0.2.3-gate/gate_v023.py <checkout> <main@58d4925>`)
  - the agent365 gate output is unchanged
- `python3 -m unittest discover -s tests` is OK, plus tests for discover_all covering 4 installs, the depth bound, and the stop at the first node_modules/openclaw match.
- There is no git subprocess anywhere in clawscore_fleet/.
- CI is green on push and on pull_request. Hand back the head SHA, both run IDs and the build log.
