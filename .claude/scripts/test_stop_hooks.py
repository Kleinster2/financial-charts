#!/usr/bin/env python3
"""Black-box tests for the Stop hooks.

Runs each script as a subprocess against synthetic vaults under a temp dir,
asserts on (exit_code, stderr_substring).

Usage: python .claude/scripts/test_stop_hooks.py
"""

import os
import subprocess
import sys
import tempfile
from datetime import datetime, timedelta
from pathlib import Path

HERE = Path(__file__).resolve().parent
DAILY = HERE / "check_daily_summary.py"
TECH = HERE / "check_tech_changelog.py"


def run(script, env_overrides):
    env = os.environ.copy()
    env.update(env_overrides)
    return subprocess.run(
        [sys.executable, str(script)],
        capture_output=True, text=True, timeout=15, env=env,
    )


def write_daily(project_dir, date_str, body):
    daily = Path(project_dir) / "investing" / "Daily" / f"{date_str}.md"
    daily.parent.mkdir(parents=True, exist_ok=True)
    daily.write_text(body, encoding="utf-8")
    return daily


def hhmm(offset_minutes):
    t = datetime.now() + timedelta(minutes=offset_minutes)
    return t.strftime("%H:%M")


# ----- daily-summary tests -----

def test_daily_no_note():
    with tempfile.TemporaryDirectory() as d:
        r = run(DAILY, {"CLAUDE_PROJECT_DIR": d})
    assert r.returncode == 0, f"expected 0, got {r.returncode}: {r.stderr}"


def test_daily_no_edit_log():
    with tempfile.TemporaryDirectory() as d:
        write_daily(d, datetime.now().strftime("%Y-%m-%d"), "#daily\n")
        r = run(DAILY, {"CLAUDE_PROJECT_DIR": d})
    assert r.returncode == 0, f"expected 0, got {r.returncode}: {r.stderr}"


def test_daily_old_entries_only():
    with tempfile.TemporaryDirectory() as d:
        body = (
            "#daily\n\n## Edit log\n\n"
            f"- {hhmm(-300)} - edited [[Old Entity]] (Actors)\n"
        )
        write_daily(d, datetime.now().strftime("%Y-%m-%d"), body)
        r = run(DAILY, {"CLAUDE_PROJECT_DIR": d})
    assert r.returncode == 0, f"expected 0, got {r.returncode}: {r.stderr}"


def test_daily_recent_no_summary_section():
    with tempfile.TemporaryDirectory() as d:
        body = (
            "#daily\n\n## Edit log\n\n"
            f"- {hhmm(-30)} - edited [[Acme Corp]] (Actors)\n"
        )
        write_daily(d, datetime.now().strftime("%Y-%m-%d"), body)
        r = run(DAILY, {"CLAUDE_PROJECT_DIR": d})
    assert r.returncode == 2, f"expected 2, got {r.returncode}: {r.stderr}"
    assert "DAILY NOTE GATE" in r.stderr
    assert "Acme Corp" in r.stderr
    assert "no '## Notes created/expanded'" in r.stderr


def test_daily_recent_missing_entity_in_summary():
    with tempfile.TemporaryDirectory() as d:
        body = (
            "#daily\n\n## Notes created/expanded\n\n"
            "- Updated [[Other Entity]] with new data.\n\n"
            "## Edit log\n\n"
            f"- {hhmm(-30)} - edited [[Acme Corp]] (Actors)\n"
            f"- {hhmm(-20)} - edited [[Other Entity]] (Concepts)\n"
        )
        write_daily(d, datetime.now().strftime("%Y-%m-%d"), body)
        r = run(DAILY, {"CLAUDE_PROJECT_DIR": d})
    assert r.returncode == 2, f"expected 2, got {r.returncode}: {r.stderr}"
    assert "DAILY NOTE GATE" in r.stderr
    assert "[[Acme Corp]]" in r.stderr
    assert "Other Entity" not in r.stderr.split("not mentioned")[1]


def test_daily_all_entities_summarized():
    with tempfile.TemporaryDirectory() as d:
        body = (
            "#daily\n\n## Notes created/expanded\n\n"
            "- Updated [[Acme Corp]] and [[Other Entity]].\n\n"
            "## Edit log\n\n"
            f"- {hhmm(-30)} - edited [[Acme Corp]] (Actors)\n"
            f"- {hhmm(-20)} - edited [[Other Entity]] (Concepts)\n"
        )
        write_daily(d, datetime.now().strftime("%Y-%m-%d"), body)
        r = run(DAILY, {"CLAUDE_PROJECT_DIR": d})
    assert r.returncode == 0, f"expected 0, got {r.returncode}: {r.stderr}"


def test_daily_unicode_entity():
    with tempfile.TemporaryDirectory() as d:
        body = (
            "#daily\n\n## Notes created/expanded\n\n"
            "- Updated [[Société Générale]].\n\n"
            "## Edit log\n\n"
            f"- {hhmm(-30)} - edited [[Société Générale]] (Actors)\n"
        )
        write_daily(d, datetime.now().strftime("%Y-%m-%d"), body)
        r = run(DAILY, {"CLAUDE_PROJECT_DIR": d})
    assert r.returncode == 0, f"expected 0, got {r.returncode}: {r.stderr}"


# ----- tech-changelog tests -----

def init_repo(path):
    subprocess.run(["git", "init", "-q", str(path)], check=True)
    subprocess.run(
        ["git", "-C", str(path), "config", "user.email", "test@example.com"], check=True
    )
    subprocess.run(
        ["git", "-C", str(path), "config", "user.name", "test"], check=True
    )


def commit_initial(path):
    subprocess.run(["git", "-C", str(path), "add", "-A"], check=True)
    subprocess.run(
        ["git", "-C", str(path), "commit", "-q", "-m", "init", "--allow-empty"],
        check=True,
    )


def test_tech_no_vault():
    with tempfile.TemporaryDirectory() as d:
        missing = Path(d) / "nope"
        r = run(TECH, {"TECH_VAULT_PATH": str(missing)})
    assert r.returncode == 0, f"expected 0, got {r.returncode}: {r.stderr}"


def test_tech_clean_repo():
    with tempfile.TemporaryDirectory() as d:
        vault = Path(d) / "vault"
        vault.mkdir()
        init_repo(vault)
        (vault / "changelog.md").write_text("# changelog\n", encoding="utf-8")
        commit_initial(vault)
        r = run(TECH, {"TECH_VAULT_PATH": str(vault)})
    assert r.returncode == 0, f"expected 0, got {r.returncode}: {r.stderr}"


def test_tech_only_changelog_changed():
    with tempfile.TemporaryDirectory() as d:
        vault = Path(d) / "vault"
        vault.mkdir()
        init_repo(vault)
        (vault / "changelog.md").write_text("# changelog\n", encoding="utf-8")
        (vault / "Note.md").write_text("body\n", encoding="utf-8")
        commit_initial(vault)
        # Modify only changelog itself — should pass
        (vault / "changelog.md").write_text("# changelog\n\n2026-04-27\n", encoding="utf-8")
        r = run(TECH, {"TECH_VAULT_PATH": str(vault)})
    assert r.returncode == 0, f"expected 0, got {r.returncode}: {r.stderr}"


def test_tech_note_changed_changelog_has_date():
    with tempfile.TemporaryDirectory() as d:
        vault = Path(d) / "vault"
        vault.mkdir()
        init_repo(vault)
        (vault / "changelog.md").write_text("# changelog\n", encoding="utf-8")
        (vault / "Note.md").write_text("body\n", encoding="utf-8")
        commit_initial(vault)
        # Modify the note; ensure today's date appears in changelog
        (vault / "Note.md").write_text("body\nupdated\n", encoding="utf-8")
        today = datetime.now().strftime("%Y-%m-%d")
        (vault / "changelog.md").write_text(f"# changelog\n\n{today}\n- updated Note\n", encoding="utf-8")
        r = run(TECH, {"TECH_VAULT_PATH": str(vault)})
    assert r.returncode == 0, f"expected 0, got {r.returncode}: {r.stderr}"


def test_tech_note_changed_no_changelog_entry():
    with tempfile.TemporaryDirectory() as d:
        vault = Path(d) / "vault"
        vault.mkdir()
        init_repo(vault)
        (vault / "changelog.md").write_text("# changelog\n\n2025-01-01\n", encoding="utf-8")
        (vault / "Note.md").write_text("body\n", encoding="utf-8")
        commit_initial(vault)
        (vault / "Note.md").write_text("body\nupdated\n", encoding="utf-8")
        r = run(TECH, {"TECH_VAULT_PATH": str(vault)})
    assert r.returncode == 2, f"expected 2, got {r.returncode}: {r.stderr}"
    assert "TECH VAULT GATE" in r.stderr
    assert "Note" in r.stderr


def test_tech_missing_changelog_file():
    with tempfile.TemporaryDirectory() as d:
        vault = Path(d) / "vault"
        vault.mkdir()
        init_repo(vault)
        (vault / "Note.md").write_text("body\n", encoding="utf-8")
        commit_initial(vault)
        (vault / "Note.md").write_text("body\nupdated\n", encoding="utf-8")
        r = run(TECH, {"TECH_VAULT_PATH": str(vault)})
    assert r.returncode == 2, f"expected 2, got {r.returncode}: {r.stderr}"
    assert "changelog.md is missing" in r.stderr


# ----- runner -----

def main():
    tests = [
        ("daily/no_note", test_daily_no_note),
        ("daily/no_edit_log", test_daily_no_edit_log),
        ("daily/old_entries_only", test_daily_old_entries_only),
        ("daily/recent_no_summary_section", test_daily_recent_no_summary_section),
        ("daily/recent_missing_entity", test_daily_recent_missing_entity_in_summary),
        ("daily/all_summarized", test_daily_all_entities_summarized),
        ("daily/unicode_entity", test_daily_unicode_entity),
        ("tech/no_vault", test_tech_no_vault),
        ("tech/clean_repo", test_tech_clean_repo),
        ("tech/only_changelog_changed", test_tech_only_changelog_changed),
        ("tech/note_changed_with_date", test_tech_note_changed_changelog_has_date),
        ("tech/note_changed_no_entry", test_tech_note_changed_no_changelog_entry),
        ("tech/missing_changelog", test_tech_missing_changelog_file),
    ]
    passed, failed = 0, []
    for name, fn in tests:
        try:
            fn()
            print(f"  PASS  {name}")
            passed += 1
        except AssertionError as e:
            print(f"  FAIL  {name}: {e}")
            failed.append(name)
        except Exception as e:
            print(f"  ERR   {name}: {type(e).__name__}: {e}")
            failed.append(name)
    print(f"\n{passed}/{len(tests)} passed")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
