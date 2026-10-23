# REA brief: ClawScore sample written report (frozen 2026-10-20, Hark)

## Why
The v2 drafts offer a free, async written report. No such report exists yet. This brief specifies one so that it can be produced when a reader asks, and proves it on installs the generator has never seen.

## Target (public, shipped, legally obtained)
- openclaw npm release tarballs, as listed in evidence/matrix/releases.json (118 rows, each with its sha256).
- The pinned advisory feed evidence/landscape/ghsa-all.json, sha256 27b020df70c9896d7b94280ad0646dc69ef4d27e504d81bc6719dedcb6446034. Its newest advisory is dated 2026-09-11.
- The public lab fleet: fleet/manifest.yaml, 30 installs. The lab installs with `npm install --ignore-scripts` and runs `sleep`, so openclaw is never executed. This is the existing lab practice.

## Questions, each with the evidence its answer needs
Q1. Which exact version, or which candidate range, is each install?
  Evidence: the fingerprint verdict, the files read, the matched files.
Q2. Which published advisories match that version?
  Evidence: GHSA ids, each with its github.com/advisories URL and severity, under the agreed package rule: casefold name == openclaw, ecosystem npm, keep-list GHSA-25gx, withdrawn excluded.
  For a range, list the union across the candidates and mark ids that apply to only some of them.
Q3. Which credential NAMES can each install reach? Never values.
  Evidence: the config paths the names were read from. Label this lab-tested only.
Q4. In what order should the installs be fixed?
  Evidence: fix_order. Patch first; the minimum release that clears every critical and high advisory is 2026.8.1 on the 2026-09-11 feed. Then rotate credential names, ordered by reach.

## Claim boundary (hard)
- State identity and matches only. Use "matches N published advisories (C critical, H high) as of 2026-09-11".
- With zero matches, write exactly: "no published advisory as of 2026-09-11".
- Banned words and phrases (enforced by the scorer regexes): safe, not vulnerable, secure/secured, no vulnerabilities, clean, protected, guarantee, risk-free, fully patched, immune.
- Every number in report.md is rendered from a field in report-data.json; nothing is typed by hand.
- The Agent 365 / Defender comparison describes the local mock only. Claims about the published schema cite inputs/rea-narrower-gap/CLAIMS.md.

## Frozen baseline (sha256)
- oracle.py 82e0033a310610669bdc0bb51ec2fcd5987ec8444ae83ec04da6c9e7dce02bf6: Hark's independent advisory oracle, not ClawScore code.
- crosscheck.txt: the oracle equals cves.build_index minus {GHSA-2j9j, GHSA-mmpf} on 117 of 117 indexed versions. 2026.10.5 has no index entry and 0 oracle advisories.
- t4-correction.txt: under the pkg-match rule, 17 versions lose 2 advisories and 11 lose 1.
- score_holdout.py 1c1675c55411828bda50260fd3fdf4e4024084669bdaa61bea4b89711711bb21: the frozen scorer.
- scorer-selftest.txt: a perfect report scores rc 0. A dropped advisory, a banned word and a credential-value leak each score rc 1.

## Sealed holdout
- 8 installs, none at a lab-manifest version.
- Categories: the pkg-match window; 2026.3.x; the collision group; 5.x/6.x with a false version; 7.x (below 2026.8.1); 8.x (at or above 2026.8.1); 9.x stripped; 2026.10.5.
- Credentials, autoApprove and MCP servers were drawn at random. The salt is inside both files.
- holdout-manifest.json sha256 91b22f52bcccf0fd8e242b5c13e178c5f83a252bdab35f54e911b653d6b619fd
- holdout-key.json sha256 d3d9c9ef449c0df8dbf30f1cda3a946da1343c2076cba544d5adbd982c1b6b28
- Reveal protocol:
  1. The generator merges at commit G.
  2. Hark reveals the manifest.
  3. The team runs holdout lab, scan and report at G, with a clean tree.
  4. Hark reveals the key and runs score_holdout.py.
- Pass means RESULT PASS, every check.

## Skeptic pass (Hark)
- Depends on pkg-match. Branch from main only after fix/pkg-match merges, or the advisory sets for 2026.1.29 through 2026.2.22-2 are off by 1-2.
- The scan field `vulnerable` must never surface as "not vulnerable". Render matches, not a verdict.
- Range installs: the lab scan reports 222 for the 2026.4.7-1/2026.4.8 group. The oracle union gives the same 222, so union is the existing behaviour.
- Credential reach comes from planted lab configs only. The report must say so, and must not generalise to customer hosts.
- Leakage: the holdout versions are public, so a generator could hard-code every version. That only proves the holdout fair, never weaker. The sealed part is which versions, strip modes and credentials.
- UNPROVEN until the holdout: that the stripped and false-version detection generalises beyond the 4 lab installs.
