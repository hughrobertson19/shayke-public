#!/usr/bin/env python3
"""Recompute the ledger hash chain and exit non-zero on any break.

Each day record under `ledger/days/YYYY-MM-DD.json` carries a `prev_hash` and a
`hash`. The `hash` is the sha256 of the canonical JSON (sorted keys, no
whitespace) of the record with `hash` removed and `prev_hash` included. The
first day's `prev_hash` is 64 zeros; every later day's `prev_hash` must equal
the previous day's `hash`.

This script is deliberately dependency-free and standalone so it can run in the
test suite and from a bare checkout.
"""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

ZERO = "0" * 64


def canonical_hash(record: dict) -> str:
    payload = {k: v for k, v in record.items() if k != "hash"}
    canon = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(canon.encode("utf-8")).hexdigest()


def day_files(days_dir: Path) -> list[Path]:
    return sorted(days_dir.glob("*.json"), key=lambda p: p.name)


def verify(days_dir: Path) -> list[str]:
    errors: list[str] = []
    prev = ZERO
    files = day_files(days_dir)
    if not files:
        return ["no day records found under ledger/days/"]
    for path in files:
        try:
            rec = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, ValueError) as exc:
            errors.append(f"{path.name}: unreadable ({exc})")
            return errors
        want = canonical_hash(rec)
        if rec.get("hash") != want:
            errors.append(f"{path.name}: stored hash {rec.get('hash')!r} != recomputed {want!r}")
        if rec.get("prev_hash") != prev:
            errors.append(f"{path.name}: prev_hash {rec.get('prev_hash')!r} != prior hash {prev!r}")
        prev = rec.get("hash") or want
    return errors


def main() -> int:
    days_dir = Path(__file__).resolve().parent / "days"
    errors = verify(days_dir)
    if errors:
        print("CHAIN BROKEN:")
        for e in errors:
            print(f"  - {e}")
        return 1
    print(f"chain OK — {len(day_files(days_dir))} day record(s) verify.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
