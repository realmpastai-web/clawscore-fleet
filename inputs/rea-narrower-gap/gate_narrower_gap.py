#!/usr/bin/env python3
"""ClawScore Fleet narrower-gap gate (Hark, 2026-10-18, internal; static reads only, executes nothing it reads).

Claim: per OpenClaw install, clawscore-fleet links exact build -> maker-feed advisory list -> readable credential
names -> patch-then-rotate fix order; Microsoft's published docs cover each link only in a different or partial form.

Side A (Microsoft): 10 verbatim quotes from 8 Learn snapshots (sources/, fetched 2026-10-18), plus absence checks.
Side B (ours): values read from a clawscore-fleet checkout (evidence/verify-report.json, evidence/scan.json, README.md).

  python3 -B gate_narrower_gap.py --checkout <clawscore-fleet @756cd2a>       # GATE PASS, exit 0
  python3 -B gate_narrower_gap.py --checkout X --quotes controls/mutant-quotes-fabricated.tsv   # exit 1
  python3 -B gate_narrower_gap.py --checkout X --report controls/mutant-verify-report.json      # exit 1
Absence = "not found in these 8 pages", never "Microsoft cannot".
"""
import argparse, hashlib, html, json, re, sys
from pathlib import Path
H = Path(__file__).resolve().parent
ap = argparse.ArgumentParser(); ap.add_argument("--checkout", required=True); ap.add_argument("--quotes", default=str(H / "quotes.tsv")); ap.add_argument("--report")
a = ap.parse_args(); C = Path(a.checkout)
fails, info = [], []
def ck(name, ok, detail=""):
    print(("PASS" if ok else "FAIL") + "\t" + name + ("\t" + str(detail) if detail != "" else "")); ok or fails.append(name)
def text(p):
    t = p.read_text(encoding="utf-8"); m = re.search(r"<main.*?</main>", t, re.S); t = m.group(0) if m else t
    t = re.sub(r"<script.*?</script>|<style.*?</style>", "", t, flags=re.S); t = html.unescape(re.sub(r"<[^>]+>", " ", t))
    return re.sub(r" ([,.:;)])", r"\1", re.sub(r"\s+", " ", t))
# S0 sums
OUT = ("./gate-output.txt", "./controls-output.txt")  # checked by diff in the README command, not here (they contain this line)
bad = [l.split("  ")[1] for l in (H / "SHA256SUMS").read_text().splitlines() if l.split("  ")[1] not in OUT and hashlib.sha256((H / l.split("  ")[1]).read_bytes()).hexdigest() != l.split("  ")[0]]
ck("S0.sha256sums", not bad, f"files={len((H/'SHA256SUMS').read_text().splitlines())} bad={bad}")
pages = {p.name: text(p) for p in sorted((H / "sources").glob("*.html"))}
ck("S1.eight_snapshots", len(pages) == 8, len(pages))
# A: quotes
rows = [l.split("\t") for l in Path(a.quotes).read_text().splitlines()[1:] if l.strip()]
for qid, side, link, page, q in rows:
    ck(f"A.{qid}.{side}.{link}", q in pages.get(page, ""), q[:90])
# A: absence across all 8 pages
for w in ["secret", "credential", "ghsa", "package.json"]:
    n = {k[:40]: v.lower().count(w) for k, v in pages.items() if w in v.lower()}
    ck(f"A.absent_all_pages.{w}", not n, n or "0 in 8 pages")
d = pages["defender-endpoint_discover-local-ai-agents.html"]
meta = d[d.find("under localAgentMetadata"): d.find("Note trustedProcess")]
props = re.findall(r"\b(vendor|relatedProcess|trustedProcess|autoApprove|deviceName|aadDeviceId|accountName|accountDomain|accountSid|localMcps)\b", meta)
ck("A.localAgentMetadata_props_no_secret_field", len(set(props)) == 10 and not re.search(r"secret|credential|token|env", meta, re.I), sorted(set(props)))
for p in ["defender-vulnerability-management_tvm-security-recommendation.html", "defender-vulnerability-management_tvm-remediation.html", "defender-xdr_security-for-ai_ai-agent-risk-assessment.html"]:
    ck(f"A.no_target_version_phrase.{p[:38]}", not re.search(r"minimum version|lowest version|version that (fixes|clears)", pages[p], re.I))
# B: ours
rep = json.loads(Path(a.report or C / "evidence/verify-report.json").read_text()); g = rep["gates"]
scan = json.loads((C / "evidence/scan.json").read_text()); readme = (C / "README.md").read_text()
ck("B0.verify_report_ok", rep.get("ok") is True and rep.get("failures") == [], f"ok={rep.get('ok')} failures={rep.get('failures')} gates={len(g)}")
m = g["matrix_exact"]; ck("B1.matrix_exact", m["pass"] and m["correct"] == m["non_colliding"] == 115 and m["total"] == 117, f"{m['correct']}/{m['non_colliding']} non-colliding of {m['total']}")
s = g["stripped"]; ck("B1.stripped_package_json", s["pass"] and s["ok"] == s["total"] == 4, f"{s['ok']}/{s['total']}")
r = g["range_verdicts"]; ck("B1.collision_range", r["pass"] and g["collisions"]["includes_pair"] == ["2026.4.7-1", "2026.4.8"], f"{r['ok']}/{r['total']} pair={g['collisions']['includes_pair']}")
ck("B1.idle_linux_version_recovered", g["idle_linux_version_recovered"]["pass"] is True and g["idle_linux_discovered"]["pass"] is True)
ck("B2.cve_mapping_diff_0", g["cve_mapping"]["pass"] and g["cve_mapping"]["diff_lines"] == 0, g["cve_mapping"]["diff_lines"])
ck("B2.ghsa_only_gate", g["ghsa_only"]["pass"] is True)
ck("B2.repo_only_advisories_in_readme", "760 from the global database and 134 published only on the repository" in readme)
b = g["blast_recall"]; ck("B3.blast_recall_planted", b["pass"] and b["found"] == b["planted"] == 42, f"{b['found']}/{b['planted']} planted (lab only)")
ins = scan["installs"]; ck("B3.credentials_names_only", all(isinstance(c, str) and re.fullmatch(r"[A-Z0-9_]+", c) for i in ins for c in i.get("credentials") or []), f"installs={len(ins)} with_credentials={sum(1 for i in ins if i.get('credentials'))}")
f = g["fix_target"]; ck("B4.min_clearing_version", f["pass"] and f["min_clearing_version"] == "2026.8.1" and f["advisories"] == 148, f"min={f['min_clearing_version']} 2026.4.22={f['advisories']}")
fo = scan["fix_order"]; acts = [x["action"] for x in fo]; k = acts.index("rotate") if "rotate" in acts else len(acts)
cc = [x["credential_count"] for x in fo[:k]]
ck("B4.patch_then_rotate_by_reach", acts[:k] == ["patch"] * k and set(acts[k:]) == {"rotate"} and cc == sorted(cc, reverse=True) and [x["reach"] for x in fo[k:]] == sorted([x["reach"] for x in fo[k:]], reverse=True), f"patch={k} rotate={len(fo)-k}")
# finding (does not fail the gate): a mock-derived count in README
hit = [l for l in readme.splitlines() if "no usable version" in l]
print("FINDING\tREADME mock-derived line (Agent 365 exposes Version; never quote it outside):\t" + (hit[0] if hit else "none"))
V = {"L1_build": "HOLDS-NARROWED: build read from shipped bytes when package.json is stripped or lies, and on idle Linux; Defender DOES show Version (Q1)",
     "L2_advisories": "HOLDS-NARROWED: Linux npm installs (Q9) and repo-only advisories; MDVM maps OpenClaw CVEs (Q2)",
     "L3_reach": "HOLDS-NARROWED: credential NAMES readable by the install (lab-planted only); Microsoft ranks identity reach (Q3)",
     "L4_fix_order": "HOLDS-NARROWED: minimum clearing version + patch-then-rotate by credential reach; Microsoft prioritizes recommendations by impact (Q4, Q5)",
     "chain": "HOLDS (published docs only): no page links build -> advisory list -> readable credential names -> ordered patch/rotate per install"}
for k2, v in V.items(): print(f"VERDICT\t{k2}\t{v}")
print("GATE PASS" if not fails else f"GATE FAIL {fails}"); sys.exit(1 if fails else 0)
