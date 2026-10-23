#!/usr/bin/env python3
"""Idle-Linux discovery + version recovery from the fixture, build-info/dirlist ONLY. No execution of the target.
Usage: python3 discover_recover.py <fixture-root>  -> prints JSON. Exit 0 iff an idle (installed, lingering, not running) gateway is found and a version recovered."""
import json, sys, hashlib
from pathlib import Path
ROOT = Path(sys.argv[1]); HERE = Path(__file__).resolve().parent
FP = json.loads((HERE / "dirlist_fingerprint.json").read_text())
EXPECT_NAMES = [l.strip() for l in (HERE / FP["names_file"]).read_text().splitlines() if l.strip()]
def find_install():
    for pj in ROOT.rglob("node_modules/openclaw/package.json"):
        try:
            if json.loads(pj.read_text()).get("name") == "openclaw": return pj.parent
        except Exception: pass
    return None
inst = find_install(); out = {"install": None, "idle": {}, "version": {}}
assert inst, "no openclaw install found"
out["install"] = str(inst.relative_to(ROOT))
# idle signals: user unit present, enabled via wants symlink, linger marker, and NO process evidence
unit = next(ROOT.rglob(".config/systemd/user/openclaw-gateway.service"), None)
wants = next(ROOT.rglob(".config/systemd/user/default.target.wants/openclaw-gateway.service"), None)
linger = list(ROOT.rglob("var/lib/systemd/linger/*"))
proc = list(ROOT.rglob("proc/*/cmdline")) + list(ROOT.rglob("*.pid"))
out["idle"] = {"user_unit": bool(unit), "enabled_symlink": bool(wants), "linger_markers": [p.name for p in linger], "running_process_evidence": len(proc)}
idle_ok = bool(unit) and bool(wants) and bool(linger) and len(proc) == 0
# version recovery, package.json version must be absent so we prove the fallback
pj = json.loads((inst / "package.json").read_text())
out["version"]["package_json_has_version"] = "version" in pj
bi = inst / "dist/build-info.json"; bs = inst / "dist/.buildstamp"
v_bi = json.loads(bi.read_text()).get("version") if bi.is_file() else None
head_bs = json.loads(bs.read_text()).get("head") if bs.is_file() else None
got_names = sorted(p.name for p in (inst / "dist").glob("*.js"))
jacc = len(set(got_names) & set(EXPECT_NAMES)) / len(set(got_names) | set(EXPECT_NAMES)) if got_names else 0.0
out["version"].update({"from_build_info": v_bi, "buildstamp_head": head_bs,
    "dirlist_jaccard_vs_%s" % FP["version"]: round(jacc, 4), "dirlist_match": jacc >= 0.99})
recovered = v_bi if (not pj.get("version") and v_bi) else None
out["version"]["recovered"] = recovered
out["recovered_without_package_version"] = bool(recovered) and out["version"]["dirlist_match"]
print(json.dumps(out, indent=1))
sys.exit(0 if idle_ok and out["recovered_without_package_version"] else 1)
