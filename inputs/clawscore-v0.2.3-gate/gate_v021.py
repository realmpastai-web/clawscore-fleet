#!/usr/bin/env python3
"""Hark frozen gate for ClawScore v0.2.1 (Defender-shaped export), spec export-spec-v0.2.1.md
sha256 ceb33179dda3ac307653d8bece6c13510c9188e60622246d7dc49d8f7e941769.
Usage: python3 gate_v021.py <PR checkout> <v0.2 baseline checkout (cc29565)> [--expected-lines expected-readme-lines.tsv]
Prints one PASS/FAIL/REPORT line per check, then a summary. Exit 1 if any FAIL."""
import csv, json, re, sys, glob, os
from pathlib import Path

PR, BASE = Path(sys.argv[1]), Path(sys.argv[2])
EXP = Path(sys.argv[sys.argv.index("--expected-lines") + 1]) if "--expected-lines" in sys.argv else Path(__file__).with_name("expected-readme-lines.tsv")
OUT = []
def rec(status, cid, msg): OUT.append((status, cid, msg)); print(f"{status}\t{cid}\t{msg}")
def check(cid, ok, msg): rec("PASS" if ok else "FAIL", cid, msg)

A_DEF = ["Agent name", "Version", "Device name", "Device ID", "OS platform", "Device type", "Account name",
         "Account domain", "Risk level", "Risk indicators", "Recommendations", "MCP servers", "Local MCPs", "First seen"]
CS = ["cs_build_verdict", "cs_candidates", "cs_reads", "cs_stripped", "cs_ghsa_ids", "cs_cve_ids", "cs_ghsa_only_count",
      "cs_crit_high_count", "cs_readable_secret_classes", "cs_fix_target", "cs_feed_newest"]
A_HEADER = A_DEF + CS
B_KEYS = ["Timestamp", "AgentId", "Name", "AgentName", "Platform", "Version", "PublishedStatus", "LifecycleStatus",
          "LastUpdatedDateTime", "McpServers", "DeclaredTools", "RawAgentInfo"] + CS
META_KEYS = ["vendor", "relatedProcess", "trustedProcess", "autoApprove", "deviceName", "aadDeviceId", "accountName",
             "accountDomain", "accountSid", "localMcps"]
UNCHANGED = ["landscape_hashes", "matrix_coverage", "matrix_exact", "collisions", "dirlist_metric", "cve_mapping",
             "semver_crosscheck", "freshness", "fix_target", "v01_regression"]
CS_GATES = {"cs_build_verdict": ["range_verdicts", "version_accuracy"], "cs_candidates": ["range_verdicts", "collisions"],
            "cs_reads": ["reads"], "cs_stripped": ["stripped"], "cs_ghsa_ids": ["cve_mapping"], "cs_cve_ids": ["cve_mapping"],
            "cs_ghsa_only_count": ["cve_mapping"], "cs_crit_high_count": ["cve_mapping"],
            "cs_readable_secret_classes": ["blast_recall"], "cs_fix_target": ["fix_target"], "cs_feed_newest": ["freshness"]}
ISO = re.compile(r"^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d(\.\d+)?Z$")
GUID = re.compile(r"^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$")
GHSA = re.compile(r"^GHSA(-[23456789cfghjmpqrvwx]{4}){3}$")
CVE = re.compile(r"^CVE-\d{4}-\d{4,}$")
SECRET_VAL = re.compile(r"(sk-[A-Za-z0-9]{16,}|ghp_[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16}|xox[bp]-[0-9A-Za-z-]{10,}|-----BEGIN|sk_live_[0-9A-Za-z]{10,})")

def find(name):
    hits = [p for p in PR.rglob(name) if ".git" not in p.parts and "node_modules" not in p.parts]
    return hits
def listcell(s):
    s = s.strip()
    if s == "": return [], "empty"
    if s.startswith("["): return json.loads(s), "json"
    for sep in (";", "|"):
        if sep in s: return [x.strip() for x in s.split(sep)], sep
    return [s], "single"

# ---------- inputs
rep = json.loads((PR / "evidence/verify-report.json").read_text())
base = json.loads((BASE / "evidence/verify-report.json").read_text())
gates = rep.get("gates", {})
scan = {x["id"]: x for x in json.loads((PR / "evidence/scan.json").read_text())["installs"]}
truth = {r["install_id"]: r for r in csv.DictReader(open(PR / "evidence/version-confusion.csv"))}
ghsa_all = json.loads((PR / "evidence/landscape/ghsa-all.json").read_text())
nocve = {a["ghsa_id"] for a in ghsa_all if not a.get("cve_id")}

# ---------- G0 release + files
check("G0.release", rep.get("release") == "0.2.1", f"release={rep.get('release')!r} (want '0.2.1')")
fa, fb = find("defender_local_agents.csv"), find("agentsinfo_local.jsonl")
check("G0.fileA", len(fa) == 1, f"defender_local_agents.csv found {len(fa)}: {[str(p.relative_to(PR)) for p in fa]}")
check("G0.fileB", len(fb) == 1, f"agentsinfo_local.jsonl found {len(fb)}: {[str(p.relative_to(PR)) for p in fb]}")
if len(fa) != 1 or len(fb) != 1:
    print("STOP: export files missing"); sys.exit(1)

# ---------- G1 File A header + types
raw = fa[0].read_bytes()
check("G1.encoding", not raw.startswith(b"\xef\xbb\xbf") and raw.decode("utf-8", "strict") is not None, "UTF-8, no BOM")
rowsA = list(csv.reader(raw.decode().splitlines()))
hdr = rowsA[0]
check("G1.header", hdr == A_HEADER, f"{len(hdr)} cols; exact match to 14 Defender + 11 cs_ names" + ("" if hdr == A_HEADER else f"; got {hdr}"))
A = [dict(zip(hdr, r)) for r in rowsA[1:]]
check("G1.rows", len(A) == 30 and all(len(r) == len(hdr) for r in rowsA[1:]), f"{len(A)} data rows (want 30, one per lab install, C10)")
devs = [r.get("Device name", "") for r in A]
check("G1.join", sorted(devs) == sorted(scan) and len(set(devs)) == len(devs), "Device name == scan.json install id, 1:1")
sepsA = set(); badA = []
for r in A:
    d = r.get("Device name")
    try:
        if r["Agent name"] != "OpenClaw": badA.append((d, "Agent name"))
        if not r["Device ID"]: badA.append((d, "Device ID empty"))
        if r["Risk level"] != "": badA.append((d, "Risk level must be empty (no E7/Agent 365 in lab, C29)"))
        for c in ("MCP servers", "Local MCPs"):
            if not re.fullmatch(r"\d+", r[c]): badA.append((d, c + " not int"))
        if not ISO.match(r["First seen"]): badA.append((d, "First seen not ISO 8601 UTC"))
        for c in ("Risk indicators", "cs_candidates", "cs_ghsa_ids", "cs_cve_ids", "cs_readable_secret_classes"):
            sepsA.add((c, listcell(r[c])[1]))
    except Exception as e: badA.append((d, f"exception {e}"))
check("G1.types", not badA, f"cell types; bad={badA[:8]}")
rec("REPORT", "G1.list_separators", sorted(sepsA))

# ---------- G2 File B keys + types
B = [json.loads(l) for l in fb[0].read_text().splitlines() if l.strip()]
check("G2.rows", len(B) == 30, f"{len(B)} JSONL rows (want 30)")
badB = []
for o in B:
    m = o.get("RawAgentInfo", {}).get("localAgentMetadata", {}) if isinstance(o.get("RawAgentInfo"), dict) else {}
    d = m.get("deviceName")
    if list(o) != B_KEYS and set(o) != set(B_KEYS): badB.append((d, f"keys {sorted(set(o) ^ set(B_KEYS))}"))
    if set(o.get("RawAgentInfo", {}) or {}) != {"localAgentMetadata"}: badB.append((d, "RawAgentInfo keys"))
    if set(m) != set(META_KEYS): badB.append((d, f"localAgentMetadata keys {sorted(set(m) ^ set(META_KEYS))}"))
    for k in ("Timestamp", "LastUpdatedDateTime"):
        if not (isinstance(o.get(k), str) and ISO.match(o[k])): badB.append((d, k))
    if not (isinstance(o.get("AgentId"), str) and GUID.match(o["AgentId"])): badB.append((d, "AgentId not GUID string (CONFLICT rule)"))
    if not (o.get("Name") == o.get("AgentName") == "OpenClaw"): badB.append((d, "Name/AgentName (CONFLICT rule: both, same value)"))
    if o.get("Platform") != "LocalAgents": badB.append((d, "Platform"))
    if not isinstance(o.get("Version"), str): badB.append((d, "Version type"))
    if o.get("PublishedStatus") not in ("Draft", "Published", None): badB.append((d, "PublishedStatus"))
    if o.get("LifecycleStatus") not in ("Active", "Blocked", "Uninstalled", "Deleted"): badB.append((d, "LifecycleStatus"))
    for k in ("McpServers", "DeclaredTools"):
        v = o.get(k)
        if not (isinstance(v, list) and all(isinstance(x, dict) and set(x) == {"name", "type", "endpoint"} for x in v)): badB.append((d, k))
    if m:
        if m.get("vendor") != "OpenClaw Foundation": badB.append((d, "vendor"))
        for k in ("trustedProcess", "autoApprove"):
            if m.get(k) not in ("true", "false"): badB.append((d, k + " must be string true/false (C20)"))
        for k in ("relatedProcess", "deviceName", "aadDeviceId", "accountName", "accountDomain", "accountSid"):
            if not isinstance(m.get(k), str): badB.append((d, k))
        lm = m.get("localMcps")
        if not (isinstance(lm, list) and all(isinstance(x, dict) and set(x) == {"name", "transportType", "commandName"} for x in lm)): badB.append((d, "localMcps"))
    if not (o.get("cs_build_verdict") in ("exact", "range", "unknown")): badB.append((d, "cs_build_verdict"))
    for k in ("cs_candidates", "cs_ghsa_ids", "cs_cve_ids", "cs_readable_secret_classes"):
        if not (isinstance(o.get(k), list) and all(isinstance(x, str) for x in o[k])): badB.append((d, k))
    for k in ("cs_reads", "cs_ghsa_only_count", "cs_crit_high_count"):
        if not (isinstance(o.get(k), int) and not isinstance(o.get(k), bool)): badB.append((d, k))
    if not isinstance(o.get("cs_stripped"), bool): badB.append((d, "cs_stripped"))
    if o.get("cs_fix_target") != "2026.5.27": badB.append((d, "cs_fix_target"))
    if o.get("cs_feed_newest") != "2026-07-02": badB.append((d, "cs_feed_newest"))
    if any(not GHSA.match(x) for x in o.get("cs_ghsa_ids") or []): badB.append((d, "GHSA id format"))
    if any(not CVE.match(x) for x in o.get("cs_cve_ids") or []): badB.append((d, "CVE id format"))
    if any(not re.fullmatch(r"[A-Z0-9_]+", x) for x in o.get("cs_readable_secret_classes") or []): badB.append((d, "secret class not a NAME"))
check("G2.keys_types", not badB, f"exact key set {len(B_KEYS)} top + {len(META_KEYS)} metadata; types; bad={badB[:8]}")
rec("REPORT", "G2.key_order_matches_list", all(list(o) == B_KEYS for o in B))
Bd = {o["RawAgentInfo"]["localAgentMetadata"]["deviceName"]: o for o in B if isinstance(o.get("RawAgentInfo"), dict) and "localAgentMetadata" in o["RawAgentInfo"]}
check("G2.join", sorted(Bd) == sorted(scan) and len({o["AgentId"] for o in B}) == len(B), "deviceName 1:1 with installs; AgentId unique")

# ---------- G3 A<->B and cs_ values vs evidence
bad3 = []
for r in A:
    d = r["Device name"]; o = Bd.get(d); s = scan.get(d); t = truth.get(d)
    if not (o and s and t): bad3.append((d, "missing in B/scan/truth")); continue
    if r["Version"] != o["Version"]: bad3.append((d, "Version A!=B"))
    if int(r["MCP servers"]) != len(o["McpServers"]): bad3.append((d, "MCP servers != len(McpServers)"))
    if int(r["Local MCPs"]) != len(o["RawAgentInfo"]["localAgentMetadata"]["localMcps"]): bad3.append((d, "Local MCPs != len(localMcps)"))
    want = {"cs_build_verdict": s["verdict"], "cs_candidates": s["candidates"], "cs_reads": len(s["files_read"]),
            "cs_stripped": t["stripped"] != "none", "cs_ghsa_ids": s["ghsa_ids"], "cs_cve_ids": s["cves"],
            "cs_ghsa_only_count": sum(1 for g in s["ghsa_ids"] if g in nocve),
            "cs_crit_high_count": s["advisory_critical"] + s["advisory_high"],
            "cs_readable_secret_classes": s["credentials"], "cs_fix_target": "2026.5.27", "cs_feed_newest": "2026-07-02"}
    for k, w in want.items():
        bv = o.get(k)
        if isinstance(w, list):
            if sorted(bv or []) != sorted(w): bad3.append((d, f"{k} B!=evidence"))
            if sorted(listcell(r[k])[0]) != sorted(w): bad3.append((d, f"{k} A!=evidence"))
        else:
            if bv != w: bad3.append((d, f"{k} B={bv!r} want {w!r}"))
            av = r[k]
            if str(w).lower() != av.lower(): bad3.append((d, f"{k} A={av!r} want {w!r}"))
    if s["verdict"] != t["verdict"]: bad3.append((d, "scan verdict != version-confusion.csv"))
check("G3.values", not bad3, f"A==B and cs_ == scan.json/version-confusion.csv/ghsa-all.json on 30 installs; bad={bad3[:8]}")
rec("REPORT", "G3.verdicts", {v: sum(1 for o in B if o["cs_build_verdict"] == v) for v in ("exact", "range", "unknown")})
rng = sorted(d for d, o in Bd.items() if o["cs_build_verdict"] == "range")
check("G3.range_pair", all(sorted(Bd[d]["cs_candidates"]) == ["2026.4.7-1", "2026.4.8"] for d in rng) and len(rng) == 4,
      f"range rows {rng}: candidates exactly [2026.4.7-1, 2026.4.8] (v0.2 lab: claw-10..13)")

# ---------- G4 cs_ gate trace
bad4 = [(c, g) for c, gs in CS_GATES.items() for g in gs if not gates.get(g, {}).get("pass")]
check("G4.cs_gate_trace", not bad4, f"every cs_ column's gates pass in the same verify-report.json; failing={bad4}")

# ---------- G5 the 10 unchanged gates
for g in UNCHANGED:
    a, b = gates.get(g), base["gates"].get(g)
    check(f"G5.{g}", a == b and a and a.get("pass") is True, "identical to v0.2 @ cc29565" + ("" if a == b else f"; diff keys {sorted(k for k in set(a or {}) | set(b or {}) if (a or {}).get(k) != (b or {}).get(k))}"))
for g in ["reads", "old_builds", "version_accuracy", "range_verdicts", "stripped", "blast_recall"]:
    a, b = gates.get(g), base["gates"].get(g)
    check(f"G5.lab.{g}", a == b and a and a.get("pass") is True, "lab gate identical to v0.2")
extra = sorted(set(gates) - set(base["gates"]))
rec("REPORT", "G5.new_gates", extra)
for g in extra: check(f"G5.new.{g}", gates[g].get("pass") is True, json.dumps(gates[g])[:200])
check("G5.ok", rep.get("ok") is True and not rep.get("failures"), f"ok={rep.get('ok')} failures={rep.get('failures')}")

# ---------- G6 README lines
readme = (PR / "README.md").read_text()
norm = lambda s: " ".join(s.replace("|", " | ").split())
nr = norm(readme)
exp = [l.rstrip("\n").split("\t", 1) for l in open(EXP) if l.strip()]
miss = [(k, v[:70]) for k, v in exp if norm(v) not in nr]
check("G6.readme_lines", not miss, f"{len(exp)-len(miss)}/{len(exp)} spec lines verbatim (12 UNPROVEN + 2 CONFLICT, whitespace-normalized); missing={miss}")

# ---------- G7 wording + secrets
texts = {str(p.relative_to(PR)): p.read_text(errors="ignore") for p in [fa[0], fb[0], PR / "README.md"]}
safe = [f for f, t in texts.items() if re.search(r"\bsafe\b", t, re.I)]
check("G7.no_safe", not safe, f"word 'safe' in {safe}")
miss_claims = [l.strip()[:90] for l in readme.splitlines() if re.search(r"defender", l, re.I) and re.search(r"\b(miss|misses|missed|blind|can't see|cannot see|fails to)\b", l, re.I)]
check("G7.no_defender_misses", not miss_claims, f"README lines claiming Defender misses: {miss_claims}")
vals = [f for f, t in texts.items() if SECRET_VAL.search(t)]
check("G7.no_secret_values", not vals, f"secret-shaped values in {vals}")

# ---------- summary
f = [c for s, c, _ in OUT if s == "FAIL"]
print(f"SUMMARY pass={sum(1 for s,_,_ in OUT if s=='PASS')} fail={len(f)} report={sum(1 for s,_,_ in OUT if s=='REPORT')} failed={f}")
sys.exit(1 if f else 0)
