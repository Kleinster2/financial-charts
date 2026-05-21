#!/usr/bin/env python3
"""Audit investing vault folder taxonomy.

Flags source-person notes that are still stored in Actors/ even though their
tags mark them as analyst/strategist/commentator notes. Those notes should
normally live in Analysts/.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
VAULT = ROOT / "investing"
ACTORS = VAULT / "Actors"
ANALYSTS = VAULT / "Analysts"

SOURCE_PERSON_TAGS = {
    "analyst",
    "strategist",
    "commentator",
    "etf-analyst",
    "equity-strategist",
}


def extract_tags(content: str) -> set[str]:
    """Extract tags from YAML frontmatter and body hashtag lines."""
    tags: set[str] = set()

    if content.startswith("---"):
        end = content.find("---", 3)
        if end != -1:
            fm = content[3:end]
            inline = re.search(r"^tags:\s*\[([^\]]*)\]", fm, re.MULTILINE)
            if inline:
                tags.update(
                    tag.strip().strip('"').strip("'").lstrip("#")
                    for tag in inline.group(1).split(",")
                    if tag.strip()
                )

            block = re.search(r"^tags:\s*\n((?:\s+-\s+.+\n?)+)", fm, re.MULTILINE)
            if block:
                tags.update(
                    tag.strip().strip('"').strip("'").lstrip("#")
                    for tag in re.findall(r"^\s+-\s+(.+?)$", block.group(1), re.MULTILINE)
                    if tag.strip()
                )

    for tag in re.findall(r"(?<!\w)#([A-Za-z0-9_-]+)\b", content):
        tags.add(tag)

    return tags


def audit() -> list[dict[str, object]]:
    """Return source-person notes that appear misplaced in Actors/."""
    findings: list[dict[str, object]] = []
    if not ACTORS.exists():
        return findings

    for path in sorted(ACTORS.glob("*.md")):
        try:
            content = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue

        tags = extract_tags(content)
        matched = sorted(tags & SOURCE_PERSON_TAGS)
        if not matched:
            continue

        destination = ANALYSTS / path.name
        findings.append(
            {
                "note": path.stem,
                "path": str(path.relative_to(ROOT)).replace("\\", "/"),
                "matched_tags": matched,
                "suggested_path": str(destination.relative_to(ROOT)).replace("\\", "/"),
                "destination_exists": destination.exists(),
            }
        )

    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit investing note folder taxonomy")
    parser.add_argument("--json", action="store_true", help="Emit JSON")
    parser.add_argument("--no-fail", action="store_true", help="Exit 0 even when findings exist")
    args = parser.parse_args()

    findings = audit()

    if args.json:
        print(json.dumps({"findings": findings, "count": len(findings)}, indent=2))
    else:
        if not findings:
            print("Taxonomy audit passed: no analyst/strategist source-person tags remain in Actors/.")
        else:
            print("Source-person notes still in Actors/:")
            for item in findings:
                tags = ", ".join(item["matched_tags"])
                collision = " (destination exists)" if item["destination_exists"] else ""
                print(f"- {item['path']} [{tags}] -> {item['suggested_path']}{collision}")
            print(f"TOTAL={len(findings)}")

    return 0 if args.no_fail or not findings else 1


if __name__ == "__main__":
    raise SystemExit(main())
