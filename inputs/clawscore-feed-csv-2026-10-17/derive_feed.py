#!/usr/bin/env python3
"""Derive the proposed v0.2.2 pinned feed from the byte-exact pages in raw/ (deterministic; no network).
Output ghsa-all.json = G (global DB, every object unchanged) UNION R-only (repo advisories absent from G),
R-only objects reshaped to G's 23 keys so clawscore_fleet/cves.py reads them unchanged:
  type="repository" (marker: not reviewed in the global DB), github_reviewed_at=None, nvd_published_at=None,
  references=[html_url], repository_advisory_url=url, source_code_location="https://github.com/openclaw/openclaw",
  vulnerabilities[*].first_patched_version = patched_versions when it is one version, '>= VERSION' or 'vVERSION' (repo API field name differs).
Order: published_at desc, then ghsa_id. Prints a report; writes ghsa-all.json, feed-diff.tsv, FEED_NEWEST."""
import json, re, sys
from pathlib import Path
D = Path(__file__).resolve().parent
def pages(tag): return [a for p in sorted((D / "raw").glob(f"{tag}-page*.json")) for a in json.loads(p.read_bytes())]
G, R = pages("G"), pages("R")
KEYS = list(G[0].keys()); gi = {a["ghsa_id"] for a in G}
assert len(gi) == len(G) and len({a["ghsa_id"] for a in R}) == len(R), "duplicate ghsa ids"
multi = []
def reshape(a):
    v = []
    for e in a.get("vulnerabilities") or []:
        pv = (e.get("patched_versions") or "").strip()
        m0 = re.fullmatch(r"(?:>=\s*)?v?(\d+(?:\.\d+)*(?:-[0-9A-Za-z.]+)?)", pv)
        one = m0.group(1) if m0 else None  # "2026.8.1", ">= 2026.4.5" or "v2026.1.29" -> lowest patched version
        if pv and not one: multi.append((a["ghsa_id"], pv))
        v.append({"package": e.get("package"), "vulnerable_version_range": e.get("vulnerable_version_range"),
                  "first_patched_version": one, "vulnerable_functions": e.get("vulnerable_functions") or []})
    m = {"type": "repository", "github_reviewed_at": None, "nvd_published_at": None, "references": [a["html_url"]],
         "repository_advisory_url": a["url"], "source_code_location": "https://github.com/openclaw/openclaw", "vulnerabilities": v}
    return {k: m[k] if k in m else a.get(k) for k in KEYS}
ronly = [reshape(a) for a in R if a["ghsa_id"] not in gi]
feed = sorted(G + ronly, key=lambda a: (a["published_at"], a["ghsa_id"]), reverse=True)
(D / "ghsa-all.json").write_text(json.dumps(feed, indent=2, sort_keys=False) + "\n")
newest = max(a["published_at"] for a in feed)[:10]; (D / "FEED_NEWEST").write_text(newest + "\n")
with open(D / "feed-diff.tsv", "w") as f:
    f.write("ghsa_id\tpublished_at\tseverity\tcve_id\tvulnerable_version_range\tfirst_patched_version\tsummary\n")
    for a in sorted(ronly, key=lambda a: (a["published_at"], a["ghsa_id"]), reverse=True):
        e = (a["vulnerabilities"] or [{}])[0]
        f.write("\t".join(str(x) for x in [a["ghsa_id"], a["published_at"], a["severity"], a["cve_id"], e.get("vulnerable_version_range"), e.get("first_patched_version"), a["summary"].replace("\t", " ")]) + "\n")
old = json.loads(Path(sys.argv[1]).read_text()) if len(sys.argv) > 1 else None
print(f"G={len(G)} R={len(R)} both={len(gi & {a['ghsa_id'] for a in R})} R_only={len(ronly)} feed={len(feed)} FEED_NEWEST={newest}")
print(f"R_only published after 2026-07-02: {sum(1 for a in ronly if a['published_at'] >= '2026-07-03')}")
print(f"GHSA-xx9p-hc9w-6p5h in feed: {any(a['ghsa_id']=='GHSA-xx9p-hc9w-6p5h' for a in feed)}")
print(f"patched_versions not a single version (first_patched_version=None): {len(multi)} {multi[:5]}")
if old is not None:
    om = {a["ghsa_id"]: a for a in old}
    same = sum(1 for a in G if om.get(a["ghsa_id"]) == a)
    print(f"v0.2 pinned file: {len(old)} entries; G objects identical to pinned: {same}/{len(G)}; G ids == pinned ids: {set(om) == gi}")
