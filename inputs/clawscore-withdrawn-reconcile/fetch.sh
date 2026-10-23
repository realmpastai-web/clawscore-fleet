#!/bin/bash
# Public GitHub REST + npm registry pulls. Run with a GitHub token for rate limits.
set -euo pipefail
cd "$(dirname "$0")/sources"
H=(-sS -H "Accept: application/vnd.github+json" -H "X-GitHub-Api-Version: 2022-11-28")
page_all(){ # url outfile ; follows Link rel=next
  local url="$1" out="$2" tmp; echo "[]" > "$out"
  while [ -n "$url" ]; do tmp=$(mktemp); hdr=$(mktemp)
    curl "${H[@]}" -D "$hdr" "$url" -o "$tmp"
    jq -s '.[0] + .[1]' "$out" "$tmp" > "$out.n" && mv "$out.n" "$out"
    url=$(grep -i '^link:' "$hdr" | tr ',' '\n' | grep 'rel="next"' | sed -E 's/.*<([^>]+)>.*/\1/' || true); rm -f "$tmp" "$hdr"
  done; }
page_all "https://api.github.com/advisories?ecosystem=npm&affects=openclaw&per_page=100" gh-global-openclaw-all.json
page_all "https://api.github.com/advisories?ecosystem=npm&affects=openclaw@2026.4.22&per_page=100" gh-global-affects-openclaw@2026.4.22.json
page_all "https://api.github.com/repos/openclaw/openclaw/security-advisories?state=published&per_page=100" gh-repo-openclaw-published.json
curl -sS https://registry.npmjs.org/openclaw/2026.4.22 -o npm-openclaw-2026.4.22.json
curl -sS "$(jq -r .dist.tarball npm-openclaw-2026.4.22.json)" -o openclaw-2026.4.22.tgz
date -u +%Y-%m-%dT%H:%M:%SZ > PULLED_AT.txt
