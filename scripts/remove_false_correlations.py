#!/usr/bin/env python
"""Remove incorrectly inserted ## Sector correlation sections from false-match notes."""

import re
from pathlib import Path

ACTORS_DIR = Path(__file__).parent.parent / 'investing' / 'Actors'

# Notes where alias collided with wrong ticker
FALSE_MATCHES = [
    'Air India',
    'Balyasny',
    'British Airways',
    'China Media Group',
    'Maison Margiela',
    'Midjourney',
    'Moelis',
    'Neuberger Berman',
    'New Balance',
    'Oman Air',
    'Sapir Organization',
    'Supermercados Dia',
    'Tenneco',
    'Vonage',
    'Suzhou TFC Optical Communication',
    'Nu Holdings',  # already had correct section as Nubank
]


def remove_correlation_section(filepath):
    """Remove the ## Sector correlation section from a note."""
    text = filepath.read_text(encoding='utf-8')
    if '## Sector correlation' not in text:
        return False

    # Find the section and its surrounding dividers
    # Pattern: ---\n\n## Sector correlation\n...\n\n---
    pattern = r'\n---\n\n## Sector correlation\n.*?(?=\n---\n)'
    new_text = re.sub(pattern, '', text, count=1, flags=re.DOTALL)

    if new_text != text:
        filepath.write_text(new_text, encoding='utf-8')
        return True
    return False


if __name__ == '__main__':
    for name in FALSE_MATCHES:
        fp = ACTORS_DIR / f'{name}.md'
        if fp.exists():
            if remove_correlation_section(fp):
                print(f'  Removed: {name}')
            else:
                print(f'  No section: {name}')
        else:
            print(f'  Not found: {name}')
