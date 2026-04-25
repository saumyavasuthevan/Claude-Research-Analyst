#!/usr/bin/env python3
"""
Renders the Source Registry appendix from a fact_registry JSON file.

The appendix lists every registered source with its type badge and confidence note.
It is appended to the bottom of the report, keeping the report body clean while
making source metadata fully auditable.

Usage:
  python3 scripts/render.py <fact_registry.json>
  python3 scripts/render.py <fact_registry.json> >> report.md

Output: markdown section (stdout).
"""

import json
import sys
from pathlib import Path

BADGE = {
    "tier1_official": "✅ tier1\_official",
    "tier2_news": "🔵 tier2\_news",
}


def render_appendix(registry_path: Path) -> str:
    with open(registry_path) as f:
        registry = json.load(f)

    lines = [
        "",
        "---",
        "",
        "## Source Registry",
        "",
        f"*Generated from `{registry_path.name}` — {len(registry)} source(s)*",
        "",
        "| Fact ID | Title | Source Type | Fetched | Note |",
        "|---|---|---|---|---|",
    ]

    for src_id, entry in sorted(registry.items()):
        title = entry.get("title", "—")
        source_type = entry.get("source_type", "")
        badge = BADGE.get(source_type, f"❌ {source_type or 'missing'}")
        fetched_at = entry.get("fetched_at", "—")
        note = entry.get("confidence_reason") or "—"

        lines.append(f"| `{src_id}` | {title} | {badge} | {fetched_at} | {note} |")

    return "\n".join(lines)


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: python3 scripts/render.py <fact_registry.json>")
        return 1

    path = Path(sys.argv[1])
    if not path.exists():
        print(f"ERROR: {path} not found")
        return 1

    print(render_appendix(path))
    return 0


if __name__ == "__main__":
    sys.exit(main())
