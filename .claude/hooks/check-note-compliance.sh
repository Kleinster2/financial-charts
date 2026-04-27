#!/usr/bin/env bash
# PostToolUse hook: runs note compliance on edited actor files.
# Only fires for investing/Actors/*.md edits. Non-blocking (advisory only).

set -euo pipefail

INPUT=$(cat)
FILE_PATH=$(echo "$INPUT" | python -c "import sys,json; print(json.load(sys.stdin).get('tool_input',{}).get('file_path',''))" 2>/dev/null || true)

[ -z "$FILE_PATH" ] && exit 0

# Normalize path separators
FILE_PATH="${FILE_PATH//\\//}"

# Only run on investing/Actors/*.md
[[ "$FILE_PATH" =~ investing/Actors/[^/]+\.md$ ]] || exit 0

PROJECT_DIR="${CLAUDE_PROJECT_DIR:-$(pwd)}"

# Resolve absolute path
if [[ "$FILE_PATH" != /* ]]; then
  ABS_PATH="$PROJECT_DIR/$FILE_PATH"
else
  ABS_PATH="$FILE_PATH"
fi

[ -f "$ABS_PATH" ] || exit 0

SCRIPT="$PROJECT_DIR/scripts/check_note_compliance.py"
[ -f "$SCRIPT" ] || exit 0

# Run compliance, capture output
RESULT=$(python "$SCRIPT" "$ABS_PATH" 2>&1) || true

# Filter to ERROR lines only
ERRORS=$(echo "$RESULT" | grep -E '^\s*ERROR' || true)
if [ -n "$ERRORS" ]; then
  NOTE_NAME=$(basename "$FILE_PATH" .md)
  echo "COMPLIANCE ($NOTE_NAME.md):" >&2
  echo "$ERRORS" | sed 's/^/  /' >&2
fi

# Always exit 0 — advisory only
exit 0
