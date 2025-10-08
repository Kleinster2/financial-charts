#!/usr/bin/env python3
"""
generate_allw_futures_replication.py

Generate portfolio using ACTUAL futures contracts that ALLW holds.
This is the most accurate replication possible.
"""

import sys
from datetime import datetime
import pandas as pd

from constants import DB_PATH, get_db_connection


def generate_futures_replication(as_of_date: str):
    """Generate portfolio using actual futures contracts."""

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

    print(f"\n{'='*70}")
    print(f"ALLW FUTURES REPLICATION - {as_of_date}")
    print(f"Using Actual Futures Contracts")
    print(f"{'='*70}\n")

    print(f"Total Holdings: {len(df)}")
    print(f"Total AUM: ${df['market_value'].sum():,.0f}\n")

    # Categorize holdings
    portfolio = []

    for _, row in df.iterrows():
        ticker = row['ticker']
        name = row['name']
        weight = row['weight']

        # Determine category
        if ticker in ['SPLG', 'SPEM', 'GXC']:
            category = 'equity_etf'
            allocation_type = 'direct'
        elif 'GOLD' in str(name).upper():
            category = 'gold_futures'
            allocation_type = 'futures'
        elif any(x in str(name).upper() for x in ['NOTE', 'BOND', 'BUND', 'GILT']):
            category = 'bond_futures'
            allocation_type = 'futures'
        elif any(x in str(name).upper() for x in ['STOXX', 'TOPIX', 'FTSE', 'SPI']):
            category = 'equity_futures'
            allocation_type = 'futures'
        elif 'GBP' in str(name).upper() or 'POUND' in str(name).upper():
            category = 'fx'
            allocation_type = 'futures'
        else:
            category = 'other'
            allocation_type = 'direct'

        portfolio.append({
            'ticker': ticker,
            'name': name,
            'weight': weight,
            'allocation_type': allocation_type,
            'category': category,
            'market_value': row['market_value'],
            'shares': row['shares']
        })

    # Calculate cash position (everything not in ETFs)
    etf_weight = sum(p['weight'] for p in portfolio if p['category'] == 'equity_etf')
    cash_weight = 1.0 - etf_weight

    if cash_weight > 0:
        portfolio.append({
            'ticker': 'CASH',
            'name': 'Cash/T-Bills (margin for futures)',
            'weight': cash_weight,
            'allocation_type': 'cash',
            'category': 'cash',
            'market_value': 0,
            'shares': 0
        })

    # Display portfolio
    print("COMPLETE REPLICATION PORTFOLIO:")
    print(f"{'Ticker':<12} {'Weight %':>9} {'Category':<20} {'Type':<10} {'Notional Value':>15}")
    print("-" * 90)

    for p in sorted(portfolio, key=lambda x: abs(x['weight']), reverse=True):
        if p['market_value'] == 0:
            notional = '-'
        else:
            notional = f"${p['market_value']:,.0f}"

        print(f"{p['ticker']:<12} {p['weight']*100:>8.2f}% {p['category']:<20} {p['allocation_type']:<10} {notional:>15}")

    total_weight = sum(p['weight'] for p in portfolio)
    print("-" * 90)
    print(f"{'TOTAL':<12} {total_weight*100:>8.2f}%")

    # Summary by category
    print(f"\n{'='*70}")
    print("SUMMARY BY ASSET CLASS:")
    print(f"{'='*70}")

    categories = {}
    for p in portfolio:
        cat = p['category']
        if cat not in categories:
            categories[cat] = {'weight': 0, 'notional': 0, 'count': 0}
        categories[cat]['weight'] += p['weight']
        categories[cat]['notional'] += p['market_value']
        categories[cat]['count'] += 1

    for cat, data in sorted(categories.items(), key=lambda x: abs(x[1]['weight']), reverse=True):
        print(f"{cat:<25} {data['weight']*100:>7.2f}%  ({data['count']} positions)  ${data['notional']:>12,.0f}")

    print(f"\n{'='*70}")
    print("REPLICATION REQUIREMENTS:")
    print(f"{'='*70}")
    print("\n1. EQUITY ETFs (Easy - available at any broker):")
    for p in portfolio:
        if p['category'] == 'equity_etf':
            print(f"   - {p['ticker']}: {p['weight']*100:.2f}% weight")

    print("\n2. FUTURES CONTRACTS (Requires futures trading account):")
    futures_by_cat = {}
    for p in portfolio:
        if p['allocation_type'] == 'futures':
            cat = p['category']
            if cat not in futures_by_cat:
                futures_by_cat[cat] = []
            futures_by_cat[cat].append(p)

    for cat, positions in futures_by_cat.items():
        print(f"\n   {cat.upper()}:")
        for p in positions:
            print(f"   - {p['ticker']}: {p['name']}")
            print(f"     Weight: {p['weight']*100:.2f}% | Notional: ${p['market_value']:,.0f}")

    print("\n3. CASH/MARGIN:")
    print(f"   - {cash_weight*100:.2f}% in T-Bills or cash")
    print(f"   - Used as margin for futures positions")

    print(f"\n{'='*70}")
    print("IMPLEMENTATION NOTES:")
    print(f"{'='*70}")
    print("""
1. BROKER REQUIREMENTS:
   - Futures trading account (Interactive Brokers, TD Ameritrade, etc.)
   - Options on futures approval (Level 3+)
   - Minimum account size: ~$25,000 for pattern day trading rules

2. MARGIN REQUIREMENTS:
   - Each futures contract requires initial margin ($3,000-$15,000 per contract)
   - Maintenance margin requirements must be maintained
   - Cash/T-Bills provide the margin

3. CONTRACT ROLLING:
   - Futures expire quarterly (Mar, Jun, Sep, Dec)
   - Must roll contracts before expiration
   - ALLW uses Dec 2025 contracts (indicated by "Z5" suffix)

4. SCALING FOR SMALLER ACCOUNTS:
   - Micro futures available for some contracts (1/10 size)
   - Can use ETF proxies for futures positions
   - Minimum practical size: ~$100,000 to replicate accurately

5. TRACKING:
   - Futures contracts have different tickers than ETFs
   - Need futures data feed (separate from stock data)
   - More complex P&L calculation
""")

    return portfolio


def save_futures_portfolio(portfolio, as_of_date: str):
    """Save futures replication portfolio to database."""

    conn = get_db_connection()

    portfolio_name = 'ALLW_FUTURES'

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
        print("  python generate_allw_futures_replication.py <as_of_date> [--save]")
        print("\nExamples:")
        print("  python generate_allw_futures_replication.py 2025-10-06")
        print("  python generate_allw_futures_replication.py 2025-10-06 --save")
        print("\nThis shows ALLW's actual holdings including futures contracts.")
        print("For practical ETF-only replication, use generate_allw_best_proxy.py")
        sys.exit(1)

    as_of_date = sys.argv[1]
    should_save = '--save' in sys.argv

    portfolio = generate_futures_replication(as_of_date)

    if portfolio and should_save:
        save_futures_portfolio(portfolio, as_of_date)


if __name__ == "__main__":
    main()
