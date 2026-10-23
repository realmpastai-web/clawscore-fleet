# Addendum: replaying G2, and the REA record

This file is not the spec. The spec remains `inputs/rea-brief-scanner-feed-gap/BRIEF.md` at commit `56f0d92`. Its sha256 stays `9dbdd55f6a8c15529e1d3eea9e64a5eea388cdbb617b222d939986e0543adf29`. Nothing in this addendum changes that file.

## Held-ID sets

G2 compares these committed files with a fresh read of the frozen DB files. They are the extracted sets. They are not the DB blobs.

- `trivy-held-2026.6.10.tsv`
- `trivy-held-2026.4.22.tsv`
- `grype-held-2026.6.10.tsv`
- `grype-held-2026.4.22.tsv`
- `trivy-sources.tsv`
- `grype-sources.tsv`
- `trivy-unresolved.tsv`
- `grype-unresolved.tsv`

`frozen/` is gitignored. A checkout of this branch does not contain `frozen/trivy/trivy.db` or `frozen/grype/vulnerability.db`. G2 cannot replay until those two files are fetched.

## How to fetch and replay

From the repo root:

```bash
inputs/rea-scanner-feed-gap-evidence/fetch_frozen_dbs.sh
python3 inputs/rea-scanner-feed-gap-evidence/gate_feed_gap.py
```

`fetch_frozen_dbs.sh` does four checks and exits 1 on any mismatch. The downloaded temp file is removed on a mismatch.

1. Download the Trivy OCI manifest by digest `sha256:bc1ab2ce4f54245efb7861f81993c8abf4ae95aca67d00dce37c60dc59e7d415` from `ghcr.io/aquasecurity/trivy-db`. The script does not resolve tag `2`. It refuses unless the manifest body sha256 equals that digest, and unless the single layer digest is `sha256:3399c7b11c8c01d0423c115e938c30c05562cd5346ddcfc56db5197e79dd97d0`.
2. Download that layer blob and refuse unless its sha256 equals the layer digest. Unpack `trivy.db` and `metadata.json` into `frozen/trivy/`.
3. Download the Grype v6 archive from the pinned URL in `digests.txt`: `https://grype.anchore.io/databases/v6/vulnerability-db_v6.1.10_2026-10-21T00:28:41Z_1792564262.tar.zst`. The script does not read `latest.json`. It refuses unless the archive sha256 is `fe51ed05fd0bf2e0642a362b75b245caf0da0eabb92b26a543e061f9873ec2ba`.
4. Unpack `vulnerability.db` into `frozen/grype/`.

The Grype archive is zstd. Unpack uses the `zstd` command when it is on `PATH`. Otherwise it uses Python module `zstandard`. A checksum match with neither tool present exits 1 and leaves the verified archive at `frozen/grype-db.tar.zst`.

`gate_feed_gap.py` without `--score` checks G1, G2, and `gap-ids.txt`. `SCORE.log` is already present. Do not pass `--score`. A second score exits 1 and does not rewrite `SCORE.log`.

A local mismatch check, with no download:

```bash
inputs/rea-scanner-feed-gap-evidence/fetch_frozen_dbs.sh --verify-sha256 SOME_FILE fe51ed05fd0bf2e0642a362b75b245caf0da0eabb92b26a543e061f9873ec2ba
```

That exits 1 when `SOME_FILE` has a different sha256, and it deletes `SOME_FILE`. Point it at a copy.

## REA 6.7.0 issued no Evidence ID

`rea --version` printed `6.7.0`. `inspect-sqlite-database` issued no Evidence ID.

- `rea-grype-inventory.json`: `resource_constraint`. `frozen/grype/vulnerability.db` is 2507653120 bytes. That exceeds `sqlite_snapshot_input_bytes` 268435456.
- `rea-grype-snapshot.json`: `capability_unavailable`. Node v22.23.3 lacks `DatabaseSync.limits`. REA asked for Node.js 24.15+ or 26+. The snapshot it refused is `frozen/grype-openclaw.sqlite` (966656 bytes), which is gitignored and not an Evidence ID.

The held-ID TSVs were read with Python sqlite3 3.46.1 and `bbolt.py`. No trivy or grype binary was used for that read.
