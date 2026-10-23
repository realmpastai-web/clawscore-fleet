"""Gate for the scanner feed gap. Rules are inputs/rea-brief-scanner-feed-gap/BRIEF.md.

G1 checks SHA256SUMS and the pinned digests.
G2 recomputes held-ID TSVs from the frozen DB files.
G3 scores P1 and P2 once into SCORE.log. Invoke it only when `test ! -e SCORE.log` succeeds.
"""

from __future__ import annotations

import argparse
import hashlib
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(ROOT))

import grype_extract
import trivy_extract

BRIEF = ROOT / "inputs" / "rea-brief-scanner-feed-gap" / "BRIEF.md"
COUNTED = ROOT / "inputs" / "rea-brief-scanner-feed-gap" / "baseline"
SCORE = HERE / "SCORE.log"
GAP = HERE / "gap-ids.txt"
SUMS = HERE / "SHA256SUMS"
DIGESTS = HERE / "digests.txt"
FROZEN = HERE / "frozen"
VERSIONS = ("2026.6.10", "2026.4.22")
MAKER = {"2026.6.10": 58, "2026.4.22": 148}
TRIVY_DIGEST = "sha256:bc1ab2ce4f54245efb7861f81993c8abf4ae95aca67d00dce37c60dc59e7d415"
GRYPE_DIGEST = "fe51ed05fd0bf2e0642a362b75b245caf0da0eabb92b26a543e061f9873ec2ba"
LAYER = "sha256:3399c7b11c8c01d0423c115e938c30c05562cd5346ddcfc56db5197e79dd97d0"
ARCHIVE = "sha256:fe51ed05fd0bf2e0642a362b75b245caf0da0eabb92b26a543e061f9873ec2ba"
HELD_FILES = [
    "trivy-held-2026.6.10.tsv",
    "trivy-held-2026.4.22.tsv",
    "grype-held-2026.6.10.tsv",
    "grype-held-2026.4.22.tsv",
]


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_ids(path: Path) -> set[str]:
    lines = path.read_text().splitlines()
    if not lines:
        return set()
    index = lines[0].split("\t").index("advisory_id")
    return {line.split("\t")[index] for line in lines[1:] if line.strip()}


def counted(version: str) -> set[str]:
    return set((COUNTED / f"counted-{version}.txt").read_text().split())


def measure(payloads: dict[str, dict] | None = None) -> dict:
    held = {}
    if payloads is None:
        for version in VERSIONS:
            for name in ("trivy", "grype"):
                held[(name, version)] = load_ids(HERE / f"{name}-held-{version}.tsv")
    else:
        for version in VERSIONS:
            held[("trivy", version)] = trivy_extract.held_ids(payloads["trivy"], version)
            held[("grype", version)] = grype_extract.held_ids(payloads["grype"], version)
    q3 = {}
    gap: set[str] = set()
    for version in VERSIONS:
        base = counted(version)
        for name in ("trivy", "grype"):
            q3[(name, version)] = len(held[(name, version)] & base)
            gap |= base - held[(name, version)]
    return {"q3": q3, "gap": gap, "held": held}


def wording(db: str, digest: str, number: int, maker: int) -> str:
    return (
        f"{db} DB digest {digest} lists {number}; "
        f"the maker's repository lists {maker} (feed newest 2026-09-11)"
    )


def score_text(result: dict) -> str:
    q3 = result["q3"]
    p1 = q3[("trivy", "2026.6.10")] == 0 and q3[("grype", "2026.6.10")] == 0
    p2 = q3[("trivy", "2026.4.22")] <= 68 and q3[("grype", "2026.4.22")] <= 68
    lines = [
        f"P1 {'HOLD' if p1 else 'DOES_NOT_HOLD'}",
        f"P2 {'HOLD' if p2 else 'DOES_NOT_HOLD'}",
        wording("trivy", TRIVY_DIGEST, q3[("trivy", "2026.6.10")], 58),
        wording("trivy", TRIVY_DIGEST, q3[("trivy", "2026.4.22")], 148),
        wording("grype", GRYPE_DIGEST, q3[("grype", "2026.6.10")], 58),
        wording("grype", GRYPE_DIGEST, q3[("grype", "2026.4.22")], 148),
        f"gap_ids {len(result['gap'])}",
    ]
    return "\n".join(lines) + "\n"


def g1() -> list[str]:
    fails = []
    if not SUMS.is_file():
        print("FAIL\tG1\tSHA256SUMS missing")
        return ["G1"]
    bad = []
    for line in SUMS.read_text().splitlines():
        if not line.strip():
            continue
        digest, name = line.split("  ", 1)
        path = HERE / name
        if not path.is_file() or sha256_file(path) != digest:
            bad.append(name)
    if bad:
        fails.append("G1")
    print(("FAIL" if bad else "PASS") + "\tG1\tSHA256SUMS" + (f"\tbad={bad}" if bad else ""))
    brief = BRIEF.read_text()
    digests = DIGESTS.read_text()
    pin_bad = []
    for pin in (TRIVY_DIGEST, LAYER, ARCHIVE):
        if pin not in brief or pin not in digests:
            pin_bad.append(pin)
    layer = FROZEN / "trivy-layer.tar.gz"
    archive = FROZEN / "grype-db.tar.zst"
    if layer.is_file() and sha256_file(layer) != LAYER.removeprefix("sha256:"):
        pin_bad.append("trivy-layer")
    if archive.is_file() and sha256_file(archive) != ARCHIVE.removeprefix("sha256:"):
        pin_bad.append("grype-archive")
    if not layer.is_file() or not archive.is_file():
        pin_bad.append("frozen-blob-absent")
    if pin_bad:
        fails.append("G1.pins")
    print(("FAIL" if pin_bad else "PASS") + "\tG1\tpins" + (f"\tbad={pin_bad}" if pin_bad else ""))
    return fails


def render_expected() -> dict[str, str]:
    trivy = trivy_extract.load()
    grype = grype_extract.load()
    return {
        "trivy-held-2026.6.10.tsv": trivy_extract.render_held(trivy, "2026.6.10"),
        "trivy-held-2026.4.22.tsv": trivy_extract.render_held(trivy, "2026.4.22"),
        "grype-held-2026.6.10.tsv": grype_extract.render_held(grype, "2026.6.10"),
        "grype-held-2026.4.22.tsv": grype_extract.render_held(grype, "2026.4.22"),
        "trivy-sources.tsv": trivy_extract.render_sources(trivy),
        "grype-sources.tsv": grype_extract.render_sources(grype),
        "trivy-unresolved.tsv": trivy_extract.render_unresolved(trivy),
        "grype-unresolved.tsv": grype_extract.render_unresolved(grype),
    }


def g2(overrides: dict[str, Path]) -> list[str]:
    expected = render_expected()
    bad = []
    for name, text in expected.items():
        path = overrides.get(name, HERE / name)
        if not path.is_file() or path.read_text() != text:
            bad.append(name)
    if bad:
        print(f"FAIL\tG2\tbad={bad}")
        return ["G2"]
    print("PASS\tG2\theld-id TSVs match the frozen DB files")
    return []


def write_gap(result: dict) -> None:
    GAP.write_text("".join(item + "\n" for item in sorted(result["gap"])))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--score", action="store_true")
    parser.add_argument("--g2-only", action="store_true")
    parser.add_argument("--tsv", action="append", default=[])
    args = parser.parse_args(argv)
    if args.score and SCORE.exists():
        print("FAIL\tG3\tSCORE.log exists")
        return 1
    fails = []
    if not args.g2_only:
        fails.extend(g1())
    overrides = {}
    for item in args.tsv:
        name, path = item.split("=", 1)
        overrides[name] = Path(path)
    fails.extend(g2(overrides))
    result = measure()
    if fails:
        print(f"GATE FAIL {fails}")
        return 1
    if args.g2_only:
        print("G2 ONLY")
        return 0
    if not result["gap"]:
        (HERE / "NO-GO.md").write_text(
            "Both DBs cover ClawScore's counted set at 2026.6.10 and 2026.4.22. No export is built.\n"
            + score_text(result)
        )
        print("NO-GO")
        return 0
    if args.score:
        write_gap(result)
        SCORE.write_text(score_text(result))
        print("PASS\tG3\twrote SCORE.log")
        print(SCORE.read_text(), end="")
        print(f"PASS\tgap-ids\t{len(result['gap'])}")
        return 0
    if GAP.is_file():
        got = [line for line in GAP.read_text().splitlines() if line.strip()]
        if got != sorted(result["gap"]):
            print("FAIL\tgap-ids\tmismatch")
            return 1
        print(f"PASS\tgap-ids\t{len(got)}")
    print("GATE PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
