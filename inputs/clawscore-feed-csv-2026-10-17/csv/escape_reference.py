#!/usr/bin/env python3
"""Reference rule for the v0.2.2 CSV formula-escape gate (Hark, 2026-10-17). Source: OWASP CSV Injection (sources/owasp-csv-injection.html).
RULE: for every TEXT cell of defender_local_agents.csv data rows (never the header, never the 5 integer columns):
  if the cell's first character is one of DANGER, or is a single quote "'", prefix it with a single quote "'".
  (Escaping a leading quote too keeps the rule reversible: a real value "'=x" becomes "''=x".) Nothing else is changed.
  Then write the row with Python csv.writer (QUOTE_MINIMAL, lineterminator "\\n"), which doubles embedded quotes
  and quotes cells holding , " \\r or \\n (RFC 4180).
  List cells are joined first ("|"), then escaped as one cell. Empty cells stay empty. JSONL is NOT escaped.
UNESCAPE (for the round-trip gate): if a cell starts with "'", drop that first char.
Run: python3 escape_reference.py  -> regenerates expected columns and checks formula-escape-vectors.tsv; exit 0 = all match."""
import csv, io, json, sys
from pathlib import Path
DANGER = ("=", "+", "-", "@", "\t", "\r", "\n", "\uff1d", "\uff0b", "\uff0d", "\uff20")  # last 4: full-width = + - @
INT_COLUMNS = ("MCP servers", "Local MCPs", "cs_reads", "cs_ghsa_only_count", "cs_crit_high_count")
def escape_cell(v: str) -> str: return "'" + v if v[:1] in DANGER + ("'",) else v
def unescape_cell(v: str) -> str: return v[1:] if v[:1] == "'" else v
def csv_field(v: str) -> str:
    b = io.StringIO(); csv.writer(b, lineterminator="\n").writerow([v]); return b.getvalue()[:-1]
if __name__ == "__main__":
    p = Path(__file__).with_name("formula-escape-vectors.tsv"); rows = list(csv.DictReader(open(p, encoding="utf-8"), delimiter="\t", quoting=csv.QUOTE_NONE))
    bad = []
    for r in rows:
        x = json.loads(r["input_json"]); e = escape_cell(x)
        ok = (e == json.loads(r["expected_cell_json"]) and csv_field(e) == json.loads(r["expected_csv_field_json"]) and unescape_cell(e) == x)
        print(("PASS" if ok else "FAIL") + "\t" + r["id"] + "\t" + r["note"]); bad += [] if ok else [r["id"]]
    print(f"VECTORS ok={len(rows)-len(bad)}/{len(rows)} fail={bad}"); sys.exit(1 if bad else 0)
