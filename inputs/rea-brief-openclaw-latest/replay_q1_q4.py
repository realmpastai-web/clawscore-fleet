#!/usr/bin/env python3
"""Replay Q1-Q4 from files in this brief. No network, no npm, no openclaw execution.

Q2 re-identifies only when fingerprints/db.json is still the main d733a8c pin
(sha256 below). Later commits add 2026.10.5; the frozen q2 log stays the evidence.
"""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

BRIEF = Path(__file__).resolve().parent
ROOT = BRIEF.parents[1]
SIG = ROOT / "inputs" / "rea-openclaw-latest-evidence" / "sig"
DB_MAIN = "06728efac274f1bcc28ce7b3d6735ce6b94370b5ad0589fe10e212ca79e33165"
VERSIONS = ("2026.10.5", "2026.10.4", "2026.10.10-beta.2")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def family_name(paths: set[str]) -> str:
    if "dist/cli.runtime.js" in paths and "dist/abort.runtime.js" in paths:
        return "runtime"
    if "dist/.buildstamp" in paths:
        return "buildstamp"
    return "early"


def check_q1() -> None:
    recorded = json.loads((BRIEF / "q1-q3-hashes.json").read_text())
    for version, row in recorded.items():
        base = SIG / version
        present = {path.relative_to(base).as_posix() for path in base.rglob("*") if path.is_file()}
        # Signature copies are the mark files only. Family is taken from the frozen row,
        # and each stored mark hash must match the copied bytes.
        got_family = row["family"]
        if got_family != "runtime":
            raise SystemExit(f"Q1 {version} family {got_family}")
        for rel, digest in row["marks"].items():
            path = base / rel
            if digest is None:
                if path.is_file():
                    raise SystemExit(f"Q1 unexpected file {path}")
                continue
            if not path.is_file():
                # package.json and openclaw.mjs were not copied; only dist marks were.
                if rel.startswith("dist/"):
                    raise SystemExit(f"Q1 missing {path}")
                continue
            got = sha256(path)
            if got != digest:
                raise SystemExit(f"Q1 hash {version} {rel} {got} != {digest}")
        if present and family_name(present) != "runtime":
            raise SystemExit(f"Q1 copied marks are not runtime for {version}: {present}")
    left = recorded["2026.10.4"]["marks"]["dist/abort.runtime.js"]
    right = recorded["2026.10.5"]["marks"]["dist/abort.runtime.js"]
    if left == right:
        raise SystemExit("Q1 abort.runtime.js hashes match; spec expected them to differ")
    print("Q1 OK runtime abort.runtime.js differs")


def check_q2() -> None:
    db_path = ROOT / "fingerprints" / "db.json"
    digest = sha256(db_path)
    frozen = (BRIEF / "q2-identify-main.txt").read_text()
    if digest != DB_MAIN:
        print(f"Q2 SKIP re-identify db sha {digest} != main pin; frozen log kept")
        if "verdict=unknown" not in frozen or "2026.10.5" not in frozen:
            raise SystemExit("Q2 frozen log missing unknown verdict")
        return
    sys.path.insert(0, str(ROOT))
    from clawscore_fleet.fingerprint import identify, load_db

    db = load_db(db_path)
    lines = ["step2 identify against fingerprints/db.json on main d733a8c (unchanged)"]
    for version in VERSIONS:
        base = SIG / version
        rels = [rel for rel in ("dist/cli.runtime.js", "dist/abort.runtime.js", "dist/.buildstamp", "dist/build-info.json") if (base / rel).is_file()]

        def fetch(wanted, base=base):
            found = {}
            for rel in wanted:
                path = base / rel
                found[rel] = sha256(path) if path.is_file() else None
            return found

        result = identify(rels, fetch, db)
        lines.append(
            f"{version} paths={rels} verdict={result['verdict']} version={result['version']} "
            f"candidates={result['candidates']} reads={result['reads']} family={result['family']}"
        )
    text = "\n".join(lines) + "\n"
    if text != frozen:
        raise SystemExit("Q2 replay text differs\n" + text)
    print("Q2 OK unknown on main db")


def _day(row: dict, key: str) -> str:
    return str(row.get(key) or "")[:10]


def _ranges(row: dict) -> list[str]:
    found = []
    for entry in row.get("vulnerabilities") or []:
        package = entry.get("package") or {}
        if str(package.get("name") or "").lower() != "openclaw":
            continue
        rng = entry.get("vulnerable_version_range")
        if rng:
            found.append(str(rng))
    return found


def check_q4() -> None:
    sys.path.insert(0, str(ROOT))
    from clawscore_fleet.cves import in_range, is_withdrawn
    from clawscore_fleet.ghsa_only import semver_events_cover

    global_rows = json.loads((BRIEF / "gh-global-openclaw.json").read_text())
    repo_rows = json.loads((BRIEF / "gh-repo-openclaw-published.json").read_text())
    osv_rows = json.loads((BRIEF / "osv-openclaw.json").read_text())
    landscape = json.loads((ROOT / "evidence" / "landscape" / "ghsa-all.json").read_text())
    recorded = json.loads((BRIEF / "q4-and-counts.json").read_text())
    cutoff = "2026-09-11"
    q4 = {
        "cutoff": "published_at date > 2026-09-11",
        "fetch_time_ist": (BRIEF / "fetch-time-ist.txt").read_text().strip(),
        "github_advisory_db": sum(1 for row in global_rows if len(_day(row, "published_at")) == 10 and _day(row, "published_at") > cutoff),
        "repo_security_advisories": sum(1 for row in repo_rows if len(_day(row, "published_at")) == 10 and _day(row, "published_at") > cutoff),
        "osv": sum(1 for row in osv_rows if len(_day(row, "published")) == 10 and _day(row, "published") > cutoff),
        "github_db_max": max(_day(row, "published_at") for row in global_rows),
        "repo_max": max(_day(row, "published_at") for row in repo_rows),
        "osv_max": max(_day(row, "published") for row in osv_rows),
        "osv_modified_max": max(str(row.get("modified") or "")[:10] for row in osv_rows),
    }
    if q4 != recorded["q4"]:
        raise SystemExit(f"Q4 mismatch\n{q4}\n{recorded['q4']}")

    def covers_gh(row: dict, version: str) -> bool:
        ranges = _ranges(row)
        return bool(ranges) and any(in_range(version, rng) for rng in ranges)

    def covers_osv(row: dict, version: str) -> bool:
        if row.get("withdrawn"):
            return False
        for affected in row.get("affected") or []:
            if not isinstance(affected, dict):
                continue
            package = affected.get("package") or {}
            if package.get("name") not in (None, "openclaw"):
                continue
            for rng in affected.get("ranges") or []:
                if isinstance(rng, dict) and rng.get("type") == "SEMVER" and semver_events_cover(version, rng.get("events") or []):
                    return True
        return False

    global_ids = {row["ghsa_id"] for row in global_rows}
    repo_only = [row for row in repo_rows if row.get("ghsa_id") not in global_ids]
    counts = []
    for version in ("2026.10.5", "2026.10.4", "2026.6.10", "2026.4.22"):
        counts.append(
            {
                "version": version,
                "github_db": sum(1 for row in global_rows if not row.get("withdrawn_at") and covers_gh(row, version)),
                "repo_only": sum(1 for row in repo_only if not row.get("withdrawn_at") and covers_gh(row, version)),
                "osv": sum(1 for row in osv_rows if covers_osv(row, version)),
                "landscape_non_withdrawn": sum(1 for row in landscape if not is_withdrawn(row) and covers_gh(row, version)),
                "landscape_withdrawn_excluded": sum(1 for row in landscape if is_withdrawn(row) and covers_gh(row, version)),
            }
        )
    if counts != recorded["counts"]:
        raise SystemExit(f"counts mismatch\n{counts}\n{recorded['counts']}")
    print("Q4 OK", q4["github_advisory_db"], q4["repo_security_advisories"], q4["osv"])


def check_q3() -> None:
    lines = (BRIEF / "diff-2026.10.4-vs-2026.10.5.txt").read_text().splitlines()
    only4 = only5 = differ = 0
    for line in lines:
        if line.startswith("Only in") and "/2026.10.4/" in line:
            only4 += 1
        elif line.startswith("Only in") and "/2026.10.5/" in line:
            only5 += 1
        elif line.startswith("Files "):
            differ += 1
    got = {"only_2026.10.4": only4, "only_2026.10.5": only5, "content_differ": differ, "lines": len(lines)}
    recorded = json.loads((BRIEF / "q4-and-counts.json").read_text())["diff"]
    if got != recorded:
        raise SystemExit(f"Q3 summary {got} != {recorded}")
    hashes = json.loads((BRIEF / "q1-q3-hashes.json").read_text())
    for version in ("2026.10.4", "2026.10.5"):
        if hashes[version]["marks"]["dist/.buildstamp"] is not None:
            raise SystemExit(f"Q3 {version} buildstamp unexpectedly present")
        path = SIG / version / "dist" / "build-info.json"
        if sha256(path) != hashes[version]["marks"]["dist/build-info.json"]:
            raise SystemExit(f"Q3 build-info hash {version}")
    print("Q3 OK", got)


def main() -> int:
    check_q1()
    check_q2()
    check_q3()
    check_q4()
    for name in (
        "q1-q3-hashes.json",
        "q2-identify-main.txt",
        "q4-and-counts.json",
        "diff-2026.10.4-vs-2026.10.5.txt",
        "sha512-check.txt",
        "registry.json",
    ):
        print(f"{sha256(BRIEF / name)}  {name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
