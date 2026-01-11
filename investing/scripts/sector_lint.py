from pathlib import Path
import re
import sys

sector_dir = Path('Sectors')
if not sector_dir.exists():
    print('Sectors folder not found')
    sys.exit(1)

date_re = re.compile(r'^\*(Created|Updated)\s+\d{4}-\d{2}-\d{2}\*$')

issues_found = False

for path in sorted(sector_dir.glob('*.md')):
    text = path.read_text(encoding='utf-8', errors='ignore')
    lines = text.splitlines()
    issues = []

    # Frontmatter and aliases
    if not lines or lines[0].strip() != '---':
        issues.append('missing frontmatter')
        end = None
    else:
        end = None
        for i in range(1, len(lines)):
            if lines[i].strip() == '---':
                end = i
                break
        if end is None:
            issues.append('frontmatter not closed')
        else:
            has_aliases = any(l.strip().startswith('aliases:') for l in lines[1:end])
            if not has_aliases:
                issues.append('missing aliases')

    # Tag line
    start = (end + 1) if end is not None else 0
    tag_idx = None
    for i in range(start, len(lines)):
        if lines[i].strip():
            tag_idx = i
            break
    if tag_idx is None or '#sector' not in lines[tag_idx]:
        issues.append('missing #sector tag line')

    # H1 title
    has_h1 = False
    if tag_idx is not None:
        for i in range(tag_idx + 1, min(tag_idx + 15, len(lines))):
            if lines[i].startswith('# '):
                has_h1 = True
                break
    if not has_h1:
        issues.append('missing H1 title')

    # Sources section
    if '## Sources' not in text:
        issues.append('missing Sources section')

    # Created/Updated line
    if not any(date_re.match(l.strip()) for l in lines):
        issues.append('missing Created/Updated line')

    if issues:
        issues_found = True
        print(f'{path.as_posix()}: ' + '; '.join(issues))

if issues_found:
    sys.exit(1)
