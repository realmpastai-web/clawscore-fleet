# CURSOR TASK: clawscore host mode (read-only scan of a real Linux host)
Frozen by Hark 2026-10-18. Repo realmpastai-web/clawscore-fleet, branch `feat/host-mode` from main **026f719**. This replaces the 2026-10-17 draft (pilot kit 2422445).

**Evidence rule:** every claim needs a file, log or command output behind it. Don't edit anything under `inputs/`.

## Why (the reverse, files in this folder)
- **Version from package.json.** main's only filesystem command, `python -m clawscore_fleet.idle_linux <root>`, takes the version from `package.json` (idle_linux.py:350-352). It compares against a single fingerprint (`fingerprint_version` = 2026.4.15 for every install).
  - **Evidence:** `main-026f719-idle_linux.table`.
  - **Fixture case H5:** its bytes are 2026.1.29 (786 advisories in the lab scan), but its `package.json` says 2026.10.4 (0 advisories). main reports **2026.10.4**.
- **Betas are invisible.** npm has 278 openclaw versions and the db has 117. The 161 missing are 160 prereleases plus 0.0.1, and that includes the current `beta` dist-tag, 2026.10.10-beta.1.
  - **Evidence:** `registry-coverage.txt`; `static-reverse.txt` shows its `dist/abort.runtime.js` sha256 `cefdee8d…` has `db_hits []`.
- **Unknown reads as clean.** An unidentified install is reported clean. `cli._unknown_report()` sets `vulnerable=False` (cli.py:65-69), and `fixorder.fix_order` keeps only truthy `vulnerable` (fixorder.py:7).
  - **Evidence:** `main-026f719-code-lines.txt`.
- **The fix exists already.** main's `fingerprint.identify` + `fingerprints/db.json` already gets all 5 fixture installs right with 1 read each: H4 = unknown, H5 = exact 2026.1.29 (`identify-main-026f719.txt`). Host mode must use it, not package.json.

## Build
1. `clawscore-fleet scan-host --root <path> --out <dir>` (subcommand of `python -m clawscore_fleet.cli`):
   - **Walk:** WALK_TOPS under `--root`, reusing `idle_linux.discover_all` (including root-owner idle).
   - **Identify:** `fingerprint.identify` with `fingerprints/db.json`, read limit 20.
   - **Advisories:** use the lab code path (CVE + GHSA-only). Credential **names** only, never values. Fix target as in the lab.
   - **Output:** `<dir>/scan.json` in the lab install schema, plus:
     - per row: `install_root` (absolute), `declared_version` (package.json, informational only) and `version_mismatch` (exact verdict ≠ declared);
     - an `idle` object;
     - top-level `unidentified` (ids with verdict `unknown`) and `fix_order`.
   - **No-gos:** no network, no docker, no writes outside `--out`.
2. **Unknown is not clean.**
   - Scan-host rows with verdict `unknown` get `vulnerable: null` and `advisory_note: "version was not identified"`. They're listed in `unidentified` and left out of `fix_order`.
   - Lab `scan` keeps its current output (don't change evidence/scan.json).
3. `clawscore-fleet merge --in <dir>... [--defender <csv>] --out <dir>`: concatenate host scan.json files, then run fixorder and export_defender. `unidentified` rows go to the Defender CSV with an empty version and the note.
4. **Tests:**
   - unit tests for `declared_version`/`version_mismatch`, `vulnerable: null` and `merge`;
   - keep `gate_root_owner.py`, the idle_paths gate and gate_v023 (base 58d4925) green.

## Acceptance (fresh clone; any miss = non-zero)
```
A0 npx -y rea-agents@6.5.0 analyze-javascript-application <extracted openclaw-2026.10.10-beta.1 package> --json > evidence/host-mode/rea-beta.json   # sha512 per sources/npm-openclaw-pins.json; record Evidence ID; confirm dist/abort.runtime.js + dist/build-info.json are in its file inventory
A1 cd inputs/clawscore-host-mode && sha256sum -c SHA256SUMS && cd -
A2 python3 inputs/clawscore-host-mode/gate_host_mode.py --checkout .           # GATE PASS (S0-S10); fetches 4 tarballs once into ~/.cache, sha512-checked
A3 for m in trust-package-json unknown-clean; do ! python3 inputs/clawscore-host-mode/gate_host_mode.py --scan-json inputs/clawscore-host-mode/controls/mutant-$m.json; done
A4 python3 inputs/clawscore-root-owner/gate_root_owner.py . && python3 -m unittest discover -s tests
A5 make matrix && make fingerprints && make verify-offline && make lab-up && make scan && make verify   # evidence/scan.json unchanged; gate_v023 fail=0; CI green on the PR head
A6 lab parity: scan-host on each lab container's `docker export` tree gives the same version/verdict/ghsa_ids as evidence/scan.json for all 30
```

## Out of scope
- macOS and Windows hosts.
- Adding prerelease fingerprints to the db. That's a separate decision: today a beta must read `unknown`, never a guessed version.
- System units in /etc/systemd/system, and homes outside /home and /root.
- Any external contact.
