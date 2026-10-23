"""make demo: compute the Agent 365 comparison from the scan."""

from __future__ import annotations

import json
from pathlib import Path

from clawscore_fleet.summary import summary_from_scan

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "evidence"


def main() -> int:
    scan_path = EVIDENCE / "scan.json"
    scan = json.loads(scan_path.read_text())
    summary = summary_from_scan(scan)
    stored = (scan.get("summary") or {}).get("sentence")
    if stored != summary["sentence"]:
        raise SystemExit("stored scan summary does not match a fresh computation")
    lines = [
        "# Agent 365 vs clawscore",
        "",
        summary["sentence"],
        "",
        "Definitions, computed from evidence/scan.json:",
        "",
        "- lab mock registry lists: rows in the lab mock registry",
        "- blank or stale mock version: the mock version is blank or differs from the clawscore exact version",
        "- vulnerable: clawscore marked the install vulnerable",
        "- tokens: credential names on those vulnerable installs, highest reach first",
        "",
        "## Rotation order",
        "",
    ]
    if not summary["rotate_order"]:
        lines.append("No tokens to rotate.")
    else:
        for index, step in enumerate(summary["rotate_order"], start=1):
            installs = ", ".join(step["installs"])
            lines.append(
                f"{index}. {step['credential']} (reach {step['reach']}; {installs})"
            )
    lines.extend(["", "## Installs", ""])
    lines.append("| device | clawscore version | method | agent365 version | vulnerable | credentials | cves |")
    lines.append("| --- | --- | --- | --- | --- | --- | --- |")
    for item in scan["installs"]:
        agent = item.get("agent365") or {}
        agent_version = agent.get("version") or ""
        creds = ", ".join(item.get("credentials") or [])
        cves = ", ".join(item.get("cves") or [])
        lines.append(
            "| {id} | {version} | {method} | {agent} | {vulnerable} | {creds} | {cves} |".format(
                id=item["id"],
                version=item.get("version") or "",
                method=item.get("method") or "",
                agent=agent_version,
                vulnerable="yes" if item.get("vulnerable") else "no",
                creds=creds,
                cves=cves,
            )
        )
    lines.append("")
    path = EVIDENCE / "agent365-vs-clawscore.md"
    path.write_text("\n".join(lines))
    print(summary["sentence"], flush=True)
    print(f"wrote {path}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
