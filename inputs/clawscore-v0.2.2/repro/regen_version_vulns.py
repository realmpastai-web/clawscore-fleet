#!/usr/bin/env python3
"""Regenerate version-vulns.json from ghsa-all.json + versions.json.
--old: grammar of recompute.py @ 3409516a (must reproduce 30a0e9bf... byte-for-byte)
default: v0.2.2 grammar (adds -alpha.N/-rc.N and glued -betaN; alpha<beta<rc<release)
Usage: python3 regen_version_vulns.py <landscape_dir> [--old] > out.json"""
import json, re, sys
from collections import Counter
d = sys.argv[1]; old = "--old" in sys.argv
A = json.load(open(f"{d}/ghsa-all.json")); V = json.load(open(f"{d}/versions.json"))
def key(s):
    if old:
        m = re.match(r'^(\d+)\.(\d+)\.(\d+)(?:-(\d+))?(?:-beta\.(\d+))?$', s.strip())
        if not m: return None
        a, b, c, post, beta = m.groups(); return (int(a), int(b), int(c), 0 if beta else 1, int(beta or 0), int(post or 0))
    m = re.match(r'^(\d+)\.(\d+)\.(\d+)(?:-(\d+))?(?:-(alpha|beta|rc)\.?(\d+))?$', s.strip())
    if not m: return None
    a, b, c, post, tag, n = m.groups()
    return (int(a), int(b), int(c), 0 if tag else 1, {"alpha": 0, "beta": 1, "rc": 2}.get(tag, 0) * 1000 + int(n or 0), int(post or 0))
def inrange(v, rng):
    kv = key(v)
    for part in rng.split(','):
        m = re.match(r'(<=|>=|<|>|=)\s*(\S+)', part.strip())
        if not m or key(m.group(2)) is None: return False
        op, kt = m.group(1), key(m.group(2))
        if not {'<': kv < kt, '<=': kv <= kt, '>': kv > kt, '>=': kv >= kt, '=': kv == kt}[op]: return False
    return True
def hits(v): return [a for a in A for p in a['vulnerabilities'] if p['package']['name'].lower() == 'openclaw' and p.get('vulnerable_version_range') and inrange(v, p['vulnerable_version_range'])]
okey = key if old else None
def stable_key(s): return re.match(r'^(\d+)\.(\d+)\.(\d+)(?:-(\d+))?$', s.strip())
stable = sorted([v for v in V if stable_key(v) and v != '0.0.1'], key=key)
out = []
for v in stable:
    h = hits(v); c = Counter(a['severity'] for a in h)
    out.append([v, re.search(r'\d{4}-\d\d-\d\d', V[v]).group(0), len(h), {s: c.get(s, 0) for s in ('critical', 'high', 'medium', 'low')}])
sys.stdout.write(json.dumps(out, indent=0))
