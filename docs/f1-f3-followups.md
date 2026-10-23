# F1–F3 follow-ups after PR #14 (`e8ed6df`)

Evidence cited below is the tree on `fix/f1-f3-followups` at `e8ed6df`. Frozen pins that this change does not edit: `fixtures/db-d733a8c.json` (sha256 `06728efac274f1bcc28ce7b3d6735ce6b94370b5ad0589fe10e212ca79e33165`, `inputs/rea-brief-openclaw-latest/BRIEF.md`), `evidence/landscape/**`, `inputs/clawscore-v0.2.3-gate/**`, `MATRIX_RELEASE_COUNT = 117` in `clawscore_fleet/versions.py`, and the existing 117 listing shard bytes.

## F1 — listing in the store

`clawscore_fleet/build_fingerprints.py` `build()` (lines 210–213) loads `load_listings()`, then if `"2026.10.5"` is absent reads `inputs/rea-openclaw-latest-evidence/listing-2026.10.5.json`. That file is a sorted array of 13982 `[path, sha256]` pairs. `dist/abort.runtime.js` is `fb7ae248c4555e5c1e90548931970b8ea68a946ab29dcc9947c5666ff92b37ba`.

The store is `evidence/matrix/listings/<version>.json.gz`, joined in `evidence/matrix/releases.json` order, checksummed by `evidence/matrix/listings.sha256` (`clawscore_fleet/listings_store.py`). Today `releases.json` `"count"` is 117 and the last row is `2026.10.4`.

Change:

- Delete the version string and the extra path from `build_fingerprints.py`. One sorted list from `load_listings()` feeds greedy selection, the confusion rows, and `_dirlist`.
- Add `evidence/matrix/listings/2026.10.5.json.gz` as `gzip -n -9` of `json.dumps(files, separators=(",", ":"))` (`payload_for` / `gzip_n9`). A round-trip of `2026.10.4.json.gz` through `gzip_n9` was byte-identical, so existing shards are not rewritten.
- Append a `releases.json` row and bump `"count"` to 118. Fields: `version` `2026.10.5`, `published` `2026-10-18T21:16:43.569Z` (`inputs/rea-brief-openclaw-latest/registry.json`), `files` 13982 (listing length and `fileCount` in that registry object), `tarball` `openclaw-2026.10.5.tgz`, `sha256` `dbb1bdcf2346292e25f672822b6a9928c234909abe6fee0df5fc4556e769d40e`. That digest is `sha256sum` of the existing tarball `/workspace/hark-tasks/clawscore-latest-1052/inputs/rea-openclaw-latest-evidence/openclaw-2026.10.5.tgz` (103343430 bytes). Its sha512 matches the registry integrity `sha512-9rCuXMweqVKZIK3KBtGcLzesz9G6+FmQ30lvwomRhmcNWDcOtlBoqdLbPditoJMuTP55jPqXpt1AA0L8tSzFHg==`. A tar read of `package/dist/abort.runtime.js` inside that tarball hashes to `fb7ae248c4555e5c1e90548931970b8ea68a946ab29dcc9947c5666ff92b37ba`. The tarball is not copied into this repo.
- Append the same digest to `evidence/matrix/tarballs.sha256`.
- Recompute `listings.sha256` with `assemble()` over the 117 current payloads plus this payload. The previous pin `b96dec456c1b1c5b3dbc7c525a4b44e2ede4f9d6128e5558a2cc48819b2a0605` is the 117-release assembly. The new file is the checksum of the expanded store.
- `clawscore_fleet/release_matrix.py` `main()` rebuilds shards from `stable_releases()` and `write_payloads()` deletes shards that are not in that list. Preserve release rows whose version is not in the landscape stable set and whose shard is already present: do not `npm pack` them, and pass their decompressed payload through `_write_assembled`. No version string in that code.

Regenerate fingerprints. The greedy set already included this listing via the special case, so `fingerprints/db.json` rows stay byte-identical, including `2026.10.5` / `dist/abort.runtime.js` = `fb7ae248c4555e5c1e90548931970b8ea68a946ab29dcc9947c5666ff92b37ba`. `fixtures/db-d733a8c.json` stays the pre-regeneration copy.

## F2 — matrix rows and dirlist

`matrix_versions` is sorted before the special-case merge (`build_fingerprints.py` lines 210 and 286–302). Confusion CSV and dirlist therefore omit `2026.10.5`. `evidence/dirlist-metric.json` is `117` of `117` (`100.0`). `evidence/verify-report.json` `gates.matrix_exact` is `correct` 115, `non_colliding` 115, `total` 117, `percent_display` `100.0`. README lines match: exact `115 of 115 (100.0%)`, directory listing `117 of 117 (100.0%)`. Tarball coverage `117 of 117` comes from `matrix_gate` over landscape `stable_releases()` and must stay. `make verify` compares those gate objects to `inputs/clawscore-v0.2.3-gate/base-verify-report-58d4925.json` in `no_regression` (`clawscore_fleet/gates_v023.py`). That base file stays pinned.

After the store includes the version, `verify_offline.fingerprint_gates` classifies every listing. It currently requires `len(fresh) == MATRIX_RELEASE_COUNT` and `dirlist["total"] == MATRIX_RELEASE_COUNT` (`verify_offline.py` lines 247 and 262). Point those two comparisons at `len(listings)`. Leave `matrix_gate`'s `MATRIX_RELEASE_COUNT` check on the landscape stable set.

Published figures that change, old then new:

| figure | old | new |
|---|---|---|
| exact classification | 115/115 of 117 (100.0%) | 116/116 of 118 (100.0%), if the new row is exact and outside the `2026.4.7-1` / `2026.4.8` group |
| directory listing | 117/117 (100.0%) | 118/118 (100.0%), if the path digest is unique |
| tarball coverage | 117/117 | 117/117 |

`no_regression` keeps full equality for every other name in `unchanged_gates_vs_base`. For `matrix_exact` and `dirlist_metric`, add the count of release rows that are not in `stable_releases()` to the frozen base's `correct`, `non_colliding`, `total` (exact) and `correct`, `total` (dirlist). That holds only while each such row is exact, non-colliding, and dirlist-unique. Update the two README result lines to the new figures. Do not hand-edit the tarball-coverage line.

## F3 — non-zero unindexed feed control

`tests/test_latest_2026_10_5.py` `test_t5_scan_matches_repinned_feed` compares `scan_host` `advisory_count` to `github_db + repo_only`. Both are 0 for `2026.10.5` (`inputs/rea-brief-openclaw-latest/BRIEF.md`). `scan_host._row` calls `report_for_versions`, which calls `_rows_for_version` (`clawscore_fleet/cves.py` lines 165–178 and 188). Versions absent from `per_version` (the landscape stable set) are scored by `_covers` over `index["advisories"]`. `2026.10.5` is absent and the fallback count is 0, so an empty fallback still passes T5.

Add `test_t6_unindexed_fallback_nonzero` in that module. Version `2026.6.7` is not in `build_index()["per_version"]`. `report_for_versions(["2026.6.7"])["advisories"]` is 61 and `withdrawn_not_counted` is empty (probe of the committed `ghsa-all.json` through `_rows_for_version`). Assert it is not indexed and `advisories == 61`. A fallback that returns no rows yields 0 and fails.

Mutant proof, not a committed edit: make the unindexed branch return `[], []` without reading advisories, run this test, restore the branch, run it again.

## Checks

`pytest -q` and `make verify-offline`. Regenerate `evidence/SHA256SUMS` with `python -m clawscore_fleet.hash_evidence` for files that changed, then `sha256sum -c SHA256SUMS` in `evidence/`. `sha256sum -c` on `evidence/landscape/SHA256SUMS` stays a pass.

## B1 — stale verify-report (PR #15 head `9131796`)

Hark's review: `evidence/verify-report.json` still has `gates.matrix_exact` `correct` 115, `non_colliding` 115, `total` 117 and `dirlist_metric` `correct` 117, `total` 117 (`display.matrix_correct` 115, `display.dirlist_total` 117). `evidence/SHA256SUMS` records that file. `clawscore_fleet/render_readme.py` line 60 says the README is generated from that report, but `README.md` lines 54 and 56 already say `116 of 116` and `118 of 118`. `json.dumps(..., indent=2, sort_keys=True)` round-trips the current report byte for byte.

`make verify-offline` (`clawscore_fleet/verify_offline.py` `main`) prints gates and does not write `verify-report.json`. `make verify` does, and it needs the lab. This change stays on `make verify-offline`.

`clawscore_fleet/feed_check.py` `_pinned_lines` reads only `feed_newest` from the report. `export_defender.build_rows` reads `fix_target` and `feed_newest` via `_shared_cs`, plus `scan.json`, not the matrix or dirlist counts. `evidence/narrower-gap/n6.txt` is a stored diff, not a generator output. Do not regenerate those.

Change:

- At the end of `verify_offline.run`, if `evidence/verify-report.json` exists, replace `gates.matrix_exact` and `gates.dirlist_metric` with the gates just computed. Set `display.matrix_correct`, `display.matrix_non_colliding`, and `display.matrix_percent` from the exact gate, and `display.dirlist_correct`, `display.dirlist_total`, and `display.dirlist_percent` from the dirlist gate. Recompute `gates.no_regression` with `no_regression` on that patched gate map. Write the file with the same `json.dumps` settings as `verify_run`. Do not create a report when the file is absent, and do not touch lab-only gates.
- `python -m clawscore_fleet.render_readme` loads that report and calls `write_readme`. After the report refresh, that command must leave `README.md` unchanged.
- `readme_drift(readme_text, report)` in `render_readme.py` returns an empty string when `readme_text` equals `render(report)`. `verify_offline` adds gate `readme_matches_report` (in `offline_names`) that runs this on `README.md` after the report write. A unit test loads the committed pair and also a scratch string with `116 of 116` replaced by `115 of 115`, which must not be empty drift.

Frozen pins that stay: `fixtures/db-d733a8c.json`, `evidence/landscape/**`, `inputs/clawscore-v0.2.3-gate/**`. Do not describe release `2026.10.5` as cleared of advisories.

## Skeptic (after the build)

Measured: `fingerprint_gates` printed exact `116/116 of 118 (100.0%)` and dirlist `118 of 118 (100.0%)`. `git diff -- fingerprints/db.json` was empty. `fixtures/db-d733a8c.json` is still `06728efac274f1bcc28ce7b3d6735ce6b94370b5ad0589fe10e212ca79e33165`. T6 failed with `0 != 61` while the unindexed branch returned `[], []`, then passed after that return was removed. `pytest -q` on CPython 3.11 was 38 passed. `make verify-offline` reported no offline failures. `sha256sum -c` passed for `evidence/SHA256SUMS` and `evidence/landscape/SHA256SUMS`.

Still unproven:

- The 13982-file listing was not rebuilt by walking the tarball in this change. The pin is the committed listing, registry `fileCount` 13982, the sha512 match, and the `package/dist/abort.runtime.js` member hash.
- `make matrix` on CI still packs the 117 landscape releases. Keeping the extra shard is implemented and unproven until that job runs.
- T5 still compares 0 with 0. The new control is `2026.6.7`, not `2026.10.5`.
- Local `make verify` was not run. `no_regression` was checked only by swapping the new matrix and dirlist gates into the committed `evidence/verify-report.json` (`pass` true, `differ` empty). The lab gates are unproven until CI.
- `evidence/verify-report.json` still records the previous lab figures (exact 115/115, dirlist 117/117). The README result lines were set to 116/116 and 118/118 ahead of that rewrite. Tarball coverage stays 117/117.
- `evidence/SHA256SUMS` lines for `fingerprint-set.json` and `feed-check.log` changed even though those blobs match `HEAD`. The previous sums did not match those bytes. Regeneration records the bytes already in git.

The stale-report bullet above is the state at `9131796`, before the B1 refresh in this note.

## Skeptic (B1)

Checked after the code above was in the worktree:

- `make verify-offline` rewrote `evidence/verify-report.json`. `gates.matrix_exact` is correct 116, non_colliding 116, total 118. `gates.dirlist_metric` is correct 118, total 118. `gates.no_regression.pass` is true and `figures.matrix_exact` is `[116, 116]`. `display.matrix_have` and `display.matrix_total` stayed 117.
- `python -m clawscore_fleet.render_readme` left `git diff --stat -- README.md` empty.
- A scratch copy of `README.md` with the first `116 of 116` replaced by `115 of 115` made `readme_drift` report line 54 and exit 1. The committed README returned an empty drift string.
- `sha256sum -c SHA256SUMS` exited 0 in `evidence/` and in `evidence/landscape/`.

Not regenerated:

- `evidence/export/defender_local_agents.csv`, `evidence/export/agentsinfo_local.jsonl`, and `evidence/feed-check.log` contain none of `115 of 115`, `116 of 116`, `matrix_exact`, or `dirlist_metric`. `feed_check._pinned_lines` reads `feed_newest` only. `export_defender.build_rows` copies `fix_target` and `feed_newest` from the report, not the matrix or dirlist counts.
- `evidence/narrower-gap/n6.txt` still quotes `115 of 115`. It is a stored diff, not a `render_readme` output.

Still unproven:

- `make verify` (the lab rewrite of the report and README) was not run in this worktree. CI runs it after `verify-offline`. The new gate compares `README.md` with the report `verify-offline` just wrote.
- The 2026.4.22 `github_db` 67 versus ClawScore 68 difference is a later feed-audit note. No feed code changed for it.
- The 2026.10.5 listing rebuild from the npm tarball is Hark's check of the existing shard. It was not repeated here.
