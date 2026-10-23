# REA brief: openclaw latest 2026.10.5

Frozen before product code. Base commit `d733a8cc79381f9fea140f0e996eb7c2a9b282ee`.
Replay: `python3 inputs/rea-brief-openclaw-latest/replay_q1_q4.py`.
This is not a NO-GO. Q2 on the main db is `unknown`, not `exact`.

Tarballs were packed and sha512-checked, then left out of git. Each file is over GitHub's 100MB limit (`sha512-check.txt`). Extracts live under `.cache/rea-openclaw-extract/` and are not committed. Signature bytes that the fingerprint reads are in `inputs/rea-openclaw-latest-evidence/sig/`.

## Q1

`2026.10.5` is family `runtime`. `fingerprint.family_name` is runtime when both `dist/cli.runtime.js` and `dist/abort.runtime.js` are present (`q1-q3-hashes.json`). The runtime signature file on main is `dist/abort.runtime.js` only (`evidence/fingerprint-set.json`, and `q1-greedy-dry-run.txt`).

| file | 2026.10.4 | 2026.10.5 |
|---|---|---|
| dist/abort.runtime.js | `b4707d245e94b8eac1a9622ecdfcb6b3efb61ea1a42ae10a6b60e71bc4e0b1f6` | `fb7ae248c4555e5c1e90548931970b8ea68a946ab29dcc9947c5666ff92b37ba` |
| dist/cli.runtime.js | `bb479cc1662ad0c83aa8b0f9fec9627378d89a3b5d43cdb147cfc5c24f1b2c37` | `46af0a1a276c656a008d9335ab1339a49f2ecf2dc40bd0afe4f68349bf592301` |

Those hashes differ. Neither hash appears on any of the 117 matrix listings except 2026.10.4's own abort hash. A dry-run of the existing greedy selector with `listing-2026.10.5.json` merged keeps the same signature files and the same unresolved group (`2026.4.7-1`, `2026.4.8`).

## Q2

Main `d733a8c` identifies the 2026.10.5 signature as **unknown** (`q2-identify-main.txt`). The same db identifies 2026.10.4 as exact and `2026.10.10-beta.2` as unknown. `fingerprints/db.json` sha256 at this brief is `06728efac274f1bcc28ce7b3d6735ce6b94370b5ad0589fe10e212ca79e33165`.

## Q3

`diff -rq` of the extracted package trees is `diff-2026.10.4-vs-2026.10.5.txt` (18374 lines: 7818 only in 2026.10.4, 8067 only in 2026.10.5, 2489 content differs).

`dist/.buildstamp` is absent in both trees (`q1-q3-hashes.json`, marks null).

`dist/build-info.json` sha256:

- 2026.10.4 `0c06698a91b39530f8ed544f9a3bd9d7edf598e0de253f6f7b9ed36b5a16d91d`
- 2026.10.5 `b1a6aeee7490b724fa7f1f859872ea71fb46777baaf30e4b914a2ef315fcc429`

Copied bytes: `inputs/rea-openclaw-latest-evidence/sig/<version>/dist/build-info.json`.

## Q4

Fetch time `fetch-time-ist.txt`: `2026-10-20 18:57:58 IST`.
Raw JSON: `gh-global-openclaw.json`, `gh-repo-openclaw-published.json`, `osv-openclaw.json`.
Cutoff is a published date strictly after `2026-09-11`. Counts in `q4-and-counts.json`:

| source | advisories | published after 2026-09-11 | newest published date |
|---|---|---|---|
| GitHub Advisory DB | 760 | 0 | 2026-07-02 |
| openclaw repo security advisories | 722 | 0 | 2026-09-11 |
| OSV npm/openclaw | 590 | 0 | 2026-07-02 |

OSV `modified` max is `2026-09-10`. There is no advisory in these three fetches published after the pinned content date.

Per-version counts, withdrawn rows excluded (`withdrawn_at` on GitHub records; truthy `withdrawn` on OSV). `repo_only` means the ghsa id is absent from the global DB. `landscape_*` is `evidence/landscape/ghsa-all.json`, which this task does not edit.

| version | github_db | repo_only | osv | landscape non-withdrawn |
|---|---|---|---|---|
| 2026.10.5 | 0 | 0 | 0 | 0 |
| 2026.10.4 | 0 | 0 | 0 | 0 |
| 2026.6.10 | 0 | 58 | 0 | 58 |
| 2026.4.22 | 68 | 80 | 67 | 148 |

`2026.4.22` landscape 148 matches the withdrawn gate's counted set. `2026.6.10` 58 and `2026.10.4` 0 match `evidence/landscape/version-vulns.json`.

npm stable releases gained one version, `2026.10.5` (`stable-versions.tsv`). Dist-tag `latest` is `2026.10.5`, published `2026-10-18T21:16:43.569Z` (`registry.json`).

## Q5

UNPROVEN. `npx -y rea-agents@6.7.0 --help` succeeded (`rea-help.log`). `analyze-javascript-application` on the extracted 2026.10.5 package exited 1 with `resource_constraint` after a partial observation (`rea-2026.10.5.summary.json`, `rea-2026.10.5.stderr.log`). Evidence id `ev_99ee139eabfa522bee0eae4446715a62e561196978f171ec6bbcca5320f6ab4d` does not support Q1 or Q3: the run stopped while parsing sources and did not finish a file inventory. The full JSON is 368089909 bytes and is not in git (GitHub rejects files over 100MB). It was moved to `.cache/rea-openclaw-extract/rea-2026.10.5.json`.

Q1 and Q3 stand on the plain-tool files above.

## Spec to build

Do not edit `evidence/landscape/ghsa-all.json` or `evidence/landscape/versions.json`. The withdrawn gate pins those hashes. Do not change `FEED_NEWEST` (`2026-09-11`). That string is the newest advisory publish date, and Q4 shows it is still current. Do not add prereleases to the fingerprint db. Do not run npm or node against an extracted openclaw tree.

### Fingerprints

`clawscore_fleet/build_fingerprints.py` loads matrix listings, then merges `inputs/rea-openclaw-latest-evidence/listing-2026.10.5.json` (array of `[path, sha256]`) as version `2026.10.5` when that key is absent. Greedy runs on the union. `fingerprints/db.json` gains an exact runtime row for `2026.10.5` on `dist/abort.runtime.js` = `fb7ae248c4555e5c1e90548931970b8ea68a946ab29dcc9947c5666ff92b37ba`.

Confusion CSV and dirlist stay on the 117 matrix versions so `make verify-offline` still sees `MATRIX_RELEASE_COUNT`. Collision groups stay the existing groups. `evidence/fingerprint-set.json` runtime version count becomes 73. Copy `fingerprints/db.json` byte-for-byte to `fixtures/db-d733a8c.json` before regenerating it. That copy's sha256 must stay `06728efac274f1bcc28ce7b3d6735ce6b94370b5ad0589fe10e212ca79e33165`.

### Host advisory count

`report_for_versions` keeps the indexed list for versions already in `per_version`. A version that is not in that map is scored by applying `cves._covers` to `evidence/landscape/ghsa-all.json`, withdrawn rows excluded. For `2026.10.5` that count is 0, so `vulnerable` is false and the note is the existing no-advisory wording. An unknown verdict still uses `vulnerable: null`.

### Feed log

`clawscore_fleet/feed_check.py` keeps the live newest-date comparison against `FEED_NEWEST` (so `comparison` stays `same` while the newest repo advisory is `2026-09-11`). `pinned_date` is the first field of `inputs/rea-brief-openclaw-latest/fetch-time-ist.txt` (`2026-10-20`). After the existing lines, append counts from the three raw JSON files in this folder, same rules as Q4, for `2026.10.5`, `2026.10.4`, `2026.6.10`, `2026.4.22`:

```
version_counts withdrawn_excluded=yes
2026.10.5 github_db=0 repo_only=0 osv=0
2026.10.4 github_db=0 repo_only=0 osv=0
2026.6.10 github_db=0 repo_only=58 osv=0
2026.4.22 github_db=68 repo_only=80 osv=67
```

The scan advisory count for an identified build is `github_db + repo_only` (the landscape union). Do not hand-edit README figures. Re-run the existing renderer only if `evidence/verify-report.json` changes.

### Tests

`tests/test_latest_2026_10_5.py`, five tests, fixtures are the committed signature files plus a one-line `package.json` written in a temp root so `scan_host` can discover `home/.../node_modules/openclaw`:

- T1: `fixtures/db-d733a8c.json` on the 2026.10.5 marks => `unknown`.
- T2: regenerated `fingerprints/db.json` on that tree => exact `2026.10.5`.
- T3: same db on the 2026.10.4 marks => exact `2026.10.4`.
- T4: same db on the `2026.10.10-beta.2` tree via `scan_host` => verdict `unknown`, `vulnerable` is null (not false).
- T5: `scan_host` on a 2026.10.5 install => exact `2026.10.5`, `advisory_count` equals that version's `github_db + repo_only` from the feed counter.

### Out of scope

External notes, host scans of a real machine, Defender export changes, merging the PR, editing the withdrawn-gate pins.
