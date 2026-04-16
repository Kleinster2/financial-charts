#!/usr/bin/env python3
"""
Weekly vault maintenance report.

Generates an actionable review covering stub quality, chart staleness,
thesis freshness, and daily-to-evergreen promotion candidates.

Usage:
    python scripts/vault_review.py              # Full report
    python scripts/vault_review.py --stubs      # Stub/backlink audit only
    python scripts/vault_review.py --charts     # Chart staleness only
    python scripts/vault_review.py --theses     # Thesis review only
    python scripts/vault_review.py --promote    # Daily promotion candidates
    python scripts/vault_review.py --chart-age 7   # Charts older than 7 days
    python scripts/vault_review.py --stub-lines 40 # Stub threshold (lines)
"""

import argparse
import os
import re
import sys
import time
from collections import defaultdict
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional


VAULT_ROOT = Path(__file__).parent.parent / "investing"
ATTACHMENTS_DIR = VAULT_ROOT / "attachments"
DAILY_DIR = VAULT_ROOT / "Daily"

# Folders to skip when scanning notes
SKIP_FOLDERS = {"attachments", ".obsidian", ".trash", "Reports"}

# Chart embed pattern
EMBED_PATTERN = re.compile(r"!\[\[([^\]]+\.png)\]\]")

# Wikilink pattern (captures link target, ignoring display text)
WIKILINK_PATTERN = re.compile(r"\[\[([^\]|#]+)(?:[|#][^\]]+)?\]\]")

# Frontmatter extraction
FRONTMATTER_PATTERN = re.compile(r"^---\s*\n(.*?)\n---", re.DOTALL)


def parse_frontmatter(content: str) -> dict:
    """Extract frontmatter fields as a simple dict."""
    m = FRONTMATTER_PATTERN.match(content)
    if not m:
        return {}
    fm = {}
    for line in m.group(1).split("\n"):
        if ":" in line:
            key, _, val = line.partition(":")
            fm[key.strip()] = val.strip()
    return fm


def get_tags(content: str) -> set[str]:
    """Extract hashtags from content (outside frontmatter)."""
    # Strip frontmatter first
    body = FRONTMATTER_PATTERN.sub("", content)
    return set(re.findall(r"(?<!\w)#(\w+)(?=\s|$)", body))


def body_line_count(content: str) -> int:
    """Count non-empty lines in the body (after frontmatter)."""
    body = FRONTMATTER_PATTERN.sub("", content).strip()
    return len([l for l in body.split("\n") if l.strip()])


def scan_vault() -> dict:
    """Scan all vault notes and return structured data.

    Returns dict with:
        notes: {stem: {path, content, lines, tags, frontmatter, embeds, links}}
        inbound: {stem: set of stems that link to it}
        chart_files: {filename: Path}
    """
    notes = {}
    inbound = defaultdict(set)
    chart_files = {}

    # Index chart files in attachments
    if ATTACHMENTS_DIR.exists():
        for f in ATTACHMENTS_DIR.iterdir():
            if f.suffix.lower() == ".png":
                chart_files[f.name] = f

    # Scan all notes
    for md_file in VAULT_ROOT.rglob("*.md"):
        # Skip folders we don't care about
        rel = md_file.relative_to(VAULT_ROOT)
        if rel.parts[0] in SKIP_FOLDERS:
            continue

        try:
            content = md_file.read_text(encoding="utf-8")
        except (UnicodeDecodeError, PermissionError):
            continue

        stem = md_file.stem
        tags = get_tags(content)
        fm = parse_frontmatter(content)
        lines = body_line_count(content)
        embeds = EMBED_PATTERN.findall(content)
        links = set(WIKILINK_PATTERN.findall(content))

        notes[stem] = {
            "path": md_file,
            "content": content,
            "lines": lines,
            "tags": tags,
            "frontmatter": fm,
            "embeds": embeds,
            "links": links,
            "folder": rel.parts[0] if len(rel.parts) > 1 else "",
        }

    # Build inbound link index
    for stem, data in notes.items():
        for link_target in data["links"]:
            inbound[link_target].add(stem)

    return {"notes": notes, "inbound": inbound, "chart_files": chart_files}


# ---------------------------------------------------------------------------
# Report: Stub / Backlink Audit
# ---------------------------------------------------------------------------

def report_stubs(vault_data: dict, stub_threshold: int = 40) -> list[str]:
    """Find thin notes and cross-reference with inbound link counts.

    Returns formatted report lines.
    """
    notes = vault_data["notes"]
    inbound = vault_data["inbound"]

    stubs = []
    for stem, data in notes.items():
        # Skip daily notes and meta
        if data["folder"] in ("Daily", "Meta"):
            continue
        if data["lines"] <= stub_threshold:
            in_count = len(inbound.get(stem, set()))
            stubs.append((stem, data["lines"], in_count, data["folder"], data["path"]))

    if not stubs:
        return ["No stubs found (all notes > {} lines).".format(stub_threshold)]

    # Split into categories
    high_inbound = sorted(
        [(s, l, i, f, p) for s, l, i, f, p in stubs if i >= 3],
        key=lambda x: -x[2],
    )
    zero_inbound = sorted(
        [(s, l, i, f, p) for s, l, i, f, p in stubs if i == 0],
        key=lambda x: x[0],
    )
    low_inbound = sorted(
        [(s, l, i, f, p) for s, l, i, f, p in stubs if 0 < i < 3],
        key=lambda x: -x[2],
    )

    lines = []
    lines.append(f"## Stub Audit (<={stub_threshold} body lines)")
    lines.append(f"Total stubs: {len(stubs)}")
    lines.append("")

    if high_inbound:
        lines.append(f"### Merge candidates (>=3 inbound links but thin) -- {len(high_inbound)} notes")
        lines.append("These are referenced often but have little content. Upgrade or merge.")
        lines.append("")
        lines.append("| Note | Lines | Inbound | Folder |")
        lines.append("|------|------:|--------:|--------|")
        for stem, ln, inc, folder, _ in high_inbound[:30]:
            lines.append(f"| {stem} | {ln} | {inc} | {folder} |")
        lines.append("")

    if zero_inbound:
        lines.append(f"### Retirement candidates (0 inbound links) — {len(zero_inbound)} notes")
        lines.append("Nothing links here. Safe to retire or merge into a parent note.")
        lines.append("")
        lines.append("| Note | Lines | Folder |")
        lines.append("|------|------:|--------|")
        for stem, ln, _, folder, _ in zero_inbound[:30]:
            lines.append(f"| {stem} | {ln} | {folder} |")
        if len(zero_inbound) > 30:
            lines.append(f"| ... and {len(zero_inbound) - 30} more | | |")
        lines.append("")

    if low_inbound:
        lines.append(f"### Low-priority stubs (1-2 inbound links) — {len(low_inbound)} notes")
        lines.append("")
        lines.append("| Note | Lines | Inbound | Folder |")
        lines.append("|------|------:|--------:|--------|")
        for stem, ln, inc, folder, _ in low_inbound[:20]:
            lines.append(f"| {stem} | {ln} | {inc} | {folder} |")
        if len(low_inbound) > 20:
            lines.append(f"| ... and {len(low_inbound) - 20} more | | | |")
        lines.append("")

    return lines


# ---------------------------------------------------------------------------
# Report: Chart Staleness
# ---------------------------------------------------------------------------

def report_chart_staleness(vault_data: dict, max_age_days: int = 14) -> list[str]:
    """Find embedded charts that haven't been regenerated recently.

    Checks chart file modification time against the threshold.
    Only reports charts embedded in non-daily, non-meta notes.
    """
    notes = vault_data["notes"]
    chart_files = vault_data["chart_files"]
    cutoff = datetime.now() - timedelta(days=max_age_days)

    stale = []
    missing = []
    seen_charts = set()

    for stem, data in notes.items():
        if data["folder"] in ("Daily", "Meta"):
            continue
        for embed_name in data["embeds"]:
            if embed_name in seen_charts:
                continue
            seen_charts.add(embed_name)

            chart_path = chart_files.get(embed_name)
            if not chart_path:
                # Chart might be in the same folder or truly missing
                local_path = data["path"].parent / embed_name
                if local_path.exists():
                    chart_path = local_path
                else:
                    missing.append((embed_name, stem))
                    continue

            mtime = datetime.fromtimestamp(chart_path.stat().st_mtime)
            age_days = (datetime.now() - mtime).days
            if mtime < cutoff:
                file_size = chart_path.stat().st_size
                stale.append((embed_name, age_days, stem, file_size))

    lines = []
    lines.append(f"## Chart Staleness (>{max_age_days} days old)")
    lines.append("")

    if stale:
        stale.sort(key=lambda x: -x[1])
        lines.append(f"### Stale charts — {len(stale)} files")
        lines.append("")
        lines.append("| Chart | Age (days) | Embedded in | Size |")
        lines.append("|-------|----------:|-----------:|-----:|")
        for name, age, note, size in stale[:40]:
            size_str = f"{size:,}" if size > 1024 else f"**{size}B**"
            lines.append(f"| {name} | {age} | {note} | {size_str} |")
        if len(stale) > 40:
            lines.append(f"| ... and {len(stale) - 40} more | | | |")
        lines.append("")
    else:
        lines.append(f"All embedded charts are within {max_age_days} days. No action needed.")
        lines.append("")

    if missing:
        lines.append(f"### Missing chart files — {len(missing)}")
        lines.append("")
        for name, note in missing[:15]:
            lines.append(f"- `{name}` (referenced in {note})")
        lines.append("")

    return lines


# ---------------------------------------------------------------------------
# Report: Thesis Freshness
# ---------------------------------------------------------------------------

def report_theses(vault_data: dict, stale_days: int = 30) -> list[str]:
    """Review thesis notes for staleness.

    Checks last_reviewed frontmatter and file modification date.
    """
    notes = vault_data["notes"]

    theses = []
    for stem, data in notes.items():
        if "thesis" not in data["tags"]:
            continue

        fm = data["frontmatter"]
        last_reviewed = fm.get("last_reviewed", "")
        status = fm.get("status", "unknown")

        # Parse last_reviewed date
        reviewed_date = None
        if last_reviewed:
            try:
                reviewed_date = datetime.strptime(last_reviewed, "%Y-%m-%d")
            except ValueError:
                pass

        # Fallback to file mtime
        mtime = datetime.fromtimestamp(data["path"].stat().st_mtime)

        reference_date = reviewed_date or mtime
        age_days = (datetime.now() - reference_date).days
        has_reviewed = reviewed_date is not None

        theses.append((stem, status, age_days, has_reviewed, data["lines"]))

    lines = []
    lines.append("## Thesis Review")
    lines.append("")

    if not theses:
        lines.append("No #thesis notes found.")
        return lines

    theses.sort(key=lambda x: -x[2])

    stale_theses = [(s, st, a, hr, l) for s, st, a, hr, l in theses if a > stale_days]
    fresh_theses = [(s, st, a, hr, l) for s, st, a, hr, l in theses if a <= stale_days]

    lines.append(f"Total thesis notes: {len(theses)}")
    lines.append("")

    if stale_theses:
        lines.append(f"### Needs review (>{stale_days} days since last review/edit) — {len(stale_theses)}")
        lines.append("")
        lines.append("| Thesis | Status | Days stale | Has last_reviewed | Lines |")
        lines.append("|--------|--------|----------:|:-----------------:|------:|")
        for stem, status, age, has_rev, ln in stale_theses:
            rev_marker = "yes" if has_rev else "no"
            lines.append(f"| {stem} | {status} | {age} | {rev_marker} | {ln} |")
        lines.append("")

    if fresh_theses:
        lines.append(f"### Recently reviewed — {len(fresh_theses)}")
        lines.append("")
        for stem, status, age, _, ln in fresh_theses:
            lines.append(f"- {stem} ({status}, {age}d ago, {ln} lines)")
        lines.append("")

    # Check for theses missing last_reviewed
    no_reviewed = [s for s, _, _, hr, _ in theses if not hr]
    if no_reviewed:
        lines.append(f"### Missing `last_reviewed` frontmatter — {len(no_reviewed)}")
        lines.append("")
        for stem in no_reviewed:
            lines.append(f"- {stem}")
        lines.append("")

    return lines


# ---------------------------------------------------------------------------
# Report: Daily-to-Evergreen Promotion
# ---------------------------------------------------------------------------

def report_promotion_candidates(vault_data: dict, lookback_days: int = 14) -> list[str]:
    """Find wikilinks in recent daily notes that point to stubs.

    These are facts that entered via daily ingestion but haven't been
    promoted into fleshed-out evergreen notes yet.
    """
    notes = vault_data["notes"]
    cutoff = datetime.now() - timedelta(days=lookback_days)

    # Identify stubs (thin notes)
    stub_stems = set()
    for stem, data in notes.items():
        if data["folder"] in ("Daily", "Meta"):
            continue
        if data["lines"] <= 40:
            stub_stems.add(stem)

    # Scan recent daily notes for links to stubs
    promotions = defaultdict(set)  # stub_stem -> set of daily notes referencing it
    for stem, data in notes.items():
        if data["folder"] != "Daily":
            continue
        # Parse date from filename
        try:
            note_date = datetime.strptime(stem, "%Y-%m-%d")
        except ValueError:
            continue
        if note_date < cutoff:
            continue

        for link_target in data["links"]:
            if link_target in stub_stems:
                promotions[link_target].add(stem)

    lines = []
    lines.append(f"## Promotion Candidates (last {lookback_days} days)")
    lines.append("Stubs referenced in recent daily notes — candidates for upgrade.")
    lines.append("")

    if not promotions:
        lines.append("No promotion candidates found.")
        return lines

    # Sort by number of daily references (most-referenced stubs first)
    ranked = sorted(promotions.items(), key=lambda x: -len(x[1]))

    lines.append(f"Found {len(ranked)} stubs referenced in recent dailies.")
    lines.append("")
    lines.append("| Stub | Daily mentions | Folder | Lines |")
    lines.append("|------|-------------:|--------|------:|")
    for stub_stem, daily_refs in ranked[:30]:
        data = notes.get(stub_stem)
        if data:
            lines.append(
                f"| {stub_stem} | {len(daily_refs)} | {data['folder']} | {data['lines']} |"
            )
        else:
            lines.append(f"| {stub_stem} (no note) | {len(daily_refs)} | — | — |")
    if len(ranked) > 30:
        lines.append(f"| ... and {len(ranked) - 30} more | | | |")
    lines.append("")

    return lines


# ---------------------------------------------------------------------------
# Report: Summary Statistics
# ---------------------------------------------------------------------------

def report_summary(vault_data: dict) -> list[str]:
    """Top-level vault statistics."""
    notes = vault_data["notes"]
    inbound = vault_data["inbound"]

    total = len(notes)
    by_folder = defaultdict(int)
    total_links = 0
    for stem, data in notes.items():
        by_folder[data["folder"]] += 1
        total_links += len(data["links"])

    # Orphans: notes with 0 inbound links (excluding Daily, Meta)
    orphans = []
    for stem, data in notes.items():
        if data["folder"] in ("Daily", "Meta"):
            continue
        if len(inbound.get(stem, set())) == 0:
            orphans.append(stem)

    # Dead ends: notes with 0 outbound links (excluding Daily, Meta)
    dead_ends = []
    for stem, data in notes.items():
        if data["folder"] in ("Daily", "Meta"):
            continue
        if len(data["links"]) == 0:
            dead_ends.append(stem)

    lines = []
    lines.append("## Vault Summary")
    lines.append("")
    lines.append(f"- **Total notes:** {total}")
    lines.append(f"- **Total wikilinks:** {total_links:,}")
    lines.append(f"- **Orphan notes** (0 inbound): {len(orphans)}")
    lines.append(f"- **Dead-end notes** (0 outbound): {len(dead_ends)}")
    lines.append("")

    lines.append("### Notes by folder")
    lines.append("")
    lines.append("| Folder | Count |")
    lines.append("|--------|------:|")
    for folder, count in sorted(by_folder.items(), key=lambda x: -x[1]):
        label = folder if folder else "(root)"
        lines.append(f"| {label} | {count} |")
    lines.append("")

    return lines


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Weekly vault maintenance report",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--stubs", action="store_true", help="Stub/backlink audit only")
    parser.add_argument("--charts", action="store_true", help="Chart staleness only")
    parser.add_argument("--theses", action="store_true", help="Thesis review only")
    parser.add_argument("--promote", action="store_true", help="Daily promotion candidates only")
    parser.add_argument("--chart-age", type=int, default=14, help="Chart staleness threshold in days (default: 14)")
    parser.add_argument("--stub-lines", type=int, default=40, help="Stub line threshold (default: 40)")
    parser.add_argument("--thesis-age", type=int, default=30, help="Thesis staleness in days (default: 30)")
    parser.add_argument("--promote-days", type=int, default=14, help="Daily lookback for promotion (default: 14)")
    args = parser.parse_args()

    # If no specific report requested, run all
    run_all = not any([args.stubs, args.charts, args.theses, args.promote])

    print("Scanning vault...", end=" ", flush=True)
    start = time.time()
    vault_data = scan_vault()
    elapsed = time.time() - start
    print(f"done ({len(vault_data['notes'])} notes, {elapsed:.1f}s)")
    print()

    output = []

    if run_all:
        output.extend(report_summary(vault_data))

    if run_all or args.stubs:
        output.extend(report_stubs(vault_data, args.stub_lines))

    if run_all or args.charts:
        output.extend(report_chart_staleness(vault_data, args.chart_age))

    if run_all or args.theses:
        output.extend(report_theses(vault_data, args.thesis_age))

    if run_all or args.promote:
        output.extend(report_promotion_candidates(vault_data, args.promote_days))

    print("\n".join(output))


if __name__ == "__main__":
    main()
