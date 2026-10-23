"""Hark independent oracle (not ClawScore code). Advisory set per openclaw npm version from pinned ghsa-all.json.
Rule (agreed 2026-10-20, pkg-match): package name casefold == openclaw AND ecosystem npm, plus keep-list GHSA-25gx-x37c-7pph; withdrawn_at rows excluded.
Order: X-alpha.N < X-beta.N < X-rc.N < X < X-N (OpenClaw -N = post-release; documented convention of the repo's version order)."""
import json,re,sys
KEEP={'GHSA-25gx-x37c-7pph'}
V=re.compile(r'^v?(\d+)\.(\d+)\.(\d+)(?:-(?:(\d+)|(alpha|beta|rc)\.?(\d+)?))?$')
RANK={'alpha':0,'beta':1,'rc':2}
def key(v):
    m=V.match(v.strip())
    if not m: raise ValueError('bad version '+v)
    a,b,c,post,tag,n=m.groups()
    return (int(a),int(b),int(c),0 if tag else 1,(RANK[tag]*1000+int(n or 0)) if tag else 0,int(post or 0))
TOK=re.compile(r'\s*(>=|<=|>|<|=)?\s*(v?\d+\.\d+\.\d+(?:-[0-9A-Za-z.]+)?)\s*,?')
def inr(r,v):
    k=key(v); pos=0; ok=True; n=0
    while pos<len(r):
        m=TOK.match(r,pos)
        if not m or m.end()==pos: raise ValueError('bad range '+r)
        op=m.group(1) or '='; x=key(m.group(2)); n+=1
        ok&={'>=':k>=x,'<=':k<=x,'>':k>x,'<':k<x,'=':k==x}[op]; pos=m.end()
    if n==0: raise ValueError('empty range')
    return ok
def applies(adv,v):
    if adv.get('withdrawn_at'): return False
    for e in adv.get('vulnerabilities') or []:
        p=e.get('package') or {}
        if str(p.get('name') or '').casefold()!='openclaw': continue
        if str(p.get('ecosystem') or '').casefold()!='npm' and adv['ghsa_id'] not in KEEP: continue
        r=e.get('vulnerable_version_range')
        if r and inr(r,v): return True
    return False
def advisories(feed,v):
    return sorted((a['ghsa_id'],a.get('severity')) for a in feed if applies(a,v))
if __name__=='__main__':
    feed=json.load(open(sys.argv[1])); 
    for v in sys.argv[2:]:
        s=advisories(feed,v); print(v,len(s),sum(1 for _,x in s if x=='critical'),sum(1 for _,x in s if x=='high'))
