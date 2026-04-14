#!/usr/bin/env python3
"""
create_aicp_index.py

Create AI Control Points (AICP) basket index.
Tracks software names that still own critical control points under AI:
compute access, enterprise identity, workflow context, and distribution.

Methodology (Apr 2026):
- Taxonomy-derived basket, not event-derived
- Equal-weight across the three representative control-point names
- Constituents: ORCL, MSFT, CRM

Usage:
    python scripts/create_aicp_index.py [--store]
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
sys.path.insert(0, str(Path(__file__).parent.parent / 'charting_app'))

import sqlite3
import pandas as pd
import numpy as np

DB_PATH = Path(__file__).parent.parent / 'market_data.db'

AICP_WEIGHTS = {
    'ORCL': 1/3,
    'MSFT': 1/3,
    'CRM': 1/3,
}

BASE_DATE = '2026-02-03'
INITIAL_VALUE = 100.0


def get_component_prices(start_date: str = '2021-07-01'):
    conn = sqlite3.connect(DB_PATH)
    tickers = list(AICP_WEIGHTS.keys())
    placeholders = ','.join(['?'] * len(tickers))
    query = f"""
        SELECT Date, Ticker, Close
        FROM prices_long
        WHERE Ticker IN ({placeholders}) AND Date >= ?
        ORDER BY Date ASC
    """
    df = pd.read_sql_query(query, conn, params=tickers + [start_date])
    conn.close()

    if df.empty:
        return df

    pivot = df.pivot(index='Date', columns='Ticker', values='Close').reset_index()
    pivot = pivot.dropna(subset=tickers, how='any').reset_index(drop=True)
    return pivot


def calculate_aicp_index(start_date: str = '2021-07-01'):
    print(f"\n{'='*70}")
    print("AI Control Points (AICP) Index")
    print(f"{'='*70}\n")

    print("Constituents:")
    for ticker, weight in AICP_WEIGHTS.items():
        print(f"  {ticker:12s} {weight*100:5.1f}%")
    print(f"\n  Total: {sum(AICP_WEIGHTS.values())*100:.0f}%")
    print(f"\nBase date: {BASE_DATE} = {INITIAL_VALUE}")

    prices_df = get_component_prices(start_date)
    if prices_df.empty:
        print("Error: No price data found")
        return None

    print(f"\nPrice data: {len(prices_df)} days from {prices_df['Date'].min()} to {prices_df['Date'].max()}")

    tickers = list(AICP_WEIGHTS.keys())
    returns_data = {'Date': prices_df['Date'].values}

    for ticker in tickers:
        prices = prices_df[ticker].values
        returns = np.zeros(len(prices))
        returns[0] = 0
        for i in range(1, len(prices)):
            if pd.notna(prices[i]) and pd.notna(prices[i-1]) and prices[i-1] != 0:
                returns[i] = (prices[i] - prices[i-1]) / prices[i-1]
            else:
                returns[i] = 0
        returns_data[ticker] = returns

    returns_df = pd.DataFrame(returns_data)
    portfolio_returns = np.zeros(len(returns_df))
    for ticker, weight in AICP_WEIGHTS.items():
        portfolio_returns += returns_df[ticker].values * weight

    dates = returns_df['Date'].values
    base_idx = 0
    for i, d in enumerate(dates):
        if str(d)[:10] >= BASE_DATE:
            base_idx = i
            break

    portfolio_value = np.zeros(len(portfolio_returns))
    portfolio_value[base_idx] = INITIAL_VALUE

    for i in range(base_idx + 1, len(portfolio_returns)):
        portfolio_value[i] = portfolio_value[i-1] * (1 + portfolio_returns[i])

    for i in range(base_idx - 1, -1, -1):
        portfolio_value[i] = portfolio_value[i+1] / (1 + portfolio_returns[i+1])

    result_df = pd.DataFrame({
        'Date': returns_df['Date'],
        'AICP': portfolio_value,
    })

    latest_value = portfolio_value[-1]
    base_value = portfolio_value[base_idx]
    print("\nIndex Values:")
    print(f"  Base ({BASE_DATE}): {base_value:.2f}")
    print(f"  Latest: {latest_value:.2f}")
    print(f"  Change from base: {(latest_value/base_value - 1)*100:+.2f}%")

    print("\nRecent values:")
    for _, row in result_df.tail(10).iterrows():
        print(f"  {str(row['Date'])[:10]}: {row['AICP']:.2f}")

    return result_df


def store_ticker(df: pd.DataFrame):
    df_narrow = df[['Date', 'AICP']].rename(columns={'AICP': 'Close'}).copy()
    df_narrow['Ticker'] = 'AICP'

    conn = sqlite3.connect(DB_PATH, timeout=30)
    try:
        rows = list(zip(df_narrow['Date'], df_narrow['Ticker'], df_narrow['Close']))
        conn.executemany(
            'INSERT OR REPLACE INTO prices_long (Date, Ticker, Close) VALUES (?, ?, ?)',
            rows
        )
        conn.commit()
        print(f"  AICP: upserted {len(rows):,} rows into prices_long")
    finally:
        conn.close()

    conn = sqlite3.connect(DB_PATH, timeout=30)
    conn.execute('''
        INSERT OR REPLACE INTO ticker_metadata
        (ticker, name, table_name, data_type, first_date, last_date, data_points)
        VALUES (?, ?, 'prices_long', 'index', ?, ?, ?)
    ''', ('AICP', 'AI Control Points Index', df['Date'].min(), df['Date'].max(), len(df)))
    conn.commit()
    conn.close()

    print("  [SUCCESS] AICP stored")


def main():
    store = '--store' in sys.argv or '-s' in sys.argv
    result_df = calculate_aicp_index()
    if result_df is not None and store:
        store_ticker(result_df)
        print("\n[DONE] You can now chart 'AICP' in your charting app")
    elif result_df is not None:
        print("\nRun with --store to save to database")


if __name__ == '__main__':
    main()
