#!/usr/bin/env python3
"""
create_weekly_drawdown_baskets.py

Create equal-weight sector baskets for groups that saw outsized drawdowns
in the week of Feb 10-13, 2026 (tariff/CPI shock week).

Baskets stored as synthetic indices in stock_prices_daily.
Base date: 2026-02-07 (pre-week Friday close) = 100.

Usage:
    python scripts/create_weekly_drawdown_baskets.py [--store]
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

import sqlite3
import pandas as pd
import numpy as np

DB_PATH = Path(__file__).parent.parent / 'market_data.db'

# Sector baskets — equal weight within each
BASKETS = {
    'DDNK': {  # Drawdown: Nuclear
        'name': 'Nuclear Drawdown Basket (Feb 2026)',
        'tickers': ['LEU', 'SMR', 'OKLO', 'NNE', 'LTBR', 'UEC'],
    },
    'DDGM': {  # Drawdown: Gaming
        'name': 'Gaming Drawdown Basket (Feb 2026)',
        'tickers': ['DKNG', 'FLUT', 'PENN', 'CZR', 'MGM', 'RSI', 'RBLX', 'TTWO'],
    },
    'DDFN': {  # Drawdown: Financials
        'name': 'Financials Drawdown Basket (Feb 2026)',
        'tickers': ['C', 'SCHW', 'WFC', 'BAC', 'HBAN', 'BK', 'SPGI', 'ICE', 'NDAQ', 'RJF', 'AMP'],
    },
    'DDSD': {  # Drawdown: Space/Defense
        'name': 'Space & Defense Drawdown Basket (Feb 2026)',
        'tickers': ['RDW', 'ASTS', 'LUNR', 'RKLB', 'AVAV', 'KTOS', 'BAH', 'CACI', 'LDOS', 'SAIC'],
    },
    'DDIT': {  # Drawdown: IT Services/Software
        'name': 'IT Services Drawdown Basket (Feb 2026)',
        'tickers': ['CSCO', 'INTU', 'CTSH', 'EPAM', 'CDW', 'TYL', 'PATH', 'CSGP', 'GDDY', 'GTLB'],
    },
}

BASE_DATE = '2026-02-07'
INITIAL_VALUE = 100.0


def calculate_basket(basket_id, config, start_date='2024-01-01'):
    """Calculate equal-weight basket index values."""
    conn = sqlite3.connect(DB_PATH)

    tickers = config['tickers']
    equal_weight = 1.0 / len(tickers)
    weights = {t: equal_weight for t in tickers}

    ticker_cols = ', '.join([f'"{t}"' for t in tickers])
    query = f"""
        SELECT Date, {ticker_cols}
        FROM stock_prices_daily
        WHERE Date >= ?
        ORDER BY Date ASC
    """
    df = pd.read_sql_query(query, conn, params=(start_date,))
    conn.close()

    if df.empty:
        print(f"  Error: No price data for {basket_id}")
        return None

    # Calculate daily returns
    returns_data = {'Date': df['Date'].values}
    missing = []

    for ticker in tickers:
        if ticker in df.columns:
            prices = df[ticker].values
            returns = np.zeros(len(prices))
            for i in range(1, len(prices)):
                if pd.notna(prices[i]) and pd.notna(prices[i-1]) and prices[i-1] != 0:
                    returns[i] = (prices[i] - prices[i-1]) / prices[i-1]
            returns_data[ticker] = returns
        else:
            missing.append(ticker)

    if missing:
        print(f"  Missing tickers: {missing}")

    returns_df = pd.DataFrame(returns_data)

    # Weighted portfolio return
    portfolio_returns = np.zeros(len(returns_df))
    for ticker, weight in weights.items():
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
        print(f"  Warning: Base date not found, using first date")
        base_idx = 0

    # Calculate cumulative value
    portfolio_value = np.zeros(len(portfolio_returns))
    portfolio_value[base_idx] = INITIAL_VALUE

    for i in range(base_idx + 1, len(portfolio_returns)):
        portfolio_value[i] = portfolio_value[i-1] * (1 + portfolio_returns[i])

    for i in range(base_idx - 1, -1, -1):
        portfolio_value[i] = portfolio_value[i+1] / (1 + portfolio_returns[i+1])

    result_df = pd.DataFrame({
        'Date': returns_df['Date'],
        basket_id: portfolio_value
    })

    latest = portfolio_value[-1]
    base = portfolio_value[base_idx]
    print(f"  {basket_id} ({config['name']})")
    print(f"    Constituents: {', '.join(tickers)} (equal weight {equal_weight*100:.1f}%)")
    print(f"    Base ({BASE_DATE}): {base:.2f} -> Latest: {latest:.2f} ({(latest/base-1)*100:+.1f}%)")

    return result_df


def store_basket(df, basket_id, config):
    """Store basket index in stock_prices_daily."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("PRAGMA table_info(stock_prices_daily)")
    columns = [row[1] for row in cursor.fetchall()]

    if basket_id not in columns:
        cursor.execute(f'ALTER TABLE stock_prices_daily ADD COLUMN "{basket_id}" REAL')
        conn.commit()

    for _, row in df.iterrows():
        cursor.execute(f'UPDATE stock_prices_daily SET "{basket_id}" = ? WHERE Date = ?',
                       (row[basket_id], row['Date']))

    conn.commit()

    cursor.execute('''
        INSERT OR REPLACE INTO ticker_metadata (ticker, name, table_name, data_type, first_date, last_date, data_points)
        VALUES (?, ?, 'stock_prices_daily', 'index', ?, ?, ?)
    ''', (basket_id, config['name'], df['Date'].min(), df['Date'].max(), len(df)))

    conn.commit()
    conn.close()
    print(f"    [STORED] {basket_id}")


def main():
    store = '--store' in sys.argv

    print(f"\n{'='*70}")
    print("Feb 2026 Drawdown Sector Baskets")
    print(f"{'='*70}\n")

    for basket_id, config in BASKETS.items():
        result = calculate_basket(basket_id, config)
        if result is not None and store:
            store_basket(result, basket_id, config)
        print()

    if not store:
        print("Run with --store to save to database")


if __name__ == "__main__":
    main()
