#!/usr/bin/env python3
"""
Compare shared skills across Codex, Claude Code, and OpenClaw.

Usage:
    python scripts/check_skill_parity.py
    python scripts/check_skill_parity.py news ingest earnings
    python scripts/check_skill_parity.py --all
    python scripts/check_skill_parity.py --scope personal-vault --strict
    python scripts/check_skill_parity.py --all-scopes --strict
    python scripts/check_skill_parity.py --json
    python scripts/check_skill_parity.py --strict
    python scripts/check_skill_parity.py --strict --optional-openclaw
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from skill_manifest import SkillParityScope, read_skill_parity_scopes


REPO_ROOT = Path(__file__).resolve().parent.parent
RUNTIME_ORDER = ["codex", "claude", "openclaw"]


@dataclass(frozen=True)
class SkillFile:
    path: Path
    digest: str
    lines: int


def read_normalized_text(path: Path) -> str:
    raw = path.read_bytes()
    text = raw.decode("utf-8-sig")
    return text.replace("\r\n", "\n").replace("\r", "\n")


def normalized_digest(path: Path) -> tuple[str, int]:
    """Hash text with normalized newlines so CRLF/LF churn is ignored."""
    normalized = read_normalized_text(path)
    digest = hashlib.sha256(normalized.encode("utf-8")).hexdigest()
    return digest, len(normalized.splitlines())


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


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Compare SKILL.md parity across .agents/skills, .claude/skills, "
            "and the OpenClaw workspace skills directory."
        )
    )
    parser.add_argument(
        "skills",
        nargs="*",
        help="Specific skill names to compare. Defaults to the shared workflow set.",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Compare the union of all discovered skill names in the selected scope.",
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
        help="Compare every registered scope whose root is available.",
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
        help=(
            "Skip OpenClaw comparison when its skills directory is absent. "
            "Useful in CI checkouts that only contain this repository."
        ),
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Emit machine-readable JSON instead of text.",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Exit nonzero if expected skills are missing or unexpected drift exists.",
    )
    return parser.parse_args()


def status_for(name: str, inventory: dict[str, dict[str, SkillFile]]) -> dict[str, Any]:
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

    hashes = {
        runtime: item.digest[:12] if item else None for runtime, item in entries.items()
    }
    lines = {runtime: item.lines if item else None for runtime, item in entries.items()}
    paths = {runtime: str(item.path) if item else None for runtime, item in entries.items()}

    return {
        "name": name,
        "present": present,
        "missing": missing,
        "codex_claude": codex_claude,
        "openclaw_status": openclaw_status,
        "hashes": hashes,
        "lines": lines,
        "paths": paths,
    }


def resolve_skill_names(
    args: argparse.Namespace,
    scope: SkillParityScope,
    inventory: dict[str, dict[str, SkillFile]],
) -> list[str]:
    if args.all:
        names = set()
        for skills in inventory.values():
            names.update(skills)
        return sorted(names)

    if args.skills:
        return list(dict.fromkeys(args.skills))

    return scope.skills


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


def runtime_roots_for_scope(
    args: argparse.Namespace, scope: SkillParityScope
) -> tuple[dict[str, Path], list[str]]:
    runtime_roots = {
        runtime: scope.runtimes[runtime]
        for runtime in RUNTIME_ORDER
        if runtime in scope.runtimes
    }
    if args.openclaw_skills is not None and "openclaw" in runtime_roots:
        runtime_roots["openclaw"] = args.openclaw_skills

    skipped_runtimes = []
    if (
        args.optional_openclaw
        and "openclaw" in runtime_roots
        and not runtime_roots["openclaw"].exists()
    ):
        skipped_runtimes.append("openclaw")
        runtime_roots.pop("openclaw")
    return runtime_roots, skipped_runtimes


def build_scope_report(args: argparse.Namespace, scope: SkillParityScope) -> dict[str, Any]:
    if scope.optional and not scope.root.exists():
        return {
            "scope": scope.name,
            "description": scope.description,
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
                "unregistered_codex_mirrors": [],
            },
        }

    runtime_roots, skipped_runtimes = runtime_roots_for_scope(args, scope)
    inventory = {runtime: discover(root) for runtime, root in runtime_roots.items()}
    skill_names = resolve_skill_names(args, scope, inventory)
    skills = [status_for(name, inventory) for name in skill_names]

    shared_all = [
        item["name"] for item in skills if len(item["present"]) == len(runtime_roots)
    ]
    missing_by_runtime = {
        runtime: [item["name"] for item in skills if runtime in item["missing"]]
        for runtime in runtime_roots
    }
    codex_claude_drift = [
        item["name"] for item in skills if item["codex_claude"] == "different"
    ]
    openclaw_unexpected_drift = [
        item["name"]
        for item in skills
        if item["openclaw_status"] == "different"
    ]
    # The Codex directory exists solely as a mirror of the registered set, so any
    # skill found there but absent from the scope manifest is drifting unchecked.
    # (Claude can hold runtime-local skills; OpenClaw's directory is shared across
    # scopes — neither supports this inference.)
    unregistered_codex_mirrors = sorted(
        set(inventory.get("codex", {})) - set(scope.skills)
    )

    return {
        "scope": scope.name,
        "description": scope.description,
        "scope_root": str(scope.root),
        "optional": scope.optional,
        "skipped": False,
        "skip_reason": None,
        "runtime_roots": {runtime: str(root) for runtime, root in runtime_roots.items()},
        "inventory_counts": {
            runtime: len(skills_for_runtime)
            for runtime, skills_for_runtime in inventory.items()
        },
        "selected_skills": skill_names,
        "skipped_runtimes": skipped_runtimes,
        "skills": skills,
        "summary": {
            "shared_all": shared_all,
            "missing_by_runtime": missing_by_runtime,
            "codex_claude_drift": codex_claude_drift,
            "openclaw_unexpected_drift": openclaw_unexpected_drift,
            "unregistered_codex_mirrors": unregistered_codex_mirrors,
        },
    }


def build_report(args: argparse.Namespace) -> dict[str, Any]:
    scopes = selected_scopes(args)
    return {
        "selected_scope_names": [scope.name for scope in scopes],
        "scopes": [build_scope_report(args, scope) for scope in scopes],
    }


def print_list(title: str, values: list[str]) -> None:
    if values:
        print(f"{title}: {', '.join(values)}")
    else:
        print(f"{title}: none")


def print_scope_report(scope_report: dict[str, Any]) -> None:
    print(f"Scope: {scope_report['scope']}")
    print(f"Root:  {scope_report['scope_root']}")
    if scope_report["description"]:
        print(f"About: {scope_report['description']}")
    print()

    if scope_report["skipped"]:
        print(f"Skipped: {scope_report['skip_reason']}")
        print()
        return

    for runtime, root in scope_report["runtime_roots"].items():
        count = scope_report["inventory_counts"][runtime]
        print(f"{runtime:8} {count:3} skills  {root}")
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
        openclaw_status = item["openclaw_status"]
        print(
            f"{item['name']:24} {codex:7} {claude:7} {openclaw:9} "
            f"{item['codex_claude']:13} {openclaw_status}"
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
    print_list(
        "Unregistered Codex mirrors (in mirror dir but not in scope manifest)",
        summary["unregistered_codex_mirrors"],
    )
    print()


def print_text_report(report: dict[str, Any]) -> None:
    print("Skill Parity Report")
    print("===================")
    print()
    for scope_report in report["scopes"]:
        print_scope_report(scope_report)


def has_scope_strict_failures(scope_report: dict[str, Any]) -> bool:
    if scope_report["skipped"]:
        return False

    summary = scope_report["summary"]
    has_missing = any(summary["missing_by_runtime"].values())
    return bool(
        has_missing
        or summary["codex_claude_drift"]
        or summary["openclaw_unexpected_drift"]
        or summary["unregistered_codex_mirrors"]
    )


def has_strict_failures(report: dict[str, Any]) -> bool:
    return any(has_scope_strict_failures(scope_report) for scope_report in report["scopes"])


def main() -> int:
    args = parse_args()
    try:
        report = build_report(args)
    except ValueError as exc:
        print(exc, file=sys.stderr)
        return 2

    if args.json:
        print(json.dumps(report, indent=2, sort_keys=True))
    else:
        print_text_report(report)

    if args.strict and has_strict_failures(report):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
