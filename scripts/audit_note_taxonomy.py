#!/usr/bin/env python3
"""Audit investing vault folder taxonomy.

Flags source-person notes that are still stored in Actors/ even though their
tags mark them as analyst/strategist/commentator notes. Also flags stale
actor taxonomy markers on notes that already live in Analysts/.
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


def extract_frontmatter_type(content: str) -> str | None:
    """Extract a simple YAML frontmatter type field."""
    if not content.startswith("---"):
        return None

    end = content.find("---", 3)
    if end == -1:
        return None

    fm = content[3:end]
    match = re.search(r"^type:\s*([A-Za-z0-9_-]+)\s*$", fm, re.MULTILINE)
    return match.group(1) if match else None


def audit() -> list[dict[str, object]]:
    """Return notes that appear misplaced or carry stale taxonomy markers."""
    findings: list[dict[str, object]] = []

    if ACTORS.exists():
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
                    "issue": "source_person_in_actors",
                    "note": path.stem,
                    "path": str(path.relative_to(ROOT)).replace("\\", "/"),
                    "matched_tags": matched,
                    "suggested_path": str(destination.relative_to(ROOT)).replace("\\", "/"),
                    "destination_exists": destination.exists(),
                }
            )

    if ANALYSTS.exists():
        for path in sorted(ANALYSTS.glob("*.md")):
            try:
                content = path.read_text(encoding="utf-8")
            except (OSError, UnicodeDecodeError):
                continue

            tags = extract_tags(content)
            frontmatter_type = extract_frontmatter_type(content)
            if "actor" not in tags and frontmatter_type != "actor":
                continue

            findings.append(
                {
                    "issue": "actor_marker_in_analysts",
                    "note": path.stem,
                    "path": str(path.relative_to(ROOT)).replace("\\", "/"),
                    "matched_tags": ["actor"] if "actor" in tags else [],
                    "frontmatter_type": frontmatter_type,
                    "suggested_fix": "remove actor tag or change type to analyst",
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
            print("Taxonomy audit passed: analyst/source-person folder taxonomy is clean.")
        else:
            source_actor_findings = [
                item for item in findings if item["issue"] == "source_person_in_actors"
            ]
            stale_marker_findings = [
                item for item in findings if item["issue"] == "actor_marker_in_analysts"
            ]

            if source_actor_findings:
                print("Source-person notes still in Actors/:")
                for item in source_actor_findings:
                    tags = ", ".join(item["matched_tags"])
                    collision = " (destination exists)" if item["destination_exists"] else ""
                    print(f"- {item['path']} [{tags}] -> {item['suggested_path']}{collision}")

            if stale_marker_findings:
                if source_actor_findings:
                    print()
                print("Analysts/ notes still carrying actor taxonomy markers:")
                for item in stale_marker_findings:
                    tags = ", ".join(item["matched_tags"]) or "none"
                    note_type = item.get("frontmatter_type") or "none"
                    print(f"- {item['path']} [type={note_type}, tags={tags}]")

            print(f"TOTAL={len(findings)}")

    return 0 if args.no_fail or not findings else 1


if __name__ == "__main__":
    raise SystemExit(main())
