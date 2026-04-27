#!/bin/bash
#
# Stop hook: blocks Claude from finishing if the daily note has
# edit log entries that aren't covered in a summary section.
#
# Flow:
#   1. PostToolUse hook logs each investing/ edit to "## Edit log"
#   2. Claude works freely — no interruptions
#   3. When Claude tries to stop, THIS hook checks:
#      - Does the edit log have entities?
#      - Does "## Notes created/expanded" exist and mention them?
#   4. If entities are missing from the summary, exit 2 → Claude is
#      told to update the daily note before finishing
#
# Skips cleanly if:
#   - No daily note exists
#   - No edit log section
#   - No entities in edit log
#   - All entities are covered in the summary

TODAY=$(date +%Y-%m-%d)
DAILY_NOTE="$(echo "$CLAUDE_PROJECT_DIR" | sed 's|\\|/|g')/investing/Daily/$TODAY.md"

# No daily note — nothing to check
if [ ! -f "$DAILY_NOTE" ]; then
  exit 0
fi

# No edit log section — nothing to check
if ! grep -q "^## Edit log" "$DAILY_NOTE" 2>/dev/null; then
  exit 0
fi

# Extract entity names from edit log section
# Grab everything from "## Edit log" to EOF, then extract [[entities]]
# (entities only appear in bullet lines, not in other ## headers, so this is safe)
EDIT_LOG_SECTION=$(sed -n '/^## Edit log/,$p' "$DAILY_NOTE" || true)

ENTITIES=$(echo "$EDIT_LOG_SECTION" | grep -o '\[\[[^]]*\]\]' | sed 's/\[\[//;s/\]\]//' | sort -u || true)

# No entities logged — nothing to check
if [ -z "$ENTITIES" ]; then
  exit 0
fi

# Check if summary section exists
if ! grep -q "^## Notes created/expanded" "$DAILY_NOTE" 2>/dev/null; then
  ENTITY_LIST=$(echo "$ENTITIES" | tr '\n' ', ' | sed 's/,$//')
  echo "DAILY NOTE GATE: Edit log has entries ($ENTITY_LIST) but no '## Notes created/expanded' section. Update the daily note with a summary of what was created/changed before finishing." >&2
  exit 2
fi

# Extract summary section
SUMMARY_SECTION=$(sed -n '/^## Notes created\/expanded/,/^## /p' "$DAILY_NOTE" || true)

# Check each entity appears in summary
MISSING=""
while IFS= read -r entity; do
  [ -z "$entity" ] && continue
  if ! echo "$SUMMARY_SECTION" | grep -qi "$entity"; then
    MISSING="$MISSING [[$entity]]"
  fi
done <<< "$ENTITIES"

if [ -n "$MISSING" ]; then
  echo "DAILY NOTE GATE: These entities were edited but not mentioned in '## Notes created/expanded':$MISSING. Add a summary line for each before finishing." >&2
  exit 2
fi

exit 0
