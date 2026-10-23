"""Per-release gzip -n -9 shards of the matrix file listing.

A single gzip of listings.json is over 50 MB, so each release is stored as
evidence/matrix/listings/<version>.json.gz. Joining those payloads in
releases.json order reproduces the original listings.json bytes. The sha256
of those bytes is evidence/matrix/listings.sha256.
"""

from __future__ import annotations

import gzip
import hashlib
import json
import subprocess
from pathlib import Path

from clawscore_fleet.versions import ROOT

MATRIX = ROOT / "evidence" / "matrix"
LISTINGS_DIR = MATRIX / "listings"
SHA_PATH = MATRIX / "listings.sha256"
UNCOMPRESSED = MATRIX / "listings.json"
# 50 decimal MB, which is also under GitHub's 50 MiB warning.
MAX_GZIP_BYTES = 50_000_000


def is_listing_blob(path: Path) -> bool:
    """Uncompressed listing, or one gzip shard. The sha256 sidecar is neither."""
    if path.name == "listings.json":
        return True
    return path.parent.name == "listings" and path.name.endswith(".json.gz")


def gzip_n9(data: bytes) -> bytes:
    proc = subprocess.run(["gzip", "-n", "-9", "-c"], input=data, capture_output=True, check=True)
    return proc.stdout


def payload_for(files: list) -> bytes:
    return json.dumps(files, separators=(",", ":")).encode()


def assemble(versions: list[str], payloads: list[bytes]) -> bytes:
    parts = []
    for version, payload in zip(versions, payloads):
        parts.append(json.dumps(version).encode() + b":" + payload)
    return b"{" + b",".join(parts) + b"}\n"


def _shard_path(version: str) -> Path:
    if not version or version in {".", ".."} or "/" in version or "\\" in version:
        raise ValueError(f"unsafe listing version {version!r}")
    return LISTINGS_DIR / f"{version}.json.gz"


def _versions_from_releases() -> list[str]:
    payload = json.loads((MATRIX / "releases.json").read_text())
    return [row["version"] for row in payload["releases"]]


def recorded_sha256() -> str:
    if not SHA_PATH.is_file():
        raise SystemExit("evidence/matrix/listings.sha256 is missing")
    token = SHA_PATH.read_text().split()
    if not token or len(token[0]) != 64:
        raise SystemExit("evidence/matrix/listings.sha256 has no sha256")
    return token[0]


def listings_present() -> bool:
    if not SHA_PATH.is_file() or not (MATRIX / "releases.json").is_file():
        return False
    try:
        versions = _versions_from_releases()
    except (OSError, json.JSONDecodeError, KeyError, TypeError):
        return False
    return bool(versions) and all(_shard_path(version).is_file() for version in versions)


def read_payloads(versions: list[str] | None = None) -> tuple[list[str], list[bytes]]:
    if versions is None:
        versions = _versions_from_releases()
    payloads = []
    missing = []
    for version in versions:
        path = _shard_path(version)
        if not path.is_file():
            missing.append(version)
            continue
        payloads.append(gzip.decompress(path.read_bytes()))
    if missing:
        raise SystemExit("missing listing shards: " + ", ".join(missing))
    return versions, payloads


def decompressed_sha256(versions: list[str] | None = None) -> str:
    loaded_versions, payloads = read_payloads(versions)
    return hashlib.sha256(assemble(loaded_versions, payloads)).hexdigest()


def require_decompressed_sha256(versions: list[str] | None = None) -> str:
    digest = decompressed_sha256(versions)
    recorded = recorded_sha256()
    if digest != recorded:
        raise SystemExit(
            f"decompressed listings sha256 {digest} != evidence/matrix/listings.sha256 {recorded}"
        )
    return digest


def load_listings() -> dict:
    versions, payloads = read_payloads()
    digest = hashlib.sha256(assemble(versions, payloads)).hexdigest()
    recorded = recorded_sha256()
    if digest != recorded:
        raise SystemExit(
            f"decompressed listings sha256 {digest} != evidence/matrix/listings.sha256 {recorded}"
        )
    return {version: json.loads(payload) for version, payload in zip(versions, payloads)}


def write_payloads(versions: list[str], payloads: list[bytes]) -> str:
    if len(versions) != len(payloads):
        raise SystemExit("listing version count does not match payload count")
    assembled = assemble(versions, payloads)
    digest = hashlib.sha256(assembled).hexdigest()
    if UNCOMPRESSED.is_file():
        on_disk = hashlib.sha256(UNCOMPRESSED.read_bytes()).hexdigest()
        if on_disk != digest:
            raise SystemExit(
                f"refusing to replace listings.json; assembled sha256 {digest} != on-disk {on_disk}"
            )
    blobs = []
    for version, payload in zip(versions, payloads):
        blob = gzip_n9(payload)
        if len(blob) > MAX_GZIP_BYTES:
            raise SystemExit(f"{version} listing gzip is {len(blob)} bytes; limit is {MAX_GZIP_BYTES}")
        if gzip.decompress(blob) != payload:
            raise SystemExit(f"{version} listing gzip roundtrip mismatch")
        blobs.append(blob)
    SHA_PATH.write_text(f"{digest}  listings.json\n")
    LISTINGS_DIR.mkdir(parents=True, exist_ok=True)
    names = []
    for version, blob in zip(versions, blobs):
        path = _shard_path(version)
        path.write_bytes(blob)
        names.append(path.name)
    for stale in LISTINGS_DIR.glob("*.json.gz"):
        if stale.name not in names:
            stale.unlink()
    if decompressed_sha256(versions) != digest:
        raise SystemExit("listing shard readback sha256 mismatch")
    if UNCOMPRESSED.exists():
        UNCOMPRESSED.unlink()
    return digest
