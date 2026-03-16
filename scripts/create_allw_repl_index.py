#!/usr/bin/env python3
"""
create_allw_repl_index.py

Create ALLW Replication synthetic indices:
  ALLW_REPL  — 1x (unleveraged) 4-ETF replication
  ALLW_REPL_LEV — levered replication matching ALLW's actual leverage schedule

Components (deleveraged weights, Mar 2026 allocation):
  SPY  27.1%  (equities)
  TLT  42.9%  (nominal bonds)
  TIP  21.5%  (TIPS)
  GLD   8.5%  (commodities)

Leverage schedule interpolated from ALLW holdings snapshots:
  Mar 2025: 0.78x → May: 1.00x → Aug: 1.23x → Dec: 1.60x → Mar 2026: 1.71x

Financing cost: ~4.8% annualized (approximates SOFR over the period).
Residual gap between ALLW_REPL_LEV and ALLW = Bridgewater model alpha.

Usage:
    python scripts/create_allw_repl_index.py [--store]
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
sys.path.insert(0, str(Path(__file__).parent.parent / 'charting_app'))
try:
    from sqlite_queries import upsert_prices_long, check_narrow_available
    NARROW_SYNC = check_narrow_available()
except ImportError:
    NARROW_SYNC = False

import sqlite3
import pandas as pd
import numpy as np

DB_PATH = Path(__file__).parent.parent / 'market_data.db'

# Deleveraged weights from ALLW March 11, 2026 allocation
ALLW_REPL_WEIGHTS = {
    'SPY': 0.271,   # Equities
    'TLT': 0.429,   # Nominal bonds
    'TIP': 0.215,   # TIPS
    'GLD': 0.085,   # Commodities (gold-heavy proxy)
}

# Base date = ALLW inception
BASE_DATE = '2025-03-06'

# Known leverage snapshots from ALLW holdings data
LEVERAGE_SCHEDULE = [
    ('2025-03-06', 0.78),
    ('2025-05-15', 1.00),
    ('2025-08-05', 1.23),
    ('2025-12-15', 1.60),
    ('2026-03-11', 1.71),
]

# Approximate financing rate (annualized) — SOFR averaged ~4.8% over the period
FINANCING_RATE = 0.048

# Time-varying deleveraged weight snapshots (date, SPY, TLT, TIP, GLD)
# From ALLW allocation evolution table
WEIGHT_SCHEDULE = [
    # date,         equity, bonds,  TIPS,   commodities
    ('2025-03-06',  0.250,  0.475,  0.194,  0.081),
    ('2025-05-15',  0.432,  0.344,  0.157,  0.067),
    ('2025-08-05',  0.539,  0.280,  0.131,  0.051),
    ('2025-12-15',  0.269,  0.452,  0.215,  0.064),
    ('2026-03-11',  0.271,  0.429,  0.215,  0.085),
]


def get_component_prices(start_date: str = '2025-03-01'):
    """Get historical prices for component tickers."""
    conn = sqlite3.connect(DB_PATH)

    tickers = list(ALLW_REPL_WEIGHTS.keys())
    ticker_cols = ', '.join([f'"{t}"' for t in tickers])

    query = f"""
        SELECT Date, {ticker_cols}
        FROM stock_prices_daily
        WHERE Date >= ?
        ORDER BY Date ASC
    """

    df = pd.read_sql_query(query, conn, params=(start_date,))
    conn.close()

    return df


def get_allw_prices(start_date: str = '2025-03-01'):
    """Get ALLW prices for comparison."""
    conn = sqlite3.connect(DB_PATH)
    query = """
        SELECT Date, "ALLW" as price
        FROM stock_prices_daily
        WHERE Date >= ? AND "ALLW" IS NOT NULL
        ORDER BY Date ASC
    """
    df = pd.read_sql_query(query, conn, params=(start_date,))
    conn.close()
    return df


def calculate_allw_repl():
    """Calculate ALLW_REPL synthetic index."""

    print(f"\n{'='*70}")
    print("ALLW Replication Index (ALLW_REPL)")
    print(f"{'='*70}\n")

    print("Components (deleveraged weights, Mar 2026):")
    for ticker, weight in ALLW_REPL_WEIGHTS.items():
        print(f"  {ticker:6s} {weight*100:5.1f}%")
    print(f"\n  Total: {sum(ALLW_REPL_WEIGHTS.values())*100:.0f}%")
    print(f"\nBase date: {BASE_DATE} (ALLW inception)")

    # Get prices
    prices_df = get_component_prices()

    if prices_df.empty:
        print("Error: No price data found")
        return None

    print(f"\nPrice data: {len(prices_df)} days")

    # Calculate daily returns for each component
    tickers = list(ALLW_REPL_WEIGHTS.keys())
    returns_data = {'Date': prices_df['Date'].values}

    for ticker in tickers:
        if ticker in prices_df.columns:
            prices = prices_df[ticker].values
            returns = np.zeros(len(prices))
            for i in range(1, len(prices)):
                if pd.notna(prices[i]) and pd.notna(prices[i-1]) and prices[i-1] != 0:
                    returns[i] = (prices[i] - prices[i-1]) / prices[i-1]
            returns_data[ticker] = returns
        else:
            print(f"  Warning: {ticker} not in price data")

    returns_df = pd.DataFrame(returns_data)

    # Weighted portfolio return
    portfolio_returns = np.zeros(len(returns_df))
    for ticker, weight in ALLW_REPL_WEIGHTS.items():
        if ticker in returns_df.columns:
            portfolio_returns += returns_df[ticker].values * weight

    # Find base date index
    dates = returns_df['Date'].values
    base_idx = None
    for i, d in enumerate(dates):
        if str(d)[:10] >= BASE_DATE:
            base_idx = i
            break

    if base_idx is None:
        print(f"Warning: Base date {BASE_DATE} not found, using first date")
        base_idx = 0

    # Get ALLW's actual price on base date to anchor the synthetic
    allw_df = get_allw_prices()
    if allw_df.empty:
        print("Error: No ALLW price data")
        return None

    allw_df['Date'] = allw_df['Date'].astype(str).str[:10]

    # Find ALLW's price on base date
    base_mask = allw_df['Date'] >= BASE_DATE[:10]
    if base_mask.any():
        initial_allw_price = float(allw_df.loc[base_mask, 'price'].iloc[0])
    else:
        initial_allw_price = 25.0  # ALLW launched at ~$25

    print(f"\nALLW price on base date: ${initial_allw_price:.2f}")

    # Build index anchored to ALLW's inception price
    portfolio_value = np.zeros(len(portfolio_returns))
    portfolio_value[base_idx] = initial_allw_price

    # Forward
    for i in range(base_idx + 1, len(portfolio_returns)):
        portfolio_value[i] = portfolio_value[i-1] * (1 + portfolio_returns[i])

    # Backward
    for i in range(base_idx - 1, -1, -1):
        portfolio_value[i] = portfolio_value[i+1] / (1 + portfolio_returns[i+1])

    result_df = pd.DataFrame({
        'Date': returns_df['Date'],
        'ALLW_REPL': portfolio_value
    })

    # Filter to only dates where ALLW exists
    result_df = result_df[result_df['Date'] >= BASE_DATE].copy()
    result_df = result_df[result_df['ALLW_REPL'] > 0]

    # Performance summary
    latest = result_df['ALLW_REPL'].iloc[-1]
    base = result_df['ALLW_REPL'].iloc[0]
    print(f"\nALLW_REPL:")
    print(f"  Base: ${base:.2f}")
    print(f"  Latest: ${latest:.2f}")
    print(f"  Return: {(latest/base - 1)*100:+.2f}%")

    # Compare to actual ALLW
    allw_base = allw_df.loc[allw_df['Date'] >= BASE_DATE[:10], 'price']
    if not allw_base.empty:
        allw_latest = float(allw_base.iloc[-1])
        allw_first = float(allw_base.iloc[0])
        print(f"\nALLW actual:")
        print(f"  Base: ${allw_first:.2f}")
        print(f"  Latest: ${allw_latest:.2f}")
        print(f"  Return: {(allw_latest/allw_first - 1)*100:+.2f}%")
        print(f"\nTracking difference: {(latest/base - allw_latest/allw_first)*100:+.2f}pp")

    print(f"\nRecent values:")
    for _, row in result_df.tail(5).iterrows():
        print(f"  {str(row['Date'])[:10]}: ${row['ALLW_REPL']:.2f}")

    return result_df


def interpolate_leverage(dates):
    """Linearly interpolate leverage for each trading day."""
    lev_dates = pd.to_datetime([d for d, _ in LEVERAGE_SCHEDULE])
    lev_values = [v for _, v in LEVERAGE_SCHEDULE]

    dates_dt = pd.to_datetime(dates, format='mixed')
    leverage = np.interp(
        dates_dt.astype(np.int64),
        lev_dates.astype(np.int64),
        lev_values
    )
    # Clamp: before first snapshot use first value, after last use last
    leverage[dates_dt < lev_dates[0]] = lev_values[0]
    leverage[dates_dt > lev_dates[-1]] = lev_values[-1]
    return leverage


def calculate_allw_repl_lev(unlevered_returns, dates, initial_price):
    """
    Calculate levered replication.

    Levered daily return = L_t * r_components - (L_t - 1) * r_financing
    where r_financing = FINANCING_RATE / 252
    """
    daily_financing = FINANCING_RATE / 252

    leverage = interpolate_leverage(dates)

    # Find base date index
    base_idx = None
    for i, d in enumerate(dates):
        if str(d)[:10] >= BASE_DATE:
            base_idx = i
            break
    if base_idx is None:
        base_idx = 0

    # Levered returns
    levered_returns = leverage * unlevered_returns - (leverage - 1) * daily_financing

    # Build price series
    portfolio_value = np.zeros(len(levered_returns))
    portfolio_value[base_idx] = initial_price

    for i in range(base_idx + 1, len(levered_returns)):
        portfolio_value[i] = portfolio_value[i-1] * (1 + levered_returns[i])

    for i in range(base_idx - 1, -1, -1):
        portfolio_value[i] = portfolio_value[i+1] / (1 + levered_returns[i+1])

    return portfolio_value, leverage


def interpolate_weights(dates):
    """Linearly interpolate deleveraged weights for each trading day.

    Returns dict of {proxy_ticker: np.array of weights}.
    """
    sched_dates = pd.to_datetime([d for d, *_ in WEIGHT_SCHEDULE])
    # columns: equity(SPY), bonds(TLT), TIPS(TIP), commodities(GLD)
    cols = {'SPY': 1, 'TLT': 2, 'TIP': 3, 'GLD': 4}

    dates_dt = pd.to_datetime(dates, format='mixed')
    dates_int = dates_dt.astype(np.int64)
    sched_int = sched_dates.astype(np.int64)

    weights = {}
    for ticker, col_idx in cols.items():
        values = [row[col_idx] for row in WEIGHT_SCHEDULE]
        w = np.interp(dates_int, sched_int, values)
        w[dates_dt < sched_dates[0]] = values[0]
        w[dates_dt > sched_dates[-1]] = values[-1]
        weights[ticker] = w

    return weights


def calculate_allw_repl_dyn(component_returns, dates, initial_price):
    """
    Calculate dynamic replication: time-varying weights + leverage + financing.

    This is the closest possible replication using publicly disclosed allocations.
    Residual gap = intra-period tactical moves (Bridgewater's daily model).
    """
    daily_financing = FINANCING_RATE / 252

    leverage = interpolate_leverage(dates)
    weights = interpolate_weights(dates)

    base_idx = None
    for i, d in enumerate(dates):
        if str(d)[:10] >= BASE_DATE:
            base_idx = i
            break
    if base_idx is None:
        base_idx = 0

    n = len(dates)
    portfolio_returns = np.zeros(n)

    for i in range(n):
        # Weighted unlevered return for this day using time-varying weights
        r_unlevered = 0.0
        for ticker in ['SPY', 'TLT', 'TIP', 'GLD']:
            r_unlevered += weights[ticker][i] * component_returns[ticker][i]

        # Apply leverage and financing
        portfolio_returns[i] = leverage[i] * r_unlevered - (leverage[i] - 1) * daily_financing

    # Build price series
    portfolio_value = np.zeros(n)
    portfolio_value[base_idx] = initial_price

    for i in range(base_idx + 1, n):
        portfolio_value[i] = portfolio_value[i-1] * (1 + portfolio_returns[i])

    for i in range(base_idx - 1, -1, -1):
        portfolio_value[i] = portfolio_value[i+1] / (1 + portfolio_returns[i+1])

    return portfolio_value


def store_ticker(df: pd.DataFrame, ticker: str, name: str):
    """Store a synthetic ticker in narrow-format prices_long table."""
    df_narrow = df[['Date', ticker]].rename(columns={ticker: 'Close'}).copy()
    df_narrow['Ticker'] = ticker

    conn = sqlite3.connect(DB_PATH, timeout=30)
    try:
        rows = list(zip(df_narrow['Date'], df_narrow['Ticker'], df_narrow['Close']))
        conn.executemany(
            'INSERT OR REPLACE INTO prices_long (Date, Ticker, Close) VALUES (?, ?, ?)',
            rows
        )
        conn.commit()
        print(f"  {ticker}: upserted {len(rows):,} rows into prices_long")
    finally:
        conn.close()

    conn = sqlite3.connect(DB_PATH, timeout=30)
    conn.execute('''
        INSERT OR REPLACE INTO ticker_metadata
        (ticker, name, table_name, data_type, first_date, last_date, data_points)
        VALUES (?, ?, 'prices_long', 'index', ?, ?, ?)
    ''', (ticker, name, df['Date'].min(), df['Date'].max(), len(df)))
    conn.commit()
    conn.close()

    print(f"  [SUCCESS] {ticker} stored")


def main():
    store = '--store' in sys.argv or '-s' in sys.argv

    result_df = calculate_allw_repl()

    if result_df is None:
        return

    # Calculate levered version using the same component returns
    # Re-derive the unlevered daily returns from the price series
    prices = result_df['ALLW_REPL'].values
    unlevered_returns = np.zeros(len(prices))
    for i in range(1, len(prices)):
        if prices[i-1] != 0:
            unlevered_returns[i] = (prices[i] - prices[i-1]) / prices[i-1]

    initial_price = result_df['ALLW_REPL'].iloc[0]
    lev_values, leverage_series = calculate_allw_repl_lev(
        unlevered_returns, result_df['Date'].values, initial_price
    )
    result_df['ALLW_REPL_LEV'] = lev_values

    # Performance summary for levered
    lev_latest = result_df['ALLW_REPL_LEV'].iloc[-1]
    lev_base = result_df['ALLW_REPL_LEV'].iloc[0]
    print(f"\nALLW_REPL_LEV (levered):")
    print(f"  Base: ${lev_base:.2f}")
    print(f"  Latest: ${lev_latest:.2f}")
    print(f"  Return: {(lev_latest/lev_base - 1)*100:+.2f}%")
    print(f"  Final leverage: {leverage_series[-1]:.2f}x")

    # Calculate dynamic version: time-varying weights + leverage
    # Need per-component returns (not weighted)
    prices_df = get_component_prices()
    tickers = ['SPY', 'TLT', 'TIP', 'GLD']
    comp_returns = {}
    for ticker in tickers:
        prices = prices_df[ticker].values
        returns = np.zeros(len(prices))
        for i in range(1, len(prices)):
            if pd.notna(prices[i]) and pd.notna(prices[i-1]) and prices[i-1] != 0:
                returns[i] = (prices[i] - prices[i-1]) / prices[i-1]
        comp_returns[ticker] = returns

    # Filter to match result_df date range
    all_dates = prices_df['Date'].values
    mask = prices_df['Date'] >= BASE_DATE
    filtered_dates = all_dates[mask]
    filtered_comp = {t: comp_returns[t][mask] for t in tickers}

    dyn_values = calculate_allw_repl_dyn(
        filtered_comp, filtered_dates, initial_price
    )
    result_df['ALLW_REPL_DYN'] = dyn_values[:len(result_df)]

    dyn_latest = result_df['ALLW_REPL_DYN'].iloc[-1]
    dyn_base = result_df['ALLW_REPL_DYN'].iloc[0]
    print(f"\nALLW_REPL_DYN (dynamic weights + leverage):")
    print(f"  Base: ${dyn_base:.2f}")
    print(f"  Latest: ${dyn_latest:.2f}")
    print(f"  Return: {(dyn_latest/dyn_base - 1)*100:+.2f}%")

    # Compare all four
    allw_df = get_allw_prices()
    allw_df['Date'] = allw_df['Date'].astype(str).str[:10]
    allw_base = allw_df.loc[allw_df['Date'] >= BASE_DATE[:10], 'price']
    if not allw_base.empty:
        allw_ret = (float(allw_base.iloc[-1]) / float(allw_base.iloc[0]) - 1) * 100
        unlev_ret = (result_df['ALLW_REPL'].iloc[-1] / result_df['ALLW_REPL'].iloc[0] - 1) * 100
        lev_ret = (lev_latest / lev_base - 1) * 100
        dyn_ret = (dyn_latest / dyn_base - 1) * 100
        print(f"\n{'='*55}")
        print(f"  ALLW actual:          {allw_ret:+.2f}%")
        print(f"  ALLW_REPL_DYN:        {dyn_ret:+.2f}%  (dynamic weights + lev)")
        print(f"  ALLW_REPL_LEV:        {lev_ret:+.2f}%  (static weights + lev)")
        print(f"  ALLW_REPL (1x):       {unlev_ret:+.2f}%  (static weights, no lev)")
        print(f"  ---")
        print(f"  Weight shift value:   {dyn_ret - lev_ret:+.2f}pp  (dynamic - static levered)")
        print(f"  Residual alpha:       {allw_ret - dyn_ret:+.2f}pp  (ALLW - dynamic)")
        print(f"{'='*55}")

    if store:
        store_ticker(result_df[['Date', 'ALLW_REPL']], 'ALLW_REPL',
                     'ALLW 4-ETF Replication 1x (SPY/TLT/TIP/GLD)')
        store_ticker(result_df[['Date', 'ALLW_REPL_LEV']], 'ALLW_REPL_LEV',
                     'ALLW 4-ETF Replication Levered (static weights)')
        store_ticker(result_df[['Date', 'ALLW_REPL_DYN']], 'ALLW_REPL_DYN',
                     'ALLW 4-ETF Replication Dynamic (time-varying weights + leverage)')
        print(f"\n[DONE] Chart: /api/chart/lw?tickers=ALLW,ALLW_REPL_DYN,ALLW_REPL_LEV,ALLW_REPL&start=2025-03-06&normalize=true&primary=ALLW")
    else:
        print(f"\nRun with --store to save to database")


if __name__ == "__main__":
    main()
