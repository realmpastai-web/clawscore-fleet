"""OpenClaw version ordering, the v0.1 seed table, and lab plan."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LANDSCAPE = ROOT / "evidence" / "landscape"

# Six historical lab releases kept as names. The v0.2 lab plan is LAB_PLAN.
LAB_VERSIONS = [
    "2026.4.15",
    "2026.4.20",
    "2026.4.21",
    "2026.4.22",
    "2026.4.23",
    "2026.10.4",
]

SEEDED_VERSIONS = ["2026.4.20", "2026.4.22", "2026.10.4"]
EXTRA_PRE_PATCH = "2026.4.15"
EXTRA_POST_PATCH = "2026.4.23"
PATCH_BOUNDARY = "2026.4.22"
PATCH_RELEASED = "2026-04-23"
OLD_BUILD_CUTOFF = "2026.3.31"
FEED_NEWEST = "2026-09-11"
NO_ADVISORY_WORDING = "no published advisory as of " + FEED_NEWEST

# 30 installs. At least eight predate 2026.3.31 and cover January, February, and March.
# 2026.4.7-1 and 2026.4.8 are the known fingerprint collision.
LAB_PLAN = [
    ("2026.1.29", 3),
    ("2026.2.14", 3),
    ("2026.3.28", 3),
    ("2026.4.7-1", 2),
    ("2026.4.8", 2),
    ("2026.4.15", 3),
    ("2026.4.20", 3),
    ("2026.4.21", 3),
    ("2026.4.22", 3),
    ("2026.4.23", 2),
    ("2026.10.4", 3),
]

SEED_FILES = [
    "package.json",
    "dist/cli.runtime.js",
    "dist/abort.runtime.js",
]

CORROBORATION_FILES = [
    "dist/abort.runtime.js",
    "dist/agent-runner.runtime.js",
    "dist/attempt-execution.runtime.js",
    "dist/audit.runtime.js",
    "dist/cli-runner.runtime.js",
    "dist/cli.runtime.js",
    "dist/command-config-resolution.runtime.js",
    "dist/commands-handlers.runtime.js",
    "dist/compact.runtime.js",
    "dist/gateway-rpc.runtime.js",
    "dist/lifecycle.runtime.js",
    "dist/register.runtime.js",
    "dist/reply.runtime.js",
    "dist/sessions.runtime.js",
    "dist/subagent-registry.runtime.js",
]

# Known-good sha256 values for the three seeded releases.
SEED_TABLE = {
    "2026.4.20": {
        "package.json": "618fe88b8b433221e700051b0058665e9d9dcee53ee806f3d96e57fac792d9d2",
        "dist/cli.runtime.js": "18aed5abc4a9b37d882e54d9200c74e2f1272b3802be826eba6c9669543ca49b",
        "dist/abort.runtime.js": "cf5ecb392c63f323a11050d722f34a57f97f78358a15ac27c40bd161fcae4cc9",
    },
    "2026.4.22": {
        "package.json": "29f6a6243f89cb256da7e85db22f8a7dc7903fb0538476f65f2b1ad0a409dd74",
        "dist/cli.runtime.js": "5ab9151b66271a28f165cd2cbe0ee11f1b82960956fb40d1e90bf2aa1d52a6b6",
        "dist/abort.runtime.js": "519e55aa702d002384fb100ca4dfbce6fa4170f44a046bf886091d12d24076cb",
    },
    "2026.10.4": {
        "package.json": "1ef9c6031d4789c57f1d7632d0b1c149d31e194b2a9441d93dcfc0010d8d74f6",
        "dist/cli.runtime.js": "bb479cc1662ad0c83aa8b0f9fec9627378d89a3b5d43cdb147cfc5c24f1b2c37",
        "dist/abort.runtime.js": "b4707d245e94b8eac1a9622ecdfcb6b3efb61ea1a42ae10a6b60e71bc4e0b1f6",
    },
}

FILE_READ_LIMIT = 20
ACCURACY_TARGET_PERCENT = 95
RECALL_TARGET_PERCENT = 90
MATRIX_RELEASE_COUNT = 117

_VERSION_RE = re.compile(
    r"^(\d+)\.(\d+)\.(\d+)(?:-(\d+))?(?:-(alpha|beta|rc)\.?(\d+))?$"
)
_STABLE_RE = re.compile(r"^\d+\.\d+\.\d+(?:-\d+)?$")
_PRERELEASE_RANK = {"alpha": 0, "beta": 1, "rc": 2}
# npm treats a comma or whitespace between comparators as AND. The whole string must be consumed.
_CMP = re.compile(r"\s*(<=|>=|<|>|=)\s*([^\s,]+)\s*,?")
_WORD_SAFE = re.compile(r"\bsafe\b", re.IGNORECASE)


class RangeSyntaxError(ValueError):
    """A vulnerable version range was not fully consumed by the comparator grammar."""


def hark_key(version: str) -> tuple[int, ...] | None:
    """Order shared with landscape recompute.

    Key is (major, minor, patch, 0 if a prerelease tag else 1, rank*1000+N, post).
    Rank is alpha=0, beta=1, rc=2. A numeric -N suffix sorts after the base release.
    Glued -beta3 equals -beta.3. Order: X-alpha.N < X-beta.N < X-rc.N < X < X-1.
    """
    match = _VERSION_RE.match(version.strip())
    if not match:
        return None
    major, minor, patch, post, tag, number = match.groups()
    rank = _PRERELEASE_RANK.get(tag, 0) * 1000 + int(number or 0)
    return (
        int(major),
        int(minor),
        int(patch),
        0 if tag else 1,
        rank,
        int(post or 0),
    )


def parse_comparators(rng: str) -> list[tuple[str, str]]:
    """Split a range into (operator, bound) pairs.

    Comparators are joined by a comma, whitespace, or both. A string that is not
    entirely comparators, or a bound this grammar rejects, is an error.
    """
    if not isinstance(rng, str) or rng == "":
        raise RangeSyntaxError(f"unparsed range {rng!r}")
    found: list[tuple[str, str]] = []
    pos = 0
    length = len(rng)
    while pos < length:
        match = _CMP.match(rng, pos)
        if match is None or match.end() == pos:
            raise RangeSyntaxError(f"unparsed range {rng!r}")
        operator, bound = match.group(1), match.group(2)
        if hark_key(bound) is None:
            raise RangeSyntaxError(f"unparsed bound {bound!r} in {rng!r}")
        found.append((operator, bound))
        pos = match.end()
    if not found:
        raise RangeSyntaxError(f"unparsed range {rng!r}")
    return found


def version_key(version: str) -> tuple[int, ...]:
    parsed = hark_key(version)
    if parsed is None:
        base = version.split("-", 1)[0]
        return tuple(int(part) for part in base.split("."))
    return parsed


def is_before(version: str, cutoff: str) -> bool:
    left = hark_key(version)
    right = hark_key(cutoff)
    if left is None or right is None:
        raise ValueError(f"unparsed version comparison {version} {cutoff}")
    return left < right


def load_published() -> dict[str, str]:
    payload = json.loads((LANDSCAPE / "versions.json").read_text())
    if not isinstance(payload, dict):
        raise SystemExit("versions.json is not an object")
    return {str(key): str(value) for key, value in payload.items()}


def stable_releases(published: dict[str, str] | None = None) -> list[str]:
    """117 stable releases: drop 0.0.1 and any alpha, beta, or rc tag. Keep numeric -N."""
    published = published if published is not None else load_published()
    found = []
    for version in published:
        if version == "0.0.1" or _STABLE_RE.match(version) is None:
            continue
        if hark_key(version) is None:
            continue
        found.append(version)
    found.sort(key=hark_key)
    return found


def contains_word_safe(text: str) -> bool:
    return _WORD_SAFE.search(text) is not None


def path_has_word_safe(path: str) -> bool:
    return contains_word_safe(path)
