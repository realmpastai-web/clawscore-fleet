# ClawScore feed re-pin + CSV formula-escape frozen inputs (Hark, 2026-10-17)
EVIDENCE RULE: every number below comes from a file in this folder; `sha256sum -c SHA256SUMS` first.

## 0. Name clash: read first
`inputs/clawscore-v0.2.2/` (commit 0b5260f, frozen earlier today) already holds a task called v0.2.2: comma strip, prerelease grammar, glued beta3. That task assumes ghsa-all.json stays at abc7b44d… and that there are 142 ranges. This package changes the feed, so the two can't share one number. Proposal: keep the semver/grammar task as **v0.2.2** and make this one **v0.2.3**, cut after v0.2.2 merges. Every count derived from ranges (version-vulns, crit/high per version, fix_target) must be recomputed with the fixed grammar on the 894-advisory feed. The counts in expected-landscape.json don't depend on grammar; per-version counts do, so they aren't frozen here (UNPROVEN until recomputed). Santhosh decides the numbering.

## A. Advisory feed re-pin
**What we found (pin.log, derive_feed.log):**
- The v0.2 pinned `evidence/landscape/ghsa-all.json` was built from the **GitHub global advisory DB** (`/advisories?ecosystem=npm&affects=openclaw`). Today that source still returns the same **760 advisories, all 760 objects byte-for-byte identical** to the pinned file, newest 2026-07-02. Re-pulling the same source does not bring the new GHSA in.
- `make feed-check` reads a **different source**, the openclaw/openclaw **repository security advisories**: 722 published. 588 are in both sources; **134 are repo-only**. GHSA-xx9p-hc9w-6p5h is one of them, and the global DB returns 404 for it.
- 75 of the 134 were published after 2026-07-02. **59 were published on or before the v0.2 pin date**, so the v0.2 feed missed advisories that already existed when it was pinned, not just newer ones.
- npm `versions.json`: the registry today equals the pinned file (278 entries, identical; versions-check.log). 2026.8.1, the fix for xx9p, is already in it. No re-pin is needed.

**Proposed pinned feed:** `ghsa-all.json` = global 760 (unchanged objects) ∪ 134 repo-only, reshaped to the same 23 keys. derive_feed.py documents every mapping, including `type:"repository"` as a marker and repo `patched_versions` mapped to `first_patched_version`. Total 894; FEED_NEWEST 2026-09-11; GHSA-xx9p-hc9w-6p5h present.
- Rebuild offline: `python3 derive_feed.py` (reads raw/*.json byte-exact pages and writes the same ghsa-all.json). Re-fetch: `python3 pin_feed.py`.
- **Expected landscape constants** (expected-landscape.json): total 894, with_cve_id 459, without_cve_id 435, without_cve_id_critical_or_high 176, feed_newest 2026-09-11. These replace the hard-coded 760/452/308/110 in verify_offline.py.
- **Simulation** (PR #3 tree, feed swapped, FEED_NEWEST=2026-09-11; sim-verify-offline.log): 5 gates fail as expected: landscape_hashes, cve_mapping, semver_crosscheck, freshness, fix_target. All 134 new ranges parse, each matches at least one stable release (range-parse-check.log), and xx9p (`< 2026.8.1`) hits 98 stable versions. **This release must regenerate these five gates' evidence and re-pass them.** The cause of the semver_crosscheck failure is UNPROVEN until the PR runs it.
- feed-diff.tsv lists the 134 added advisories (id, date, severity, range, first patched, summary). The 75 newer ones split 30 high, 40 medium, 5 low.

## B. CSV formula-escape test vectors
- Rule (escape_reference.py, from the OWASP CSV Injection page, snapshot in csv/sources): for every TEXT cell of the CSV data rows (never the header, never the 5 integer columns), prefix `'` when the first char is `= + - @`, TAB, CR, LF, full-width `＝ ＋ － ＠`, or `'`. Then write with RFC 4180 quoting. Unescape drops one leading `'`, so the rule is reversible. JSONL is not escaped.
- `formula-escape-vectors.tsv`: 30 vectors (input, expected cell, expected CSV field bytes), including both OWASP examples (V12 matches OWASP's output byte for byte). `python3 escape_reference.py` reports VECTORS ok=30/30 (check_vectors.log).
- `planted-row.source.json` → `planted-row.expected.csv`: one synthetic install with payloads in 6 text columns. The gate feeds it through the PR's exporter and compares bytes.
- Current PR #3 export: 0 of the text cells start with a danger char (pr3-export-scan.log). It is safe today only by its data, as you said.
- Known limit (OWASP): Excel can drop the quote on save and re-open. The tab-prefix variant is the Excel-resistant option. Its trade-offs are UNPROVEN for our consumers, so it is not chosen.

## C. Proposed gates for this release (for the checklist I'll freeze when the PR lands)
1. feed: evidence/landscape/ghsa-all.json is byte-identical to this ghsa-all.json, and FEED_NEWEST is "2026-09-11".
2. landscape constants equal expected-landscape.json.
3. feed-check log: comparison is "same" (newest 2026-09-11 equals pinned).
4. The 5 regenerated gates pass; the other gates are byte-identical to v0.2.1 except where the feed drives them (the PR lists each one).
5. csv_escape: the exporter's escape function gives 30/30 vectors; the planted row is byte-equal to planted-row.expected.csv; no text cell in the real export starts with a danger char; unescape round-trips to scan.json values.
6. v0.2.1 fix first (PR #3 must not merge as is): G1.types and G2.keys_types pass (see v021-gate-pr3.log). No empty Device ID, First seen, Timestamp or LastUpdatedDateTime, and PublishedStatus is null rather than "".
