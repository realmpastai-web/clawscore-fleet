#!/usr/bin/env python3
"""Regenerate idle-Linux REA lists from an extracted openclaw package tree.

Static reads only: dist/*.js basenames, CHANGELOG GHSA ids, package.json
keys, and the build-info files. This script does not import or execute the
package.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from pathlib import Path

GHSA_RE = re.compile(r"GHSA-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}")


def version_probe(package_json: Path) -> str:
    payload = json.loads(package_json.read_text(encoding="utf-8"))
    lines = [
        "has_version_field: " + str("version" in payload),
        "version_value: " + repr(payload.get("version")),
        "has_gitHead: " + str("gitHead" in payload),
        "gitHead: " + repr(payload.get("gitHead")),
        "name: " + repr(payload.get("name")),
        "bin: " + repr(payload.get("bin")),
        "main: " + repr(payload.get("main")),
    ]
    return "\n".join(lines) + "\n"


def regenerate(package: Path, out: Path) -> dict:
    dist = package / "dist"
    if not dist.is_dir():
        raise SystemExit(f"missing dist directory: {dist}")
    changelog_path = package / "CHANGELOG.md"
    package_json = package / "package.json"
    build_info = dist / "build-info.json"
    buildstamp = dist / ".buildstamp"
    for path in (changelog_path, package_json, build_info, buildstamp):
        if not path.is_file():
            raise SystemExit(f"missing {path}")
    names = sorted(path.name for path in dist.glob("*.js") if path.is_file())
    changelog = changelog_path.read_text(encoding="utf-8", errors="replace")
    ids = sorted(set(GHSA_RE.findall(changelog)))
    probe = version_probe(package_json)
    out.mkdir(parents=True, exist_ok=True)
    (out / "dist-names-2026.4.15.txt").write_text("\n".join(names) + "\n")
    (out / "changelog-ghsa-2026.4.15.txt").write_text("\n".join(ids) + ("\n" if ids else ""))
    (out / "package-json-version.txt").write_text(probe)
    shutil.copyfile(build_info, out / "build-info.json")
    shutil.copyfile(buildstamp, out / "buildstamp")
    return {
        "dist_js": len(names),
        "changelog_ghsa": len(ids),
        "package_json_has_version": "version" in json.loads(package_json.read_text(encoding="utf-8")),
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Regenerate idle-Linux REA lists from an extracted tarball")
    parser.add_argument("--package", required=True, type=Path, help="extracted package directory")
    parser.add_argument("--out", required=True, type=Path, help="directory for the regenerated lists")
    args = parser.parse_args(argv)
    result = regenerate(args.package, args.out)
    sys.stdout.write(json.dumps(result) + "\n")
    sys.stdout.write((args.out / "package-json-version.txt").read_text(encoding="utf-8"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
