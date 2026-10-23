# rea-agent365-schema (Hark, frozen 2026-10-18)
This replaces the MOCK behind idle-Linux G3 with real public artifacts: Microsoft Graph CSDL (v1.0 and beta) at msgraph-metadata 34b8e9c, plus the Defender and Agent 365 schema docs (SOURCES.md).
Extracted: 117 Graph agent types (v1.0 23, beta 94) in extracted/graph-*-agent-types.json, 35 AgentsInfo columns, 41 Azure Monitor AgentsInfo columns, 13 DeviceTvmSoftwareVulnerabilities columns.
Run `python3 gate_agent365_schema.py` (offline). Add `--refetch` to re-download the CSDL at the pinned commit, check its sha256 and re-extract.
Result at freeze:
- A "idle host not exposed": PROVEN
- B "per-build GHSA list not exposed": PROVEN
Both verdicts are limited to the published schemas and docs.
Caveats:
- AgentsInfo does expose a self-reported Version per agent.
- beta riskyAgent carries deviceId and machineId, but that is Entra ID risk data, not inventory.
- Unpublished RawAgentInfo fields and Microsoft's backend stay UNPROVEN.
- The discovery docs cover Windows and macOS only, so this says nothing about Linux-native support Microsoft might ship later.
