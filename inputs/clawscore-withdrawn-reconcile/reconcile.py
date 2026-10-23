#!/usr/bin/env python3
"""Reconcile the openclaw@2026.4.22 advisory count from public GitHub data (offline over sources/).
Range evaluation uses clawscore-fleet's own clawscore_fleet.versions (hark_key, parse_comparators) at main 026f719,
the same evaluator evidence/landscape/recompute.py uses.
Usage (from this folder in a clawscore-fleet checkout): python3 reconcile.py | diff - reconcile-output.txt
Writes counted-2026.4.22.tsv (one row per counted advisory)."""
import json, sys
from collections import Counter
from pathlib import Path
S = Path(__file__).resolve().parent / "sources"
ROOT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from clawscore_fleet.versions import hark_key as key, parse_comparators
VER = "2026.4.22"
import re
NORMALIZED = Counter()
def inrange(v, rng):
    """OR over '||' alternatives; a 'v' before a version digit is dropped (repo advisories write '<=v2026.4.2').
    A bare version ('2026.1.29') is an exact match, as in npm semver.
    Any range clawscore's parser still rejects aborts the run (exit 2) rather than being skipped."""
    kv = key(v)
    for alt in rng.split("||"):
        clean = re.sub(r"(?<![\w.])v(?=\d)", "", alt).strip()
        if clean != alt.strip(): NORMALIZED["v-prefix"] += 1
        if not clean: continue
        if re.fullmatch(r"\d[\w.\-]*", clean): clean = "=" + clean; NORMALIZED["bare-version-as-="] += 1
        try: parts = parse_comparators(clean)
        except Exception as e: print("UNPARSED", repr(rng), e, file=sys.stderr); raise SystemExit(2)
        if all({'<': kv < key(b), '<=': kv <= key(b), '>': kv > key(b), '>=': kv >= key(b), '=': kv == key(b)}[op] for op, b in parts): return True
    return False
def rows(advs):
    out = []
    for a in advs:
        for p in a.get("vulnerabilities") or []:
            pk = p.get("package") or {}
            if (pk.get("ecosystem") or "npm").lower() == "npm" and (pk.get("name") or "").lower() == "openclaw" and p.get("vulnerable_version_range") and inrange(VER, p["vulnerable_version_range"]):
                out.append(a)
    return out
J = lambda f: json.loads((S / f).read_text())
G, R, A = J("gh-global-openclaw-all.json"), J("gh-repo-openclaw-published.json"), J("gh-global-affects-openclaw@2026.4.22.json")
F = json.loads((Path(sys.argv[2]) if len(sys.argv) > 2 else ROOT / "evidence/landscape/ghsa-all.json").read_text())
def report(name, advs):
    r = rows(advs); ids = [a["ghsa_id"] for a in r]; c = Counter(ids); u = {a["ghsa_id"]: a for a in r}
    wd = sorted(i for i, a in u.items() if a.get("withdrawn_at"))
    print(f"{name}: match_rows={len(r)} unique={len(u)} duplicate_rows={sum(n-1 for n in c.values())} withdrawn={len(wd)} counted={len(u)-len(wd)}")
    return u, wd
print("pulled_at", (S / "PULLED_AT.txt").read_text().strip(), "| sources: global", len(G), "repo", len(R), "affects", len(A))
gu, gw = report("GLOBAL_DB (ours)", G)
ru, rw = report("REPO_PUBLISHED (ours)", R)
print("range_normalizations (global+repo, first pass)", dict(NORMALIZED))
au = {a["ghsa_id"]: a for a in A}; aw = sorted(i for i, a in au.items() if a.get("withdrawn_at"))
print(f"GLOBAL_DB (GitHub affects=openclaw@{VER}): unique={len(au)} withdrawn={len(aw)} counted={len(au)-len(aw)}")
if F is not None: fu, fw = report("FROZEN ghsa-all.json (README 181)", F)
print("ours_vs_github_affects: only_ours", sorted(set(gu) - set(au)), "only_github", sorted(set(au) - set(gu)))
gc = set(gu) - set(gw); rc = set(ru)
print(f"counted global (non-withdrawn)={len(gc)} | repo={len(rc)} | both={len(gc & rc)} | global_only={len(gc - rc)} | repo_only={len(rc - gc)} | UNION_COUNTED={len(gc | rc)}")
print("withdrawn_also_in_repo_published", sorted(set(gw) & rc))
# alias check: CVE ids shared by more than one counted GHSA
allu = {**ru, **{i: gu[i] for i in gc}}  # severity: GitHub-reviewed global record where one exists, else the repo advisory
cve = Counter(a.get("cve_id") for a in allu.values() if a.get("cve_id"))
print("cve_shared_by_>1_counted_ghsa", sorted(k for k, n in cve.items() if n > 1))
sev = Counter(a["severity"] for a in allu.values()); print("UNION severity (global record preferred)", dict(sorted(sev.items())))
sev_diff = sorted((i, ru[i]["severity"], gu[i]["severity"]) for i in gc & rc if ru[i]["severity"] != gu[i]["severity"])
print("severity_differs_repo_vs_global", len(sev_diff), sev_diff)
if F is not None:
    fc = set(fu) - set(fw); print("FROZEN_counted == UNION_COUNTED:", fc == (gc | rc), "| frozen_only", sorted(fc - (gc | rc)), "| fresh_only", sorted((gc | rc) - fc))
dup = [i for i, n in Counter(a["ghsa_id"] for a in rows(R)).items() if n > 1]
for i in dup: print("repo advisory with >1 matching openclaw range (counted once):", i, [p.get("vulnerable_version_range") for p in ru[i]["vulnerabilities"]])
# the two global-only rows: how the repo advisory names the package
for i in sorted(gc - rc):
    rr = {a["ghsa_id"]: a for a in R}.get(i)
    print("GLOBAL_ONLY", i, "repo_published:", bool(rr), "repo_packages:", [((p.get("package") or {}).get("name"), p.get("vulnerable_version_range")) for p in (rr or {}).get("vulnerabilities", [])], "global_packages:", [(p["package"]["name"], p["vulnerable_version_range"]) for p in gu[i]["vulnerabilities"]])
# withdrawn duplicates -> original by title
norm = lambda t: re.sub(r"^(duplicate advisory:\s*)?(openclaw:\s*|openclaw's\s*)?", "", t.strip().lower())
title = {}
for i, a in allu.items(): title.setdefault(norm(a["summary"]), []).append(i)
print("\nWITHDRAWN -> ORIGINAL (title match after dropping 'Duplicate Advisory:' / 'OpenClaw:')")
unmatched = 0
for i in gw:
    o = title.get(norm(gu[i]["summary"]), [])
    unmatched += not o; print(f"{i}\t-> {','.join(o) or 'NO TITLE MATCH'}\t{'counted' if o else ''}")
print("withdrawn_with_counted_original", len(gw) - unmatched, "no_title_match", unmatched)
print("\nWITHDRAWN (global DB, range covers 2026.4.22):")
for i in gw:
    a = gu[i]; print(f"{i}\twithdrawn_at={a['withdrawn_at'][:10]}\tseverity={a['severity']}\tcve={a.get('cve_id') or '-'}\tin_repo_published={'yes' if i in rc else 'no'}\t{a['summary'][:90]}")
print("\nREPO_ONLY counted (absent from global DB as non-withdrawn):", len(rc - gc))
print("GLOBAL_ONLY counted (repo advisory exists but its package row is not npm openclaw):")
for i in sorted(gc - rc): print(f"{i}\t{gu[i]['severity']}\t{gu[i].get('repository_advisory_url') or '-'}\t{gu[i]['summary'][:80]}")

with open(Path(__file__).resolve().parent / "counted-2026.4.22.tsv", "w") as fh:
    fh.write("ghsa_id\tseverity\tin_global_db\tin_repo_published\tcve_id\tsummary\n")
    for i in sorted(gc | rc):
        a = allu[i]; fh.write(f"{i}\t{a['severity']}\t{'yes' if i in gc else 'no'}\t{'yes' if i in rc else 'no'}\t{a.get('cve_id') or '-'}\t{a['summary']}\n")
