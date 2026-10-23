# ClawScore Fleet v0.2.3 frozen gate (Hark, 2026-10-18)

FROZEN. Don't edit anything in this folder. Run `sha256sum -c SHA256SUMS` first, then:

    python3 gate_v023.py <PR checkout> <main checkout @ 58d4925c3f83> [--semver <tools/semver/node_modules/semver>]

Inputs: the feed-csv package @ 1216d18 (ghsa-all.json 27b020df, csv vectors) and the v0.2.2 task @ 0b5260f (grammar, repro.log). Every constant is in expected-v023.json and comes from reference-repro.log.

## STOP-SHIP finding for stage 2: space-separated AND ranges
The 894 feed has 5 repo-only ranges that join their comparators with a space instead of a comma (expected-v023.json `space_and_ranges`). `cves.in_range` splits on "," only, so it reads `>= 2026.2.26 < 2026.7.1` as `>= 2026.2.26` with no upper bound. On main's code with the feed swapped in, project and reference disagree on 44 to 248 versions per range (space-and-evidence.log). Every later release then picks up phantom advisories, and the fix target becomes None, because 2026.10.4 still shows one high.
- Fix: one comparator grammar used everywhere: `\s*(<=|>=|<|>|=)\s*([^\s,]+)\s*,?`, repeated until the whole string is consumed (npm semantics: comma or whitespace means AND). A range it cannot consume is an error, not False.
- My mistake: feed README section A claims "all 134 new ranges parse". The parse check only tested the first comparator. The gate now tests every comparator (G4).

## What the PR must provide (interfaces the gate reads)
1. verify-report.json: `release` "0.2.3"; `base` "58d4925c3f83a0fae5ed947bd285cbc3d32f72f7" (or its 7-char form).
2. evidence/landscape/: ghsa-all.json = 27b020df (copied from @1216d18), versions.json = 6e2b3ff8 (unchanged), version-vulns.json = version-vulns-v023.json from this folder (556bd11e), and SHA256SUMS passing. versions.py `FEED_NEWEST = "2026-09-11"`.
3. Gates, all `pass: true`: landscape_hashes 894/459/435/176; freshness feed_newest 2026-09-11; semver_crosscheck semver 7.8.5, decisions 52820, disagreements 65, unexplained 0; fix_target min_clearing_version 2026.8.1, focus 2026.4.22 = 181 (1/100/64/16); new gates `semver_comma_normalized`, `prerelease_order`, `csv_escape`, `feed_check_same` (with `status`).
4. evidence/feed-check.log with `comparison: same`, `newest_date: 2026-09-11`, `pinned_date: 2026-09-11`.
5. evidence/v0.2.2-repro.log: sections 1 to 4 of the v0.2.2 repro (repro-v0.2.2.log here), as run in stage 1.
6. evidence/cve-map.json: advisory_count 894, with_cve_id 459, feed_newest 2026-09-11. For each of the 117 stable versions, `ghsa_ids` and counts equal the reference. 2026.1.29 = 786 (23/295/390/78).
7. `clawscore_fleet.export_defender.escape_cell(str)->str` and `unescape_cell(str)->str`, importable with no side effects, passing 30/30 vectors.
8. A file named `planted-row.csv` (one, anywhere outside .git), made by the PR's exporter from planted-row.source.json and byte-equal to planted-row.expected.csv.
9. The real export: every text cell round-trips (escape(unescape(c)) == c) and none starts with a bare danger char. Every row has cs_fix_target 2026.8.1 and cs_feed_newest 2026-09-11. For exact-verdict rows, cs_ghsa_ids equal the reference for that version.
10. No regression against main: the 14 gates in `unchanged_gates_vs_base` are byte-identical dicts, and every gate passes. gate_v021 is re-run and its 27 schema/lab checks must PASS. Its feed-driven checks are reported, not gated. Its G5.new.* checks don't apply when the base is main.

## feed_check_same policy (newer advisory upstream)
- `same` (upstream newest == 2026-09-11): pass.
- `newer` (GitHub publishes an advisory after 2026-09-11): **FAIL, and the release blocks.** feed-check.log must list each newer GHSA id, date and severity. Don't add it to ghsa-all.json inside v0.2.3: that would break the pinned sha and every frozen count. The fix is a re-pin release (v0.2.4): Hark refreezes the feed and constants, then the PR re-runs.
- `offline`/error: in `make verify-offline` log `SKIP feed_check_same (offline)`, with pass null, never true. CI runs it live with GITHUB_TOKEN. A SKIP can't ship.
- Why block rather than warn: cs_feed_newest goes into every export row and the README freshness line. Shipping 2026-09-11 while a newer advisory is public would make that field false.

## Re-freeze 2026-10-18 12:30 IST (after PR #5 @ 75fa8cf review)
- **G8.v021_schema_checks: was a gate bug.** gate_v021 hard-codes the v0.2.1 feed pins (cs_fix_target 2026.5.27, cs_feed_newest 2026-07-02) inside G2.keys_types and G3.values. G8 now runs a copy re-pinned from expected-v023.json (2026.8.1, 2026-09-11), and G8.v021_repin_scope asserts that exactly 3 lines change. On 75fa8cf the result is 27/27 PASS.
- **G9 (new).** `make verify` must not need git history. CI runs 39104181631 (pull_request) and 39104167829 (push) failed at `git show 58d4925:evidence/verify-report.json`, because actions/checkout defaults to fetch-depth 1. The base report is frozen here as base-verify-report-58d4925.json (sha256 d6c81247…237c, which equals main@58d4925).
