"""Categorize the unmatched-not-in-registry chart filenames.

Goal: confirm each category is correctly handled as static <img>.
Surface anything that doesn't fit a known static-screenshot pattern for review.
"""
from __future__ import annotations
import re
from pathlib import Path
import yaml

V = Path('investing')
EMBED = re.compile(r'!\[\[([^\]|]+\.png)(?:\|[^\]]*)?\]\]')


def classify_known(fn: str) -> bool:
    name = fn[:-4]
    if 'fundamentals' in name.lower():
        return True
    if '-vs-' in name:
        return True
    if '-price-chart' in name:
        return True
    if name.endswith('-ytd'):
        return True
    if re.search(r'-(\d+)(d|y)$', name, re.I):
        return True
    if name.endswith('-sankey') or name.endswith('-waterfall'):
        return True
    return False


def main() -> None:
    embeds: dict[str, list[str]] = {}
    for md in V.rglob('*.md'):
        if any(p in {'.obsidian', '.trash', 'attachments'} for p in md.parts):
            continue
        try:
            t = md.read_text(encoding='utf-8', errors='ignore')
        except Exception:
            continue
        for m in EMBED.finditer(t):
            raw = m.group(1).strip()
            fn = raw.replace('\\', '/').split('/')[-1]
            if fn.lower().endswith('.png'):
                embeds.setdefault(fn, []).append(str(md))

    fm = re.match(r'^---\n(.*?)\n---', (V / 'chart-registry.md').read_text(encoding='utf-8'), re.S)
    reg = yaml.safe_load(fm.group(1)).get('charts', {})

    cands = sorted([fn for fn in embeds if not classify_known(fn) and fn not in reg])
    print(f'Total unknown-not-in-registry: {len(cands)}\n')

    cats = {
        'employees-chart': lambda f: f.endswith('-employees-chart.png') or f.endswith('-employees.png'),
        'sankey-variant': lambda f: '-sankey' in f,
        'waterfall-variant': lambda f: 'waterfall' in f,
        'ft-source': lambda f: f.startswith('ft-') or '-ft-' in f or f.endswith('-ft.png'),
        'bloomberg-source': lambda f: 'bloomberg' in f,
        'quartr-source': lambda f: 'quartr' in f,
        'aurelion-source': lambda f: 'aurelion' in f,
        'wsj-source': lambda f: '-wsj' in f or 'wsj-' in f,
        'analyst-source': lambda f: '-analyst' in f,
        'documentation-example': lambda f: f == 'chart.png',
        'map/diagram/network': lambda f: any(s in f for s in ['-map', '-network', '-geography', '-diagram', 'value-chain']),
        'kalshi-polymarket': lambda f: 'kalshi' in f or 'polymarket' in f,
        'fed-fomc': lambda f: 'fomc' in f or 'fed-' in f,
    }
    classified: set[str] = set()
    for cat, test in cats.items():
        matches = [f for f in cands if test(f) and f not in classified]
        classified.update(matches)
        if matches:
            print(f'  {cat:25s} {len(matches):4d}')

    unclass = sorted(set(cands) - classified)
    print(f'  {"unclassified":25s} {len(unclass):4d}')
    print()
    print('=== UNCLASSIFIED (review for interactivity) ===')
    for fn in unclass:
        note = embeds[fn][0]
        print(f'  {fn}  ->  {note}')


if __name__ == '__main__':
    main()
