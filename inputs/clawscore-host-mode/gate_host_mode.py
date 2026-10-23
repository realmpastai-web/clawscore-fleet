#!/usr/bin/env python3
"""Gate for ClawScore host mode (frozen by Hark 2026-10-18 on main 026f719).

  python3 gate_host_mode.py --checkout <repo> [--cache DIR]   # build fixture, run scan-host, judge
  python3 gate_host_mode.py --scan-json <scan.json>           # judge an existing scan.json (controls)

Fixture: 5 installs from 4 pinned npm tarballs (build_host_fixture.py). Expected advisories per
version come from main 026f719 evidence/scan.json (expected-advisories-026f719.json).
"""
import argparse, json, subprocess, sys, tempfile
from pathlib import Path

H = Path(__file__).resolve().parent
sys.path.insert(0, str(H))
import build_host_fixture as fx  # noqa: E402

EXP = json.loads((H / "expected-advisories-026f719.json").read_text())["by_version"]
ROOTS = {hid: "/" + rel for hid, (_, rel, _) in fx.LAYOUT.items()}
fails = []


def chk(tag, ok, note=""):
    print(("PASS" if ok else "FAIL") + f"\t{tag}\t{note}")
    ok or fails.append(tag)


def judge(doc: dict, outputs_text: str = "") -> None:
    installs = doc.get("installs") or []
    by_root = {r.get("install_root"): r for r in installs}
    chk("S1.five_installs", sorted(by_root) == sorted(ROOTS.values()), f"got {sorted(k for k in by_root if k)}")
    for hid in ("H1", "H2", "H3"):
        version = fx.LAYOUT[hid][0]
        r = by_root.get(ROOTS[hid], {})
        e = EXP[version]
        ok = (r.get("verdict") == "exact" and r.get("version") == version and r.get("family") == e["family"]
              and r.get("cves") == e["cves"] and r.get("ghsa_ids") == e["ghsa_ids"]
              and r.get("advisory_count") == e["advisory_count"] and r.get("vulnerable") is e["vulnerable"])
        chk(f"S2.{hid}.exact_{version}_advisories_equal_lab", ok,
            f"verdict={r.get('verdict')} version={r.get('version')} adv={r.get('advisory_count')} want {e['advisory_count']}")
    r4 = by_root.get(ROOTS["H4"], {})
    chk("S3.H4.beta_unknown_not_clean",
        r4.get("verdict") == "unknown" and r4.get("version") is None and r4.get("vulnerable") is None
        and r4.get("declared_version") == "2026.10.10-beta.1",
        f"verdict={r4.get('verdict')} version={r4.get('version')} vulnerable={r4.get('vulnerable')!r} declared={r4.get('declared_version')}")
    unid = doc.get("unidentified")
    chk("S4.H4.listed_unidentified", isinstance(unid, list) and r4.get("id") in unid and len(unid) == 1, f"unidentified={unid}")
    fo_ids = [item.get("id") for item in doc.get("fix_order") or []]
    chk("S5.H4.not_in_fix_order_as_vulnerable", r4.get("id") is not None and r4.get("id") not in fo_ids)
    r5 = by_root.get(ROOTS["H5"], {})
    e = EXP["2026.1.29"]
    chk("S6.H5.bytes_beat_package_json",
        r5.get("verdict") == "exact" and r5.get("version") == "2026.1.29" and r5.get("declared_version") == "2026.10.4"
        and r5.get("version_mismatch") is True and r5.get("advisory_count") == e["advisory_count"]
        and r5.get("ghsa_ids") == e["ghsa_ids"] and r5.get("vulnerable") is True,
        f"version={r5.get('version')} declared={r5.get('declared_version')} mismatch={r5.get('version_mismatch')} adv={r5.get('advisory_count')}")
    chk("S7.mismatch_only_H5", sorted(r.get("install_root") for r in installs if r.get("version_mismatch")) == [ROOTS["H5"]])
    want_fo = sorted(by_root[ROOTS[h]]["id"] for h in ("H2", "H3", "H5") if ROOTS[h] in by_root)
    chk("S8.fix_order_is_the_3_vulnerable", sorted(fo_ids) == want_fo and len(fo_ids) == 3, f"{fo_ids}")
    r2 = by_root.get(ROOTS["H2"], {})
    idle = r2.get("idle") or {}
    chk("S9.H2.root_linger_idle", idle.get("linger_markers") == ["root"] and idle.get("user_unit") is True, f"{idle}")
    text = outputs_text or json.dumps(doc)
    chk("S10.no_credential_values", fx.CANARY not in text)


def run_checkout(checkout: Path, cache: Path) -> None:
    with tempfile.TemporaryDirectory() as tmp:
        root, out = Path(tmp) / "host", Path(tmp) / "out"
        fx.build(root, cache)
        before = fx.manifest(root)
        proc = subprocess.run([sys.executable, "-m", "clawscore_fleet.cli", "scan-host", "--root", str(root), "--out", str(out)],
                              cwd=str(checkout), capture_output=True, text=True)
        chk("S0.scan_host_exit0", proc.returncode == 0, f"exit={proc.returncode} {(proc.stderr or '').strip().splitlines()[-1:]}")
        chk("S0.read_only_root", fx.manifest(root) == before)
        scan = out / "scan.json"
        if not scan.is_file():
            chk("S0.scan_json_written", False, "no <out>/scan.json")
            return
        texts = "".join(p.read_text(errors="replace") for p in out.rglob("*") if p.is_file()) + proc.stdout + proc.stderr
        judge(json.loads(scan.read_text()), texts)


ap = argparse.ArgumentParser()
ap.add_argument("--checkout")
ap.add_argument("--scan-json")
ap.add_argument("--cache", default=str(Path.home() / ".cache" / "clawscore-host-fixture"))
a = ap.parse_args()
if a.scan_json:
    judge(json.loads(Path(a.scan_json).read_text()))
else:
    run_checkout(Path(a.checkout).resolve(), Path(a.cache))
print("GATE " + ("PASS" if not fails else f"FAIL {fails}"))
sys.exit(1 if fails else 0)
