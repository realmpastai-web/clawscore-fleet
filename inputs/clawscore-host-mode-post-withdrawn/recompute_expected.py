#!/usr/bin/env python3
"""Post-withdrawn host-mode expectations (Hark, 2026-10-18).
Recomputes the per-version advisory sets the host-mode gate pins (inputs/clawscore-host-mode/
expected-advisories-026f719.json) from evidence/landscape/ghsa-all.json (27b020df) with the evaluator
frozen in inputs/clawscore-withdrawn-gate/gate_withdrawn.py (verbatim 026f719 grammar), report_for_versions
semantics (ghsa_ids sorted, cves = sorted unique cve_id, vulnerable = critical+high > 0), family carried over.
  python3 recompute_expected.py [--repo .]  -> prints the recompute, writes expected-advisories-post-withdrawn.json
Control: with withdrawn INCLUDED the result must equal expected-advisories-026f719.json exactly, else exit 1.
"""
import argparse, hashlib, importlib.util, json, sys
from collections import Counter
from pathlib import Path
H = Path(__file__).resolve().parent
ap = argparse.ArgumentParser(); ap.add_argument("--repo", default=str(H.parents[1])); a = ap.parse_args()
repo = Path(a.repo).resolve()
spec = importlib.util.spec_from_file_location("gw", repo / "inputs/clawscore-withdrawn-gate/gate_withdrawn.py")
gw = importlib.util.module_from_spec(spec); spec.loader.exec_module(gw)
ga = repo / "evidence/landscape/ghsa-all.json"; vj = repo / "evidence/landscape/versions.json"
old_p = repo / "inputs/clawscore-host-mode/expected-advisories-026f719.json"
for p, want in ((ga, gw.PINS["evidence/landscape/ghsa-all.json"]), (vj, gw.PINS["evidence/landscape/versions.json"])):
    got = gw.sha(p); print(f"pin {p.relative_to(repo)} {got} {'OK' if got == want else 'MISMATCH'}")
    if got != want: sys.exit(2)
adv = json.loads(ga.read_text()); pub = {str(k): str(v) for k, v in json.loads(vj.read_text()).items()}
old = json.loads(old_p.read_text())
print(f"old expected {old_p.relative_to(repo)} sha256 {gw.sha(old_p)} source {old['source']}")
def entry(per, v, fam):
    rows = sorted(per[v], key=lambda x: x["ghsa_id"]); c = Counter(x.get("severity") for x in rows)
    return {"advisory_count": len(rows), "cves": sorted({x["cve_id"] for x in rows if x.get("cve_id")}), "family": fam,
            "ghsa_ids": [x["ghsa_id"] for x in rows], "vulnerable": c["critical"] + c["high"] > 0}, c
_, per_w = gw.recompute(adv, pub, True); _, per_x = gw.recompute(adv, pub, False)
withdrawn = {x["ghsa_id"] for x in adv if x.get("withdrawn_at")}
ok = True; new = {}
print("version     host     with_withdrawn(cves)  ==026f719  excluded  withdrawn_dropped  post(cves)  crit/high/med/low  vulnerable")
hosts = {"2026.10.4": "H1", "2026.4.15": "H2", "2026.1.29": "H3,H5"}
for v in sorted(old["by_version"], key=gw.hark_key):
    fam = old["by_version"][v]["family"]
    ew, _ = entry(per_w, v, fam); ex, c = entry(per_x, v, fam)
    same = ew == old["by_version"][v]; ok &= same
    dropped = set(ew["ghsa_ids"]) - set(ex["ghsa_ids"])
    ok &= dropped <= withdrawn and not (set(ex["ghsa_ids"]) & withdrawn)
    new[v] = ex
    print(f"{v:11} {hosts[v]:8} {ew['advisory_count']:4} ({len(ew['cves']):3})            {same!s:9}  {ex['advisory_count']:4}      {len(dropped):3}                {ex['advisory_count']:4} ({len(ex['cves']):3})  "
          f"{c['critical']}/{c['high']}/{c['medium']}/{c['low']}         {ex['vulnerable']}")
out = {"source": "recompute from evidence/landscape/ghsa-all.json with withdrawn_at advisories excluded (Hark recompute_expected.py)",
       "ghsa_all_sha256": gw.PINS["evidence/landscape/ghsa-all.json"], "versions_sha256": gw.PINS["evidence/landscape/versions.json"],
       "replaces": f"expected-advisories-026f719.json sha256 {gw.sha(old_p)}", "by_version": new}
text = json.dumps(out, indent=2, sort_keys=True) + "\n"
(H / "expected-advisories-post-withdrawn.json").write_text(text)
print(f"wrote expected-advisories-post-withdrawn.json sha256 {hashlib.sha256(text.encode()).hexdigest()}")
print("CONTROL " + ("OK (with-withdrawn recompute == 026f719 expected; only withdrawn ids dropped)" if ok else "BROKEN"))
sys.exit(0 if ok else 1)
