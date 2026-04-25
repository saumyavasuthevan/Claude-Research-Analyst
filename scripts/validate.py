#!/usr/bin/env python3
"""
Validates fact_registry JSON files produced by the create-company agent.

Gates (in order):
  1. Domain not in KNOWN_BAD (hard block — overrides declared type)
  2. source_type field present and is a valid enum value (tier1_official | tier2_news)
  3. All other required FactSource fields present (url, title, fetched_at, quote)

Usage:
  python3 scripts/validate.py <fact_registry.json> [fact_registry2.json ...]

Exit 0 = all registries valid.
Exit 1 = violations found — do not write the report until fixed.
"""

import json
import sys
from pathlib import Path
from urllib.parse import urlparse

sys.path.insert(0, str(Path(__file__).parent))
from schemas import FactSource, KNOWN_BAD  # noqa: E402

from pydantic import ValidationError


def get_domain(url: str) -> str:
    return urlparse(url).netloc.removeprefix("www.")


def validate_registry(registry_path: Path) -> list[dict]:
    errors: list[dict] = []

    try:
        with open(registry_path) as f:
            registry = json.load(f)
    except json.JSONDecodeError as exc:
        return [{"id": str(registry_path), "error": f"invalid JSON: {exc}"}]

    for src_id, entry in registry.items():
        url = entry.get("url", "")
        domain = get_domain(url)

        # Gate 1: KNOWN_BAD — hard block regardless of declared source_type
        if domain in KNOWN_BAD:
            errors.append({
                "id": src_id,
                "domain": domain,
                "error": (
                    f"'{domain}' is a blocked aggregator domain. "
                    "Replace with a tier1_official or tier2_news source, "
                    "or remove and label the claim [UNVERIFIED]."
                ),
            })
            continue

        # Gate 2 + 3: validate against FactSource schema (enforces source_type enum + required fields)
        try:
            FactSource.model_validate(entry)
        except ValidationError as exc:
            for err in exc.errors():
                field = " → ".join(str(x) for x in err["loc"])
                errors.append({
                    "id": src_id,
                    "field": field,
                    "error": err["msg"],
                })

    return errors


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: python3 scripts/validate.py <fact_registry.json> [...]")
        return 1

    all_errors: list[dict] = []

    for path_str in sys.argv[1:]:
        path = Path(path_str)
        if not path.exists():
            print(f"ERROR: {path} not found")
            return 1

        errors = validate_registry(path)
        for e in errors:
            e["file"] = str(path)
        all_errors.extend(errors)

    if all_errors:
        print(f"\n❌ VALIDATION FAILED — {len(all_errors)} violation(s):\n")
        for e in all_errors:
            loc = e.get("field") or e.get("domain") or ""
            loc_str = f" [{loc}]" if loc else ""
            print(f"  [{e['file']}] {e['id']}{loc_str}: {e['error']}")
        print("\nFix all violations and re-run before writing the report.")
        return 1

    print("✅ VALIDATION PASSED — all sources verified")
    return 0


if __name__ == "__main__":
    sys.exit(main())
