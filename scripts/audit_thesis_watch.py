"""Audit actor notes for the One-line read + What to watch structural slots.

Per feedback_thesis_and_watch_in_actor_notes (2026-05-12 refinement), every
mature actor note (and any concept/event note anchoring an active investment
case) must include:

  1. A One-line read sentence at the top — a single thesis sentence so a
     reader can extract "what's the bet" without scrolling.
  2. A What to watch dial-set near the bottom — 3-6 named signals pre-registering
     where future news, earnings, datapoints, and filings hook into the note.

Detection is strict: only an explicit section header / bolded prefix matching
the canonical name (or close synonyms) counts. Existing thesis-shaped prose
that isn't in a slot is NOT counted as "has the slot" — the whole point of
the rule is structural, not stylistic.

Usage:
    python scripts/audit_thesis_watch.py                 # all Actors/
    python scripts/audit_thesis_watch.py --min-lines 100 # mature only
    python scripts/audit_thesis_watch.py --since 2026-02-13  # git-touched window
    python scripts/audit_thesis_watch.py --folder Concepts   # other folder
    python scripts/audit_thesis_watch.py --report           # write markdown report
"""
from __future__ import annotations
import argparse
import csv
import re
import subprocess
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
VAULT = REPO / "investing"

# Canonical + acceptable variants for the One-line read slot.
ONE_LINER_HEADER_PATTERNS = [
    r"one[\s-]?line[\s-]?read",
    r"one[\s-]?liner",
    r"tl;?dr",
    r"the\s+bet",
    r"active\s+read",
    r"position\s+read",
    r"the\s+position",
]
ONE_LINER_HEADER_RE = re.compile(
    r"(?im)^#{1,6}\s*(" + "|".join(ONE_LINER_HEADER_PATTERNS) + r")\b"
)
ONE_LINER_BOLD_RE = re.compile(
    r"(?im)^\s*\*\*\s*(" + "|".join(ONE_LINER_HEADER_PATTERNS) + r")\s*\*\*\s*[:\-]"
)

WATCH_HEADER_PATTERNS = [
    r"what\s+to\s+watch(?:\s+for)?",
    r"watch[\s-]?list",
    r"signals?\s+to\s+watch",
    r"next\s+signals?",
    r"dials?\s+to\s+watch",
]
WATCH_HEADER_RE = re.compile(
    r"(?im)^#{1,6}\s*(" + "|".join(WATCH_HEADER_PATTERNS) + r")\b"
)

SYNOPSIS_RE = re.compile(r"(?im)^#{1,6}\s*synopsis\b")
FRONTMATTER_RE = re.compile(r"\A---\n.*?\n---\n", re.DOTALL)


def strip_frontmatter(text: str) -> str:
    m = FRONTMATTER_RE.match(text)
    return text[m.end():] if m else text


def has_one_liner(text: str) -> bool:
    """Search the top ~5000 chars (post-frontmatter) for an explicit slot."""
    body = strip_frontmatter(text)
    head = body[:5000]
    return bool(ONE_LINER_HEADER_RE.search(head) or ONE_LINER_BOLD_RE.search(head))


def has_watch_list(text: str) -> bool:
    """Anywhere in the note — watch lists conventionally live near the bottom
    but we don't care about position, only presence."""
    return bool(WATCH_HEADER_RE.search(text))


def has_synopsis(text: str) -> bool:
    return bool(SYNOPSIS_RE.search(text))


def git_touched_paths(folder: str, since: str) -> set[str]:
    """Return paths under investing/<folder>/ touched in git since the date."""
    out = subprocess.check_output(
        ["git", "log", f"--since={since}", "--name-only", "--pretty=format:",
         "--", f"investing/{folder}/"],
        cwd=REPO, text=True, errors="ignore",
    )
    prefix = f"investing/{folder}/"
    return {
        line.strip() for line in out.splitlines()
        if line.strip().startswith(prefix) and line.strip().endswith(".md")
    }


def audit(folder: str, min_lines: int, since: str | None) -> list[dict]:
    folder_path = VAULT / folder
    if not folder_path.is_dir():
        raise SystemExit(f"folder not found: {folder_path}")
    touched = git_touched_paths(folder, since) if since else None
    rows: list[dict] = []
    for md in sorted(folder_path.glob("*.md")):
        rel = md.relative_to(REPO).as_posix()
        if touched is not None and rel not in touched:
            continue
        try:
            text = md.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        lines = text.count("\n") + 1
        if lines < min_lines:
            continue
        rows.append({
            "path": rel,
            "lines": lines,
            "has_synopsis": has_synopsis(text),
            "has_one_liner": has_one_liner(text),
            "has_watch_list": has_watch_list(text),
        })
    return rows


def summarize(rows: list[dict]) -> dict:
    total = len(rows)
    syn = sum(1 for r in rows if r["has_synopsis"])
    ol = sum(1 for r in rows if r["has_one_liner"])
    wl = sum(1 for r in rows if r["has_watch_list"])
    both = sum(1 for r in rows if r["has_one_liner"] and r["has_watch_list"])
    neither = sum(1 for r in rows if not r["has_one_liner"] and not r["has_watch_list"])
    return {
        "total": total,
        "has_synopsis": syn,
        "has_one_liner": ol,
        "has_watch_list": wl,
        "both": both,
        "neither": neither,
    }


def write_csv(rows: list[dict], out: Path) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["path", "lines", "has_synopsis",
                                           "has_one_liner", "has_watch_list"])
        w.writeheader()
        for r in rows:
            w.writerow(r)


def write_report(rows: list[dict], out: Path, summary: dict, args) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    by_gap = {
        "Missing both (One-line read + What to watch)": [
            r for r in rows if not r["has_one_liner"] and not r["has_watch_list"]
        ],
        "Has watch list, missing One-line read": [
            r for r in rows if not r["has_one_liner"] and r["has_watch_list"]
        ],
        "Has One-line read, missing watch list": [
            r for r in rows if r["has_one_liner"] and not r["has_watch_list"]
        ],
        "Has both": [r for r in rows if r["has_one_liner"] and r["has_watch_list"]],
    }
    for bucket in by_gap.values():
        bucket.sort(key=lambda r: -r["lines"])

    lines = [
        "# Thesis & Watch-list Audit",
        "",
        f"Folder: `investing/{args.folder}/`  | min lines: {args.min_lines}"
        + (f"  | since: {args.since}" if args.since else ""),
        "",
        "## Summary",
        "",
        f"- Total notes scanned: **{summary['total']}**",
        f"- Has Synopsis section: {summary['has_synopsis']}",
        f"- Has One-line read slot: **{summary['has_one_liner']}**",
        f"- Has What to watch slot: **{summary['has_watch_list']}**",
        f"- Has both: **{summary['both']}**",
        f"- Has neither: **{summary['neither']}**",
        "",
    ]
    for label, bucket in by_gap.items():
        lines.append(f"## {label} ({len(bucket)})")
        lines.append("")
        if not bucket:
            lines.append("_(none)_")
            lines.append("")
            continue
        lines.append("| Lines | Path | Synopsis |")
        lines.append("|------:|------|:--------:|")
        for r in bucket[:50]:
            syn = "✓" if r["has_synopsis"] else "-"
            lines.append(f"| {r['lines']} | `{r['path']}` | {syn} |")
        if len(bucket) > 50:
            lines.append(f"_…and {len(bucket) - 50} more (full list in CSV)._")
        lines.append("")
    out.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--folder", default="Actors",
                   help="vault subfolder under investing/ (default: Actors)")
    p.add_argument("--min-lines", type=int, default=100,
                   help="line-count floor for 'mature' note (default: 100)")
    p.add_argument("--since", default=None,
                   help="optional git --since date to scope to touched notes")
    p.add_argument("--csv", default="tmp/thesis_watch_audit.csv",
                   help="CSV output path (relative to repo root)")
    p.add_argument("--report", action="store_true",
                   help="also write a markdown report")
    p.add_argument("--report-path", default="tmp/thesis_watch_audit.md",
                   help="markdown report path (relative to repo root)")
    args = p.parse_args()

    rows = audit(args.folder, args.min_lines, args.since)
    summary = summarize(rows)
    csv_path = REPO / args.csv
    write_csv(rows, csv_path)

    print(f"Folder: investing/{args.folder}/  | min lines: {args.min_lines}"
          + (f"  | since: {args.since}" if args.since else ""))
    print(f"Total scanned:       {summary['total']}")
    print(f"  has Synopsis:      {summary['has_synopsis']}")
    print(f"  has One-line read: {summary['has_one_liner']}")
    print(f"  has Watch list:    {summary['has_watch_list']}")
    print(f"  has both:          {summary['both']}")
    print(f"  has neither:       {summary['neither']}")
    print(f"\nCSV: {csv_path}")

    if args.report:
        rp = REPO / args.report_path
        write_report(rows, rp, summary, args)
        print(f"Report: {rp}")


if __name__ == "__main__":
    main()
