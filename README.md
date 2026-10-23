# clawscore-fleet 0.4.0

clawscore-fleet reports, for each OpenClaw install in a fleet, the exact version or a version range when builds share a fingerprint, the advisories that apply, the credential names that install can reach, and a fix order. It diffs that report against a local mock of the inventory Microsoft Defender / Agent 365 exposes. Published-schema verdicts come from the frozen gate over Microsoft Graph CSDL and Defender learn pages, not from that mock. Credential values are never printed or stored.

## Threat

The Claw Chain advisories below are fixed in openclaw@2026.4.22 (released 2026-04-23). Later releases can still match other advisories. The minimum release that clears every critical and high advisory in this feed is 2026.8.1. On a vulnerable install, MCP server settings and the process environment can put cloud and chat tokens in reach of the agent. autoApprove means the agent can act without a person confirming each action. Patch those installs first, then rotate the highest-reach tokens on the installs that are still vulnerable.

Chain overview: https://www.cyera.com/blog/claw-chain-cyera-research-unveil-four-chainable-vulnerabilities-in-openclaw

Advisory feed newest date: 2026-09-11. For a release with no matching advisory, the report says: no published advisory as of 2026-09-11.

The pinned feed has 894 advisories: 760 from the global database and 134 published only on the repository. 59 of those repository advisories were already published on or before 2026-07-02. On that previous feed, 2026.1.29 moved from 712 advisories to 714 after the prerelease grammar fix.

## How this differs from Agent 365 / Defender

Microsoft Defender for Endpoint can discover OpenClaw and record the host process, the device, the user, autoApprove, and MCP servers. Discovery is not an exact build fingerprint. Agent 365 and Defender expose a Version string per agent. This lab's mock assigns no risk score, and it leaves version blank or stale for a configured subset of installs. That local mock is not the published schema. clawscore-fleet adds the build fingerprint, the advisory list, credential names only, and the fix order. Against the published schema, the claim is narrower: the idle Linux host, the per-build GHSA list, and the fix order.

Local-agent discovery fields: https://learn.microsoft.com/en-us/defender-endpoint/discover-local-ai-agents

Defender agent inventory: https://learn.microsoft.com/en-us/defender-xdr/security-for-ai/ai-agent-inventory

This repo does not call Microsoft. The mock is a local FastAPI service.

## What Defender / Agent 365 already do, and what we add

Defender and Agent 365 show each OpenClaw agent's version and map OpenClaw CVEs through Defender Vulnerability Management. ClawScore Fleet adds, per install: the build read from the shipped files (even when package.json is stripped, and on idle Linux hosts), the maker's full advisory list including repo-only advisories, the credential names that install can read, and a patch-then-rotate order with the minimum release that clears every critical and high advisory (2026.8.1 on the 2026-09-11 feed). Credential reach is lab-tested only.

Source: [inputs/rea-narrower-gap/CLAIMS.md](inputs/rea-narrower-gap/CLAIMS.md)

## Lab

Each image runs `npm install` for one pinned OpenClaw release. Compose starts the fleet on an internal Docker network and publishes no ports. 4 installs are stripped: package.json is removed, or rewritten so its version string is a lie. The fingerprint does not read package.json. Shared fingerprints return a range instead of picking one release. The scanner does not open the answer key. File reads per install stay within the limit (20).

The matrix covers 117 stable releases from 2026.1.29 through 2026.10.4. The lab runs 30 installs. 9 of them predate 2026.3.31 and were published in 2026-01, 2026-02, 2026-03.

Python 3.11.

## Idle Linux hosts

ClawScore scores an idle Linux host whose gateway is installed as a systemd user unit, enabled for the default target, with a linger marker and no running process. On that host package.json has no version string. The version is recovered from dist/build-info.json and kept when the hashed dist listing reaches Jaccard 0.99 against the reversed public tarball openclaw@2026.4.15 (digest 8c95f77538130c77967c970da4744786c4d5b773937b8208f622efb4cf0d2564). That static read is recorded under evidence/rea/idle-linux. The on-disk CHANGELOG has 30 GHSA ids. 17 of those ids are absent from the pinned feed. That count compares the pinned feed with the CHANGELOG. It is not an Agent 365 result.

Published schema gate: verdict A, idle host not exposed, is PROVEN (published docs: discovery needs observed activity; native Linux unsupported; no idle lifecycle state). Verdict B, per-build GHSA list not exposed, is PROVEN (no vuln field on Graph agent types or AgentsInfo; TVM keys on CveId only; Version string IS exposed). Scope: published schemas and docs at the frozen commits only; Microsoft's backend and unpublished RawAgentInfo fields stay UNPROVEN.

- Host state: idle. Version source: build-info+dirlist. Recovered version: 2026.4.15. Dirlist Jaccard: 1.0.

## Results

Generated from evidence/verify-report.json by make verify. Do not edit this section by hand.

lab mock registry lists 30 / 14 with a blank or stale mock version / 27 vulnerable / rotate these 8 tokens first

- Stable releases with a tarball and listing: 117 of 117.
- Exact classification on non-colliding releases: 116 of 116 (100.0%).
- Fingerprint collision groups: 1. Included group: 2026.4.7-1, 2026.4.8.
- Directory listing alone: 118 of 118 (100.0%).
- File reads per install: max 1, mean 1.00 (limit 20).
- Lab installs before 2026.3.31: 9 (minimum 8).
- Exact version on non-colliding lab installs: 26 of 26 (100.0%). Target 95%.
- Exact version before 2026.3.31: 9 of 9 (100.0%).
- Range verdicts on colliding lab installs: 4 of 4.
- Stripped installs classified: 4 of 4.
- CVE map diff lines: 0.
- semver disagreements: 65. Unexplained: 0.
- 2026.4.22 shows 148 advisories (1 critical / 84 high). Cited from evidence/landscape/CLAIMS.md.
- Blast-radius recall: 42 of 42 (100.0%). Target 90%.
- Seed hashes from the v0.1 table: 9 of 9.
- Gate status: pass.

No gate failures.

Rotation order (highest reach first):

- AWS_ACCESS_KEY_ID (reach 5; claw-09, claw-10, claw-16, claw-25, claw-26)
- SLACK_BOT_TOKEN (reach 5; claw-07, claw-13, claw-14, claw-15, claw-23)
- STRIPE_SECRET_KEY (reach 5; claw-08, claw-14, claw-15, claw-16, claw-24)
- ANTHROPIC_API_KEY (reach 4; claw-09, claw-15, claw-16, claw-25)
- AWS_SECRET_ACCESS_KEY (reach 4; claw-10, claw-11, claw-26, claw-27)
- GITHUB_PERSONAL_ACCESS_TOKEN (reach 4; claw-05, claw-12, claw-13, claw-21)
- OPENAI_API_KEY (reach 4; claw-06, claw-13, claw-14, claw-22)
- DISCORD_BOT_TOKEN (reach 3; claw-11, claw-12, claw-27)

Claw Chain advisories from the generated map:

- CVE-2026-44112: OpenClaw: OpenShell FS bridge writes stay pinned to the sandbox mount root (affected <= 2026.4.21, fixed in 2026.4.22)
  - https://github.com/advisories/GHSA-wppj-c6mr-83jj
  - https://nvd.nist.gov/vuln/detail/CVE-2026-44112
- CVE-2026-44113: OpenClaw: OpenShell FS bridge reads pin and verify the opened file before returning bytes (affected <= 2026.4.21, fixed in 2026.4.22)
  - https://github.com/advisories/GHSA-5h3g-6xhh-rg6p
  - https://nvd.nist.gov/vuln/detail/CVE-2026-44113
- GHSA-x3h8-jrgh-p8jx: OpenClaw's exec allowlist analysis rejects shell expansion in unquoted heredocs (affected <= 2026.4.21, fixed in 2026.4.22)
  - https://github.com/advisories/GHSA-x3h8-jrgh-p8jx
- CVE-2026-44118: OpenClaw: MCP loopback owner context is derived from server-issued bearer tokens (affected <= 2026.4.21, fixed in 2026.4.22)
  - https://github.com/advisories/GHSA-r6xh-pqhr-v4xh
  - https://nvd.nist.gov/vuln/detail/CVE-2026-44118

## Defender export

`make export` writes one row per lab install to evidence/export/defender_local_agents.csv and evidence/export/agentsinfo_local.jsonl. CSV text cells, except the header and the integer columns, are prefixed with a single quote when the first character would start a formula, then quoted under RFC 4180. Excel can drop that quote when a workbook is saved and opened again. A leading tab was not used. Whether that variant is better for our consumers is UNPROVEN. JSONL cells are not escaped. Risk level is empty. Device ID is lab-derived, Defender format UNPROVEN: a hash of device fields recorded in the lab scan. The derivation is in docs/defender-export-lab-fields.md. The lab scan records no observation clock, so `make export` and `make verify` write one UTC time to evidence/lab-scan-observed-at.txt when that file is absent and then reuse the committed line. First seen, Timestamp, and LastUpdatedDateTime are that recorded observation. PublishedStatus is null. `make feed-check` logs the newest OpenClaw advisory on GitHub against the pinned feed date. It does not change pinned results. It logs SKIP when the query cannot be completed.

Version is the fingerprinted release when the verdict is exact, and blank when the verdict is a range. Remote MCP rows are the servers that have an endpoint in the scan. Local MCP rows are the server names recorded for the install. trustedProcess is the string false because the scan records no trusted-process grant. LifecycleStatus is Active when evidence/ps.txt shows the container is Up. AgentId is a GUID derived from the install id. aadDeviceId stays empty because the scan records no directory device id. Credential cells list class names only.

Spec lines copied verbatim:

GLOBAL UNPROVENS (Learn doesn't document them)
- Export file format (CSV or XLSX), header spelling in the file, column order, date format, encoding. Learn says only "select Export to download the list" (C09).
- How Defender formats an OpenClaw Version string, e.g. "2026.4.22" vs "v2026.4.22".
- Row grain is documented: one row per agent installation, so a repeat on several devices or accounts appears more than once (C10).
Agent name | string, "OpenClaw" for our rows | C01; the Name value "OpenClaw", vendor "OpenClaw Foundation" (C27, support matrix) | documented; the cell type is UNPROVEN
Version | string | C01 "The discovered agent, and the version installed." | documented; format UNPROVEN
Device ID | string | C02 | documented; format UNPROVEN
OS platform | string (Windows, macOS) | C02 | documented; value set UNPROVEN
Device type | string | C02 | documented; value set UNPROVEN
Risk indicators | string list, e.g. "Running on a Critical Device" | C05 | documented; list separator UNPROVEN
Recommendations | string | C06 | documented; cell format (count vs names) UNPROVEN
First seen | datetime | C08 | documented; format UNPROVEN, so emit ISO 8601 UTC
AgentId | CONFLICT: schema says string (C14 page) vs discover says guid (C13) | emit a GUID string | flag in README
Name / AgentName | CONFLICT: discover lists Name (C16), schema lists AgentName (C15) | emit both keys, same value | flag in README
PublishedStatus | string: Draft or Published | C18 | documented; value for local agents UNPROVEN
  relatedProcess string (C23); OpenClaw's process name is UNPROVEN

## GHSA-only advisories

Lists the OpenClaw advisories that have no CVE id (59 in the OSV snapshot of 2026-10-18) per install, marking the 2026.4.3 to 2026.4.7 window as possibly affected where GitHub's range stops early.

On Linux hosts where OpenClaw is installed with npm, Defender Vulnerability Management does not list the package (Microsoft Learn, tvm-software-inventory), so neither CVE nor GHSA-only advisories surface there. ClawScore lists the GHSA-only ones.
