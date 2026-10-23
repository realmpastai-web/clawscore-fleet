#!/usr/bin/env python3
"""Hark frozen gate for ClawScore Fleet v0.2.3 (v0.2.2 semver/grammar fix + 894-advisory feed re-pin + CSV formula escape).
Frozen 2026-10-18. Inputs: feed-csv package @ 1216d18 (inputs/clawscore-feed-csv-2026-10-17), v0.2.2 task @ 0b5260f
(inputs/clawscore-v0.2.2), constants in expected-v023.json (all reproduced by regen_v023.py / npm_xcheck.py in this folder).
Usage: python3 gate_v023.py <PR checkout> <main checkout @ 58d4925> [--semver <dir of npm semver 7.8.5>]
Prints one PASS/FAIL/REPORT line per check, then SUMMARY. Exit 1 if any FAIL. Never edits the checkout.
Run `sha256sum -c SHA256SUMS` in this folder first."""
import csv, hashlib, importlib.util, io, json, re, subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PR, BASE = Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve()
SEM = sys.argv[sys.argv.index("--semver") + 1] if "--semver" in sys.argv else str(PR / "tools/semver/node_modules/semver")
X = json.loads((HERE / "expected-v023.json").read_text())
OUT = []
def rec(s, cid, msg): OUT.append((s, cid, msg)); print(f"{s}\t{cid}\t{msg}", flush=True)
def check(cid, ok, msg): rec("PASS" if ok else "FAIL", cid, msg)
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def jload(p):
    try: return json.loads(Path(p).read_text())
    except Exception as e: return {"__error__": str(e)}
def guard(cid, fn):
    try: fn()
    except Exception as e: check(cid, False, f"exception {type(e).__name__}: {e}")

# ---- reference grammar (regen_v023.py, frozen) loaded as a module on the PR's pinned landscape
REF_SRC = (HERE / "regen_v023.py").read_text().split("R = [")[0]
ref = {}
exec(REF_SRC.replace("d = sys.argv[1]", f"d = {str(PR / 'evidence/landscape')!r}"), ref)
A, V, key, comparators, inrange = ref["A"], ref["V"], ref["key"], ref["comparators"], ref["inrange"]
RANGES = [(a, p["vulnerable_version_range"]) for a in A for p in a["vulnerabilities"]
          if p["package"]["name"].lower() == "openclaw" and p.get("vulnerable_version_range")]
STABLE = sorted([v for v in V if re.match(r"^\d+\.\d+\.\d+(?:-\d+)?$", v.strip()) and v != "0.0.1"], key=key)
def ref_ids(v): return sorted({a["ghsa_id"] for a, r in RANGES if comparators(r) and inrange(v, comparators(r))})

rep = jload(PR / "evidence/verify-report.json"); base = jload(BASE / "evidence/verify-report.json")
G = rep.get("gates", {}) if isinstance(rep, dict) else {}

# ---- G0 release + base
check("G0.release", rep.get("release") == X["release"], f"release={rep.get('release')!r} (want {X['release']!r})")
check("G0.base", rep.get("base") in (X["base"], X["base"][:7]), f"base={rep.get('base')!r} (want {X['base'][:7]})")
check("G0.base_checkout", jload(BASE / "evidence/verify-report.json").get("release") == "0.2.1", "second arg is main @ 58d4925 (release 0.2.1)")

# ---- G1 feed pin (stage 2)
for rel, want in X["sha256"].items():
    p = PR / rel
    got = sha(p) if p.exists() else "MISSING"
    check(f"G1.sha.{Path(rel).name}", got == want, f"{rel} {got[:12]} (want {want[:12]})")
vt = (PR / "clawscore_fleet/versions.py").read_text()
m = re.search(r'^FEED_NEWEST\s*=\s*"([^"]+)"', vt, re.M)
check("G1.FEED_NEWEST", bool(m) and m.group(1) == X["feed_newest"], f"versions.py FEED_NEWEST={m.group(1) if m else None!r}")
check("G1.no_xx9p_gap", any(a["ghsa_id"] == "GHSA-xx9p-hc9w-6p5h" for a in A), "GHSA-xx9p-hc9w-6p5h in pinned feed")
lsum = PR / "evidence/landscape/SHA256SUMS"
ok = lsum.exists() and subprocess.run(["sha256sum", "-c", "--quiet", "SHA256SUMS"], cwd=lsum.parent, capture_output=True).returncode == 0
check("G1.landscape_sums", ok, "sha256sum -c evidence/landscape/SHA256SUMS")

# ---- G2 landscape constants + freshness
lh = G.get("landscape_hashes", {})
check("G2.landscape_hashes", lh.get("pass") is True and all(lh.get(k) == v for k, v in X["landscape"].items()),
      f"{ {k: lh.get(k) for k in X['landscape']} } want {X['landscape']}")
fr = G.get("freshness", {})
check("G2.freshness", fr.get("pass") is True and fr.get("feed_newest") == X["feed_newest"], f"freshness.feed_newest={fr.get('feed_newest')!r}")

# ---- G3 feed_check_same (policy: newer upstream => FAIL; offline => SKIP never PASS)
fc = PR / "evidence/feed-check.log"
fct = fc.read_text() if fc.exists() else ""
kv = dict(re.findall(r"^(\w+):\s*(.*)$", fct, re.M))
check("G3.feed_check_log", kv.get("comparison") == "same" and kv.get("newest_date") == X["feed_newest"] and kv.get("pinned_date") == X["feed_newest"],
      f"comparison={kv.get('comparison')!r} newest_date={kv.get('newest_date')!r} pinned_date={kv.get('pinned_date')!r}")
fg = G.get("feed_check_same", {})
check("G3.feed_check_gate", fg.get("pass") is True and fg.get("status") == "same", f"gates.feed_check_same={fg}")

# ---- G4 range grammar (v0.2.2 stage 1 carried + space-separated AND found in the 894 feed)
unparsed = [r for _, r in RANGES if comparators(r) is None]
uniq = sorted({r for _, r in RANGES})
check("G4.ref_ranges", not unparsed and len(RANGES) == X["ranges"]["advisories_with_openclaw_range"] and len(uniq) == X["ranges"]["unique_ranges"]
      and sum(len(comparators(r)) for r in uniq) == X["ranges"]["unique_range_comparators"],
      f"{len(RANGES)} ranges, {len(uniq)} unique, {sum(len(comparators(r) or []) for r in uniq)} comparators, unparsed={unparsed[:3]}")
sp = sorted(r for r in uniq if len(comparators(r)) > 1 and "," not in r)
check("G4.space_and_set", sp == X["ranges"]["space_and_ranges"], f"space-AND ranges {sp}")
def pr_mod(name):
    sys.path.insert(0, str(PR))
    try: return importlib.import_module(name)
    finally: sys.path.pop(0)
def g4_project():
    cves = pr_mod("clawscore_fleet.cves"); vers = pr_mod("clawscore_fleet.versions")
    hk = getattr(vers, "hark_key", None) or getattr(cves, "hark_key")
    none_v = [v for v in V if hk(v) is None]
    bounds = sorted({b for r in uniq for _, b in comparators(r)})
    none_b = [b for b in bounds if hk(b) is None]
    check("G4.hark_key_total", not none_v and not none_b, f"hark_key None: versions {none_v[:3]} of {len(V)}, bounds {none_b[:3]} of {len(bounds)}")
    allv = sorted(set(V) | set(bounds))
    pk = None if (none_v or none_b) else sorted(allv, key=lambda x: (hk(x), x))
    check("G4.key_order_equals_ref", pk is not None and pk == sorted(allv, key=lambda x: (key(x), x)), f"project hark_key order == regen_v023 key order over {len(allv)} versions+bounds")
    order = ["2026.5.19-alpha.1", "2026.5.19-beta.2", "2026.5.19", "2026.5.19-1"]
    check("G4.prerelease_order", None not in [hk(x) for x in order + ["2026.1.29-beta3"]] and [hk(x) for x in order] == sorted(hk(x) for x in order) and hk("2026.1.29-beta3") == hk("2026.1.29-beta.3"),
          "alpha.1 < beta.2 < release < -1; beta3 == beta.3")
    diff = [(v, r) for v in sorted(V) for r in uniq if cves.in_range(v, r) != inrange(v, comparators(r))]
    check("G4.in_range_equals_ref", not diff, f"project in_range != reference on {len(diff)} of {len(V)*len(uniq)} pairs; first {diff[:3]}")
guard("G4.project", g4_project)

# ---- G5 semver cross-check vs npm 7.8.5 (commas->spaces, includePrerelease)
sc = G.get("semver_crosscheck", {})
check("G5.semver_crosscheck", sc.get("pass") is True and all(sc.get(k) == v for k, v in X["semver_crosscheck"].items()),
      f"{ {k: sc.get(k) for k in X['semver_crosscheck']} } want {X['semver_crosscheck']}")
for g in ("semver_comma_normalized", "prerelease_order"):
    check(f"G5.gate.{g}", G.get(g, {}).get("pass") is True, f"gates.{g}.pass={G.get(g, {}).get('pass')!r}")
scl = PR / "evidence/semver-crosscheck.log"
st = scl.read_text() if scl.exists() else ""
check("G5.no_grammar_label", "hark-grammar" not in st and scl.exists(), f"'hark-grammar' lines in semver-crosscheck.log: {st.count('hark-grammar')}")
if Path(SEM).exists():
    r = subprocess.run([sys.executable, str(HERE / "npm_xcheck.py"), str(PR / "evidence/landscape"), SEM], capture_output=True, text=True)
    want = f"decisions {X['semver_crosscheck']['decisions']} disagreements {X['semver_crosscheck']['disagreements']} post_release_suffix {X['semver_crosscheck']['disagreements']} other 0"
    check("G5.npm_xcheck_ref", want in r.stdout and r.stdout.startswith("semver 7.8.5"), r.stdout.strip() or r.stderr.strip()[-200:])
else:
    rec("REPORT", "G5.npm_xcheck_ref", f"SKIP: no semver package at {SEM} (run npm ci in tools/semver)")
rl = PR / "evidence/v0.2.2-repro.log"
frozen = [l for l in (HERE / "repro-v0.2.2.log").read_text().splitlines() if not l.startswith("== 5") and "/" not in l]
got = set(rl.read_text().splitlines()) if rl.exists() else set()
miss = [l for l in frozen if l not in got]
check("G5.v022_repro_log", rl.exists() and not miss, f"evidence/v0.2.2-repro.log has all {len(frozen)} frozen sections 1-4 lines; missing {miss[:3]}")

# ---- G6 per-version counts, CVE map, fix target
vv = jload(PR / "evidence/landscape/version-vulns.json")
check("G6.stable", len(STABLE) == X["stable_releases"], f"{len(STABLE)} stable releases")
cm = jload(PR / "evidence/cve-map.json")
check("G6.cve_map_header", cm.get("advisory_count") == X["landscape"]["total_advisories"] and cm.get("with_cve_id") == X["landscape"]["with_cve_id"]
      and cm.get("feed_newest") == X["feed_newest"], f"advisory_count={cm.get('advisory_count')} with_cve_id={cm.get('with_cve_id')} feed_newest={cm.get('feed_newest')}")
vrows = cm.get("versions", {}) if isinstance(cm, dict) else {}
vvd = {r[0]: r for r in vv} if isinstance(vv, list) else {}
bad = []
for v in STABLE:
    ids = ref_ids(v); row = vrows.get(v, {}); exp = vvd.get(v)
    if row.get("ghsa_ids") != ids: bad.append((v, "ghsa_ids", len(row.get("ghsa_ids") or []), len(ids)))
    elif exp and (row.get("advisories"), {s: row.get(s) for s in ("critical", "high", "medium", "low")}) != (exp[2], exp[3]): bad.append((v, "counts"))
check("G6.cve_map_versions", not bad and len(vrows) == len(STABLE), f"{len(STABLE)-len(bad)}/{len(STABLE)} versions == reference; bad {bad[:4]}")
r129 = vrows.get("2026.1.29", {})
check("G6.v2026_1_29", {k: r129.get(k) for k in X["v2026_1_29"]} == X["v2026_1_29"], f"2026.1.29 { {k: r129.get(k) for k in X['v2026_1_29']} }")
ft = G.get("fix_target", {}); fo = jload(PR / "evidence/fixorder.json")
check("G6.fix_target", ft.get("pass") is True and all(ft.get(k) == v for k, v in X["fix_target"].items()) and fo.get("min_clearing_version") == X["fix_target"]["min_clearing_version"],
      f"fix_target { {k: ft.get(k) for k in X['fix_target']} }; fixorder.min_clearing_version={fo.get('min_clearing_version')!r}")
check("G6.cve_mapping", G.get("cve_mapping", {}).get("pass") is True and G.get("cve_mapping", {}).get("diff_lines") == 0, f"cve_mapping={G.get('cve_mapping')}")

# ---- G7 CSV formula escape
E = {}
exec((HERE / "escape_reference.py").read_text().split('if __name__')[0], E)
def g7():
    exp_mod = pr_mod("clawscore_fleet.export_defender")
    esc, unesc = getattr(exp_mod, "escape_cell"), getattr(exp_mod, "unescape_cell")
    rows = list(csv.DictReader(open(HERE / "formula-escape-vectors.tsv", encoding="utf-8"), delimiter="\t", quoting=csv.QUOTE_NONE))
    badv = [r["id"] for r in rows if not (esc(json.loads(r["input_json"])) == json.loads(r["expected_cell_json"])
            and E["csv_field"](esc(json.loads(r["input_json"]))) == json.loads(r["expected_csv_field_json"])
            and unesc(esc(json.loads(r["input_json"]))) == json.loads(r["input_json"]))]
    check("G7.vectors", len(rows) == X["csv_vectors"] and not badv, f"PR escape_cell/unescape_cell: {len(rows)-len(badv)}/{len(rows)} vectors; fail {badv}")
guard("G7.vectors", g7)
pp = list(PR.rglob("planted-row.csv"))
pp = [p for p in pp if ".git" not in p.parts]
check("G7.planted_row", len(pp) == 1 and pp[0].read_bytes() == (HERE / "planted-row.expected.csv").read_bytes(),
      f"planted-row.csv found {[str(p.relative_to(PR)) for p in pp]}; byte-equal to planted-row.expected.csv")
fa = [p for p in PR.rglob("defender_local_agents.csv") if ".git" not in p.parts]
badc, n = [], 0
if len(fa) == 1:
    rows = list(csv.DictReader(open(fa[0], encoding="utf-8", newline="")))
    for r in rows:
        for c, v in r.items():
            if c in E["INT_COLUMNS"] or v == "": continue
            n += 1
            if v[:1] in E["DANGER"] or E["escape_cell"](E["unescape_cell"](v)) != v: badc.append((r.get("Device name"), c, v[:20]))
    check("G7.export_cells", not badc, f"{n} text cells: escape(unescape(cell)) == cell and no bare danger start; bad {badc[:4]}")
    fx = {(r["cs_fix_target"], r["cs_feed_newest"]) for r in rows}
    check("G7.export_cs_shared", fx == {(X["fix_target"]["min_clearing_version"], X["feed_newest"])}, f"(cs_fix_target, cs_feed_newest) = {fx}")
    badg = [r["Device name"] for r in rows if r["cs_build_verdict"] == "exact" and r["cs_ghsa_ids"].split("|") != ref_ids(r["cs_candidates"]) and not (r["cs_ghsa_ids"] == "" and not ref_ids(r["cs_candidates"]))]
    check("G7.export_ghsa_ref", not badg, f"exact-verdict rows whose cs_ghsa_ids != reference: {badg[:5]} of {sum(r['cs_build_verdict']=='exact' for r in rows)}")
else:
    check("G7.export_cells", False, f"defender_local_agents.csv found {len(fa)}")
check("G7.gate", G.get("csv_escape", {}).get("pass") is True, f"gates.csv_escape={G.get('csv_escape')}")

# ---- G8 no regression vs main @ 58d4925
same = [g for g in X["unchanged_gates_vs_base"] if G.get(g) != base.get("gates", {}).get(g)]
check("G8.unchanged_gates", not same, f"{len(X['unchanged_gates_vs_base'])-len(same)}/{len(X['unchanged_gates_vs_base'])} gates identical to main; differ {same}")
check("G8.all_gates_pass", G and all(isinstance(v, dict) and v.get("pass") is True for v in G.values()), f"failing gates {[k for k, v in G.items() if not (isinstance(v, dict) and v.get('pass') is True)]}")
# gate_v021 hard-codes the v0.2.1 feed pins (cs_fix_target 2026.5.27, cs_feed_newest 2026-07-02) inside G2.keys_types/G3.values.
# Re-pin exactly those two constants to this gate's frozen feed values (expected-v023.json); every other v021 line runs unchanged.
import tempfile
v21 = (HERE / "gate_v021.py").read_text()
v21r = v21.replace('"2026.5.27"', json.dumps(X["fix_target"]["min_clearing_version"])).replace('"2026-07-02"', json.dumps(X["feed_newest"]))
nchg = sum(a != b for a, b in zip(v21.splitlines(), v21r.splitlines()))
check("G8.v021_repin_scope", nchg == 3 and len(v21.splitlines()) == len(v21r.splitlines()), f"re-pinned gate_v021 differs on {nchg} lines (want 3: L125 fix_target, L126 feed_newest, L147 reference row)")
with tempfile.TemporaryDirectory() as td:
    (Path(td) / "gate_v021_repinned.py").write_text(v21r)
    r = subprocess.run([sys.executable, str(Path(td) / "gate_v021_repinned.py"), str(PR), str(BASE), "--expected-lines", str(HERE / "expected-readme-lines.tsv")], capture_output=True, text=True, cwd=HERE)
res = dict((l.split("\t")[1], l.split("\t")[0]) for l in r.stdout.splitlines() if l.count("\t") >= 2)
need = [c for c in X["v021_checks_must_pass"] if res.get(c) != "PASS"]
check("G8.v021_schema_checks", not need, f"{len(X['v021_checks_must_pass'])-len(need)}/{len(X['v021_checks_must_pass'])} gate_v021 checks PASS; not passing {need}")
rec("REPORT", "G8.v021_feed_driven", {c: res.get(c) for c in X["v021_checks_feed_driven_allowed_to_fail"]})
rec("REPORT", "G8.new_gates", sorted(set(G) - set(base.get("gates", {}))))

# ---- G9 CI-safe: verify must not need git history (actions/checkout default fetch-depth 1; PR #5 CI run 39104181631 died on `git show 58d4925:evidence/verify-report.json`)
gitcalls = sorted(f"{q.relative_to(PR)}:{i}" for q in (PR / "clawscore_fleet").rglob("*.py") for i, l in enumerate(q.read_text().splitlines(), 1) if re.search(r'["\']git["\']', l))
check("G9.no_git_in_package", not gitcalls, f"clawscore_fleet/*.py lines invoking git: {gitcalls}")
bfr = HERE / "base-verify-report-58d4925.json"
check("G9.frozen_base_report", sha(bfr) == X["base_verify_report_sha256"] and sha(BASE / "evidence/verify-report.json") == X["base_verify_report_sha256"], f"frozen base report sha256 {sha(bfr)[:12]} == main@58d4925 evidence/verify-report.json")

f = [c for s, c, _ in OUT if s == "FAIL"]
print(f"SUMMARY pass={sum(1 for s,_,_ in OUT if s=='PASS')} fail={len(f)} report={sum(1 for s,_,_ in OUT if s=='REPORT')} failed={f}")
sys.exit(1 if f else 0)
