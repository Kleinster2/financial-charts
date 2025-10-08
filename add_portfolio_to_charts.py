#!/usr/bin/env python3
"""
add_portfolio_to_charts.py

Add replication portfolio tickers to the charting app workspace.
"""

import json
import sys
from pathlib import Path

from constants import DB_PATH, get_db_connection


def get_portfolio_tickers(portfolio_name: str, as_of_date: str, include_cash: bool = False):
    """Get list of tickers from a portfolio."""
    conn = get_db_connection()

    query = """
        SELECT ticker, name, weight
        FROM replication_portfolios
        WHERE portfolio_name = ? AND as_of_date = ?
        ORDER BY weight DESC
    """

    cursor = conn.execute(query, (portfolio_name, as_of_date))
    rows = cursor.fetchall()
    conn.close()

    if include_cash:
        return [(row[0], row[2]) for row in rows]
    else:
        return [(row[0], row[2]) for row in rows if row[0] != 'CASH']


def add_portfolio_to_workspace(portfolio_name: str, as_of_date: str,
                                workspace_file: str, page: str = "22"):
    """Add portfolio chart to the workspace JSON."""

    # Load workspace
    workspace_path = Path(workspace_file)
    if not workspace_path.exists():
        print(f"Error: Workspace file not found: {workspace_file}")
        return False

    with open(workspace_path, 'r', encoding='utf-8') as f:
        workspace = json.load(f)

    # Get portfolio tickers
    tickers_with_weights = get_portfolio_tickers(portfolio_name, as_of_date, include_cash=False)

    if not tickers_with_weights:
        print(f"Error: No tickers found for portfolio {portfolio_name} as of {as_of_date}")
        return False

    tickers = [t[0] for t in tickers_with_weights]
    weights = {t[0]: t[1] for t in tickers_with_weights}

    print(f"\nPortfolio tickers: {', '.join(tickers)}")

    # Create multipliers based on weights (optional - for visual comparison)
    # Normalize to make largest weight = 1.0
    max_weight = max(weights.values())
    multipliers = {ticker: 1.0 for ticker in tickers}  # Or: weight/max_weight for scaled view

    # Create new chart card
    new_card = {
        "page": page,
        "tickers": tickers,
        "showDiff": False,
        "showAvg": False,
        "showVol": False,
        "multipliers": multipliers,
        "hidden": [],
        "range": {"from": 1704067200, "to": 1759708800},  # Default range ~2024-2025
        "useRaw": False,
        "title": portfolio_name.replace('_', ' '),
        "lastLabelVisible": False,
        "showZeroLine": False,
        "height": 500,
        "fontSize": 12
    }

    # Check if chart already exists
    existing_idx = None
    for idx, card in enumerate(workspace['cards']):
        if card.get('title') == new_card['title'] and card.get('page') == page:
            existing_idx = idx
            break

    if existing_idx is not None:
        print(f"Updating existing chart at index {existing_idx}")
        workspace['cards'][existing_idx] = new_card
    else:
        print(f"Adding new chart to page {page}")
        workspace['cards'].append(new_card)

    # Save workspace
    with open(workspace_path, 'w', encoding='utf-8') as f:
        json.dump(workspace, f, indent=2)

    print(f"[SUCCESS] Chart added to workspace: {portfolio_name}")
    print(f"   Page: {page}")
    print(f"   Tickers: {len(tickers)}")

    return True


def main():
    # Default workspace path
    workspace_file = Path(__file__).parent / "charting_app" / "workspace.json"

    if len(sys.argv) < 3:
        print("Usage:")
        print("  python add_portfolio_to_charts.py <portfolio_name> <date> [page]")
        print("\nExamples:")
        print("  python add_portfolio_to_charts.py ALLW_SCALED 2025-10-06")
        print("  python add_portfolio_to_charts.py ALLW_ETF_ONLY 2025-10-06 22")
        print("\nAvailable portfolios:")
        conn = get_db_connection()
        cursor = conn.execute("""
            SELECT DISTINCT portfolio_name, as_of_date
            FROM replication_portfolios
            ORDER BY as_of_date DESC
        """)
        for portfolio_name, date in cursor.fetchall():
            print(f"  - {portfolio_name} ({date})")
        conn.close()
        sys.exit(1)

    portfolio_name = sys.argv[1]
    as_of_date = sys.argv[2]
    page = sys.argv[3] if len(sys.argv) > 3 else "22"

    success = add_portfolio_to_workspace(
        portfolio_name, as_of_date, str(workspace_file), page
    )

    if success:
        print(f"\n[DONE] Reload your charting app to see the new chart on page {page}")
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
