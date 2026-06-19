#!/usr/bin/env python3
"""Stop hook: if any .md note in the technologies vault has uncommitted changes,
require changelog.md to have an entry for each unique mtime date.

Avoids date-rollover false positives: yesterday's still-uncommitted edits are
covered by yesterday's changelog entry, not today's.

Exit codes:
  0  pass (no vault, no changes, or all dates covered)
  2  block — changelog missing entries for one or more dates
  1  unexpected error
"""

import os
import subprocess
import sys
from datetime import datetime
from pathlib import Path

TECH_VAULT = Path(
    os.environ.get("TECH_VAULT_PATH", "C:/Users/klein/obsidian/technologies")
)


def parse_porcelain(line):
    """Extract the path from a `git status --porcelain` line."""
    # Format: "XY path" or "XY orig -> path" (rename); paths may be quoted.
    if not line or len(line) < 4:
        return None
    rest = line[3:]
    if " -> " in rest:
        rest = rest.split(" -> ", 1)[1]
    rest = rest.strip()
    if rest.startswith('"') and rest.endswith('"'):
        rest = rest[1:-1]
    return rest


def main():
    if not TECH_VAULT.is_dir():
        return 0

    try:
        result = subprocess.run(
            ["git", "-C", str(TECH_VAULT), "status", "--porcelain"],
            capture_output=True, text=True, timeout=10,
        )
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return 0

    if result.returncode != 0 or not result.stdout.strip():
        return 0

    changed_paths = []
    for line in result.stdout.splitlines():
        rel = parse_porcelain(line)
        if not rel or not rel.endswith(".md"):
            continue
        if os.path.basename(rel).lower() == "changelog.md":
            continue
        full = TECH_VAULT / rel
        if full.is_file():
            changed_paths.append(full)

    if not changed_paths:
        return 0

    names = sorted({p.stem for p in changed_paths})
    changelog = TECH_VAULT / "changelog.md"

    if not changelog.is_file():
        sys.stderr.write(
            f"TECH VAULT GATE: Notes changed in technologies vault "
            f"({', '.join(names)}) but changelog.md is missing.\n"
        )
        return 2

    text = changelog.read_text(encoding="utf-8")
    changed_dates = sorted({
        datetime.fromtimestamp(p.stat().st_mtime).strftime("%Y-%m-%d")
        for p in changed_paths
    })
    missing = [d for d in changed_dates if d not in text]

    if not missing:
        return 0

    sys.stderr.write(
        f"TECH VAULT GATE: Notes changed in technologies vault "
        f"({', '.join(names)}) but changelog.md has no entry for "
        f"{', '.join(missing)}. Add a changelog section before finishing.\n"
    )
    return 2


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:
        sys.stderr.write(f"Tech changelog hook failed: {e}\n")
        sys.exit(1)
