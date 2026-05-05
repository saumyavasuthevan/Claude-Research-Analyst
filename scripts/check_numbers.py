#!/usr/bin/env python3
"""
Verifies that every unitised numeric value adjacent to a SRC:id citation in a report
appears in the quote field of the corresponding fact_registry entry.

Design decisions to minimise false positives:
  - Only checks numbers WITH a recognised unit (%, M, B, K, billion, million, thousand, percent).
    Bare integers and 4-digit years are excluded.
  - Nearest-SRC ownership: a number is only checked against the SRC:id closest to it by
    character distance. Prevents numbers from adjacent table cells being attributed to the
    wrong citation.
  - Magnitude-tolerant comparison: 17,560M and 17.6B resolve to the same base value
    (within 2% tolerance). Percentages are compared exactly (within 0.05pp).

Usage:
  python3 scripts/check_numbers.py <report.md> <fact_registry.json> [...]

Multiple registries are merged before lookup (supports multi-registry reports).

Exit 0 = no mismatches
Exit 1 = mismatches found — fix the claim or update the quote field in the registry
"""

import json
import re
import sys
from pathlib import Path
from typing import List, Optional, Set, Tuple

WINDOW_BACK = 100   # chars before the SRC:id — where the cited claim normally sits
WINDOW_FWD  = 30    # chars after — small allowance for "SRC:id shows that 5.3M…" style

SRC_PATTERN = re.compile(r"\bSRC:[a-zA-Z0-9_]+")

# Matches agent-applied labels that explicitly acknowledge missing/uncertain data
LABELED_PATTERN = re.compile(
    r"\[(UNVERIFIED|SEARCH FAILED|ASSUMPTION|INSUFFICIENT DATA|URL NOT RETRIEVED|FETCH FAILED)[^\]]*\]",
    re.IGNORECASE,
)

NUMBER_UNIT_PATTERN = re.compile(
    r"\b(\d[\d,\.]*)\s*(percent|billion|million|thousand|bn|mn|[BMKT%](?!\w))\b",
    re.IGNORECASE,
)

_UNIT_NORM = {
    "percent": "%", "%": "%",
    "b": "billion", "bn": "billion", "billion": "billion",
    "m": "million", "mn": "million", "million": "million",
    "t": "thousand", "k": "thousand", "thousand": "thousand",
}

_UNIT_SCALE = {
    "billion": 1e9,
    "million": 1e6,
    "thousand": 1e3,
}


def _parse(raw_num: str, raw_unit: str) -> Optional[Tuple[float, str]]:
    try:
        val = float(raw_num.replace(",", ""))
    except ValueError:
        return None
    unit = _UNIT_NORM.get(raw_unit.lower().rstrip(), raw_unit.lower())
    return (val, unit)


def _to_comparable(val: float, unit: str) -> Tuple[str, float]:
    """Return a (kind, magnitude) pair for tolerance-based comparison."""
    scale = _UNIT_SCALE.get(unit)
    if scale is not None:
        return ("mag", val * scale)
    return ("%", val)  # percentages compared as-is


def _close(a: Tuple[str, float], b: Tuple[str, float]) -> bool:
    if a[0] != b[0]:
        return False
    if a[0] == "%":
        return abs(a[1] - b[1]) < 0.051  # within 0.05pp
    ref = max(abs(a[1]), abs(b[1]))
    if ref == 0:
        return True
    return abs(a[1] - b[1]) / ref < 0.02  # within 2% for magnitudes


def extract_numbers(text: str) -> Set[Tuple[float, str]]:
    results = set()
    for m in NUMBER_UNIT_PATTERN.finditer(text):
        pair = _parse(m.group(1), m.group(2))
        if pair is not None:
            results.add(pair)
    return results


def load_registries(paths: List[Path]) -> dict:
    merged: dict = {}
    for path in paths:
        with open(path) as f:
            merged.update(json.load(f))
    return merged


def check_report(report_path: Path, registry: dict) -> List[dict]:
    text = report_path.read_text()

    # Index all SRC:id positions for ownership checks
    src_positions = [(m.start(), m.group()) for m in SRC_PATTERN.finditer(text)]

    mismatches: List[dict] = []
    seen: Set[tuple] = set()

    for src_pos, src_id in src_positions:
        entry = registry.get(src_id)
        if entry is None:
            continue

        quote = entry.get("quote", "")
        if not quote or quote.startswith("[FETCH FAILED"):
            continue

        quote_comparable = {_to_comparable(v, u) for v, u in extract_numbers(quote)}

        window_start = max(0, src_pos - WINDOW_BACK)
        window_end   = min(len(text), src_pos + len(src_id) + WINDOW_FWD)

        # Skip dense citation zones (>2 other SRC:ids in window) — attribution unreliable
        other_in_window = sum(
            1 for op, _ in src_positions
            if op != src_pos and window_start <= op <= window_end
        )
        if other_in_window > 2:
            continue

        orphaned = []
        for num_m in NUMBER_UNIT_PATTERN.finditer(text, window_start, window_end):
            num_pos = num_m.start()
            pair = _parse(num_m.group(1), num_m.group(2))
            if pair is None:
                continue

            # Skip numbers that already carry an explicit agent label (UNVERIFIED, etc.)
            near_text = text[max(0, num_pos - 10): min(len(text), num_pos + 80)]
            if LABELED_PATTERN.search(near_text):
                continue

            # Ownership: only flag if this SRC:id is the nearest one to this number
            dist = abs(num_pos - src_pos)
            if any(abs(num_pos - op) < dist for op, _ in src_positions if op != src_pos):
                continue

            cmp = _to_comparable(*pair)
            if not any(_close(cmp, q) for q in quote_comparable):
                orphaned.append(pair)

        if not orphaned:
            continue

        key = (src_id, tuple(sorted(orphaned)))
        if key in seen:
            continue
        seen.add(key)

        snippet = text[window_start:window_end].replace("\n", " ").strip()[:120]
        orphaned_str = ", ".join(f"{v:g}{u}" for v, u in sorted(orphaned))
        mismatches.append(
            {
                "src_id": src_id,
                "orphaned": orphaned_str,
                "snippet": snippet,
                "quote": quote[:120],
            }
        )

    return mismatches


def main() -> int:
    if len(sys.argv) < 3:
        print("Usage: python3 scripts/check_numbers.py <report.md> <fact_registry.json> [...]")
        return 1

    report_path = Path(sys.argv[1])
    registry_paths = [Path(p) for p in sys.argv[2:]]

    for p in [report_path, *registry_paths]:
        if not p.exists():
            print(f"ERROR: {p} not found")
            return 1

    registry = load_registries(registry_paths)
    mismatches = check_report(report_path, registry)

    if mismatches:
        print(f"\n❌ NUMBER CHECK FAILED — {len(mismatches)} mismatch(es):\n")
        col = 42
        print(f"{'SRC:id':<{col}} {'Orphaned (claim)':<32} Snippet")
        print("-" * 118)
        for item in mismatches:
            print(f"{item['src_id']:<{col}} {item['orphaned']:<32} {item['snippet']}")
            print(f"  → quote: {item['quote']}")
            print()
        print("Fix: correct the claim to match the source quote, or update the quote field in the registry.")
        return 1

    print("✅ NUMBER CHECK PASSED — all cited unitised numbers match source quotes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
