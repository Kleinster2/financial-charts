#!/bin/bash
# Check for broken markdown links in documentation
# Returns non-zero exit code if broken links found

cd "$(dirname "$0")/.."

echo "Checking documentation links..."

BROKEN=0

# Directories to exclude from doc checks
EXCLUDE_DIRS="node_modules test-results playwright-report .sessions .kiro .git"

# Build find exclusion args
FIND_EXCLUDES=""
for dir in $EXCLUDE_DIRS; do
  FIND_EXCLUDES="$FIND_EXCLUDES -path ./$dir -prune -o"
done

# Find all markdown files to check (excluding noisy directories)
FILES="README.md $(find docs charting_sandbox scripts $FIND_EXCLUDES -name '*.md' -print 2>/dev/null)"

for file in $FILES; do
  [ -f "$file" ] || continue
  dir=$(dirname "$file")

  # Extract markdown links: [text](path.md) or [text](path.md#anchor)
  links=$(grep -oE '\[[^]]*\]\([^)]+\.md[^)]*\)' "$file" 2>/dev/null | \
    sed 's/.*](//' | sed 's/)$//' | sed 's/#.*//')

  for link in $links; do
    # Skip external links
    if [[ "$link" == http* ]]; then
      continue
    fi

    # Resolve link path
    if [[ "$link" == /* ]]; then
      # Repo-root relative (e.g., /docs/foo.md) - strip leading slash
      resolved="${link#/}"
    else
      # Relative to containing file's directory
      resolved="$dir/$link"
    fi

    # Normalize path (remove ./ and resolve ../)
    resolved=$(cd "$(dirname "$resolved")" 2>/dev/null && pwd)/$(basename "$resolved")
    resolved=${resolved#$(pwd)/}

    # Check if file exists
    if [ ! -f "$resolved" ]; then
      echo "BROKEN in $file: $link"
      BROKEN=1
    fi
  done
done

if [ $BROKEN -eq 1 ]; then
  echo ""
  echo "Found broken links!"
  exit 1
else
  echo "All documentation links valid."
  exit 0
fi
