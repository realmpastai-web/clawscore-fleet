CURSOR TASK: PR #5 (feat/v0.2.3-feed-csv @ 75fa8cf) - make CI green. Two changes only.
Evidence rule: no claim without file, log or command output. Draft PR stays draft; Hark gates it.

Why: CI verify FAILED on both runs (pull_request run 39104181631 and push run 39104167829). The log says:
  fatal: path 'evidence/verify-report.json' exists on disk, but not in '58d4925c3f83a0fae5ed947bd285cbc3d32f72f7'
  gates_v023.py line 415 readme_facts -> subprocess.CalledProcessError: git show 58d4925...:evidence/verify-report.json (exit 128)
  make: *** [Makefile:41: verify] Error 1
Cause: actions/checkout@v4 defaults to fetch-depth 1, so the base commit is not in the CI clone.

1. Copy inputs/clawscore-v0.2.3-gate/ from hark-inputs-2026-10-17 at the commit Hark names, replacing the PR copy.
   It adds base-verify-report-58d4925.json (sha256 d6c81247...237c, equal to main@58d4925 evidence/verify-report.json),
   the re-pinned G8 and the new G9.
2. In clawscore_fleet/gates_v023.py there are 2 call sites (no_regression ~L371 and readme_facts ~L416).
   Replace json.loads(subprocess.check_output(["git","show",f"{BASE}:evidence/verify-report.json"],...))
   with json.loads((ROOT / "inputs/clawscore-v0.2.3-gate/base-verify-report-58d4925.json").read_text()).
   Do not set fetch-depth: 0. Verify must stay offline and history-free.

Acceptance:
- cd inputs/clawscore-v0.2.3-gate && sha256sum -c SHA256SUMS -> 19/19 OK
- python3 inputs/clawscore-v0.2.3-gate/gate_v023.py <PR checkout> <main@58d4925 checkout> -> SUMMARY fail=0
  (Hark simulation of exactly this patch on 75fa8cf: pass=43 fail=0)
- make verify-offline, make export, make feed-check and make verify all exit 0; evidence SHA256SUMS OK
- CI verify (push and pull_request) green on the new HEAD
