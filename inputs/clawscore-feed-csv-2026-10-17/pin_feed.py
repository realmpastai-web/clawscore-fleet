#!/usr/bin/env python3
"""Fetch the two OpenClaw advisory sources page by page and store the page bodies byte-exact (Hark, 2026-10-17).
G = GitHub global advisory DB  (source of the v0.2 pinned evidence/landscape/ghsa-all.json)
R = openclaw/openclaw repository security advisories (source feed_check.py compares against)"""
import json, re, urllib.request, hashlib, datetime, sys
from pathlib import Path
OUT = Path(__file__).resolve().parent / "raw"; OUT.mkdir(exist_ok=True)
H = {"Accept": "application/vnd.github+json", "User-Agent": "clawscore-fleet-v022-pin", "X-GitHub-Api-Version": "2022-11-28"}
SRC = {"G": "https://api.github.com/advisories?ecosystem=npm&affects=openclaw&per_page=100",
       "R": "https://api.github.com/repos/openclaw/openclaw/security-advisories?state=published&per_page=100&sort=published&direction=desc"}
log = [f"pinned_at_utc\t{datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}"]
for tag, url in SRC.items():
    n = 0
    while url:
        r = urllib.request.urlopen(urllib.request.Request(url, headers=H), timeout=60); body = r.read(); n += 1
        p = OUT / f"{tag}-page{n:02d}.json"; p.write_bytes(body)
        log.append(f"{tag}\t{n}\t{r.status}\t{len(json.loads(body))}\t{hashlib.sha256(body).hexdigest()}\t{url}")
        m = re.search(r'<([^>]+)>; rel="next"', r.headers.get("Link") or ""); url = m.group(1) if m else None
(OUT / "pin.log").write_text("\n".join(log) + "\n"); print("\n".join(log))
