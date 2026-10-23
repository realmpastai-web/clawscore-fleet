# clawscore-idle-paths (Hark, frozen 2026-10-18)
This replaces the unevidenced `~/.local/share/openclaw` path in `../rea-gate-idle-linux/build_fixture.py` with the install roots the shipped OpenClaw installers actually write. The installers were read statically from sources/ and never executed; see sources/PINS.tsv for their URLs and sha256s.

| id | root | evidence |
|---|---|---|
| L1 | /usr/lib/node_modules/openclaw | install.sh `install -g` on the system prefix (sudo npm i -g) |
| L2 | ~/.npm-global/lib/node_modules/openclaw | install.sh `npm config set prefix "$HOME/.npm-global"` |
| L3 | ~/.openclaw/tools/node-v24.21.0/lib/node_modules/openclaw | install-cli.sh: default prefix ~/.openclaw, `node_dir`=${PREFIX}/tools/node-v${NODE_VERSION}, `install -g --prefix "$(node_dir)"` |
| L3s | same as L3, package.json without version | ClawScore claim 3 (version recovery) |

Run: `python3 gate_idle_paths.py`. The output matches gate-output.txt and ends in GATE PASS.

**Result:**
- osquery 5.23.1 and Wazuh 4.14.9 see L1 and L2 with their versions, and miss L3 and L3s. Their default path lists are parsed from frozen source.
- ClawScore's reference discovery finds all 4 at 2026.4.15. L3s gets its version from dist/build-info.json.

**Limits:**
- Each comparator is an emulation of its default path list, not a run of the real agent.
- osquery can still reach L3 with an explicit `directory=` constraint.
- install.sh's nvm route is covered by both tools (nvm paths).
- The git install method (~/openclaw checkout plus a ~/.local/bin wrapper) is not modelled: UNPROVEN.

Re-check 2026-10-18 against main 90c2ae4:
- This folder holds checksum 10/10 OK. The gate output is byte-identical (17 PASS, GATE PASS). The positioning checksum is OK.
- These inputs do not depend on main, so none of them moved.
- Only the CURSOR_TASK was re-frozen. It now points at #4's real code, clawscore_fleet/fixtures/idle_linux.py and clawscore_fleet/idle_linux.py, and keeps inputs/rea-gate-idle-linux frozen.
