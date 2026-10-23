CLAWSCORE v0.2.1: DEFENDER-SHAPED EXPORT COLUMN SPEC (Hark, 2026-10-17)
Sources: inputs/ms-defender-check/sources/*.txt @ 7eb57ff. Quote IDs C01-C29 are in export-spec-quotes.tsv (29/29 verified). Page keys: discover = https://learn.microsoft.com/en-us/defender-endpoint/discover-local-ai-agents, agentsinfo = https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-agentsinfo-table, risk = https://learn.microsoft.com/en-us/defender-xdr/security-for-ai/ai-agent-risk-assessment.

GLOBAL UNPROVENS (Learn doesn't document them)
- Export file format (CSV or XLSX), header spelling in the file, column order, date format, encoding. Learn says only "select Export to download the list" (C09).
- How Defender formats an OpenClaw Version string, e.g. "2026.4.22" vs "v2026.4.22".
- Row grain is documented: one row per agent installation, so a repeat on several devices or accounts appears more than once (C10).

FILE A: defender_local_agents.csv (mirrors Portal > Assets > AI agents > Local agents)
col | our type | documented by | status
Agent name | string, "OpenClaw" for our rows | C01; the Name value "OpenClaw", vendor "OpenClaw Foundation" (C27, support matrix) | documented; the cell type is UNPROVEN
Version | string | C01 "The discovered agent, and the version installed." | documented; format UNPROVEN
Device name | string | C02 | documented
Device ID | string | C02 | documented; format UNPROVEN
OS platform | string (Windows, macOS) | C02 | documented; value set UNPROVEN
Device type | string | C02 | documented; value set UNPROVEN
Account name | string | C03 | documented
Account domain | string | C03 | documented
Risk level | enum: High, Medium, Low, No known risk, Not evaluated | C04 + risk page (C11, C12) | documented; needs E7 or Agent 365 (C29), so leave empty without one
Risk indicators | string list, e.g. "Running on a Critical Device" | C05 | documented; list separator UNPROVEN
Recommendations | string | C06 | documented; cell format (count vs names) UNPROVEN
MCP servers | int | C07 "The number of remote MCP servers..." | documented
Local MCPs | int | C07 | documented
First seen | datetime | C08 | documented; format UNPROVEN, so emit ISO 8601 UTC

FILE B: agentsinfo_local.jsonl (AgentsInfo rows where Platform == "LocalAgents", C21)
col | Learn type | documented by | status
Timestamp | datetime | C28 | documented
AgentId | CONFLICT: schema says string (C14 page) vs discover says guid (C13) | emit a GUID string | flag in README
Name / AgentName | CONFLICT: discover lists Name (C16), schema lists AgentName (C15) | emit both keys, same value | flag in README
Platform | string, "LocalAgents" | C21 | documented
Version | string | C16 + schema | documented
PublishedStatus | string: Draft or Published | C18 | documented; value for local agents UNPROVEN
LifecycleStatus | string: Active, Blocked, Uninstalled, Deleted | C17 | documented
LastUpdatedDateTime | datetime | C19 | documented
McpServers | dynamic array of {name, type, endpoint} | C16; field names from discover query (C25) | documented
DeclaredTools | dynamic array of {name, type, endpoint} | C16; discover query | documented
RawAgentInfo.localAgentMetadata | dynamic | C16 | documented, with:
  vendor string "OpenClaw Foundation" (C22, C27)
  relatedProcess string (C23); OpenClaw's process name is UNPROVEN
  trustedProcess string "true"/"false", not bool (C20)
  autoApprove string "true"/"false", not bool (C20)
  deviceName, aadDeviceId, accountName, accountDomain, accountSid strings (discover table)
  localMcps array of {name, transportType, commandName} (C24, C26)
Other AgentsInfo columns (Owners, Model, Instructions, ...) are for cloud agents and empty for local agents (C16 context), so omit them.

CLAWSCORE EXTENSION COLUMNS (ours, not Defender's; prefix cs_, appended to both files)
cs_build_verdict string exact|range|unknown | cs_candidates string list | cs_reads int | cs_stripped bool | cs_ghsa_ids string list | cs_cve_ids string list | cs_ghsa_only_count int | cs_crit_high_count int | cs_readable_secret_classes string list (class names only, never values) | cs_fix_target string (2026.5.27) | cs_feed_newest date (2026-07-02)
Each must trace to verify-report.json gates: stripped, range_verdicts, cve_mapping, blast_recall, fix_target, freshness.

ACCEPTANCE FOR v0.2.1
- Header row of File A equals the 14 names above in that order, plus the cs_ columns.
- README lists every UNPROVEN and both CONFLICTs verbatim.
- No cs_ value appears without its gate passing in the same verify-report.json.
