"""Fetch the 117 stable OpenClaw tarballs and record per-file sha256 listings."""

from __future__ import annotations

import gzip
import hashlib
import json
import os
import subprocess
import tarfile
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path

from clawscore_fleet.listings_store import _shard_path, payload_for, write_payloads
from clawscore_fleet.versions import FEED_NEWEST, ROOT, hark_key, load_published, stable_releases

EVIDENCE = ROOT / "evidence"
MATRIX = EVIDENCE / "matrix"
CACHE = ROOT / ".cache" / "tarballs"
PARTS = ROOT / ".cache" / "listing-parts"
WORKERS = 3


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _listing(tarball: Path) -> list[list[str]]:
    files: list[list[str]] = []
    with tarfile.open(tarball, "r:*") as handle:
        for member in handle:
            if not member.isfile():
                continue
            name = member.name
            if name.startswith("package/"):
                name = name[len("package/") :]
            if not name or name.endswith("/") or ".." in name.split("/"):
                continue
            extracted = handle.extractfile(member)
            if extracted is None:
                continue
            files.append([name, hashlib.sha256(extracted.read()).hexdigest()])
    files.sort()
    return files


def _pack(version: str, destination: Path) -> Path:
    destination.mkdir(parents=True, exist_ok=True)
    print(f"npm pack openclaw@{version}", flush=True)
    proc = subprocess.run(
        ["npm", "pack", f"openclaw@{version}", "--silent", "--pack-destination", str(destination)],
        capture_output=True,
        text=True,
        check=False,
    )
    if proc.stdout:
        print(proc.stdout, end="" if proc.stdout.endswith("\n") else "\n", flush=True)
    if proc.returncode != 0:
        detail = (proc.stderr or "") + (proc.stdout or "")
        raise RuntimeError(f"npm pack openclaw@{version} failed\n{detail}")
    name = proc.stdout.strip().splitlines()[-1].strip() if proc.stdout.strip() else ""
    candidate = destination / name if name else None
    if candidate is not None and candidate.is_file():
        return candidate
    matches = sorted(destination.glob(f"openclaw-{version}.tgz"))
    if len(matches) == 1:
        return matches[0]
    raise RuntimeError(f"npm pack openclaw@{version} produced {matches} stdout={proc.stdout!r}")


def process_version(version: str) -> dict:
    PARTS.mkdir(parents=True, exist_ok=True)
    CACHE.mkdir(parents=True, exist_ok=True)
    part_path = PARTS / f"{version}.json"
    tarball = CACHE / f"openclaw-{version}.tgz"
    if part_path.is_file() and tarball.is_file():
        part = json.loads(part_path.read_text())
        if part.get("version") == version and part.get("files") and part.get("sha256"):
            print(f"cached {version} files {len(part['files'])}", flush=True)
            return {
                "version": version,
                "sha256": part["sha256"],
                "filename": tarball.name,
                "files": len(part["files"]),
                "cached": True,
            }
    if not tarball.is_file():
        packed = _pack(version, CACHE)
        if packed.resolve() != tarball.resolve():
            packed.replace(tarball)
    digest = _sha256_file(tarball)
    files = _listing(tarball)
    part_path.write_text(
        json.dumps({"version": version, "sha256": digest, "filename": tarball.name, "files": files})
    )
    print(f"listed {version} files {len(files)} sha256 {digest}", flush=True)
    return {
        "version": version,
        "sha256": digest,
        "filename": tarball.name,
        "files": len(files),
        "cached": False,
    }


def _preserved_listings(stable: set[str]) -> dict[str, tuple[bytes, dict]]:
    """Shards already in the store for versions outside the landscape stable set.

    make matrix rebuilds the landscape releases. These rows stay without another
    pack step, so the next listing is a store file rather than a version branch
    in the fingerprint builder.
    """
    path = MATRIX / "releases.json"
    if not path.is_file():
        return {}
    payload = json.loads(path.read_text())
    kept: dict[str, tuple[bytes, dict]] = {}
    for row in payload.get("releases") or []:
        version = row.get("version")
        if not isinstance(version, str) or not version or version in stable:
            continue
        shard = _shard_path(version)
        if not shard.is_file():
            continue
        kept[version] = (gzip.decompress(shard.read_bytes()), row)
    return kept


def _write_assembled(
    versions: list[str],
    published: dict[str, str],
    preserved: dict[str, tuple[bytes, dict]] | None = None,
) -> None:
    preserved = preserved or {}
    MATRIX.mkdir(parents=True, exist_ok=True)
    releases = []
    sha_lines = []
    payloads: list[bytes] = []
    for version in versions:
        if version in preserved:
            payload_bytes, row = preserved[version]
            releases.append(row)
            sha_lines.append(f"{row['sha256']}  {row['tarball']}")
            payloads.append(payload_bytes)
            continue
        part = json.loads((PARTS / f"{version}.json").read_text())
        releases.append(
            {
                "version": version,
                "published": published.get(version, ""),
                "tarball": part["filename"],
                "sha256": part["sha256"],
                "files": len(part["files"]),
            }
        )
        sha_lines.append(f"{part['sha256']}  {part['filename']}")
        payloads.append(payload_for(part["files"]))
    write_payloads(versions, payloads)
    (MATRIX / "releases.json").write_text(
        json.dumps(
            {"count": len(releases), "feed_newest": FEED_NEWEST, "releases": releases},
            indent=2,
            sort_keys=True,
        )
        + "\n"
    )
    (MATRIX / "tarballs.sha256").write_text("\n".join(sha_lines) + "\n")


def main() -> int:
    published = load_published()
    versions = stable_releases(published)
    preserved = _preserved_listings(set(versions))
    print(f"stable releases {len(versions)}", flush=True)
    if preserved:
        print("preserved listings " + ",".join(sorted(preserved, key=lambda item: hark_key(item) or (0,))), flush=True)
    PARTS.mkdir(parents=True, exist_ok=True)
    failures = []
    workers = int(os.environ.get("CLAWSCORE_MATRIX_WORKERS", str(WORKERS)))
    with ProcessPoolExecutor(max_workers=workers) as pool:
        future_map = {pool.submit(process_version, version): version for version in versions}
        for future in as_completed(future_map):
            version = future_map[future]
            try:
                future.result()
            except Exception as exc:
                text = f"{version}\n{exc}"
                print(text, flush=True)
                failures.append(text)
    if failures:
        (MATRIX / "pack-failures.log").write_text("\n\n".join(failures) + "\n")
    else:
        failure_path = MATRIX / "pack-failures.log"
        if failure_path.exists():
            failure_path.unlink()
    ready = [version for version in versions if (PARTS / f"{version}.json").is_file()]
    combined = list(ready)
    for version in preserved:
        if version not in combined:
            combined.append(version)
    combined.sort(key=lambda version: hark_key(version) or (0,))
    _write_assembled(combined, published, preserved)
    print(f"matrix releases {len(ready)} of {len(versions)} failures {len(failures)}", flush=True)
    return 0 if len(ready) == len(versions) and not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
