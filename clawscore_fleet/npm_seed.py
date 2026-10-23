"""Download OpenClaw tarballs and hash the seed and corroboration files."""

from __future__ import annotations

import hashlib
import subprocess
import sys
import tarfile
import tempfile
from pathlib import Path

from clawscore_fleet.versions import CORROBORATION_FILES, LAB_VERSIONS, SEED_FILES, SEED_TABLE


def _members() -> list[str]:
    seen: list[str] = []
    for rel in [*SEED_FILES, *CORROBORATION_FILES]:
        if rel not in seen:
            seen.append(rel)
    return seen


def hash_tarball(tarball: Path) -> dict[str, str]:
    wanted = _members()
    found: dict[str, str] = {}
    with tarfile.open(tarball) as handle:
        for rel in wanted:
            member = f"package/{rel}"
            try:
                extracted = handle.extractfile(member)
            except KeyError as exc:
                raise SystemExit(f"missing {member} in {tarball.name}") from exc
            if extracted is None:
                raise SystemExit(f"missing {member} in {tarball.name}")
            found[rel] = hashlib.sha256(extracted.read()).hexdigest()
    return found


def fetch_hashes(versions: list[str] | None = None) -> dict[str, dict[str, str]]:
    versions = list(versions or LAB_VERSIONS)
    hashed: dict[str, dict[str, str]] = {}
    with tempfile.TemporaryDirectory(prefix="clawscore-npm-") as tmp:
        work = Path(tmp)
        for version in versions:
            print(f"npm pack openclaw@{version}", flush=True)
            subprocess.run(
                ["npm", "pack", f"openclaw@{version}", "--silent"],
                cwd=work,
                check=True,
            )
            matches = list(work.glob(f"openclaw-{version}.tgz"))
            if len(matches) != 1:
                raise SystemExit(f"expected one tarball for {version}, found {matches}")
            hashed[version] = hash_tarball(matches[0])
            matches[0].unlink()
    return hashed


def seed_mismatches(hashes: dict[str, dict[str, str]]) -> list[str]:
    errors = []
    for version, files in SEED_TABLE.items():
        for rel, expected in files.items():
            got = hashes.get(version, {}).get(rel)
            if got != expected:
                errors.append(
                    "SEED MISMATCH "
                    f"{version} {rel}\n  expected {expected}\n  got      {got}"
                )
            else:
                print(f"seed OK {version} {rel} {got}", flush=True)
    return errors


def die_on_seed_mismatch(hashes: dict[str, dict[str, str]]) -> None:
    errors = seed_mismatches(hashes)
    if errors:
        print("FINGERPRINT SEED CHECK FAILED", file=sys.stderr)
        for error in errors:
            print(error, file=sys.stderr)
        raise SystemExit(1)
