"""Identify an OpenClaw install from a family fingerprint. Shared signatures stay a range."""

from __future__ import annotations

import json
from pathlib import Path

from clawscore_fleet.versions import FILE_READ_LIMIT, ROOT, hark_key

DB_PATH = ROOT / "fingerprints" / "db.json"


class ReadLimitError(RuntimeError):
    pass


def family_name(paths: set[str]) -> str:
    if "dist/cli.runtime.js" in paths and "dist/abort.runtime.js" in paths:
        return "runtime"
    if "dist/.buildstamp" in paths:
        return "buildstamp"
    return "early"


def load_db(path: Path | None = None) -> dict:
    return json.loads((path or DB_PATH).read_text())


def match_signature(db: dict, family: str, hashes: dict[str, str | None]) -> list[str]:
    files = list(db["families"][family]["files"])
    hits = []
    for version, row in db["versions"].items():
        if row.get("family") != family:
            continue
        stored = row.get("files") or {}
        if all(stored.get(rel) == hashes.get(rel) for rel in files):
            hits.append(version)
    hits.sort(key=lambda version: hark_key(version) or (0,))
    return hits


def identify(paths: list[str], fetch, db: dict) -> dict:
    """fetch(rels) -> {rel: sha256 or None}. Missing files are not counted as reads."""
    family = family_name(set(paths))
    if family not in db["families"]:
        family = "early"
    files = list(db["families"][family]["files"])
    fetched = fetch(files)
    read = [rel for rel in files if fetched.get(rel)]
    if len(read) > FILE_READ_LIMIT:
        raise ReadLimitError(f"read {len(read)} files")
    hits = match_signature(db, family, fetched)
    if len(hits) == 1:
        verdict = "exact"
        version = hits[0]
    elif len(hits) > 1:
        verdict = "range"
        version = None
    else:
        verdict = "unknown"
        version = None
    return {
        "family": family,
        "verdict": verdict,
        "version": version,
        "candidates": hits,
        "files_read": read,
        "reads": len(read),
        "matched_files": list(files) if verdict != "unknown" else [],
    }


def collision_groups(db: dict) -> list[list[str]]:
    grouped: dict[tuple, list[str]] = {}
    for version, row in db["versions"].items():
        files = db["families"][row["family"]]["files"]
        signature = (row["family"], tuple(row["files"].get(rel) for rel in files))
        grouped.setdefault(signature, []).append(version)
    groups = []
    for versions in grouped.values():
        if len(versions) < 2:
            continue
        versions.sort(key=lambda version: hark_key(version) or (0,))
        groups.append(versions)
    groups.sort(key=lambda item: hark_key(item[0]) or (0,))
    return groups
