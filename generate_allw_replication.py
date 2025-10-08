#!/usr/bin/env python3
"""
generate_allw_replication.py

Generate a replicating portfolio for ALLW ETF based on the latest holdings data.
Creates tradeable portfolio allocations and stores them in the database.
"""

import sqlite3
import sys
from datetime import datetime
from typing import Dict, List, Tuple
import pandas as pd

from constants import DB_PATH, get_db_connection


# ETF proxies for different asset classes
ETF_PROXIES = {
    'us_equity': ['SPY', 'VOO', 'IVV', 'SPLG'],
    'emerging_markets': ['VWO', 'IEMG', 'EEM', 'SPEM'],
    'china': ['FXI', 'MCHI', 'GXC'],
    'gold': ['GLD', 'IAU', 'GLDM'],
    'long_treasury': ['TLT', 'VGLT'],
    'intermediate_treasury': ['IEF', 'VGIT'],
    'international_bonds': ['BNDX', 'IAGG'],
    'europe_equity': ['VGK', 'IEUR', 'FEZ'],
    'japan_equity': ['EWJ', 'DXJ'],
    'uk_equity': ['EWU'],
}


def get_latest_holdings(conn: sqlite3.Connection) -> Tuple[pd.DataFrame, str]:
    """Get the latest ALLW holdings from the database."""
    # Get latest snapshot date
    cursor = conn.execute(
        "SELECT MAX(snapshot_date) FROM etf_holdings_daily WHERE etf = 'ALLW'"
    )
    latest_date = cursor.fetchone()[0]

    if not latest_date:
        raise ValueError("No ALLW holdings found in database. Run download_allw_holdings.py first.")

    # Get holdings for latest date
    query = """
        SELECT ticker, name, weight, shares, market_value
        FROM etf_holdings_daily
        WHERE etf = 'ALLW' AND snapshot_date = ?
        ORDER BY ABS(weight) DESC
    """
    df = pd.read_sql_query(query, conn, params=(latest_date,))

    return df, latest_date


def classify_holdings(holdings_df: pd.DataFrame) -> Dict[str, List[Dict]]:
    """Classify holdings into asset categories."""
    categories = {
        'us_equity_etf': [],
        'emerging_markets_etf': [],
        'china_etf': [],
        'gold_futures': [],
        'equity_futures': [],
        'bond_futures': [],
        'currency': [],
        'other': []
    }

    for _, row in holdings_df.iterrows():
        ticker = str(row['ticker']).strip()
        name = str(row['name']).strip().upper()
        weight = row['weight']

        holding = {
            'ticker': ticker,
            'name': row['name'],
            'weight': weight,
            'weight_pct': weight * 100
        }

        # Classify by ticker/name patterns
        if ticker == 'SPLG':
            categories['us_equity_etf'].append(holding)
        elif ticker == 'SPEM':
            categories['emerging_markets_etf'].append(holding)
        elif ticker == 'GXC':
            categories['china_etf'].append(holding)
        elif 'GC' in ticker and ('FUTR' in name or 'GOLD' in name):
            categories['gold_futures'].append(holding)
        elif any(x in name for x in ['STOXX', 'TOPIX', 'FTSE', 'SPI']):
            categories['equity_futures'].append(holding)
        elif any(x in name for x in ['BOND', 'NOTE', 'BUND', 'GILT']):
            categories['bond_futures'].append(holding)
        elif 'STERLING' in name or 'DOLLAR' in name:
            categories['currency'].append(holding)
        else:
            categories['other'].append(holding)

    return categories


def generate_etf_only_portfolio(categories: Dict) -> pd.DataFrame:
    """Generate simplified ETF-only replication portfolio."""
    portfolio = []

    # Core ETF holdings (direct replication)
    for cat in ['us_equity_etf', 'emerging_markets_etf', 'china_etf']:
        for holding in categories[cat]:
            portfolio.append({
                'ticker': holding['ticker'],
                'name': holding['name'],
                'weight': holding['weight'],
                'allocation_type': 'direct',
                'category': cat
            })

    # Add ETF proxies for futures positions
    # Gold futures -> GLD
    gold_weight = sum(h['weight'] for h in categories['gold_futures'])
    if gold_weight > 0:
        portfolio.append({
            'ticker': 'GLD',
            'name': 'SPDR Gold Trust',
            'weight': gold_weight,
            'allocation_type': 'proxy',
            'category': 'gold'
        })

    # Equity futures -> regional ETFs (small weights, approximate)
    equity_futures_weight = sum(h['weight'] for h in categories['equity_futures'])
    if equity_futures_weight > 0.002:  # Only if > 0.2%
        # Split among regions
        portfolio.append({
            'ticker': 'VGK',
            'name': 'Vanguard FTSE Europe ETF',
            'weight': equity_futures_weight * 0.5,  # Approximate Europe weight
            'allocation_type': 'proxy',
            'category': 'international_equity'
        })
        portfolio.append({
            'ticker': 'EWJ',
            'name': 'iShares MSCI Japan ETF',
            'weight': equity_futures_weight * 0.3,  # Approximate Japan weight
            'allocation_type': 'proxy',
            'category': 'international_equity'
        })

    # Bond futures -> TLT + IEF
    bond_weight = sum(h['weight'] for h in categories['bond_futures'])
    if bond_weight > 0.001:  # Only if > 0.1%
        portfolio.append({
            'ticker': 'TLT',
            'name': 'iShares 20+ Year Treasury Bond ETF',
            'weight': bond_weight * 0.7,
            'allocation_type': 'proxy',
            'category': 'bonds'
        })
        portfolio.append({
            'ticker': 'IEF',
            'name': 'iShares 7-10 Year Treasury Bond ETF',
            'weight': bond_weight * 0.3,
            'allocation_type': 'proxy',
            'category': 'bonds'
        })

    df = pd.DataFrame(portfolio)

    # Calculate cash allocation (remainder to 100%)
    allocated_weight = df['weight'].sum()
    cash_weight = 1.0 - allocated_weight

    # Add cash position
    cash_row = pd.DataFrame([{
        'ticker': 'CASH',
        'name': 'Cash / Money Market',
        'weight': cash_weight,
        'allocation_type': 'cash',
        'category': 'cash'
    }])
    df = pd.concat([df, cash_row], ignore_index=True)

    return df


def generate_scaled_portfolio(categories: Dict) -> pd.DataFrame:
    """Generate portfolio with ETF positions scaled to 100% (no cash)."""
    portfolio = []

    # Get only ETF positions
    for cat in ['us_equity_etf', 'emerging_markets_etf', 'china_etf']:
        for holding in categories[cat]:
            portfolio.append({
                'ticker': holding['ticker'],
                'name': holding['name'],
                'original_weight': holding['weight'],
                'category': cat
            })

    # Add gold proxy
    gold_weight = sum(h['weight'] for h in categories['gold_futures'])
    if gold_weight > 0:
        portfolio.append({
            'ticker': 'GLD',
            'name': 'SPDR Gold Trust',
            'original_weight': gold_weight,
            'category': 'gold'
        })

    df = pd.DataFrame(portfolio)

    # Scale weights to sum to 100%
    total_weight = df['original_weight'].sum()
    df['weight'] = df['original_weight'] / total_weight
    df['allocation_type'] = 'scaled'

    return df[['ticker', 'name', 'weight', 'allocation_type', 'category', 'original_weight']]


def save_portfolio_to_db(portfolio_df: pd.DataFrame, portfolio_name: str,
                         as_of_date: str, conn: sqlite3.Connection):
    """Save generated portfolio to database."""

    # Create table if not exists
    conn.execute("""
        CREATE TABLE IF NOT EXISTS replication_portfolios (
            portfolio_name TEXT NOT NULL,
            as_of_date TEXT NOT NULL,
            ticker TEXT NOT NULL,
            name TEXT,
            weight REAL,
            allocation_type TEXT,
            category TEXT,
            original_weight REAL,
            created_at TEXT NOT NULL,
            PRIMARY KEY (portfolio_name, as_of_date, ticker)
        )
    """)

    # Prepare data
    df = portfolio_df.copy()
    df['portfolio_name'] = portfolio_name
    df['as_of_date'] = as_of_date
    df['created_at'] = datetime.now().isoformat()

    # Add original_weight if not present
    if 'original_weight' not in df.columns:
        df['original_weight'] = df['weight']

    # Insert into database
    df.to_sql('_tmp_portfolio', conn, if_exists='replace', index=False)

    conn.execute("""
        INSERT OR REPLACE INTO replication_portfolios
        SELECT portfolio_name, as_of_date, ticker, name, weight,
               allocation_type, category, original_weight, created_at
        FROM _tmp_portfolio
    """)

    conn.execute("DROP TABLE _tmp_portfolio")
    conn.commit()


def print_portfolio_summary(df: pd.DataFrame, title: str):
    """Print portfolio allocation summary."""
    print(f"\n{'='*80}")
    print(f"{title}")
    print(f"{'='*80}")

    # Sort by weight descending
    df_sorted = df.sort_values('weight', ascending=False)

    print(f"\n{'Ticker':<8} {'Name':<40} {'Weight %':>10} {'Type':<12}")
    print("-" * 80)

    for _, row in df_sorted.iterrows():
        weight_pct = row['weight'] * 100
        ticker = row['ticker']
        name = row['name'][:38]  # Truncate long names
        alloc_type = row['allocation_type']

        print(f"{ticker:<8} {name:<40} {weight_pct:>9.2f}% {alloc_type:<12}")

    print("-" * 80)
    print(f"{'TOTAL':<49} {df['weight'].sum() * 100:>9.2f}%")
    print()

    # Category summary
    if 'category' in df.columns:
        print("\nAllocation by Category:")
        print("-" * 40)
        category_summary = df.groupby('category')['weight'].sum().sort_values(ascending=False)
        for cat, weight in category_summary.items():
            print(f"  {cat:<30} {weight*100:>6.2f}%")


def main():
    print(f"Using database: {DB_PATH}")
    print("="*80)

    try:
        conn = get_db_connection()

        # Get latest holdings
        print("\n📊 Fetching latest ALLW holdings...")
        holdings_df, as_of_date = get_latest_holdings(conn)
        print(f"✅ Loaded {len(holdings_df)} holdings as of {as_of_date}")

        # Classify holdings
        print("\n🔍 Classifying holdings by asset type...")
        categories = classify_holdings(holdings_df)

        # Print classification summary
        print("\nHoldings Classification:")
        for cat, holdings in categories.items():
            if holdings:
                total_weight = sum(h['weight_pct'] for h in holdings)
                print(f"  {cat:<25} {len(holdings):>2} holdings, {total_weight:>6.2f}% total weight")

        # Generate portfolios
        print("\n🎯 Generating replication portfolios...")

        # Portfolio 1: ETF-only with cash
        etf_portfolio = generate_etf_only_portfolio(categories)
        save_portfolio_to_db(etf_portfolio, 'ALLW_ETF_ONLY', as_of_date, conn)
        print_portfolio_summary(etf_portfolio, "Portfolio 1: ETF-Only Replication (with cash)")

        # Portfolio 2: Scaled to 100%
        scaled_portfolio = generate_scaled_portfolio(categories)
        save_portfolio_to_db(scaled_portfolio, 'ALLW_SCALED', as_of_date, conn)
        print_portfolio_summary(scaled_portfolio, "Portfolio 2: Scaled Portfolio (100% invested)")

        conn.close()

        print("\n✅ Portfolios saved to database!")
        print("\nTo view saved portfolios:")
        print(f"  sqlite3 {DB_PATH} \"SELECT * FROM replication_portfolios WHERE as_of_date='{as_of_date}';\"")

    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
