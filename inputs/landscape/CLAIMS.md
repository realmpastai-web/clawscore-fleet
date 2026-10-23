# Cited claims, OpenClaw landscape (retrieved 2026-10-17 ~15:50 IST)

Each claim lists its source query, the snapshot file and the snapshot's SHA-256. Re-run with `python3 recompute.py`.

| # | Claim | Value | Source | Snapshot (sha256) |
|---|---|---|---|---|
| 1 | Total GHSA advisories affecting openclaw | 760 | GET https://api.github.com/advisories?affects=openclaw&ecosystem=npm&per_page=100 (all pages via Link rel=next) | ghsa-all.json (abc7b44d833c8961…) |
| 2 | Severity split crit/high/med/low | 26/266/392/76 | GET https://api.github.com/advisories?affects=openclaw&ecosystem=npm&per_page=100 (all pages via Link rel=next) | ghsa-all.json (abc7b44d833c8961…) |
| 3 | Advisories with a CVE id | 452 | GET https://api.github.com/advisories?affects=openclaw&ecosystem=npm&per_page=100 (all pages via Link rel=next) | ghsa-all.json (abc7b44d833c8961…) |
| 4 | Publish date range | 2026-02-04 to 2026-07-02 | GET https://api.github.com/advisories?affects=openclaw&ecosystem=npm&per_page=100 (all pages via Link rel=next) | ghsa-all.json (abc7b44d833c8961…) |
| 5 | Known advisories affecting 2026.4.22 (crit/high) | 101 (1/53) | GHSA ranges matched against version, see recompute.py | version-vulns.json (30a0e9bf7bb5a81f…) |
| 6 | Known advisories affecting 2026.4.20 | 119 | same | version-vulns.json |
| 7 | Known advisories affecting 2026.1.29 | 712 | same | version-vulns.json |
| 8 | Stable npm releases | 117 | GET https://registry.npmjs.org/openclaw | versions.json (6e2b3ff8619dba5c…) |
| 9 | Releases with dist/cli.runtime.js + dist/abort.runtime.js | 71 (from 2026.3.31) | unpkg/jsdelivr file fetch + sha256 | stable-3file.json (d2cc724fd7180650…) |
| 10 | Dist-pair hash collision | 2026.4.7-1 == 2026.4.8 | same | stable-3file.json |

Caveats: the GitHub advisory feed's newest entry is 2026-07-02, so 0 known for later versions means no advisory has been published, not that the version is proven safe. Version-range matching is Hark's own semver-like parser (post-release suffix -N sorts after the base release, beta sorts before it). The repo should re-verify it with a proper library.
