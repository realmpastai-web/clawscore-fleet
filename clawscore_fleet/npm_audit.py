"""npm audit comparison. Port of inputs/rea-brief-npm-audit-gap/probe.py.

Live mode POSTs the endpoint npm audit uses (npm 12.2.0, audit-report.js):
  POST https://registry.npmjs.org/-/npm/v1/security/advisories/bulk
  body {"openclaw": ["<version>"]}

Offline mode re-scores saved response bytes and refuses a response whose sha256
does not match its meta file. This module does not install or run openclaw.
"""

from __future__ import annotations

import argparse
import datetime
import hashlib
import importlib.util
import json
import re
import urllib.request
from dataclasses import dataclass
from pathlib import Path

from clawscore_fleet.versions import FEED_NEWEST, ROOT

ENDPOINT = "https://registry.npmjs.org/-/npm/v1/security/advisories/bulk"
OPENCLAW_SOURCE = "https://github.com/openclaw/openclaw"
GHSA = re.compile(r"GHSA-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}")
ORACLE_PATH = ROOT / "inputs" / "rea-brief-npm-audit-gap" / "oracle.py"
FEED_PATH = ROOT / "evidence" / "landscape" / "ghsa-all.json"
GLOBAL_PATH = ROOT / "inputs" / "rea-brief-openclaw-latest" / "gh-global-openclaw.json"
SPLIT_PATH = ROOT / "evidence" / "npm-audit" / "split.json"
DAY = re.compile(r"\d{4}-\d{2}-\d{2}")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def request_body(version: str) -> bytes:
    return json.dumps({"openclaw": [version]}, separators=(",", ":")).encode()


@dataclass
class Context:
    oracle: object
    feed: list
    global_db: set[str]
    oracle_sha256: str
    feed_sha256: str
    global_db_sha256: str
    feed_newest: str


def load_oracle():
    spec = importlib.util.spec_from_file_location("hark_npm_audit_oracle", ORACLE_PATH)
    if spec is None or spec.loader is None:
        raise SystemExit(f"cannot load {ORACLE_PATH}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_context() -> Context:
    oracle = load_oracle()
    feed_bytes = FEED_PATH.read_bytes()
    global_bytes = GLOBAL_PATH.read_bytes()
    feed = json.loads(feed_bytes)
    global_db = {row["ghsa_id"] for row in json.loads(global_bytes)}
    return Context(
        oracle=oracle,
        feed=feed,
        global_db=global_db,
        oracle_sha256=sha256_bytes(ORACLE_PATH.read_bytes()),
        feed_sha256=sha256_bytes(feed_bytes),
        global_db_sha256=sha256_bytes(global_bytes),
        feed_newest=FEED_NEWEST,
    )


def clawscore_ids(oracle, feed, version: str) -> set[str]:
    return {ghsa_id for ghsa_id, _severity in oracle.advisories(feed, version)}


def classify(
    clawscore_ids: set[str], npm_ids: set[str], global_db: set[str]
) -> tuple[set[str], set[str], set[str], set[str]]:
    """Same split as probe.py. The parts of S are overlap, db_not_npm, and repo_only."""
    overlap = clawscore_ids & npm_ids
    db_not_npm = (clawscore_ids & global_db) - npm_ids
    repo_only = clawscore_ids - global_db
    npm_only = npm_ids - clawscore_ids
    return overlap, db_not_npm, repo_only, npm_only


def assert_disjoint(overlap: set[str], db_not_npm: set[str], repo_only: set[str], clawscore_n: int) -> None:
    if len(overlap) + len(db_not_npm) + len(repo_only) != clawscore_n:
        raise AssertionError(
            "overlap + db_not_npm + repo_only != clawscore "
            f"({len(overlap)} + {len(db_not_npm)} + {len(repo_only)} != {clawscore_n})"
        )


def source_histogram(feed: list, ids: set[str]) -> dict[str, int]:
    locs: dict[str, str] = {}
    for advisory in feed:
        ghsa_id = advisory.get("ghsa_id")
        if ghsa_id in ids and ghsa_id not in locs:
            locs[ghsa_id] = advisory.get("source_code_location") or ""
    hist: dict[str, int] = {}
    for loc in locs.values():
        hist[loc] = hist.get(loc, 0) + 1
    missing = len(ids - set(locs))
    if missing:
        hist[""] = hist.get("", 0) + missing
    return hist


def foreign_count(hist: dict[str, int]) -> int:
    return sum(count for loc, count in hist.items() if loc != OPENCLAW_SOURCE)


def format_source_line(version: str, ids: set[str], hist: dict[str, int]) -> str:
    ordered = {key: hist[key] for key in sorted(hist)}
    return f"{version} {len(ids)} {ordered} not_openclaw {foreign_count(ordered)}\n"


def sentence_for(row: dict, feed_newest: str) -> str:
    """Counts only. The second clause follows the source_code_location check."""
    day = str(row["npm_audit_date_utc"])[:10]
    if DAY.fullmatch(day) is None:
        raise SystemExit(f"npm query date is not YYYY-MM-DD: {row['npm_audit_date_utc']!r}")
    npm_audit = row["npm_audit"]
    clawscore = row["clawscore"]
    version = row["version"]
    if int(row["foreign_source_count"]) == 0:
        tail = f"the maker's repository lists {clawscore}"
    else:
        tail = f"the GitHub advisory database and the maker's repository list {clawscore}"
    return (
        f"npm audit returned {npm_audit} advisories for openclaw@{version} on {day}; "
        f"{tail} (feed newest {feed_newest})."
    )


def parse_npm_ids(data: bytes) -> tuple[set[str], int]:
    rows = json.loads(data).get("openclaw", [])
    ids = set()
    for row in rows:
        match = GHSA.search(str(row.get("url", "")))
        if not match:
            raise SystemExit(f"row without GHSA url: {row.get('id')}")
        ids.add(match.group(0))
    return ids, len(rows)


def load_response(raw: Path, version: str) -> tuple[bytes, dict]:
    data = (raw / f"resp-{version}.json").read_bytes()
    meta = json.loads((raw / f"meta-{version}.json").read_text())
    if sha256_bytes(data) != meta["response_sha256"]:
        raise SystemExit(f"raw response for {version} does not match its recorded sha256")
    return data, meta


def fetch(version: str, raw: Path) -> None:
    body = request_body(version)
    req = urllib.request.Request(
        ENDPOINT,
        data=body,
        method="POST",
        headers={"content-type": "application/json", "user-agent": "clawscore-npm-audit-probe/1"},
    )
    fetched = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")
    with urllib.request.urlopen(req, timeout=60) as response:
        data, status, server_date = response.read(), response.status, response.headers.get("Date")
    raw.mkdir(parents=True, exist_ok=True)
    (raw / f"req-{version}.json").write_bytes(body)
    (raw / f"resp-{version}.json").write_bytes(data)
    meta = {
        "endpoint": ENDPOINT,
        "fetched_utc": fetched,
        "method": "POST",
        "request_sha256": sha256_bytes(body),
        "response_bytes": len(data),
        "response_sha256": sha256_bytes(data),
        "server_date": server_date,
        "status": status,
        "version": version,
    }
    (raw / f"meta-{version}.json").write_text(json.dumps(meta, indent=1, sort_keys=True))


def score_versions(raw: Path, versions: list[str]) -> tuple[dict, str]:
    ctx = load_context()
    rows = []
    source_lines = []
    for version in versions:
        data, meta = load_response(raw, version)
        npm, nrows = parse_npm_ids(data)
        ids = clawscore_ids(ctx.oracle, ctx.feed, version)
        overlap, db_not_npm, repo_only, npm_only = classify(ids, npm, ctx.global_db)
        assert_disjoint(overlap, db_not_npm, repo_only, len(ids))
        hist = source_histogram(ctx.feed, ids)
        row = {
            "clawscore": len(ids),
            "db_not_npm": sorted(db_not_npm),
            "foreign_source_count": foreign_count(hist),
            "npm_audit": len(npm),
            "npm_audit_date_utc": meta["fetched_utc"],
            "npm_audit_rows": nrows,
            "npm_only": sorted(npm_only),
            "overlap": len(overlap),
            "repo_only": len(repo_only),
            "response_sha256": meta["response_sha256"],
            "server_date": meta["server_date"],
            "version": version,
        }
        row["sentence"] = sentence_for(row, ctx.feed_newest)
        rows.append(row)
        source_lines.append(format_source_line(version, ids, hist))
    result = {
        "feed_newest": ctx.feed_newest,
        "feed_sha256": ctx.feed_sha256,
        "global_db_sha256": ctx.global_db_sha256,
        "oracle_sha256": ctx.oracle_sha256,
        "versions": rows,
    }
    return result, "".join(source_lines)


def report_lines(row: dict) -> list[str]:
    db_ids = row["db_not_npm"]
    npm_only = row["npm_only"]
    probe = (
        f"{row['version']} npm_audit={row['npm_audit']} clawscore={row['clawscore']} = "
        f"overlap {row['overlap']} + db_not_npm {len(db_ids)} {db_ids} + "
        f"repo_only {row['repo_only']}; npm_only {len(npm_only)}"
    )
    compact = (
        f"{row['version']}: {row['npm_audit']} / {row['clawscore']} = "
        f"{row['overlap']} + {len(db_ids)} + {row['repo_only']}, npm-only {len(npm_only)}."
    )
    if db_ids:
        detail = (
            f"{row['version']}: {row['npm_audit']} / {row['clawscore']} = "
            f"{row['overlap']} + {len(db_ids)} ({', '.join(db_ids)}) + {row['repo_only']}, "
            f"npm-only {len(npm_only)}."
        )
    else:
        detail = compact
    lines = [probe, "  " + row["sentence"]]
    if detail != compact:
        lines.append(compact)
    lines.append(detail)
    return lines


def distinct_versions(scan: dict) -> list[str]:
    found: list[str] = []
    for item in scan.get("installs") or []:
        candidates = [str(version) for version in (item.get("candidates") or []) if version]
        if not candidates and item.get("version"):
            candidates = [str(item["version"])]
        for version in candidates:
            if version not in found:
                found.append(version)
    return found


def lab_versions() -> list[str]:
    scan = json.loads((ROOT / "evidence" / "scan.json").read_text())
    return distinct_versions(scan)


def versions_in_raw(raw: Path) -> list[str]:
    found = []
    for path in sorted(raw.glob("meta-*.json")):
        meta = json.loads(path.read_text())
        found.append(str(meta["version"]))
    if not found:
        raise SystemExit(f"no meta-*.json files in {raw}")
    return found


def load_npm_section(scan: dict, path: Path | None = None) -> dict | None:
    """Section rows for this scan. Absent when split.json is missing or incomplete."""
    split_path = SPLIT_PATH if path is None else path
    if not split_path.is_file():
        return None
    split = json.loads(split_path.read_text())
    versions = distinct_versions(scan)
    by_version = {row["version"]: row for row in split.get("versions") or []}
    if not versions or any(version not in by_version for version in versions):
        return None
    feed_newest = str(split["feed_newest"])
    rows = []
    for version in versions:
        source = by_version[version]
        row = {
            "clawscore": source["clawscore"],
            "db_not_npm": sorted(source["db_not_npm"]),
            "foreign_source_count": source["foreign_source_count"],
            "npm_audit": source["npm_audit"],
            "npm_audit_date_utc": source["npm_audit_date_utc"],
            "npm_only": sorted(source["npm_only"]),
            "overlap": source["overlap"],
            "repo_only": source["repo_only"],
            "version": source["version"],
        }
        row["sentence"] = sentence_for(row, feed_newest)
        rows.append(row)
    return {"feed_newest": feed_newest, "rows": rows}


def write_score(raw: Path, versions: list[str], out: Path) -> dict:
    result, source_log = score_versions(raw, versions)
    out.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(result, indent=1, sort_keys=True).encode()
    (out / "split.json").write_bytes(payload)
    (out / "source-check.log").write_text(source_log)
    for row in result["versions"]:
        for line in report_lines(row):
            print(line)
    print("split.json sha256", sha256_bytes(payload))
    return result


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="python3 -m clawscore_fleet.npm_audit")
    parser.add_argument("--live", action="store_true")
    parser.add_argument("--offline", metavar="RAW")
    parser.add_argument("--versions", nargs="+")
    parser.add_argument("--out")
    parser.add_argument("--print-versions", action="store_true")
    args = parser.parse_args(argv)
    if args.print_versions:
        print(" ".join(lab_versions()))
        return 0
    if args.live == bool(args.offline):
        raise SystemExit("choose one of --live or --offline")
    if args.live:
        if not args.out:
            raise SystemExit("--out is required with --live")
        if not args.versions:
            raise SystemExit("--versions is required with --live")
        out = Path(args.out)
        raw = out / "raw"
        for version in args.versions:
            fetch(version, raw)
        write_score(raw, list(args.versions), out)
        return 0
    raw = Path(args.offline)
    out = Path(args.out) if args.out else raw.parent
    versions = list(args.versions) if args.versions else versions_in_raw(raw)
    write_score(raw, versions, out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
