"""Fix broken YAML frontmatter where aliases contain wikilinks.

Pattern: aliases: [[[Foo]] Bar, Baz] — strict YAML can't parse this because
[[ starts a nested flow sequence and the syntax is malformed. The intent is
"alias as a string that visually emphasizes a sub-name." The fix strips
the wikilink brackets from anywhere inside the frontmatter, leaving plain
strings: aliases: [Foo Bar, Baz].

Only modifies the frontmatter block (between leading --- and --- markers).
Note bodies (where wikilinks belong) are untouched.

Usage:
  python scripts/fix_alias_wikilinks.py investing            # apply fix
  python scripts/fix_alias_wikilinks.py investing --dry-run  # preview only
"""
import re
import sys
from pathlib import Path

FRONTMATTER_RE = re.compile(r"^(---\r?\n)(.+?)(\r?\n---\r?\n)", re.DOTALL)


def process(path, dry_run=False):
    content = path.read_text(encoding="utf-8")
    m = FRONTMATTER_RE.match(content)
    if not m:
        return None

    pre, fm_body, post = m.groups()

    if "[[" not in fm_body and "]]" not in fm_body:
        return None

    new_fm = fm_body.replace("[[", "").replace("]]", "")
    if new_fm == fm_body:
        return None

    if not dry_run:
        new_content = pre + new_fm + post + content[m.end():]
        path.write_text(new_content, encoding="utf-8")

    return (fm_body, new_fm)


def main():
    args = sys.argv[1:]
    dry_run = "--dry-run" in args
    args = [a for a in args if not a.startswith("--")]
    root = Path(args[0]) if args else Path("investing")

    fixed = []
    for p in sorted(root.rglob("*.md")):
        result = process(p, dry_run=dry_run)
        if result is None:
            continue
        old, new = result
        rel = p.relative_to(root.parent if root.parent != Path(".") else Path("."))
        fixed.append(rel)
        if dry_run:
            print(f"[DRY] {rel}")
            for old_line, new_line in zip(old.split("\n"), new.split("\n")):
                if old_line != new_line:
                    print(f"      - {old_line!r}")
                    print(f"      + {new_line!r}")
        else:
            print(f"fixed {rel}")

    print(f"\nTotal {'would fix' if dry_run else 'fixed'}: {len(fixed)}")


if __name__ == "__main__":
    main()
