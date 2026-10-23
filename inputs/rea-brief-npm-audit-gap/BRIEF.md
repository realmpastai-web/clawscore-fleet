# REA brief: npm audit gap for openclaw (frozen 2026-10-20, Hark)

## Target (public, shipped)
- The npm CLI 12.2.0 tarball from the registry. Its sha512 integrity matched the registry and its sha256 is 6666b48816b39b86c3febac7b51a4ee4de6c5ca589c382ad8004b6b113f86677.
  Static grep (npm-cli-endpoint-grep.txt): node_modules/@npmcli/arborist/lib/audit-report.js calls npmFetch('/-/npm/v1/security/advisories/bulk').
  That is the endpoint npm audit queries.
- Endpoint: POST https://registry.npmjs.org/-/npm/v1/security/advisories/bulk, body {"openclaw":["<version>"]}.
- ClawScore side: clawscore-fleet main de79e1c5757b626ed6289cc15e94824d7387bac6 (codeload sha256 cc9239ce6a1fd8b5ef3da4cdd189d00622ba8aa0b08653205092002baf009a84).
  - evidence/landscape/ghsa-all.json 27b020df70c9896d7b94280ad0646dc69ef4d27e504d81bc6719dedcb6446034 (feed newest 2026-09-11)
  - inputs/rea-brief-openclaw-latest/gh-global-openclaw.json 4f02bd7f1e9a213c1824e290a716d34e1fe0cfa622516a8f1a425cada7bbb0aa
  - Hark oracle.py 82e0033a310610669bdc0bb51ec2fcd5987ec8444ae83ec04da6c9e7dce02bf6. It agrees with build_index on 117 of 117 versions at PR #16.
- openclaw itself is never installed or run.

## Results (live.log; the offline replay is byte-identical, replay.log)
Raw responses were captured with their timestamps (live/raw/meta-*.json). Server Date was Tue, 20 Oct 2026 17:34:41 GMT for 2026.4.22.

| version | npm audit | ClawScore | overlap | in GitHub DB, not returned | repo-only | npm-only |
|---|---|---|---|---|---|---|
| 2026.4.22 | 67 | 148 | 67 | 1 (GHSA-2j8v-hwgc-x698, listed as "Openclaw") | 80 | 0 |
| 2026.6.10 | 0 | 58 | 0 | 0 | 58 | 0 |
| 2026.1.29 (extra) | 555 | 627 | 555 | 2 (GHSA-2j8v, GHSA-hggm-x7r9-mm7v) | 70 | 0 |

- 67 + 1 + 80 = 148, and 0 + 0 + 58 = 58. Each part is disjoint, and probe.py asserts that the parts sum to the total.
- Response sha256: 2026.4.22 fc192cbb8e0bb87b4165a67d77059404e73ea6cf7b9cf8a33e09d7d793109dae. It is byte-identical to the 23:05 IST probe (rea-npm-audit.tgz 44345ec74d80e02261f38fcd7292a7cfba3249cfa2d21fba7ea582c0c3d85f1d).

## Wording (hard)
- Allowed: "npm audit returned N advisories for openclaw@X on <date>; the maker's repository lists M (feed newest 2026-09-11)."
- Never say a version is safe. Never say npm audit is wrong, misses, or fails: state only what it returned.
- Always pair the two dates: the npm query date and the feed date.

## Observations, inferences, unknowns
- OBSERVED: npm-only = 0 on all three versions, so every advisory npm audit returned is also in ClawScore's set.
- OBSERVED: GHSA-hggm-x7r9-mm7v is live in the GitHub DB, range <= 2026.3.23, first_patched "2026.03.28". npm audit did not return it for 2026.3.23 or 2026.3.22 (hggm.txt).
- INFERENCE, UNPROVEN: the non-semver first_patched "2026.03.28", and the capital-O package name on GHSA-2j8v, keep those rows out of the npm bulk result. npm's backend is not observable, so the report states counts only, never causes.
- UNKNOWN: the endpoint's result can change over time. Every report run re-queries, stores the raw response with its sha256, and prints the query date.

## Skeptic pass
- The feeds are on different dates (npm live on 2026-10-20, ClawScore pinned at 2026-09-11). That gap can only make npm look larger, never smaller, and npm-only = 0 anyway.
- The "maker's repository lists M" phrase covers both global-DB and repo-only rows. All of them carry source openclaw/openclaw. The PR must show this with a count of rows whose source_code_location is not github.com/openclaw/openclaw (expected 0; if not 0, reword to "the GitHub advisory database and the maker's repository list M").
- The script needs network for live mode. Tests use --offline over the committed raw responses.
