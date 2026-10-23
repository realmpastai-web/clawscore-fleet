# Post-withdrawn host-mode expectations (Hark, 2026-10-18, base main 3439300)

**What this is:** the host-mode gate frozen at ab18b4e, rerun against expectations for after the withdrawn fix lands.

**Run both gates on a withdrawn-fix PR head:**
```
git checkout origin/hark-inputs-2026-10-18 -- inputs/clawscore-withdrawn-reconcile inputs/clawscore-withdrawn-gate inputs/clawscore-host-mode-post-withdrawn
bash inputs/clawscore-host-mode-post-withdrawn/run_both.sh      # BOTH PASS, exit 0 = APPROVE
```

## Files
- `recompute_expected.py` recomputes the per-version sets from `ghsa-all.json` (27b020df), with `withdrawn_at` advisories excluded. It uses the evaluator frozen in `gate_withdrawn.py` (the verbatim 026f719 grammar) and `report_for_versions` semantics.
- **Control:** the same recompute *with* withdrawn rows must equal `expected-advisories-026f719.json` (14b77eef…) exactly.
- **Output:** `expected-advisories-post-withdrawn.json` (8ce3ae9c…). The run log is `recompute-output-main-3439300.txt`.

| version | host | before | after | dropped (all withdrawn) | after: crit/high/med/low | CVEs |
|---|---|---|---|---|---|---|
| 2026.1.29 | H3, H5 | 786 | 629 | 157 | 18/249/306/56 | 428 → 427 |
| 2026.4.15 | H2 | 217 | 169 | 48 | 1/86/68/14 | 62 |
| 2026.10.4 | H1 | 0 | 0 | 0 | 0 | 0 |

CVE-2026-34508 drops out of 2026.1.29. Its only record is the withdrawn duplicate GHSA-8288-jpqp-95fx.

## How `gate_host_mode_post_withdrawn.py` works
1. **P0:** the checkout's `gate_host_mode.py`, `build_host_fixture.py` and `sources/npm-openclaw-pins.json` must match ab18b4e's sha256.
2. **P1:** the post-withdrawn expected file must match its pin.
3. **P2:** the checkout's own `expected-advisories-026f719.json` must be either the original file or byte-equal to the post-withdrawn set. So a PR can re-pin that file in place, but only to exactly this set.
4. It copies the gate to a temp dir, swaps in the post-withdrawn expected file under the gate's fixed name, and runs `gate_host_mode.py --checkout` unchanged.
5. **Exit codes:** 0 pass, 1 gate fail, 2 a P0, P1 or P2 failure.

## Controls on main 3439300
Run with `run_controls.sh`. The log is `controls-output-main-3439300.txt`.

| Case | Expected exit |
|---|---|
| C0: main as-is | 1 (S2.H2, S2.H3, S6 fail) |
| C1: scratch fix (skip `withdrawn_at` in `build_index`) | 0 |
| M1: scratch fix with the original gate | 1 (shows the re-pin is required) |
| C2: scratch fix with an in-place re-pin to this set | 0 |
| M2: scratch fix with an in-place re-pin to a wrong set | 2 (P2) |

Result: CONTROLS OK.

## Not covered
The host gate does not check `evidence/scan.json` itself. The withdrawn PR must regenerate it (its lab 2026.1.29 / 2026.4.15 rows change), and that needs review.
