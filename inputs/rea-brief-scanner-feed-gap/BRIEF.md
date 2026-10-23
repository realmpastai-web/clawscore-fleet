# REA brief: scanner feed gap for openclaw (spec only)

Status of this commit: clean-room spec and frozen ClawScore baseline. The Trivy DB blob and the Grype DB archive are not downloaded here. No scanner binary is installed or run. No hold count from either DB is stated, because neither DB has been read.

Base checkout: `feat/scanner-feed-gap` at `aaec31f` (`aaec31fc23f0c622abe72f7e5b286196ec8d6ffe`, "chore: bump version to 0.4.0"). Hark named `c67f7ee`. `git diff --name-only c67f7ee..aaec31f` is only `README.md`, `clawscore_fleet/__init__.py`, `evidence/SHA256SUMS`, `evidence/verify-report.json`, and `pyproject.toml` (the 0.4.0 version strings). `evidence/landscape/version-vulns.json` is blob `9181cfb13b4d28d4ce3e7918f268de9db8731677` at both commits. File sha256 `254867ae994467d7d7e933e7850d8bc81f9a1b6ed6df8fcf7dc4351926a53757`. `evidence/landscape/ghsa-all.json` sha256 `27b020df70c9896d7b94280ad0646dc69ef4d27e504d81bc6719dedcb6446034`. Feed newest date is `FEED_NEWEST` in `clawscore_fleet/versions.py`: `2026-09-11`.

## Targets (pinned before the DB blobs are fetched)

### (a) trivy-db

OCI artifact `ghcr.io/aquasecurity/trivy-db:2`.

Registry `GET /v2/aquasecurity/trivy-db/manifests/2` at `Wed, 21 Oct 2026 15:29:09 GMT` (`pins/trivy-manifest.headers`). Response header:

`docker-content-digest: sha256:bc1ab2ce4f54245efb7861f81993c8abf4ae95aca67d00dce37c60dc59e7d415`

The manifest body (`pins/trivy-manifest.json`) sha256 is the same digest. Media type `application/vnd.oci.image.manifest.v1+json`. Annotation `org.opencontainers.image.created` = `2026-10-21T13:24:54Z`. One layer:

- title `db.tar.gz`
- media type `application/vnd.aquasec.trivy.db.layer.v1.tar+gzip`
- digest `sha256:3399c7b11c8c01d0423c115e938c30c05562cd5346ddcfc56db5197e79dd97d0`
- size `135854562`

The tag `2` is not the pin. The pin is the manifest digest and the layer digest above. The blob URL, fetched only after this commit, is `https://ghcr.io/v2/aquasecurity/trivy-db/blobs/sha256:3399c7b11c8c01d0423c115e938c30c05562cd5346ddcfc56db5197e79dd97d0`.

### (b) Grype DB v6

Listing `https://grype.anchore.io/databases/v6/latest.json`, fetched `Wed, 21 Oct 2026 15:29:10 GMT` (`pins/grype-latest.headers`). File sha256 `2859883b06c55066e267ce1b3115870c4af9f6651c62c9f4c07c3f9e2ccb3912` (`pins/grype-latest.json`).

Listing fields: `status` active, `schemaVersion` `v6.1.10`, `built` `2026-10-21T06:31:02Z`, `path` `vulnerability-db_v6.1.10_2026-10-21T00:28:41Z_1792564262.tar.zst`, `checksum` `sha256:fe51ed05fd0bf2e0642a362b75b245caf0da0eabb92b26a543e061f9873ec2ba`.

The archive URL is the listing directory plus `path`:

`https://grype.anchore.io/databases/v6/vulnerability-db_v6.1.10_2026-10-21T00:28:41Z_1792564262.tar.zst`

`HEAD` of that URL at `Wed, 21 Oct 2026 15:33:41 GMT` returned `200`, `content-type: application/zstd`, `content-length: 193498638` (`pins/grype-archive.headers`). The body was not downloaded. The checksum pin is the listing `checksum`, not the HEAD etag.

## Questions

Q1. Which advisory sources does each DB record for npm packages (GHSA, OSV, NVD)?

Q2. For openclaw@2026.6.10 and @2026.4.22, how many advisory IDs does each DB hold?

Q3. Of ClawScore's counted set (58 at 2026.6.10, 148 at 2026.4.22, from version-vulns.json at c67f7ee), how many does each DB hold?

Answers to Q1–Q3 are written only in Step 1 evidence, after the DB files are read. They are not answered in this file.

## Sealed predictions

`PREDICTIONS.txt` sha256 `1efacd3abcf950705fcd9a47fb76b9e8cd79ef402ad0598016527799f34a14f3`. Text, sealed before any DB read:

P1. Both DBs hold 0 of the 58 at 2026.6.10.

P2. Both DBs hold at most 68 of the 148 at 2026.4.22.

Scored once, later, into `inputs/rea-scanner-feed-gap-evidence/SCORE.log`. The scoring command is guarded by `test ! -e SCORE.log`. A second score must not rewrite that file. P1 holds only when Q3 for trivy at 2026.6.10 is 0 and Q3 for grype at 2026.6.10 is 0. P2 holds only when Q3 for trivy at 2026.4.22 is <= 68 and Q3 for grype at 2026.4.22 is <= 68. A prediction result does not by itself authorize or block the export. The export decision is the gap rule below.

## Wording

Allowed sentence when a DB count is placed next to the maker's count:

`<scanner DB digest X> lists N; the maker's repository lists M (feed newest 2026-09-11)`

`X` is the pinned digest (trivy manifest digest, or the Grype checksum without a scheme prefix). `M` is 58 for 2026.6.10 and 148 for 2026.4.22. Never write "wrong" or "misses". Never call a version safe.

## Counted set (frozen before either DB is read)

A row is in `C(V)` when `clawscore_fleet.cves.build_index()["per_version"][V]` contains it. That index uses `affecting_advisories`: `withdrawn_at is None`, package name casefold `openclaw`, ecosystem casefold `npm` (or a keep-list id in `data/non-npm-keep.tsv`), and `in_range` on `vulnerable_version_range` via `hark_key`. Withdrawn rows are listed by the code and are not counted.

`version-vulns.json` at the 2026.4.22 record (the array whose first field is `2026.4.22`) stores count 148. The 2026.6.10 record stores count 58. The same counts come out of `build_index` on this checkout: `baseline/counted-2026.6.10.txt` has 58 lines, sha256 `c9e053d502f379e1511bf14cfd2183802d2b63adb832173a1ccfcbca7f2d8e09`. `baseline/counted-2026.4.22.txt` has 148 lines, sha256 `8737f805df2d2de23685bbf6fb5299f4e8cf138a684b5ca75307c1d02a54c764`. One `GHSA-` id per line, sorted, trailing newline.

`baseline/range-shapes.stdout` sha256 `72a38748692a5ec9e8787623d24bc8eb46a2243fc72b9515982bd9fa061a98d7` records the union of those two files: 155 ids, 51 in both, 7 only in 2026.6.10, 97 only in 2026.4.22. Each of the 155 has one openclaw npm range. Comparator shapes: 89 `<`, 43 `<=`, 22 `>=` and `<`, 1 `>` and `<` (`GHSA-fwgr-fpv9-vf5x`, `> 2026.4.20, < 2026.5.28`). CVSS vector prefix `CVSS:3.1` on 140, none on 15. Zero ranges failed `parse_comparators`.

## How a DB "holds" an ID (rule fixed before the read)

Step 1 records the on-file schema in `recon.log` before it writes ID lists. An ID counts as **held** for version `V` only when all three are true:

1. Package name casefolds to `openclaw`.
2. The ecosystem is npm. Accept a stored ecosystem/namespace whose casefold is `npm`, or a purl whose type is `pkg:npm/`. Any other ecosystem string, including a language label that does not say npm, is unresolved. It is not held.
3. The version constraint is one of these forms, and it includes `V`:
   - Form A: one text value fully consumed by `parse_comparators`, and `in_range(V, text)`.
   - Form B: an explicit list of version strings that contains `V` exactly.
   - Form C: an inclusive introduced bound (null means no lower bound) and either an exclusive fixed bound or an inclusive last-affected bound (null means no upper bound). `fixed` and `last_affected` are not both set. Compare bounds with `hark_key`. A bound `hark_key` rejects is unresolved.

Column names are quoted in the extraction query. A column is mapped onto Form C only when its name contains `fixed` or `patched` (exclusive end), `last_affected` (inclusive end), or `introduced` (inclusive start). Anything that does not fit Form A, B, or C is listed in `unresolved-<db>.tsv` and is not held. Unresolved IDs do not increase Q2 or Q3 and do not cover the counted set.

Q2 for a DB and version is the number of distinct held advisory IDs. Q3 is the number of those IDs that also appear in the frozen counted file for that version.

Q1 reports the stored source/provider strings on npm openclaw rows, quoted. A label is applied only by this rule: substring `nvd` -> NVD; substring `ghsa` or `github` -> GHSA; substring `osv` -> OSV; otherwise UNCLASSIFIED. The label is not a second source field.

## Readers

Do not install or run `trivy` or `grype`.

- trivy-db is bbolt inside the pinned `db.tar.gz` layer. Read it with a Python bbolt reader. `bolt-cli` is not required. REA 6.7.0's help list has `inspect-sqlite-database` and no bbolt command, so REA is not the bbolt reader.
- Grype v6 is SQLite inside the pinned `.tar.zst`. `command -v sqlite3` is empty on this box. Read SQL with Python's `sqlite3` module (library `3.46.1`). Also run REA `6.7.0` (`/home/box/.npm/_npx/a1722018f28f9df2/node_modules/.bin/rea`, `package.json` version `6.7.0`) `inspect-sqlite-database` on the extracted SQLite snapshot. Record the REA version and the Evidence IDs it returns. Unpacking `.tar.zst` may use a zstd decompressor. That decompressor is not the grype binary.

Frozen DB files live under `inputs/rea-scanner-feed-gap-evidence/frozen/` and stay gitignored. Commit digests, URLs, queries, TSV ID lists, and logs. Do not commit the DB blobs.

## Gate

`inputs/rea-scanner-feed-gap-evidence/gate_feed_gap.py`, after this spec commit, not in it.

- G1: every file listed in that directory's `SHA256SUMS` matches. The recorded trivy manifest digest, layer digest, and Grype checksum equal the pins in this brief. If a frozen blob is present, its sha256 equals the pin. A mismatch exits 1.
- G2: ID sets recomputed from the frozen DB files equal the committed TSV sets. The mutant is a copy of one TSV with one extra `GHSA-` id appended. G2 on that copy exits 1. The committed TSV is not edited.
- G3: P1 and P2 scored once into `SCORE.log`, and only when `test ! -e SCORE.log` succeeds.

Both DBs cover ClawScore's set only when Q3 is 58 and 58 at 2026.6.10 and 148 and 148 at 2026.4.22. If that is true, write `NO-GO.md` with the evidence and stop. No export is built.

Otherwise the gap is the sorted union of:

- `C(2026.6.10)` minus trivy held at 2026.6.10
- `C(2026.6.10)` minus grype held at 2026.6.10
- `C(2026.4.22)` minus trivy held at 2026.4.22
- `C(2026.4.22)` minus grype held at 2026.4.22

One advisory is exported when a counted version contains it and at least one DB does not hold it at that version. The gate writes `gap-ids.txt` (one id per line, sorted, trailing newline). The export file count must equal the line count of `gap-ids.txt`.

## Export (only after the gate shows a non-empty gap)

Command: `clawscore export-osv --package openclaw`.

Any package other than `openclaw` exits non-zero. Withdrawn advisories (`withdrawn_at` not null) are excluded. One OSV JSON file per gap id, path `evidence/scanner-feed-gap/osv/<ghsa_id>.json`. Encode with `json.dumps(sort_keys=True, indent=2, ensure_ascii=False)` plus a trailing newline.

Validate every file against `pins/osv-schema-1.6.0.json` (sha256 `b30f59611f61a5c233dc5666379b683eeca6bb42e8c5acba172415d445f4f86e`, bytes from `https://raw.githubusercontent.com/ossf/osv-schema/v1.6.0/validation/schema.json`, `content-length: 7675`). The schema `required` array is `id` and `modified`. `additionalProperties` is false. Severity types in that schema are `CVSS_V2` and `CVSS_V3` only. `schema_version` on each document is the string `1.6.0`.

Field mapping from the `ghsa-all.json` object, and from nowhere else:

- `id`: `ghsa_id`
- `modified`: `updated_at`
- `published`: `published_at`
- `summary`: `summary` when non-empty
- `details`: `description` when non-empty
- `aliases`: `[cve_id]` when `cve_id` is a non-empty string; otherwise omit `aliases`
- `severity`: when `cvss.vector_string` starts with `CVSS:3`, one item `{"type": "CVSS_V3", "score": "<vector_string>"}`. The OSV `score` is the vector, not the numeric score. Omit `severity` when there is no CVSS:3 vector.
- `references`: one `{"type": "ADVISORY", "url": "<url>"}` per string in `references`. Stop if a reference is not an `http` or `https` URL.
- `affected`: one element, because each counted advisory has one openclaw npm range (`range-shapes.stdout`). `package.ecosystem` is `npm`. `package.name` is `openclaw`.

Range events use type `ECOSYSTEM`, not `SEMVER`. `hark_key` orders `X-1` after `X`, which is not SemVer order. Each event object has one key. A range includes an `introduced` event. `fixed` and `last_affected` are not both emitted.

- `< U` -> `introduced` `0`, `fixed` `U`
- `<= U` -> `introduced` `0`, `last_affected` `U`
- `>= L` and `< U` -> `introduced` `L`, `fixed` `U`
- `>` and `<` (`GHSA-fwgr-fpv9-vf5x`) -> no introduced event at the exclusive bound. `versions` is the sorted list of stable catalog versions for which `in_range` is true, ordered by `hark_key`. Do not invent a successor version.

`0` means no lower bound in the OSV event, not a published openclaw version. `database_specific.vulnerable_version_range` on the affected element is the verbatim range. `database_specific.first_patched_version` is set when that field is non-null. Events follow the range, not `first_patched_version`. Root `database_specific` also stores `clawscore_feed_newest` = `2026-09-11` and `source_sha256` = the `ghsa-all.json` sha256 above.

A fresh checkout of the PR head, with no DB download, reruns the command into an empty directory and produces the same sha256 for every OSV file. The unit tests stay green. This command reads `gap-ids.txt` and `ghsa-all.json`. It does not open the scanner DBs.

## What this commit does not establish

- Any Q1, Q2, or Q3 count. The DB blobs are not on disk for this commit.
- Whether P1 or P2 holds. They are sealed and unscored.
- Whether the gap is empty. No OSV export is produced by this commit.
- A defect label for either database. Later sentences use the wording rule.
- A REA Evidence ID. `inspect-sqlite-database` has not been run on the Grype snapshot.
- That the registry tag `2` or `latest.json` will still resolve to these digests later. The pins are the digests in this file.
