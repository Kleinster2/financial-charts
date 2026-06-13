#!/usr/bin/env python3
"""PostToolUse hook: consolidated daily-note logging + actor compliance check.

Replaces check-daily-note.ps1 and check-note-compliance.ps1.
Reads hook payload from stdin, extracts file_path, then:
  1. Logs the edit to today's daily note (if vault .md file)
  2. Runs note compliance on actor files (advisory only)

Always exits 0 — never blocks edits.
"""

import json
import os
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path


def read_hook_payload():
    """Parse the PostToolUse JSON payload from stdin.

    Read raw bytes and decode UTF-8 explicitly. On Windows, text-mode
    sys.stdin defaults to cp1252, which mangles multi-byte UTF-8 paths
    (e.g. CJK note names like 中特估) into mojibake before they ever reach
    the edit log. The harness always sends UTF-8.
    """
    try:
        raw = sys.stdin.buffer.read()
        return json.loads(raw.decode("utf-8"))
    except Exception:
        return {}


SESSION_EDITS_SUBDIR = os.path.join(".claude", ".session_edits")


def record_session_edit(note_name, session_id, project_dir):
    """Record this session's vault-note edit in a per-session, per-day sidecar.

    The Stop-hook gate (check_daily_summary.py) reads only the stopping
    session's sidecar, so a concurrent session's in-progress edits no longer
    deadlock whichever session stops first. No session_id -> skip (the Stop
    hook then falls back to its legacy edit-log scan).
    """
    safe_sid = re.sub(r"[^A-Za-z0-9_-]", "", session_id or "")[:64]
    if not safe_sid:
        return
    today = datetime.now().strftime("%Y-%m-%d")
    sess_dir = os.path.join(project_dir, SESSION_EDITS_SUBDIR)
    try:
        os.makedirs(sess_dir, exist_ok=True)
        # Opportunistic cleanup: drop sidecars from previous days.
        for fn in os.listdir(sess_dir):
            if fn.endswith(".txt") and not fn.startswith(f"{today}_"):
                try:
                    os.remove(os.path.join(sess_dir, fn))
                except OSError:
                    pass
        path = os.path.join(sess_dir, f"{today}_{safe_sid}.txt")
        existing = set()
        if os.path.isfile(path):
            with open(path, "r", encoding="utf-8") as f:
                existing = {ln.strip() for ln in f if ln.strip()}
        if note_name not in existing:
            with open(path, "a", encoding="utf-8") as f:
                f.write(note_name + "\n")
    except Exception:
        pass


def normalize_path(p):
    return p.replace("\\", "/")


def get_project_dir():
    d = os.environ.get("CLAUDE_PROJECT_DIR", "")
    if d:
        return normalize_path(d)
    return normalize_path(os.getcwd())


def get_markdown_section(text, heading):
    """Extract content under a markdown ## heading."""
    pattern = rf"(?ms)^{re.escape(heading)}\s*$\n?(.*?)(?=^## |\Z)"
    m = re.search(pattern, text)
    return m.group(1).strip() if m else ""


def log_to_daily_note(file_path, project_dir):
    """Log the edited file to today's daily note edit log."""
    today = datetime.now().strftime("%Y-%m-%d")

    # Skip if editing today's daily note itself
    if file_path.endswith(f"investing/Daily/{today}.md"):
        return

    daily_dir = os.path.join(project_dir, "investing", "Daily")
    os.makedirs(daily_dir, exist_ok=True)

    daily_note = os.path.join(daily_dir, f"{today}.md")
    if not os.path.exists(daily_note):
        with open(daily_note, "w", encoding="utf-8") as f:
            f.write("#daily\n\n")

    content = open(daily_note, "r", encoding="utf-8").read()

    # Ensure edit log section exists
    if not re.search(r"(?m)^## Edit log\s*$", content):
        if content and not content.endswith("\n"):
            content += "\n"
        content += "\n## Edit log\n\n"
        with open(daily_note, "w", encoding="utf-8") as f:
            f.write(content)
        content = open(daily_note, "r", encoding="utf-8").read()

    # Check if entity already logged
    note_name = Path(file_path).stem
    edit_log = get_markdown_section(content, "## Edit log")
    entity_token = f"[[{note_name}]]"
    if entity_token in edit_log:
        return

    # Determine subfolder
    m = re.search(r"investing/([^/]+)/", file_path)
    subfolder = m.group(1) if m else "Unknown"

    timestamp = datetime.now().strftime("%H:%M")
    entry = f"- {timestamp} - edited [[{note_name}]] ({subfolder})\n"
    with open(daily_note, "a", encoding="utf-8") as f:
        f.write(entry)

    print(f"Logged edit to [[{note_name}]] in daily note. Remember to expand the edit log into a proper summary section before finishing.")


def run_compliance_check(file_path, project_dir):
    """Run note compliance on actor files. Advisory only."""
    script = os.path.join(project_dir, "scripts", "check_note_compliance.py")
    if not os.path.exists(script):
        return

    abs_path = file_path if os.path.isabs(file_path) else os.path.join(project_dir, file_path)
    if not os.path.exists(abs_path):
        return

    try:
        result = subprocess.run(
            [sys.executable, script, abs_path],
            capture_output=True, text=True, timeout=10
        )
        if result.returncode != 0:
            errors = [
                line.strip() for line in result.stdout.splitlines()
                if line.strip().startswith("ERROR")
            ]
            if errors:
                note_name = Path(file_path).stem
                error_list = "\n  ".join(errors)
                print(f"COMPLIANCE ({note_name}.md):\n  {error_list}", file=sys.stderr)
    except Exception:
        pass


def main():
    # Windows defaults stdout/stderr to cp1252; printing a CJK note name
    # (中特估) would raise UnicodeEncodeError. Reconfigure to UTF-8 so the
    # hook's own status prints never crash on non-ASCII note names.
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8")
        except Exception:
            pass

    payload = read_hook_payload()
    file_path = payload.get("tool_input", {}).get("file_path", "")
    session_id = payload.get("session_id", "")
    if not file_path:
        return

    file_path = normalize_path(file_path)

    # Only process vault markdown files
    if "investing/" not in file_path or not file_path.endswith(".md"):
        return

    # Reports are disposable cross-vault syntheses — handled by /report skill,
    # not entity edits. Skip auto edit-log + compliance.
    if "investing/Reports/" in file_path:
        return

    project_dir = get_project_dir()

    # Don't treat edits to today's daily note itself as a logged entity.
    today = datetime.now().strftime("%Y-%m-%d")
    if file_path.endswith(f"investing/Daily/{today}.md"):
        return

    note_name = Path(file_path).stem

    # 0. Record this session's edit so the Stop-hook gate can scope to it.
    record_session_edit(note_name, session_id, project_dir)

    # 1. Log to daily note
    try:
        log_to_daily_note(file_path, project_dir)
    except Exception as e:
        print(f"Daily note logging failed: {e}", file=sys.stderr)

    # 2. Compliance check (actors only)
    if re.search(r"investing/Actors/[^/]+\.md$", file_path):
        run_compliance_check(file_path, project_dir)


if __name__ == "__main__":
    main()
