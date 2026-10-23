#!/usr/bin/env python3
"""Compare scan-host on each lab container's docker export to evidence/scan.json.

Prints version, verdict, and ghsa_ids length for every claw-* install. Does not
print credential values. Exit 0 only when all 30 match.
"""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _compare(ident: str, want: dict) -> bool:
    with tempfile.TemporaryDirectory(prefix=f"hm-a6-{ident}-") as tmp:
        root = Path(tmp) / "root"
        out = Path(tmp) / "out"
        root.mkdir()
        export = subprocess.Popen(["docker", "export", ident], stdout=subprocess.PIPE)
        tar = subprocess.run(["tar", "-xf", "-", "-C", str(root)], stdin=export.stdout, check=False)
        if export.stdout is not None:
            export.stdout.close()
        export_rc = export.wait()
        if export_rc != 0 or tar.returncode != 0:
            err = (tar.stderr or b"")[:500]
            print(f"FAIL\t{ident}\texport={export_rc} tar={tar.returncode} {err!r}", flush=True)
            return False
        proc = subprocess.run(
            [sys.executable, "-m", "clawscore_fleet.cli", "scan-host", "--root", str(root), "--out", str(out)],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        if proc.returncode != 0:
            tail = (proc.stderr or proc.stdout or "").strip().splitlines()[-4:]
            print(f"FAIL\t{ident}\tscan-host exit={proc.returncode} {tail}", flush=True)
            return False
        document = json.loads((out / "scan.json").read_text())
        rows = document.get("installs") or []
        if len(rows) != 1:
            roots = [row.get("install_root") for row in rows]
            print(f"FAIL\t{ident}\tinstalls={len(rows)} roots={roots}", flush=True)
            return False
        got = rows[0]
        same = (
            got.get("version") == want.get("version")
            and got.get("verdict") == want.get("verdict")
            and got.get("ghsa_ids") == want.get("ghsa_ids")
        )
        print(
            ("PASS" if same else "FAIL")
            + f"\t{ident}\tverdict={got.get('verdict')} version={got.get('version')} "
            + f"ghsa={len(got.get('ghsa_ids') or [])} "
            + f"want {want.get('verdict')} {want.get('version')} {len(want.get('ghsa_ids') or [])}",
            flush=True,
        )
        if not same and got.get("ghsa_ids") != want.get("ghsa_ids"):
            print(
                f"\tghsa_len got={len(got.get('ghsa_ids') or [])} want={len(want.get('ghsa_ids') or [])}",
                flush=True,
            )
        return same


def main() -> int:
    scan = json.loads((ROOT / "evidence" / "scan.json").read_text())
    installs = scan.get("installs") or []
    fails = []
    print(f"installs {len(installs)}", flush=True)
    for item in installs:
        ident = item.get("id")
        if not isinstance(ident, str):
            fails.append(str(ident))
            print(f"FAIL\t{ident}\tmissing id", flush=True)
            continue
        if not _compare(ident, item):
            fails.append(ident)
    print(f"A6 {'PASS' if not fails else 'FAIL'} {len(installs) - len(fails)}/{len(installs)}", flush=True)
    if fails:
        print("failed " + " ".join(fails), flush=True)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
