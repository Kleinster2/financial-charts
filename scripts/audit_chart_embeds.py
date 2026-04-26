"""Audit chart embeds in the investing vault.

For each unique chart filename embedded in the vault, classify how the Quartz
LightweightCharts plugin will treat it:
  - parsed-*  : filename matches a parser pattern (vs / price-chart / ytd / dur)
  - skip-fund : filename contains 'fundamentals' -> static image (intentional)
  - static-financial : sankey/waterfall -> static image (intentional)
  - unknown   : falls through to registry lookup

Then check which 'unknown' filenames are missing from chart-registry.md.
Those are the embeds that need migration work.
"""
from __future__ import annotations
import re
from pathlib import Path
import yaml

VAULT = Path('investing')
EMBED_PAT = re.compile(r'!\[\[([^\]|]+\.png)(?:\|[^\]]*)?\]\]')
SKIP_FOLDERS = {'attachments', '.obsidian', '.trash', 'Daily', 'Meta', 'Newsletter', 'Reports'}
SKIP_FILES = {'chart-registry.md', 'research-queue.md'}


def classify(fn: str) -> str:
    name = fn[:-4] if fn.lower().endswith('.png') else fn
    nl = name.lower()
    if 'fundamentals' in nl:
        return 'skip-fund'
    if '-vs-' in name:
        return 'parsed-vs'
    if '-price-chart' in name:
        return 'parsed-price'
    if name.endswith('-ytd'):
        return 'parsed-ytd'
    if re.search(r'-(\d+)(d|y)$', name, re.I):
        return 'parsed-dur'
    if name.endswith('-sankey') or name.endswith('-waterfall'):
        return 'static-financial'
    return 'unknown'


def main() -> None:
    embeds: dict[str, list[str]] = {}
    for md in VAULT.rglob('*.md'):
        if any(p in SKIP_FOLDERS for p in md.parts):
            continue
        if md.name in SKIP_FILES:
            continue
        try:
            text = md.read_text(encoding='utf-8', errors='ignore')
        except Exception:
            continue
        for m in EMBED_PAT.finditer(text):
            fn = Path(m.group(1).strip().replace('\\', '/')).name
            if fn.lower().endswith('.png'):
                embeds.setdefault(fn, []).append(str(md))

    reg_text = (VAULT / 'chart-registry.md').read_text(encoding='utf-8')
    fm = re.match(r'^---\n(.*?)\n---', reg_text, re.S)
    reg = yaml.safe_load(fm.group(1)) if fm else {}
    registered = set((reg or {}).get('charts', {}).keys())

    buckets: dict[tuple[str, bool], list[tuple[str, int, list[str]]]] = {}
    for fn, notes in embeds.items():
        key = (classify(fn), fn in registered)
        buckets.setdefault(key, []).append((fn, len(notes), notes[:3]))

    print(f'Total unique chart filenames embedded: {len(embeds)}')
    print(f'Total registry entries: {len(registered)}')
    print()
    print('--- Classification ---')
    for (c, in_reg), items in sorted(buckets.items()):
        print(f'  {c:18s} in_registry={in_reg!s:5s}  {len(items):4d} files')
    print()
    print('=== UNMATCHED + NOT IN REGISTRY (broken/static, need attention) ===')
    miss = buckets.get(('unknown', False), [])
    miss.sort(key=lambda x: -x[1])
    for fn, count, notes in miss:
        print(f'  {count:3d}x  {fn}')
    print(f'\nTotal unknown-not-in-registry: {len(miss)}')

    print()
    print('=== Registry entries with NO embeds (orphans) ===')
    orphans = sorted(registered - set(embeds.keys()))
    for fn in orphans:
        print(f'  {fn}')
    print(f'\nTotal orphan registry entries: {len(orphans)}')


if __name__ == '__main__':
    main()
