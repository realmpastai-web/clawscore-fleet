# clawscore-ghsa-only (Hark, frozen 2026-10-18)
These are the inputs and gate for the S1 Cursor build (see CURSOR_TASK_clawscore-ghsa-only.md).
`python3 gate_ghsa_only.py` runs the self-checks and a negative control, and its output is byte-identical to gate-output.txt. `--report R.json` judges a fleet report.
**Controls** (`controls/*.log`): a correct report passes. Dropping one id, or marking the gap window as affected, fails.

**Contents:**
- **OSV_SNAPSHOT.json:** the pinned OSV npm/openclaw query, 590 advisories, 59 with no CVE alias, with its sha256.
- **expected-ghsa-only.json:** the 59 ids plus 5 fixture versions with their expected status.
- **baseline-main-bdd8c9b.json:** what main reports today. The gate must reject it.
- **sources:** the landscape @bdd8c9b, 2 github/advisory-database records pinned at their main SHA, 5 Wazuh v4.14.9 files and the CTI pages.

**Findings:**
- **Gap window:** the GitHub API range shows `last_known_affected` (`<= 2026.4.2`) while the source says `fixed 2026.4.8`. So main misses 2 GHSA-only ids on 2026.4.7.
- **Wazuh question, settled at the schema level:** 4.14.9 has no way to carry a no-CVE advisory. Its feed is CVE5 records keyed by `cveId`, and its alert builders hard-code `enumeration="CVE"`. Not tested: CTI's private pipeline, and Wazuh 5.x/main.
