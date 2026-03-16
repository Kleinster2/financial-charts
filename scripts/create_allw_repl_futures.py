#!/usr/bin/env python3
"""
create_allw_repl_futures.py

ALLW replication using direct futures proxies instead of US-listed ETFs.

The key insight: ALLW holds currency-unhedged international bond futures.
Using BNDX (USD-hedged) misses the FX component entirely. This script uses:

  Equity:  STOXX50E + FTSE + AXJO + N225 indices (not VGK/EWJ)
           Plus SPYM(SPLG), SPEM, GXC as before (actual ETF holdings)
  Bonds:   IBGL_L (EUR govt bonds) + IGLT_L (UK gilts) + VGB_AX (AUS bonds)
           Converted to USD returns using FX pairs (unhedged, like ALLW)
           Plus ZN=F, ZB=F for US bonds (actual futures in our DB)
  TIPS:    TIP (same as before)
  Commod:  GC=F (gold futures) + GSG (BCOMTR proxy)

Produces:
  ALLW_FUTURES   -- futures-proxy replication with daily weights + leverage

Usage:
    python scripts/create_allw_repl_futures.py [--store]
"""

import sys
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

# Import snapshot parsing from daily script
sys.path.insert(0, str(Path(__file__).parent))
from create_allw_repl_daily import (
    parse_all_snapshots, build_daily_schedule,
    WEIGHT_SCHEDULE, LEVERAGE_SCHEDULE_FALLBACK
)

# ---------------------------------------------------------------------------
# Ticker mapping: ALLW holding -> DB proxy
# ---------------------------------------------------------------------------

# Equity: mix of actual ETF holdings + index proxies for futures
# Sub-weights from daily snapshots (eq_us, eq_europe, eq_japan, eq_em, eq_china)
EQUITY_MAP = {
    'eq_us':     'SPLG',      # SPYM/SPLG — actual holding
    'eq_europe': 'STOXX50E',  # EURO STOXX 50 index (was VGK)
    'eq_japan':  'N225',      # Nikkei 225 index (was EWJ, TOPIX unavailable)
    'eq_em':     'SPEM',      # actual holding
    'eq_china':  'GXC',       # actual holding
}

# Europe equity includes FTSE + SPI (Australia) — weight these within eq_europe
# From Mar 12 snapshot: STOXX=105.4, FTSE=44.9, SPI=42.3 -> STOXX=55%, FTSE=23%, SPI=22%
EUROPE_SUBS = {
    'STOXX50E': 0.55,
    'FTSE':     0.23,
    'AXJO':     0.22,  # Australia equity lumped with Europe (same as VGK approach)
}

# Bonds: local-currency ETFs + FX for unhedged USD return
# Sub-weights from daily snapshots (bond_tlt, bond_ief, bond_bndx)
# bond_bndx gets split into Bund/Gilt/Aust using notional weights
# From Mar 12: Bund=199.2, Gilt=67.5, Aust=104.7 -> Bund=54%, Gilt=18%, Aust=28%
BOND_US_MAP = {
    'bond_tlt': 'ZB=F',   # US Long Bond futures (was TLT)
    'bond_ief': 'ZN=F',   # US 10Y Note futures (was IEF)
}

BOND_INTL_SUBS = {
    # (local bond ETF, FX pair for USD conversion)
    'bund': ('IBGL_L', 'EURUSD=X', 0.54),
    'gilt': ('IGLT_L', 'GBPUSD=X', 0.18),
    'aust': ('VGB_AX', 'AUDUSD=X', 0.28),
}

# Commodities
COMMOD_MAP = {
    'commod_gld': 'GC=F',   # Gold futures (was GLD)
    'commod_gsg': 'GSG',    # BCOMTR proxy (no futures available)
}

# All tickers we need
ALL_TICKERS = (
    ['SPLG', 'SPEM', 'GXC']  # Equity ETFs (actual holdings)
    + list(EUROPE_SUBS.keys())  # Equity indices
    + ['N225']  # Japan index
    + ['ZB=F', 'ZN=F']  # US bond futures
    + ['IBGL_L', 'IGLT_L', 'VGB_AX']  # International bond ETFs
    + ['EURUSD=X', 'GBPUSD=X', 'AUDUSD=X']  # FX pairs
    + ['TIP']  # TIPS
    + ['GC=F', 'GSG']  # Commodities
)


def get_prices():
    """Get all prices from wide + narrow + futures tables."""
    conn = sqlite3.connect(str(DB_PATH))

    # Wide table columns
    cursor = conn.cursor()
    cursor.execute("PRAGMA table_info(stock_prices_daily)")
    wide_cols = {row[1] for row in cursor.fetchall()}

    # Narrow table tickers
    try:
        narrow_tickers = {r[0] for r in cursor.execute(
            "SELECT DISTINCT Ticker FROM prices_long").fetchall()}
    except sqlite3.OperationalError:
        narrow_tickers = set()

    # Futures table tickers
    try:
        futures_tickers = {r[0] for r in cursor.execute(
            "SELECT DISTINCT Ticker FROM futures_prices_long").fetchall()}
    except sqlite3.OperationalError:
        futures_tickers = set()

    start = '2025-01-01'

    # Start with dates from wide table
    df = pd.read_sql_query(
        "SELECT DISTINCT Date FROM stock_prices_daily WHERE Date >= ? ORDER BY Date",
        conn, params=(start,))

    # Add wide-format tickers
    wide_need = [t for t in ALL_TICKERS if t in wide_cols]
    if wide_need:
        cols = ', '.join([f'"{t}"' for t in wide_need])
        wdf = pd.read_sql_query(
            f'SELECT Date, {cols} FROM stock_prices_daily WHERE Date >= ? ORDER BY Date',
            conn, params=(start,))
        df = df.merge(wdf, on='Date', how='left')

    # Add narrow-format tickers
    narrow_need = [t for t in ALL_TICKERS if t not in wide_cols and t in narrow_tickers]
    if narrow_need:
        ph = ','.join(['?'] * len(narrow_need))
        ndf = pd.read_sql_query(
            f'SELECT Date, Ticker, Close FROM prices_long '
            f'WHERE Ticker IN ({ph}) AND Date >= ? ORDER BY Date',
            conn, params=narrow_need + [start])
        if not ndf.empty:
            pivot = ndf.pivot(index='Date', columns='Ticker', values='Close').reset_index()
            df = df.merge(pivot, on='Date', how='left')

    # Add futures tickers
    fut_need = [t for t in ALL_TICKERS if t not in wide_cols and t not in narrow_tickers
                and t in futures_tickers]
    if fut_need:
        ph = ','.join(['?'] * len(fut_need))
        fdf = pd.read_sql_query(
            f'SELECT Date, Ticker, Close FROM futures_prices_long '
            f'WHERE Ticker IN ({ph}) AND Date >= ? ORDER BY Date',
            conn, params=fut_need + [start])
        if not fdf.empty:
            pivot = fdf.pivot(index='Date', columns='Ticker', values='Close').reset_index()
            df = df.merge(pivot, on='Date', how='left')

    conn.close()
    return df


def compute_returns(prices_df, tickers):
    """Compute daily returns."""
    returns = {}
    for t in tickers:
        if t not in prices_df.columns:
            print(f"  Warning: {t} not in data")
            continue
        p = prices_df[t].values
        r = np.zeros(len(p))
        for i in range(1, len(p)):
            if pd.notna(p[i]) and pd.notna(p[i-1]) and p[i-1] != 0:
                r[i] = (p[i] - p[i-1]) / p[i-1]
        returns[t] = r
    return returns


def compute_unhedged_bond_returns(returns, fx_returns):
    """Compute USD returns for local-currency bonds.

    USD return = local bond return + FX return (approx for small daily changes).
    This replicates what holding an unhedged bond future gives you.
    """
    unhedged = {}
    for name, (bond_ticker, fx_ticker, _) in BOND_INTL_SUBS.items():
        if bond_ticker in returns and fx_ticker in returns:
            # Unhedged USD return ≈ local return + FX return
            unhedged[name] = returns[bond_ticker] + returns[fx_ticker]
        else:
            print(f"  Warning: missing {bond_ticker} or {fx_ticker} for {name}")
            unhedged[name] = np.zeros(len(next(iter(returns.values()))))
    return unhedged


def build_futures_repl(dates, returns, unhedged_bonds, schedule, initial_price):
    """Build futures-proxy replication."""
    daily_fin = FINANCING_RATE / 252
    n = len(dates)
    sub = schedule['sub_weights']

    base_idx = 0
    for i, d in enumerate(dates):
        if str(d)[:10] >= BASE_DATE:
            base_idx = i
            break

    port_ret = np.zeros(n)
    for i in range(n):
        eq_w = schedule['equities'][i]
        bond_w = schedule['bonds'][i]
        tips_w = schedule['tips'][i]
        commod_w = schedule['commodities'][i]

        r = 0.0

        # --- Equity ---
        # US: SPLG
        if 'SPLG' in returns:
            r += eq_w * sub['eq_us'][i] * returns['SPLG'][i]

        # Europe: weighted blend of STOXX50E, FTSE, AXJO
        europe_r = 0.0
        for idx_ticker, idx_wt in EUROPE_SUBS.items():
            if idx_ticker in returns:
                europe_r += idx_wt * returns[idx_ticker][i]
        r += eq_w * sub['eq_europe'][i] * europe_r

        # Japan: N225
        if 'N225' in returns:
            r += eq_w * sub['eq_japan'][i] * returns['N225'][i]

        # EM + China: actual ETFs
        if 'SPEM' in returns:
            r += eq_w * sub['eq_em'][i] * returns['SPEM'][i]
        if 'GXC' in returns:
            r += eq_w * sub['eq_china'][i] * returns['GXC'][i]

        # --- Bonds ---
        # US: actual futures
        if 'ZB=F' in returns:
            r += bond_w * sub['bond_tlt'][i] * returns['ZB=F'][i]
        if 'ZN=F' in returns:
            r += bond_w * sub['bond_ief'][i] * returns['ZN=F'][i]

        # International: unhedged local bonds
        bndx_w = sub['bond_bndx'][i]
        for name, (_, _, sub_wt) in BOND_INTL_SUBS.items():
            if name in unhedged_bonds:
                r += bond_w * bndx_w * sub_wt * unhedged_bonds[name][i]

        # --- TIPS ---
        if 'TIP' in returns:
            r += tips_w * returns['TIP'][i]

        # --- Commodities ---
        if 'GC=F' in returns:
            r += commod_w * sub['commod_gld'][i] * returns['GC=F'][i]
        if 'GSG' in returns:
            r += commod_w * sub['commod_gsg'][i] * returns['GSG'][i]

        lev = schedule['leverage'][i]
        port_ret[i] = lev * r - (lev - 1) * daily_fin

    vals = np.zeros(n)
    vals[base_idx] = initial_price
    for i in range(base_idx + 1, n):
        vals[i] = vals[i-1] * (1 + port_ret[i])
    for i in range(base_idx - 1, -1, -1):
        vals[i] = vals[i+1] / (1 + port_ret[i+1])
    return vals


def store_ticker(df, ticker, name):
    df_n = df[['Date', ticker]].rename(columns={ticker: 'Close'}).copy()
    df_n['Ticker'] = ticker

    conn = sqlite3.connect(str(DB_PATH), timeout=30)
    try:
        rows = list(zip(df_n['Date'], df_n['Ticker'], df_n['Close']))
        conn.executemany(
            'INSERT OR REPLACE INTO prices_long (Date, Ticker, Close) VALUES (?, ?, ?)', rows)
        conn.commit()
        print(f"  {ticker}: upserted {len(rows):,} rows")
    finally:
        conn.close()

    conn = sqlite3.connect(str(DB_PATH), timeout=30)
    conn.execute('''INSERT OR REPLACE INTO ticker_metadata
        (ticker, name, table_name, data_type, first_date, last_date, data_points)
        VALUES (?, ?, 'prices_long', 'index', ?, ?, ?)''',
        (ticker, name, df['Date'].min(), df['Date'].max(), len(df)))
    conn.commit()
    conn.close()


def main():
    store = '--store' in sys.argv

    print(f"\n{'='*60}")
    print("ALLW Futures-Proxy Replication")
    print(f"{'='*60}\n")

    # Parse daily snapshots
    print("Parsing vault snapshots...")
    snapshots = parse_all_snapshots()
    print(f"  {len(snapshots)} snapshots")

    # Load prices
    print(f"\nLoading prices for {len(ALL_TICKERS)} tickers...")
    prices_df = get_prices()
    print(f"  {len(prices_df)} trading days")

    # Check coverage
    print(f"\n  Ticker coverage:")
    for t in ALL_TICKERS:
        if t in prices_df.columns:
            non_null = prices_df[t].notna().sum()
            print(f"    {t:12s} {non_null:4d} days")
        else:
            print(f"    {t:12s} MISSING")

    # Filter to ALLW period
    mask = prices_df['Date'] >= BASE_DATE
    dates = prices_df.loc[mask, 'Date'].values
    pf = prices_df.loc[mask].reset_index(drop=True)

    # Build schedule
    schedule = build_daily_schedule(snapshots, dates)

    # Compute returns
    all_need = list(set(ALL_TICKERS))
    returns = compute_returns(pf, all_need)

    # FX-adjusted international bond returns
    fx_returns = {t: returns[t] for t in ['EURUSD=X', 'GBPUSD=X', 'AUDUSD=X'] if t in returns}
    unhedged_bonds = compute_unhedged_bond_returns(returns, fx_returns)

    # ALLW anchor price
    conn = sqlite3.connect(str(DB_PATH))
    allw_df = pd.read_sql_query(
        'SELECT Date, "ALLW" as price FROM stock_prices_daily '
        'WHERE Date >= \'2025-03-01\' AND "ALLW" IS NOT NULL ORDER BY Date', conn)
    conn.close()
    allw_df['Date'] = allw_df['Date'].astype(str).str[:10]
    allw_base = allw_df.loc[allw_df['Date'] >= BASE_DATE[:10], 'price']
    initial_price = float(allw_base.iloc[0]) if not allw_base.empty else 25.0

    # Build replication
    vals = build_futures_repl(dates, returns, unhedged_bonds, schedule, initial_price)

    result_df = pd.DataFrame({'Date': dates, 'ALLW_FUTURES': vals})
    result_df = result_df[result_df['ALLW_FUTURES'] > 0]

    # Performance
    f_ret = (result_df['ALLW_FUTURES'].iloc[-1] / result_df['ALLW_FUTURES'].iloc[0] - 1) * 100
    allw_ret = (float(allw_base.iloc[-1]) / float(allw_base.iloc[0]) - 1) * 100

    print(f"\n{'='*60}")
    print(f"  ALLW actual:              {allw_ret:+.2f}%")
    print(f"  ALLW_FUTURES:             {f_ret:+.2f}%  (futures-proxy + daily wts)")
    print(f"  ---")
    print(f"  Prior best (4-ETF Daily): +8.54%")
    print(f"  Prior best (11-ETF Daily):+7.24%")
    print(f"  ---")
    print(f"  Improvement vs 4-ETF:     {f_ret - 8.54:+.2f}pp")
    print(f"  Residual:                 {allw_ret - f_ret:+.2f}pp")
    print(f"{'='*60}")

    if store:
        store_ticker(result_df, 'ALLW_FUTURES',
                     'ALLW Futures-Proxy Replication (indices + unhedged bonds + daily wts)')
        print(f"\n[DONE] Chart: /api/chart/lw?tickers=ALLW,ALLW_FUTURES,ALLW_REPL_DAILY"
              f"&start=2025-03-06&normalize=true&primary=ALLW"
              f"&labels=ALLW_FUTURES:Futures%20Proxy,ALLW_REPL_DAILY:4-ETF%20Daily")
    else:
        print(f"\nRun with --store to save to database")


if __name__ == '__main__':
    main()
