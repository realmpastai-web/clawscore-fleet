# rea-defender-ghsa-only (Hark, frozen 2026-10-18)
**Question:** would Microsoft Defender Vulnerability Management (MDVM), Defender for Containers, or Agent 365 surface a **no-CVE GHSA** on an npm package like openclaw? The sources are public Microsoft Learn pages plus the Agent 365 schema extracted earlier.
Run `python3 gate_defender_ghsa_only.py`. Its output equals gate-output.txt: 16 PASS, GATE PASS.
**Mutation:** adding OpenClaw to the components list makes the gate FAIL (mutation-components-add-openclaw.log).

| Q | Verdict |
|---|---|
| Q1 Linux host, npm-installed openclaw | **PROVEN (docs): not listed.** On Linux, MDVM lists only software from native package managers, and its custom components list excludes OpenClaw and npm. So no advisory surfaces there at all, CVE or GHSA. |
| Q2 Can Defender show a non-CVE vulnerability? | **Yes.** MDVM names non-CVE vulnerabilities `TVM-YYYY-NNN`, so "Defender is CVE-only" is FALSE. Advanced hunting keys on `CveId`, and none of the 11 archived pages mention GHSA. Whether GHSA-only npm advisories become TVM ids: UNPROVEN. |
| Q3 Containers | **Threat path.** Defender for Containers scans Node.js language packages in Linux images, at registry and runtime. A containerised openclaw is in scope. Whether GHSA-only advisories surface there: UNPROVEN. |
| Q4 Agent 365 (AgentsInfo) | **PROVEN (schema):** an agent inventory with a self-reported Version and no advisory column. Unpublished RawAgentInfo fields stay UNPROVEN. |

**README claim allowed:** "On Linux hosts where OpenClaw is installed with npm, Defender Vulnerability Management does not list the package (Microsoft Learn, tvm-software-inventory), so neither CVE nor GHSA-only advisories surface there. ClawScore lists the GHSA-only ones."
**Forbidden:**
- "Defender can't show non-CVE advisories"
- any claim about container images
- any claim about Agent 365's backend
