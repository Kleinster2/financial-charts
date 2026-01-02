import os, re, yaml
from collections import defaultdict

os.chdir('investing')

all_notes = []
for root, dirs, files in os.walk('.'):
    dirs[:] = [d for d in dirs if not d.startswith('.')]
    for f in files:
        if f.endswith('.md'):
            all_notes.append((f[:-3], os.path.join(root, f)))

file_names = {name.lower(): name for name, path in all_notes}
aliases = {}

for name, path in all_notes:
    try:
        content = open(path, 'r', encoding='utf-8').read()
        if content.startswith('---'):
            end = content.find('---', 3)
            if end > 0:
                fm = yaml.safe_load(content[3:end])
                if fm and 'aliases' in fm and fm['aliases']:
                    for alias in fm['aliases']:
                        aliases[alias.lower()] = name
    except: pass

link_pattern = re.compile(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]')
outgoing = defaultdict(set)
incoming = defaultdict(set)

for name, path in all_notes:
    try:
        content = open(path, 'r', encoding='utf-8').read()
        for match in link_pattern.findall(content):
            target = match.strip().lower()
            if target in file_names:
                resolved = file_names[target]
            elif target in aliases:
                resolved = aliases[target]
            else:
                continue
            if resolved != name:
                outgoing[name].add(resolved)
                incoming[resolved].add(name)
    except: pass

total = len(all_notes)
total_links = sum(len(v) for v in outgoing.values())
notes_with_out = sum(1 for n in outgoing if outgoing[n])
notes_with_in = sum(1 for n in incoming if incoming[n])
islands = [n for n, _ in all_notes if n not in incoming and n not in outgoing]

print('=== GRAPH CONNECTIVITY ===')
print()
print(f'Total links:        {total_links}')
print(f'Avg links/note:     {total_links/total:.1f}')
print(f'Notes with links:   {notes_with_out} ({100*notes_with_out/total:.0f}%)')
print(f'Notes linked to:    {notes_with_in} ({100*notes_with_in/total:.0f}%)')
print(f'Orphan notes:       {len(islands)}')
print()

print('Most linked TO (hubs):')
for name, sources in sorted(incoming.items(), key=lambda x: -len(x[1]))[:10]:
    print(f'  {len(sources):3d}  {name}')
print()

print('Most links FROM (connectors):')
for name, targets in sorted(outgoing.items(), key=lambda x: -len(x[1]))[:10]:
    print(f'  {len(targets):3d}  {name}')

if islands:
    print()
    print(f'Orphan notes ({len(islands)}):')
    for name in sorted(islands)[:20]:
        print(f'  - {name}')
