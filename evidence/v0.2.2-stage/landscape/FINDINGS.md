# OpenClaw landscape findings (Hark, 2026-10-17 ~15:55 IST) — evidence files alongside
Sources: registry.npmjs.org/openclaw ; api.github.com/advisories?affects=openclaw (paginated) ; unpkg/jsdelivr file fetches.
- npm: 278 versions, 117 stable (2026.1.29 → 2026.10.4). dist-tags latest 2026.10.4, extended-stable 2026.9.33. -> evidence/openclaw-landscape/versions.json
- GHSA: 760 advisories (26 critical / 266 high / 392 medium / 76 low), 452 with CVE ids, published 2026-02-04 → 2026-07-02. -> ghsa-all.json
- Per-version known-vuln count (range match on GHSA ranges) -> version-vulns.json. 2026.4.20: 119 ; 2026.4.22: 101 (1 critical) ; 2026.5.27: 1 ; ≥2026.6.6: 0 known.
  CAVEAT: no advisory published after 2026-07-02 in the API feed, so "0" for later versions = no published advisory, NOT proven safe.
- Claw Chain: CVE-2026-44112/44113/44118 + GHSA-x3h8-jrgh-p8jx (no CVE id) all "<= 2026.4.21", fixed 2026.4.22.
- Fingerprint (3-file SHA-256) across stable releases -> stable-3file.json:
  - package.json present in 114/117, all distinct (but trivially editable; version string inside).
  - dist/cli.runtime.js + dist/abort.runtime.js exist only from 2026.3.31 on (71 versions). Pair distinct for 70/71; COLLISION: 2026.4.7-1 == 2026.4.8.
  - Releases before 2026.3.31 (~43 stable) lack these files -> need a different file set for the old fleet, which carries the most CVEs (e.g. 2026.1.29: 714 advisories after the v0.2.2 grammar fix).
- Design implications for clawscore-fleet: (1) build file-set selection from all stable tarballs, not 3 hand-picked releases; (2) report "range" when dist hashes collide (4.7-1/4.8); (3) CVE mapping must be generated from GHSA ranges incl. non-CVE GHSA ids and "-N" post-release suffixes; (4) state advisory-feed freshness date in every report.
