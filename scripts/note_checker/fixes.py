"""Auto-fix and stub-creation helpers for NoteChecker (mixin).

Extracted from check_note_compliance.py: dead-link extraction, stub creation,
bold removal, and missing-wikilink auto-fix.
"""
import re
from pathlib import Path


class FixMixin:
    def get_dead_links(self, content: str) -> list[str]:
        """Get list of dead links from content."""
        wikilinks = re.findall(r'\[\[([^\]|\\]+)(?:\\?\|[^\]]+)?\]\]', content)
        dead = []
        seen = set()
        for link in wikilinks:
            if link.endswith(('.png', '.jpg', '.jpeg', '.gif', '.svg')):
                continue
            note_name = link.split("#", 1)[0]
            if not note_name:
                continue
            note_name = note_name.replace("\\", "/").split("/")[-1]
            if note_name in seen:
                continue
            seen.add(note_name)
            if note_name not in self.existing_notes and note_name not in self.known_aliases:
                dead.append(link)
        return dead

    def create_stub_note(self, name: str, source_filepath: Path) -> Path:
        """Create a minimal stub note for a dead link.

        Returns the path to the created stub.
        """
        # Determine folder based on name heuristics
        # People: names with spaces that look like "First Last"
        # Concepts: abstract terms, often lowercase-ish or descriptive
        # Default to Actors for companies/entities

        words = name.split()
        is_person = (
            len(words) == 2 and
            words[0][0].isupper() and
            words[1][0].isupper() and
            not any(corp in name for corp in ['Inc', 'Corp', 'Ltd', 'LLC', 'Co', 'Group', 'Fund', 'Capital', 'Partners', 'Ventures'])
        )

        is_concept = any(keyword in name.lower() for keyword in [
            'theory', 'effect', 'law', 'principle', 'strategy', 'model',
            'cycle', 'thesis', 'hypothesis', 'paradigm', 'framework',
            'advertising', 'market', 'sector', 'industry', 'trend',
            'shortage', 'crisis', 'boom', 'bubble', 'war', 'disruption'
        ])

        # Determine folder
        if is_concept:
            folder = self.vault_root / "Concepts"
            tags = "#concept"
        elif is_person:
            folder = self.vault_root / "Actors"
            tags = "#actor #person"
        else:
            folder = self.vault_root / "Actors"
            tags = "#actor"

        stub_path = folder / f"{name}.md"

        # Don't overwrite existing files
        if stub_path.exists():
            return stub_path

        # Create stub content
        if is_person:
            stub_content = f"""---
aliases: []
---
{tags}

**{name}** —

---

## Quick stats

| Metric | Value |
|--------|-------|
| Role | |

---

## Related

- [[{source_filepath.stem}]]

"""
        elif is_concept:
            stub_content = f"""---
aliases: []
---
{tags}

**{name}** —

---

## Related

- [[{source_filepath.stem}]]

"""
        else:
            stub_content = f"""---
aliases: []
---
{tags}

**{name}** —

---

## Quick stats

| Metric | Value |
|--------|-------|
| Ticker | |
| Market cap | |

---

## Related

- [[{source_filepath.stem}]]

"""
        stub_path.write_text(stub_content, encoding="utf-8")

        # Add to existing notes index
        self.existing_notes.add(name)

        return stub_path

    def fix_bold(self, filepath: Path) -> int:
        """Remove bold formatting (**text**) from a note, preserving the first instance
        (opening definition line convention). Returns count of fixes."""
        content = filepath.read_text(encoding="utf-8")

        # Preserve frontmatter
        frontmatter = ""
        body = content
        if content.startswith("---"):
            second_dash = content.find("---", 3)
            if second_dash != -1:
                frontmatter = content[:second_dash + 3]
                body = content[second_dash + 3:]

        # Count bold instances in body (outside code blocks)
        total = len(re.findall(r'\*\*(.+?)\*\*', body))

        # Only fix if there are bold instances beyond the first (definition line)
        if total > 1:
            # Replace **text** with text, but skip code blocks and preserve first instance
            parts = re.split(r'(```.*?```)', body, flags=re.DOTALL)
            new_parts = []
            first_seen = False
            for part in parts:
                if part.startswith('```'):
                    new_parts.append(part)  # Keep code blocks as-is
                else:
                    if not first_seen:
                        # Preserve first bold, replace the rest
                        state = {'seen': False}
                        def replace_after_first(match):
                            if not state['seen']:
                                state['seen'] = True
                                return match.group(0)  # Keep first bold
                            return match.group(1)  # Strip bold from rest
                        part = re.sub(r'\*\*(.+?)\*\*', replace_after_first, part)
                        first_seen = True
                    else:
                        part = re.sub(r'\*\*(.+?)\*\*', r'\1', part)
                    new_parts.append(part)
            body = ''.join(new_parts)
            filepath.write_text(frontmatter + body, encoding="utf-8")
            return total - 1  # Don't count the preserved first instance

        return 0

    def fix_missing_links(self, filepath: Path) -> list[str]:
        """Auto-fix missing wikilinks in a note. Returns list of fixed names."""
        content = filepath.read_text(encoding="utf-8")
        fixed = []

        # Get already-linked notes
        linked = set(re.findall(r'\[\[([^\]|\\]+)(?:\\?\|[^\]]+)?\]\]', content))

        # Check against content without links to avoid false positives
        content_without_links = re.sub(r'\[\[[^\]]+\]\]', '', content)

        # Sort by length descending so "AMD Ventures" matches before "AMD"
        for note_name in sorted(self.existing_notes, key=lambda n: (-len(n), n)):
            if note_name == filepath.stem:  # Skip self
                continue
            if note_name in linked:  # Already linked
                continue

            # Only proceed if term exists outside of wikilinks
            if not re.search(rf'\b{re.escape(note_name)}\b', content_without_links):
                continue

            # Replace only occurrences NOT inside wikilinks
            # Use a function to check each match
            def replace_if_not_in_link(match):
                start = match.start()
                # Check if this position is inside a wikilink
                before = content[:start]
                open_brackets = before.count('[[') - before.count(']]')
                if open_brackets > 0:
                    return match.group(0)  # Inside a link, don't replace
                return f'[[{note_name}]]'

            pattern = rf'\b{re.escape(note_name)}\b'
            new_content = re.sub(pattern, replace_if_not_in_link, content)
            if new_content != content:
                content = new_content
                fixed.append(note_name)

        if fixed:
            filepath.write_text(content, encoding="utf-8")

        return fixed
