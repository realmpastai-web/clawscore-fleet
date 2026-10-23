# Gate: ClawScore withdrawn fix (Hark, 2026-10-18)

Run it on the PR head. The gate needs this folder and `inputs/clawscore-withdrawn-reconcile/` (61cef9c) in the checkout:
```
git checkout <PR head>
git checkout origin/hark-inputs-2026-10-18 -- inputs/clawscore-withdrawn-gate inputs/clawscore-withdrawn-reconcile
(cd inputs/clawscore-withdrawn-gate && sha256sum -c SHA256SUMS)
python3 inputs/clawscore-withdrawn-gate/gate_withdrawn.py      # expect GATE PASS, exit 0
```

## Checks
| Check | Passes when |
|---|---|
| G0 | `ghsa-all.json` (27b020df…), `versions.json` (6e2b3ff8…) and `counted-2026.4.22.tsv` are byte-identical to their pins. The fix must not edit the feed. |
| G1 | The gate's evaluator, run *with* withdrawn rows, reproduces main 026f719 `version-vulns.json` (556bd11e…) exactly. That evaluator is copied verbatim from 026f719 `clawscore_fleet/versions.py` (sha256 2441d1e4…). |
| G2 | Every row of `version-vulns.json` (version, date, total, severity) equals the recompute with `withdrawn_at` advisories excluded. That's 117 rows, none missing and none extra. |
| G3 | The recomputed 2026.4.22 id set equals `counted-2026.4.22.tsv`: 148 ids, split 1 critical, 84 high, 53 medium, 10 low. |
| G4 | The checkout's own `clawscore_fleet.cves.build_index()` gives the same 148 ids for 2026.4.22, and no withdrawn id appears under any version. |

## Main 026f719 fails (`gate-output-main-026f719.txt`)
`G2` fails on 80 of 117 rows (2026.4.22: file 181, expected 148). `G4` fails with code=181 ids and 168 withdrawn ids counted. Result: GATE FAIL, exit 1.

## Controls (`run_controls.sh`, output in `controls-output-main-026f719.txt`)
Run these from main or this branch only, not on the PR. Each case uses a scratch copy:

| Case | Expected | Result |
|---|---|---|
| C0: main as-is | exit 1 | exit 1 |
| C1: minimal fix (skip `withdrawn_at` in `build_index`, regenerate rows) | exit 0, GATE PASS | GATE PASS |
| M1: fixed code, but rows still count withdrawn (the main file) | exit 1 | exit 1 on G2 |
| M2: fixed rows, but code counts withdrawn again | exit 1 | exit 1 on G4 |
| M3: fixed, 2026.4.22 high bumped by 1 | exit 1 | exit 1 on G2 |

Result: CONTROLS OK.

## Not covered
- README and `CLAIMS.md` wording (the 181 on README line 59).
- `gates_v023` SUMS for the regenerated file.
- Check those in review.
