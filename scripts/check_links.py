#!/usr/bin/env python3
"""
HTTP-validates every URL in one or more fact_registry JSON files.

For each entry:
  - 2xx → adds url_status: "ok" (in-place)
  - 4xx / 5xx / timeout → sets url to "[URL NOT RETRIEVED — <status>]",
    overwrites quote with "[FETCH FAILED — <status> at <date>]",
    adds url_status: "<code>"

Writes patched registries back to disk.

Usage:
  python3 scripts/check_links.py <fact_registry.json> [...]

Exit 0 = all URLs ok or already marked
Exit 1 = one or more URLs newly patched as broken
"""

import json
import sys
import time
import urllib.error
import urllib.request
from datetime import date
from pathlib import Path
from typing import List

TIMEOUT = 10
SLEEP_BETWEEN = 2
SKIP_PREFIX = "[URL NOT RETRIEVED"

HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; fact-registry-checker/1.0)"}


def _fetch_status(url: str) -> str:
    """Return HTTP status code as string, or an error label on failure."""
    req = urllib.request.Request(url, headers=HEADERS, method="GET")
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            return str(resp.status)
    except urllib.error.HTTPError as exc:
        return str(exc.code)
    except urllib.error.URLError as exc:
        return f"URLError:{exc.reason}"
    except Exception as exc:  # noqa: BLE001
        return f"Error:{type(exc).__name__}"


def check_registry(registry_path: Path) -> List[str]:
    with open(registry_path) as f:
        registry = json.load(f)

    violations: List[str] = []
    modified = False

    for src_id, entry in registry.items():
        url = entry.get("url", "")

        if not url or url.startswith(SKIP_PREFIX):
            continue

        time.sleep(SLEEP_BETWEEN)

        status = _fetch_status(url)
        ok = status.isdigit() and 200 <= int(status) < 300

        if ok:
            entry["url_status"] = "ok"
        else:
            today = date.today().isoformat()
            original_url = url
            entry["url"] = f"[URL NOT RETRIEVED — {status}]"
            entry["quote"] = f"[FETCH FAILED — HTTP {status} at {today}]"
            entry["url_status"] = status
            modified = True
            violations.append(f"  {src_id}: {original_url} → {status}")

    if modified:
        with open(registry_path, "w") as f:
            json.dump(registry, f, indent=2)

    return violations


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: python3 scripts/check_links.py <fact_registry.json> [...]")
        return 1

    all_violations: List[str] = []

    for path_str in sys.argv[1:]:
        path = Path(path_str)
        if not path.exists():
            print(f"ERROR: {path} not found")
            return 1
        violations = check_registry(path)
        for v in violations:
            all_violations.append(f"[{path.name}]{v}")

    if all_violations:
        print(f"\n❌ LINK CHECK FAILED — {len(all_violations)} broken URL(s) patched in registry:\n")
        for v in all_violations:
            print(v)
        print(
            "\nAffected entries have been updated to [URL NOT RETRIEVED] in the registry."
            "\nRe-source these claims or label them [UNVERIFIED — source URL inaccessible]."
        )
        return 1

    print("✅ LINK CHECK PASSED — all URLs reachable")
    return 0


if __name__ == "__main__":
    sys.exit(main())
