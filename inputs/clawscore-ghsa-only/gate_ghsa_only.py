#!/usr/bin/env python3
"""clawscore-ghsa-only gate (Hark, frozen 2026-10-18). Stdlib only, offline.

  python3 gate_ghsa_only.py                 # self-checks + negative control (baseline from main bdd8c9b must FAIL)
  python3 gate_ghsa_only.py --report R.json # judge a ClawScore Fleet ghsa-only report (Cursor acceptance)

Ground truth = pinned OSV snapshot (2026-10-18) of npm/openclaw: the 59 advisories with no CVE alias.
Status per fixture version: affected = GitHub vulnerable_version_range (landscape @bdd8c9b) includes it;
possibly_affected = OSV (introduced..fixed) includes it but the GitHub range stops at last_known_affected."""
import argparse, hashlib, json, re, sys
from pathlib import Path
H = Path(__file__).resolve().parent; S = H / "sources"; fails = []
def chk(t, ok, m): print(("PASS" if ok else "FAIL") + "\t" + t + "\t" + m); ok or fails.append(t)
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()

def key(v):
    m = re.fullmatch(r"(\d+)\.(\d+)\.(\d+)(?:-(.+))?", v)
    if not m: raise SystemExit(f"unparseable version {v}")
    return (int(m[1]), int(m[2]), int(m[3])), m[4]
def cmp(a, b):
    (ta, sa), (tb, sb) = key(a), key(b)
    if ta != tb: return -1 if ta < tb else 1
    if sa == sb: return 0
    raise SystemExit(f"suffix tie {a} vs {b}: not decidable without a convention; fixtures avoid it")
def osv_affected(adv, v):
    for a in adv["affected"]:
        if a["package"]["name"] != "openclaw": continue
        for r in a["ranges"]:
            lo = None
            for e in r["events"]:
                if "introduced" in e: lo = e["introduced"]; continue
                end, inclusive = (e["fixed"], False) if "fixed" in e else (e["last_affected"], True)
                if lo is not None and (lo == "0" or cmp(v, lo) >= 0) and (cmp(v, end) <= 0 if inclusive else cmp(v, end) < 0): return True
                lo = None
            if lo is not None and (lo == "0" or cmp(v, lo) >= 0): return True
    return False
def gh_in_range(rng, v):
    for part in rng.split(","):
        op, b = re.fullmatch(r"\s*(<=|>=|<|>|=)\s*(\S+)\s*", part).groups(); c = cmp(v, b)
        if not {"<": c < 0, "<=": c <= 0, ">": c > 0, ">=": c >= 0, "=": c == 0}[op]: return False
    return True

snap = json.loads((H / "OSV_SNAPSHOT.json").read_text())
osv_path = S / "osv" / "osv-query-openclaw-npm.json"
chk("snapshot.sha256", sha(osv_path) == snap["sha256"], f"OSV snapshot {snap['fetched']} sha256 {snap['sha256'][:16]}…")
osv = {a["id"]: a for a in json.loads(osv_path.read_text())}
nocve = sorted(i for i, a in osv.items() if not any(x.startswith("CVE-") for x in a.get("aliases", [])))
exp = json.loads((H / "expected-ghsa-only.json").read_text())
chk("expected.59", len(nocve) == 59 and nocve == exp["ghsa_only_ids"], f"{len(nocve)} OSV advisories without a CVE alias = expected-ghsa-only.json")
land = {a["ghsa_id"]: a for a in json.loads((S / "landscape-ghsa-all-bdd8c9b.json").read_text())}
chk("landscape.has_all", all(i in land and not land[i].get("cve_id") and not land[i].get("withdrawn_at") for i in nocve),
    "all 59 are in the fleet's landscape feed @bdd8c9b, live, with cve_id null")
def expected_for(v):
    out = {}
    for i in nocve:
        if not osv_affected(osv[i], v): continue
        rngs = [x["vulnerable_version_range"] for x in land[i]["vulnerabilities"] if (x.get("package") or {}).get("name") == "openclaw"]
        out[i] = "affected" if any(gh_in_range(r, v) for r in rngs) else "possibly_affected"
    return out
calc = {h["version"]: expected_for(h["version"]) for h in exp["fixture_hosts"]}
chk("expected.recomputed", all(calc[h["version"]] == h["expected"] for h in exp["fixture_hosts"]), "per-host expected sets recompute from OSV + landscape")
cover = set().union(*[set(c) for c in calc.values()])
chk("expected.cover_all", cover == set(nocve), f"fixture versions {[h['version'] for h in exp['fixture_hosts']]} cover all {len(cover)} ids")
pa = sorted({(v, i) for v, c in calc.items() for i, s in c.items() if s == "possibly_affected"})
chk("expected.gap_window", pa == [("2026.4.7", "GHSA-gfmx-pph7-g46x"), ("2026.4.7", "GHSA-jf56-mccx-5f3f")], f"possibly_affected cases: {pa}")
for i in ["GHSA-gfmx-pph7-g46x", "GHSA-jf56-mccx-5f3f"]:
    d = json.loads((S / "advisory-database" / f"{i}.json").read_text())
    a = d["affected"][0]
    chk(f"source.{i}", a["ranges"][0]["events"] == [{"introduced": "0"}, {"fixed": "2026.4.8"}] and a["database_specific"]["last_known_affected_version_range"] == "<= 2026.4.2",
        "github/advisory-database: fixed 2026.4.8 but last_known_affected <= 2026.4.2 (the GitHub API range shows only the latter)")

# Wazuh: does it drop GHSA-only advisories? (settled from shipped v4.14.9 source + CTI)
W = S / "wazuh-v4.14.9"
cand = (W / "vulnerabilityCandidate.fbs").read_text(); cve5 = (W / "cve5.fbs").read_text()
chk("wazuh.candidate_keyed_cveId", "cveId: string;" in cand, "vulnerabilityCandidate.fbs: a detection candidate carries cveId")
chk("wazuh.feed_is_cve5", "cveId: string;" in cve5 and "table CVSS_V3_1" in cve5, "cve5.fbs: the feed is CVE JSON 5 records")
enum = [f for f in ["eventPackageAlertDetailsBuilder.hpp", "eventDetailsBuilder.hpp"] if '["enumeration"] = "CVE";' in (W / f).read_text()]
chk("wazuh.enumeration_CVE", len(enum) == 2, f'alert builders hard-code vulnerability.enumeration = "CVE": {enum}')
st = dict(l.split()[:2] for l in (S / "cti" / "cti-status.txt").read_text().splitlines())
chk("wazuh.cti", st["CVE-2026-32064"] == "200" and st["GHSA-p73f-w79w-jqr5"] == "404" and st["GHSA-2858-xg23-26fp"] == "404" and st["CVE-2099-9999999"] == "404",
    "CTI serves OpenClaw CVEs; GHSA-only ids 404 like a nonexistent CVE")
print("VERDICT wazuh: PROVEN at schema level for 4.14.9 - its feed is CVE5 records keyed by cveId and every package alert says enumeration=CVE, so a no-CVE GHSA advisory has no record to match. Residual (not testable from public artifacts): CTI's private build pipeline; Wazuh 5.x/main not covered.")

def judge(rep, tag):
    bad = []
    if rep.get("osv_snapshot_sha256") != snap["sha256"]: bad.append("osv_snapshot_sha256")
    hosts = {h.get("version"): h for h in rep.get("hosts", [])}
    for h in exp["fixture_hosts"]:
        r = hosts.get(h["version"])
        if r is None: bad.append(f"{h['version']}:host_missing"); continue
        got = {x["id"]: x["status"] for x in r.get("ghsa_only", [])}
        miss = sorted(set(h["expected"]) - set(got)); extra = sorted(set(got) - set(h["expected"]))
        wrong = sorted(i for i in set(got) & set(h["expected"]) if got[i] != h["expected"][i])
        cvebad = sorted(i for i in got if i in set(r.get("cves", [])))
        notlisted = sorted(i for i, s in got.items() if s == "affected" and i not in set(r.get("ghsa_ids", [])))
        for k, v in [("missing", miss), ("extra", extra), ("wrong_status", wrong), ("in_cves", cvebad), ("affected_not_in_ghsa_ids", notlisted)]:
            if v: bad.append(f"{h['version']}:{k}={v[:3]}{'…' if len(v) > 3 else ''}({len(v)})")
    seen = {x["id"] for r in rep.get("hosts", []) for x in r.get("ghsa_only", [])}
    if seen != set(nocve): bad.append(f"union={len(seen & set(nocve))}/59")
    return bad

ap = argparse.ArgumentParser(); ap.add_argument("--report"); a = ap.parse_args()
if a.report:
    bad = judge(json.loads(Path(a.report).read_text()), "report")
    chk("report.ghsa_only", not bad, "fleet report lists every expected no-CVE id per fixture host with the right status" if not bad else "; ".join(bad))
else:
    base = json.loads((H / "baseline-main-bdd8c9b.json").read_text())
    bad = judge(base, "baseline")
    print("BASELINE main@bdd8c9b: " + "; ".join(bad))
    chk("negative_control.baseline_fails", bool(bad) and any("ghsa_only" in b or "missing" in b for b in bad),
        "the gate rejects today's fleet output (no ghsa_only field; 2026.4.7 ghsa_ids omit the 2 gap-window ids)")
    b47 = {h["version"]: h for h in base["hosts"]}["2026.4.7"]
    chk("negative_control.real_miss", not {"GHSA-gfmx-pph7-g46x", "GHSA-jf56-mccx-5f3f"} & set(b47["ghsa_ids"]),
        "main@bdd8c9b report_for_versions(['2026.4.7']) omits GHSA-gfmx-pph7-g46x and GHSA-jf56-mccx-5f3f (OSV: affected until 2026.4.8)")
print("GATE " + ("PASS" if not fails else "FAIL " + str(sorted(set(fails)))))
sys.exit(1 if fails else 0)
