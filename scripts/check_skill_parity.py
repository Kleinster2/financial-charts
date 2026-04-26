#!/usr/bin/env python3
"""
Compare shared skills across Codex, Claude Code, and OpenClaw.

Usage:
    python scripts/check_skill_parity.py
    python scripts/check_skill_parity.py news ingest earnings
    python scripts/check_skill_parity.py --all
    python scripts/check_skill_parity.py --json
    python scripts/check_skill_parity.py --strict
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parent.parent
RUNTIMES = {
    "codex": REPO_ROOT / ".agents" / "skills",
    "claude": REPO_ROOT / ".claude" / "skills",
    "openclaw": Path(r"C:\Users\klein\clawd\skills"),
}

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

# OpenClaw skills often need absolute paths and runtime-specific guardrails.
DEFAULT_OPENCLAW_ADAPTED = {
    "deepdive",
    "news",
    "ingest",
    "earnings",
    "report",
    "newsletter",
    "story",
    "morning-scan",
}


@dataclass(frozen=True)
class SkillFile:
    path: Path
    digest: str
    lines: int


def normalized_digest(path: Path) -> tuple[str, int]:
    """Hash text with normalized newlines so CRLF/LF churn is ignored."""
    raw = path.read_bytes()
    text = raw.decode("utf-8-sig")
    normalized = text.replace("\r\n", "\n").replace("\r", "\n")
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
        help="Compare the union of all discovered skill names.",
    )
    parser.add_argument(
        "--openclaw-skills",
        type=Path,
        default=RUNTIMES["openclaw"],
        help="Path to OpenClaw skills directory.",
    )
    parser.add_argument(
        "--adapted-openclaw",
        nargs="*",
        default=sorted(DEFAULT_OPENCLAW_ADAPTED),
        help=(
            "OpenClaw skills expected to differ from Codex/Claude because "
            "they are runtime-adapted ports."
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

    codex = entries["codex"]
    claude = entries["claude"]
    openclaw = entries["openclaw"]

    codex_claude = "n/a"
    if codex and claude:
        codex_claude = "same" if codex.digest == claude.digest else "different"

    openclaw_status = "missing"
    if openclaw:
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
    args: argparse.Namespace, inventory: dict[str, dict[str, SkillFile]]
) -> list[str]:
    if args.all:
        names = set()
        for skills in inventory.values():
            names.update(skills)
        return sorted(names)

    if args.skills:
        return list(dict.fromkeys(args.skills))

    return DEFAULT_WORKFLOW_SKILLS.copy()


def build_report(args: argparse.Namespace) -> dict[str, Any]:
    runtime_roots = dict(RUNTIMES)
    runtime_roots["openclaw"] = args.openclaw_skills
    inventory = {runtime: discover(root) for runtime, root in runtime_roots.items()}
    skill_names = resolve_skill_names(args, inventory)
    adapted_openclaw = set(args.adapted_openclaw)
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
        and item["name"] not in adapted_openclaw
    ]
    openclaw_adapted = [
        item["name"]
        for item in skills
        if item["openclaw_status"] == "different"
        and item["name"] in adapted_openclaw
    ]

    return {
        "runtime_roots": {runtime: str(root) for runtime, root in runtime_roots.items()},
        "inventory_counts": {
            runtime: len(skills_for_runtime)
            for runtime, skills_for_runtime in inventory.items()
        },
        "selected_skills": skill_names,
        "adapted_openclaw": sorted(adapted_openclaw),
        "skills": skills,
        "summary": {
            "shared_all": shared_all,
            "missing_by_runtime": missing_by_runtime,
            "codex_claude_drift": codex_claude_drift,
            "openclaw_adapted": openclaw_adapted,
            "openclaw_unexpected_drift": openclaw_unexpected_drift,
        },
    }


def print_list(title: str, values: list[str]) -> None:
    if values:
        print(f"{title}: {', '.join(values)}")
    else:
        print(f"{title}: none")


def print_text_report(report: dict[str, Any]) -> None:
    print("Skill Parity Report")
    print("===================")
    print()
    for runtime, root in report["runtime_roots"].items():
        count = report["inventory_counts"][runtime]
        print(f"{runtime:8} {count:3} skills  {root}")
    print()

    header = (
        f"{'Skill':24} {'Codex':7} {'Claude':7} {'OpenClaw':9} "
        f"{'Codex/Claude':13} {'OpenClaw compare'}"
    )
    print(header)
    print("-" * len(header))
    for item in report["skills"]:
        present = set(item["present"])
        codex = "yes" if "codex" in present else "missing"
        claude = "yes" if "claude" in present else "missing"
        openclaw = "yes" if "openclaw" in present else "missing"
        openclaw_status = item["openclaw_status"]
        if item["name"] in report["adapted_openclaw"] and openclaw_status == "different":
            openclaw_status = "adapted"
        print(
            f"{item['name']:24} {codex:7} {claude:7} {openclaw:9} "
            f"{item['codex_claude']:13} {openclaw_status}"
        )

    print()
    summary = report["summary"]
    print_list("Shared across all three", summary["shared_all"])
    for runtime, values in summary["missing_by_runtime"].items():
        print_list(f"Missing in {runtime}", values)
    print_list("Codex/Claude drift", summary["codex_claude_drift"])
    print_list("OpenClaw adapted ports", summary["openclaw_adapted"])
    print_list("OpenClaw unexpected drift", summary["openclaw_unexpected_drift"])


def has_strict_failures(report: dict[str, Any]) -> bool:
    summary = report["summary"]
    has_missing = any(summary["missing_by_runtime"].values())
    return bool(
        has_missing
        or summary["codex_claude_drift"]
        or summary["openclaw_unexpected_drift"]
    )


def main() -> int:
    args = parse_args()
    report = build_report(args)

    if args.json:
        print(json.dumps(report, indent=2, sort_keys=True))
    else:
        print_text_report(report)

    if args.strict and has_strict_failures(report):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
