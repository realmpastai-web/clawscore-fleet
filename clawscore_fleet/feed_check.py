"""Read-only log of the newest OpenClaw GHSA on GitHub versus the pinned feed date.

This does not rewrite the pinned landscape, scan, or verify gates.
"""

from __future__ import annotations

import json
import re
import subprocess
import urllib.error
import urllib.request
from pathlib import Path

from clawscore_fleet.cves import in_range
from clawscore_fleet.ghsa_only import semver_events_cover
from clawscore_fleet.pkgmatch import is_openclaw_npm
from clawscore_fleet.versions import FEED_NEWEST, ROOT, contains_word_safe

EVIDENCE = ROOT / "evidence"
BRIEF = ROOT / "inputs" / "rea-brief-openclaw-latest"
COUNT_VERSIONS = ("2026.10.5", "2026.10.4", "2026.6.10", "2026.4.22")
QUERY = (
    "https://api.github.com/repos/openclaw/openclaw/security-advisories"
    "?state=published&per_page=100&sort=published&direction=desc"
)
GH_PATH = (
    "repos/openclaw/openclaw/security-advisories"
    "?state=published&per_page=100&sort=published&direction=desc"
)


class Offline(Exception):
    pass


def _clean(value: str) -> str:
    if contains_word_safe(value):
        return "[omitted]"
    return value


def _newest(rows: list) -> dict:
    chosen = None
    chosen_key = ""
    for row in rows:
        if not isinstance(row, dict):
            continue
        published = str(row.get("published_at") or "")
        ghsa_id = str(row.get("ghsa_id") or "")
        key = published + "\t" + ghsa_id
        if chosen is None or key > chosen_key:
            chosen = row
            chosen_key = key
    if chosen is None:
        raise Offline("advisory list was empty")
    return chosen


def _next_link(header: str) -> str | None:
    match = re.search(r'<([^>]+)>; rel="next"', header or "")
    return match.group(1) if match else None


def _from_urllib() -> tuple[str, list]:
    rows: list = []
    url: str | None = QUERY
    pages = 0
    try:
        while url and pages < 5:
            request = urllib.request.Request(
                url,
                headers={
                    "User-Agent": "clawscore-fleet-feed-check",
                    "Accept": "application/vnd.github+json",
                },
            )
            with urllib.request.urlopen(request, timeout=25) as response:
                payload = json.loads(response.read().decode("utf-8"))
                link = response.headers.get("Link") or ""
            if isinstance(payload, dict):
                message = str(payload.get("message") or "unexpected object")
                raise Offline(_clean(message)[:200])
            if not isinstance(payload, list):
                raise Offline("unexpected payload")
            rows.extend(item for item in payload if isinstance(item, dict))
            pages += 1
            last = str(payload[-1].get("published_at") or "")[:10] if payload else ""
            if not last or last <= FEED_NEWEST:
                break
            url = _next_link(link)
    except Offline:
        raise
    except urllib.error.HTTPError as exc:
        raise Offline(f"http {exc.code}") from exc
    except urllib.error.URLError as exc:
        raise Offline(f"url error {exc.reason}") from exc
    except (TimeoutError, json.JSONDecodeError, OSError) as exc:
        raise Offline(str(exc)) from exc
    if not rows:
        raise Offline("advisory list was empty")
    return "public advisories API", rows


def _from_gh() -> tuple[str, list]:
    try:
        proc = subprocess.run(
            ["gh", "api", GH_PATH, "-H", "Accept: application/vnd.github+json"],
            capture_output=True,
            text=True,
            timeout=60,
            check=False,
        )
    except (FileNotFoundError, subprocess.TimeoutExpired, OSError) as exc:
        raise Offline(str(exc)) from exc
    if proc.returncode != 0:
        detail = (proc.stderr or proc.stdout or "").strip().splitlines()
        message = detail[0] if detail else f"gh api exit {proc.returncode}"
        raise Offline(_clean(message)[:200])
    try:
        payload = json.loads(proc.stdout)
    except json.JSONDecodeError as exc:
        raise Offline("gh api returned non-json") from exc
    if not isinstance(payload, list):
        raise Offline("gh api returned an unexpected payload")
    return "gh api", [item for item in payload if isinstance(item, dict)]


def _pinned_lines() -> list[str]:
    lines = [f"pinned_feed_newest: {FEED_NEWEST}"]
    path = EVIDENCE / "verify-report.json"
    if not path.is_file():
        lines.append("verify_report_feed_newest: missing")
        return lines
    report = json.loads(path.read_text())
    lines.append(f"verify_report_feed_newest: {report.get('feed_newest')}")
    freshness = (report.get("gates") or {}).get("freshness") or {}
    lines.append(f"freshness_gate_feed_newest: {freshness.get('feed_newest')}")
    return lines


def _format(client: str, newest: dict) -> list[str]:
    published = str(newest.get("published_at") or "")
    day = published[:10]
    if len(day) == 10 and day > FEED_NEWEST:
        relation = "newer"
    elif day == FEED_NEWEST:
        relation = "same"
    elif len(day) == 10:
        relation = "older"
    else:
        relation = "undated"
    summary = _clean(str(newest.get("summary") or ""))
    return [
        f"client: {client}",
        f"query: {QUERY}",
        f"newest_ghsa: {_clean(str(newest.get('ghsa_id') or ''))}",
        f"newest_published: {_clean(published)}",
        f"newest_updated: {_clean(str(newest.get('updated_at') or ''))}",
        f"newest_severity: {_clean(str(newest.get('severity') or ''))}",
        f"newest_html_url: {_clean(str(newest.get('html_url') or ''))}",
        f"newest_summary: {summary}",
        f"comparison: {relation}",
        f"newest_date: {day}",
        f"pinned_date: {pinned_fetch_date()}",
    ]


def pinned_fetch_date() -> str:
    """Date of the frozen advisory fetch. The content newest date stays FEED_NEWEST."""
    return (BRIEF / "fetch-time-ist.txt").read_text().strip().split()[0]


def _openclaw_ranges(row: dict) -> list[str]:
    found = []
    ghsa_id = row.get("ghsa_id")
    for entry in row.get("vulnerabilities") or []:
        package = entry.get("package") or {}
        if not is_openclaw_npm(package, ghsa_id):
            continue
        rng = entry.get("vulnerable_version_range")
        if rng:
            found.append(str(rng))
    return found


def _covers_github(row: dict, version: str) -> bool:
    ranges = _openclaw_ranges(row)
    return bool(ranges) and any(in_range(version, rng) for rng in ranges)


def _covers_osv(row: dict, version: str) -> bool:
    if row.get("withdrawn"):
        return False
    for affected in row.get("affected") or []:
        if not isinstance(affected, dict):
            continue
        package = affected.get("package") or {}
        if not is_openclaw_npm(package, row.get("id")):
            continue
        for rng in affected.get("ranges") or []:
            if isinstance(rng, dict) and rng.get("type") == "SEMVER" and semver_events_cover(version, rng.get("events") or []):
                return True
    return False


def source_counts(versions: tuple[str, ...] = COUNT_VERSIONS) -> list[dict]:
    """GitHub DB / repo-only / OSV counts with withdrawn rows excluded."""
    global_rows = json.loads((BRIEF / "gh-global-openclaw.json").read_text())
    repo_rows = json.loads((BRIEF / "gh-repo-openclaw-published.json").read_text())
    osv_rows = json.loads((BRIEF / "osv-openclaw.json").read_text())
    global_ids = {row.get("ghsa_id") for row in global_rows}
    repo_only = [row for row in repo_rows if row.get("ghsa_id") not in global_ids]
    counted = []
    for version in versions:
        counted.append(
            {
                "version": version,
                "github_db": sum(1 for row in global_rows if not row.get("withdrawn_at") and _covers_github(row, version)),
                "repo_only": sum(1 for row in repo_only if not row.get("withdrawn_at") and _covers_github(row, version)),
                "osv": sum(1 for row in osv_rows if _covers_osv(row, version)),
            }
        )
    return counted


def version_count_lines() -> list[str]:
    lines = ["version_counts withdrawn_excluded=yes"]
    for row in source_counts():
        lines.append(
            f"{row['version']} github_db={row['github_db']} repo_only={row['repo_only']} osv={row['osv']}"
        )
    return lines


def _newer_rows(rows: list) -> list[dict]:
    found = []
    for row in rows:
        if not isinstance(row, dict):
            continue
        day = str(row.get("published_at") or "")[:10]
        if len(day) == 10 and day > FEED_NEWEST:
            found.append(row)
    return found


def evaluate() -> dict:
    """Compare the live repository advisory list with the pinned feed date.

    same -> pass. newer -> fail, and the rows are listed. offline -> pass is null.
    """
    lines = ["feed-check", *_pinned_lines()]
    try:
        try:
            client, rows = _from_urllib()
        except Offline:
            client, rows = _from_gh()
        newest = _newest(rows)
        lines.extend(_format(client, newest))
        lines.extend(version_count_lines())
        newer = _newer_rows(rows)
        for row in newer:
            day = str(row.get("published_at") or "")[:10]
            lines.append(
                "newer: "
                + _clean(str(row.get("ghsa_id") or ""))
                + " "
                + day
                + " "
                + _clean(str(row.get("severity") or ""))
            )
        relation = "newer" if newer else lines_relation(lines)
        status = relation if relation in {"same", "newer", "older", "undated"} else "offline"
        passed: bool | None = True if status == "same" else False
    except Offline as exc:
        lines.append("SKIP feed_check_same (offline)")
        lines.append("SKIP offline: " + _clean(str(exc)))
        status = "offline"
        passed = None
        newer = []
    text = "\n".join(lines) + "\n"
    if contains_word_safe(text):
        text = "\n".join([*lines[:3], "SKIP feed_check_same (offline)"]) + "\n"
        status = "offline"
        passed = None
    return {"status": status, "pass": passed, "text": text, "newer": len(newer)}


def lines_relation(lines: list[str]) -> str:
    for line in lines:
        if line.startswith("comparison: "):
            return line.split(": ", 1)[1].strip()
    return "offline"


def main() -> int:
    result = evaluate()
    print(result["text"], end="", flush=True)
    if result["status"] == "same":
        return 0
    if result["status"] == "offline":
        return 0
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
