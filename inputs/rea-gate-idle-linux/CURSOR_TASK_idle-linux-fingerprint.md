CURSOR TASK: ClawScore idle-Linux fingerprint + offline version recovery (invention-in-reverse)
FROZEN 2026-10-18 by Hark. Branch feat/idle-linux-fingerprint from main. Draft PR only; Hark gates it.
EVIDENCE RULE: no claim without the file, log or command output. Reverse-first: the fixture mirrors the shipped openclaw@2026.4.15 layout (recon.log). Do not invent fields the tarball does not show.

Goal: ClawScore must score an idle-Linux host (gateway installed as a systemd USER unit with linger, no running process) and recover its version when package.json has no version string.

1. Fixture: port build_fixture.py. The fixture must have (a) node_modules/openclaw with package.json that has NO version/gitHead, (b) dist/build-info.json + dist/.buildstamp, (c) the 2147 hashed dist/*.js names from dist-names-2026.4.15.txt, (d) ~/.config/systemd/user/openclaw-gateway.service + default.target.wants symlink, (e) /var/lib/systemd/linger/<user>, (f) ~/.openclaw credential files with NAMES ONLY (no secret values), (g) CHANGELOG.md with the 30 GHSAs. Never write a real token.
2. Discovery + recovery: port discover_recover.py. Find the install, confirm idle (unit + enable symlink + linger marker + zero process evidence), and recover the version from build-info.json with a dirlist Jaccard >= 0.99 vs dist-names-2026.4.15.txt. package.json version must be absent so the fallback is proven.
3. Assertion: CHANGELOG-parsed GHSA set (changelog-ghsa-2026.4.15.txt, 30 ids) must have >= 1 id absent from mock-agent365-export.json. Keep G4: >= 1 CHANGELOG id is not in the pinned feed CSV, so ClawScore's four counts still need the feed.
4. Acceptance test = gate_idle_linux.py must print GATE PASS (G1, G2.*, G3.*, G4). Replay it in CI.
Reference (do not edit): build_fixture.py, discover_recover.py, gate_idle_linux.py, dirlist_fingerprint.json, dist-names-2026.4.15.txt, changelog-ghsa-2026.4.15.txt, mock-agent365-export.json. Expected: expected-idle-linux.json.
