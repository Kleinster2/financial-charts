#!/usr/bin/env python3
"""
Backfill R&D, SG&A, interest expense, tax, and D&A from Alpha Vantage
into income_statement_annual and income_statement_quarterly tables.

Usage:
    python scripts/backfill_income_detail.py ORCL AAPL MSFT
    python scripts/backfill_income_detail.py --all  # all tickers in DB
"""
import os
import sys
import time
import sqlite3
import argparse
import requests

DB_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'market_data.db')

# Load .env
env_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '.env')
if os.path.exists(env_path):
    with open(env_path) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                key, val = line.split('=', 1)
                os.environ.setdefault(key.strip(), val.strip())

API_KEY = os.environ.get('ALPHA_VANTAGE_API_KEY', '')

# AV field -> DB column mapping
FIELD_MAP = {
    'researchAndDevelopment': 'research_and_development',
    'sellingGeneralAndAdministrative': 'selling_general_administrative',
    'interestExpense': 'interest_expense',
    'incomeTaxExpense': 'income_tax_expense',
    'depreciationAndAmortization': 'depreciation_amortization',
    # Also backfill core fields if they're NULL
    'totalRevenue': 'total_revenue',
    'costOfRevenue': 'cost_of_revenue',
    'grossProfit': 'gross_profit',
    'operatingIncome': 'operating_income',
    'netIncome': 'net_income',
    'ebit': None,  # skip, we use ebitda
    'ebitda': 'ebitda',
}


def fetch_income_statement(symbol):
    """Fetch income statement from Alpha Vantage."""
    url = "https://www.alphavantage.co/query"
    params = {
        'function': 'INCOME_STATEMENT',
        'symbol': symbol,
        'apikey': API_KEY,
    }
    resp = requests.get(url, params=params)
    data = resp.json()
    
    if 'Note' in data or 'Information' in data:
        msg = data.get('Note', data.get('Information', ''))
        print(f"  AV rate limit/error: {msg[:80]}")
        return None
    
    return data


def persist_reports(conn, ticker, reports, table):
    """Upsert income statement detail fields."""
    cursor = conn.cursor()
    updated = 0
    inserted = 0
    
    for report in reports:
        fiscal_date = report.get('fiscalDateEnding')
        if not fiscal_date:
            continue
        
        # Check if row exists
        cursor.execute(f"SELECT id FROM {table} WHERE ticker = ? AND fiscal_date_ending = ?",
                       (ticker, fiscal_date))
        row = cursor.fetchone()
        
        # Build update values
        updates = {}
        for av_field, db_col in FIELD_MAP.items():
            if db_col is None:
                continue
            val = report.get(av_field)
            if val is not None and val != 'None':
                try:
                    updates[db_col] = float(val)
                except (ValueError, TypeError):
                    continue
        
        if not updates:
            continue
        
        if row:
            # Update existing row with new detail columns
            set_clause = ', '.join(f'{col} = ?' for col in updates.keys())
            values = list(updates.values()) + [ticker, fiscal_date]
            cursor.execute(f"UPDATE {table} SET {set_clause} WHERE ticker = ? AND fiscal_date_ending = ?",
                           values)
            if cursor.rowcount > 0:
                updated += 1
        else:
            # Insert new row
            updates['ticker'] = ticker
            updates['fiscal_date_ending'] = fiscal_date
            cols = ', '.join(updates.keys())
            placeholders = ', '.join('?' * len(updates))
            cursor.execute(f"INSERT INTO {table} ({cols}) VALUES ({placeholders})",
                           list(updates.values()))
            inserted += 1
    
    conn.commit()
    return updated, inserted


def process_ticker(ticker):
    """Fetch and persist income statement details for a ticker."""
    print(f"\n{ticker}:")
    
    data = fetch_income_statement(ticker)
    if not data:
        return False
    
    conn = sqlite3.connect(DB_PATH)
    
    # Annual reports
    annual = data.get('annualReports', [])
    if annual:
        upd, ins = persist_reports(conn, ticker, annual, 'income_statement_annual')
        print(f"  Annual: {upd} updated, {ins} inserted ({len(annual)} reports)")
    
    # Quarterly reports
    quarterly = data.get('quarterlyReports', [])
    if quarterly:
        upd, ins = persist_reports(conn, ticker, quarterly, 'income_statement_quarterly')
        print(f"  Quarterly: {upd} updated, {ins} inserted ({len(quarterly)} reports)")
    
    conn.close()
    return True


def main():
    parser = argparse.ArgumentParser(description='Backfill income statement detail from Alpha Vantage')
    parser.add_argument('tickers', nargs='*', help='Tickers to backfill')
    parser.add_argument('--all', action='store_true', help='Backfill all tickers in DB')
    args = parser.parse_args()
    
    if not API_KEY:
        print("Error: ALPHA_VANTAGE_API_KEY not set")
        sys.exit(1)
    
    if args.all:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("SELECT DISTINCT ticker FROM income_statement_annual ORDER BY ticker")
        tickers = [row[0] for row in c.fetchall()]
        conn.close()
        print(f"Backfilling {len(tickers)} tickers")
    elif args.tickers:
        tickers = [t.upper() for t in args.tickers]
    else:
        print("Provide tickers or use --all")
        sys.exit(1)
    
    for i, ticker in enumerate(tickers):
        success = process_ticker(ticker)
        # AV rate limit: 5 calls/min on free tier, 12s spacing
        if success and i < len(tickers) - 1:
            print("  (waiting 13s for AV rate limit)")
            time.sleep(13)
    
    print("\nDone!")


if __name__ == '__main__':
    main()
