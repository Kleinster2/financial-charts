#!/usr/bin/env python3
"""
generate_allw_true_replication.py

Create TRUE 1:1 replication of ALLW using actual futures tickers.
This is the exact portfolio ALLW holds - no proxies, no substitutions.
"""

import sys
from datetime import datetime
import pandas as pd

from constants import DB_PATH, get_db_connection


def generate_true_replication(as_of_date: str):
    """Generate exact 1:1 replication portfolio."""

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

    print(f"\n{'='*80}")
    print(f"ALLW TRUE REPLICATION PORTFOLIO - {as_of_date}")
    print(f"Exact 1:1 Copy of ALLW Holdings")
    print(f"{'='*80}\n")

    print(f"Total Positions: {len(df)}")
    print(f"Total AUM: ${df['market_value'].sum():,.0f}\n")

    # Build exact portfolio - everything ALLW holds
    portfolio = []

    print("COMPLETE HOLDINGS LIST:")
    print(f"{'Ticker':<15} {'Name':<35} {'Weight %':>10} {'Type':<12} {'Notional':<15}")
    print("-" * 100)

    for _, row in df.iterrows():
        ticker = row['ticker']
        name = row['name']
        weight = row['weight']
        market_value = row['market_value']

        # Determine type
        if ticker in ['SPLG', 'SPEM', 'GXC']:
            position_type = 'ETF'
        elif '=' in ticker or any(x in ticker for x in ['Z5', 'H6', 'M6', 'U6']):
            position_type = 'FUTURES'
        else:
            # Check if it's a futures contract by name
            if any(x in str(name).upper() for x in ['FUTURE', 'FUTR', 'FUT', 'INDEX']):
                position_type = 'FUTURES'
            else:
                position_type = 'OTHER'

        portfolio.append({
            'ticker': ticker,
            'name': name,
            'weight': weight,
            'type': position_type,
            'market_value': market_value,
            'shares': row['shares']
        })

        # Display
        notional_str = f"${market_value:,.0f}" if market_value != 0 else "-"
        print(f"{ticker:<15} {name[:35]:<35} {weight*100:>9.2f}% {position_type:<12} {notional_str:<15}")

    # Calculate cash (everything not directly held)
    direct_weight = sum(p['weight'] for p in portfolio if p['type'] in ['ETF', 'OTHER'])
    cash_weight = 1.0 - direct_weight

    if cash_weight != 0:
        portfolio.append({
            'ticker': 'CASH',
            'name': 'Cash/T-Bills (margin collateral)',
            'weight': cash_weight,
            'type': 'CASH',
            'market_value': 0,
            'shares': 0
        })
        print(f"{'CASH':<15} {'Cash/T-Bills (margin collateral)':<35} {cash_weight*100:>9.2f}% {'CASH':<12} {'-':<15}")

    print("-" * 100)
    total_weight = sum(p['weight'] for p in portfolio)
    print(f"{'TOTAL':<15} {'':35} {total_weight*100:>9.2f}%\n")

    # Categorize by asset class
    print(f"\n{'='*80}")
    print("ASSET CLASS BREAKDOWN:")
    print(f"{'='*80}\n")

    categories = {
        'US Equity': [],
        'Emerging Markets': [],
        'China': [],
        'Gold': [],
        'Bonds': [],
        'International Equity': [],
        'FX': [],
        'Cash': []
    }

    for p in portfolio:
        ticker = p['ticker']
        name = str(p['name']).upper()

        if ticker == 'SPLG':
            categories['US Equity'].append(p)
        elif ticker == 'SPEM':
            categories['Emerging Markets'].append(p)
        elif ticker == 'GXC':
            categories['China'].append(p)
        elif 'GOLD' in name or ticker == 'GCZ5':
            categories['Gold'].append(p)
        elif any(x in name for x in ['NOTE', 'BOND', 'BUND', 'GILT']):
            categories['Bonds'].append(p)
        elif any(x in name for x in ['STOXX', 'TOPIX', 'FTSE', 'SPI']):
            categories['International Equity'].append(p)
        elif 'POUND' in name or 'GBP' in name or 'STERLING' in name:
            categories['FX'].append(p)
        elif ticker == 'CASH':
            categories['Cash'].append(p)

    for category, positions in categories.items():
        if not positions:
            continue

        total_weight = sum(p['weight'] for p in positions)
        print(f"{category:.<30} {total_weight*100:>6.2f}%")

        for p in positions:
            if p['ticker'] != 'CASH':
                print(f"  {p['ticker']:<12} {p['name'][:50]:<50} {p['weight']*100:>6.2f}%")

    # Futures ticker mapping
    print(f"\n{'='*80}")
    print("FUTURES TICKER REFERENCE:")
    print(f"{'='*80}\n")
    print("For charting/trading, you'll need prices for these futures contracts:\n")

    futures = [p for p in portfolio if p['type'] == 'FUTURES']

    if futures:
        print(f"{'ALLW Ticker':<15} {'Contract Name':<40} {'Yahoo Symbol':<15}")
        print("-" * 80)

        # Map to Yahoo Finance futures symbols
        futures_map = {
            'GCZ5': ('GOLD 100 OZ FUTR  DEC25', 'GC=F'),
            'TYZ5': ('US 10YR NOTE (CBT)DEC25', 'ZN=F'),
            'USZ5': ('US LONG BOND(CBT) DEC25', 'ZB=F'),
            'RXZ5': ('EURO-BUND FUTURE  DEC25', 'FGBL=F'),
            'G Z5': ('LONG GILT FUTURE  DEC25', 'GF=F'),
            'XMZ5': ('AUST 10Y BOND FUT DEC25', 'XM=F'),
            'VGZ5': ('EURO STOXX 50     DEC25', 'FESX=F'),
            'TPZ5': ('TOPIX INDX FUTR   DEC25', 'TPI=F'),
            'Z Z5': ('FTSE 100 IDX FUT  DEC25', 'FF=F'),
            'XPZ5': ('SPI 200 FUTURES   DEC25', 'AP=F'),
        }

        for p in futures:
            ticker = p['ticker']
            name = p['name']
            yahoo_symbol = futures_map.get(ticker, ('', 'UNKNOWN'))[1]
            print(f"{ticker:<15} {name[:40]:<40} {yahoo_symbol:<15}")

    print("\nNote: Futures tickers with '=F' suffix are continuous contracts on Yahoo Finance")
    print("ALLW holds specific expiration months (Dec 2025 = 'Z5' suffix)")

    return portfolio


def save_true_replication(portfolio, as_of_date: str):
    """Save true replication portfolio."""

    conn = get_db_connection()

    portfolio_name = 'ALLW_TRUE'

    # Delete existing
    conn.execute("""
        DELETE FROM replication_portfolios
        WHERE portfolio_name = ? AND as_of_date = ?
    """, (portfolio_name, as_of_date))

    # Insert
    created_at = datetime.now().isoformat()

    for item in portfolio:
        # Determine category
        ticker = item['ticker']
        if ticker in ['SPLG', 'SPEM', 'GXC']:
            category = 'equity_etf'
        elif ticker == 'CASH':
            category = 'cash'
        elif item['type'] == 'FUTURES':
            name = str(item['name']).upper()
            if 'GOLD' in name:
                category = 'gold_futures'
            elif any(x in name for x in ['NOTE', 'BOND', 'BUND', 'GILT']):
                category = 'bond_futures'
            elif any(x in name for x in ['STOXX', 'TOPIX', 'FTSE', 'SPI']):
                category = 'equity_futures'
            else:
                category = 'fx'
        else:
            category = 'other'

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
            item['type'].lower(),
            category,
            created_at
        ))

    conn.commit()
    conn.close()

    print(f"\n{'='*80}")
    print(f"[SUCCESS] True replication portfolio saved as '{portfolio_name}'")
    print(f"{'='*80}\n")


def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python generate_allw_true_replication.py <as_of_date> [--save]")
        print("\nExamples:")
        print("  python generate_allw_true_replication.py 2025-10-06")
        print("  python generate_allw_true_replication.py 2025-10-06 --save")
        print("\nThis creates an EXACT copy of ALLW's holdings - no proxies!")
        sys.exit(1)

    as_of_date = sys.argv[1]
    should_save = '--save' in sys.argv

    portfolio = generate_true_replication(as_of_date)

    if portfolio and should_save:
        save_true_replication(portfolio, as_of_date)
        print("\nNext steps:")
        print("1. Download futures price data for the tickers listed above")
        print("2. Create synthetic ticker:")
        print(f"   python create_synthetic_ticker.py ALLW_TRUE {as_of_date} ALLW_TRUE --yes")


if __name__ == "__main__":
    main()
