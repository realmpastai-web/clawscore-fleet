"""Recompute CLAIMS.md figures from the snapshots (offline). Usage: python3 recompute.py

Writes version-vulns.json from the same counted rows the fleet matcher uses.
Advisories with a non-null withdrawn_at are printed as withdrawn (not counted)
and are omitted from version-vulns.json.
"""
import json,re,sys
from collections import Counter
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from clawscore_fleet.cves import build_index, version_vuln_rows
A=json.load(open('ghsa-all.json'));V=json.load(open('versions.json'))
print('advisories',len(A),dict(Counter(a['severity'] for a in A)),'with CVE',sum(1 for a in A if a.get('cve_id')))
print('published',min(a['published_at'] for a in A)[:10],max(a['published_at'] for a in A)[:10])
stable=[v for v in V if re.match(r'^\d+\.\d+\.\d+(?:-\d+)?$',v) and v!='0.0.1']; print('stable releases',len(stable))
index=build_index()
rows={row[0]: row for row in version_vuln_rows()}
for v in ['2026.1.29','2026.4.20','2026.4.22']:
    row=rows[v]
    print(v,row[2],row[3])
    withdrawn=index['withdrawn_by_version'][v]
    print(v,'withdrawn (not counted)',len(withdrawn),dict(Counter(a['severity'] for a in withdrawn)))
Path('version-vulns.json').write_text(json.dumps(version_vuln_rows(), indent=0)+'\n')
o=json.load(open('stable-3file.json')); F=['dist/cli.runtime.js','dist/abort.runtime.js']
both=[v for v in stable if all(not o[v][f].startswith('MISS') for f in F)]
from collections import defaultdict; g=defaultdict(list)
for v in both: g[tuple(o[v][f] for f in F)].append(v)
print('dist-pair versions',len(both),'collisions',[x for x in g.values() if len(x)>1])
