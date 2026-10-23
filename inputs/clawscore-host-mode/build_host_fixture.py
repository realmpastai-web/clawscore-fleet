#!/usr/bin/env python3
"""Build the host-mode fixture root from 4 public npm tarballs (frozen by Hark 2026-10-18).

  python3 build_host_fixture.py <out_root> [--cache DIR]

Tarballs are fetched from registry.npmjs.org only if not in --cache, and every one must match
the sha512 integrity pinned in sources/npm-openclaw-pins.json, or the build aborts. Nothing is executed.
"""
import base64, hashlib, io, json, os, shutil, sys, tarfile, urllib.request
from pathlib import Path

H = Path(__file__).resolve().parent
PINS = json.loads((H / "sources" / "npm-openclaw-pins.json").read_text())["versions"]
CANARY = "hark-canary-7f3e1c-NOT-A-REAL-TOKEN"

# id -> (version, install dir relative to root, package.json version override or None)
LAYOUT = {
    "H1": ("2026.10.4", "usr/lib/node_modules/openclaw", None),
    "H2": ("2026.4.15", "root/.npm-global/lib/node_modules/openclaw", None),
    "H3": ("2026.1.29", "home/alice/.openclaw/tools/node-v22.22.0/lib/node_modules/openclaw", None),
    "H4": ("2026.10.10-beta.1", "opt/openclaw-beta/lib/node_modules/openclaw", None),
    "H5": ("2026.1.29", "home/bob/.npm-global/lib/node_modules/openclaw", "2026.10.4"),
}


def tarball(version: str, cache: Path) -> bytes:
    pin = PINS[version]
    path = cache / Path(pin["tarball"]).name
    if not path.is_file():
        cache.mkdir(parents=True, exist_ok=True)
        with urllib.request.urlopen(pin["tarball"], timeout=300) as r:
            path.write_bytes(r.read())
    data = path.read_bytes()
    got = "sha512-" + base64.b64encode(hashlib.sha512(data).digest()).decode()
    if got != pin["integrity"]:
        raise SystemExit(f"integrity mismatch for {version}: {got}")
    return data


def extract(data: bytes, dest: Path) -> None:
    with tarfile.open(fileobj=io.BytesIO(data), mode="r:gz") as tf:
        for m in tf.getmembers():
            if not m.isfile() or not m.name.startswith("package/") or ".." in Path(m.name).parts:
                continue
            out = dest / m.name[len("package/"):]
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_bytes(tf.extractfile(m).read())


def build(root: Path, cache: Path) -> dict:
    if root.exists():
        shutil.rmtree(root)
    for hid, (version, rel, override) in LAYOUT.items():
        dest = root / rel
        extract(tarball(version, cache), dest)
        if override:
            pj = json.loads((dest / "package.json").read_text())
            pj["version"] = override
            (dest / "package.json").write_text(json.dumps(pj, indent=2) + "\n")
    # H2 runs as root under systemd --user with linger (same shape as inputs/clawscore-root-owner).
    unit_dir = root / "root/.config/systemd/user"
    unit_dir.mkdir(parents=True)
    install = "/" + LAYOUT["H2"][1]
    (unit_dir / "openclaw-gateway.service").write_text(
        "[Unit]\nDescription=OpenClaw gateway\n\n[Service]\n"
        f"WorkingDirectory={install}\nExecStart=/usr/bin/node {install}/openclaw.mjs gateway\n\n"
        "[Install]\nWantedBy=default.target\n")
    (unit_dir / "default.target.wants").mkdir()
    os.symlink("../openclaw-gateway.service", unit_dir / "default.target.wants/openclaw-gateway.service")
    (root / "var/lib/systemd/linger").mkdir(parents=True)
    (root / "var/lib/systemd/linger/root").write_text("")
    # Credential canary: host mode may report the NAME, never the value.
    cfg = root / "root/.openclaw"
    cfg.mkdir(parents=True)
    (cfg / "openclaw.json").write_text(json.dumps({"env": {"OPENAI_API_KEY": CANARY}}, indent=2) + "\n")
    return {hid: {"version": v, "install_root": "/" + rel, "declared_version": o or v} for hid, (v, rel, o) in LAYOUT.items()}


def manifest(root: Path) -> dict:
    out = {}
    for p in sorted(root.rglob("*")):
        rel = str(p.relative_to(root))
        if p.is_symlink():
            out[rel] = "link:" + os.readlink(p)
        elif p.is_file():
            out[rel] = hashlib.sha256(p.read_bytes()).hexdigest()
    return out


if __name__ == "__main__":
    args = sys.argv[1:]
    cache = Path(args[args.index("--cache") + 1]) if "--cache" in args else Path.home() / ".cache" / "clawscore-host-fixture"
    print(json.dumps(build(Path(args[0]), cache), indent=1, sort_keys=True))
