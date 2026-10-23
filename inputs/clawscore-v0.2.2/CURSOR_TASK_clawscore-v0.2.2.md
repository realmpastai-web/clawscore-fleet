CURSOR TASK: ClawScore Fleet v0.2.2 (semver cross-check + version grammar fixes)

FROZEN 2026-10-17 by Hark. Do not change the scope, the expected numbers or the gates. If a number does not come out exactly as written, stop and paste the output. Do not tune the code to hit the number.

EVIDENCE RULE
Nothing counts without the file, log or command output that produced it. Every number below was produced by the Hark repro in this folder (repro/, log repro/repro.log) on clawscore-fleet @ cc29565 (the tree merged to main as 6ccf7f6). Paste failures verbatim.

BASE
Repo: realmpastai-web/clawscore-fleet
Start only after the Defender export build (v0.2.1) is merged to main. Cut branch fix/v0.2.2-semver from that main HEAD and record its sha as "base" in verify-report.json.
Release field in verify-report.json: "0.2.2"
No merge to main, no npm publish, no outside contact. Open a draft PR; Hark gates it.

WHY (Hark gate of v0.2 @ cc29565, findings F1 and F2, plus F4 found while freezing this task)
F1. semver_check.py labels 737 disagreements "hark-grammar: a range bound does not match this parser". That label is wrong. _BOUND = r"(<=|>=|<|>|=)\s*(\S+)" captures the trailing comma ("2026.5.19,"), so hark_key(bound) is None and _explain picks the grammar branch. The real cause is that npm semver rejects GHSA comma ranges (">= a, <= b"), so its default call returns false. With commas stripped, 719 of the 737 agree and 18 are -N post-release cases.
F2. versions.py _VERSION_RE accepts only -N and -beta.N. "2026.5.19-alpha.1" (in the 278-version catalog) parses as None, so in_range returns False for every range. Example: "2026.5.19-alpha.1" in "<= 2026.5.19-beta.2" gives project False, npm True.
F4 (new, has a real effect). Two HIGH advisories use the glued bound "2.0.0-beta3", which _VERSION_RE rejects, so both ranges match nothing:
  GHSA-7xhj-55q9-pc3m (CVE-2026-28393, high)  range ">= 2.0.0-beta3, <= 2026.2.13"
  GHSA-hv93-r4j3-q65f (no CVE, high)          range ">= 2.0.0-beta3, < 2026.2.12"
The v0.2 cross-check missed this because npm's default call also returned false (it rejects the comma range), so the two sides "agreed". Effect: 16 of 117 stable releases (2026.1.29 to 2026.2.13) undercount by 1 or 2 high advisories. The same grammar is in Hark's landscape recompute.py, so Hark's version-vulns.json carries the same undercount. Hark supplies corrected landscape inputs in landscape-v0.2.2/.

INPUTS (copy in unchanged)
Build evidence/landscape/ as inputs/landscape/ on hark-inputs-2026-10-17 (the v0.2 inputs, byte-identical to what v0.2 used) overlaid with the 5 files in this folder's landscape-v0.2.2/: recompute.py, version-vulns.json, CLAIMS.md, FINDINGS.md, SHA256SUMS. Never edit them. `sha256sum -c evidence/landscape/SHA256SUMS` must pass.
- Unchanged: ghsa-all.json abc7b44d833c8961bba33e6d352b1bfa3de7e252607b173bc8fb075cc86a0b8d, versions.json 6e2b3ff8619dba5c5043dafb3944c270623ac15a3991ad30fb9c07e78a11dfda, and the count_nocve files, meta-*.json and stable-3file.json.
- Changed: recompute.py 771f969e194861e21c0d44260570831a4f32c638bd48957aec59a47ffdc32a80 (new key grammar; the stable filter is now ^\d+\.\d+\.\d+(-\d+)?$). version-vulns.json c8b9b34f9ede4ef54d77bbc80ec4782a73a3525e50e21c64e79e7bae05fd10f8 (was 30a0e9bf7bb5a81fa337ab5225a254848fb250419d443f80b66ca704436f5a0c). CLAIMS.md row 7: 2026.1.29 = 714 (23/256), was 712. FINDINGS.md: the same figure.

SCOPE

Fix 1: GHSA comma normalization (F1)
1. clawscore_fleet/semver_check.py: before calling npm, normalize each range with re.sub(r"\s*,\s*", " ", rng). Never feed a raw comma range to npm.
2. The reference decision is npm satisfies(version, normalized_range, {includePrerelease: true}). That matches the project's semantics: a prerelease sorts inside a range. Keep the default-call result as a logged column and report its disagreement count, but do not gate on it.
3. _BOUND must not capture commas: r"(<=|>=|<|>|=)\s*([^\s,]+)".
4. Rewrite _explain so a "hark-grammar" label is only possible when hark_key really returns None for the version or a comma-free bound. After the fixes, that count must be 0.

Fix 2: version grammar and prerelease order (F2 + F4)
5. clawscore_fleet/versions.py: one grammar shared by hark_key, cves.in_range and fingerprints:
   ^(\d+)\.(\d+)\.(\d+)(?:-(\d+))?(?:-(alpha|beta|rc)\.?(\d+))?$
   Key: (major, minor, patch, 0 if tag else 1, rank*1000 + N, post), with rank alpha=0, beta=1, rc=2.
   Required order: X-alpha.N < X-beta.N < X-rc.N < X < X-1 < X-2. Glued "-beta3" equals "-beta.3".
   This must equal landscape-v0.2.2/recompute.py key() on every catalog version and every GHSA bound. Add a test that asserts equality over all 278 versions and all 142 ranges' bounds.
6. Release-matrix selection must not change: still 117 stable releases (exclude any alpha/beta/rc; keep -N).
7. Regenerate cve-map.json, fixorder.json and the scan/CVE outputs against the new landscape. The changes are limited to what Gate C lists.

Explanations after both fixes: only "post-release-suffix" remains (OpenClaw's -N is a post-release, npm reads -N as a prerelease). There is no "prerelease" or "hark-grammar" residue.

REPRO (run these and paste their output into evidence/v0.2.2-repro.log)
Hark scripts are in repro/ in this folder; copy them to tools/hark-repro/ unchanged.
  bash tools/hark-repro/run_repro.sh <checkout of cc29565> inputs/landscape   (the v0.2 inputs)
Expected output, exactly as in repro/repro.log:
  1. On the v0.2 log (5,267 DISAGREE lines): agree_after_norm 5236; post_release 30; parser_diff 1 (2026.5.19-alpha.1 | <= 2026.5.19-beta.2); mislabeled_grammar 737, of which agree_was_grammar 719 and leftover_was:hark-grammar 18.
  2. Full 39,476 decisions, v0.2 grammar: normalized disagreements 35 other + 67 post-release (the 35 = 28 for the two glued-bound ranges + 7 for 2026.5.19-alpha.1).
  3. Alpha/rc fix only: 28 other + 67 post-release.
  4. Alpha/rc + glued fix: 53, all post-release, 0 other; default-call disagreements 5,314 (reported only).
  5. regen_version_vulns.py --old reproduces 30a0e9bf…0c byte for byte; the new grammar gives c8b9b34f…f8.
Then the project's own run on the new branch must match 4:
  make verify-offline
  python3 -m clawscore_fleet.semver_check
Expected: "semver 7.8.5 decisions 39476 disagreements 53 unexplained 0" (disagreements here means normalized + includePrerelease).

NEW GATES (keys under gates{} in verify-report.json, each with pass bool and actuals)
A. semver_comma_normalized
   - No npm call receives a range containing ","; assert it in check.js input (count of comma ranges sent = 0).
   - Explanations starting "hark-grammar: a range bound" = 0 (was 737).
   - Frozen regression: repro_crosscheck.py on cc29565's semver-crosscheck.log returns agree 5236 / post_release 30 / parser_diff 1 / mislabeled 737.
B. prerelease_order
   - hark_key returns non-None for 278/278 catalog versions and for all 183 bounds across the 142 ranges (incl. "2.0.0-beta3").
   - Order assertions: 2026.5.19-alpha.1 < 2026.5.19-beta.2 < 2026.5.19 < 2026.5.19-1; "2026.1.29-beta3" == "2026.1.29-beta.3".
   - in_range("2026.5.19-alpha.1", "<= 2026.5.19-beta.2") is True.
   - Normalized disagreements over 39,476 = 53; post-release-suffix 53; parser_diff 0; unexplained 0.
   - Project key == landscape-v0.2.2 recompute.py key on all versions and bounds.
C. glued_bound_effect (landscape + CVE map)
   - evidence/landscape version-vulns.json sha256 = c8b9b34f9ede4ef54d77bbc80ec4782a73a3525e50e21c64e79e7bae05fd10f8; cve-map-diff.txt is 0 bytes against it.
   - Exactly 16 of 117 releases change versus v0.2, a total of +30 advisories, +0 critical. +2 high for 2026.1.29, 2026.1.30, 2026.2.1, 2026.2.2, 2026.2.2-1, 2026.2.2-2, 2026.2.2-3, 2026.2.3, 2026.2.3-1, 2026.2.6, 2026.2.6-1, 2026.2.6-2, 2026.2.6-3, 2026.2.9. +1 high for 2026.2.12 and 2026.2.13.
   - The added advisories are exactly GHSA-7xhj-55q9-pc3m (all 16) and GHSA-hv93-r4j3-q65f (the 14 below 2026.2.12).
   - 2026.1.29 = 714 (23 critical / 256 high). 2026.4.22 still 101 (1/53). Fix target still 2026.5.27.
   - Lab: only the installs whose true version is 2026.1.29 (3 in the v0.2 lab) change their advisory list, by those two GHSA IDs. Every other install's scan output is identical to v0.2.
D. no_regression: every v0.2 and v0.2.1 gate still passes with the same actuals, except cve_mapping/fixorder/blast counts that Gate C explains. Version-accuracy figures (26/26, 9/9, 4/4, 4/4, 115/115, 117/117) must not move.

DELIVERABLE
Draft PR fix/v0.2.2-semver with: the code, tests, the new landscape inputs, tools/hark-repro/, evidence/v0.2.2-repro.log, the regenerated evidence + SHA256SUMS, and verify-report.json with gates A to D. In the PR body, list each gate with pass/fail and its actuals, and paste the 4 run_repro sections. CI green, and the CI artifact verify-report.json byte-identical to the committed one.

OUT OF SCOPE
Defender export (v0.2.1), new fingerprints, lab changes, README marketing copy. The one wording change: wherever a v0.2 output or doc says 2026.1.29 has 712 advisories, it now says 714.
