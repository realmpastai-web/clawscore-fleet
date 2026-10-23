"""Patch vulnerable installs first, then rotate highest-reach tokens."""

from __future__ import annotations


def fix_order(installs: list[dict]) -> list[dict]:
    vulnerable = [item for item in installs if item.get("vulnerable")]
    vulnerable.sort(
        key=lambda item: (
            -len(item.get("credentials") or []),
            not bool(item.get("auto_approve")),
            item["id"],
        )
    )
    steps: list[dict] = []
    for item in vulnerable:
        steps.append(
            {
                "action": "patch",
                "install": item["id"],
                "version": item.get("version"),
                "cves": list(item.get("cves") or []),
                "credential_count": len(item.get("credentials") or []),
                "auto_approve": bool(item.get("auto_approve")),
            }
        )
    reach: dict[str, list[str]] = {}
    for item in vulnerable:
        for name in item.get("credentials") or []:
            reach.setdefault(name, []).append(item["id"])
    for name, ids in sorted(reach.items(), key=lambda pair: (-len(pair[1]), pair[0])):
        steps.append(
            {
                "action": "rotate",
                "credential": name,
                "reach": len(ids),
                "installs": sorted(ids),
            }
        )
    return steps
