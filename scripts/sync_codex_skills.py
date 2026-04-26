#!/usr/bin/env python3
"""
Sync repo-local Claude workflow skills into Codex's repo skill path.

Usage:
    python scripts/sync_codex_skills.py
    python scripts/sync_codex_skills.py news ingest
    python scripts/sync_codex_skills.py --all
    python scripts/sync_codex_skills.py --dry-run
"""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
CLAUDE_SKILLS = REPO_ROOT / ".claude" / "skills"
CODEX_SKILLS = REPO_ROOT / ".agents" / "skills"
DEFAULT_WORKFLOW_SKILLS = [
    "news",
    "ingest",
    "earnings",
    "report",
    "deepdive",
    "newsletter",
    "story",
    "morning-scan",
    "replicate",
]


def discover_syncable_skills() -> list[str]:
    """Return Claude skills that look like user-facing workflows."""
    names: list[str] = []
    if not CLAUDE_SKILLS.exists():
        return names

    for child in sorted(CLAUDE_SKILLS.iterdir(), key=lambda p: p.name.lower()):
        if not child.is_dir():
            continue
        if child.name.endswith("-workspace"):
            continue
        if not (child / "SKILL.md").exists():
            continue
        names.append(child.name)
    return names


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Copy repo-local workflow skills from .claude/skills into "
            ".agents/skills so Codex can discover them."
        )
    )
    parser.add_argument(
        "skills",
        nargs="*",
        help="Specific skill names to sync. Defaults to the repo workflow set.",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Sync every non-workspace skill found under .claude/skills.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show planned actions without copying files.",
    )
    return parser.parse_args()


def resolve_skill_names(args: argparse.Namespace) -> list[str]:
    if args.all:
        names = discover_syncable_skills()
    elif args.skills:
        names = args.skills
    else:
        names = DEFAULT_WORKFLOW_SKILLS

    # Preserve order while removing duplicates.
    seen: set[str] = set()
    deduped: list[str] = []
    for name in names:
        if name in seen:
            continue
        seen.add(name)
        deduped.append(name)
    return deduped


def validate_sources(skill_names: list[str]) -> tuple[list[tuple[str, Path, Path]], list[str]]:
    planned: list[tuple[str, Path, Path]] = []
    missing: list[str] = []

    for name in skill_names:
        src = CLAUDE_SKILLS / name
        dest = CODEX_SKILLS / name
        if not (src / "SKILL.md").exists():
            missing.append(name)
            continue
        planned.append((name, src, dest))

    return planned, missing


def sync_skill(name: str, src: Path, dest: Path, dry_run: bool) -> str:
    if dry_run:
        if dest.exists():
            return f"WOULD UPDATE {name}: {dest.relative_to(REPO_ROOT)}"
        return f"WOULD CREATE {name}: {dest.relative_to(REPO_ROOT)}"

    CODEX_SKILLS.mkdir(parents=True, exist_ok=True)
    if dest.exists():
        shutil.rmtree(dest)
    shutil.copytree(src, dest)
    return f"SYNCED {name}: {dest.relative_to(REPO_ROOT)}"


def main() -> int:
    args = parse_args()
    skill_names = resolve_skill_names(args)

    if not skill_names:
        print("No skills selected.")
        return 0

    planned, missing = validate_sources(skill_names)

    if missing:
        print("Missing source skills:")
        for name in missing:
            print(f"  - {name}")
        if not planned:
            return 1
        print()

    for name, src, dest in planned:
        print(sync_skill(name, src, dest, args.dry_run))

    if args.dry_run:
        print("\nDry run only. No files were changed.")
    else:
        print("\nRestart Codex if the updated skills do not appear immediately.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
