#!/usr/bin/env python3
"""
Build/refresh the sandbox "Clusters" pages from the cluster-validation campaign.

Reads every main cohort config in scripts/cluster_configs/*.yaml (skips sub_*.yaml),
pulls the cohort members + its benchmark ETF + the latest intra-corr / PC1% from
scripts/cluster_registry.csv, classifies each cohort into a theme, and writes one
normalized chart card per cohort onto themed pages (71-80) under a "Clusters"
category in charting_app/workspace.json.

Verdict pages (added 2026-07-02): the same cohorts are ALSO grouped onto three
verdict-tier pages (81 Validated / 82 Qualified / 83 Falsified), classified from
the owner note's cluster-status callout in the vault ([!success] / [!warning] /
[!failure]). Cohorts whose owner note can't be matched are listed at the end of
the run and can be pinned in VERDICT_OVERRIDES.

Idempotent: every card it writes is tagged "cluster"; a re-run removes the previous
cluster cards first, so adding new cohort configs + re-running keeps the pages current.

Usage:  python scripts/build_cluster_pages.py
"""
import csv
import glob
import json
import os
import re
import yaml

WS = 'charting_app/workspace.json'
CONFIGS = 'scripts/cluster_configs'
REGISTRY = 'scripts/cluster_registry.csv'
VAULT = 'investing'

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


# verdict tier -> (page number, tab label)
VERDICT_PAGES = {
    'success': (81, 'Validated'),
    'warning': (82, 'Qualified'),
    'failure': (83, 'Falsified'),
}

CALLOUT_RE = re.compile(r'^>\s*\[!(success|warning|failure)\]\s*Cluster status', re.IGNORECASE)

# Cohort name -> tier, for cohorts whose owner note can't be matched by
# title/alias containment (callout lives in a differently-named note, or the
# verdict is vault-recorded outside a callout). Cohorts with NO stamped verdict
# anywhere stay off the verdict pages (they still appear on theme pages).
VERDICT_OVERRIDES = {
    '中特估 cohort — banks + energy + telecoms': 'warning',   # China special valuation: real co-movement, duration basket, not distinct
    'Animal health': 'failure',            # callout lives in Actors/Zoetis.md
    'Appliance / housing durables': 'failure',   # callout lives in Actors/Whirlpool.md
    'Crypto-exposed financial platforms': 'warning',  # callout lives in Actors/Coinbase.md
    'Waste management': 'success',         # owner note is Sectors/Solid waste.md
    'Casinos': 'warning',                  # owner note is Concepts/Casino industry structure.md
    'GLP-1 obesity': 'failure',            # owner note is Concepts/GLP-1 receptor agonists.md
    'IoT module duopoly': 'success',       # Wireless module chokepoints callout = the validated Quectel+Fibocom pair
    'IoT cellular modules': 'failure',     # the 3-name cohort is falsified (Sivers dilution) in the same note
    'Live sports and entertainment rights': 'failure',  # callout lives in Assets/TKO securities note.md (sector-orphan)
    'Nuclear / SMR': 'warning',            # owner note is Concepts/Nuclear renaissance.md
    'Golden Dome defense-tech': 'failure', # super-cluster falsified in Sectors/Space pure-plays.md
    'Brazilian banks': 'warning',          # taxonomy zero-width table: real factor, embedded, not separable
    'WFE quartet': 'success',              # owner is Sectors/WFE.md ([!success]); Concepts/WFE quartet basket.md carries an older [!warning] stamp — two-stamp inconsistency flagged 2026-07-02
}


def _norm(s):
    s = s.lower()
    s = re.sub(r'\(.*?\)', ' ', s)          # drop parentheticals: "(ECPR)", "(ALTM)"
    s = re.sub(r'[^a-z0-9一-鿿]+', ' ', s)
    return ' '.join(s.split())


def load_note_verdicts():
    """Scan vault notes for cluster-status callouts.
    Returns [(tier, normalized note title, [normalized aliases])]."""
    out = []
    for path in glob.glob(os.path.join(VAULT, '**', '*.md'), recursive=True):
        try:
            text = open(path, encoding='utf-8').read()
        except OSError:
            continue
        m = CALLOUT_RE.search(text) if '[!' in text else None
        if not m:
            for line in text.splitlines():
                if CALLOUT_RE.match(line):
                    m = CALLOUT_RE.match(line)
                    break
        if not m:
            continue
        tier = m.group(1).lower()
        title = os.path.splitext(os.path.basename(path))[0]
        aliases = []
        am = re.search(r'^aliases:\s*\[([^\]]*)\]', text, re.MULTILINE)
        if am:
            aliases = [a.strip().strip('"\'') for a in am.group(1).split(',') if a.strip()]
        out.append((tier, _norm(title), [_norm(a) for a in aliases if a]))
    return out


def verdict_for(name, note_verdicts):
    """Match a cohort name to its owner note's callout tier.
    Containment either way on normalized title or aliases; overrides win."""
    if name in VERDICT_OVERRIDES:
        return VERDICT_OVERRIDES[name]
    n = _norm(name)
    if not n:
        return None
    best = None
    best_len = 0
    for tier, title, aliases in note_verdicts:
        for cand in [title] + aliases:
            if not cand:
                continue
            if n == cand or (n in cand) or (cand in n):
                # prefer the longest overlapping candidate (most specific note)
                if len(cand) > best_len:
                    best, best_len = tier, len(cand)
    return best

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
    note_verdicts = load_note_verdicts()
    files = sorted(glob.glob(os.path.join(CONFIGS, '*.yaml')))
    cards = []
    per_theme = {}
    per_verdict = {}
    unmatched = []
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

        tier = verdict_for(name, note_verdicts)
        if tier in VERDICT_PAGES:
            vpage, _ = VERDICT_PAGES[tier]
            cards.append(make_card(vpage, title, tickers, etf))
            per_verdict[tier] = per_verdict.get(tier, 0) + 1
        else:
            unmatched.append(name)

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
    for tier, (pg, label) in VERDICT_PAGES.items():
        names[str(pg)] = f"{label} ({per_verdict.get(tier, 0)})"
        if pg not in plist and str(pg) not in [str(x) for x in plist]:
            plist.append(pg)
        cluster_pages.append(pg)
    cats['Clusters'] = sorted(cluster_pages)

    tmp = WS + '.tmp'
    json.dump(ws, open(tmp, 'w', encoding='utf-8'), ensure_ascii=True)
    os.replace(tmp, WS)

    print(f"cohort cards built: {len(cards)}  (removed {removed} prior cluster cards)")
    print(f"registry stats matched: {matched}")
    for theme, (pg, label) in THEME_PAGES.items():
        print(f"   page {pg} {label:<34}: {per_theme.get(theme, 0)} cohorts")
    for tier, (pg, label) in VERDICT_PAGES.items():
        print(f"   page {pg} {label:<34}: {per_verdict.get(tier, 0)} cohorts")
    if unmatched:
        print(f"NO VERDICT MATCH ({len(unmatched)}) — not on verdict pages; pin in VERDICT_OVERRIDES if needed:")
        for n in unmatched:
            print(f"   - {n}")
    print(f"total cards now: {len(ws['cards'])}")


if __name__ == '__main__':
    main()
