#!/usr/bin/env python3
"""
Build/refresh the sandbox "Clusters" pages from the cluster-validation campaign.

Reads every main cohort config in scripts/cluster_configs/*.yaml (skips sub_*.yaml),
pulls the cohort members + its benchmark ETF + the latest intra-corr / PC1% from
scripts/cluster_registry.csv, classifies each cohort into a theme, and writes one
normalized chart card per cohort onto 7 themed pages (71-77) under a "Clusters"
category in charting_app/workspace.json.

Idempotent: every card it writes is tagged "cluster"; a re-run removes the previous
cluster cards first, so adding new cohort configs + re-running keeps the pages current.

Usage:  python scripts/build_cluster_pages.py
"""
import csv
import glob
import json
import os
import yaml

WS = 'charting_app/workspace.json'
CONFIGS = 'scripts/cluster_configs'
REGISTRY = 'scripts/cluster_registry.csv'

# theme key -> (page number, tab label)
THEME_PAGES = {
    'fin':         (71, 'Financials & Insurance'),
    'aitech':      (72, 'AI / Semis / Software'),
    'energy':      (73, 'Energy / Power / Materials'),
    'health':      (74, 'Healthcare'),
    'consumer':    (75, 'Consumer & Retail'),
    'reit':        (76, 'REITs / Real Assets'),
    'intl':        (77, 'International'),
    'media':       (78, 'Media & Telecom'),
    'industrials': (79, 'Industrials & Transports'),
    'defense':     (80, 'Defense & Aerospace'),
}

KEYWORDS = [
    ('intl',        ['brazil', 'china', 'chinese', '中特估', 'korea', 'japan', 'indian', 'european', 'luxury']),
    ('defense',     ['defense', 'aerospace', 'space pure', 'golden dome']),
    ('energy',      ['oil', 'gas', 'refiner', 'midstream', 'pipeline', 'oilfield', 'solar', 'nuclear', 'smr', 'uranium', 'copper', 'lithium', 'steel', 'aluminum', 'gold', 'silver', 'metal', 'rare earth', 'chemical', 'fertilizer', 'mining', 'power', 'ipp', 'utilit']),
    ('health',      ['pharma', 'biotech', 'medtech', 'telehealth', 'glp', 'obesity', 'managed care', 'life science', 'contract research', 'animal health', 'drug distributor', 'hospital']),
    ('reit',        ['reit', 'tower', 'self-storage', 'net-lease']),
    ('fin',         ['bank', 'insur', 'reinsur', 'payment', 'card network', 'exchange', 'asset manager', 'alt-asset', 'wealth', 'advisory', 'financial data', 'title', 'crypto equit', 'crypto-exposed']),
    ('aitech',      ['ai ', 'a.i', 'aifd', 'semi', 'fabless', 'foundry', 'memory', 'wfe', 'hyperscaler', 'neocloud', 'optic', 'quantum', 'cyber', 'saas', 'data-infra', 'consumption data', 'ad-tech', 'adtech', 'iot', 'compute', 'mag 7', 'software', 'it services', 'platform', 'scp', 'ecpr', 'analog']),
    ('media',       ['media', 'content', 'streaming', 'studios', 'theatrical', 'exhibition', 'live sports', 'entertainment', 'telecom']),
    ('industrials', ['building product', 'industrial distributor', 'trucking', 'ltl', 'railroad', 'tanker', 'waste', 'freight']),
]

def classify(name):
    low = ' ' + name.lower() + ' '
    for theme, kws in KEYWORDS:
        for kw in kws:
            if kw in low:
                return theme
    return 'consumer'   # fallback

def parse_config(path):
    """Return (name, {group_key: [tickers]}). Handles flow- and block-style YAML."""
    d = yaml.safe_load(open(path, encoding='utf-8')) or {}
    name = d.get('name')
    groups = {}
    for k, v in (d.get('groups', {}) or {}).items():
        groups[k] = list((v or {}).get('tickers', []) or [])
    return name, groups

def pick_benchmark(groups):
    etfs = []
    for k, v in groups.items():
        if 'etf' in k.lower():
            etfs += v
    for t in etfs:
        if t.upper() != 'SPY':
            return t
    return etfs[0] if etfs else 'SPY'

def load_registry_stats():
    stats = {}
    if not os.path.exists(REGISTRY):
        return stats
    for row in csv.DictReader(open(REGISTRY, encoding='utf-8')):
        nm = row.get('cohort_name')
        td = row.get('test_date', '')
        intra = row.get('intra_corr_1y', '')
        pc1 = row.get('pc1_variance_pct', '')
        if not nm or not intra:
            continue
        if nm not in stats or td > stats[nm]['date']:
            stats[nm] = {'date': td, 'intra': intra, 'pc1': pc1}
    return stats

DEFAULTS = {
    "page": "1", "type": None, "thesisId": None, "tickers": [],
    "showDiff": False, "showAvg": False, "showVol": False, "showVolume": False,
    "showRevenue": False, "showFundamentalsPane": False,
    "fundamentalsMetrics": ["revenue", "netincome"], "multipliers": {}, "hidden": [],
    "range": {"from": 1717200000, "to": 1782000000}, "useRaw": False, "useLogScale": False,
    "title": "", "lastLabelVisible": False, "lastTickerVisible": True, "showZeroLine": False,
    "showFixedLegend": True, "showLegendTickers": False, "fixedLegendPos": {"x": 20, "y": 20},
    "fixedLegendSize": {"height": 220, "width": 440}, "height": 520, "fontSize": 12,
    "showNotes": False, "notes": "", "manualInterval": "daily", "decimalPrecision": 2,
    "tickerColors": {}, "priceScaleAssignments": {}, "volumePaneStretchFactor": 1,
    "revenuePaneStretchFactor": 1, "fundamentalsPaneStretchFactor": 1, "starred": False,
    "tags": ["cluster"], "noteLink": "",
}

def make_card(page, title, tickers, etf):
    c = dict(DEFAULTS)
    c['page'] = str(page)
    c['title'] = title
    c['tickers'] = tickers
    c['tickerColors'] = {etf: "#9E9E9E"}   # benchmark ETF greyed as control
    c['tags'] = ["cluster"]
    return c

def main():
    stats = load_registry_stats()
    files = sorted(glob.glob(os.path.join(CONFIGS, '*.yaml')))
    cards = []
    per_theme = {}
    matched = 0
    for f in files:
        if os.path.basename(f).startswith('sub_'):
            continue
        name, groups = parse_config(f)
        members = groups.get('cluster', [])
        if not name or not members:
            continue
        etf = pick_benchmark(groups)
        tickers = list(members) + ([etf] if etf and etf not in members else [])
        st = stats.get(name)
        if st:
            matched += 1
            try:
                title = f"{name} | corr {float(st['intra']):.2f} PC1 {float(st['pc1']):.0f}%"
            except ValueError:
                title = name
        else:
            title = name
        theme = classify(name)
        page, _ = THEME_PAGES[theme]
        cards.append(make_card(page, title, tickers, etf))
        per_theme[theme] = per_theme.get(theme, 0) + 1

    ws = json.load(open(WS, encoding='utf-8'))
    # idempotent: drop previous cluster cards
    kept = [c for c in ws['cards'] if 'cluster' not in (c.get('tags') or [])]
    removed = len(ws['cards']) - len(kept)
    ws['cards'] = kept + cards

    pages = ws.setdefault('pages', {})
    names = pages.setdefault('names', {})
    cats = pages.setdefault('categories', {})
    plist = pages.setdefault('pages', [])
    cluster_pages = []
    for theme, (pg, label) in THEME_PAGES.items():
        names[str(pg)] = label
        if pg not in plist and str(pg) not in [str(x) for x in plist]:
            plist.append(pg)
        cluster_pages.append(pg)
    cats['Clusters'] = sorted(cluster_pages)

    tmp = WS + '.tmp'
    json.dump(ws, open(tmp, 'w', encoding='utf-8'), ensure_ascii=True)
    os.replace(tmp, WS)

    print(f"cohorts built: {len(cards)}  (removed {removed} prior cluster cards)")
    print(f"registry stats matched: {matched}/{len(cards)}")
    for theme, (pg, label) in THEME_PAGES.items():
        print(f"   page {pg} {label:<34}: {per_theme.get(theme, 0)} cohorts")
    print(f"total cards now: {len(ws['cards'])}")


if __name__ == '__main__':
    main()
