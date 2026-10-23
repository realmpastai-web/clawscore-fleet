"""Read-only bbolt (etcd-io/bbolt v1.3.11 page layout) walker.

Used on the trivy-db file. It does not execute anything stored in the database.
"""

from __future__ import annotations

import mmap
import struct
from typing import Iterator

MAGIC = 0xED0CDAED
BRANCH = 0x01
LEAF = 0x02
META = 0x04
BUCKET_LEAF = 0x01
FNV_OFFSET = 14695981039346656037
FNV_PRIME = 1099511628211


def _fnv64a(data: bytes) -> int:
    hash_value = FNV_OFFSET
    for byte in data:
        hash_value ^= byte
        hash_value = (hash_value * FNV_PRIME) & 0xFFFFFFFFFFFFFFFF
    return hash_value


def _u16(buf: mmap.mmap, offset: int) -> int:
    return struct.unpack_from("<H", buf, offset)[0]


def _u32(buf: mmap.mmap, offset: int) -> int:
    return struct.unpack_from("<I", buf, offset)[0]


def _u64(buf: mmap.mmap, offset: int) -> int:
    return struct.unpack_from("<Q", buf, offset)[0]


class BoltDB:
    def __init__(self, path: str):
        self._file = open(path, "rb")
        self.mm = mmap.mmap(self._file.fileno(), 0, access=mmap.ACCESS_READ)
        page_size = _u32(self.mm, 24)
        if page_size == 0 or page_size > 1 << 24:
            raise ValueError(f"implausible page size {page_size}")
        first = self._read_meta(0, page_size)
        second = self._read_meta(page_size, page_size)
        valid = [item for item in (first, second) if item is not None]
        if not valid:
            raise ValueError("no valid bbolt meta page")
        self.meta = max(valid, key=lambda item: item["txid"])
        self.page_size = self.meta["page_size"]

    def close(self) -> None:
        self.mm.close()
        self._file.close()

    def _read_meta(self, offset: int, page_size: int) -> dict | None:
        if offset + 16 + 64 > len(self.mm):
            return None
        flags = _u16(self.mm, offset + 8)
        if flags != META:
            return None
        magic = _u32(self.mm, offset + 16)
        if magic != MAGIC:
            return None
        meta_bytes = self.mm[offset + 16 : offset + 16 + 64]
        if _fnv64a(meta_bytes[:56]) != _u64(self.mm, offset + 16 + 56):
            return None
        version = _u32(self.mm, offset + 20)
        stored_page = _u32(self.mm, offset + 24)
        if stored_page != page_size:
            return None
        return {
            "version": version,
            "page_size": stored_page,
            "root": _u64(self.mm, offset + 32),
            "sequence": _u64(self.mm, offset + 40),
            "freelist": _u64(self.mm, offset + 48),
            "pgid": _u64(self.mm, offset + 56),
            "txid": _u64(self.mm, offset + 64),
        }

    def root_entries(self) -> Iterator[tuple[bytes, bytes, int]]:
        yield from self._walk(self.meta["root"], None)

    def bucket(self, *names: bytes) -> Iterator[tuple[bytes, bytes, int]]:
        root = self.meta["root"]
        inline = None
        for name in names:
            found = None
            for key, value, flags in self._walk(root, inline):
                if key == name and flags & BUCKET_LEAF:
                    found = value
                    break
            if found is None:
                return
            root, inline = self._open_bucket(found)
        yield from self._walk(root, inline)

    def _open_bucket(self, value: bytes) -> tuple[int, bytes | None]:
        root = struct.unpack_from("<Q", value, 0)[0]
        if root == 0:
            return 0, value[16:]
        return root, None

    def _walk(self, root: int, inline: bytes | None) -> Iterator[tuple[bytes, bytes, int]]:
        if inline is not None:
            yield from self._walk_buffer(inline, 0)
            return
        yield from self._walk_page(root)

    def _walk_page(self, pgid: int) -> Iterator[tuple[bytes, bytes, int]]:
        base = pgid * self.page_size
        flags = _u16(self.mm, base + 8)
        count = _u16(self.mm, base + 10)
        if flags & BRANCH:
            for index in range(count):
                element = base + 16 + index * 16
                child = _u64(self.mm, element + 8)
                yield from self._walk_page(child)
            return
        if flags & LEAF:
            yield from self._walk_buffer(self.mm, base)
            return
        raise ValueError(f"unexpected page flags {flags:#x} at {pgid}")

    def _walk_buffer(self, buf, base: int) -> Iterator[tuple[bytes, bytes, int]]:
        flags = struct.unpack_from("<H", buf, base + 8)[0]
        count = struct.unpack_from("<H", buf, base + 10)[0]
        if flags & BRANCH:
            for index in range(count):
                element = base + 16 + index * 16
                child = struct.unpack_from("<Q", buf, element + 8)[0]
                if isinstance(buf, mmap.mmap):
                    yield from self._walk_page(child)
                else:
                    raise ValueError("inline branch page is not supported")
            return
        if not flags & LEAF:
            raise ValueError(f"unexpected buffer flags {flags:#x}")
        for index in range(count):
            element = base + 16 + index * 16
            leaf_flags, pos, key_size, value_size = struct.unpack_from("<IIII", buf, element)
            start = element + pos
            key = bytes(buf[start : start + key_size])
            value = bytes(buf[start + key_size : start + key_size + value_size])
            yield key, value, leaf_flags
