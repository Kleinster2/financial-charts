#!/usr/bin/env python3
"""
generate_allw_best_proxy.py

Generate best real-world proxy portfolio for ALLW using available ETFs.
This attempts to replicate ALLW's actual exposure including futures positions.
"""

import sys
from datetime import datetime
import pandas as pd

from constants import DB_PATH, get_db_connection


def analyze_allw_holdings(as_of_date: str):
    """Analyze ALLW holdings and categorize by asset class."""

    conn = get_db_connection()

    query = """
        SELECT ticker, name, weight, market_value, shares
        FROM etf_holdings_daily
        WHERE etf = 'ALLW' AND snapshot_date = ?
        ORDER BY ABS(weight) DESC
    """

    df = pd.read_sql_query(query, conn, params=(as_of_date,))
    conn.close()

    if df.empty:
        print(f"Error: No ALLW holdings found for {as_of_date}")
        return None

    # Categorize holdings
    equity_etfs = df[df['ticker'].isin(['SPLG', 'SPEM', 'GXC'])]
    gold_futures = df[df['name'].str.contains('GOLD', case=False, na=False)]
    bond_futures = df[df['name'].str.contains('NOTE|BOND|BUND|GILT', case=False, na=False)]
    equity_futures = df[df['name'].str.contains('STOXX|TOPIX|FTSE|SPI', case=False, na=False)]
    fx_positions = df[df['name'].str.contains('GBP|POUND', case=False, na=False)]

    print(f"\n{'='*70}")
    print(f"ALLW Holdings Analysis - {as_of_date}")
    print(f"{'='*70}\n")

    print(f"Total Holdings: {len(df)}")
    print(f"Total AUM (estimated): ${df['market_value'].sum():,.0f}\n")

    print("EQUITY ETFs:")
    for _, row in equity_etfs.iterrows():
        print(f"  {row['ticker']:<8} {row['weight']*100:>6.2f}%  ${row['market_value']:>12,.0f}")

    print(f"\nGOLD FUTURES:")
    for _, row in gold_futures.iterrows():
        print(f"  {row['ticker']:<8} {row['weight']*100:>6.2f}%  ${row['market_value']:>12,.0f}")

    print(f"\nBOND FUTURES:")
    for _, row in bond_futures.iterrows():
        print(f"  {row['ticker']:<8} {row['weight']*100:>6.2f}%  ${row['market_value']:>12,.0f}")

    print(f"\nEQUITY INDEX FUTURES:")
    for _, row in equity_futures.iterrows():
        print(f"  {row['ticker']:<8} {row['weight']*100:>6.2f}%  ${row['market_value']:>12,.0f}")

    print(f"\nFX POSITIONS:")
    for _, row in fx_positions.iterrows():
        print(f"  {row['ticker']:<8} {row['weight']*100:>6.2f}%  ${row['market_value']:>12,.0f}")

    # Calculate exposures
    equity_etf_weight = equity_etfs['weight'].sum()
    gold_weight = gold_futures['weight'].sum()
    bond_weight = bond_futures['weight'].sum()
    equity_fut_weight = equity_futures['weight'].sum()
    fx_weight = fx_positions['weight'].sum()

    cash_weight = 1.0 - equity_etf_weight

    print(f"\n{'='*70}")
    print("SUMMARY BY ASSET CLASS:")
    print(f"{'='*70}")
    print(f"  Equity ETFs:         {equity_etf_weight*100:>6.2f}%")
    print(f"  Gold Futures:        {gold_weight*100:>6.2f}%")
    print(f"  Bond Futures:        {bond_weight*100:>6.2f}%")
    print(f"  Equity Futures:      {equity_fut_weight*100:>6.2f}%")
    print(f"  FX Positions:        {fx_weight*100:>6.2f}%")
    print(f"  Cash/Margin:         {cash_weight*100:>6.2f}%")

    return {
        'equity_etf_weight': equity_etf_weight,
        'gold_weight': gold_weight,
        'bond_weight': bond_weight,
        'equity_fut_weight': equity_fut_weight,
        'fx_weight': fx_weight,
        'cash_weight': cash_weight,
        'equity_etfs': equity_etfs,
        'total_aum': df['market_value'].sum()
    }


def generate_best_proxy(as_of_date: str):
    """Generate best real-world proxy portfolio."""

    analysis = analyze_allw_holdings(as_of_date)
    if analysis is None:
        return None

    print(f"\n{'='*70}")
    print("BEST PROXY PORTFOLIO (Using Available ETFs)")
    print(f"{'='*70}\n")

    portfolio = []

    # Get actual equity ETF holdings
    for _, row in analysis['equity_etfs'].iterrows():
        portfolio.append({
            'ticker': row['ticker'],
            'name': row['name'],
            'weight': row['weight'],
            'allocation_type': 'direct',
            'category': 'equity_etf',
            'notes': 'Direct holding from ALLW'
        })

    # Gold exposure via GLD (proxy for gold futures)
    gold_weight = analysis['gold_weight']
    if gold_weight != 0:
        portfolio.append({
            'ticker': 'GLD',
            'name': 'SPDR Gold Trust',
            'weight': gold_weight,
            'allocation_type': 'proxy',
            'category': 'gold',
            'notes': f'Proxy for ALLW gold futures exposure'
        })

    # Bond exposure via AGG (proxy for bond futures)
    bond_weight = analysis['bond_weight']
    if bond_weight != 0:
        portfolio.append({
            'ticker': 'AGG',
            'name': 'iShares Core U.S. Aggregate Bond ETF',
            'weight': bond_weight,
            'allocation_type': 'proxy',
            'category': 'bonds',
            'notes': f'Proxy for ALLW bond futures exposure'
        })

    # International equity via VEA (proxy for equity index futures)
    equity_fut_weight = analysis['equity_fut_weight']
    if equity_fut_weight != 0:
        portfolio.append({
            'ticker': 'VEA',
            'name': 'Vanguard FTSE Developed Markets ETF',
            'weight': equity_fut_weight,
            'allocation_type': 'proxy',
            'category': 'intl_equity',
            'notes': f'Proxy for ALLW international equity futures'
        })

    # Cash/Margin position via BIL (1-3 month T-bills)
    cash_weight = analysis['cash_weight']
    if cash_weight > 0:
        portfolio.append({
            'ticker': 'BIL',
            'name': 'SPDR Bloomberg 1-3 Month T-Bill ETF',
            'weight': cash_weight,
            'allocation_type': 'cash',
            'category': 'cash',
            'notes': f'Cash/margin for futures positions'
        })

    # Display portfolio
    print("Ticker    Weight %   Category          Type        Notes")
    print("-" * 90)
    for p in portfolio:
        print(f"{p['ticker']:<8} {p['weight']*100:>7.2f}%   {p['category']:<15} {p['allocation_type']:<10}  {p['notes']}")

    total_weight = sum(p['weight'] for p in portfolio)
    print("-" * 90)
    print(f"{'TOTAL':<8} {total_weight*100:>7.2f}%")

    return portfolio


def save_proxy_portfolio(portfolio, as_of_date: str, portfolio_name: str = 'ALLW_PROXY'):
    """Save proxy portfolio to database."""

    conn = get_db_connection()

    # Delete existing
    conn.execute("""
        DELETE FROM replication_portfolios
        WHERE portfolio_name = ? AND as_of_date = ?
    """, (portfolio_name, as_of_date))

    # Insert new portfolio
    created_at = datetime.now().isoformat()

    for item in portfolio:
        conn.execute("""
            INSERT INTO replication_portfolios
            (portfolio_name, as_of_date, ticker, name, weight,
             allocation_type, category, created_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            portfolio_name,
            as_of_date,
            item['ticker'],
            item['name'],
            item['weight'],
            item['allocation_type'],
            item['category'],
            created_at
        ))

    conn.commit()
    conn.close()

    print(f"\n[SUCCESS] Portfolio '{portfolio_name}' saved to database")


def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python generate_allw_best_proxy.py <as_of_date> [--save]")
        print("\nExamples:")
        print("  python generate_allw_best_proxy.py 2025-10-06")
        print("  python generate_allw_best_proxy.py 2025-10-06 --save")
        sys.exit(1)

    as_of_date = sys.argv[1]
    should_save = '--save' in sys.argv

    portfolio = generate_best_proxy(as_of_date)

    if portfolio and should_save:
        save_proxy_portfolio(portfolio, as_of_date, 'ALLW_PROXY')
        print("\nNext steps:")
        print(f"  1. Create synthetic ticker:")
        print(f"     python create_synthetic_ticker.py ALLW_PROXY {as_of_date} ALLW_PROXY --yes")
        print(f"  2. Add to charts:")
        print(f"     python add_portfolio_to_charts.py ALLW_PROXY {as_of_date} 22")


if __name__ == "__main__":
    main()
