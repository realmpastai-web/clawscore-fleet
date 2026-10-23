# Cited claims, OpenClaw landscape (retrieved 2026-10-17 ~15:50 IST)

Each claim lists its source query, the snapshot file and the snapshot's SHA-256. Re-run with `python3 recompute.py`.

| # | Claim | Value | Source | Snapshot (sha256) |
|---|---|---|---|---|
| 1 | Total GHSA advisories affecting openclaw | 894 | pinned ghsa-all.json (global advisory database plus repository-only advisories); recompute.py | ghsa-all.json (27b020df70c9896d…) |
| 2 | Severity split crit/high/med/low | 26/335/449/84 | same snapshot | ghsa-all.json (27b020df70c9896d…) |
| 3 | Advisories with a CVE id | 459 | same snapshot | ghsa-all.json (27b020df70c9896d…) |
| 4 | Publish date range | 2026-01-31 to 2026-09-11 | same snapshot | ghsa-all.json (27b020df70c9896d…) |
| 5 | Known advisories affecting 2026.4.22 (crit/high) | 148 (1/84); withdrawn (not counted) 33 | GHSA ranges matched against version, see recompute.py | version-vulns.json (254867ae994467d7…) |
| 6 | Known advisories affecting 2026.4.20 | 157; withdrawn (not counted) 41 | same | version-vulns.json |
| 7 | Known advisories affecting 2026.1.29 | 627 (18 critical / 249 high); withdrawn (not counted) 157. npm ecosystem filter drops GHSA-2j9j-gf59-p4p5 and GHSA-mmpf-jwf4-h3qv (both low). On the previous 760-advisory feed the v0.2.2 grammar fix moved this release from 712 to 714 for the GHSA bound "2.0.0-beta3" | same | version-vulns.json |
| 8 | Stable npm releases | 117 | GET https://registry.npmjs.org/openclaw | versions.json (6e2b3ff8619dba5c…) |
| 9 | Releases with dist/cli.runtime.js + dist/abort.runtime.js | 71 (from 2026.3.31) | unpkg/jsdelivr file fetch + sha256 | stable-3file.json (d2cc724fd7180650…) |
| 10 | Dist-pair hash collision | 2026.4.7-1 == 2026.4.8 | same | stable-3file.json |

Caveats: the GitHub advisory feed's newest entry is 2026-09-11, so 0 known for later versions means no advisory has been published, not that the version is proven safe. Version-range matching is Hark's own semver-like parser (post-release suffix -N sorts after the base release, beta sorts before it). The repo should re-verify it with a proper library.
