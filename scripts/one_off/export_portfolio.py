import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent.parent.parent))
#!/usr/bin/env python3
"""
export_portfolio.py

Export replication portfolio in various formats for trading platforms.
"""

import sys
import json
import csv
from datetime import datetime

from constants import DB_PATH, get_db_connection


def export_to_csv(portfolio_name: str, as_of_date: str, output_file: str = None):
    """Export portfolio to CSV format."""
    conn = get_db_connection()

    query = """
        SELECT ticker, name, weight, allocation_type, category
        FROM replication_portfolios
        WHERE portfolio_name = ? AND as_of_date = ?
        ORDER BY weight DESC
    """

    cursor = conn.execute(query, (portfolio_name, as_of_date))
    rows = cursor.fetchall()

    if not rows:
        print(f"No portfolio found: {portfolio_name} as of {as_of_date}")
        return

    if output_file is None:
        output_file = f"{portfolio_name}_{as_of_date}.csv"

    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Ticker', 'Name', 'Weight %', 'Allocation Type', 'Category'])

        for row in rows:
            ticker, name, weight, alloc_type, category = row
            writer.writerow([ticker, name, f"{weight*100:.4f}", alloc_type, category])

    print(f"✅ Exported to {output_file}")
    conn.close()


def export_to_json(portfolio_name: str, as_of_date: str, output_file: str = None):
    """Export portfolio to JSON format."""
    conn = get_db_connection()

    query = """
        SELECT ticker, name, weight, allocation_type, category
        FROM replication_portfolios
        WHERE portfolio_name = ? AND as_of_date = ?
        ORDER BY weight DESC
    """

    cursor = conn.execute(query, (portfolio_name, as_of_date))
    rows = cursor.fetchall()

    if not rows:
        print(f"No portfolio found: {portfolio_name} as of {as_of_date}")
        return

    if output_file is None:
        output_file = f"{portfolio_name}_{as_of_date}.json"

    portfolio = {
        'name': portfolio_name,
        'as_of_date': as_of_date,
        'holdings': []
    }

    for row in rows:
        ticker, name, weight, alloc_type, category = row
        portfolio['holdings'].append({
            'ticker': ticker,
            'name': name,
            'weight': weight,
            'weight_percent': weight * 100,
            'allocation_type': alloc_type,
            'category': category
        })

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(portfolio, f, indent=2)

    print(f"✅ Exported to {output_file}")
    conn.close()


def print_broker_format(portfolio_name: str, as_of_date: str, portfolio_value: float = 10000):
    """Print portfolio in format suitable for broker order entry."""
    conn = get_db_connection()

    query = """
        SELECT ticker, name, weight
        FROM replication_portfolios
        WHERE portfolio_name = ? AND as_of_date = ?
        AND ticker != 'CASH'
        ORDER BY weight DESC
    """

    cursor = conn.execute(query, (portfolio_name, as_of_date))
    rows = cursor.fetchall()

    if not rows:
        print(f"No portfolio found: {portfolio_name} as of {as_of_date}")
        return

    print(f"\n{'='*80}")
    print(f"Portfolio Orders for ${portfolio_value:,.2f} investment")
    print(f"Portfolio: {portfolio_name} as of {as_of_date}")
    print(f"{'='*80}\n")

    print(f"{'Ticker':<8} {'Name':<40} {'Weight %':>10} {'$ Amount':>12}")
    print("-" * 80)

    for ticker, name, weight in rows:
        amount = portfolio_value * weight
        print(f"{ticker:<8} {name[:38]:<40} {weight*100:>9.2f}% ${amount:>11.2f}")

    print("-" * 80)
    total_invested = sum(row[2] for row in rows) * portfolio_value
    cash = portfolio_value - total_invested
    print(f"{'CASH':<8} {'Cash / Money Market':<40} {(cash/portfolio_value)*100:>9.2f}% ${cash:>11.2f}")
    print(f"\n{'TOTAL':<49} {'100.00%':>10} ${portfolio_value:>11.2f}\n")

    conn.close()


def list_available_portfolios():
    """List all available portfolios in the database."""
    conn = get_db_connection()

    query = """
        SELECT DISTINCT portfolio_name, as_of_date,
               COUNT(*) as num_holdings,
               created_at
        FROM replication_portfolios
        GROUP BY portfolio_name, as_of_date
        ORDER BY as_of_date DESC, portfolio_name
    """

    cursor = conn.execute(query)
    rows = cursor.fetchall()

    print("\n" + "="*80)
    print("Available Portfolios")
    print("="*80 + "\n")

    print(f"{'Portfolio Name':<25} {'As Of Date':<15} {'Holdings':>10} {'Created':<20}")
    print("-" * 80)

    for portfolio_name, as_of_date, num_holdings, created_at in rows:
        created_short = created_at[:19] if created_at else 'Unknown'
        print(f"{portfolio_name:<25} {as_of_date:<15} {num_holdings:>10} {created_short:<20}")

    print()
    conn.close()


def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python export_portfolio.py list")
        print("  python export_portfolio.py csv <portfolio_name> <date>")
        print("  python export_portfolio.py json <portfolio_name> <date>")
        print("  python export_portfolio.py broker <portfolio_name> <date> [amount]")
        print("\nExamples:")
        print("  python export_portfolio.py list")
        print("  python export_portfolio.py csv ALLW_SCALED 2025-10-06")
        print("  python export_portfolio.py json ALLW_ETF_ONLY 2025-10-06")
        print("  python export_portfolio.py broker ALLW_SCALED 2025-10-06 50000")
        sys.exit(1)

    command = sys.argv[1].lower()

    if command == 'list':
        list_available_portfolios()

    elif command == 'csv':
        if len(sys.argv) < 4:
            print("Error: csv command requires portfolio_name and date")
            sys.exit(1)
        portfolio_name = sys.argv[2]
        date = sys.argv[3]
        output = sys.argv[4] if len(sys.argv) > 4 else None
        export_to_csv(portfolio_name, date, output)

    elif command == 'json':
        if len(sys.argv) < 4:
            print("Error: json command requires portfolio_name and date")
            sys.exit(1)
        portfolio_name = sys.argv[2]
        date = sys.argv[3]
        output = sys.argv[4] if len(sys.argv) > 4 else None
        export_to_json(portfolio_name, date, output)

    elif command == 'broker':
        if len(sys.argv) < 4:
            print("Error: broker command requires portfolio_name and date")
            sys.exit(1)
        portfolio_name = sys.argv[2]
        date = sys.argv[3]
        amount = float(sys.argv[4]) if len(sys.argv) > 4 else 10000.0
        print_broker_format(portfolio_name, date, amount)

    else:
        print(f"Unknown command: {command}")
        sys.exit(1)


if __name__ == "__main__":
    main()
