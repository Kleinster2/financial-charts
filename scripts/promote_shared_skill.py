#!/usr/bin/env python3
"""
Promote the intended shared workflow skill copy across all runtimes.

Usage:
    python scripts/promote_shared_skill.py story --from newest --dry-run
    python scripts/promote_shared_skill.py story --from openclaw
    python scripts/promote_shared_skill.py --all --from claude
    python scripts/promote_shared_skill.py --scope personal-vault --all --from claude
"""

from __future__ import annotations

import argparse
import shutil
import sys
from dataclasses import dataclass
from pathlib import Path

from skill_manifest import SkillParityScope, read_skill_parity_scopes


REPO_ROOT = Path(__file__).resolve().parent.parent
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
        help="Specific shared skill names to promote. Defaults to the selected scope set.",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Promote every skill listed in the selected scope.",
    )
    parser.add_argument(
        "--scope",
        help=(
            "Skill parity scope from skills/skill-parity-scopes.json. "
            "Defaults to that manifest's defaultScope."
        ),
    )
    parser.add_argument(
        "--all-scopes",
        action="store_true",
        help="Promote every selected skill across every registered scope whose root is available.",
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
        default=None,
        help="Override the OpenClaw skills directory for every selected scope.",
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


def selected_scopes(args: argparse.Namespace) -> list[SkillParityScope]:
    default_scope, scopes = read_skill_parity_scopes()
    by_name = {scope.name: scope for scope in scopes}

    if args.all_scopes:
        return scopes

    scope_name = args.scope or default_scope
    scope = by_name.get(scope_name)
    if scope is None:
        names = ", ".join(sorted(by_name))
        raise ValueError(f"Unknown skill parity scope {scope_name!r}. Registered scopes: {names}")
    return [scope]


def runtime_roots(args: argparse.Namespace, scope: SkillParityScope) -> dict[str, Path]:
    roots = {
        runtime: scope.runtimes[runtime]
        for runtime in RUNTIME_ORDER
        if runtime in scope.runtimes
    }
    if args.openclaw_skills is not None and "openclaw" in roots:
        roots["openclaw"] = args.openclaw_skills
    if args.optional_openclaw and "openclaw" in roots and not roots["openclaw"].exists():
        roots.pop("openclaw")
    return roots


def resolve_skill_names(args: argparse.Namespace, scope: SkillParityScope) -> list[str]:
    if args.all or not args.skills:
        names = scope.skills
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


def display_path(path: Path, scope: SkillParityScope | None = None) -> str:
    if scope is not None:
        try:
            return str(path.relative_to(scope.root))
        except ValueError:
            pass
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def copy_skill_tree(
    source: SkillCopy,
    dest_root: Path,
    name: str,
    dry_run: bool,
    scope: SkillParityScope,
) -> str:
    dest_dir = dest_root / name
    if dest_dir.resolve() == source.skill_dir.resolve():
        return f"UNCHANGED {name}: {source.runtime} is source"

    if dry_run:
        action = "WOULD UPDATE" if dest_dir.exists() else "WOULD CREATE"
        return (
            f"{action} {name}: {display_path(source.skill_dir, scope)} -> "
            f"{display_path(dest_dir, scope)}"
        )

    dest_root.mkdir(parents=True, exist_ok=True)
    if dest_dir.exists():
        shutil.rmtree(dest_dir)
    shutil.copytree(source.skill_dir, dest_dir)
    return (
        f"SYNCED {name}: {source.runtime} -> "
        f"{display_path(dest_dir, scope)}"
    )


def promote_skill(
    name: str,
    roots: dict[str, Path],
    source_runtime: str,
    dry_run: bool,
    scope: SkillParityScope,
) -> list[str]:
    copies = discover_copies(roots, name)
    source = choose_source(name, copies, source_runtime)
    lines = [
        (
            f"{name}: promoting {source.runtime} "
            f"({display_path(source.skill_file, scope)})"
        )
    ]

    for runtime in RUNTIME_ORDER:
        root = roots.get(runtime)
        if root is None:
            lines.append(f"SKIPPED {name}: {runtime} runtime not selected")
            continue
        lines.append(copy_skill_tree(source, root, name, dry_run, scope))

    return lines


def main() -> int:
    args = parse_args()
    try:
        scopes = selected_scopes(args)
    except ValueError as exc:
        print(exc, file=sys.stderr)
        return 2

    had_error = False
    promoted_any = False
    for scope in scopes:
        if scope.optional and not scope.root.exists():
            print(f"SKIPPED SCOPE {scope.name}: root not found ({scope.root})")
            print()
            continue

        roots = runtime_roots(args, scope)
        names = resolve_skill_names(args, scope)
        if not names:
            print(f"No skills selected for scope {scope.name}.")
            print()
            continue

        print(f"Scope {scope.name}: {scope.root}")
        for name in names:
            try:
                for line in promote_skill(
                    name, roots, args.source_runtime, args.dry_run, scope
                ):
                    print(line)
                    promoted_any = True
            except ValueError as exc:
                had_error = True
                print(exc, file=sys.stderr)
            print()
        print()

    if args.dry_run:
        print("Dry run only. No files were changed.")
    elif promoted_any:
        scope_flag = "--all-scopes" if args.all_scopes else f"--scope {scopes[0].name}"
        print(f"Run python scripts/check_skill_parity.py {scope_flag} --strict to verify parity.")
    else:
        print("No files were changed.")

    return 1 if had_error else 0


if __name__ == "__main__":
    sys.exit(main())
