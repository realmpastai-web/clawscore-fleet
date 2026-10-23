# CURSOR TASK: clawscore root-owned gateway idle detection
Repo: realmpastai-web/clawscore-fleet. Branch `fix/root-owner` from main AFTER feat/ghsa-only merges (base at freeze: 4294427).
## Bug (proven by gate-output-4294427.txt)
A gateway run as root (unit in /root/.config/systemd/user, enabled, /var/lib/systemd/linger/root) never reads as idle.
- clawscore_fleet/idle_linux.py:103-108 `_path_owner` maps only home/<user>; root/... installs return None.
- clawscore_fleet/idle_linux.py:246-248 `_idle_for_system` iterates only root/"home" user dirs, so /root's units are never read.
- WALK_TOPS (line 41) already walks "root", so installs there are discovered but their owner is lost.
## Change
1. Treat the scanned `root/` dir as the home of user `root` (home per sources/getent-passwd-root.txt: /root). `_path_owner("root/...")` returns "root".
2. In `_idle_for_system`, scan `root/.config/systemd/user` alongside `home/*`, with the same unit-matching and linger rules.
3. Add the 4 gate cases as unit tests in tests/test_idle_linux.py. Do not edit gate_root_owner.py or anything under inputs/.
## Acceptance
- `python3 inputs/clawscore-root-owner/gate_root_owner.py .` prints `SUMMARY pass=4 fail=0`, exit 0.
- `python3 -m unittest discover -s tests` OK; the existing idle_paths gate stays L1/L2/L3/L3s true.
- Full pipeline green: make matrix && make fingerprints && make verify-offline && make lab-up && make scan && make verify; gate_v023 (base 58d4925) fail=0; CI verify green on the PR head.
- Out of scope: other users' homes outside /home (e.g. /var/lib/<svc>), system-level units in /etc/systemd/system.
