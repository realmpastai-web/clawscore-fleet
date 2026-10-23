#!/usr/bin/env python3
"""Hark repro: re-judge every DISAGREE line of evidence/semver-crosscheck.log with
npm semver (tools/semver), commas stripped from the range, includePrerelease=true.
Usage: python3 repro_crosscheck.py <repo_root>"""
import json, re, subprocess, sys, collections
root = sys.argv[1]
lines = open(f"{root}/evidence/semver-crosscheck.log").read().splitlines()
rows = []
for i, l in enumerate(lines):
    if l.startswith("DISAGREE\t"):
        _, v, r, h, n, p = l.split("\t")
        exp = lines[i+1].strip().removeprefix("explanation: ")
        rows.append((v, r, h == "hark=1", exp.split(":")[0], exp.startswith("hark-grammar: a range bound")))
js = """const s=require('semver');let raw='';process.stdin.on('data',c=>raw+=c);process.stdin.on('end',()=>{const p=JSON.parse(raw);
process.stdout.write(JSON.stringify(p.map(([v,r])=>{try{return s.satisfies(v,r,{includePrerelease:true})}catch(e){return null}})))});"""
pairs = [[v, re.sub(r",", " ", r)] for v, r, *_ in rows]
out = subprocess.run(["node", "-e", js], input=json.dumps(pairs), capture_output=True, text=True,
                     cwd=f"{root}/tools/semver", check=True).stdout
npm = json.loads(out)
post = re.compile(r"\d+\.\d+\.\d+-\d+$")
c = collections.Counter(); left = []
for (v, r, h, cat, mis), n in zip(rows, npm):
    c["total"] += 1; c[f"label:{cat}"] += 1; c["mislabeled_grammar"] += mis
    if n == h: c["agree_after_norm"] += 1; c["agree_was_grammar"] += mis; continue
    bounds = re.findall(r"(?:<=|>=|<|>|=)\s*([^\s,]+)", r)
    kind = "post_release" if any(post.match(x) for x in [v, *bounds]) else "parser_diff"
    c[kind] += 1; c[f"leftover_was:{cat}"] += 1; left.append((kind, v, r, h, n))
for k in sorted(c): print(f"{k}\t{c[k]}")
for k, v, r, h, n in left:
    if k == "parser_diff": print("PARSER_DIFF", v, "|", r, "| project", h, "npm", n)
