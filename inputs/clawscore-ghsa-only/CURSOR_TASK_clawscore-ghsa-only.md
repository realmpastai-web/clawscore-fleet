# CURSOR TASK: clawscore-ghsa-only (frozen by Hark 2026-10-18)

## Goal
ClawScore Fleet reports, per discovered OpenClaw install, every **GHSA-only advisory** (one with no CVE id) that affects its version. Each gets a status:
- `affected`: the GitHub range covers the version.
- `possibly_affected`: OSV's introduced..fixed range covers it, but GitHub's range stops at `last_known_affected`.

**Why:** this is the one survivor of `rea-clawscore-survivors` that is a market gap (S1).
- osquery maps no advisories.
- Defender lists no npm software on Linux.
- Wazuh 4.14.9's feed is CVE5 records keyed by cveId, and its alerts hard-code `enumeration="CVE"`.

**Ground truth:** `inputs/clawscore-ghsa-only/` holds a pinned OSV snapshot (sha256 in OSV_SNAPSHOT.json). It lists 59 no-CVE ids, in expected-ghsa-only.json.

**A real miss in main today:** at bdd8c9b, `report_for_versions(["2026.4.7"])` omits GHSA-gfmx-pph7-g46x and GHSA-jf56-mccx-5f3f.
- The GitHub API range is `<= 2026.4.2` (last_known_affected).
- github/advisory-database says `fixed: 2026.4.8`.
- So 2026.4.3 to 2026.4.7 sit in an unknown window that the fleet currently reports as clean.

## Base, branch, inputs
- **Branch:** `feat/ghsa-only` off `main`, **after** the idle-paths PR merges. Reuse its fixture layouts.
- **Read-only inputs:** never modify `inputs/clawscore-ghsa-only/` or any other `inputs/*`. The CI gate checks their SHA256SUMS.
- **Dependencies:** none new. Stdlib plus the existing requirements.

## Build
1. **`clawscore_fleet/ghsa_only.py`.** Load the OSV snapshot from `inputs/clawscore-ghsa-only/sources/osv/osv-query-openclaw-npm.json`, and refuse to run if its sha256 differs from OSV_SNAPSHOT.json. For a version, return the sorted list `[{"id": GHSA, "status": "affected"|"possibly_affected"}]`, built as follows:
   - **No-CVE rule:** an advisory is no-CVE when it has no `CVE-` alias in OSV **and** `cve_id` is null in `evidence/landscape/ghsa-all.json`.
   - **affected:** some openclaw `vulnerable_version_range` in the landscape covers the version. Use the existing `cves.in_range`.
   - **possibly_affected:** not affected by that rule, but an OSV SEMVER range (introduced/fixed/last_affected) covers the version.
   - **Version ordering:** use `versions.hark_key`. Document and unit-test `2026.4.7-1`: hark_key treats `-N` as post-release, while OSV SEMVER would call it a prerelease.
2. **`scan.json` fields.** Each install gets `ghsa_only` (the list above). The document gets a top-level `osv_snapshot_sha256`.
   - Leave `ghsa_ids`, `cves`, the counts and `fix_order` **unchanged**. `possibly_affected` lives only in `ghsa_only`, so every existing matrix number stays byte-identical.
3. **`python3 -m clawscore_fleet.ghsa_only_fixtures --out evidence/ghsa-only`.** Build 5 filesystem fixture hosts, one per version in `expected-ghsa-only.json` (2026.2.1, 2026.3.1, 2026.4.7, 2026.4.15 and 2026.10.4), with the idle-paths fixture builder on its default global layout.
   - Run them through the **same discovery, identify and report path** as a real scan. The version must come from discovery, never from the fixture's label.
   - Write `evidence/ghsa-only/report.json` as `{"osv_snapshot_sha256", "hosts": [{"id", "version", "layout", "version_source", "cves", "ghsa_ids", "ghsa_only"}]}`.
   - Also write a SHA256SUMS for it.
4. **New gate `ghsa_only`** in the gates module, wired into `make matrix` and CI. It runs the commands in steps 1 to 3 of the next section and fails on any non-zero exit.
5. **README claim, and only while the gate passes:** "Lists the OpenClaw advisories that have no CVE id (59 in the OSV snapshot of 2026-10-18) per install, marking the 2026.4.3 to 2026.4.7 window as possibly affected where GitHub's range stops early." Make no claim about other vendors beyond what `rea-clawscore-survivors` proves.

## Acceptance commands (all must pass in CI from a fresh checkout)
```
cd inputs/clawscore-ghsa-only && sha256sum -c SHA256SUMS && python3 gate_ghsa_only.py | diff - gate-output.txt && cd -
python3 -m clawscore_fleet.ghsa_only_fixtures --out evidence/ghsa-only
python3 inputs/clawscore-ghsa-only/gate_ghsa_only.py --report evidence/ghsa-only/report.json      # GATE PASS, exit 0
for m in mutant-drop-one mutant-gap-as-affected; do ! python3 inputs/clawscore-ghsa-only/gate_ghsa_only.py --report inputs/clawscore-ghsa-only/controls/$m.json; done
python3 -m pytest -q                                   # full suite, plus new unit tests for ghsa_only.py (incl. 2026.4.7 gap ids, 2026.4.7-1 ordering, sha mismatch refusal)
make matrix && git diff --exit-code evidence/release-matrix* evidence/cve-map*   # existing numbers unchanged: 117/117, 0 failures
python3 -m clawscore_fleet.gates_v023                  # SUMMARY fail=0 with the new ghsa_only gate listed
```

## Out of scope / do not
- Do not refresh the landscape or the OSV snapshot. Freshness is a separate task.
- Do not fold `possibly_affected` into `ghsa_ids` or into the counts.
- The same gap window also exists for advisories that have CVEs: 13 in the landscape, 10 of them no-CVE. Record it as a follow-up and do not fix it here.
- Do not claim anything about Wazuh 5.x/main, CrowdStrike or SentinelOne.
