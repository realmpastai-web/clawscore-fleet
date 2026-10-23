"""Cross-check every advisory range decision with the pinned npm semver package."""

from __future__ import annotations

import json
import re
import subprocess
from pathlib import Path

from clawscore_fleet.cves import _load_advisories, _openclaw_ranges, in_range
from clawscore_fleet.versions import LANDSCAPE, ROOT, RangeSyntaxError, hark_key, parse_comparators

EVIDENCE = ROOT / "evidence"
CHECK_JS = ROOT / "tools" / "semver" / "check.js"
_POST = re.compile(r"^\d+\.\d+\.\d+-\d+$")
_COMMA = re.compile(r"\s*,\s*")


def _catalog_versions() -> list[str]:
    published = json.loads((LANDSCAPE / "versions.json").read_text())
    return list(published.keys())


def _ranges() -> list[str]:
    """Unique range strings on an openclaw-named package, any ecosystem.

    Scoring uses ``is_openclaw_npm`` via ``_openclaw_ranges``. This grammar
    cross-check still includes a string that only a non-npm row carries.
    ``inputs/clawscore-v0.2.3-gate/expected-v023.json`` pins ``decisions`` at
    52820 (278 catalog versions × 190 unique strings) and that folder is
    frozen. The only such string in the pinned landscape is ``<=2026.2.14``
    on GHSA-mmpf-jwf4-h3qv. ``<= 2026.2.22-2`` on GHSA-2j9j-gf59-p4p5 is also
    on an npm row, so it stays in the set either way.
    """
    found = []
    seen = set()
    for advisory in _load_advisories():
        for rng in _openclaw_ranges(advisory):
            if rng not in seen:
                seen.add(rng)
                found.append(rng)
        for entry in advisory.get("vulnerabilities") or []:
            package = entry.get("package") or {}
            name = package.get("name")
            rng = entry.get("vulnerable_version_range")
            if not isinstance(name, str) or name.casefold() != "openclaw" or not rng:
                continue
            text = str(rng)
            if text not in seen:
                seen.add(text)
                found.append(text)
    return found


def npm_range(rng: str) -> str:
    """Comma-joined GHSA ranges become whitespace-joined ranges before npm sees them."""
    return _COMMA.sub(" ", rng)


def _bounds(rng: str) -> list[str] | None:
    try:
        return [bound for _operator, bound in parse_comparators(rng)]
    except RangeSyntaxError:
        return None


def _explain(version: str, rng: str, hark_value: bool, npm_value: bool | None, error: str | None) -> str:
    """A hark-grammar label is only used when hark_key really returns None."""
    bounds = _bounds(rng)
    if hark_key(version) is None or bounds is None or any(hark_key(item) is None for item in bounds):
        if hark_key(version) is None:
            return "hark-grammar: this parser does not accept the version string; npm semver did not return a boolean"
        return (
            "hark-grammar: a range bound does not match this parser, so the range matches nothing; "
            "npm semver parsed that bound"
        )
    if error or npm_value is None:
        return "npm-error: " + (error or "no boolean")
    involved = [version, *bounds]
    if any(_POST.match(item) for item in involved):
        return (
            "post-release-suffix: this parser sorts a numeric -N suffix after the base release; "
            "npm semver sorts -N as a prerelease before the base release, and a prerelease does not "
            "satisfy a range that does not name that prerelease."
        )
    if hark_value != npm_value:
        return ""
    return ""


def run() -> dict:
    versions = _catalog_versions()
    ranges = _ranges()
    pairs = [(version, rng) for version in versions for rng in ranges]
    hark_bits = [in_range(version, rng) for version, rng in pairs]
    npm_pairs = [(version, npm_range(rng)) for version, rng in pairs]
    comma_sent = sum(1 for _version, rng in npm_pairs if "," in rng)
    proc = subprocess.run(
        ["node", str(CHECK_JS)],
        input=json.dumps({"pairs": npm_pairs}),
        capture_output=True,
        text=True,
        check=False,
    )
    if proc.returncode != 0:
        raise SystemExit(proc.stderr or "semver check failed")
    payload = json.loads(proc.stdout)
    standard = payload["standard"]
    prerelease = payload["prerelease"]
    error_map = {index: message for index, message in payload.get("errors") or []}
    if len(standard) != len(pairs) or len(prerelease) != len(pairs):
        raise SystemExit("semver check returned the wrong number of decisions")
    if comma_sent != 0 or payload.get("comma_ranges") not in (0, None):
        raise SystemExit(f"comma ranges sent to npm: python {comma_sent} check.js {payload.get('comma_ranges')}")
    lines = [
        f"npm_semver {payload.get('semver')}",
        f"versions {len(versions)}",
        f"ranges {len(ranges)}",
        f"decisions {len(pairs)}",
        "comma_ranges_sent 0",
    ]
    disagreements = []
    unexplained = []
    default_disagreements = 0
    for index, (version, rng) in enumerate(pairs):
        npm_default = standard[index]
        npm_value = prerelease[index]
        hark_value = hark_bits[index]
        if npm_default != hark_value:
            default_disagreements += 1
        if npm_value == hark_value:
            continue
        reason = _explain(version, rng, hark_value, npm_value, error_map.get(index))
        row = {
            "version": version,
            "range": rng,
            "hark": hark_value,
            "npm": npm_default,
            "npm_include_prerelease": npm_value,
            "explanation": reason,
        }
        disagreements.append(row)
        if not reason:
            unexplained.append(row)
    lines.append(f"disagreements {len(disagreements)}")
    lines.append(f"default_call_disagreements {default_disagreements}")
    lines.append(f"unexplained {len(unexplained)}")
    lines.append("")
    for row in disagreements:
        hark_bit = "1" if row["hark"] else "0"
        npm_bit = "null" if row["npm"] is None else ("1" if row["npm"] else "0")
        pre_bit = (
            "null"
            if row["npm_include_prerelease"] is None
            else ("1" if row["npm_include_prerelease"] else "0")
        )
        lines.append(
            "DISAGREE"
            f"\t{row['version']}\t{row['range']}\thark={hark_bit}\tnpm={npm_bit}\tincludePrerelease={pre_bit}"
        )
        if row["explanation"]:
            lines.append("  explanation: " + row["explanation"])
        else:
            lines.append("  explanation: UNEXPLAINED")
    text = "\n".join(lines) + "\n"
    EVIDENCE.mkdir(parents=True, exist_ok=True)
    (EVIDENCE / "semver-crosscheck.log").write_text(text)
    return {
        "semver": payload.get("semver"),
        "decisions": len(pairs),
        "disagreements": len(disagreements),
        "default_call_disagreements": default_disagreements,
        "unexplained": len(unexplained),
        "comma_ranges_sent": comma_sent,
        "pass": len(unexplained) == 0 and comma_sent == 0,
    }


def main() -> int:
    result = run()
    print(
        f"semver {result['semver']} decisions {result['decisions']} "
        f"disagreements {result['disagreements']} unexplained {result['unexplained']}",
        flush=True,
    )
    return 0 if result["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
