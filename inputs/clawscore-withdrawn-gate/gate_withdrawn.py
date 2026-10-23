#!/usr/bin/env python3
"""Gate for the ClawScore withdrawn fix (Hark, 2026-10-18).

Usage, from a clawscore-fleet checkout (PR head or main):
  python3 inputs/clawscore-withdrawn-gate/gate_withdrawn.py [--repo .] [--version-vulns PATH]
Exit 0 = GATE PASS, 1 = GATE FAIL, 2 = setup error.

The evaluator below is copied verbatim from clawscore_fleet/versions.py at main 026f719
(hark_key, parse_comparators, stable_releases; source sha256 in PINS) so a PR that edits
versions.py cannot move the expected numbers. G4 imports the checkout's own clawscore_fleet.cves
to check the advisory id set its code produces.

G0 pins     ghsa-all.json, versions.json and the reconcile counted-2026.4.22.tsv match their frozen sha256
G1 control  this evaluator WITH withdrawn rows reproduces main 026f719 version-vulns.json exactly (proves it is main's evaluator)
G2 rows     every row of version-vulns.json == recompute with withdrawn_at advisories excluded (version, date, total, severity)
G3 ids      recomputed 2026.4.22 id set == counted-2026.4.22.tsv (148) and severity split matches the tsv
G4 code     checkout's clawscore_fleet.cves.build_index(): 2026.4.22 ids == tsv, and no withdrawn id under any version
"""
import argparse, hashlib, json, re, sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
PINS = {
    "evidence/landscape/ghsa-all.json": "27b020df70c9896d7b94280ad0646dc69ef4d27e504d81bc6719dedcb6446034",
    "evidence/landscape/versions.json": "6e2b3ff8619dba5c5043dafb3944c270623ac15a3991ad30fb9c07e78a11dfda",
    "inputs/clawscore-withdrawn-reconcile/counted-2026.4.22.tsv": None,  # filled from SHA256SUMS of the reconcile folder
}
MAIN_VV_SHA = "556bd11e0d5f9fa49ddf8dc1910f24d6f075073e29eafd0e22cd5437097c732c"
VERSIONS_PY_026F719_SHA = "2441d1e499aa1172941b036b1157f70fe8e6e2750bb8b6f0d7fc36dc99d922ed"
VER = "2026.4.22"

# ---- verbatim from clawscore_fleet/versions.py @ 026f719 ----
_VERSION_RE = re.compile(
    r"^(\d+)\.(\d+)\.(\d+)(?:-(\d+))?(?:-(alpha|beta|rc)\.?(\d+))?$"
)
_STABLE_RE = re.compile(r"^\d+\.\d+\.\d+(?:-\d+)?$")
_PRERELEASE_RANK = {"alpha": 0, "beta": 1, "rc": 2}
_CMP = re.compile(r"\s*(<=|>=|<|>|=)\s*([^\s,]+)\s*,?")
class RangeSyntaxError(ValueError):
    pass
def hark_key(version):
    match = _VERSION_RE.match(version.strip())
    if not match:
        return None
    major, minor, patch, post, tag, number = match.groups()
    rank = _PRERELEASE_RANK.get(tag, 0) * 1000 + int(number or 0)
    return (int(major), int(minor), int(patch), 0 if tag else 1, rank, int(post or 0))
def parse_comparators(rng):
    if not isinstance(rng, str) or rng == "":
        raise RangeSyntaxError(f"unparsed range {rng!r}")
    found = []
    pos = 0
    length = len(rng)
    while pos < length:
        match = _CMP.match(rng, pos)
        if match is None or match.end() == pos:
            raise RangeSyntaxError(f"unparsed range {rng!r}")
        operator, bound = match.group(1), match.group(2)
        if hark_key(bound) is None:
            raise RangeSyntaxError(f"unparsed bound {bound!r} in {rng!r}")
        found.append((operator, bound))
        pos = match.end()
    if not found:
        raise RangeSyntaxError(f"unparsed range {rng!r}")
    return found
def stable_releases(published):
    found = []
    for version in published:
        if version == "0.0.1" or _STABLE_RE.match(version) is None:
            continue
        if hark_key(version) is None:
            continue
        found.append(version)
    found.sort(key=hark_key)
    return found
# ---- end verbatim ----

OPS = {"<": lambda a, b: a < b, "<=": lambda a, b: a <= b, ">": lambda a, b: a > b, ">=": lambda a, b: a >= b, "=": lambda a, b: a == b}
def in_range(v, rng):
    left = hark_key(v)
    if left is None:
        return False
    return all(OPS[op](left, hark_key(b)) for op, b in parse_comparators(rng))
def ranges(a):
    return [str(e["vulnerable_version_range"]) for e in a.get("vulnerabilities") or []
            if str((e.get("package") or {}).get("name") or "").lower() == "openclaw" and e.get("vulnerable_version_range")]
def recompute(adv, published, include_withdrawn):
    stable = stable_releases(published)
    per = {v: [] for v in stable}
    for a in adv:
        if a.get("withdrawn_at") and not include_withdrawn:
            continue
        rs = ranges(a)
        for v in stable:
            if rs and any(in_range(v, r) for r in rs):
                per[v].append(a)
    rows = []
    for v in stable:
        c = Counter(a.get("severity") for a in per[v])
        rows.append([v, re.search(r"\d{4}-\d\d-\d\d", published[v]).group(0), len(per[v]), {s: c.get(s, 0) for s in ("critical", "high", "medium", "low")}])
    return rows, per
def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=str(HERE.parents[1]))
    ap.add_argument("--version-vulns", default=None, help="file to check instead of <repo>/evidence/landscape/version-vulns.json")
    a = ap.parse_args()
    repo = Path(a.repo).resolve()
    results = []
    def check(name, ok, detail=""):
        results.append(ok); print(f"{'PASS' if ok else 'FAIL'}\t{name}\t{detail}")
    # G0
    recon_sums = {l.split()[1].lstrip("./"): l.split()[0] for l in (repo / "inputs/clawscore-withdrawn-reconcile/SHA256SUMS").read_text().splitlines() if l.strip()}
    PINS["inputs/clawscore-withdrawn-reconcile/counted-2026.4.22.tsv"] = recon_sums.get("counted-2026.4.22.tsv")
    for rel, want in PINS.items():
        p = repo / rel
        got = sha(p) if p.exists() else "MISSING"
        check(f"G0.pin {rel}", got == want, got[:16])
    adv = json.loads((repo / "evidence/landscape/ghsa-all.json").read_text())
    published = {str(k): str(v) for k, v in json.loads((repo / "evidence/landscape/versions.json").read_text()).items()}
    main_vv = HERE / "controls/mutant-counts-withdrawn-main-026f719.json"
    # G1
    with_w, _ = recompute(adv, published, True)
    check("G1.control evaluator WITH withdrawn == main 026f719 version-vulns.json", sha(main_vv) == MAIN_VV_SHA and with_w == json.loads(main_vv.read_text()), f"rows={len(with_w)} main_sha={sha(main_vv)[:16]}")
    # G2
    exp, per = recompute(adv, published, False)
    vv_path = Path(a.version_vulns).resolve() if a.version_vulns else repo / "evidence/landscape/version-vulns.json"
    got = json.loads(vv_path.read_text())
    gmap = {r[0]: r for r in got}
    bad = [(r[0], gmap.get(r[0], [None, None, "MISSING"])[2], r[2]) for r in exp if gmap.get(r[0]) != r]
    extra = sorted(set(gmap) - {r[0] for r in exp})
    check("G2.rows version-vulns == recompute excluding withdrawn", not bad and not extra and len(got) == len(exp),
          f"rows={len(got)}/{len(exp)} mismatched={len(bad)} extra={extra} first={bad[:3]} (version, file_total, expected_total)")
    row = gmap.get(VER)
    print(f"INFO\t{VER} file={row[2:] if row else None} expected={next(r[2:] for r in exp if r[0] == VER)}")
    # G3
    tsv = [l.split("\t") for l in (repo / "inputs/clawscore-withdrawn-reconcile/counted-2026.4.22.tsv").read_text().splitlines()[1:] if l]
    tsv_ids = {r[0] for r in tsv}; tsv_sev = Counter(r[1] for r in tsv)
    rid = {x["ghsa_id"] for x in per[VER]}; rsev = Counter(x["severity"] for x in per[VER])
    check(f"G3.ids recompute {VER} == counted-2026.4.22.tsv", rid == tsv_ids and rsev == tsv_sev,
          f"recompute={len(rid)} tsv={len(tsv_ids)} only_recompute={sorted(rid - tsv_ids)[:5]} only_tsv={sorted(tsv_ids - rid)[:5]} sev={dict(sorted(rsev.items()))}")
    # G4
    withdrawn = {x["ghsa_id"] for x in adv if x.get("withdrawn_at")}
    try:
        sys.path.insert(0, str(repo))
        for m in [k for k in sys.modules if k.startswith("clawscore_fleet")]:
            del sys.modules[m]
        from clawscore_fleet import cves
        idx = cves.build_index()
        cid = {x.get("ghsa_id") for x in idx["per_version"].get(VER, [])}
        leaked = sorted({x.get("ghsa_id") for v in idx["per_version"].values() for x in v} & withdrawn)
        check(f"G4.code clawscore_fleet.cves {VER} ids == tsv", cid == tsv_ids, f"code={len(cid)} only_code={sorted(cid - tsv_ids)[:5]} only_tsv={sorted(tsv_ids - cid)[:5]}")
        check("G4.code no withdrawn id under any version", not leaked, f"withdrawn_counted={len(leaked)} e.g. {leaked[:3]}")
    except Exception as e:
        check("G4.code import clawscore_fleet.cves", False, repr(e)[:200])
    ok = all(results)
    print("GATE PASS" if ok else f"GATE FAIL ({results.count(False)} checks)")
    return 0 if ok else 1

if __name__ == "__main__":
    sys.exit(main())
