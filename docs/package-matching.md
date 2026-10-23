# Package matching

Spec for which advisory package rows attach to an npm `openclaw` release. Written from the pinned files below, before the matcher. The matcher implements this section and does not add an id exclusion list.

## Pinned feed (do not edit)

`cves._load_advisories` reads `evidence/landscape/ghsa-all.json`. sha256 before this change:

```
27b020df70c9896d7b94280ad0646dc69ef4d27e504d81bc6719dedcb6446034  evidence/landscape/ghsa-all.json
6e2b3ff8619dba5c5043dafb3944c270623ac15a3991ad30fb9c07e78a11dfda  evidence/landscape/versions.json
483efca8718a87d14dd1440c4a55b6d7b2c438e03ad6f50c51d947ea94807c65  evidence/landscape/version-vulns.json
50f71dccc4138d1c5bcdef3ad56da526e5fb93e3f280b99cb91af4ffd8b8ec74  inputs/rea-brief-openclaw-latest/osv-openclaw.json
4f02bd7f1e9a213c1824e290a716d34e1fe0cfa622516a8f1a425cada7bbb0aa  inputs/rea-brief-openclaw-latest/gh-global-openclaw.json
b3f784205d65f25406647dfcaaa247e0757651a9e1f27563e8948e7ac25616c9  inputs/rea-brief-openclaw-latest/gh-repo-openclaw-published.json
```

`ghsa-all.json` and `versions.json` stay byte-identical. `version-vulns.json` is the derived recount (`evidence/landscape/recompute.py` calls `version_vuln_rows`) and is regenerated with `evidence/landscape/SHA256SUMS`.

## Rule

`clawscore_fleet.pkgmatch.is_openclaw_npm(package, ghsa_id)` is true when either clause holds:

1. `package["name"].casefold() == "openclaw"` and `package["ecosystem"].casefold() == "npm"`.
2. `ghsa_id` is a data row in `data/non-npm-keep.tsv`.

Missing name or ecosystem fails clause 1. Clause 2 does not look at the package. There is no separate deny list.

Every advisory package-name comparison in the fleet scorer calls this function:

- `cves._openclaw_ranges` and `cves._first_patched` (the `build_index` path).
- `feed_check._openclaw_ranges` (GitHub `ghsa_id`) and `feed_check._covers_osv` (OSV `id`).
- `ghsa_only._osv_semver_covers`, `ghsa_only._github_ranges`, `ghsa_only._osv_fixed_versions`.
- `gates_v023._openclaw_ranges` and the range walk in `glued_bound_effect`.
- The range collection in `tests/test_grammar.py`.

Not this function: directory-name checks (`scan_host`, `idle_linux`, `docker_target`). Frozen trees under `inputs/` and `tools/hark-repro/` stay byte-pinned.

`semver_check._ranges` still collects every openclaw-named range string, including one that scoring drops. `inputs/clawscore-v0.2.3-gate/expected-v023.json` pins `decisions` at 52820 (278 catalog versions × 190 unique strings) and that folder is frozen. The only unique string that fails clause 1 and clause 2 is `<=2026.2.14` on `GHSA-mmpf-jwf4-h3qv`. `<= 2026.2.22-2` on `GHSA-2j9j-gf59-p4p5` is also on an npm row, so it stays in both sets. This grammar cross-check does not attach either id.

## Rows in the scorer feed

`evidence/landscape/ghsa-all.json`, one vulnerability object each.

`GHSA-2j8v-hwgc-x698` (lines 8753–8757), severity high, `withdrawn_at` null:

```
"ecosystem": "npm",
"name": "Openclaw"
"vulnerable_version_range": "<= 2026.5.16",
"first_patched_version": "2026.5.18",
```

Clause 1 matches `Openclaw` and `openclaw`. The same row is in `gh-global-openclaw.json`. It is absent from `osv-openclaw.json` (590 records, zero with that id). For `2026.4.22`, `feed_check._covers_github` minus `feed_check._covers_osv` is `[GHSA-2j8v-hwgc-x698]` (github_db 68, osv 67). OSV was queried as `openclaw`; this row's GitHub package name is `Openclaw`. The pinned OSV file is not rewritten.

`GHSA-w7j5-j98m-w679` (lines 59770–59774), severity high:

```
"ecosystem": "npm",
"name": "openclaw"
"vulnerable_version_range": "< 2026.2.21",
"first_patched_version": "2026.2.21",
```

The scorer feed tags this id npm, so clause 1 keeps it. The same npm tag is in `gh-global-openclaw.json` and in both OSV files (`pkg:npm/openclaw`). The repository advisory file tags the same id `other` with range `<= 2026.2.19-2`. That repository row is not repo-only: the id is already in the global file. `feed_check` github_db reads the global file. No deny-list entry.

Its description (line 59746) names `scripts/docker/` and `scripts/e2e/` Dockerfiles that run as root. Shard path listings do not ship those paths (below). The npm tag still attaches the row.

`GHSA-25gx-x37c-7pph` (lines 65333–65337), severity high, `cve_id` `CVE-2026-32064`:

```
"ecosystem": "npm",
"name": "openclaw"
"vulnerable_version_range": "< 2026.2.21",
"first_patched_version": "2026.2.21",
```

Clause 1 matches this landscape row, so `build_index` keeps it without consulting the keep-list. The keep-list still lists the id because `gh-repo-openclaw-published.json` tags the same id `ecosystem: other`, `name: openclaw`, range `<=2026.2.19-2`. Clause 2 is what matches that non-npm package object. Description line 65302: "The sandbox browser entrypoint launched `x11vnc` without authentication (`-nopw`) for noVNC observer sessions." Line 65301 is the summary and does not contain that sentence.

`GHSA-2j9j-gf59-p4p5` (lines 71471–71475), severity low, not in the global DB:

```
"ecosystem": "swift",
"name": "openclaw"
"vulnerable_version_range": "<= 2026.2.22-2",
"first_patched_version": "2026.2.23",
```

Description line 71449: "Advisory package metadata: `openclaw` (`swift` ecosystem)." and "internal preview iOS builds only". Clause 1 fails. The id is not on the keep-list. It attaches to no stable version.

`GHSA-mmpf-jwf4-h3qv` (lines 74273–74277), severity low, not in the global DB:

```
"ecosystem": "other",
"name": "openclaw"
"vulnerable_version_range": "<=2026.2.14",
"first_patched_version": "2026.2.15",
```

Description line 74251: "option injection in the repository's `git-hooks/pre-commit` hook" and "the npm package does not ship `git-hooks/`". Clause 1 fails. Not on the keep-list. It attaches to no stable version.

Name/ecosystem groups in this file for a casefolded name `openclaw`: npm `openclaw` 865, npm `Openclaw` 1 (`GHSA-2j8v-hwgc-x698`), npm `OpenClaw` 1 (`GHSA-vm29-7mq3-9jrg`, withdrawn), swift 1 (`GHSA-2j9j-gf59-p4p5`), other 1 (`GHSA-mmpf-jwf4-h3qv`).

## Keep-list

`data/non-npm-keep.tsv` has four columns: `ghsa_id`, `package/ecosystem`, `decision`, `evidence`. One data row: `GHSA-25gx-x37c-7pph`, `openclaw/other`, `keep`. The `package/ecosystem` value is the non-npm package object (`openclaw`, ecosystem `other`) cited for this keep decision. `pkgmatch.keep_ids` reads the `ghsa_id` column.

Shipped-artifact check:

- `evidence/matrix/listings/2026.2.14.json.gz`: 5147 paths. Zero paths contain `scripts/docker`, `scripts/e2e`, `git-hooks`, `Dockerfile`, `noVNC`, `x11vnc`, or `-nopw`. `dist/plugin-sdk/agents/sandbox/browser.d.ts` is present.
- `evidence/matrix/listings/2026.2.19-2.json.gz`: 7676 paths. The same zero path hits. `dist/plugin-sdk/agents/sandbox/browser.d.ts` is present.
- `evidence/matrix/tarballs.sha256` names `openclaw-2026.2.14.tgz` `eecbf4565a1e71df1e2f6c9dceaf0192d59fd11b59fa68ffc5cadfea546db7ef` and `openclaw-2026.2.19-2.tgz` `296cc537462a2ff0b9b2a3c4b7c5083171a13523c4c3ba82ca10ef1c5b915c71`. `inputs/pr16-review-ev/x11vnc-grep.txt` sha256 `6747882e3f2e1485695a2d4dacd73bddfccd4cd49c2e14ddc090774210f5dd31` records the dist byte grep of those tarballs: noVNC strings ship in dist of 2026.2.14 (10 paths) and 2026.2.19-2 (11 paths). That file lists no `x11vnc` hits and no `-nopw` hits.
- `evidence/matrix/listings/2026.2.21.json.gz` lists `dist/plugin-sdk/agents/sandbox/novnc-auth.d.ts`. That release is the landscape `first_patched_version` for `GHSA-25gx-x37c-7pph`, not one of the two tarballs above.

## Recount already measured on the pre-change matcher

`build_index` on the unmodified name match (`str(name).lower() == "openclaw"`, no ecosystem check), stable set 117 (`2026.1.29` through `2026.10.4`):

| id | versions attached |
|---|---|
| GHSA-2j9j-gf59-p4p5 | 28, `2026.1.29` through `2026.2.22-2` |
| GHSA-mmpf-jwf4-h3qv | 17, `2026.1.29` through `2026.2.14` |
| GHSA-w7j5-j98m-w679 | 22, `2026.1.29` through `2026.2.19-2` |
| GHSA-25gx-x37c-7pph | 22, `2026.1.29` through `2026.2.19-2` |
| GHSA-2j8v-hwgc-x698 | covers `2026.4.22`, does not cover `2026.5.18` |

Dropping only `GHSA-2j9j-gf59-p4p5` and `GHSA-mmpf-jwf4-h3qv` (both severity low) changes 28 versions: 17 lose 2 (`2026.1.29` through `2026.2.14`), 11 lose 1 (`2026.2.15` through `2026.2.22-2`). `2026.4.22` stays 148. `feed_check.version_count_lines` before the change:

```
version_counts withdrawn_excluded=yes
2026.10.5 github_db=0 repo_only=0 osv=0
2026.10.4 github_db=0 repo_only=0 osv=0
2026.6.10 github_db=0 repo_only=58 osv=0
2026.4.22 github_db=68 repo_only=80 osv=67
```

Those four versions sit after `2026.2.22-2`, and every global-DB `openclaw` row in `gh-global-openclaw.json` is ecosystem npm (758 `openclaw`, 1 `Openclaw`, 1 `OpenClaw`). The ecosystem filter does not change those four lines. `2026.1.29` in `evidence/landscape/CLAIMS.md` is 629 and moves by the two low rows; critical/high on that claim stay as `recompute.py` prints them. Separate figures 722, 134, 75, 58, `2026-09-11`, and `2026.10.5` are not this recount.
