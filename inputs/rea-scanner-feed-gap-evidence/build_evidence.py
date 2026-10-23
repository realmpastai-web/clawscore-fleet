"""Write Step 1 evidence from the frozen DB files.

Schema text is written to recon.log before any ID-list TSV is opened.
"""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import grype_extract
import trivy_extract

PINS = {
    "trivy_manifest": "sha256:bc1ab2ce4f54245efb7861f81993c8abf4ae95aca67d00dce37c60dc59e7d415",
    "trivy_layer": "sha256:3399c7b11c8c01d0423c115e938c30c05562cd5346ddcfc56db5197e79dd97d0",
    "grype_archive": "sha256:fe51ed05fd0bf2e0642a362b75b245caf0da0eabb92b26a543e061f9873ec2ba",
}
GRYPE_URL = (
    "https://grype.anchore.io/databases/v6/"
    "vulnerability-db_v6.1.10_2026-10-21T00:28:41Z_1792564262.tar.zst"
)
REA = "/home/box/.npm/_npx/a1722018f28f9df2/node_modules/.bin/rea"
FROZEN = HERE / "frozen"
RECON = HERE / "recon.log"


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    layer = FROZEN / "trivy-layer.tar.gz"
    archive = FROZEN / "grype-db.tar.zst"
    layer_hash = sha256_file(layer)
    archive_hash = sha256_file(archive)
    if "sha256:" + layer_hash != PINS["trivy_layer"]:
        raise SystemExit(f"trivy layer pin mismatch {layer_hash}")
    if "sha256:" + archive_hash != PINS["grype_archive"]:
        raise SystemExit(f"grype archive pin mismatch {archive_hash}")
    digests = (
        f"trivy_manifest {PINS['trivy_manifest']}\n"
        f"trivy_layer sha256:{layer_hash}\n"
        f"grype_archive sha256:{archive_hash}\n"
        f"grype_url {GRYPE_URL}\n"
    )
    (HERE / "digests.txt").write_text(digests)

    meta = json.loads((FROZEN / "trivy" / "metadata.json").read_text())
    schema = grype_extract.schema_sql()
    RECON.write_text(
        "\n".join(
            [
                "schema recorded before ID-list TSVs",
                f"trivy metadata.json {json.dumps(meta, sort_keys=True)}",
                f"trivy bbolt meta will be read next; layer sha256 {layer_hash}",
                "grype sqlite_master tables used by grype_extract.sql:",
                schema.rstrip(),
                "",
            ]
        )
    )

    snapshot = FROZEN / "grype-openclaw.sqlite"
    grype_extract.build_snapshot(snapshot)
    rea_out = HERE / "rea-grype-snapshot.json"
    version = subprocess.run([REA, "--version"], check=True, capture_output=True, text=True)
    inspected = subprocess.run(
        [
            REA,
            "inspect-sqlite-database",
            str(snapshot),
            "--schema-scope",
            "database",
            "--format",
            "json",
        ],
        capture_output=True,
        text=True,
    )
    rea_out.write_text(inspected.stdout or inspected.stderr)
    with RECON.open("a") as handle:
        handle.write(f"rea --version\n{version.stdout}\n")
        handle.write(f"rea inspect exit {inspected.returncode}\n")
        handle.write(f"rea snapshot bytes {snapshot.stat().st_size}\n")
        handle.write("full-db refusal is rea-grype-inventory.json\n")

    print("loading trivy", flush=True)
    trivy = trivy_extract.load()
    print("loading grype", flush=True)
    grype = grype_extract.load()
    files = {
        "trivy-sources.tsv": trivy_extract.render_sources(trivy),
        "grype-sources.tsv": grype_extract.render_sources(grype),
        "trivy-unresolved.tsv": trivy_extract.render_unresolved(trivy),
        "grype-unresolved.tsv": grype_extract.render_unresolved(grype),
    }
    for version in trivy_extract.VERSIONS:
        files[f"trivy-held-{version}.tsv"] = trivy_extract.render_held(trivy, version)
        files[f"grype-held-{version}.tsv"] = grype_extract.render_held(grype, version)
    for name, text in files.items():
        (HERE / name).write_text(text)
        print(f"wrote {name} bytes {len(text)}", flush=True)
    return 0 if inspected.returncode == 0 else inspected.returncode


if __name__ == "__main__":
    raise SystemExit(main())
