#!/bin/bash
# Check for broken markdown links in documentation
# Returns non-zero exit code if broken links found

cd "$(dirname "$0")/.."

echo "Checking documentation links..."

BROKEN=0

# Find all markdown files to check
FILES="README.md $(find docs charting_sandbox/README.md scripts/README.md -name '*.md' 2>/dev/null)"

for file in $FILES; do
  [ -f "$file" ] || continue
  dir=$(dirname "$file")

  # Extract markdown links: [text](path.md) or [text](path.md#anchor)
  grep -oE '\[[^]]*\]\([^)]+\.md[^)]*\)' "$file" 2>/dev/null | \
    sed 's/.*](//' | sed 's/)$//' | sed 's/#.*//' | \
    while read -r link; do
      # Skip external links
      if [[ "$link" == http* ]]; then
        continue
      fi

      # Resolve relative path from the file's directory
      if [[ "$link" == ./* ]] || [[ "$link" == ../* ]]; then
        resolved="$dir/$link"
      else
        resolved="$link"
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
