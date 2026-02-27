#!/usr/bin/env python3
"""Find actor notes missing synopsis (lightweight, no full compliance check)."""
import re
from pathlib import Path

vault = Path(__file__).parent.parent / "investing"

def has_tag(content, tag):
    return bool(re.search(rf'(?<!\w){re.escape(tag)}(?=\s|$)', content, re.MULTILINE))

def check_synopsis(filepath):
    content = filepath.read_text(encoding='utf-8')
    if not has_tag(content, '#actor'):
        return False
    
    # Get body after frontmatter
    body = content
    if content.startswith('---'):
        idx = content.find('---', 3)
        if idx != -1:
            body = content[idx + 3:]
    
    # Skip stubs
    non_empty = sum(1 for l in body.split('\n') if l.strip())
    if non_empty < 40:
        return False
    
    # Find definition line and check for synopsis after it
    lines = body.strip().split('\n')
    def_idx = None
    for i, line in enumerate(lines):
        s = line.strip()
        if not s:
            continue
        if s.startswith('#') and not s.startswith('##'):
            continue
        if s.startswith('**') or ' — ' in s or ' — ' in s:
            def_idx = i
            break
        break
    
    if def_idx is None:
        return False
    
    # Check for substantial text after def line before first heading/---
    synopsis = []
    for i in range(def_idx + 1, len(lines)):
        s = lines[i].strip()
        if s.startswith('##') or s == '---':
            break
        if s:
            synopsis.append(s)
    
    return sum(len(s) for s in synopsis) < 100

missing = []
for f in sorted(vault.glob('Actors/*.md')):
    try:
        if check_synopsis(f):
            missing.append(f.stem)
    except:
        pass

print(f'Total: {len(missing)}')
for name in missing:
    print(name)
