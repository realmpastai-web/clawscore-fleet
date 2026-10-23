#!/usr/bin/env python3
"""rea-agent365-schema gate (Hark, frozen 2026-10-18). Offline over frozen files; --refetch also re-extracts Graph CSDL at the pinned commit.
Claim A: "an idle host is not exposed" (installed openclaw gateway, nothing running, native Linux)
Claim B: "the per-build GHSA list is not exposed"
Each verdict is PROVEN or UNPROVEN, and is scoped to the PUBLISHED schemas and docs frozen here, not to Microsoft's backend."""
import json, re, sys, html, hashlib, subprocess, urllib.request
from pathlib import Path
H = Path(__file__).resolve().parent
GSHA = "34b8e9c29032c82352a6fd7138be0a864a842bb2"
VULN = re.compile(r"vulnerab|\bcve|ghsa|advisor|security ?update|patch", re.I)
fail = []
def say(tag, ok, msg):
    print(("PASS" if ok else "FAIL") + "\t" + tag + "\t" + msg)
    if not ok: fail.append(tag)
def text(n):
    s = (H / "sources/learn" / (n + ".html")).read_text()
    m = re.search(r"<main.*?</main>", s, re.S)
    return " ".join(html.unescape(re.sub(r"<[^>]+>", " ", m.group(0) if m else s)).split())
# --- G0 optional refetch of the Graph CSDL at the pinned commit
if "--refetch" in sys.argv:
    for line in (H / "sources/graph-csdl.sha256").read_text().splitlines()[1:]:
        sha, rel, url = line.split("  ")
        if "WithDescriptions" not in rel: continue
        data = urllib.request.urlopen(url, timeout=120).read(); p = Path("/tmp") / Path(rel).name; p.write_bytes(data)
        say("G0.csdl_sha", hashlib.sha256(data).hexdigest() == sha, rel)
        tag = "v1.0" if "v1.0" in rel else "beta"
        out = subprocess.run([sys.executable, str(H / "extract_graph_agent_types.py"), str(p), tag], capture_output=True, text=True).stdout
        say("G0.extract_matches_frozen", json.loads(out) == json.loads((H / f"extracted/graph-{tag}-agent-types.json").read_text()), tag)
# --- G1 Graph agent types: no vulnerability/CVE/GHSA property; list version/host/state carriers
g = json.loads((H / "extracted/graph-v1.0-agent-types.json").read_text()) + json.loads((H / "extracted/graph-beta-agent-types.json").read_text())
vuln_props = [(t["metadata"], t["name"], p["name"]) for t in g for p in t["props"] if VULN.search(p["name"] or "") or VULN.search(p["type"] or "")]
say("G1.graph_agent_types_counted", len(g) == 117, f"{len(g)} agent types (v1.0 23 + beta 94)")
say("G1.graph_no_vuln_property", not vuln_props, f"vuln/cve/ghsa/advisory props on agent types: {vuln_props}")
ver = sorted({f"{t['metadata']}:{t['name']}.{p['name']}" for t in g for p in t["props"] if re.fullmatch(r"(version|protocolVersion)", p["name"] or "")})
host = sorted({f"{t['metadata']}:{t['name']}.{p['name']}" for t in g for p in t["props"] if re.search(r"device|host|machine", p["name"] or "", re.I)})
print(f"INFO\tgraph version props: {ver}\nINFO\tgraph host props: {host}")
# --- G2 Defender AgentsInfo: Version present (self-reported), no vuln column, LifecycleStatus values
cols = [l.split(" | ") for l in (H / "extracted/defender-agentsinfo-columns.txt").read_text().splitlines() if " | " in l]
names = [c[0] for c in cols]
say("G2.agentsinfo_35_columns", len(names) == 35, f"{len(names)} columns")
say("G2.agentsinfo_no_vuln_column", not [n for n, _, d in cols if VULN.search(n) or VULN.search(d)], "no vuln/cve/ghsa column or description")
say("G2.agentsinfo_has_version", "Version" in names, "Version | string | Version of the agent  (one string per agent row, so version IS exposed)")
life = next(d for n, _, d in cols if n == "LifecycleStatus")
say("G2.lifecycle_no_idle_state", not re.search(r"idle|installed|stopped|not running|dormant", life.replace("Uninstalled", ""), re.I), f"LifecycleStatus: {life}")
# --- G3 Defender TVM: the only vulnerability identifier is CveId
tvm = [l.split(" | ")[0] for l in (H / "extracted/defender-devicetvmsoftwarevulnerabilities-columns.txt").read_text().splitlines() if " | " in l]
say("G3.tvm_cve_only", "CveId" in tvm and not [c for c in tvm if re.search(r"ghsa|advisory", c, re.I)], f"DeviceTvmSoftwareVulnerabilities ids: {[c for c in tvm if re.search('cve|ghsa|advis', c, re.I)]}")
# --- G4 quotes: discovery needs observed activity; Windows/macOS only; OpenClaw listed
Q = {"local-agent-discovery-overview": ["Defender discovers local AI agents on Windows and macOS endpoints.",
                                        "An installed agent might not appear until Defender observes agent activity.",
                                        "Defender lists a local AI agent after it observes agent activity on an onboarded device."],
     "ai-agent-support-matrix": ["WSL support doesn't indicate support for native Linux endpoints.",
                                 "Defender lists an agent after it observes agent activity on an onboarded device.",
                                 "OpenClaw OpenClaw Foundation"],
     "discover-local-ai-agents": ["relatedProcess The process that hosts the agent"]}
for page, qs in Q.items():
    t = text(page)
    for q in qs: say("G4.quote", q in t, f"{page}: \"{q}\"")
# --- verdicts
A = all(not x.startswith(("G4", "G2.lifecycle")) for x in fail)
B = all(not x.startswith(("G1.graph_no_vuln", "G2.agentsinfo_no_vuln", "G3")) for x in fail)
print(f"VERDICT A idle host not exposed: {'PROVEN' if A else 'UNPROVEN'} (published docs: discovery needs observed activity; native Linux unsupported; no idle lifecycle state)")
print(f"VERDICT B per-build GHSA list not exposed: {'PROVEN' if B else 'UNPROVEN'} (no vuln field on Graph agent types or AgentsInfo; TVM keys on CveId only; Version string IS exposed)")
print("SCOPE published schemas and docs at the frozen commits only; Microsoft's backend and unpublished RawAgentInfo fields stay UNPROVEN")
sys.exit(0 if not fail else 1)
