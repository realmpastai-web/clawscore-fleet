# openclaw@2026.4.22: reconciled advisory count (Hark, 2026-10-18)

**Answer: 148 counted advisories cover openclaw@2026.4.22. That is 181 matched minus the 33 withdrawn ones. There are 0 duplicates among the 148 and 0 shared CVE aliases.**
Severity of the 148, using the GitHub-reviewed record where one exists: 1 critical, 84 high, 53 medium, 10 low.

Replay from this folder in a clawscore-fleet checkout (offline, uses `clawscore_fleet.versions`):
```
sha256sum -c SHA256SUMS
python3 reconcile.py | diff - reconcile-output.txt     # empty diff
```
`fetch.sh` re-pulls the public sources (GitHub REST plus the npm registry). Pulled 2026-10-18 13:19 UTC (`sources/PULLED_AT.txt`). A re-pull can differ as advisories change.

## Where 181, 148 and 146 come from (all from `reconcile-output.txt`)
| Set | Matched | Withdrawn | Counted |
|---|---|---|---|
| GitHub Advisory DB, npm `openclaw` (760 advisories) | 101 | 33 | 68 |
| openclaw repo published advisories (722) | 146 unique (147 rows) | 0 | 146 |
| Union by GHSA id | 181 | 33 | **148** |
| Frozen `evidence/landscape/ghsa-all.json` (the README's 181) | 181 | 33 | 148, the same set (`FROZEN_counted == UNION_COUNTED: True`) |
| GitHub's own `affects=openclaw@2026.4.22` filter | 100 | 33 | 67 |

- **148 vs 146.** 146 counts only advisories whose *repo* record names npm `openclaw`. Two more are in the GitHub DB under `openclaw`. Their repo record names a different package:
  - GHSA-77q5-rr5v-x43q: repo package name is empty; DB names `openclaw`, `< 2026.5.7`.
  - GHSA-jvm4-4j77-39p6: repo package is `@openclaw/qqbot`; DB names `openclaw`, `<= 2026.4.27`. The 2026.4.22 tarball ships `dist/extensions/qqbot` (`tarball/tarball-check.txt`), so the code is in openclaw itself.
- **181 − 33 = 148 is exact.** None of the 33 withdrawn ids appears among the published repo advisories (`withdrawn_also_in_repo_published []`). So nothing withdrawn is counted twice.
- **The 33 withdrawn are all GitHub "Duplicate Advisory" entries.** Each maps by title to a counted original (`withdrawn_with_counted_original 33 no_title_match 0`), and the id pairs are in `reconcile-output.txt`. Counting them would double-count 33 issues.
- **One repo row duplicate.** GHSA-q7q8-3mgw-q67r has two openclaw ranges (`<= 2026.5.18`, `<= 2026.5.19-beta.2`), counted once.
- **GitHub's filter is 1 short of our DB match.** GHSA-2j8v-hwgc-x698 lists its package as `Openclaw` (capital O). GitHub's `affects` filter misses it, and our lower-cased match keeps it (npm names are lower-case).
- **Severity depends on the source.** 27 counted advisories carry a different severity in the repo than in the DB. The only critical, GHSA-w4v6-g3wm-w36c, is `medium` in the repo. State the source next to any severity split.
- **Range normalization.** Repo ranges write `<=v2026.4.2` and bare `2026.1.29`. The script drops the `v` and treats a bare version as `=`, as npm semver does. Anything else unparsable exits 2.

## Shipped 2026.4.22 tarball (static only; nothing executed)
- **Integrity:** sha256 `5c055f30846666a42ab509650538f55a1c0e5193f1cca5f9d28bf012d0f6c04e`. Its sha1 and sha512 equal npm `dist.shasum` and `dist.integrity` (`tarball/tarball-check.txt`). 7457 files.
- **Dependency set:** 42 dependencies plus 2 peers (`tarball/dependency-set.tsv`), none of them `@openclaw/*`. There's no `npm-shrinkwrap.json` or `package-lock.json`, so the tarball does not pin transitive versions.
- **Bundled plugins:** 106 are bundled under `dist/extensions` (`tarball/dist-extensions.txt`).
- **Scope of the 148:** advisories against the `openclaw` package only. **Dependency advisories are not in it and are UNPROVEN here.** Without a lockfile they depend on what each install resolved.

## Files
- **`counted-2026.4.22.tsv`:** the 148 ids, each with severity, DB/repo membership, CVE and summary.
- **`reconcile-output.txt`:** the full output, including the 33 withdrawn ids with dates and their originals.
- **`sources/`:** the raw API pulls.
