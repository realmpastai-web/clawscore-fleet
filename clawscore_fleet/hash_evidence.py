"""sha256 every evidence file except the frozen landscape and this sums file."""

from __future__ import annotations

import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "evidence"


def main() -> int:
    lines = []
    for path in sorted(EVIDENCE.rglob("*")):
        if not path.is_file():
            continue
        rel = path.relative_to(EVIDENCE)
        if rel.parts and rel.parts[0] == "landscape":
            continue
        if path.name == "SHA256SUMS":
            continue
        if rel.as_posix() == "matrix/listings.json":
            continue
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        lines.append(f"{digest}  {rel.as_posix()}")
    text = "\n".join(lines) + ("\n" if lines else "")
    (EVIDENCE / "SHA256SUMS").write_text(text)
    print(f"hashed {len(lines)} evidence files", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
