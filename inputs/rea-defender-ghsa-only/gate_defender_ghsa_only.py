#!/usr/bin/env python3
"""rea-defender-ghsa-only gate (Hark, frozen 2026-10-18). Offline, stdlib only.
Question: from public Microsoft docs only, would Microsoft Defender Vulnerability Management (MDVM), Defender for
Containers, or Agent 365 (AgentsInfo) surface a no-CVE GHSA advisory on an npm package such as openclaw?"""
import hashlib, re, sys
from pathlib import Path
H = Path(__file__).resolve().parent; L = H / "sources" / "learn"; P = H / "sources" / "prior"; fails = []
def chk(t, ok, m): print(("PASS" if ok else "FAIL") + "\t" + t + "\t" + m); ok or fails.append(t)
def t(n): return (L / f"{n}.txt").read_text(encoding="utf-8")
def quote(tag, n, q): chk(tag, q in t(n), f'{n}: "{q[:120]}"')

for line in (P / "PRIOR_HASHES.txt").read_text().split("\n"):
    if line.strip():
        h, f = line.split(); chk("prior.hash", hashlib.sha256((P / f).read_bytes()).hexdigest() == h, f"prior/{f} = rea-agent365-schema @2d4e787")

# Q1 Linux host, npm-installed openclaw (Defender for Endpoint / MDVM)
quote("Q1.linux_native_pkg_only", "learn-tvm-software-inventory", "On Linux, Defender Vulnerability Management only lists software installed using native package managers such as rpm , dnf , and yum .")
quote("Q1.manual_not_listed", "learn-tvm-software-inventory", "Applications installed manually or with custom methods such as unpacked binaries or JAR based applications, aren't listed.")
comp = t("learn-tvm-vulnerable-components")
chk("Q1.components_list", "supports the following software components:" in comp and "openclaw" not in comp.lower() and not re.search(r"\bnpm\b", comp, re.I),
    "custom vulnerable-components list (Log4J, Next.js, React Server DOM ...) names neither OpenClaw nor npm")
quote("Q1.cpe_required", "learn-tvm-software-inventory", "Software products without a CPE are shown in the software inventory page, but they're not supported by vulnerability management.")

# Q2 identifiers: MDVM CAN name a non-CVE vulnerability
quote("Q2.tvm_ids_exist", "defender-vulnerability-management_tvm-weaknesses", "If there's no official CVE-ID assigned to a vulnerability, the vulnerability name is assigned by Defender Vulnerability Management using the format TVM-2020-002 .")
quote("Q2.hunting_cveid", "defender-xdr_advanced-hunting-devicetvmsoftwarevulnerabilities-table", "CveId string Unique identifier assigned to the security vulnerability under the Common Vulnerabilities and Exposures (CVE) system")
quote("Q2.hunting_kb_cveid", "defender-xdr_advanced-hunting-devicetvmsoftwarevulnerabilitieskb-table", "CveId string Unique identifier assigned to the security vulnerability under the Common Vulnerabilities and Exposures (CVE) system")
ghsa = [f.name for f in sorted(L.glob("*.txt")) if "GHSA" in f.read_text(encoding="utf-8")]
chk("Q2.no_ghsa_anywhere", not ghsa, f"0 of {len(list(L.glob('*.txt')))} archived Microsoft Learn pages mention GHSA")

# Q3 containers: Defender for Containers DOES scan Node.js packages in Linux images (the threat path)
quote("Q3.containers_nodejs", "azure_defender-for-cloud_support-matrix-defender-for-containers", "Language specific packages Supported * Python * Node.js")
quote("Q3.language_linux_only", "azure_defender-for-cloud_agentless-vulnerability-assessment-azure", "Language package vulnerability assessment (Linux only)")
quote("Q3.findings_cves_tab", "azure_defender-for-cloud_view-and-remediate-vulnerability-assessment-findings", "CVEs tab to review the CVEs associated with the recommendation")

# Q4 Agent 365 / AgentsInfo: agent inventory, no advisory columns
cols = [l.split("|")[0].strip() for l in (P / "defender-agentsinfo-columns.txt").read_text().splitlines() if "|" in l]
az = [l.split("|")[0].strip() for l in (P / "azmon-agentsinfo-columns.txt").read_text().splitlines() if "|" in l]
adv = re.compile(r"cve|ghsa|vuln|advis|weakness", re.I)
chk("Q4.agentsinfo_no_advisory", len(cols) >= 30 and not [c for c in cols + az if adv.search(c)], f"AgentsInfo ({len(cols)} Defender, {len(az)} Azure Monitor columns): no CVE/GHSA/vulnerability column")
chk("Q4.agentsinfo_has_version", "Version" in cols, "AgentsInfo does carry a self-reported Version per agent (caveat)")

print("VERDICT Q1 Linux host, npm-global openclaw: MDVM does not list it (docs: Linux = native package managers only; custom components exclude OpenClaw/npm) -> no advisory of any kind, CVE or GHSA. PROVEN within published docs.")
print("VERDICT Q2 no-CVE representation: MDVM CAN name non-CVE vulnerabilities (TVM-YYYY-NNN), so 'Defender is CVE-only' is FALSE as a blanket claim. Advanced hunting keys on CveId; no archived page mentions GHSA. Whether MDVM's feed imports GHSA-only npm advisories as TVM ids: UNPROVEN.")
print("VERDICT Q3 containers: Defender for Containers scans Node.js language packages in Linux images (registry + runtime). A containerised openclaw IS in scope; whether a GHSA-only advisory surfaces there: UNPROVEN. Threat path - do not claim containers.")
print("VERDICT Q4 Agent 365: AgentsInfo is an agent inventory with a self-reported Version and no advisory columns. PROVEN for the published schema (unpublished RawAgentInfo fields stay UNPROVEN).")
print("README CLAIM ALLOWED: 'On Linux hosts where OpenClaw is installed with npm, Defender Vulnerability Management does not list the package (Microsoft Learn, tvm-software-inventory), so neither CVE nor GHSA-only advisories surface there; ClawScore lists the GHSA-only ones.'")
print("README CLAIM FORBIDDEN: 'Defender cannot show non-CVE advisories' / anything about container images / anything about Agent 365 backend.")
print("GATE " + ("PASS" if not fails else "FAIL " + str(sorted(set(fails)))))
sys.exit(1 if fails else 0)
