#!/usr/bin/env python3
"""clawscore-idle-paths gate (Hark, frozen 2026-10-18). Offline and deterministic. It never executes the installer scripts in sources/.
Steps:
  1. Prove each install root from the shipped OpenClaw installers (static read).
  2. Build an idle-Linux fixture with one gateway per root: a systemd USER unit, a linger marker, and no process.
  3. Emulate the default npm path lists of osquery 5.23.1 and Wazuh v4.14.9. The lists are parsed from their frozen source, not typed by hand.
  4. Run the ClawScore reference discovery.
  5. Gate:
     - osquery and Wazuh see L1 and L2, and miss L3 and L3s.
     - ClawScore finds all 4 with version 2026.4.15. For L3s the version comes from dist/build-info.json.
Usage: python3 gate_idle_paths.py [fixture_dir]   (default: a temp dir, removed afterwards)"""
import fnmatch, json, os, re, shutil, sys, tempfile
from pathlib import Path
H = Path(__file__).resolve().parent; S = H / "sources"
rd = lambda p: Path(p).read_text(errors="replace")
fails = []
def chk(tag, ok, msg):
    print(("PASS" if ok else "FAIL") + f"\t{tag}\t{msg}")
    if not ok: fails.append(tag)

# ---- 1. install roots from shipped installers (quotes are exact lines) ----
cli, ins = rd(S / "openclaw-install-cli.sh.txt"), rd(S / "openclaw-install.sh.txt")
Q = [("R.cli.default_prefix", cli, '  --prefix <path>                     Install prefix (default: ~/.openclaw; use \\$OPENCLAW_PREFIX to override)'),
     ("R.cli.node_dir", cli, '  echo "${PREFIX}/tools/node-v${NODE_VERSION}"'),
     ("R.cli.default_node", cli, 'DEFAULT_NODE_VERSION="24.21.0"'),
     ("R.cli.npm_global_into_node_dir", cli, '  local npm_install_args=(install -g --prefix "$(node_dir)" "${npm_args[@]}")'),
     ("R.cli.entry", cli, '  installed_entry="$(node_dir)/lib/node_modules/openclaw/dist/entry.js"'),
     ("R.sh.global_install", ins, '    cmd+=(--no-fund --no-audit "$freshness_flag" install -g)'),
     ("R.sh.npm_global_prefix", ins, '    npm config set prefix "$HOME/.npm-global" < /dev/null'),
     ("R.sh.sudo_system_prefix_warning", ins, 'Avoid sudo npm i -g for future OpenClaw updates')]
for tag, src, q in Q: chk(tag, q in src, repr(q))
NODE = re.search(r'DEFAULT_NODE_VERSION="([\d.]+)"', cli).group(1)
LAYOUTS = {  # id: (path relative to fixture root, keep version in package.json, which installer evidences it)
    "L1": ("usr/lib/node_modules/openclaw", True, "install.sh `install -g`, system prefix /usr (Debian/Ubuntu node; sudo npm i -g)"),
    "L2": ("home/claw2/.npm-global/lib/node_modules/openclaw", True, "install.sh `npm config set prefix $HOME/.npm-global`"),
    "L3": (f"home/claw3/.openclaw/tools/node-v{NODE}/lib/node_modules/openclaw", True, "install-cli.sh default prefix ~/.openclaw, node_dir, install -g --prefix"),
    "L3s": (f"home/claw4/.openclaw/tools/node-v{NODE}/lib/node_modules/openclaw", False, "L3 with version/gitHead stripped from package.json (ClawScore claim 3)")}
VERSION, COMMIT = "2026.4.15", "041266a6699cac3baef8ef39db41fa26f29f9db3"  # from ../rea-gate-idle-linux/recon.log dist/build-info.json

# ---- 2. fixture ----
def w(p, s): p.parent.mkdir(parents=True, exist_ok=True); p.write_text(s)
def build(root):
    for lid, (rel, keep, _) in LAYOUTS.items():
        pkg = root / rel
        pj = {"name": "openclaw", "bin": {"openclaw": "openclaw.mjs"}}
        if keep: pj = {"name": "openclaw", "version": VERSION, **{k: v for k, v in pj.items() if k != "name"}}
        w(pkg / "package.json", json.dumps(pj, indent=1) + "\n")
        w(pkg / "dist/build-info.json", json.dumps({"version": VERSION, "commit": COMMIT}) + "\n")
        w(pkg / "dist/entry.js", "// shipped entry\n")
        user = rel.split("/")[1] if rel.startswith("home/") else "claw1"
        home = root / "home" / user
        unit = home / ".config/systemd/user/openclaw-gateway.service"
        w(unit, f"[Service]\nExecStart=/{rel}/dist/entry.js gateway\n[Install]\nWantedBy=default.target\n")
        link = unit.parent / "default.target.wants/openclaw-gateway.service"; link.parent.mkdir(parents=True, exist_ok=True)
        if not link.exists(): os.symlink("../openclaw-gateway.service", link)
        w(root / "var/lib/systemd/linger" / user, "")

# ---- 3. comparator emulation (path lists parsed from frozen source) ----
def osq_paths():
    s = rd(S / "osquery-5.23.1_npm_packages.cpp"); blk = s.split("const std::set<std::string> kNodeModulesPath = {", 1)[1].split("};", 1)[0]
    nonwin = blk.split("#else", 1)[1].split("#endif", 1)[0]
    return [p.replace("%", "*") for p in re.findall(r'"(/[^"]+)"', nonwin) if not p.startswith("/Users/")]
def wz_paths():
    s = rd(S / "wazuh-v4.14.9_sharedDefs.h"); blk = s.split("UNIX_NPM_DEFAULT_BASE_DIRS", 1)[1].split("};", 1)[0]
    return [p for p in re.findall(r'"(/[^"]+)"', blk) if not p.startswith(("/Users/", "/private/"))]
def expand(root, pat):
    parts = [x for x in pat.strip("/").split("/")]; cur = [root]
    for seg in parts:
        nxt = []
        for c in cur:
            if any(ch in seg for ch in "*?["):
                nxt += [c / n for n in sorted(os.listdir(c)) if fnmatch.fnmatchcase(n, seg)] if c.is_dir() else []
            elif (c / seg).exists(): nxt.append(c / seg)
        cur = nxt
    return cur
def emulate(root, pats, need_version):
    seen = {}
    for pat in pats:
        for base in expand(root, pat):
            pj = base / "node_modules/openclaw/package.json"
            if pj.is_file():
                d = json.loads(pj.read_text())
                if need_version and "version" not in d: continue  # Wazuh packagesNPM.hpp: name && version required
                seen[str(pj.parent.relative_to(root))] = d.get("version", "")
    return seen

# ---- 4. ClawScore reference discovery: every */lib/node_modules/openclaw under /usr, /opt and each home, depth-bounded ----
def clawscore(root):
    out = {}
    for top in ["usr", "opt", "home", "root"]:
        t = root / top
        if not t.is_dir(): continue
        for dp, dns, _ in os.walk(t):
            rel = Path(dp).relative_to(root)
            if len(rel.parts) > 9: dns[:] = []; continue
            if Path(dp).name == "openclaw" and Path(dp).parent.name == "node_modules" and (Path(dp) / "package.json").is_file():
                d = json.loads((Path(dp) / "package.json").read_text()); v, src = d.get("version", ""), "package.json"
                bi = Path(dp) / "dist/build-info.json"
                if not v and bi.is_file(): v, src = json.loads(bi.read_text()).get("version", ""), "dist/build-info.json"
                out[str(rel)] = (v, src); dns[:] = []
    return out

def main():
    keep = len(sys.argv) > 1; root = Path(sys.argv[1]).resolve() if keep else Path(tempfile.mkdtemp(prefix="idle-paths-"))
    try:
        build(root)
        idle = all((root / "var/lib/systemd/linger" / u).exists() for u in ["claw1", "claw2", "claw3", "claw4"])
        chk("F.idle", idle and not (root / "proc").exists(), "4 users with linger markers and user units; fixture has no /proc, so no process evidence")
        op, wp = osq_paths(), wz_paths()
        chk("E.osquery_paths", "/usr/lib" in op and "/home/*/.npm-global/lib" in op and not any(".openclaw" in p for p in op), f"{len(op)} non-mac osquery roots parsed; ~/.openclaw absent")
        chk("E.wazuh_paths", "/usr/lib" in wp and "/home/*/.npm-global/lib" in wp and not any(".openclaw" in p for p in wp), f"{len(wp)} non-mac Wazuh roots parsed; ~/.openclaw absent")
        o, z, c = emulate(root, op, False), emulate(root, wp, True), clawscore(root)
        rel = {k: v[0] for k, v in LAYOUTS.items()}
        rows = []
        for lid, r in rel.items():
            rows.append((lid, o.get(r, "-") if r in o else "MISS", z.get(r) if r in z else "MISS", f"{c[r][0]} ({c[r][1]})" if r in c else "MISS"))
            print(f"ROW\t{lid}\tosquery={rows[-1][1] or '(empty)'}\twazuh={rows[-1][2]}\tclawscore={rows[-1][3]}\t{LAYOUTS[lid][2]}")
        chk("G1.osquery_sees_L1_L2", o.get(rel["L1"]) == VERSION and o.get(rel["L2"]) == VERSION, "osquery 5.23.1 default roots list L1 and L2 with version")
        chk("G2.wazuh_sees_L1_L2", z.get(rel["L1"]) == VERSION and z.get(rel["L2"]) == VERSION, "Wazuh 4.14.9 default roots list L1 and L2 with version")
        chk("G3.defaults_miss_L3", all(rel[x] not in o and rel[x] not in z for x in ("L3", "L3s")), "neither default list reaches ~/.openclaw/tools/node-v*/lib (install-cli.sh)")
        chk("G4.clawscore_all4", all(c.get(rel[x], ("",))[0] == VERSION for x in rel), "ClawScore reference finds L1, L2, L3, L3s with version 2026.4.15")
        chk("G5.L3s_from_build_info", c.get(rel["L3s"], ("", ""))[1] == "dist/build-info.json", "L3s version recovered from dist/build-info.json (package.json has none)")
        chk("G6.no_false_extra", set(c) == set(rel.values()), f"ClawScore found exactly {len(c)} installs")
    finally:
        if not keep: shutil.rmtree(root, ignore_errors=True)
    print("GATE " + ("PASS" if not fails else f"FAIL {fails}"))
    return 1 if fails else 0
if __name__ == "__main__": sys.exit(main())
