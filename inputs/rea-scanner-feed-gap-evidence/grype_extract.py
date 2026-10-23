"""Grype v6 SQLite extraction for npm openclaw. Rules are BRIEF.md.

Read with Python sqlite3. vulnerability_handles.name is the advisory ID.
blobs.value JSON ranges[].version.constraint is Form A when version.type is npm.
status is recorded and not used as a filter. The spec's hold rule has no status test.
"""

from __future__ import annotations

import json
import sqlite3
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT))

from clawscore_fleet.cves import in_range
from clawscore_fleet.versions import RangeSyntaxError, parse_comparators

VERSIONS = ("2026.6.10", "2026.4.22")
GRYPE_DB = HERE / "frozen" / "grype" / "vulnerability.db"

OPENCLAW_SQL = """
SELECT vh.name, vh.provider_id, vh.status, b.value
FROM affected_package_handles AS aph
JOIN packages AS p ON p.id = aph.package_id
JOIN vulnerability_handles AS vh ON vh.id = aph.vulnerability_id
JOIN blobs AS b ON b.id = aph.blob_id
WHERE p.ecosystem = 'npm' AND lower(p.name) = 'openclaw'
ORDER BY vh.name
"""


def label(value: str) -> str:
    text = value.casefold()
    found = []
    if "nvd" in text:
        found.append("NVD")
    if "ghsa" in text or "github" in text:
        found.append("GHSA")
    if "osv" in text:
        found.append("OSV")
    return "+".join(found) if found else "UNCLASSIFIED"


def connect(db_path: Path | None = None) -> sqlite3.Connection:
    path = db_path or GRYPE_DB
    return sqlite3.connect(f"file:{path}?mode=ro", uri=True)


def _form_a(text: str) -> bool:
    try:
        parse_comparators(text)
    except RangeSyntaxError:
        return False
    return True


def load(db_path: Path | None = None) -> dict:
    con = connect(db_path)
    try:
        return _load(con)
    finally:
        con.close()


def _load(con: sqlite3.Connection) -> dict:
    cur = con.cursor()
    sources = []
    for (provider_id,) in cur.execute("SELECT id FROM providers ORDER BY id"):
        sources.append(("provider_id", provider_id, label(provider_id), "providers-table", ""))
    for provider_id, count in cur.execute(
        """
        SELECT vh.provider_id, COUNT(*)
        FROM affected_package_handles AS aph
        JOIN packages AS p ON p.id = aph.package_id
        JOIN vulnerability_handles AS vh ON vh.id = aph.vulnerability_id
        WHERE p.ecosystem = 'npm'
        GROUP BY vh.provider_id
        ORDER BY vh.provider_id
        """
    ):
        sources.append(("provider_id", provider_id, label(provider_id), "npm-packages", str(count)))
    for provider_id, count in cur.execute(
        """
        SELECT vh.provider_id, COUNT(*)
        FROM cpes AS c
        JOIN affected_cpe_handles AS ach ON ach.cpe_id = c.id
        JOIN vulnerability_handles AS vh ON vh.id = ach.vulnerability_id
        WHERE c.product = 'openclaw'
        GROUP BY vh.provider_id
        ORDER BY vh.provider_id
        """
    ):
        sources.append(("provider_id", provider_id, label(provider_id), "cpe-product-openclaw", str(count)))

    held = {version: {} for version in VERSIONS}
    unresolved = []
    openclaw_providers: dict[str, int] = {}
    for name, provider_id, status, raw in cur.execute(OPENCLAW_SQL):
        openclaw_providers[provider_id] = openclaw_providers.get(provider_id, 0) + 1
        try:
            blob = json.loads(raw)
        except json.JSONDecodeError:
            unresolved.append((name, provider_id, "blob is not JSON"))
            continue
        ranges = blob.get("ranges") if isinstance(blob, dict) else None
        if not isinstance(ranges, list) or not ranges:
            unresolved.append((name, provider_id, "ranges missing"))
            continue
        constraints = []
        good = []
        bad = False
        for item in ranges:
            version = (item or {}).get("version") or {}
            if version.get("type") != "npm":
                bad = True
                constraints.append(str(version.get("constraint")))
                continue
            constraint = version.get("constraint")
            if not isinstance(constraint, str) or not _form_a(constraint):
                bad = True
                constraints.append(str(constraint))
                continue
            constraints.append(constraint)
            good.append(constraint)
        constraint_text = " | ".join(constraints)
        if not good:
            unresolved.append((name, provider_id, f"unparsed {constraint_text}"))
            continue
        for version in VERSIONS:
            if any(in_range(version, item) for item in good):
                held[version][name] = {
                    "source": provider_id,
                    "status": status or "",
                    "constraint": constraint_text,
                }
    for provider_id in sorted(openclaw_providers):
        sources.append(
            (
                "provider_id",
                provider_id,
                label(provider_id),
                "npm-openclaw",
                str(openclaw_providers[provider_id]),
            )
        )
    return {"sources": sources, "held": held, "unresolved": unresolved}


def render_sources(payload: dict) -> str:
    lines = ["source_field\tsource_value\tlabel\tscope\trow_count"]
    for row in sorted(payload["sources"]):
        lines.append("\t".join(row))
    return "\n".join(lines) + "\n"


def render_held(payload: dict, version: str) -> str:
    lines = ["advisory_id\tversion\tsource\tstatus\tconstraint"]
    for adv_id in sorted(payload["held"][version]):
        row = payload["held"][version][adv_id]
        lines.append(f"{adv_id}\t{version}\t{row['source']}\t{row['status']}\t{row['constraint']}")
    return "\n".join(lines) + "\n"


def render_unresolved(payload: dict) -> str:
    lines = ["advisory_id\tsource\treason"]
    for adv_id, source, reason in sorted(set(payload["unresolved"])):
        lines.append(f"{adv_id}\t{source}\t{reason}")
    return "\n".join(lines) + "\n"


def schema_sql(db_path: Path | None = None) -> str:
    con = connect(db_path)
    try:
        rows = con.execute(
            """
            SELECT name, sql FROM sqlite_master
            WHERE type = 'table' AND name IN (
                'affected_package_handles', 'blobs', 'cpes', 'affected_cpe_handles',
                'db_metadata', 'packages', 'providers', 'vulnerability_handles'
            )
            ORDER BY name
            """
        ).fetchall()
    finally:
        con.close()
    return "\n".join(f"{name}\n{sql};\n" for name, sql in rows)


def build_snapshot(dest: Path, db_path: Path | None = None) -> None:
    """Copy the npm-openclaw rows into a small SQLite file for REA. Does not modify the source."""
    if dest.exists():
        dest.unlink()
    src = connect(db_path)
    dst = sqlite3.connect(dest)
    try:
        dst.executescript(
            """
            CREATE TABLE db_metadata (build_timestamp datetime, model integer, revision integer, addition integer);
            CREATE TABLE providers (id text, version text, processor text, date_captured datetime, input_digest text);
            CREATE TABLE packages (id integer primary key, ecosystem text, name text);
            CREATE TABLE vulnerability_handles (
                id integer primary key, name text, status text, published_date datetime,
                modified_date datetime, withdrawn_date datetime, provider_id text, blob_id integer
            );
            CREATE TABLE affected_package_handles (
                id integer primary key, vulnerability_id integer, operating_system_id integer,
                package_id integer, blob_id integer
            );
            CREATE TABLE blobs (id integer primary key, value text);
            """
        )
        dst.executemany("INSERT INTO db_metadata VALUES (?,?,?,?)", src.execute("SELECT * FROM db_metadata"))
        dst.executemany(
            "INSERT INTO providers VALUES (?,?,?,?,?)",
            src.execute("SELECT id, version, processor, date_captured, input_digest FROM providers"),
        )
        package_ids = [
            row[0]
            for row in src.execute(
                "SELECT id FROM packages WHERE ecosystem = 'npm' AND lower(name) = 'openclaw'"
            )
        ]
        dst.executemany(
            "INSERT INTO packages VALUES (?,?,?)",
            src.execute(
                f"SELECT id, ecosystem, name FROM packages WHERE id IN ({','.join('?' * len(package_ids))})",
                package_ids,
            ),
        )
        handles = src.execute(
            f"""
            SELECT id, vulnerability_id, operating_system_id, package_id, blob_id
            FROM affected_package_handles WHERE package_id IN ({','.join('?' * len(package_ids))})
            """,
            package_ids,
        ).fetchall()
        dst.executemany("INSERT INTO affected_package_handles VALUES (?,?,?,?,?)", handles)
        vuln_ids = sorted({row[1] for row in handles})
        vulns = src.execute(
            f"""
            SELECT id, name, status, published_date, modified_date, withdrawn_date, provider_id, blob_id
            FROM vulnerability_handles WHERE id IN ({','.join('?' * len(vuln_ids))})
            """,
            vuln_ids,
        ).fetchall()
        dst.executemany("INSERT INTO vulnerability_handles VALUES (?,?,?,?,?,?,?,?)", vulns)
        blob_ids = sorted({row[4] for row in handles} | {row[7] for row in vulns if row[7] is not None})
        blobs = src.execute(
            f"SELECT id, value FROM blobs WHERE id IN ({','.join('?' * len(blob_ids))})",
            blob_ids,
        ).fetchall()
        dst.executemany("INSERT INTO blobs VALUES (?,?)", blobs)
        dst.commit()
    finally:
        src.close()
        dst.close()
