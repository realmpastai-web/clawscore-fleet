# Narrower gap: what we may and may not say (internal, 2026-10-18)

Scope: 8 Microsoft Learn pages frozen in sources/ (fetched 2026-10-18; Defender endpoint docs git_commit_id 2d0cefa3, dated 2026-10-07) and clawscore-fleet main 756cd2a. Absence means "not found in these 8 pages", never "Microsoft can't".

| Link | Microsoft documents (quote id) | We prove (gate line) | Verdict |
|---|---|---|---|
| L1 build | Version per agent (Q1); may not appear until activity (Q8); Windows/macOS, P2 (Q7, Q10) | 115/115 exact, 4/4 stripped, collision pair as range, idle Linux recovered (B1) | HOLDS-NARROWED |
| L2 advisories | MDVM supports openclaw (Q2); "device with vulnerabilities" indicator (Q6); Linux lists native pkgs only (Q9); "GHSA" 0 hits | maker feed incl. 134 repo-only advisories, CVE map diff 0 (B2) | HOLDS-NARROWED |
| L3 reach | identity blast-radius hunting query (Q3); localAgentMetadata has no secret field; "secret"/"credential" 0 hits | credential names, 42/42 planted, lab only (B3) | HOLDS-NARROWED, UNPROVEN on real hosts |
| L4 fix order | recommendations "prioritized by their impact" (Q4, Q5); no target-version phrase found | min clearing version 2026.8.1, patch-then-rotate by reach (B4) | HOLDS-NARROWED |
| Chain | no page links all four per install | one per-install report (scan.json) | HOLDS, published docs only |

## Allowed
"Defender and Agent 365 show each OpenClaw agent's version and map OpenClaw CVEs through Defender Vulnerability Management. ClawScore Fleet adds, per install: the build read from the shipped files (even when package.json is stripped, and on idle Linux hosts), the maker's full advisory list including repo-only advisories, the credential names that install can read, and a patch-then-rotate order with the minimum release that clears every critical and high advisory (2026.8.1 on the 2026-09-11 feed). Credential reach is lab-tested only."

## Forbidden
- Agent 365 or Defender "doesn't show versions", or "14 with no usable version" (the README Results line comes from the local mock).
- "Microsoft has no fix order" (Q4) or "no blast radius" (Q3).
- "Microsoft doesn't map OpenClaw CVEs" (Q2).
- Credential reach measured on customer or real hosts.
- Anything about Microsoft's backend or unpublished RawAgentInfo fields.

## Follow-up for Cursor (not changed here)
README.md:45 (`registry sees 30 / 14 with no usable version / ...`) is mock-derived. Reword it as a lab-mock line, or drop "no usable version".
