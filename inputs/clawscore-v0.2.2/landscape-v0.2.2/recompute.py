"""Recompute CLAIMS.md figures from the snapshots (offline). Usage: python3 recompute.py"""
import json,re
from collections import Counter
A=json.load(open('ghsa-all.json'));V=json.load(open('versions.json'))
def key(s):
    # v0.2.2: also -alpha.N / -rc.N and glued -betaN (GHSA bound "2.0.0-beta3"); alpha<beta<rc<release
    m=re.match(r'^(\d+)\.(\d+)\.(\d+)(?:-(\d+))?(?:-(alpha|beta|rc)\.?(\d+))?$',s.strip())
    if not m: return None
    a,b,c,post,tag,n=m.groups(); return (int(a),int(b),int(c),0 if tag else 1,{'alpha':0,'beta':1,'rc':2}.get(tag,0)*1000+int(n or 0),int(post or 0))
def inrange(v,rng):
    kv=key(v)
    for part in rng.split(','):
        m=re.match(r'(<=|>=|<|>|=)\s*(\S+)',part.strip())
        if not m or key(m.group(2)) is None: return False
        op,kt=m.group(1),key(m.group(2))
        if not {'<':kv<kt,'<=':kv<=kt,'>':kv>kt,'>=':kv>=kt,'=':kv==kt}[op]: return False
    return True
def hits(v): return [a for a in A for p in a['vulnerabilities'] if p['package']['name'].lower()=='openclaw' and p.get('vulnerable_version_range') and inrange(v,p['vulnerable_version_range'])]
print('advisories',len(A),dict(Counter(a['severity'] for a in A)),'with CVE',sum(1 for a in A if a.get('cve_id')))
print('published',min(a['published_at'] for a in A)[:10],max(a['published_at'] for a in A)[:10])
stable=[v for v in V if re.match(r'^\d+\.\d+\.\d+(?:-\d+)?$',v) and v!='0.0.1']; print('stable releases',len(stable))
for v in ['2026.1.29','2026.4.20','2026.4.22']:
    h=hits(v); print(v,len(h),dict(Counter(a['severity'] for a in h)))
o=json.load(open('stable-3file.json')); F=['dist/cli.runtime.js','dist/abort.runtime.js']
both=[v for v in stable if all(not o[v][f].startswith('MISS') for f in F)]
from collections import defaultdict; g=defaultdict(list)
for v in both: g[tuple(o[v][f] for f in F)].append(v)
print('dist-pair versions',len(both),'collisions',[x for x in g.values() if len(x)>1])
