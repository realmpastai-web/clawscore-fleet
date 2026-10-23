"""Product summary computed from a scan document."""

from __future__ import annotations


def summary_from_scan(scan: dict) -> dict:
    installs = scan["installs"]
    by_id = {item["id"]: item for item in installs}
    rows = scan.get("agent365_rows")
    if rows is None:
        rows = [
            {
                "device": item["id"],
                "version": (item.get("agent365") or {}).get("version") or "",
            }
            for item in installs
        ]
    no_usable = 0
    for row in rows:
        detected = (by_id.get(row.get("device")) or {}).get("version") or ""
        agent_version = (row.get("version") or "").strip()
        if agent_version == "" or agent_version != detected:
            no_usable += 1
    registry = len(rows)
    vulnerable = sum(1 for item in installs if item.get("vulnerable"))
    rotate = [step for step in scan.get("fix_order") or [] if step.get("action") == "rotate"]
    tokens = [
        {"credential": step["credential"], "reach": step["reach"], "installs": list(step["installs"])}
        for step in rotate
    ]
    sentence = (
        f"lab mock registry lists {registry} / {no_usable} with a blank or stale mock version / "
        f"{vulnerable} vulnerable / rotate these {len(tokens)} tokens first"
    )
    return {
        "sentence": sentence,
        "registry_sees": registry,
        "no_usable_version": no_usable,
        "vulnerable": vulnerable,
        "rotate_tokens": len(tokens),
        "rotate_order": tokens,
    }
