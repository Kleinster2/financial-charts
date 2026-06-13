#!/usr/bin/env python3
"""Stop hook: ensure the entities THIS session edited today also appear in the
daily note's '## Notes created/expanded' summary section.

Session-aware: the PostToolUse hook (quick_compliance_check.py) records each
vault-note edit into a per-session sidecar under .claude/.session_edits/. This
hook reads only the stopping session's sidecar, so a concurrent session's
in-progress edits no longer deadlock whichever session stops first. When no
session_id is available (manual run / older harness) it falls back to the legacy
behavior: every edit-log entry from the last 120 minutes.

The pre-commit hook remains the hard enforcement (it blocks committing staged
vault notes that aren't logged); this gate is the earlier, session-scoped nudge.

Exit codes:
  0  pass (no daily note, this session edited nothing, or all entities summarized)
  2  block — this session's edits lack a matching summary line
  1  unexpected error
"""

import json
import os
import re
import sys
import unicodedata
from datetime import datetime, timedelta

SESSION_EDITS_SUBDIR = os.path.join(".claude", ".session_edits")


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


def get_session_id():
    """Read session_id from the Stop-hook JSON payload on stdin (UTF-8).

    Returns "" when unavailable (manual run / older harness), which the caller
    treats as a signal to fall back to the legacy edit-log scan.
    """
    try:
        raw = sys.stdin.buffer.read()
        if not raw:
            return ""
        return json.loads(raw.decode("utf-8")).get("session_id", "") or ""
    except Exception:
        return ""


def safe_session_id(session_id):
    return re.sub(r"[^A-Za-z0-9_-]", "", session_id or "")[:64]


def session_edits_path(project_dir, today_str, session_id):
    return os.path.join(
        project_dir, SESSION_EDITS_SUBDIR, f"{today_str}_{safe_session_id(session_id)}.txt"
    )


def read_session_entities(project_dir, today_str, session_id):
    """Entities this session edited today, from its sidecar.

    None  -> no usable session_id; caller falls back to the legacy edit-log scan
    []    -> session known but made no tracked vault-note edits today (pass)
    [...] -> the entities to verify against the summary
    """
    if not safe_session_id(session_id):
        return None
    path = session_edits_path(project_dir, today_str, session_id)
    if not os.path.isfile(path):
        return []
    try:
        with open(path, "r", encoding="utf-8") as f:
            return [unicodedata.normalize("NFC", ln.strip()) for ln in f if ln.strip()]
    except Exception:
        return []


def legacy_recent_entities(text, today):
    """Original behavior: entities from edit-log entries in the last 120 minutes."""
    edit_log = get_markdown_section(text, "## Edit log")
    if not edit_log.strip():
        return []
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
    return recent


def main():
    today = datetime.now()
    today_str = today.strftime("%Y-%m-%d")
    project_dir = get_project_dir()
    session_id = get_session_id()

    daily_note = os.path.join(project_dir, "investing", "Daily", f"{today_str}.md")
    if not os.path.isfile(daily_note):
        return 0

    text = read_note(daily_note)

    session_entities = read_session_entities(project_dir, today_str, session_id)
    if session_entities is None:
        # No session id (manual run / older harness) -> legacy edit-log scan.
        entities = sorted(set(legacy_recent_entities(text, today)))
    else:
        # Session-aware: only this session's own vault-note edits.
        entities = sorted(set(session_entities))

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
