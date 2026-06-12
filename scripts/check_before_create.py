#!/usr/bin/env python3
"""
Check for existing notes before creating a new one.
Searches filenames and frontmatter aliases for conflicts.

Uses a cached index (.vault_index.json) for fast lookups.
Index is rebuilt automatically when stale (based on git status or age).

Usage:
    python scripts/check_before_create.py "Hospitality"
    python scripts/check_before_create.py "Short selling" "Commercial real estate"
    python scripts/check_before_create.py --rebuild   # force rebuild index
"""

import sys
import re
import json
import time
import subprocess
from pathlib import Path

# Windows consoles default to cp1252; conflict lists contain non-ASCII aliases
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

VAULT_ROOT = Path(__file__).parent.parent / "investing"
INDEX_PATH = Path(__file__).parent.parent / ".vault_index.json"
INDEX_MAX_AGE = 300  # seconds before auto-rebuild (5 min)


def extract_aliases(filepath: Path) -> list[str]:
    """Extract aliases from frontmatter."""
    try:
        # Only read first 2KB — frontmatter is always at the top
        with open(filepath, "r", encoding="utf-8") as f:
            header = f.read(2048)
    except Exception:
        return []

    if not header.startswith("---"):
        return []

    end = header.find("---", 3)
    if end == -1:
        return []

    frontmatter = header[3:end]
    aliases = []

    # Format: aliases: [a, b, c]
    bracket_match = re.search(r'aliases:\s*\[([^\]]+)\]', frontmatter)
    if bracket_match:
        raw = bracket_match.group(1)
        aliases = [a.strip().strip('"\'') for a in raw.split(",")]
    else:
        # Format: aliases:\n  - a\n  - b
        in_aliases = False
        for line in frontmatter.split("\n"):
            if line.startswith("aliases:"):
                in_aliases = True
                continue
            if in_aliases:
                if line.strip().startswith("-"):
                    alias = line.strip()[1:].strip().strip('"\'')
                    aliases.append(alias)
                elif line.strip() and not line.startswith(" "):
                    break

    return [a for a in aliases if a]


def build_index() -> dict:
    """Scan all vault .md files and build {path: {stem, aliases}} index."""
    entries = {}
    for md_file in VAULT_ROOT.rglob("*.md"):
        rel = str(md_file.relative_to(VAULT_ROOT))
        # Skip Reports — disposable cross-vault syntheses, not entity notes.
        if rel.startswith("Reports/") or rel.startswith("Reports\\"):
            continue
        entries[rel] = {
            "stem": md_file.stem,
            "aliases": extract_aliases(md_file),
        }
    return entries


def save_index(entries: dict):
    """Write index to disk."""
    data = {"built": time.time(), "entries": entries}
    INDEX_PATH.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")


def load_index() -> dict | None:
    """Load index if fresh enough, else return None."""
    if not INDEX_PATH.exists():
        return None
    try:
        data = json.loads(INDEX_PATH.read_text(encoding="utf-8"))
    except Exception:
        return None

    age = time.time() - data.get("built", 0)
    if age > INDEX_MAX_AGE:
        return None

    return data.get("entries")


def get_or_build_index(force: bool = False) -> dict:
    """Return cached index or rebuild."""
    if not force:
        cached = load_index()
        if cached is not None:
            return cached
    entries = build_index()
    save_index(entries)
    return entries


def normalize(s: str) -> str:
    """Normalize string for comparison."""
    return re.sub(r'[^a-z0-9]', '', s.lower())


def find_conflicts(proposed: str, index: dict) -> list[dict]:
    """Find notes that might conflict with proposed name."""
    conflicts = []
    proposed_norm = normalize(proposed)
    proposed_words = set(proposed.lower().split())

    for rel_path, info in index.items():
        stem = info["stem"]
        stem_norm = normalize(stem)
        aliases = info["aliases"]
        aliases_norm = [normalize(a) for a in aliases]

        match_reasons = []

        # Exact match on filename
        if proposed_norm == stem_norm:
            match_reasons.append("exact filename match")

        # Exact match on alias
        for i, alias_norm in enumerate(aliases_norm):
            if proposed_norm == alias_norm:
                match_reasons.append(f"exact alias match: '{aliases[i]}'")

        # Substring match (proposed in filename or vice versa)
        if len(proposed_norm) >= 4:
            if proposed_norm in stem_norm:
                match_reasons.append(f"filename contains '{proposed}'")
            elif stem_norm in proposed_norm:
                match_reasons.append(f"'{stem}' is substring of proposed")

        # Substring match on aliases
        for i, alias_norm in enumerate(aliases_norm):
            if len(proposed_norm) >= 4 and len(alias_norm) >= 4:
                if proposed_norm in alias_norm:
                    match_reasons.append(f"alias '{aliases[i]}' contains '{proposed}'")
                elif alias_norm in proposed_norm:
                    match_reasons.append(f"proposed contains alias '{aliases[i]}'")

        # Word overlap (for multi-word names)
        if len(proposed_words) > 1:
            stem_words = set(stem.lower().split())
            overlap = proposed_words & stem_words
            if len(overlap) >= 1 and len(overlap) / len(proposed_words) >= 0.5:
                match_reasons.append(f"word overlap: {overlap}")

        if match_reasons:
            conflicts.append({
                "path": rel_path,
                "name": stem,
                "aliases": aliases,
                "reasons": match_reasons,
            })

    return conflicts


def main():
    if len(sys.argv) >= 2 and sys.argv[1] == "--rebuild":
        print("Rebuilding index...")
        entries = get_or_build_index(force=True)
        print(f"Indexed {len(entries)} notes → {INDEX_PATH}")
        sys.exit(0)

    if len(sys.argv) < 2:
        print("Usage: python check_before_create.py <proposed_name> [<proposed_name2> ...]")
        print("       python check_before_create.py --rebuild")
        sys.exit(1)

    proposed_names = sys.argv[1:]
    index = get_or_build_index()
    any_conflicts = False

    for proposed in proposed_names:
        print(f"\n{'='*60}")
        print(f"Checking: {proposed}")
        print("=" * 60)

        conflicts = find_conflicts(proposed, index)

        if conflicts:
            any_conflicts = True
            print(f"\nCONFLICTS FOUND ({len(conflicts)}):\n")
            for c in conflicts:
                print(f"  {c['path']}")
                if c["aliases"]:
                    print(f"     aliases: {', '.join(c['aliases'])}")
                for reason in c["reasons"]:
                    print(f"     - {reason}")
                print()
            print("  Consider linking to existing note instead of creating new one.")
        else:
            print("\n[OK] No conflicts found. Safe to create.\n")

    sys.exit(1 if any_conflicts else 0)


if __name__ == "__main__":
    main()
