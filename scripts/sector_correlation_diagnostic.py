#!/usr/bin/env python
"""
Whole-vault sector correlation diagnostic.

Walks every Sectors/*.md hub in the investing vault, extracts [[Actor]]
wikilinks, maps them to tickers via Actors/*.md frontmatter aliases plus
ticker_metadata fallback, and computes average pairwise daily-return
correlation over the trailing window.

Output: ranked table of sectors by internal correlation, plus a list of
sectors with insufficient mapped tickers for diagnosis.

Usage:
    python scripts/sector_correlation_diagnostic.py
    python scripts/sector_correlation_diagnostic.py --window 252
    python scripts/sector_correlation_diagnostic.py --min-actors 5
"""

import argparse
import re
import sqlite3
import statistics
import sys
from pathlib import Path

VAULT = Path(__file__).parent.parent / 'investing'
DB = Path(__file__).parent.parent / 'market_data.db'

FRONTMATTER_RE = re.compile(r'^---\n(.*?)\n---', re.DOTALL)
ALIAS_RE = re.compile(r'aliases:\s*\[([^\]]*)\]')
WIKILINK_RE = re.compile(r'\[\[([^\]|#]+?)(?:\|[^\]]*)?\]\]')


def build_actor_ticker_map(db_tickers, name_to_ticker):
    actor_to_ticker = {}
    for md in (VAULT / 'Actors').glob('*.md'):
        actor_name = md.stem
        text = md.read_text(encoding='utf-8', errors='ignore')
        fm = FRONTMATTER_RE.match(text)
        candidates = []
        if fm:
            am = ALIAS_RE.search(fm.group(1))
            if am:
                for a in am.group(1).split(','):
                    a = a.strip().strip('"').strip("'")
                    if a:
                        candidates.append(a)
        chosen = None
        for c in candidates:
            cu = c.upper()
            if cu in db_tickers:
                chosen = cu
                break
        if not chosen and actor_name.lower() in name_to_ticker:
            t = name_to_ticker[actor_name.lower()]
            if t in db_tickers:
                chosen = t
        if chosen:
            actor_to_ticker[actor_name.lower()] = chosen
    return actor_to_ticker


def pearson(xs, ys):
    n = len(xs)
    if n < 2:
        return None
    mx = sum(xs) / n
    my = sum(ys) / n
    num = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    dx = (sum((x - mx) ** 2 for x in xs)) ** 0.5
    dy = (sum((y - my) ** 2 for y in ys)) ** 0.5
    if dx == 0 or dy == 0:
        return None
    return num / (dx * dy)


def main(window, min_actors):
    conn = sqlite3.connect(str(DB))
    cur = conn.cursor()
    cur.execute("PRAGMA table_info(stock_prices_daily)")
    db_tickers = {r[1] for r in cur.fetchall() if r[1] != 'Date'}

    cur.execute("SELECT ticker, name FROM ticker_metadata")
    name_to_ticker = {}
    for tk, nm in cur.fetchall():
        if not nm:
            continue
        name_to_ticker[nm.lower()] = tk
        base = re.sub(
            r',?\s+(Inc\.?|Corp\.?|Corporation|Co\.?|Company|Ltd\.?|Limited|PLC|N\.V\.|S\.A\.|Holdings|Group|Plc)$',
            '', nm, flags=re.IGNORECASE).strip()
        if base.lower() != nm.lower():
            name_to_ticker[base.lower()] = tk

    actor_to_ticker = build_actor_ticker_map(db_tickers, name_to_ticker)
    print(f"Mapped {len(actor_to_ticker)} actors to tickers", file=sys.stderr)

    sector_actors = {}
    for md in (VAULT / 'Sectors').glob('*.md'):
        sector_name = md.stem
        text = md.read_text(encoding='utf-8', errors='ignore')
        seen = set()
        tickers = []
        for link in WIKILINK_RE.findall(text):
            key = link.strip().lower()
            if key in actor_to_ticker:
                t = actor_to_ticker[key]
                if t not in seen:
                    tickers.append(t)
                    seen.add(t)
        sector_actors[sector_name] = tickers

    cur.execute("SELECT Date FROM stock_prices_daily ORDER BY Date DESC LIMIT ?", (window,))
    dates = [r[0] for r in cur.fetchall()][::-1]
    date_set = ','.join(f"'{d}'" for d in dates)

    ticker_returns = {}

    def get_returns(ticker):
        if ticker in ticker_returns:
            return ticker_returns[ticker]
        try:
            cur.execute(
                f'SELECT Date, "{ticker}" FROM stock_prices_daily '
                f'WHERE Date IN ({date_set}) ORDER BY Date'
            )
            rows = cur.fetchall()
        except sqlite3.OperationalError:
            ticker_returns[ticker] = None
            return None
        prices = [r[1] for r in rows]
        if len(prices) < 60:
            ticker_returns[ticker] = None
            return None
        rets = []
        for i in range(1, len(prices)):
            a, b = prices[i - 1], prices[i]
            if a is None or b is None or a == 0:
                rets.append(None)
            else:
                rets.append((b - a) / a)
        ticker_returns[ticker] = rets
        return rets

    results = []
    for sector, tickers in sector_actors.items():
        valid = []
        for t in tickers:
            r = get_returns(t)
            if r is not None:
                valid.append((t, r))
        if len(valid) < min_actors:
            results.append((sector, len(tickers), len(valid), None, None))
            continue
        corrs = []
        n = len(valid)
        for i in range(n):
            for j in range(i + 1, n):
                _, r1 = valid[i]
                _, r2 = valid[j]
                xs, ys = [], []
                for a, b in zip(r1, r2):
                    if a is not None and b is not None:
                        xs.append(a)
                        ys.append(b)
                if len(xs) < 30:
                    continue
                c = pearson(xs, ys)
                if c is not None:
                    corrs.append(c)
        if corrs:
            results.append((sector, len(tickers), len(valid),
                            statistics.mean(corrs), statistics.median(corrs)))
        else:
            results.append((sector, len(tickers), len(valid), None, None))

    with_data = sorted([r for r in results if r[3] is not None], key=lambda x: -x[3])
    no_data = [r for r in results if r[3] is None]

    print(f"\n{'Sector':<32} {'Actors':>7} {'Mapped':>7} {'AvgCorr':>8} {'MedCorr':>8}")
    print("-" * 70)
    for sector, total, mapped, avg, med in with_data:
        print(f"{sector:<32} {total:>7} {mapped:>7} {avg:>8.3f} {med:>8.3f}")
    print(f"\n=== Insufficient mapped tickers ({len(no_data)}) ===")
    for sector, total, mapped, _, _ in sorted(no_data, key=lambda x: -x[1]):
        print(f"{sector:<32} {total:>7} actors, {mapped:>3} mapped")


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--window', type=int, default=252,
                   help='Trailing trading days (default 252)')
    p.add_argument('--min-actors', type=int, default=3,
                   help='Minimum mapped actors to compute correlation (default 3)')
    args = p.parse_args()
    main(args.window, args.min_actors)
