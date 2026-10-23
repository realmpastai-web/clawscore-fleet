#!/usr/bin/env python3
"""v0.2.3 reference: version-vulns.json from <landscape_dir>/ghsa-all.json + versions.json.
Grammar = v0.2.2 key(). Range = AND of comparators separated by commas and/or whitespace (npm semantics),
each comparator (<=|>=|<|>|=) then optional spaces then a bound. The whole string must be consumed; else the range is UNPARSED (exit 2).
Usage: python3 regen_v023.py <landscape_dir> [--stats]"""
import json, re, sys
from collections import Counter
d = sys.argv[1]
A = json.load(open(f"{d}/ghsa-all.json")); V = json.load(open(f"{d}/versions.json"))
def key(s):
    m = re.match(r'^(\d+)\.(\d+)\.(\d+)(?:-(\d+))?(?:-(alpha|beta|rc)\.?(\d+))?$', s.strip())
    if not m: return None
    a, b, c, post, tag, n = m.groups()
    return (int(a), int(b), int(c), 0 if tag else 1, {"alpha": 0, "beta": 1, "rc": 2}.get(tag, 0) * 1000 + int(n or 0), int(post or 0))
CMP = re.compile(r'\s*(<=|>=|<|>|=)\s*([^\s,]+)\s*,?')
def comparators(rng):
    out, pos = [], 0
    while pos < len(rng):
        m = CMP.match(rng, pos)
        if not m or m.end() == pos: return None
        out.append((m.group(1), m.group(2))); pos = m.end()
    return out if out and all(key(b) is not None for _, b in out) else None
def inrange(v, cs):
    kv = key(v)
    return all({'<': kv < kt, '<=': kv <= kt, '>': kv > kt, '>=': kv >= kt, '=': kv == kt}[op] for op, kt in ((o, key(b)) for o, b in cs))
R = [(a, p['vulnerable_version_range']) for a in A for p in a['vulnerabilities'] if p['package']['name'].lower() == 'openclaw' and p.get('vulnerable_version_range')]
P = [(a, r, comparators(r)) for a, r in R]
bad = [r for _, r, c in P if c is None]
if bad: print("UNPARSED", bad, file=sys.stderr); sys.exit(2)
stable = sorted([v for v in V if re.match(r'^\d+\.\d+\.\d+(?:-\d+)?$', v.strip()) and v != '0.0.1'], key=key)
def hits(v): return [a for a, r, c in P if inrange(v, c)]
out = []
for v in stable:
    h = hits(v); c = Counter(a['severity'] for a in h)
    out.append([v, re.search(r'\d{4}-\d\d-\d\d', V[v]).group(0), len(h), {s: c.get(s, 0) for s in ('critical', 'high', 'medium', 'low')}])
if "--stats" in sys.argv:
    ch = lambda r: r[3]['critical'] + r[3]['high']
    clr = next((out[i][0] for i in range(len(out)) if all(ch(x) == 0 for x in out[i:])), None)
    d2 = {r[0]: r for r in out}
    print(json.dumps({"advisories": len(A), "advisories_with_openclaw_range": len(R), "unique_ranges": len({r for _, r in R}),
        "comparators": sum(len(c) for _, _, c in P), "space_and_ranges": sorted({r for _, r, c in P if len(c) > 1 and ',' not in r}),
        "stable": len(out), "min_clearing_version": clr, "2026.1.29": d2["2026.1.29"], "2026.4.22": d2["2026.4.22"]}, indent=1))
else:
    sys.stdout.write(json.dumps(out, indent=0))
