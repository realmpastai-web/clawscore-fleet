#!/usr/bin/env python3
"""Hark repro of v0.2.2 expected state over ALL decisions (versions x ranges), using
the project's own in_range, with (a) commas stripped for npm, includePrerelease=true,
and (b) optionally a reference hark_key that accepts -alpha.N/-rc.N (alpha<beta<rc<release).
Usage: python3 repro_full.py <repo_root> [--fixed-key]"""
import json, re, subprocess, sys, collections
root = sys.argv[1]; fixed = "--fixed-key" in sys.argv
sys.path.insert(0, root)
import clawscore_fleet.versions as V
if fixed:
    RX = re.compile(r"^(\d+)\.(\d+)\.(\d+)(?:-(\d+))?(?:-(alpha|beta|rc)\.?(\d+))?$" if "--glued" in sys.argv else r"^(\d+)\.(\d+)\.(\d+)(?:-(\d+))?(?:-(alpha|beta|rc)\.(\d+))?$")
    RANK = {"alpha": 0, "beta": 1, "rc": 2}
    def hark_key(v):
        m = RX.match(v.strip())
        if not m: return None
        a, b, c, post, tag, n = m.groups()
        return (int(a), int(b), int(c), 0 if tag else 1, RANK.get(tag, 0) * 1000 + int(n or 0), int(post or 0))
    V.hark_key = hark_key
import clawscore_fleet.cves as C
if fixed: C.hark_key = V.hark_key
from clawscore_fleet.semver_check import _catalog_versions, _ranges
from clawscore_fleet.cves import in_range
vs, rs = _catalog_versions(), _ranges()
pairs = [(v, r) for v in vs for r in rs]
hk = [in_range(v, r) for v, r in pairs]
js = """const s=require('semver');let raw='';process.stdin.on('data',c=>raw+=c);process.stdin.on('end',()=>{const p=JSON.parse(raw);
process.stdout.write(JSON.stringify(p.map(([v,r])=>{try{return [s.satisfies(v,r),s.satisfies(v,r.replace(/,/g,' '),{includePrerelease:true})]}catch(e){return [null,null]}})))});"""
out = json.loads(subprocess.run(["node", "-e", js], input=json.dumps(pairs), capture_output=True, text=True, cwd=f"{root}/tools/semver", check=True).stdout)
post = re.compile(r"\d+\.\d+\.\d+-\d+$")
c = collections.Counter()
for (v, r), h, (d, p) in zip(pairs, hk, out):
    c["decisions"] += 1
    c["disagree_default_raw"] += (d != h)
    if p != h:
        b = re.findall(r"(?:<=|>=|<|>|=)\s*([^\s,]+)", r)
        k = "post_release" if any(post.match(x) for x in [v, *b]) else "other"
        c["disagree_norm_pre:" + k] += 1
        if k == "other": print("OTHER", v, "|", r, "| hark", h, "npm", p)
print("fixed_key", fixed, "glued", "--glued" in sys.argv, "versions", len(vs), "ranges", len(rs))
for k in sorted(c): print(f"{k}\t{c[k]}")
