# rea-narrower-gap (internal, 2026-10-18)
Question: Agent 365/Defender already show agent versions. Does our narrower gap (exact build -> advisories -> reachable credentials -> fix order) still hold?
Answer: each link HOLDS-NARROWED and the per-install chain HOLDS, on published docs only. The wording is in CLAIMS.md.

Target: 8 Microsoft Learn pages (sources/*.html, fetched 2026-10-18 with curl) and clawscore-fleet main 756cd2a. Static reads only.
```
C=<path to codeload of clawscore-fleet 756cd2a>
cd inputs/rea-narrower-gap && sha256sum -c SHA256SUMS \
 && python3 -B gate_narrower_gap.py --checkout $C | diff - gate-output.txt \
 && bash run_controls.sh $C | diff - controls-output.txt
```
Expected: no diff output. gate-output.txt ends `GATE PASS`, and controls-output.txt ends `CONTROLS OK` (M1 fabricated quote and M2 weakened report both exit 1).
