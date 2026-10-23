"""Greedy file-set fingerprints for every stable release in the matrix."""

from __future__ import annotations

import bisect
import csv
import hashlib
import json
import re
from collections import defaultdict
from pathlib import Path

from clawscore_fleet.fingerprint import collision_groups, family_name, identify, load_db
from clawscore_fleet.listings_store import listings_present, load_listings
from clawscore_fleet.versions import (
    FEED_NEWEST,
    FILE_READ_LIMIT,
    ROOT,
    hark_key,
    path_has_word_safe,
)

EVIDENCE = ROOT / "evidence"
FINGERPRINTS = ROOT / "fingerprints"

_RUNTIME = re.compile(r"^dist/[^/]+\.runtime\.js$")
_HASHED = re.compile(r"-[A-Za-z0-9_]{8,}\.[A-Za-z0-9]+$")
PREFER = {
    "dist/.buildstamp": 0,
    "dist/build-info.json": 1,
    "dist/version.js": 2,
    "dist/cli.runtime.js": 3,
    "dist/abort.runtime.js": 4,
    "dist/entry.js": 5,
    "dist/index.js": 6,
    "openclaw.mjs": 7,
}


def _has(files: list[list[str]], rel: str) -> bool:
    names = [pair[0] for pair in files]
    index = bisect.bisect_left(names, rel)
    return index < len(names) and names[index] == rel


def _lookup_hash(files: list[list[str]], rel: str) -> str | None:
    names = [pair[0] for pair in files]
    index = bisect.bisect_left(names, rel)
    if index < len(names) and names[index] == rel:
        return files[index][1]
    return None


def _is_hashed(path: str) -> bool:
    base = path.rsplit("/", 1)[-1]
    match = _HASHED.search(base)
    if not match:
        return False
    token = match.group(0).split(".", 1)[0][1:]
    return any(char.isdigit() for char in token) and any(char.isalpha() for char in token)


def _allowed(path: str) -> bool:
    if path_has_word_safe(path) or path == "package.json":
        return False
    if "/node_modules/" in path or path.startswith("docs/") or path.startswith("skills/"):
        return False
    return True


def _percent(numerator: int, denominator: int) -> str:
    if denominator <= 0:
        return "0.0"
    scaled = (numerator * 1000) // denominator
    return f"{scaled // 10}.{scaled % 10}"


def _score(groups: dict) -> tuple[int, int]:
    sizes = [len(members) for members in groups.values()]
    separated = sum(size for size in sizes if size == 1)
    sumsq = sum(size * size for size in sizes)
    return separated, -sumsq


def _partition(versions: list[str], selected: list[str], indexes: dict[str, dict[str, str]]) -> dict:
    groups: dict[tuple, list[str]] = {}
    for version in versions:
        table = indexes[version]
        signature = tuple(table.get(path) for path in selected)
        groups.setdefault(signature, []).append(version)
    return groups


def _greedy(
    versions: list[str],
    candidates: list[str],
    indexes: dict[str, dict[str, str]],
    selected: list[str] | None = None,
) -> list[str]:
    chosen = list(selected or [])
    current = _partition(versions, chosen, indexes)
    current_score = _score(current)
    while len(chosen) < FILE_READ_LIMIT and current_score[0] < len(versions):
        best_path = None
        best_rank = None
        for path in candidates:
            if path in chosen:
                continue
            trial = _score(_partition(versions, chosen + [path], indexes))
            rank = (trial[0], trial[1], -PREFER.get(path, 100))
            if best_rank is None or rank > best_rank or (rank == best_rank and path < best_path):
                best_rank = rank
                best_path = path
        if best_path is None:
            break
        trial_score = (best_rank[0], best_rank[1])
        if trial_score <= current_score:
            break
        chosen.append(best_path)
        current_score = trial_score
    return chosen


def _indexes(raw: dict, versions: list[str], wanted: set[str]) -> dict[str, dict[str, str]]:
    indexes = {}
    for version in versions:
        table = {}
        for path, digest in raw[version]:
            if path in wanted:
                table[path] = digest
        indexes[version] = table
    return indexes


def _candidates(raw: dict, versions: list[str], family: str, hashed: bool) -> list[str]:
    found = set()
    for version in versions:
        for path, _digest in raw[version]:
            if not _allowed(path):
                continue
            if family == "runtime":
                if _RUNTIME.fullmatch(path):
                    found.add(path)
                continue
            hashed_name = _is_hashed(path)
            if hashed != hashed_name:
                continue
            if path == "openclaw.mjs" or path.startswith("dist/"):
                if hashed and path.count("/") != 1:
                    continue
                found.add(path)
    return sorted(found)


def _unresolved(versions: list[str], selected: list[str], indexes: dict[str, dict[str, str]]) -> list[list[str]]:
    groups = []
    for members in _partition(versions, selected, indexes).values():
        if len(members) > 1:
            members.sort(key=lambda version: hark_key(version) or (0,))
            groups.append(members)
    groups.sort(key=lambda item: hark_key(item[0]) or (0,))
    return groups


def _dirlist(raw: dict, versions: list[str]) -> dict:
    buckets: dict[str, list[str]] = defaultdict(list)
    for version in versions:
        digest = hashlib.sha256()
        for path, _file_hash in raw[version]:
            digest.update(path.encode())
            digest.update(b"\0")
        buckets[digest.hexdigest()].append(version)
    correct = 0
    collisions = []
    for members in buckets.values():
        if len(members) == 1:
            correct += 1
            continue
        clusters: list[list[str]] = []
        for version in members:
            paths = [pair[0] for pair in raw[version]]
            placed = False
            for cluster in clusters:
                if paths == [pair[0] for pair in raw[cluster[0]]]:
                    cluster.append(version)
                    placed = True
                    break
            if not placed:
                clusters.append([version])
        for cluster in clusters:
            if len(cluster) == 1:
                correct += 1
            else:
                cluster.sort(key=lambda version: hark_key(version) or (0,))
                collisions.append(cluster)
    collisions.sort(key=lambda item: hark_key(item[0]) or (0,))
    total = len(versions)
    return {
        "feed_newest": FEED_NEWEST,
        "correct": correct,
        "total": total,
        "accuracy_display": _percent(correct, total),
        "listing_collision_groups": len(collisions),
        "listing_collisions": collisions,
    }


def build() -> dict:
    raw = load_listings()
    versions = sorted(raw, key=lambda version: hark_key(version) or (0,))
    families: dict[str, list[str]] = defaultdict(list)
    for version in versions:
        present = {mark for mark in ("dist/cli.runtime.js", "dist/abort.runtime.js", "dist/.buildstamp") if _has(raw[version], mark)}
        families[family_name(present)].append(version)

    family_meta = {}
    version_rows = {}
    for family in ("runtime", "buildstamp", "early"):
        members = families.get(family) or []
        if not members:
            family_meta[family] = {"files": [], "versions": 0, "unresolved": []}
            continue
        if family == "runtime":
            wanted = set(_candidates(raw, members, family, hashed=False))
            indexes = _indexes(raw, members, wanted)
            selected = _greedy(members, sorted(wanted), indexes)
        else:
            wanted = set(_candidates(raw, members, family, hashed=False))
            indexes = _indexes(raw, members, wanted)
            selected = _greedy(members, sorted(wanted), indexes)
            if _unresolved(members, selected, indexes):
                extra = set(_candidates(raw, members, family, hashed=True))
                indexes_extra = _indexes(raw, members, wanted | extra)
                indexes = indexes_extra
                selected = _greedy(members, sorted(wanted | extra), indexes, selected)
        unresolved = _unresolved(members, selected, indexes)
        family_meta[family] = {
            "files": selected,
            "versions": len(members),
            "unresolved": unresolved,
        }
        for version in members:
            table = indexes[version]
            version_rows[version] = {
                "family": family,
                "files": {path: table.get(path) for path in selected},
            }
        print(
            f"family {family} versions {len(members)} files {len(selected)} "
            f"unresolved {len(unresolved)}",
            flush=True,
        )
        for path in selected:
            print(f"  file {path}", flush=True)

    db = {
        "feed_newest": FEED_NEWEST,
        "read_limit": FILE_READ_LIMIT,
        "families": {
            "runtime": {
                "requires_all": ["dist/cli.runtime.js", "dist/abort.runtime.js"],
                "files": family_meta["runtime"]["files"],
            },
            "buildstamp": {
                "requires_all": ["dist/.buildstamp"],
                "files": family_meta["buildstamp"]["files"],
            },
            "early": {
                "requires_all": [],
                "files": family_meta["early"]["files"],
            },
        },
        "versions": version_rows,
    }
    FINGERPRINTS.mkdir(parents=True, exist_ok=True)
    (FINGERPRINTS / "db.json").write_text(json.dumps(db, indent=2, sort_keys=True) + "\n")
    stale = FINGERPRINTS / "corroborate.json"
    if stale.exists():
        stale.unlink()

    rows = []
    for version in versions:
        result = identify(
            [pair[0] for pair in raw[version]],
            lambda rels, files=raw[version]: {rel: _lookup_hash(files, rel) for rel in rels},
            db,
        )
        rows.append(
            {
                "version": version,
                "predicted": result["version"] or "",
                "verdict": result["verdict"],
                "candidates": "|".join(result["candidates"]),
                "reads": result["reads"],
            }
        )
    groups = collision_groups(db)
    dirlist = _dirlist(raw, versions)
    fingerprint_set = {
        "feed_newest": FEED_NEWEST,
        "read_limit": FILE_READ_LIMIT,
        "families": [
            {
                "name": family,
                "files": family_meta[family]["files"],
                "reads": len(family_meta[family]["files"]),
                "versions": family_meta[family]["versions"],
                "unresolved": family_meta[family]["unresolved"],
            }
            for family in ("runtime", "buildstamp", "early")
        ],
    }
    EVIDENCE.mkdir(parents=True, exist_ok=True)
    (EVIDENCE / "fingerprint-set.json").write_text(
        json.dumps(fingerprint_set, indent=2, sort_keys=True) + "\n"
    )
    (EVIDENCE / "collisions.json").write_text(
        json.dumps(
            {"feed_newest": FEED_NEWEST, "count": len(groups), "groups": groups},
            indent=2,
            sort_keys=True,
        )
        + "\n"
    )
    (EVIDENCE / "dirlist-metric.json").write_text(json.dumps(dirlist, indent=2, sort_keys=True) + "\n")
    with (EVIDENCE / "matrix-confusion.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=["version", "predicted", "verdict", "candidates", "reads"],
        )
        writer.writeheader()
        writer.writerows(rows)
    print(f"collisions {len(groups)}", flush=True)
    for group in groups:
        print("  group " + ",".join(group), flush=True)
    print(
        f"dirlist {dirlist['correct']} of {dirlist['total']} ({dirlist['accuracy_display']}%)",
        flush=True,
    )
    return {"db": db, "rows": rows, "groups": groups, "dirlist": dirlist}


def main() -> int:
    if not listings_present():
        raise SystemExit("evidence/matrix/listings shards are missing; run make matrix")
    build()
    db = load_db()
    print(f"wrote fingerprints for {len(db['versions'])} versions", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
