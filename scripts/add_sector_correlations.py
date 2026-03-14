#!/usr/bin/env python
"""
Add ## Sector correlation sections to public company actor notes.

Calculates 1-year daily return correlations against sector ETFs,
picks the top 3 fits, and inserts a formatted markdown section.

Usage:
    python scripts/add_sector_correlations.py --list             # list processable notes
    python scripts/add_sector_correlations.py --dry-run          # preview sections
    python scripts/add_sector_correlations.py                    # process all
    python scripts/add_sector_correlations.py --ticker AAPL      # single ticker
    python scripts/add_sector_correlations.py --start 2025-06-01 # custom start
"""

import argparse
import sqlite3
import re
import sys
from pathlib import Path
from datetime import datetime, timedelta

import pandas as pd
import numpy as np

DB_PATH = Path(__file__).parent.parent / 'market_data.db'
ACTORS_DIR = Path(__file__).parent.parent / 'investing' / 'Actors'

# Sector ETFs → display name (wikilinks where vault note exists)
SECTOR_ETFS = {
    'XLK': 'Technology',
    'XLF': 'Financials',
    'XLE': '[[Energy and Utilities|Energy]]',
    'XLV': '[[Healthcare]]',
    'XLI': 'Industrials',
    'XLU': 'Utilities',
    'XLC': 'Communications',
    'XLY': '[[Consumer]]',
    'XLP': '[[Consumer Staples]]',
    'XLRE': '[[Real estate|Real Estate]]',
    'SMH': '[[Semiconductors]]',
    'ITA': '[[Defense]]',
    'KRE': '[[Banks|Regional Banks]]',
    'XOP': 'Oil & Gas E&P',
    'IGV': 'Software',
    'KWEB': 'China Internet',
}


def get_db_tickers(conn):
    """Get all ticker columns in stock_prices_daily."""
    cursor = conn.execute("PRAGMA table_info(stock_prices_daily)")
    return {row[1] for row in cursor.fetchall() if row[1] != 'Date'}


def load_all_prices(conn, tickers, start_date):
    """Load price data for given tickers."""
    cols = ', '.join([f'"{t}"' for t in tickers])
    query = f'SELECT Date, {cols} FROM stock_prices_daily WHERE Date >= "{start_date}" ORDER BY Date'
    df = pd.read_sql(query, conn)
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.set_index('Date')
    return df


def calculate_all_correlations(returns_df, stock_tickers):
    """Calculate each stock ticker's correlation against sector ETFs + SPY."""
    results = {}
    etf_list = list(SECTOR_ETFS.keys()) + ['SPY']

    for ticker in stock_tickers:
        if ticker not in returns_df.columns:
            continue
        corrs = {}
        for etf in etf_list:
            if etf == ticker:
                continue
            if etf not in returns_df.columns:
                continue
            pair = returns_df[[ticker, etf]].dropna()
            if len(pair) < 30:
                continue
            c = pair[ticker].corr(pair[etf])
            if not np.isnan(c):
                corrs[etf] = round(c, 2)
        if corrs:
            results[ticker] = corrs

    return results


def parse_aliases(filepath):
    """Extract aliases list and full text from a note."""
    text = filepath.read_text(encoding='utf-8')
    m = re.match(r'^---\n(.*?)\n---', text, re.DOTALL)
    if not m:
        return [], text

    fm_text = m.group(1)

    # Inline list: aliases: [A, B, C]
    inline = re.search(r'aliases:\s*\[([^\]]*)\]', fm_text)
    if inline:
        aliases = [a.strip().strip('"').strip("'") for a in inline.group(1).split(',')]
        return [a for a in aliases if a], text

    # Multi-line list
    multi = re.search(r'aliases:\s*\n((?:\s+-\s+.+\n?)+)', fm_text)
    if multi:
        aliases = re.findall(r'-\s+(.+)', multi.group(0))
        return [a.strip().strip('"').strip("'") for a in aliases], text

    # Single value: aliases: A
    single = re.search(r'aliases:\s+(\S+)', fm_text)
    if single:
        return [single.group(1).strip('"').strip("'")], text

    return [], text


def extract_ticker(aliases, db_tickers):
    """Find a DB-matching ticker from aliases."""
    for alias in aliases:
        clean = alias.strip()
        if clean in db_tickers:
            return clean
        up = clean.upper()
        if up in db_tickers:
            return up
        # BRK.B → BRK-B
        alt = clean.replace('.', '-')
        if alt in db_tickers:
            return alt
    return None


def should_skip(text):
    """Check if note should be skipped (ETFs, funds, people, countries, etc.)."""
    tags_area = text[:500]
    # Skip ETFs and funds — need benchmark comparison, not sector correlation
    if re.search(r'#(etf|fund|index)\b', tags_area):
        return True
    # Skip non-company entities
    skip_tags = (
        r'person|analyst|investor|country|institution|central.?bank|regulator|'
        r'university|nonprofit|consortium|ngo|standard|government|military|'
        r'agency|ministry|embassy|lobbyist|politician|journalist|academic|'
        r'think.?tank|research.?institute|labor.?union|union'
    )
    if re.search(rf'#({skip_tags})\b', tags_area):
        return True
    # Also check YAML-style tags: [actor, university, ...]
    fm_match = re.match(r'^---\n(.*?)\n---', text, re.DOTALL)
    if fm_match:
        tags_line = re.search(r'tags:\s*\[([^\]]*)\]', fm_match.group(1))
        if tags_line:
            yaml_tags = [t.strip() for t in tags_line.group(1).split(',')]
            skip_set = {'person', 'analyst', 'investor', 'country', 'institution',
                        'university', 'nonprofit', 'consortium', 'ngo', 'government',
                        'military', 'etf', 'fund', 'index', 'politician', 'journalist',
                        'academic', 'lobbyist'}
            if skip_set & set(yaml_tags):
                return True
    return False


def has_correlation_section(text):
    """Check if note already has a correlation section."""
    return '## Sector correlation' in text or '## Volatility correlation' in text


def format_section(ticker, correlations):
    """Generate markdown for the correlation section."""
    sector_corrs = {k: v for k, v in correlations.items() if k in SECTOR_ETFS}
    spy_corr = correlations.get('SPY')

    if not sector_corrs:
        return None

    sorted_sectors = sorted(sector_corrs.items(), key=lambda x: abs(x[1]), reverse=True)
    top3 = sorted_sectors[:3]
    max_corr = abs(top3[0][1])
    is_orphan = max_corr < 0.50

    lines = ['## Sector correlation', '']

    if is_orphan:
        lines.append('> [!warning] Sector Orphan')
        lines.append(f'> {ticker} does not trade tightly with any sector ETF (max r = {top3[0][1]:.2f} with {top3[0][0]}).')
        lines.append('')

    lines.append('| Sector | ETF | Correlation |')
    lines.append('|--------|-----|-------------|')

    for etf, corr in top3:
        name = SECTOR_ETFS[etf]
        lines.append(f'| {name} | {etf} | {corr:.2f} |')

    if spy_corr is not None:
        lines.append(f'| *S&P 500* | *SPY* | *{spy_corr:.2f}* |')

    lines.append('')

    # Interpretation
    best_etf, best_corr = top3[0]
    best_name = SECTOR_ETFS[best_etf]
    clean_name = re.sub(r'\[\[([^|\]]*\|)?([^\]]+)\]\]', r'\2', best_name)

    if best_corr >= 0.70:
        lines.append(f'{ticker} trades as a core {clean_name} name ({best_etf} r = {best_corr:.2f}).')
    elif best_corr >= 0.50:
        lines.append(f'{ticker} shows moderate {clean_name} correlation ({best_etf} r = {best_corr:.2f}).')
    else:
        if len(top3) > 1:
            second_name = re.sub(r'\[\[([^|\]]*\|)?([^\]]+)\]\]', r'\2', SECTOR_ETFS[top3[1][0]])
            lines.append(f'{ticker} trades between {clean_name} and {second_name} without a tight sector fit.')
        else:
            lines.append(f'{ticker} trades with limited sector correlation — idiosyncratic story.')

    return '\n'.join(lines)


def find_insert_position(text):
    """Find where to insert the correlation section.

    Places section right after the intro paragraph (and Synopsis if present),
    before the first body content section.
    """
    # Find the end of frontmatter
    fm_match = re.match(r'^---\n.*?\n---\n', text, re.DOTALL)
    if not fm_match:
        idx = text.find('\n## ')
        return idx + 1 if idx >= 0 else len(text.rstrip())

    after_fm = fm_match.end()

    # Find the first --- divider after frontmatter
    # This separates the intro paragraph from body content
    first_divider = text.find('\n---\n', after_fm)
    if first_divider < 0:
        idx = text.find('\n## ', after_fm)
        return idx + 1 if idx >= 0 else len(text.rstrip())

    # Check if Synopsis follows the divider
    divider_end = first_divider + 5  # skip \n---\n
    remaining = text[divider_end:].lstrip('\n')
    if remaining.startswith('## Synopsis'):
        synopsis_pos = text.index('## Synopsis', divider_end)
        next_divider = text.find('\n---\n', synopsis_pos + 10)
        next_header = text.find('\n## ', synopsis_pos + 10)
        if next_divider >= 0 and (next_header < 0 or next_divider <= next_header):
            return next_divider + 1
        elif next_header >= 0:
            return next_header + 1

    # Insert at the first divider position (after intro, before body)
    return first_divider + 1


def insert_section_into_note(text, section_text):
    """Insert correlation section at the right position. Returns new text."""
    pos = find_insert_position(text)

    before = text[:pos].rstrip()
    after = text[pos:]

    if before.endswith('---'):
        pre = before[:-3].rstrip()
        return pre + '\n\n---\n\n' + section_text + '\n\n---\n\n' + after
    elif after.lstrip().startswith('---'):
        return before + '\n\n---\n\n' + section_text + '\n\n' + after
    else:
        return before + '\n\n---\n\n' + section_text + '\n\n---\n\n' + after


def main():
    parser = argparse.ArgumentParser(description='Add sector correlation sections to actor notes')
    parser.add_argument('--ticker', help='Process single ticker')
    parser.add_argument('--dry-run', action='store_true', help='Preview without writing')
    parser.add_argument('--list', action='store_true', help='List processable notes')
    parser.add_argument('--start', default=None, help='Start date (default: 1 year ago)')
    args = parser.parse_args()

    if args.start is None:
        start_date = (datetime.now() - timedelta(days=365)).strftime('%Y-%m-%d')
    else:
        start_date = args.start

    conn = sqlite3.connect(DB_PATH)
    db_tickers = get_db_tickers(conn)

    # Collect processable notes
    notes = []
    skipped_excluded = 0
    skipped_has_section = 0
    skipped_no_db = []

    if args.ticker:
        # Single ticker mode
        ticker_upper = args.ticker.upper()
        for f in ACTORS_DIR.glob('*.md'):
            aliases, text = parse_aliases(f)
            t = extract_ticker(aliases, db_tickers)
            if t and t.upper() == ticker_upper:
                if has_correlation_section(text):
                    print(f"Already has section: {f.name}")
                    return
                notes.append((f, t))
                break
        if not notes:
            print(f"No actor note found for ticker {args.ticker}")
            return
    else:
        for f in sorted(ACTORS_DIR.glob('*.md')):
            aliases, text = parse_aliases(f)

            if should_skip(text):
                skipped_excluded += 1
                continue

            if has_correlation_section(text):
                skipped_has_section += 1
                continue

            ticker = extract_ticker(aliases, db_tickers)
            if not ticker:
                skipped_no_db.append(f.stem)
                continue

            notes.append((f, ticker))

    if args.list:
        print(f"Would process {len(notes)} notes:")
        for f, t in notes:
            print(f"  {t:10s}  {f.stem}")
        print(f"\nSkipped: {skipped_excluded} excluded (ETFs/people/etc), "
              f"{skipped_has_section} already have section, "
              f"{len(skipped_no_db)} no DB ticker")
        if skipped_no_db:
            shown = skipped_no_db[:30]
            print(f"No DB ticker: {', '.join(shown)}"
                  f"{'...' if len(skipped_no_db) > 30 else ''}")
        return

    if not notes:
        print("No notes to process.")
        return

    # Load all price data at once
    all_tickers = list(set(
        [t for _, t in notes] + list(SECTOR_ETFS.keys()) + ['SPY']
    ))
    all_tickers = [t for t in all_tickers if t in db_tickers]

    print(f"Loading prices for {len(all_tickers)} tickers from {start_date}...")
    prices = load_all_prices(conn, all_tickers, start_date)
    returns = prices.pct_change(fill_method=None)
    print(f"  {len(returns)} trading days, {len(returns.columns)} tickers loaded")

    print(f"Calculating correlations for {len(notes)} notes...")
    stock_tickers = list(set(t for _, t in notes))
    all_corrs = calculate_all_correlations(returns, stock_tickers)

    # Process each note
    processed = 0
    failed = 0

    for filepath, ticker in notes:
        if ticker not in all_corrs:
            print(f"  SKIP {ticker:10s}  {filepath.stem} — insufficient data")
            failed += 1
            continue

        section = format_section(ticker, all_corrs[ticker])
        if section is None:
            print(f"  SKIP {ticker:10s}  {filepath.stem} — no correlations")
            failed += 1
            continue

        if args.dry_run:
            print(f"\n{'='*60}")
            print(f"  {filepath.stem} ({ticker})")
            print(f"{'='*60}")
            print(section)
            processed += 1
        else:
            try:
                text = filepath.read_text(encoding='utf-8')
                new_text = insert_section_into_note(text, section)
                filepath.write_text(new_text, encoding='utf-8')
                print(f"  OK   {ticker:10s}  {filepath.stem}")
                processed += 1
            except Exception as e:
                print(f"  FAIL {ticker:10s}  {filepath.stem}: {e}")
                failed += 1

    print(f"\nDone: {processed} processed, {failed} failed")
    if skipped_has_section:
        print(f"  {skipped_has_section} already had section")
    if skipped_no_db:
        print(f"  {len(skipped_no_db)} had no DB ticker")

    conn.close()


if __name__ == '__main__':
    main()
