#!/usr/bin/env python3
"""npm audit gap probe (Hark, REA brief npm-audit-gap). Static: never installs or runs openclaw.

Usage: python3 probe.py --repo <clawscore-fleet checkout> --out <dir> [--versions 2026.4.22 2026.6.10]
  --offline <dir>  re-score saved raw responses instead of calling the registry.

Live mode POSTs the same endpoint npm audit uses (npm 12.2.0, @npmcli/arborist/lib/audit-report.js):
  POST https://registry.npmjs.org/-/npm/v1/security/advisories/bulk
  body {"openclaw": ["<version>"]}
It saves the request body, raw response bytes, HTTP status, the server Date header and the UTC fetch time, each with its sha256.

ClawScore side: Hark oracle.py (sha256 82e0033a...) over evidence/landscape/ghsa-all.json (feed newest 2026-09-11).
Split of ClawScore's set S for a version (each part disjoint, sum == |S|):
  overlap   = S & npm_audit
  db_not_npm = S & global_db - npm_audit            (in the GitHub global DB pinned file, not returned by npm audit)
  repo_only = S - global_db                         (published only on the openclaw repository)
  npm_only  = npm_audit - S                         (reported, expected 0)
"""
import argparse, datetime, hashlib, json, os, re, sys, urllib.request

ENDPOINT = "https://registry.npmjs.org/-/npm/v1/security/advisories/bulk"
GHSA = re.compile(r"GHSA-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}")


def sha(b):
    return hashlib.sha256(b).hexdigest()


def fetch(version, raw):
    body = json.dumps({"openclaw": [version]}, separators=(",", ":")).encode()
    req = urllib.request.Request(ENDPOINT, data=body, method="POST", headers={"content-type": "application/json", "user-agent": "clawscore-npm-audit-probe/1"})
    t = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")
    with urllib.request.urlopen(req, timeout=60) as r:
        data, status, date = r.read(), r.status, r.headers.get("Date")
    open(os.path.join(raw, f"req-{version}.json"), "wb").write(body)
    open(os.path.join(raw, f"resp-{version}.json"), "wb").write(data)
    meta = {"version": version, "endpoint": ENDPOINT, "method": "POST", "fetched_utc": t, "server_date": date, "status": status,
            "request_sha256": sha(body), "response_sha256": sha(data), "response_bytes": len(data)}
    json.dump(meta, open(os.path.join(raw, f"meta-{version}.json"), "w"), indent=1, sort_keys=True)
    return data, meta


def npm_ids(data):
    rows = json.loads(data).get("openclaw", [])
    ids = set()
    for r in rows:
        m = GHSA.search(str(r.get("url", "")))
        if not m:
            raise SystemExit(f"row without GHSA url: {r.get('id')}")
        ids.add(m.group(0))
    return ids, len(rows)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--offline")
    ap.add_argument("--versions", nargs="+", default=["2026.4.22", "2026.6.10"])
    a = ap.parse_args()
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import oracle
    feed_p = os.path.join(a.repo, "evidence/landscape/ghsa-all.json")
    glob_p = os.path.join(a.repo, "inputs/rea-brief-openclaw-latest/gh-global-openclaw.json")
    feed = json.load(open(feed_p))
    global_db = {r["ghsa_id"] for r in json.load(open(glob_p))}
    raw = a.offline or os.path.join(a.out, "raw")
    os.makedirs(raw, exist_ok=True)
    os.makedirs(a.out, exist_ok=True)
    result = {"oracle_sha256": sha(open(oracle.__file__, "rb").read()), "feed_sha256": sha(open(feed_p, "rb").read()),
              "global_db_sha256": sha(open(glob_p, "rb").read()), "feed_newest": "2026-09-11", "versions": []}
    for v in a.versions:
        if a.offline:
            data = open(os.path.join(raw, f"resp-{v}.json"), "rb").read()
            meta = json.load(open(os.path.join(raw, f"meta-{v}.json")))
            if sha(data) != meta["response_sha256"]:
                raise SystemExit(f"raw response for {v} does not match its recorded sha256")
        else:
            data, meta = fetch(v, raw)
        npm, nrows = npm_ids(data)
        S = {g for g, _ in oracle.advisories(feed, v)}
        overlap, db_not_npm, repo_only, npm_only = S & npm, (S & global_db) - npm, S - global_db, npm - S
        assert len(overlap) + len(db_not_npm) + len(repo_only) == len(S)
        row = {"version": v, "npm_audit_date_utc": meta["fetched_utc"], "server_date": meta["server_date"], "response_sha256": meta["response_sha256"],
               "npm_audit_rows": nrows, "npm_audit": len(npm), "clawscore": len(S), "overlap": len(overlap), "db_not_npm": sorted(db_not_npm),
               "repo_only": len(repo_only), "npm_only": sorted(npm_only),
               "sentence": f"npm audit returned {len(npm)} advisories for openclaw@{v} on {meta['fetched_utc'][:10]}; the maker's repository lists {len(S)} (feed newest 2026-09-11)."}
        result["versions"].append(row)
        print(f"{v} npm_audit={len(npm)} clawscore={len(S)} = overlap {len(overlap)} + db_not_npm {len(db_not_npm)} {sorted(db_not_npm)} + repo_only {len(repo_only)}; npm_only {len(npm_only)}")
        print("  " + row["sentence"])
    out = json.dumps(result, indent=1, sort_keys=True).encode()
    open(os.path.join(a.out, "split.json"), "wb").write(out)
    print("split.json sha256", sha(out))


if __name__ == "__main__":
    main()
