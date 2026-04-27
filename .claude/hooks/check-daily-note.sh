#!/bin/bash
#
# PostToolUse hook: after any Edit/Write to an investing/ note,
# appends a timestamped log entry to today's daily note under
# a "## Edit log" section. This creates an automatic record of
# every entity touched, which Claude then expands into a proper summary.
#
# - Skips non-investing files and non-.md files
# - Skips edits to the daily note itself (avoid recursion)
# - Creates the daily note if it doesn't exist
# - Deduplicates: won't log the same entity twice

INPUT=$(cat)
FILE_PATH=$(echo "$INPUT" | python -c "import sys,json; print(json.load(sys.stdin).get('tool_input',{}).get('file_path',''))" 2>/dev/null)

# Normalize path separators
FILE_PATH=$(echo "$FILE_PATH" | sed 's|\\|/|g')

# Only track edits inside investing/
if [[ ! "$FILE_PATH" =~ investing/ ]]; then
  exit 0
fi

# Only track .md files
if [[ ! "$FILE_PATH" =~ \.md$ ]]; then
  exit 0
fi

TODAY=$(date +%Y-%m-%d)

# Skip edits to the daily note itself
if [[ "$FILE_PATH" =~ investing/Daily/$TODAY\.md ]]; then
  exit 0
fi

DAILY_NOTE="$(echo "$CLAUDE_PROJECT_DIR" | sed 's|\\|/|g')/investing/Daily/$TODAY.md"

# Extract note name and folder
NOTE_NAME=$(basename "$FILE_PATH" .md)

# Determine the subfolder (Actors, Concepts, Events, etc.)
SUBFOLDER=$(echo "$FILE_PATH" | sed -n 's|.*investing/\([^/]*\)/.*|\1|p')

# Create daily note if it doesn't exist
if [ ! -f "$DAILY_NOTE" ]; then
  echo -e "#daily\n" > "$DAILY_NOTE"
fi

# Check if edit log section exists; add it if not
if ! grep -q "^## Edit log" "$DAILY_NOTE" 2>/dev/null; then
  echo -e "\n## Edit log\n" >> "$DAILY_NOTE"
fi

# Deduplicate: skip if this entity is already in the edit log
if grep -q "\[\[$NOTE_NAME\]\]" "$DAILY_NOTE" 2>/dev/null; then
  # Entity already mentioned — check if it's in the edit log specifically
  # Use a simple check: if the edit log section contains the entity, skip
  if sed -n '/^## Edit log/,/^## /p' "$DAILY_NOTE" | grep -q "\[\[$NOTE_NAME\]\]" 2>/dev/null; then
    exit 0
  fi
fi

# Append log entry
TIMESTAMP=$(date +%H:%M)
echo "- $TIMESTAMP — edited [[$NOTE_NAME]] ($SUBFOLDER)" >> "$DAILY_NOTE"

# Remind Claude via stdout that it needs to write a proper summary later
echo "Logged edit to [[$NOTE_NAME]] in daily note. Remember to expand the edit log into a proper summary section before committing."

exit 0
