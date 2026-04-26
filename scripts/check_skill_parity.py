#!/usr/bin/env python3
"""
Compare shared skills across Codex, Claude Code, and OpenClaw.

Usage:
    python scripts/check_skill_parity.py
    python scripts/check_skill_parity.py news ingest earnings
    python scripts/check_skill_parity.py --all
    python scripts/check_skill_parity.py --json
    python scripts/check_skill_parity.py --strict
    python scripts/check_skill_parity.py --strict --optional-openclaw
"""

from __future__ import annotations

import argparse
import difflib
import hashlib
import json
import os
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from skill_manifest import read_manifest_list


REPO_ROOT = Path(__file__).resolve().parent.parent
RUNTIMES = {
    "codex": REPO_ROOT / ".agents" / "skills",
    "claude": REPO_ROOT / ".claude" / "skills",
    "openclaw": Path(
        os.environ.get("OPENCLAW_SKILLS_DIR", r"C:\Users\klein\clawd\skills")
    ),
}


@dataclass(frozen=True)
class SkillFile:
    path: Path
    digest: str
    semantic_digest: str
    lines: int
    semantic_lines: int


def read_normalized_text(path: Path) -> str:
    raw = path.read_bytes()
    text = raw.decode("utf-8-sig")
    return text.replace("\r\n", "\n").replace("\r", "\n")


def normalized_digest(path: Path) -> tuple[str, int]:
    """Hash text with normalized newlines so CRLF/LF churn is ignored."""
    normalized = read_normalized_text(path)
    digest = hashlib.sha256(normalized.encode("utf-8")).hexdigest()
    return digest, len(normalized.splitlines())


TYPOGRAPHIC_EQUIVALENTS = str.maketrans(
    {
        "\u2014": "-",
        "\u2013": "-",
        "\u2192": "->",
        "\u2190": "<-",
        "\u2018": "'",
        "\u2019": "'",
        "\u201c": '"',
        "\u201d": '"',
    }
)


REPO_ROOT_VARIANTS = {
    str(REPO_ROOT),
    str(REPO_ROOT).replace("\\", "/"),
    r"C:\Users\klein\financial-charts",
    "C:/Users/klein/financial-charts",
}


RUNTIME_ONLY_LINE_PATTERNS = [
    re.compile(r"^\s*Set-Location\s+\.\s*$"),
    re.compile(r"^\s*Get-Content\s+CLAUDE\.md\s*$"),
]


RUNTIME_ONLY_SENTENCES = [
    " Before reading or writing vault files, run `Set-Location .` and read `CLAUDE.md`.",
]


def normalize_repo_paths(text: str) -> str:
    """Collapse runtime-specific absolute repo paths into repo-relative paths."""
    normalized = text
    for root in sorted(REPO_ROOT_VARIANTS, key=len, reverse=True):
        normalized = normalized.replace(f"{root}\\", "")
        normalized = normalized.replace(f"{root}/", "")
        normalized = normalized.replace(root, ".")
    return normalized.replace("\\", "/")


def semantic_text(path: Path) -> str:
    """
    Normalize only differences that should not change workflow meaning.

    OpenClaw ports may need absolute repo paths, shell setup lines, and ASCII-safe
    punctuation. After removing those runtime details, adapted ports should still
    say the same thing as the Codex/Claude source.
    """
    text = read_normalized_text(path).translate(TYPOGRAPHIC_EQUIVALENTS)
    text = normalize_repo_paths(text)

    lines: list[str] = []
    for line in text.split("\n"):
        for sentence in RUNTIME_ONLY_SENTENCES:
            line = line.replace(sentence, "")
        line = re.sub(r" for the investing vault at `\.`", "", line)
        line = re.sub(r" from `\.`", "", line)
        line = re.sub(r" at `\.`", "", line)
        line = line.rstrip()
        if any(pattern.match(line) for pattern in RUNTIME_ONLY_LINE_PATTERNS):
            continue
        lines.append(line)

    return "\n".join(lines)


def semantic_digest(path: Path) -> tuple[str, int]:
    normalized = semantic_text(path)
    digest = hashlib.sha256(normalized.encode("utf-8")).hexdigest()
    return digest, len(normalized.splitlines())


def first_semantic_diff(left: SkillFile, right: SkillFile, limit: int = 8) -> list[str]:
    """Return a small normalized diff preview for diagnostics."""
    diff = difflib.unified_diff(
        semantic_text(left.path).splitlines(),
        semantic_text(right.path).splitlines(),
        fromfile=str(left.path),
        tofile=str(right.path),
        lineterm="",
        n=2,
    )
    lines: list[str] = []
    for line in diff:
        lines.append(line)
        if len(lines) >= limit:
            break
    return lines


def discover(root: Path) -> dict[str, SkillFile]:
    skills: dict[str, SkillFile] = {}
    if not root.exists():
        return skills

    for child in sorted(root.iterdir(), key=lambda p: p.name.lower()):
        skill_file = child / "SKILL.md"
        if not child.is_dir() or not skill_file.exists():
            continue
        digest, lines = normalized_digest(skill_file)
        sem_digest, sem_lines = semantic_digest(skill_file)
        skills[child.name] = SkillFile(skill_file, digest, sem_digest, lines, sem_lines)
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
        "--optional-openclaw",
        action="store_true",
        help=(
            "Skip OpenClaw comparison when its skills directory is absent. "
            "Useful in CI checkouts that only contain this repository."
        ),
    )
    parser.add_argument(
        "--adapted-openclaw",
        nargs="*",
        default=None,
        help=(
            "OpenClaw skills expected to differ from Codex/Claude because "
            "they are runtime-adapted ports. Defaults to the shared workflow manifest."
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
    canonical = codex or claude

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

    openclaw_semantic = "skipped"
    semantic_diff: list[str] = []
    if "openclaw" in inventory and not openclaw:
        openclaw_semantic = "missing"
    elif openclaw and canonical:
        if openclaw.semantic_digest == canonical.semantic_digest:
            openclaw_semantic = "same"
        else:
            openclaw_semantic = "different"
            semantic_diff = first_semantic_diff(canonical, openclaw)
    elif openclaw:
        openclaw_semantic = "n/a"

    hashes = {
        runtime: item.digest[:12] if item else None for runtime, item in entries.items()
    }
    semantic_hashes = {
        runtime: item.semantic_digest[:12] if item else None
        for runtime, item in entries.items()
    }
    lines = {runtime: item.lines if item else None for runtime, item in entries.items()}
    semantic_lines = {
        runtime: item.semantic_lines if item else None for runtime, item in entries.items()
    }
    paths = {runtime: str(item.path) if item else None for runtime, item in entries.items()}

    return {
        "name": name,
        "present": present,
        "missing": missing,
        "codex_claude": codex_claude,
        "openclaw_status": openclaw_status,
        "openclaw_semantic": openclaw_semantic,
        "hashes": hashes,
        "semantic_hashes": semantic_hashes,
        "lines": lines,
        "semantic_lines": semantic_lines,
        "paths": paths,
        "semantic_diff": semantic_diff,
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

    return read_manifest_list("workflowSkills")


def build_report(args: argparse.Namespace) -> dict[str, Any]:
    runtime_roots = dict(RUNTIMES)
    runtime_roots["openclaw"] = args.openclaw_skills
    skipped_runtimes = []
    if args.optional_openclaw and not runtime_roots["openclaw"].exists():
        skipped_runtimes.append("openclaw")
        runtime_roots.pop("openclaw")

    inventory = {runtime: discover(root) for runtime, root in runtime_roots.items()}
    skill_names = resolve_skill_names(args, inventory)
    adapted_values = (
        read_manifest_list("openclawAdapted")
        if args.adapted_openclaw is None
        else args.adapted_openclaw
    )
    adapted_openclaw = set(adapted_values)
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
    openclaw_semantic_drift = [
        item["name"] for item in skills if item["openclaw_semantic"] == "different"
    ]

    return {
        "runtime_roots": {runtime: str(root) for runtime, root in runtime_roots.items()},
        "inventory_counts": {
            runtime: len(skills_for_runtime)
            for runtime, skills_for_runtime in inventory.items()
        },
        "selected_skills": skill_names,
        "adapted_openclaw": sorted(adapted_openclaw),
        "skipped_runtimes": skipped_runtimes,
        "skills": skills,
        "summary": {
            "shared_all": shared_all,
            "missing_by_runtime": missing_by_runtime,
            "codex_claude_drift": codex_claude_drift,
            "openclaw_adapted": openclaw_adapted,
            "openclaw_semantic_drift": openclaw_semantic_drift,
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
    for runtime in report["skipped_runtimes"]:
        print(f"{runtime:8} skipped   directory not found")
    print()

    header = (
        f"{'Skill':24} {'Codex':7} {'Claude':7} {'OpenClaw':9} "
        f"{'Codex/Claude':13} {'OpenClaw compare':17} {'Semantic'}"
    )
    print(header)
    print("-" * len(header))
    for item in report["skills"]:
        present = set(item["present"])
        codex = "yes" if "codex" in present else "missing"
        claude = "yes" if "claude" in present else "missing"
        if "openclaw" in report["skipped_runtimes"]:
            openclaw = "skipped"
        else:
            openclaw = "yes" if "openclaw" in present else "missing"
        openclaw_status = item["openclaw_status"]
        if item["name"] in report["adapted_openclaw"] and openclaw_status == "different":
            openclaw_status = "adapted"
        print(
            f"{item['name']:24} {codex:7} {claude:7} {openclaw:9} "
            f"{item['codex_claude']:13} {openclaw_status:17} "
            f"{item['openclaw_semantic']}"
        )

    print()
    summary = report["summary"]
    shared_label = "Shared across selected runtimes"
    if not report["skipped_runtimes"]:
        shared_label = "Shared across all three"
    print_list(shared_label, summary["shared_all"])
    for runtime, values in summary["missing_by_runtime"].items():
        print_list(f"Missing in {runtime}", values)
    print_list("Codex/Claude drift", summary["codex_claude_drift"])
    print_list("OpenClaw adapted ports", summary["openclaw_adapted"])
    print_list("OpenClaw semantic drift", summary["openclaw_semantic_drift"])
    print_list("OpenClaw unexpected drift", summary["openclaw_unexpected_drift"])
    if summary["openclaw_semantic_drift"]:
        print("Semantic drift previews are available with --json.")


def has_strict_failures(report: dict[str, Any]) -> bool:
    summary = report["summary"]
    has_missing = any(summary["missing_by_runtime"].values())
    return bool(
        has_missing
        or summary["codex_claude_drift"]
        or summary["openclaw_semantic_drift"]
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
