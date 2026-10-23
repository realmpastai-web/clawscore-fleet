"""Count openclaw GitHub advisories without a CVE id.
Offline (default): python3 count_nocve.py            -> reads ghsa-all.json snapshot
Live re-query:     python3 count_nocve.py --live      -> GET https://api.github.com/advisories?affects=openclaw&ecosystem=npm&per_page=100 (all pages)"""
import json,sys,re,hashlib,urllib.request
from collections import Counter
if '--live' in sys.argv:
    A=[];url="https://api.github.com/advisories?affects=openclaw&ecosystem=npm&per_page=100"
    while url:
        r=urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'flakecert-verify'}),timeout=60)
        A+=json.load(r); m=re.search(r'<([^>]+)>; rel="next"',r.headers.get('Link') or ''); url=m.group(1) if m else None
    src='LIVE api.github.com'
else:
    raw=open('ghsa-all.json','rb').read(); A=json.loads(raw); src='ghsa-all.json sha256='+hashlib.sha256(raw).hexdigest()
no=[a for a in A if not a.get('cve_id')]
print('source:',src)
print('total_advisories:',len(A))
print('with_cve_id:',len(A)-len(no))
print('without_cve_id:',len(no))
print('without_cve_id_by_severity:',dict(sorted(Counter(a['severity'] for a in no).items())))
print('without_cve_id_critical_or_high:',sum(1 for a in no if a['severity'] in('critical','high')))
print('newest_published:',max(a['published_at'] for a in A))
print('example_ghsa_without_cve:',sorted(a['ghsa_id'] for a in no)[:3])
