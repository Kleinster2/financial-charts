#!/usr/bin/env python3
"""Global skill parity checker/promoter for repo-scoped agent skills."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve().parent
DEFAULT_REGISTRY = HERE / "registry.json"
DEFAULT_OPENCLAW_SKILLS_DIR = Path(
    os.environ.get("OPENCLAW_SKILLS_DIR", r"C:\Users\klein\clawd\skills")
)
RUNTIME_ORDER = ["codex", "claude", "openclaw"]
PROMOTE_RUNTIME_ORDER = ["claude", "codex", "openclaw"]


@dataclass(frozen=True)
class SkillFile:
    path: Path
    digest: str
    lines: int


@dataclass(frozen=True)
class Scope:
    name: str
    description: str
    root: Path
    skills: list[str]
    runtimes: dict[str, Path]
    manifest: Path
    optional: bool = False


@dataclass(frozen=True)
class SkillCopy:
    runtime: str
    root: Path
    skill_dir: Path
    skill_file: Path
    modified_ns: int


def read_json(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, dict):
        raise ValueError(f"{path} must contain a JSON object")
    return data


def dedupe_strings(values: Any, source: str) -> list[str]:
    if not isinstance(values, list) or not all(isinstance(item, str) for item in values):
        raise ValueError(f"{source} must be a string list")

    seen: set[str] = set()
    duplicates: list[str] = []
    result: list[str] = []
    for item in values:
        if item in seen:
            duplicates.append(item)
            continue
        seen.add(item)
        result.append(item)

    if duplicates:
        names = ", ".join(sorted(set(duplicates)))
        raise ValueError(f"{source} has duplicate entries: {names}")

    return result


def resolve_path(value: str, base: Path) -> Path:
    if value == "$OPENCLAW_SKILLS_DIR":
        return DEFAULT_OPENCLAW_SKILLS_DIR

    expanded = os.path.expandvars(value)
    path = Path(expanded)
    if not path.is_absolute():
        path = base / path
    return path


def registry_manifests(path: Path) -> list[Path]:
    data = read_json(path)
    manifests = dedupe_strings(data.get("manifests"), f"{path}.manifests")
    return [resolve_path(item, path.parent) for item in manifests]


def read_scope_skills(scope_data: dict[str, Any], manifest: Path, source: str) -> list[str]:
    if "skills" in scope_data:
        return dedupe_strings(scope_data["skills"], f"{source}.skills")

    skills_from = scope_data.get("skillsFrom")
    if not isinstance(skills_from, dict):
        raise ValueError(f"{source} must contain either skills or skillsFrom")

    manifest_value = skills_from.get("path")
    key = skills_from.get("key")
    if not isinstance(manifest_value, str) or not isinstance(key, str):
        raise ValueError(f"{source}.skillsFrom must contain string path and key")

    skill_manifest = resolve_path(manifest_value, manifest.parent.parent)
    data = read_json(skill_manifest)
    return dedupe_strings(data.get(key), f"{skill_manifest}.{key}")


def read_scopes_from_manifest(manifest: Path) -> list[Scope]:
    data = read_json(manifest)
    scopes_data = data.get("scopes")
    if not isinstance(scopes_data, list):
        raise ValueError(f"{manifest} must contain a scopes list")

    scopes: list[Scope] = []
    seen: set[str] = set()
    for index, scope_data in enumerate(scopes_data):
        source = f"{manifest}.scopes[{index}]"
        if not isinstance(scope_data, dict):
            raise ValueError(f"{source} must be a JSON object")

        name = scope_data.get("name")
        description = scope_data.get("description", "")
        root_value = scope_data.get("root")
        runtimes_data = scope_data.get("runtimes")
        optional = scope_data.get("optional", False)

        if not isinstance(name, str) or not name:
            raise ValueError(f"{source}.name must be a non-empty string")
        if name in seen:
            raise ValueError(f"{manifest} has duplicate scope: {name}")
        seen.add(name)
        if not isinstance(description, str):
            raise ValueError(f"{source}.description must be a string")
        if not isinstance(root_value, str):
            raise ValueError(f"{source}.root must be a string")
        if not isinstance(runtimes_data, dict):
            raise ValueError(f"{source}.runtimes must be an object")
        if not isinstance(optional, bool):
            raise ValueError(f"{source}.optional must be a boolean when present")

        root = resolve_path(root_value, manifest.parent.parent)
        runtimes: dict[str, Path] = {}
        for runtime, path_value in runtimes_data.items():
            if not isinstance(runtime, str) or not isinstance(path_value, str):
                raise ValueError(f"{source}.runtimes keys and values must be strings")
            runtimes[runtime] = resolve_path(path_value, root)

        scopes.append(
            Scope(
                name=name,
                description=description,
                root=root,
                skills=read_scope_skills(scope_data, manifest, source),
                runtimes=runtimes,
                manifest=manifest,
                optional=optional,
            )
        )

    return scopes


def load_scopes(args: argparse.Namespace) -> list[Scope]:
    manifests: list[Path] = []
    if args.manifest:
        manifests.extend(resolve_path(item, Path.cwd()) for item in args.manifest)
    else:
        manifests.extend(registry_manifests(args.registry))

    scopes: list[Scope] = []
    seen: set[str] = set()
    for manifest in manifests:
        for scope in read_scopes_from_manifest(manifest):
            if scope.name in seen:
                raise ValueError(f"Duplicate scope registered globally: {scope.name}")
            seen.add(scope.name)
            scopes.append(scope)
    return scopes


def select_scopes(args: argparse.Namespace) -> list[Scope]:
    scopes = load_scopes(args)
    if args.all_scopes:
        return scopes

    selected = set(args.scope or [])
    if not selected:
        selected.add(scopes[0].name)

    by_name = {scope.name: scope for scope in scopes}
    missing = sorted(selected - set(by_name))
    if missing:
        names = ", ".join(sorted(by_name))
        raise ValueError(f"Unknown scope(s): {', '.join(missing)}. Registered scopes: {names}")
    return [by_name[name] for name in scopes_name_order(scopes, selected)]


def scopes_name_order(scopes: list[Scope], selected: set[str]) -> list[str]:
    return [scope.name for scope in scopes if scope.name in selected]


def normalized_text(path: Path) -> str:
    raw = path.read_bytes()
    return raw.decode("utf-8-sig").replace("\r\n", "\n").replace("\r", "\n")


def normalized_digest(path: Path) -> tuple[str, int]:
    text = normalized_text(path)
    return hashlib.sha256(text.encode("utf-8")).hexdigest(), len(text.splitlines())


def discover(root: Path) -> dict[str, SkillFile]:
    skills: dict[str, SkillFile] = {}
    if not root.exists():
        return skills
    for child in sorted(root.iterdir(), key=lambda p: p.name.lower()):
        skill_file = child / "SKILL.md"
        if not child.is_dir() or not skill_file.exists():
            continue
        digest, lines = normalized_digest(skill_file)
        skills[child.name] = SkillFile(skill_file, digest, lines)
    return skills


def runtime_roots_for_scope(args: argparse.Namespace, scope: Scope) -> tuple[dict[str, Path], list[str]]:
    roots = {
        runtime: scope.runtimes[runtime]
        for runtime in RUNTIME_ORDER
        if runtime in scope.runtimes
    }
    if args.openclaw_skills is not None and "openclaw" in roots:
        roots["openclaw"] = args.openclaw_skills

    skipped: list[str] = []
    if args.optional_openclaw and "openclaw" in roots and not roots["openclaw"].exists():
        skipped.append("openclaw")
        roots.pop("openclaw")
    return roots, skipped


def resolve_skill_names(
    args: argparse.Namespace, scope: Scope, inventory: dict[str, dict[str, SkillFile]]
) -> list[str]:
    if args.all:
        names = set()
        for skills in inventory.values():
            names.update(skills)
        return sorted(names)
    if args.skills:
        return list(dict.fromkeys(args.skills))
    return scope.skills


def skill_status(name: str, inventory: dict[str, dict[str, SkillFile]]) -> dict[str, Any]:
    entries = {runtime: skills.get(name) for runtime, skills in inventory.items()}
    present = sorted(runtime for runtime, item in entries.items() if item is not None)
    missing = sorted(runtime for runtime, item in entries.items() if item is None)

    codex = entries.get("codex")
    claude = entries.get("claude")
    openclaw = entries.get("openclaw")

    codex_claude = "n/a"
    if codex and claude:
        codex_claude = "same" if codex.digest == claude.digest else "different"

    openclaw_status = "skipped"
    if "openclaw" in inventory and not openclaw:
        openclaw_status = "missing"
    elif openclaw:
        if codex and openclaw.digest == codex.digest:
            openclaw_status = "same-as-codex"
        elif claude and openclaw.digest == claude.digest:
            openclaw_status = "same-as-claude"
        else:
            openclaw_status = "different"

    return {
        "name": name,
        "present": present,
        "missing": missing,
        "codex_claude": codex_claude,
        "openclaw_status": openclaw_status,
        "hashes": {runtime: item.digest[:12] if item else None for runtime, item in entries.items()},
        "lines": {runtime: item.lines if item else None for runtime, item in entries.items()},
        "paths": {runtime: str(item.path) if item else None for runtime, item in entries.items()},
    }


def build_scope_report(args: argparse.Namespace, scope: Scope) -> dict[str, Any]:
    if scope.optional and not scope.root.exists():
        return {
            "scope": scope.name,
            "description": scope.description,
            "manifest": str(scope.manifest),
            "scope_root": str(scope.root),
            "optional": scope.optional,
            "skipped": True,
            "skip_reason": "scope root not found",
            "runtime_roots": {},
            "inventory_counts": {},
            "selected_skills": scope.skills,
            "skipped_runtimes": [],
            "skills": [],
            "summary": {
                "shared_all": [],
                "missing_by_runtime": {},
                "codex_claude_drift": [],
                "openclaw_unexpected_drift": [],
            },
        }

    roots, skipped = runtime_roots_for_scope(args, scope)
    inventory = {runtime: discover(root) for runtime, root in roots.items()}
    skill_names = resolve_skill_names(args, scope, inventory)
    skills = [skill_status(name, inventory) for name in skill_names]

    summary = {
        "shared_all": [item["name"] for item in skills if len(item["present"]) == len(roots)],
        "missing_by_runtime": {
            runtime: [item["name"] for item in skills if runtime in item["missing"]]
            for runtime in roots
        },
        "codex_claude_drift": [
            item["name"] for item in skills if item["codex_claude"] == "different"
        ],
        "openclaw_unexpected_drift": [
            item["name"] for item in skills if item["openclaw_status"] == "different"
        ],
    }

    return {
        "scope": scope.name,
        "description": scope.description,
        "manifest": str(scope.manifest),
        "scope_root": str(scope.root),
        "optional": scope.optional,
        "skipped": False,
        "skip_reason": None,
        "runtime_roots": {runtime: str(root) for runtime, root in roots.items()},
        "inventory_counts": {runtime: len(items) for runtime, items in inventory.items()},
        "selected_skills": skill_names,
        "skipped_runtimes": skipped,
        "skills": skills,
        "summary": summary,
    }


def build_report(args: argparse.Namespace) -> dict[str, Any]:
    scopes = select_scopes(args)
    return {
        "registry": str(args.registry),
        "selected_scope_names": [scope.name for scope in scopes],
        "scopes": [build_scope_report(args, scope) for scope in scopes],
    }


def print_list(title: str, values: list[str]) -> None:
    print(f"{title}: {', '.join(values) if values else 'none'}")


def print_scope_report(scope_report: dict[str, Any]) -> None:
    print(f"Scope: {scope_report['scope']}")
    print(f"Root:  {scope_report['scope_root']}")
    print(f"Manifest: {scope_report['manifest']}")
    if scope_report["description"]:
        print(f"About: {scope_report['description']}")
    print()

    if scope_report["skipped"]:
        print(f"Skipped: {scope_report['skip_reason']}")
        print()
        return

    for runtime, root in scope_report["runtime_roots"].items():
        print(f"{runtime:8} {scope_report['inventory_counts'][runtime]:3} skills  {root}")
    for runtime in scope_report["skipped_runtimes"]:
        print(f"{runtime:8} skipped   directory not found")
    print()

    header = (
        f"{'Skill':24} {'Codex':7} {'Claude':7} {'OpenClaw':9} "
        f"{'Codex/Claude':13} {'OpenClaw compare'}"
    )
    print(header)
    print("-" * len(header))
    for item in scope_report["skills"]:
        present = set(item["present"])
        codex = "yes" if "codex" in present else "missing"
        claude = "yes" if "claude" in present else "missing"
        if "openclaw" in scope_report["skipped_runtimes"]:
            openclaw = "skipped"
        else:
            openclaw = "yes" if "openclaw" in present else "missing"
        print(
            f"{item['name']:24} {codex:7} {claude:7} {openclaw:9} "
            f"{item['codex_claude']:13} {item['openclaw_status']}"
        )
    print()

    summary = scope_report["summary"]
    shared_label = "Shared across selected runtimes"
    if not scope_report["skipped_runtimes"]:
        shared_label = "Shared across all three"
    print_list(shared_label, summary["shared_all"])
    for runtime, values in summary["missing_by_runtime"].items():
        print_list(f"Missing in {runtime}", values)
    print_list("Codex/Claude drift", summary["codex_claude_drift"])
    print_list("OpenClaw unexpected drift", summary["openclaw_unexpected_drift"])
    print()


def print_report(report: dict[str, Any]) -> None:
    print("Global Skill Parity Report")
    print("==========================")
    print(f"Registry: {report['registry']}")
    print()
    for scope_report in report["scopes"]:
        print_scope_report(scope_report)


def has_failures(report: dict[str, Any]) -> bool:
    for scope_report in report["scopes"]:
        if scope_report["skipped"]:
            continue
        summary = scope_report["summary"]
        if (
            any(summary["missing_by_runtime"].values())
            or summary["codex_claude_drift"]
            or summary["openclaw_unexpected_drift"]
        ):
            return True
    return False


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
    for runtime in PROMOTE_RUNTIME_ORDER:
        root = roots.get(runtime)
        if root is None:
            continue
        copy = skill_copy(runtime, root, name)
        if copy is not None:
            copies[runtime] = copy
    return copies


def choose_source(name: str, copies: dict[str, SkillCopy], source_runtime: str) -> SkillCopy:
    if source_runtime != "newest":
        copy = copies.get(source_runtime)
        if copy is None:
            raise ValueError(f"{name}: missing source copy in {source_runtime}")
        return copy
    if not copies:
        raise ValueError(f"{name}: no SKILL.md found in any selected runtime")
    return max(
        copies.values(),
        key=lambda copy: (copy.modified_ns, PROMOTE_RUNTIME_ORDER.index(copy.runtime)),
    )


def display_path(path: Path, scope: Scope) -> str:
    try:
        return str(path.relative_to(scope.root))
    except ValueError:
        return str(path)


def copy_skill_tree(source: SkillCopy, dest_root: Path, name: str, dry_run: bool, scope: Scope) -> str:
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
    return f"SYNCED {name}: {source.runtime} -> {display_path(dest_dir, scope)}"


def promote_scope(args: argparse.Namespace, scope: Scope) -> bool:
    if scope.optional and not scope.root.exists():
        print(f"SKIPPED SCOPE {scope.name}: root not found ({scope.root})")
        print()
        return False

    roots, _ = runtime_roots_for_scope(args, scope)
    inventory = {runtime: discover(root) for runtime, root in roots.items()}
    names = resolve_skill_names(args, scope, inventory)
    if not names:
        print(f"No skills selected for scope {scope.name}.")
        print()
        return False

    print(f"Scope {scope.name}: {scope.root}")
    changed = False
    for name in names:
        copies = discover_copies(roots, name)
        source = choose_source(name, copies, args.source_runtime)
        print(f"{name}: promoting {source.runtime} ({display_path(source.skill_file, scope)})")
        for runtime in PROMOTE_RUNTIME_ORDER:
            root = roots.get(runtime)
            if root is None:
                print(f"SKIPPED {name}: {runtime} runtime not selected")
                continue
            line = copy_skill_tree(source, root, name, args.dry_run, scope)
            print(line)
            changed = changed or line.startswith(("SYNCED", "WOULD"))
        print()
    print()
    return changed


def add_common_args(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("skills", nargs="*", help="Specific skills. Defaults to the scope set.")
    parser.add_argument("--registry", type=Path, default=DEFAULT_REGISTRY)
    parser.add_argument(
        "--manifest",
        action="append",
        help="Extra or replacement scope manifest. May be passed multiple times.",
    )
    parser.add_argument("--scope", action="append", help="Scope name. May be passed multiple times.")
    parser.add_argument("--all-scopes", action="store_true", help="Use every registered scope.")
    parser.add_argument("--all", action="store_true", help="Use every discovered skill in each scope.")
    parser.add_argument("--openclaw-skills", type=Path, default=None)
    parser.add_argument("--optional-openclaw", action="store_true")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    check = subparsers.add_parser("check", help="Compare registered scope parity.")
    add_common_args(check)
    check.add_argument("--json", action="store_true")
    check.add_argument("--strict", action="store_true")

    promote = subparsers.add_parser("promote", help="Promote one runtime's skill copies.")
    add_common_args(promote)
    promote.add_argument(
        "--from",
        dest="source_runtime",
        choices=["newest", *PROMOTE_RUNTIME_ORDER],
        default="newest",
    )
    promote.add_argument("--dry-run", action="store_true")

    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        if args.command == "check":
            report = build_report(args)
            if args.json:
                print(json.dumps(report, indent=2, sort_keys=True))
            else:
                print_report(report)
            return 1 if args.strict and has_failures(report) else 0

        scopes = select_scopes(args)
        changed = False
        for scope in scopes:
            changed = promote_scope(args, scope) or changed
        if args.dry_run:
            print("Dry run only. No files were changed.")
        elif changed:
            print("Run agent_skill_parity.py check --all-scopes --strict to verify parity.")
        else:
            print("No files were changed.")
        return 0
    except ValueError as exc:
        print(exc, file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
