#!/usr/bin/env python3
"""Stop hook: ensure entities recently logged in the daily note's edit log
also appear in the '## Notes created/expanded' summary section.

Exit codes:
  0  pass (no recent entries, no daily note, or all entities summarized)
  2  block — recent edits lack a matching summary line
  1  unexpected error
"""

import os
import re
import sys
import unicodedata
from datetime import datetime, timedelta


def get_project_dir():
    return os.environ.get("CLAUDE_PROJECT_DIR") or os.getcwd()


def get_markdown_section(text, heading):
    pattern = rf"(?ms)^{re.escape(heading)}\s*$\n?(.*?)(?=^## |\Z)"
    m = re.search(pattern, text)
    return m.group(1).strip() if m else ""


def repair_double_utf8(s):
    """Reverse double-encoded UTF-8 (é stored as Ã©).

    Try latin-1 first, then cp1252. Windows tooling double-encodes via cp1252,
    whose 0x80-0x9F map to printable characters (‰, œ, …) that fall outside
    latin-1's range — which is why CJK note names (中特估, 东数西算) failed to
    repair and tripped the daily-note gate even when correctly summarized.
    """
    for codec in ("latin-1", "cp1252"):
        try:
            repaired = s.encode(codec).decode("utf-8")
            return unicodedata.normalize("NFC", repaired)
        except (UnicodeEncodeError, UnicodeDecodeError):
            continue
    return s


def read_note(path):
    with open(path, "r", encoding="utf-8") as f:
        return unicodedata.normalize("NFC", f.read())


def main():
    today = datetime.now()
    today_str = today.strftime("%Y-%m-%d")
    project_dir = get_project_dir()

    daily_note = os.path.join(project_dir, "investing", "Daily", f"{today_str}.md")
    if not os.path.isfile(daily_note):
        return 0

    text = read_note(daily_note)
    edit_log = get_markdown_section(text, "## Edit log")
    if not edit_log.strip():
        return 0

    # Only entries from the last 120 minutes count, to avoid false positives
    # from prior sessions whose summaries may not yet be written.
    cutoff = timedelta(minutes=120)
    entry_re = re.compile(r"^\s*-\s+(\d{1,2}):(\d{2})\s+-\s+edited\s+\[\[([^\]|]+)")

    recent = []
    for line in edit_log.splitlines():
        m = entry_re.match(line)
        if not m:
            continue
        hour, minute, entity = int(m.group(1)), int(m.group(2)), m.group(3)
        entry_time = today.replace(hour=hour, minute=minute, second=0, microsecond=0)
        # Midnight wraparound: future-stamped entries belong to yesterday.
        if entry_time > today + timedelta(minutes=5):
            entry_time -= timedelta(days=1)
        diff = today - entry_time
        if timedelta(0) <= diff <= cutoff:
            recent.append(unicodedata.normalize("NFC", entity))

    entities = sorted(set(recent))
    if not entities:
        return 0

    summary = get_markdown_section(text, "## Notes created/expanded")

    # Before 6am, also accept yesterday's summary (working past midnight).
    if today.hour < 6:
        yesterday_str = (today - timedelta(days=1)).strftime("%Y-%m-%d")
        yesterday_note = os.path.join(
            project_dir, "investing", "Daily", f"{yesterday_str}.md"
        )
        if os.path.isfile(yesterday_note):
            ytext = read_note(yesterday_note)
            ysummary = get_markdown_section(ytext, "## Notes created/expanded")
            if ysummary.strip():
                summary = (summary + "\n" + ysummary) if summary else ysummary

    note_filename = os.path.basename(daily_note)
    if not summary.strip():
        sys.stderr.write(
            f"DAILY NOTE GATE ({note_filename}): Edit log has entries "
            f"({', '.join(entities)}) but no '## Notes created/expanded' section. "
            "Update the daily note with a summary of what was created/changed before finishing.\n"
        )
        return 2

    missing = []
    for entity in entities:
        found = re.search(re.escape(entity), summary, re.IGNORECASE) is not None
        if not found:
            repaired = repair_double_utf8(entity)
            if repaired != entity:
                found = re.search(re.escape(repaired), summary, re.IGNORECASE) is not None
        if not found:
            missing.append(f"[[{repair_double_utf8(entity)}]]")

    if missing:
        sys.stderr.write(
            f"DAILY NOTE GATE ({note_filename}): These entities were edited but not "
            f"mentioned in '## Notes created/expanded': {' '.join(missing)}. "
            "Add a summary line for each before finishing.\n"
        )
        return 2

    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:
        sys.stderr.write(f"Stop hook failed: {e}\n")
        sys.exit(1)
