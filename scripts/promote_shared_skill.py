#!/usr/bin/env python3
"""
Promote the intended shared workflow skill copy across all runtimes.

Usage:
    python scripts/promote_shared_skill.py story --from newest --dry-run
    python scripts/promote_shared_skill.py story --from openclaw
    python scripts/promote_shared_skill.py --all --from claude
"""

from __future__ import annotations

import argparse
import os
import shutil
import sys
from dataclasses import dataclass
from pathlib import Path

from skill_manifest import read_manifest_list


REPO_ROOT = Path(__file__).resolve().parent.parent
RUNTIME_ROOTS = {
    "claude": REPO_ROOT / ".claude" / "skills",
    "codex": REPO_ROOT / ".agents" / "skills",
    "openclaw": Path(
        os.environ.get("OPENCLAW_SKILLS_DIR", r"C:\Users\klein\clawd\skills")
    ),
}
RUNTIME_ORDER = ["claude", "codex", "openclaw"]


@dataclass(frozen=True)
class SkillCopy:
    runtime: str
    root: Path
    skill_dir: Path
    skill_file: Path
    modified_ns: int


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Promote one shared workflow skill copy into the other runtimes. "
            "Use this when the newest intended edit was made in OpenClaw, "
            "Codex, or Claude and should become canonical everywhere."
        )
    )
    parser.add_argument(
        "skills",
        nargs="*",
        help="Specific shared skill names to promote. Defaults to the manifest set.",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Promote every skill listed in skills/shared-workflows.json.",
    )
    parser.add_argument(
        "--from",
        dest="source_runtime",
        choices=["newest", *RUNTIME_ORDER],
        default="newest",
        help="Source runtime to promote. Defaults to newest SKILL.md mtime.",
    )
    parser.add_argument(
        "--openclaw-skills",
        type=Path,
        default=RUNTIME_ROOTS["openclaw"],
        help="Path to the OpenClaw skills directory.",
    )
    parser.add_argument(
        "--optional-openclaw",
        action="store_true",
        help="Skip OpenClaw writes when its skills directory is absent.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show planned promotions without copying files.",
    )
    return parser.parse_args()


def runtime_roots(args: argparse.Namespace) -> dict[str, Path]:
    roots = dict(RUNTIME_ROOTS)
    roots["openclaw"] = args.openclaw_skills
    if args.optional_openclaw and not roots["openclaw"].exists():
        roots.pop("openclaw")
    return roots


def resolve_skill_names(args: argparse.Namespace) -> list[str]:
    if args.all or not args.skills:
        names = read_manifest_list("workflowSkills")
    else:
        names = args.skills

    seen: set[str] = set()
    deduped: list[str] = []
    for name in names:
        if name in seen:
            continue
        seen.add(name)
        deduped.append(name)
    return deduped


def skill_copy(runtime: str, root: Path, name: str) -> SkillCopy | None:
    skill_dir = root / name
    skill_file = skill_dir / "SKILL.md"
    if not skill_file.exists():
        return None
    return SkillCopy(
        runtime=runtime,
        root=root,
        skill_dir=skill_dir,
        skill_file=skill_file,
        modified_ns=skill_file.stat().st_mtime_ns,
    )


def discover_copies(roots: dict[str, Path], name: str) -> dict[str, SkillCopy]:
    copies: dict[str, SkillCopy] = {}
    for runtime in RUNTIME_ORDER:
        root = roots.get(runtime)
        if root is None:
            continue
        copy = skill_copy(runtime, root, name)
        if copy is not None:
            copies[runtime] = copy
    return copies


def choose_source(
    name: str, copies: dict[str, SkillCopy], source_runtime: str
) -> SkillCopy:
    if source_runtime != "newest":
        copy = copies.get(source_runtime)
        if copy is None:
            raise ValueError(f"{name}: missing source copy in {source_runtime}")
        return copy

    if not copies:
        raise ValueError(f"{name}: no SKILL.md found in any selected runtime")

    return max(
        copies.values(),
        key=lambda copy: (copy.modified_ns, RUNTIME_ORDER.index(copy.runtime)),
    )


def display_path(path: Path) -> str:
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def copy_skill_tree(source: SkillCopy, dest_root: Path, name: str, dry_run: bool) -> str:
    dest_dir = dest_root / name
    if dest_dir.resolve() == source.skill_dir.resolve():
        return f"UNCHANGED {name}: {source.runtime} is source"

    if dry_run:
        action = "WOULD UPDATE" if dest_dir.exists() else "WOULD CREATE"
        return (
            f"{action} {name}: {display_path(source.skill_dir)} -> "
            f"{display_path(dest_dir)}"
        )

    dest_root.mkdir(parents=True, exist_ok=True)
    if dest_dir.exists():
        shutil.rmtree(dest_dir)
    shutil.copytree(source.skill_dir, dest_dir)
    return (
        f"SYNCED {name}: {source.runtime} -> "
        f"{display_path(dest_dir)}"
    )


def promote_skill(
    name: str, roots: dict[str, Path], source_runtime: str, dry_run: bool
) -> list[str]:
    copies = discover_copies(roots, name)
    source = choose_source(name, copies, source_runtime)
    lines = [
        (
            f"{name}: promoting {source.runtime} "
            f"({display_path(source.skill_file)})"
        )
    ]

    for runtime in RUNTIME_ORDER:
        root = roots.get(runtime)
        if root is None:
            lines.append(f"SKIPPED {name}: {runtime} runtime not selected")
            continue
        lines.append(copy_skill_tree(source, root, name, dry_run))

    return lines


def main() -> int:
    args = parse_args()
    roots = runtime_roots(args)
    names = resolve_skill_names(args)

    if not names:
        print("No skills selected.")
        return 0

    had_error = False
    for name in names:
        try:
            for line in promote_skill(name, roots, args.source_runtime, args.dry_run):
                print(line)
        except ValueError as exc:
            had_error = True
            print(exc, file=sys.stderr)
        print()

    if args.dry_run:
        print("Dry run only. No files were changed.")
    else:
        print("Run python scripts/check_skill_parity.py --strict to verify parity.")

    return 1 if had_error else 0


if __name__ == "__main__":
    sys.exit(main())
