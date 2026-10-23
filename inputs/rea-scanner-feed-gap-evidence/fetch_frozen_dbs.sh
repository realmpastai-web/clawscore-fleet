#!/usr/bin/env bash
# Fetch the pinned Trivy DB and Grype v6 archive, then unpack them for G2.
# Pins are the digests in inputs/rea-brief-scanner-feed-gap/BRIEF.md.
# This script does not read the moving tag "2" or latest.json.
# A checksum mismatch removes the downloaded temp file and exits 1.
set -euo pipefail

HERE="$(cd "$(dirname "$0")" && pwd)"
FROZEN="${HERE}/frozen"

TRIVY_MANIFEST="sha256:bc1ab2ce4f54245efb7861f81993c8abf4ae95aca67d00dce37c60dc59e7d415"
TRIVY_LAYER="sha256:3399c7b11c8c01d0423c115e938c30c05562cd5346ddcfc56db5197e79dd97d0"
GRYPE_SHA256="fe51ed05fd0bf2e0642a362b75b245caf0da0eabb92b26a543e061f9873ec2ba"
GRYPE_URL="https://grype.anchore.io/databases/v6/vulnerability-db_v6.1.10_2026-10-21T00:28:41Z_1792564262.tar.zst"

refuse() {
  echo "REFUSE $*" >&2
  exit 1
}

sha256_file() {
  sha256sum "$1" | awk '{print $1}'
}

verify_sha256() {
  local path="$1"
  local expected="$2"
  local label="$3"
  local got
  got="$(sha256_file "$path")"
  if [[ "$got" != "$expected" ]]; then
    rm -f "$path"
    refuse "${label} sha256 ${got} != ${expected}"
  fi
  echo "OK ${label} ${got}"
}

if [[ "${1:-}" == "--verify-sha256" ]]; then
  [[ $# -eq 3 ]] || refuse "usage: $0 --verify-sha256 FILE HEX"
  verify_sha256 "$2" "$3" "check"
  exit 0
fi

if [[ $# -ne 0 ]]; then
  refuse "usage: $0    or    $0 --verify-sha256 FILE HEX"
fi

mkdir -p "$FROZEN"
work="$(mktemp -d)"
trap 'rm -rf "$work"' EXIT

curl_fetch() {
  curl --fail --location --retry 5 --retry-delay 2 --retry-all-errors --silent --show-error "$@"
}

echo "FETCH trivy manifest ${TRIVY_MANIFEST}"
token="$(curl_fetch "https://ghcr.io/token?service=ghcr.io&scope=repository:aquasecurity/trivy-db:pull" \
  | python3 -c 'import json,sys; print(json.load(sys.stdin)["token"])')"
[[ -n "$token" ]] || refuse "ghcr token empty"

curl_fetch \
  -D "$work/trivy-manifest.headers" \
  -H "Authorization: Bearer ${token}" \
  -H "Accept: application/vnd.oci.image.manifest.v1+json" \
  -o "$work/trivy-manifest.json" \
  "https://ghcr.io/v2/aquasecurity/trivy-db/manifests/${TRIVY_MANIFEST}"
verify_sha256 "$work/trivy-manifest.json" "${TRIVY_MANIFEST#sha256:}" "trivy-manifest"

header_digest="$(awk 'tolower($1)=="docker-content-digest:" {print $2}' "$work/trivy-manifest.headers" | tr -d '\r' | tail -n 1)"
if [[ -n "$header_digest" && "$header_digest" != "$TRIVY_MANIFEST" ]]; then
  refuse "trivy docker-content-digest ${header_digest} != ${TRIVY_MANIFEST}"
fi
echo "OK trivy-manifest-header ${header_digest:-absent}"

python3 - "$work/trivy-manifest.json" "$TRIVY_LAYER" <<'PY'
import json
import sys

path, want = sys.argv[1], sys.argv[2]
manifest = json.load(open(path))
layers = manifest.get("layers") or []
if len(layers) != 1:
    sys.exit(f"REFUSE trivy manifest layer count {len(layers)} != 1")
got = layers[0].get("digest")
if got != want:
    sys.exit(f"REFUSE trivy layer digest {got} != {want}")
print(f"OK trivy-manifest-layer {got}")
PY

echo "FETCH trivy layer ${TRIVY_LAYER}"
curl_fetch \
  -H "Authorization: Bearer ${token}" \
  -o "$work/trivy-layer.tar.gz" \
  "https://ghcr.io/v2/aquasecurity/trivy-db/blobs/${TRIVY_LAYER}"
verify_sha256 "$work/trivy-layer.tar.gz" "${TRIVY_LAYER#sha256:}" "trivy-layer"
mv "$work/trivy-layer.tar.gz" "$FROZEN/trivy-layer.tar.gz"

mkdir -p "$FROZEN/trivy"
tar -xzf "$FROZEN/trivy-layer.tar.gz" -C "$FROZEN/trivy"
[[ -f "$FROZEN/trivy/trivy.db" ]] || refuse "trivy archive has no trivy.db"
echo "OK trivy-unpacked $FROZEN/trivy/trivy.db"

echo "FETCH grype archive ${GRYPE_URL}"
curl_fetch -o "$work/grype-db.tar.zst" "$GRYPE_URL"
verify_sha256 "$work/grype-db.tar.zst" "$GRYPE_SHA256" "grype-archive"
mv "$work/grype-db.tar.zst" "$FROZEN/grype-db.tar.zst"

mkdir -p "$FROZEN/grype"
if command -v zstd >/dev/null 2>&1; then
  zstd -dc "$FROZEN/grype-db.tar.zst" | tar -x -C "$FROZEN/grype" vulnerability.db
else
  python3 - "$FROZEN/grype-db.tar.zst" "$FROZEN/grype/vulnerability.db" <<'PY'
import shutil
import sys
import tarfile

try:
    import zstandard
except ImportError:
    sys.exit("REFUSE grype archive checksum matched; unpack needs zstd or Python module zstandard")

src, dst = sys.argv[1], sys.argv[2]
found = False
dctx = zstandard.ZstdDecompressor()
with open(src, "rb") as handle:
    reader = dctx.stream_reader(handle)
    with tarfile.open(fileobj=reader, mode="r|") as archive:
        for member in archive:
            name = member.name.removeprefix("./")
            if name != "vulnerability.db":
                continue
            extracted = archive.extractfile(member)
            if extracted is None:
                sys.exit("REFUSE grype archive member vulnerability.db is not a file")
            with open(dst, "wb") as out:
                shutil.copyfileobj(extracted, out)
            found = True
            break
if not found:
    sys.exit("REFUSE grype archive has no vulnerability.db")
print("OK grype-unpacked", dst)
PY
fi
[[ -f "$FROZEN/grype/vulnerability.db" ]] || refuse "grype unpack did not write vulnerability.db"
echo "OK grype-db $FROZEN/grype/vulnerability.db"
echo "FETCH DONE"
