"""Render README.md from evidence/verify-report.json. The template has no digits."""

from __future__ import annotations

import json
import re
from pathlib import Path

from clawscore_fleet.export_defender import verbatim_flag_lines

ROOT = Path(__file__).resolve().parents[1]

TEMPLATE = """# clawscore-fleet {release}

clawscore-fleet reports, for each OpenClaw install in a fleet, the exact version or a version range when builds share a fingerprint, the advisories that apply, the credential names that install can reach, and a fix order. It diffs that report against a local mock of the inventory Microsoft Defender / {agent_product} exposes. Published-schema verdicts come from the frozen gate over Microsoft Graph CSDL and Defender learn pages, not from that mock. Credential values are never printed or stored.

## Threat

The Claw Chain advisories below are fixed in openclaw@{patch_boundary} (released {patch_released}). Later releases can still match other advisories. The minimum release that clears every critical and high advisory in this feed is {fix_version}. On a vulnerable install, MCP server settings and the process environment can put cloud and chat tokens in reach of the agent. autoApprove means the agent can act without a person confirming each action. Patch those installs first, then rotate the highest-reach tokens on the installs that are still vulnerable.

Chain overview: {chain_url}

Advisory feed newest date: {feed_newest}. For a release with no matching advisory, the report says: {no_advisory_wording}.

The pinned feed has {advisory_total} advisories: {advisory_global} from the global database and {advisory_repo_only} published only on the repository. {advisory_repo_already} of those repository advisories were already published on or before {previous_feed_newest}. On that previous feed, {cited_version} moved from {grammar_before} advisories to {grammar_after} after the prerelease grammar fix.

## How this differs from {agent_product} / Defender

Microsoft Defender for Endpoint can discover OpenClaw and record the host process, the device, the user, autoApprove, and MCP servers. Discovery is not an exact build fingerprint. {version_sentence} This lab's mock assigns no risk score, and it leaves version blank or stale for a configured subset of installs. That local mock is not the published schema. clawscore-fleet adds the build fingerprint, the advisory list, credential names only, and the fix order. Against the published schema, the claim is narrower: the idle Linux host, the per-build GHSA list, and the fix order.

Local-agent discovery fields: {defender_url}

Defender agent inventory: {xdr_url}

This repo does not call Microsoft. The mock is a local FastAPI service.

## What Defender / {agent_product} already do, and what we add

Defender and {agent_product} show each OpenClaw agent's version and map OpenClaw CVEs through Defender Vulnerability Management. ClawScore Fleet adds, per install: the build read from the shipped files (even when package.json is stripped, and on idle Linux hosts), the maker's full advisory list including repo-only advisories, the credential names that install can read, and a patch-then-rotate order with the minimum release that clears every critical and high advisory ({fix_version} on the {feed_newest} feed). Credential reach is lab-tested only.

Source: [inputs/rea-narrower-gap/CLAIMS.md](inputs/rea-narrower-gap/CLAIMS.md)

## Lab

Each image runs `npm install` for one pinned OpenClaw release. Compose starts the fleet on an internal Docker network and publishes no ports. {stripped_total} installs are stripped: package.json is removed, or rewritten so its version string is a lie. The fingerprint does not read package.json. Shared fingerprints return a range instead of picking one release. The scanner does not open the answer key. File reads per install stay within the limit ({read_limit}).

The matrix covers {matrix_total} stable releases from {matrix_first} through {matrix_last}. The lab runs {install_count} installs. {old_count} of them predate {old_cutoff} and were published in {old_months}.

Python {python_requirement}.

## Idle Linux hosts

ClawScore scores an idle Linux host whose gateway is installed as a systemd user unit, enabled for the default target, with a linger marker and no running process. On that host package.json has no version string. The version is recovered from dist/build-info.json and kept when the hashed dist listing reaches Jaccard {idle_jaccard_min} against the reversed public tarball openclaw@{idle_version} (digest {idle_tarball_sha256}). That static read is recorded under evidence/rea/idle-linux. The on-disk CHANGELOG has {changelog_ghsa_count} GHSA ids. {changelog_feed_missing} of those ids are absent from the pinned feed. That count compares the pinned feed with the CHANGELOG. It is not an {agent_product} result.

Published schema gate: verdict A, idle host not exposed, is {verdict_a} ({verdict_a_detail}). Verdict B, per-build GHSA list not exposed, is {verdict_b} ({verdict_b_detail}). Scope: {schema_scope}.

- Host state: {idle_state}. Version source: {idle_version_source}. Recovered version: {idle_version}. Dirlist Jaccard: {idle_jaccard}.

## Results

Generated from evidence/verify-report.json by make verify. Do not edit this section by hand.

{sentence}

- Stable releases with a tarball and listing: {matrix_have} of {matrix_total}.
- Exact classification on non-colliding releases: {matrix_correct} of {matrix_non_colliding} ({matrix_percent}%).
- Fingerprint collision groups: {collision_count}. Included group: {collision_group}.
- Directory listing alone: {dirlist_correct} of {dirlist_total} ({dirlist_percent}%).
- File reads per install: max {reads_max}, mean {reads_mean} (limit {read_limit}).
- Lab installs before {old_cutoff}: {old_count} (minimum {old_minimum}).
- Exact version on non-colliding lab installs: {acc_correct} of {acc_total} ({acc_percent}%). Target {acc_target}%.
- Exact version before {old_cutoff}: {pre_correct} of {pre_total} ({pre_percent}%).
- Range verdicts on colliding lab installs: {range_ok} of {range_total}.
- Stripped installs classified: {stripped_ok} of {stripped_total}.
- CVE map diff lines: {diff_lines}.
- semver disagreements: {semver_disagreements}. Unexplained: {semver_unexplained}.
- {focus_version} shows {focus_advisories} advisories ({focus_critical} critical / {focus_high} high). Cited from evidence/landscape/CLAIMS.md.
- Blast-radius recall: {blast_found} of {blast_planted} ({blast_percent}%). Target {blast_target}%.
- Seed hashes from the {seed_label} table: {seed_matched} of {seed_total}.
- Gate status: {gate_status}.

{failure_block}

Rotation order (highest reach first):

{rotation_block}

Claw Chain advisories from the generated map:

{cve_block}

## Defender export

`make export` writes one row per lab install to evidence/export/defender_local_agents.csv and evidence/export/agentsinfo_local.jsonl. CSV text cells, except the header and the integer columns, are prefixed with a single quote when the first character would start a formula, then quoted under {csv_standard}. Excel can drop that quote when a workbook is saved and opened again. A leading tab was not used. Whether that variant is better for our consumers is UNPROVEN. JSONL cells are not escaped. Risk level is empty. Device ID is lab-derived, Defender format UNPROVEN: a hash of device fields recorded in the lab scan. The derivation is in docs/defender-export-lab-fields.md. The lab scan records no observation clock, so `make export` and `make verify` write one UTC time to evidence/lab-scan-observed-at.txt when that file is absent and then reuse the committed line. First seen, Timestamp, and LastUpdatedDateTime are that recorded observation. PublishedStatus is null. `make feed-check` logs the newest OpenClaw advisory on GitHub against the pinned feed date. It does not change pinned results. It logs SKIP when the query cannot be completed.

Version is the fingerprinted release when the verdict is exact, and blank when the verdict is a range. Remote MCP rows are the servers that have an endpoint in the scan. Local MCP rows are the server names recorded for the install. trustedProcess is the string false because the scan records no trusted-process grant. LifecycleStatus is Active when evidence/ps.txt shows the container is Up. AgentId is a GUID derived from the install id. aadDeviceId stays empty because the scan records no directory device id. Credential cells list class names only.

Spec lines copied verbatim:

{spec_flags}
"""


def assert_template_has_no_digits() -> None:
    static = re.sub(r"\{[a-z0-9_]+\}", "", TEMPLATE)
    digits = re.findall(r"\d", static)
    if digits:
        raise SystemExit("README template contains raw digits")


def _rotation_block(order: list[dict]) -> str:
    if not order:
        return "No tokens to rotate."
    lines = []
    for step in order:
        installs = ", ".join(step["installs"])
        lines.append(f"- {step['credential']} (reach {step['reach']}; {installs})")
    return "\n".join(lines)


def _cve_block(cves: list[dict]) -> str:
    if not cves:
        return "No Claw Chain advisories were found in the generated map."
    lines = []
    for item in cves:
        lines.append(
            f"- {item['id']}: {item['title']} (affected {item['affected']}, fixed in {item['fixed_in']})"
        )
        for source in item["sources"]:
            lines.append(f"  - {source}")
    return "\n".join(lines)


def _failure_block(failures: list[str]) -> str:
    if not failures:
        return "No gate failures."
    return "\n".join(f"- {item}" for item in failures)


def _idle_fields(report: dict) -> dict:
    gates = report.get("gates") or {}
    discovered = (gates.get("idle_linux_discovered") or {}).get("actuals") or {}
    recovered = (gates.get("idle_linux_version_recovered") or {}).get("actuals") or {}
    ghsa = (gates.get("changelog_ghsa_30") or {}).get("actuals") or {}
    schema = (gates.get("agent365_published_schema") or {}).get("actuals") or {}
    feed = (gates.get("changelog_not_in_feed") or {}).get("actuals") or {}
    version_line = schema.get("agentsinfo_version_line") or ""
    product = report.get("agent_product") or ""
    if "version IS exposed" in version_line:
        version_sentence = f"{product} and Defender expose a Version string per agent."
    else:
        version_sentence = ""
    return {
        "idle_state": discovered.get("state", ""),
        "idle_version_source": recovered.get("version_source", ""),
        "idle_version": recovered.get("version", ""),
        "idle_jaccard": recovered.get("dirlist_jaccard", ""),
        "idle_jaccard_min": recovered.get("jaccard_min", ""),
        "idle_tarball_sha256": recovered.get("tarball_sha256", ""),
        "changelog_ghsa_count": ghsa.get("count", ""),
        "changelog_feed_missing": feed.get("missing", ""),
        "verdict_a": schema.get("verdict_a", ""),
        "verdict_a_detail": schema.get("verdict_a_detail", ""),
        "verdict_b": schema.get("verdict_b", ""),
        "verdict_b_detail": schema.get("verdict_b_detail", ""),
        "schema_scope": schema.get("scope", ""),
        "version_sentence": version_sentence,
    }


def render(report: dict) -> str:
    assert_template_has_no_digits()
    raw_flags = report.get("spec_unprovens") or verbatim_flag_lines()
    spec_flags = "\n".join(raw_flags).replace("{", "{{").replace("}", "}}")
    idle = _idle_fields(report)
    text = TEMPLATE.format(
        release=report["release"],
        agent_product=report["agent_product"],
        patch_boundary=report["patch_boundary"],
        patch_released=report["patch_released"],
        fix_version=report["fix_version"],
        chain_url=report["chain_url"],
        feed_newest=report["feed_newest"],
        no_advisory_wording=report["no_advisory_wording"],
        advisory_total=report["advisory_total"],
        advisory_global=report["advisory_global"],
        advisory_repo_only=report["advisory_repo_only"],
        advisory_repo_already=report["advisory_repo_already"],
        previous_feed_newest=report["previous_feed_newest"],
        cited_version=report["cited_version"],
        grammar_before=report["grammar_before"],
        grammar_after=report["grammar_after"],
        csv_standard=report["csv_standard"],
        defender_url=report["defender_url"],
        xdr_url=report["xdr_url"],
        stripped_total=report["display"]["stripped_total"],
        read_limit=report["display"]["read_limit"],
        matrix_total=report["display"]["matrix_total"],
        matrix_first=report["display"]["matrix_first"],
        matrix_last=report["display"]["matrix_last"],
        install_count=report["display"]["install_count"],
        old_count=report["display"]["old_count"],
        old_cutoff=report["display"]["old_cutoff"],
        old_months=report["display"]["old_months"],
        python_requirement=report["python_requirement"],
        idle_state=idle["idle_state"],
        idle_version_source=idle["idle_version_source"],
        idle_version=idle["idle_version"],
        idle_jaccard=idle["idle_jaccard"],
        idle_jaccard_min=idle["idle_jaccard_min"],
        idle_tarball_sha256=idle["idle_tarball_sha256"],
        changelog_ghsa_count=idle["changelog_ghsa_count"],
        changelog_feed_missing=idle["changelog_feed_missing"],
        verdict_a=idle["verdict_a"],
        verdict_a_detail=idle["verdict_a_detail"],
        verdict_b=idle["verdict_b"],
        verdict_b_detail=idle["verdict_b_detail"],
        schema_scope=idle["schema_scope"],
        version_sentence=idle["version_sentence"],
        sentence=report["summary"]["sentence"],
        matrix_have=report["display"]["matrix_have"],
        matrix_correct=report["display"]["matrix_correct"],
        matrix_non_colliding=report["display"]["matrix_non_colliding"],
        matrix_percent=report["display"]["matrix_percent"],
        collision_count=report["display"]["collision_count"],
        collision_group=report["display"]["collision_group"],
        dirlist_correct=report["display"]["dirlist_correct"],
        dirlist_total=report["display"]["dirlist_total"],
        dirlist_percent=report["display"]["dirlist_percent"],
        reads_max=report["display"]["reads_max"],
        reads_mean=report["display"]["reads_mean"],
        old_minimum=report["display"]["old_minimum"],
        acc_correct=report["display"]["acc_correct"],
        acc_total=report["display"]["acc_total"],
        acc_percent=report["display"]["acc_percent"],
        acc_target=report["display"]["acc_target"],
        pre_correct=report["display"]["pre_correct"],
        pre_total=report["display"]["pre_total"],
        pre_percent=report["display"]["pre_percent"],
        range_ok=report["display"]["range_ok"],
        range_total=report["display"]["range_total"],
        stripped_ok=report["display"]["stripped_ok"],
        diff_lines=report["display"]["diff_lines"],
        semver_disagreements=report["display"]["semver_disagreements"],
        semver_unexplained=report["display"]["semver_unexplained"],
        focus_version=report["display"]["focus_version"],
        focus_advisories=report["display"]["focus_advisories"],
        focus_critical=report["display"]["focus_critical"],
        focus_high=report["display"]["focus_high"],
        blast_found=report["display"]["blast_found"],
        blast_planted=report["display"]["blast_planted"],
        blast_percent=report["display"]["blast_percent"],
        blast_target=report["display"]["blast_target"],
        seed_label=report["display"]["seed_label"],
        seed_matched=report["display"]["seed_matched"],
        seed_total=report["display"]["seed_total"],
        gate_status=report["gate_status"],
        failure_block=_failure_block(report["failures"]),
        rotation_block=_rotation_block(report["summary"]["rotate_order"]),
        cve_block=_cve_block(report["cves"]),
        spec_flags=spec_flags,
    )
    text += _ghsa_section(report)
    if not text.endswith("\n"):
        text += "\n"
    return text


def _ghsa_section(report: dict) -> str:
    """GHSA-only sentences. Present only while that gate passes."""
    gate = (report.get("gates") or {}).get("ghsa_only") or {}
    if gate.get("pass") is not True:
        return ""
    paragraphs = [
        text.strip()
        for text in (gate.get("readme_claim") or "", gate.get("defender_claim") or "")
        if text and text.strip()
    ]
    if not paragraphs:
        return ""
    return "\n## GHSA-only advisories\n\n" + "\n\n".join(paragraphs) + "\n"


def write_readme(report: dict) -> Path:
    path = ROOT / "README.md"
    path.write_text(render(report))
    return path


def readme_drift(readme_text: str, report: dict) -> str:
    """Empty when readme_text is exactly render(report). Otherwise the first differing line."""
    rendered = render(report)
    if readme_text == rendered:
        return ""
    left = readme_text.splitlines()
    right = rendered.splitlines()
    limit = max(len(left), len(right))
    for index in range(limit):
        got = left[index] if index < len(left) else ""
        wanted = right[index] if index < len(right) else ""
        if got != wanted:
            return f"line {index + 1}: {got!r} != {wanted!r}"
    return "readme trailing newline differs from render(verify-report)"


def main() -> int:
    report = json.loads((ROOT / "evidence" / "verify-report.json").read_text())
    write_readme(report)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
