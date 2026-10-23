#!/usr/bin/env python3
"""Reference semver cross-check (npm semver 7.8.5, commas->spaces, includePrerelease) vs regen_v023 grammar. Usage: python3 npm_xcheck.py <landscape_dir> <path to semver package dir>"""
import json, re, subprocess, sys
L, SEM = sys.argv[1], sys.argv[2]
src = open(__file__.replace('npm_xcheck.py', 'regen_v023.py')).read().split("R = [")[0].replace('d = sys.argv[1]', 'd = L')
exec(src)
R = sorted({p['vulnerable_version_range'] for a in A for p in a['vulnerabilities'] if p['package']['name'].lower() == 'openclaw' and p.get('vulnerable_version_range')})
pairs = [(v, r) for v in sorted(V) for r in R]
js = "const s=require(process.argv[1]);const P=JSON.parse(require('fs').readFileSync(0));console.log(JSON.stringify([s.SEMVER_SPEC_VERSION&&require(process.argv[1]+'/package.json').version,P.map(([v,r])=>{try{return s.satisfies(v,r.replace(/\\s*,\\s*/g,' '),{includePrerelease:true})}catch(e){return null}})]))"
ver, out = json.loads(subprocess.run(['node', '-e', js, SEM], input=json.dumps(pairs), capture_output=True, text=True, check=True).stdout)
dis = [(v, r) for (v, r), n in zip(pairs, out) if n is None or inrange(v, comparators(r)) != n]
post = [x for x in dis if re.search(r'\d-\d+$', x[0]) or re.search(r'\d-\d+(\s|,|$)', x[1])]
print(f"semver {ver} versions {len(set(v for v,_ in pairs))} ranges {len(R)} decisions {len(pairs)} disagreements {len(dis)} post_release_suffix {len(post)} other {len(dis)-len(post)}")
