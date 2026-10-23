# Written report

Spec for the reader-facing sample report. Written from the pinned brief and the pinned feed below, before `clawscore_fleet/report.py`. The generator implements this file and does not add a second advisory rule.

## Pinned inputs

Hark's bundle is `inputs/rea-brief-sample-report/report-brief.tgz`, sha256 `4f5eea7ada9bbd110387ea9e70686632bc3e57d8c22e6777cd875f911e780c91`. `sha256sum -c SHA256SUMS` in `inputs/rea-brief-sample-report/report-brief/` is the check for the extracted files. There is no `sealed/` directory in that bundle.

| file | sha256 | role |
|---|---|---|
| `inputs/rea-brief-sample-report/report-brief/BRIEF.md` | `d81ddcf7f77957a16031f539f412d3f41357ae4eb10297d88aee7b0d9c94f126` | questions Q1–Q4 and the claim boundary |
| `inputs/rea-brief-sample-report/report-brief/CURSOR-TASK-SAMPLE-REPORT.txt` | `e14a8e56b979d304db2315aed4950fd6dd601fe9a0edebe0c15f1b6d05693316` | build B1–B4 and acceptance A1–A7 |
| `inputs/rea-brief-sample-report/report-brief/oracle.py` | `82e0033a310610669bdc0bb51ec2fcd5987ec8444ae83ec04da6c9e7dce02bf6` | independent advisory oracle |
| `inputs/rea-brief-sample-report/report-brief/score_holdout.py` | `1c1675c55411828bda50260fd3fdf4e4024084669bdaa61bea4b89711711bb21` | frozen scorer |
| `evidence/landscape/ghsa-all.json` | `27b020df70c9896d7b94280ad0646dc69ef4d27e504d81bc6719dedcb6446034` | pinned advisory feed |

`BRIEF.md` states the feed's newest advisory date as 2026-09-11. `clawscore_fleet.versions.FEED_NEWEST` is that same date. The feed pin is the sha256 in the table above.

The public lab scan already on this branch is `evidence/scan.json` (30 installs). Range installs `claw-10` through `claw-13` have candidates `2026.4.7-1` and `2026.4.8`. Running the oracle on the pinned feed gives 222 advisories for `2026.4.7-1`, 202 for `2026.4.8`, and 222 for the union. Twenty of those ids cover only `2026.4.7-1`. `2026.10.4` and `2026.10.5` each return 0. `cves.min_clearing_version` on this feed is `2026.8.1` (`evidence/fixorder.json`).

Branch base is main `de79e1c5757b626ed6289cc15e94824d7387bac6` (the squash-merge of fix/pkg-match).

## Command

```
python3 -m clawscore_fleet.report --scan evidence/scan.json --out evidence/report/
```

Optional `--observed-at <file>`. When omitted, the first line of `evidence/lab-scan-observed-at.txt` is used. That file is the clock already recorded for the lab (`2026-10-17T15:54:49Z`). The generator does not read file mtimes and does not call `datetime.now`.

Writes `report-data.json` and `report.md`. Same scan, same observed-at file, and same `git rev-parse HEAD` produce byte-identical output. JSON is `json.dumps(..., indent=2, sort_keys=True)` plus a trailing newline. Markdown is rendered only from that JSON object.

`report.pdf` is written with pandoc when `pandoc` is on `PATH`. Its sha256 is recorded in `pdf-status.txt`. When pandoc is absent, `pdf-status.txt` says pandoc was not available and no PDF was written. The PDF is not an acceptance gate.

## report-data.json

### header

| field | source |
|---|---|
| `fleet` | `lab` in `fleet/manifest.yaml` (`clawscore-fleet`) |
| `observed_at` | first line of the observed-at file |
| `feed_newest` | `FEED_NEWEST` (`2026-09-11`) |
| `feed_sha256` | sha256 of `evidence/landscape/ghsa-all.json` |
| `tool_commit` | `git rev-parse HEAD` |
| `rule` | `package name casefold equals openclaw and ecosystem npm, or the ghsa_id is a data row in data/non-npm-keep.tsv; rows with withdrawn_at set are excluded` |

### installs

One object per `evidence/scan.json` install, in scan order.

| field | source |
|---|---|
| `id`, `verdict`, `version`, `candidates`, `files_read`, `matched_files` | copied from the scan. `version` is JSON null when the scan value is null |
| `auto_approve`, `mcp_servers` | copied from the scan |
| `credential_names` | the scan's `credentials` list, sorted. Names only |
| `credential_count` | `len(credential_names)`. The fleet summary table prints this field |
| `mcp_count` | `len(mcp_servers)`. The fleet summary table prints this field |
| `credential_sources` | the scan's `config_paths` list, in scan order |
| `advisories` | union below |
| `critical`, `high`, `advisory_count` | counts over that union |
| `advisory_note` | empty string when `advisory_count` is not 0; otherwise exactly `no published advisory as of <feed_newest>` |

Each advisory object:

| field | value |
|---|---|
| `ghsa_id` | the id |
| `url` | `https://github.com/advisories/` plus the id |
| `severity` | the feed row's `severity` |
| `applies_to` | JSON null when the id covers every candidate. Otherwise the candidate versions it covers, in the scan's candidate order |

The union uses `cves._rows_for_version` (which calls `pkgmatch.is_openclaw_npm` and drops `withdrawn_at`). For each candidate, take the non-withdrawn covering rows. The install's list is those ids sorted by `ghsa_id`. An id that covers only some candidates has `applies_to` set to that subset. A range is never reduced to `candidates[0]`.

`2026.4.7-1` contributes ids that do not cover `2026.4.8`. Those twenty ids are why a range install's list is the union (222), and why `applies_to` is required.

No advisory description or summary is copied. Those strings are not part of this schema.

### summary

Counts rendered in the markdown, so every printed integer has a field:

| field | meaning |
|---|---|
| `install_count` | length of `installs` |
| `exact_count` | verdict `exact` |
| `range_count` | verdict `range` |
| `unknown_count` | verdict `unknown` |
| `critical_or_high_count` | installs whose `critical + high` is greater than 0 |
| `zero_advisory_count` | installs whose `advisory_count` is 0 |
| `mock_registry_rows` | `summary_from_scan` `registry_sees` |
| `mock_blank_or_stale` | `summary_from_scan` `no_usable_version` |
| `agent365_label` | the string `Agent 365`, so the digits in that name are a field the markdown renders |

The mock fields are the local Agent 365 mock already stored on the scan (`agent365` / `agent365_rows`). They are not a reading of the published schema.

### fix_order

Patch, then rotate. The predicate matches `clawscore_fleet.fixorder.fix_order`: an install is in the patch list when `critical + high` is greater than 0. Sort key: more credential names first, then `auto_approve` true before false, then `id`.

`min_clear_release` is `cves.min_clearing_version()` (`2026.8.1` on this feed). It is stored on `fix_order` and on every patch row. `fix_order.min_clear_medium_count` and `fix_order.min_clear_medium_ids` are the severity `medium` rows from `advisories_for([min_clear_release])`. The generator refuses to write the report when that same call still returns a critical or high row.

The fix-order sentence reads those fields and `header.feed_newest`:

`min_clear_release (earliest release from which no critical or high published advisory matches, as of <feed_newest>) is <min_clear_release>; it still matches <min_clear_medium_count> medium advisories.`

```
fix_order.min_clear_release
fix_order.min_clear_medium_count
fix_order.min_clear_medium_ids
fix_order.patch[]: install, version, candidates, min_clear_release, credential_count, auto_approve
fix_order.rotate[]: credential, reach, installs
```

Rotate rows are only credential names that appear on a patch install. Order is reach descending, then the name. `reach` is the number of patch installs that carry that name. `installs` is those ids, sorted. Credential names that appear only on zero-advisory installs are not in this list. That is the same reach rule as `fix_order` on `evidence/scan.json`.

## report.md

Five sections, in this order, plus an optional npm audit comparison when `evidence/npm-audit/split.json` covers every distinct version in the scan. The renderer reads `report-data.json` only. It does not recompute advisory ids from the feed. The match sentence uses `advisory_count`, `critical`, `high`, and `header.feed_newest`. The npm audit sentence uses the split row's `npm_audit`, `clawscore`, `npm_audit_date_utc`, and `foreign_source_count`.

1. Header. Fleet, observed_at, feed_newest, feed_sha256, tool_commit, and the rule sentence.
2. Fleet summary table. One row per install: id, verdict, version, candidates, advisory_count, critical, high, `credential_count`, auto_approve, `mcp_count`. A prose sentence states `mock_registry_rows` and `mock_blank_or_stale` and says, in that same sentence, that this Agent 365 comparison is a local mock.
   When the split covers the scan, `## npm audit comparison` follows this table. One row per distinct version, in scan order: npm query date, feed newest, npm audit, ClawScore, overlap, GitHub-DB-not-returned with ids, repo-only, npm-only. The sentence is `npm audit returned N advisories for openclaw@X on <fetched date>; the maker's repository lists M (feed newest <feed_newest>).` When `foreign_source_count` is not 0, the second clause is `the GitHub advisory database and the maker's repository list M`. The section states those counts only.
3. Fix order. The prose sentence is the `min_clear_release` sentence above. The patch table includes `min_clear_release` on every row. The rotate table is the `rotate` list, already ordered by reach.
4. Per-install detail. For each install: verdict, version, candidates, files read, matched files. Then either `matches N published advisories (C critical, H high) as of <feed_newest>` using that install's fields, or the exact `advisory_note` when the count is 0. Critical and high advisories are listed here (id, severity, url, and `applies_to` when it is not null). Credential names and `credential_sources` are in a sentence that contains the words `credential reach is lab-tested only`. auto_approve and mcp server names follow.
5. Method and limits. States the match sentence and the zero-advisory sentence as the only identity wording. States `credential reach is lab-tested only` and that the paths are the planted lab config paths, not customer hosts. States that the Agent 365 comparison is a local mock, in the same sentence as any figure taken from the mock, and cites `inputs/rea-narrower-gap/CLAIMS.md` for the published-schema limits. An appendix lists every advisory id for every install.

### Wording

- With one or more matches: `matches N published advisories (C critical, H high) as of <feed_newest>`.
- With zero matches: exactly `no published advisory as of <feed_newest>`.
- Do not write these, including inside a quotation or a negation: safe, not vulnerable, secure, secured, secures, no vulnerabilities, clean, protected, guarantee, risk-free, fully patched, immune. The scorer in `score_holdout.py` applies those patterns case-insensitively to the whole markdown file.
- Do not print credential values. `fleet/secrets-pool.json` is not read by the generator.

The scan field `vulnerable` is not copied and is not rendered.

## Lab key for the scorer

`score_holdout.py` reads a key with a `key` list. Build that list from `fleet/manifest.yaml` and `oracle.py`, not from `report-data.json`.

For each manifest install:

- `id`, `auto_approve`, and `credential_names` (sorted) come from the manifest.
- If the manifest version is in a `fingerprint.collision_groups` group, `verdict` is `range` and `candidates` is that group. Otherwise `verdict` is `exact` and `candidates` is the one-element list of the manifest version.
- `advisory_ids` is the sorted union of `oracle.advisories` over those candidates. `advisory_count`, `critical`, and `high` are counts on that union (`critical` and `high` are the oracle severity strings).
- `zero_wording` is `no published advisory as of 2026-09-11` when the union is empty, and `""` otherwise.

`python3 inputs/rea-brief-sample-report/report-brief/score_holdout.py <key> evidence/report/report-data.json evidence/report/report.md fleet/secrets-pool.json` must print `RESULT PASS`.

v2 notes: the frozen scorer would not catch "No known vulnerabilities" but test_banned_words does.

## Holdout lab

`python3 fleet/gen_lab.py --holdout <manifest.json> --out fleet-holdout/` writes a separate tree. With no arguments, `gen_lab.py` keeps its current behavior. `fleet/compose.yaml`, `fleet/manifest.yaml`, and `fleet/plants/` stay byte-identical.

Manifest schema:

```
{
  salt, feed_sha256,
  installs: [{
    id, version,
    stripped: none|removed|false-version,
    false_version, auto_approve,
    credentials: [pool names],
    mcp_servers: [filesystem|github|slack]
  }]
}
```

`feed_sha256` must equal the sha256 of `evidence/landscape/ghsa-all.json`. Credential checks use pool names only. The generator refuses an unknown name and does not print pool values.

Images use the same Dockerfile shape as the main lab: `npm install --ignore-scripts` and no openclaw process. Containers use `fleet/entrypoint.sh`, which execs `sleep`. Compose project `clawscore-holdout`, internal network `clawscore-holdout`, label `clawscore.holdout=1`. The main lab label `clawscore.lab=1` is not set, so `make lab-down` does not remove holdout containers.

`fixtures/holdout-example.json` has three installs and three versions that already appear in `fleet/manifest.yaml` (`2026.1.29`, `2026.4.22`, `2026.10.4`). It is not the sealed holdout.

Make targets, default `MANIFEST=fixtures/holdout-example.json`:

| target | behavior |
|---|---|
| `holdout-lab-up` | generate `fleet-holdout/`, build images, compose up, require every container's pid 1 to be `sleep`, require the network to be internal and unpublished |
| `holdout-scan` | fingerprint those containers into `evidence/holdout/scan.json`. Write `evidence/holdout/observed-at.txt` only when that file is absent |
| `holdout-report` | print `git rev-parse HEAD`. Exit non-zero when `git status --porcelain` is non-empty, before writing a report. On a clean tree, run the generator on `evidence/holdout/scan.json` into `evidence/holdout/report/` |
| `holdout-lab-down` | compose down and remove containers labeled `clawscore.holdout=1` |

`fleet-holdout/` and `evidence/holdout/` are generated at holdout time and are gitignored, so generating them does not dirty the tree that `holdout-report` checks. The sealed manifest and key are not in this repo. Scoring them is the post-merge holdout, not this PR.

## Sample

B4 writes the public 30-install report to `evidence/report/report.md` and `evidence/report/report-data.json`, then regenerates `evidence/SHA256SUMS` with `python -m clawscore_fleet.hash_evidence`. The sample report file is `report.md`. The same markdown is also written to `evidence/report/sample-report.md`.

## Out of scope

Holdout steps H1–H4 run after merge, on a clean tree, once. This spec does not reveal or invent `holdout-manifest.json` or `holdout-key.json`.
