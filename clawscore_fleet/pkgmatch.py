"""Whether an advisory package row is npm openclaw, or a cited keep-list id.

See docs/package-matching.md. The keep-list is read on each call.
"""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
KEEP_PATH = ROOT / "data" / "non-npm-keep.tsv"


def keep_ids() -> set[str]:
    """Data rows of data/non-npm-keep.tsv. An empty file yields an empty set."""
    found: set[str] = set()
    if not KEEP_PATH.is_file():
        return found
    for line in KEEP_PATH.read_text().splitlines():
        text = line.strip()
        if not text or text.startswith("#"):
            continue
        ghsa_id, _sep, _rest = text.partition("\t")
        if ghsa_id == "ghsa_id" or not ghsa_id:
            continue
        found.add(ghsa_id)
    return found


def is_openclaw_npm(package: object, ghsa_id: object) -> bool:
    """True for npm openclaw (any name case) or a ghsa_id on the keep-list."""
    if ghsa_id is not None and str(ghsa_id) in keep_ids():
        return True
    if not isinstance(package, dict):
        return False
    name = package.get("name")
    ecosystem = package.get("ecosystem")
    if not isinstance(name, str) or not isinstance(ecosystem, str):
        return False
    return name.casefold() == "openclaw" and ecosystem.casefold() == "npm"
