"""Remove bold markdown (**...**) from note bodies while preserving:
- Bold on header lines (lines starting with #)
- The first-mention of note name (typically the very first paragraph after frontmatter)
- Inline code blocks (which can use ** without intending bold)

Pre-existing bold cleanup for notes flagged by `check_note_compliance.py`.
"""
from __future__ import annotations
import argparse
import re
import sys
from pathlib import Path


def is_in_code_block(line: str, in_code: bool) -> tuple[bool, bool]:
    """Track triple-backtick code block state. Returns (new_state, is_currently_in_code)."""
    if line.strip().startswith("```"):
        return (not in_code, True)
    return (in_code, in_code)


def clean_bold(text: str, preserve_first_mention: bool = True) -> tuple[str, int]:
    """Strip **...** from body lines, preserving the first paragraph if requested.

    Returns (new_text, num_bolds_removed).
    """
    lines = text.split("\n")
    out: list[str] = []
    in_code = False
    in_frontmatter = False
    seen_first_para = False
    first_para_complete = False
    bolds_removed = 0

    for i, line in enumerate(lines):
        stripped = line.strip()

        # Frontmatter handling
        if i == 0 and stripped == "---":
            in_frontmatter = True
            out.append(line)
            continue
        if in_frontmatter:
            if stripped == "---":
                in_frontmatter = False
            out.append(line)
            continue

        # Code block tracking
        new_state, was_in_code = is_in_code_block(line, in_code)
        if was_in_code or stripped.startswith("```"):
            in_code = new_state
            out.append(line)
            continue
        in_code = new_state

        # Header line — leave as-is
        if stripped.startswith("#"):
            # Detect we've reached body content via the first H1 / H2 header line.
            # First paragraph is "the very first non-empty, non-header, non-frontmatter line(s)"
            out.append(line)
            continue

        # Track first paragraph (the very first non-empty body content)
        if not first_para_complete:
            if stripped == "":
                if seen_first_para:
                    first_para_complete = True
                out.append(line)
                continue
            seen_first_para = True
            # Preserve bold in first paragraph (note name first-mention)
            out.append(line)
            continue

        # Body line — strip bold markers
        # Match **text** but not ***text*** (italics + bold), and not single asterisks
        def strip_one(match):
            nonlocal bolds_removed
            bolds_removed += 1
            return match.group(1)

        new_line = re.sub(r"\*\*([^\*\n]+?)\*\*", strip_one, line)
        out.append(new_line)

    return "\n".join(out), bolds_removed


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("files", nargs="+", help="Markdown files to clean")
    parser.add_argument("--dry-run", action="store_true", help="Report counts, don't write")
    args = parser.parse_args()

    for path_str in args.files:
        path = Path(path_str)
        if not path.exists():
            print(f"  SKIP {path_str}: not found")
            continue
        original = path.read_text(encoding="utf-8")
        cleaned, count = clean_bold(original)
        if count == 0:
            print(f"  {path.name}: 0 bolds to remove")
            continue
        if args.dry_run:
            print(f"  {path.name}: would remove {count} bolds (dry run)")
        else:
            path.write_text(cleaned, encoding="utf-8")
            print(f"  {path.name}: removed {count} bolds")


if __name__ == "__main__":
    main()
