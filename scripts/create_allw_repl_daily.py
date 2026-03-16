#!/usr/bin/env python3
"""
create_allw_repl_daily.py

ALLW Replication using actual daily holdings data from Risk Parity vault.

Reads ~41 daily snapshots (Jan 8 - Mar 12, 2026) from:
  C:/Users/klein/obsidian/Risk Parity/10 - Portfolio Tracking/ALLW/

For the pre-snapshot period (Mar 2025 - Jan 2026), falls back to the
5-point interpolation from create_allw_repl_index.py.

Produces:
  ALLW_REPL_DAILY  -- 4-ETF (SPY/TLT/TIP/GLD) with actual daily weights + leverage
  ALLW_11ETF_DAILY -- 11-ETF with actual daily sub-weights + leverage

Usage:
    python scripts/create_allw_repl_daily.py [--store]
"""

import sys
import re
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
sys.path.insert(0, str(Path(__file__).parent.parent / 'charting_app'))

import sqlite3
import pandas as pd
import numpy as np

DB_PATH = Path(__file__).parent.parent / 'market_data.db'
VAULT_PATH = Path('C:/Users/klein/obsidian/Risk Parity/10 - Portfolio Tracking/ALLW')
BASE_DATE = '2025-03-06'
FINANCING_RATE = 0.048

# Fallback schedule for pre-snapshot period (Mar 2025 - Jan 2026)
WEIGHT_SCHEDULE = [
    # date,         equity, bonds,  TIPS,   commodities
    ('2025-03-06',  0.250,  0.475,  0.194,  0.081),
    ('2025-05-15',  0.432,  0.344,  0.157,  0.067),
    ('2025-08-05',  0.539,  0.280,  0.131,  0.051),
    ('2025-12-15',  0.269,  0.452,  0.215,  0.064),
]

LEVERAGE_SCHEDULE_FALLBACK = [
    ('2025-03-06', 0.78),
    ('2025-05-15', 1.00),
    ('2025-08-05', 1.23),
    ('2025-12-15', 1.60),
]

# Static sub-weight defaults (used before Jan 2026 snapshot coverage)
DEFAULT_EQ_SUBS = {'us': 0.316, 'europe': 0.401, 'japan': 0.116, 'em': 0.100, 'china': 0.068}
DEFAULT_BOND_SUBS = {'tlt': 0.306, 'ief': 0.204, 'bndx': 0.490}
DEFAULT_COMMOD_SUBS = {'gld': 0.72, 'gsg': 0.28}

TICKERS_4ETF = ['SPY', 'TLT', 'TIP', 'GLD']
TICKERS_11ETF = ['SPLG', 'VGK', 'EWJ', 'SPEM', 'GXC', 'TLT', 'IEF', 'BNDX', 'TIP', 'GLD', 'GSG']


# ---------------------------------------------------------------------------
# Snapshot parsing
# ---------------------------------------------------------------------------

def parse_frontmatter(text):
    """Extract YAML-like frontmatter values from markdown text."""
    fm = {}
    in_fm = False
    for line in text.split('\n'):
        if line.strip() == '---':
            if in_fm:
                break
            in_fm = True
            continue
        if in_fm and ':' in line:
            key, _, val = line.partition(':')
            key = key.strip()
            val = val.strip()
            # Skip array values like tags
            if val.startswith('['):
                continue
            try:
                fm[key] = float(val)
            except ValueError:
                fm[key] = val
    return fm


def parse_dollar_value(cell):
    """Extract dollar value in millions from a table cell like '$126.5M'."""
    m = re.search(r'\$([\d,.]+)M', cell)
    if m:
        return float(m.group(1).replace(',', ''))
    return 0.0


def parse_all_tables(text):
    """Extract ALL table data rows from the markdown, preserving section context.

    Returns list of (section_name, [cell0, cell1, cell2, cell3]) tuples.
    Keeps empty cells to preserve column alignment.
    """
    rows = []
    current_section = ''
    for line in text.split('\n'):
        if line.strip().startswith('###'):
            current_section = line.strip().lstrip('#').strip().lower()
            continue
        if '|' in line:
            # Split keeping all cells (including empty)
            parts = line.split('|')
            # Remove first and last (empty from leading/trailing |)
            if len(parts) >= 3:
                cells = [p.strip() for p in parts[1:-1]]
            else:
                continue
            # Skip header/separator rows
            if all(c.startswith('-') or c == '' for c in cells):
                continue
            if any(c in ('Holding', 'Ticker', 'Weight', 'Value', 'Notional', '% of NAV',
                         'Asset Class', 'Metric', 'Risk %', '%', '% of NAV') for c in cells):
                continue
            rows.append((current_section, cells))
    return rows


def find_dollar_value(cells):
    """Find dollar value in any cell of a row."""
    for cell in cells:
        val = parse_dollar_value(cell)
        if val > 0:
            return val
    return 0.0


def parse_snapshot(filepath):
    """Parse a daily snapshot markdown file."""
    text = filepath.read_text(encoding='utf-8')
    fm = parse_frontmatter(text)

    if 'date' not in fm:
        return None

    result = {
        'date': str(fm['date']).split(' ')[0],  # Handle date-only or datetime
        'nav': float(fm.get('nav', 0)),
        'leverage': float(fm.get('leverage', 1.0)),
        'equities': float(fm.get('equities', 0)) / 100,
        'bonds': float(fm.get('bonds', 0)) / 100,
        'tips': float(fm.get('tips', 0)) / 100,
        'commodities': float(fm.get('commodities', 0)) / 100,
    }

    # --- Parse holdings for sub-weights ---
    # Parse all table rows, classify by holding name (not section)
    all_rows = parse_all_tables(text)

    equity_etf_values = {}
    equity_futures = {}
    bond_futures = {}
    gold_notional = 0
    bcomtr_notional = 0

    for section, cells in all_rows:
        if not cells:
            continue
        name = cells[0].upper()
        val = find_dollar_value(cells)
        if val == 0:
            continue

        # Classify by name pattern (regardless of section)
        # Equity ETFs
        if any(t in cells[1] if len(cells) > 1 else '' for t in ['SPYM', 'SPLG']):
            equity_etf_values['us_etf'] = val
        elif 'SPEM' in (cells[1] if len(cells) > 1 else ''):
            equity_etf_values['em'] = val
        elif 'GXC' in (cells[1] if len(cells) > 1 else ''):
            equity_etf_values['china'] = val
        # Equity Futures (by name, even if in wrong section)
        elif 'TOPIX' in name:
            equity_futures['japan'] = val
        elif 'EURO STOXX' in name:
            equity_futures['euro_stoxx'] = val
        elif 'FTSE' in name:
            equity_futures['ftse'] = val
        elif 'SPI' in name and 'BOND' not in name:
            equity_futures['spi'] = val
        # Bond Futures
        elif 'LONG BOND' in name or 'US LONG' in name:
            bond_futures['us_long'] = val
        elif '10YR' in name and 'AUST' not in name:
            bond_futures['us_10y'] = val
        elif 'BUND' in name:
            bond_futures['bund'] = val
        elif 'GILT' in name:
            bond_futures['gilt'] = val
        elif 'AUST' in name and 'BOND' in name:
            bond_futures['aust'] = val
        # Commodities
        elif 'GOLD' in name and ('FUTR' in name or 'OZ' in name):
            gold_notional = val
        elif 'BCOMTR' in name:
            bcomtr_notional = val

    # Compute equity sub-weights
    us_eq = equity_etf_values.get('us_etf', 0)
    em_eq = equity_etf_values.get('em', 0)
    china_eq = equity_etf_values.get('china', 0)
    europe_eq = sum(equity_futures.get(k, 0) for k in ['euro_stoxx', 'ftse', 'spi'])
    japan_eq = equity_futures.get('japan', 0)
    total_eq = us_eq + em_eq + china_eq + europe_eq + japan_eq

    if total_eq > 0:
        result['eq_us'] = us_eq / total_eq
        result['eq_europe'] = europe_eq / total_eq
        result['eq_japan'] = japan_eq / total_eq
        result['eq_em'] = em_eq / total_eq
        result['eq_china'] = china_eq / total_eq
    else:
        for k, v in DEFAULT_EQ_SUBS.items():
            result[f'eq_{k}'] = v

    # Bond sub-weights
    us_long = bond_futures.get('us_long', 0)
    us_10y = bond_futures.get('us_10y', 0)
    intl = sum(bond_futures.get(k, 0) for k in ['bund', 'gilt', 'aust'])
    total_bonds = us_long + us_10y + intl

    if total_bonds > 0:
        result['bond_tlt'] = us_long / total_bonds
        result['bond_ief'] = us_10y / total_bonds
        result['bond_bndx'] = intl / total_bonds
    else:
        for k, v in DEFAULT_BOND_SUBS.items():
            result[f'bond_{k}'] = v

    # Commodity sub-weights
    total_commod = gold_notional + bcomtr_notional
    if total_commod > 0:
        result['commod_gld'] = gold_notional / total_commod
        result['commod_gsg'] = bcomtr_notional / total_commod
    else:
        for k, v in DEFAULT_COMMOD_SUBS.items():
            result[f'commod_{k}'] = v

    return result


def parse_all_snapshots():
    """Parse all daily snapshot files, return sorted list."""
    snapshots = []
    for f in sorted(VAULT_PATH.glob('ALLW-2026-*.md')):
        snap = parse_snapshot(f)
        if snap:
            snapshots.append(snap)
    return sorted(snapshots, key=lambda x: x['date'])


# ---------------------------------------------------------------------------
# Daily schedule builder
# ---------------------------------------------------------------------------

def build_daily_schedule(snapshots, all_dates):
    """Build complete daily weight + leverage arrays.

    Pre-snapshot period (Mar 2025 - Jan 2026): fallback interpolation.
    Snapshot period (Jan 8 - Mar 12, 2026): actual daily data, interpolated between gaps.
    Post-snapshot: hold last value.
    """
    dates_dt = pd.to_datetime(all_dates, format='mixed')
    dates_int = dates_dt.astype(np.int64)

    # Fallback interpolation for pre-snapshot
    fb_dates = pd.to_datetime([d for d, *_ in WEIGHT_SCHEDULE])
    fb_int = fb_dates.astype(np.int64)
    lev_fb_dates = pd.to_datetime([d for d, _ in LEVERAGE_SCHEDULE_FALLBACK])
    lev_fb_int = lev_fb_dates.astype(np.int64)
    lev_fb_vals = [v for _, v in LEVERAGE_SCHEDULE_FALLBACK]

    equities = np.interp(dates_int, fb_int, [r[1] for r in WEIGHT_SCHEDULE])
    bonds = np.interp(dates_int, fb_int, [r[2] for r in WEIGHT_SCHEDULE])
    tips = np.interp(dates_int, fb_int, [r[3] for r in WEIGHT_SCHEDULE])
    commodities = np.interp(dates_int, fb_int, [r[4] for r in WEIGHT_SCHEDULE])
    leverage = np.interp(dates_int, lev_fb_int, lev_fb_vals)

    # Clamp before first date
    for arr, col_idx in [(equities, 1), (bonds, 2), (tips, 3), (commodities, 4)]:
        arr[dates_dt < fb_dates[0]] = WEIGHT_SCHEDULE[0][col_idx]
    leverage[dates_dt < lev_fb_dates[0]] = lev_fb_vals[0]

    # Overlay snapshot data from Jan 2026 onward
    if snapshots:
        snap_dates = pd.to_datetime([s['date'] for s in snapshots])
        snap_int = snap_dates.astype(np.int64)

        snap_eq = np.array([s['equities'] for s in snapshots])
        snap_bonds = np.array([s['bonds'] for s in snapshots])
        snap_tips = np.array([s['tips'] for s in snapshots])
        snap_commod = np.array([s['commodities'] for s in snapshots])
        snap_lev = np.array([s['leverage'] for s in snapshots])

        # Replace from first snapshot onward
        mask = dates_dt >= snap_dates[0]
        if mask.any():
            mi = dates_int[mask]
            equities[mask] = np.interp(mi, snap_int, snap_eq)
            bonds[mask] = np.interp(mi, snap_int, snap_bonds)
            tips[mask] = np.interp(mi, snap_int, snap_tips)
            commodities[mask] = np.interp(mi, snap_int, snap_commod)
            leverage[mask] = np.interp(mi, snap_int, snap_lev)

            # After last snapshot, hold constant
            after = dates_dt > snap_dates[-1]
            equities[after] = snap_eq[-1]
            bonds[after] = snap_bonds[-1]
            tips[after] = snap_tips[-1]
            commodities[after] = snap_commod[-1]
            leverage[after] = snap_lev[-1]

    # Sub-weights for 11-ETF (interpolated between snapshots, defaults before)
    sub_keys = ['eq_us', 'eq_europe', 'eq_japan', 'eq_em', 'eq_china',
                'bond_tlt', 'bond_ief', 'bond_bndx',
                'commod_gld', 'commod_gsg']

    defaults = {**{f'eq_{k}': v for k, v in DEFAULT_EQ_SUBS.items()},
                **{f'bond_{k}': v for k, v in DEFAULT_BOND_SUBS.items()},
                **{f'commod_{k}': v for k, v in DEFAULT_COMMOD_SUBS.items()}}

    sub_weights = {}
    if snapshots:
        snap_dates_loc = pd.to_datetime([s['date'] for s in snapshots])
        snap_int_loc = snap_dates_loc.astype(np.int64)

        for key in sub_keys:
            vals = np.array([s.get(key, defaults.get(key, 0)) for s in snapshots])
            arr = np.full(len(dates_dt), defaults.get(key, 0))
            # Before snapshots: use default
            # From first snapshot onward: interpolate
            mask = dates_dt >= snap_dates_loc[0]
            if mask.any():
                arr[mask] = np.interp(dates_int[mask], snap_int_loc, vals)
                after = dates_dt > snap_dates_loc[-1]
                arr[after] = vals[-1]
            sub_weights[key] = arr
    else:
        for key in sub_keys:
            sub_weights[key] = np.full(len(dates_dt), defaults.get(key, 0))

    return {
        'equities': equities,
        'bonds': bonds,
        'tips': tips,
        'commodities': commodities,
        'leverage': leverage,
        'sub_weights': sub_weights,
    }


# ---------------------------------------------------------------------------
# Price data
# ---------------------------------------------------------------------------

def get_prices(tickers, start_date='2025-03-01'):
    """Get prices from wide and narrow tables."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("PRAGMA table_info(stock_prices_daily)")
    wide_cols = {row[1] for row in cursor.fetchall()}

    try:
        narrow_tickers = {r[0] for r in cursor.execute(
            "SELECT DISTINCT Ticker FROM prices_long").fetchall()}
    except sqlite3.OperationalError:
        narrow_tickers = set()

    wide_tickers = [t for t in tickers if t in wide_cols]
    narrow_only = [t for t in tickers if t not in wide_cols and t in narrow_tickers]

    if wide_tickers:
        cols = ', '.join([f'"{t}"' for t in wide_tickers])
        df = pd.read_sql_query(
            f'SELECT Date, {cols} FROM stock_prices_daily WHERE Date >= ? ORDER BY Date',
            conn, params=(start_date,))
    else:
        df = pd.read_sql_query(
            f'SELECT DISTINCT Date FROM stock_prices_daily WHERE Date >= ? ORDER BY Date',
            conn, params=(start_date,))

    if narrow_only:
        ph = ','.join(['?'] * len(narrow_only))
        ndf = pd.read_sql_query(
            f'SELECT Date, Ticker, Close FROM prices_long '
            f'WHERE Ticker IN ({ph}) AND Date >= ? ORDER BY Date',
            conn, params=narrow_only + [start_date])
        if not ndf.empty:
            pivot = ndf.pivot(index='Date', columns='Ticker', values='Close').reset_index()
            df = df.merge(pivot, on='Date', how='left')

    conn.close()
    return df


def get_allw_prices():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query(
        'SELECT Date, "ALLW" as price FROM stock_prices_daily '
        'WHERE Date >= \'2025-03-01\' AND "ALLW" IS NOT NULL ORDER BY Date', conn)
    conn.close()
    return df


def compute_returns(prices_df, tickers):
    returns = {}
    for t in tickers:
        if t not in prices_df.columns:
            print(f"  Warning: {t} not in price data")
            continue
        p = prices_df[t].values
        r = np.zeros(len(p))
        for i in range(1, len(p)):
            if pd.notna(p[i]) and pd.notna(p[i-1]) and p[i-1] != 0:
                r[i] = (p[i] - p[i-1]) / p[i-1]
        returns[t] = r
    return returns


# ---------------------------------------------------------------------------
# Replication builders
# ---------------------------------------------------------------------------

def build_4etf(dates, returns, schedule, initial_price):
    """4-ETF replication: SPY=equity, TLT=bonds, TIP=tips, GLD=commodities."""
    daily_fin = FINANCING_RATE / 252
    n = len(dates)

    base_idx = 0
    for i, d in enumerate(dates):
        if str(d)[:10] >= BASE_DATE:
            base_idx = i
            break

    port_ret = np.zeros(n)
    mapping = [('SPY', 'equities'), ('TLT', 'bonds'), ('TIP', 'tips'), ('GLD', 'commodities')]
    for i in range(n):
        r = sum(schedule[key][i] * returns.get(ticker, np.zeros(n))[i]
                for ticker, key in mapping)
        lev = schedule['leverage'][i]
        port_ret[i] = lev * r - (lev - 1) * daily_fin

    vals = np.zeros(n)
    vals[base_idx] = initial_price
    for i in range(base_idx + 1, n):
        vals[i] = vals[i-1] * (1 + port_ret[i])
    for i in range(base_idx - 1, -1, -1):
        vals[i] = vals[i+1] / (1 + port_ret[i+1])
    return vals


def build_11etf(dates, returns, schedule, initial_price):
    """11-ETF replication with daily sub-weights."""
    daily_fin = FINANCING_RATE / 252
    n = len(dates)
    sub = schedule['sub_weights']

    base_idx = 0
    for i, d in enumerate(dates):
        if str(d)[:10] >= BASE_DATE:
            base_idx = i
            break

    eq_map = [('SPLG', 'eq_us'), ('VGK', 'eq_europe'), ('EWJ', 'eq_japan'),
              ('SPEM', 'eq_em'), ('GXC', 'eq_china')]
    bond_map = [('TLT', 'bond_tlt'), ('IEF', 'bond_ief'), ('BNDX', 'bond_bndx')]
    commod_map = [('GLD', 'commod_gld'), ('GSG', 'commod_gsg')]

    port_ret = np.zeros(n)
    for i in range(n):
        eq_w = schedule['equities'][i]
        bond_w = schedule['bonds'][i]
        tips_w = schedule['tips'][i]
        commod_w = schedule['commodities'][i]

        r = 0.0
        for ticker, key in eq_map:
            if ticker in returns:
                r += eq_w * sub[key][i] * returns[ticker][i]
        for ticker, key in bond_map:
            if ticker in returns:
                r += bond_w * sub[key][i] * returns[ticker][i]
        if 'TIP' in returns:
            r += tips_w * returns['TIP'][i]
        for ticker, key in commod_map:
            if ticker in returns:
                r += commod_w * sub[key][i] * returns[ticker][i]

        lev = schedule['leverage'][i]
        port_ret[i] = lev * r - (lev - 1) * daily_fin

    vals = np.zeros(n)
    vals[base_idx] = initial_price
    for i in range(base_idx + 1, n):
        vals[i] = vals[i-1] * (1 + port_ret[i])
    for i in range(base_idx - 1, -1, -1):
        vals[i] = vals[i+1] / (1 + port_ret[i+1])
    return vals


# ---------------------------------------------------------------------------
# Storage
# ---------------------------------------------------------------------------

def store_ticker(df, ticker, name):
    df_n = df[['Date', ticker]].rename(columns={ticker: 'Close'}).copy()
    df_n['Ticker'] = ticker

    conn = sqlite3.connect(DB_PATH, timeout=30)
    try:
        rows = list(zip(df_n['Date'], df_n['Ticker'], df_n['Close']))
        conn.executemany(
            'INSERT OR REPLACE INTO prices_long (Date, Ticker, Close) VALUES (?, ?, ?)', rows)
        conn.commit()
        print(f"  {ticker}: upserted {len(rows):,} rows")
    finally:
        conn.close()

    conn = sqlite3.connect(DB_PATH, timeout=30)
    conn.execute('''INSERT OR REPLACE INTO ticker_metadata
        (ticker, name, table_name, data_type, first_date, last_date, data_points)
        VALUES (?, ?, 'prices_long', 'index', ?, ?, ?)''',
        (ticker, name, df['Date'].min(), df['Date'].max(), len(df)))
    conn.commit()
    conn.close()


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    store = '--store' in sys.argv

    print(f"\n{'='*60}")
    print("ALLW Daily-Weight Replication")
    print(f"{'='*60}\n")

    # Parse vault snapshots
    print("Parsing Risk Parity vault snapshots...")
    snapshots = parse_all_snapshots()
    print(f"  {len(snapshots)} snapshots: {snapshots[0]['date']} to {snapshots[-1]['date']}")

    print(f"\n  Sample allocations:")
    for s in [snapshots[0], snapshots[len(snapshots)//2], snapshots[-1]]:
        print(f"    {s['date']}: eq={s['equities']*100:.1f}% bonds={s['bonds']*100:.1f}% "
              f"tips={s['tips']*100:.1f}% commod={s['commodities']*100:.1f}% lev={s['leverage']:.2f}x")
        print(f"      Eq: US={s.get('eq_us',0)*100:.0f}% EU={s.get('eq_europe',0)*100:.0f}% "
              f"JP={s.get('eq_japan',0)*100:.0f}% EM={s.get('eq_em',0)*100:.0f}% "
              f"CN={s.get('eq_china',0)*100:.0f}%")
        print(f"      Bond: TLT={s.get('bond_tlt',0)*100:.0f}% IEF={s.get('bond_ief',0)*100:.0f}% "
              f"BNDX={s.get('bond_bndx',0)*100:.0f}%")
        print(f"      Commod: GLD={s.get('commod_gld',0)*100:.0f}% GSG={s.get('commod_gsg',0)*100:.0f}%")

    # Load prices
    all_tickers = list(set(TICKERS_4ETF + TICKERS_11ETF))
    print(f"\nLoading prices for {len(all_tickers)} tickers...")
    prices_df = get_prices(all_tickers)
    print(f"  {len(prices_df)} trading days")

    # Filter to ALLW period
    mask = prices_df['Date'] >= BASE_DATE
    dates = prices_df.loc[mask, 'Date'].values
    prices_filtered = prices_df.loc[mask].reset_index(drop=True)

    # Build daily schedule
    schedule = build_daily_schedule(snapshots, dates)

    # Returns
    returns_4 = compute_returns(prices_filtered, TICKERS_4ETF)
    returns_11 = compute_returns(prices_filtered, TICKERS_11ETF)

    # ALLW price anchor
    allw_df = get_allw_prices()
    allw_df['Date'] = allw_df['Date'].astype(str).str[:10]
    allw_base = allw_df.loc[allw_df['Date'] >= BASE_DATE[:10], 'price']
    initial_price = float(allw_base.iloc[0]) if not allw_base.empty else 25.0

    # Build replications
    vals_4 = build_4etf(dates, returns_4, schedule, initial_price)
    vals_11 = build_11etf(dates, returns_11, schedule, initial_price)

    result_df = pd.DataFrame({
        'Date': dates,
        'ALLW_REPL_DAILY': vals_4,
        'ALLW_11ETF_DAILY': vals_11,
    })
    result_df = result_df[result_df['ALLW_REPL_DAILY'] > 0]

    # Performance
    d4_ret = (result_df['ALLW_REPL_DAILY'].iloc[-1] / result_df['ALLW_REPL_DAILY'].iloc[0] - 1) * 100
    d11_ret = (result_df['ALLW_11ETF_DAILY'].iloc[-1] / result_df['ALLW_11ETF_DAILY'].iloc[0] - 1) * 100
    allw_ret = (float(allw_base.iloc[-1]) / float(allw_base.iloc[0]) - 1) * 100 if not allw_base.empty else 0

    print(f"\n{'='*60}")
    print(f"  ALLW actual:              {allw_ret:+.2f}%")
    print(f"  ALLW_REPL_DAILY (4-ETF):  {d4_ret:+.2f}%  (daily weights)")
    print(f"  ALLW_11ETF_DAILY (11-ETF): {d11_ret:+.2f}%  (daily sub-weights)")
    print(f"  ---")
    print(f"  Prior 4-ETF DYN (5-pt):   +8.21%")
    print(f"  Prior 11-ETF DYN (5-pt):  +6.82%")
    print(f"  ---")
    print(f"  4-ETF improvement:        {d4_ret - 8.21:+.2f}pp  vs 5-point interpolation")
    print(f"  11-ETF improvement:       {d11_ret - 6.82:+.2f}pp  vs 5-point interpolation")
    print(f"  ---")
    print(f"  Residual (4-ETF):         {allw_ret - d4_ret:+.2f}pp")
    print(f"  Residual (11-ETF):        {allw_ret - d11_ret:+.2f}pp")
    print(f"{'='*60}")

    if store:
        store_ticker(result_df, 'ALLW_REPL_DAILY', 'ALLW 4-ETF Daily-Weight Replication')
        store_ticker(result_df, 'ALLW_11ETF_DAILY', 'ALLW 11-ETF Daily-Weight Replication')
        print(f"\n[DONE] Chart: /api/chart/lw?tickers=ALLW,ALLW_REPL_DAILY,ALLW_REPL_DYN"
              f"&start=2025-03-06&normalize=true&primary=ALLW"
              f"&labels=ALLW_REPL_DAILY:4-ETF%20Daily,ALLW_REPL_DYN:4-ETF%205-Point")
    else:
        print(f"\nRun with --store to save to database")


if __name__ == '__main__':
    main()
