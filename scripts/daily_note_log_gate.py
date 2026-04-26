#!/usr/bin/env python3
"""Ensure staged vault notes are linked from the session daily note."""

from __future__ import annotations

import argparse
from datetime import date, datetime, timedelta
import os
from pathlib import Path
import re
import subprocess
import sys
import unicodedata


REPO_ROOT = Path(__file__).resolve().parent.parent
SKIP_DIRS = {"Daily", "Meta", "Reports", "Newsletter", ".obsidian"}
WIKILINK_RE = re.compile(r"\[\[([^\]\n]+)\]\]")


def run_git(args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )


def normalized_name(value: str) -> str:
    return unicodedata.normalize("NFC", value).casefold().strip()


def note_key_from_path(path: Path) -> str:
    return normalized_name(path.stem)


def wikilink_keys(content: str) -> set[str]:
    keys = set()
    for match in WIKILINK_RE.finditer(content):
        target = match.group(1).split("|", 1)[0].split("#", 1)[0].strip()
        if not target:
            continue
        target = target.replace("\\", "/")
        stem = target.rsplit("/", 1)[-1]
        if stem.endswith(".md"):
            stem = stem[:-3]
        if stem:
            keys.add(normalized_name(stem))
    return keys


def staged_paths() -> list[tuple[str, Path]]:
    result = run_git(["diff", "--cached", "--name-status", "-z"])
    if result.returncode != 0:
        print(result.stderr.strip(), file=sys.stderr)
        raise SystemExit(result.returncode)

    parts = result.stdout.split("\0")
    paths: list[tuple[str, Path]] = []
    i = 0
    while i < len(parts):
        status = parts[i]
        i += 1
        if not status:
            continue

        code = status[0]
        if code in {"R", "C"}:
            if i + 1 >= len(parts):
                break
            _old_path = parts[i]
            new_path = parts[i + 1]
            i += 2
            paths.append((code, Path(new_path)))
            continue

        if i >= len(parts):
            break
        path = parts[i]
        i += 1
        paths.append((code, Path(path)))

    return paths


def is_reportable_note(status: str, path: Path) -> bool:
    if status == "D":
        return False

    parts = path.parts
    if len(parts) < 2 or parts[0] != "investing":
        return False
    if path.suffix.lower() != ".md":
        return False
    if len(parts) > 1 and parts[1] in SKIP_DIRS:
        return False
    return True


def read_index_file(path: Path) -> str | None:
    result = run_git(["show", f":{path.as_posix()}"])
    if result.returncode != 0:
        return None
    return result.stdout


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Check that staged investing vault notes are linked in today's "
            "daily note."
        )
    )
    parser.add_argument(
        "--staged",
        action="store_true",
        help="Check staged git changes. This is the mode used by the hook.",
    )
    parser.add_argument(
        "--date",
        default=os.environ.get("DAILY_NOTE_DATE") or date.today().strftime("%Y-%m-%d"),
        help="Daily note date to check, YYYY-MM-DD. Defaults to today.",
    )
    parser.add_argument(
        "--early-hour",
        type=int,
        default=6,
        help=(
            "Before this hour, also accept yesterday's daily note. "
            "Use 0 to disable. Defaults to 6."
        ),
    )
    return parser.parse_args()


def daily_paths(date_str: str, early_hour: int) -> list[Path]:
    dates = [date_str]
    if early_hour > 0 and datetime.now().hour < early_hour:
        try:
            parsed = datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            return [Path("investing") / "Daily" / f"{date_str}.md"]
        dates.append((parsed - timedelta(days=1)).strftime("%Y-%m-%d"))

    return [Path("investing") / "Daily" / f"{value}.md" for value in dates]


def main() -> int:
    args = parse_args()
    if not args.staged:
        print("Nothing to check: pass --staged to inspect staged note changes.")
        return 0

    touched = [
        path
        for status, path in staged_paths()
        if is_reportable_note(status, path)
    ]
    if not touched:
        print("No staged investing notes require daily-note reporting.")
        return 0

    daily_contents = []
    for path in daily_paths(args.date, args.early_hour):
        content = read_index_file(path)
        if content is not None:
            daily_contents.append((path, content))

    if not daily_contents:
        checked_paths = ", ".join(
            path.as_posix() for path in daily_paths(args.date, args.early_hour)
        )
        print(
            "Daily note log check failed: none of these daily notes are staged "
            f"or tracked: {checked_paths}.",
            file=sys.stderr,
        )
        print("Add today's daily note with links for:", file=sys.stderr)
        for path in touched:
            print(f"  - [[{path.stem}]] ({path.as_posix()})", file=sys.stderr)
        return 1

    linked = set()
    for _path, content in daily_contents:
        linked.update(wikilink_keys(content))

    missing = [path for path in touched if note_key_from_path(path) not in linked]

    if missing:
        checked_paths = ", ".join(path.as_posix() for path, _content in daily_contents)
        print(
            "Daily note log check failed: checked daily note(s) do not link "
            f"these staged notes: {checked_paths}",
            file=sys.stderr,
        )
        for path in missing:
            print(f"  - [[{path.stem}]] ({path.as_posix()})", file=sys.stderr)
        print(
            "Add each note under ## Notes created/expanded or ## Edit log, "
            "then stage the daily note.",
            file=sys.stderr,
        )
        return 1

    checked_paths = ", ".join(path.as_posix() for path, _content in daily_contents)
    print(
        f"Daily note log check passed: {len(touched)} staged note(s) linked in "
        f"{checked_paths}."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
