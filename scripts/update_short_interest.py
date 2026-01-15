"""
Fetch and store short interest data from yfinance.

Usage:
  python fetch_short_interest.py AAPL MSFT TSLA         # Fetch for specific tickers
  python fetch_short_interest.py --priority             # Fetch priority tickers (Mag 7, semis, etc.)
  python fetch_short_interest.py --all                  # Fetch for all tickers with metadata

Short interest is reported by FINRA twice monthly. This script fetches the latest
SI data from yfinance and stores it in the short_interest table.
"""

import sys
import os
import sqlite3
import logging
import argparse
import time
from datetime import datetime
from typing import List, Optional, Dict

import yfinance as yf

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from constants import DB_PATH

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Priority tickers to track for short interest
PRIORITY_TICKERS = [
    # Mag 7
    'AAPL', 'MSFT', 'GOOGL', 'AMZN', 'META', 'NVDA', 'TSLA',
    # Semiconductors
    'TSM', 'AMD', 'AVGO', 'QCOM', 'INTC', 'MU', 'ASML', 'ARM', 'MRVL', 'LRCX', 'KLAC', 'AMAT',
    # AI/High-growth
    'PLTR', 'COIN', 'SNOW', 'DDOG', 'NET', 'CRWD', 'PANW', 'ZS', 'MDB',
    # EVs
    'RIVN', 'LCID', 'NIO', 'LI', 'XPEV',
    # Other notable
    'GME', 'AMC', 'BBBY', 'CVNA', 'SMCI', 'MSTR',
]


def get_short_interest_data(ticker: str) -> Optional[Dict]:
    """
    Fetch short interest data for a ticker from yfinance.
    Returns dict with SI fields or None if not available.
    """
    try:
        yf_ticker = yf.Ticker(ticker)
        info = yf_ticker.info

        if not info or 'sharesShort' not in info:
            return None

        # Extract settlement date (Unix timestamp)
        settlement_ts = info.get('dateShortInterest')
        if settlement_ts:
            settlement_date = datetime.fromtimestamp(settlement_ts).strftime('%Y-%m-%d')
        else:
            settlement_date = datetime.now().strftime('%Y-%m-%d')

        return {
            'ticker': ticker,
            'settlement_date': settlement_date,
            'short_interest': info.get('sharesShort'),
            'shares_outstanding': info.get('sharesOutstanding'),
            'short_percent_float': info.get('shortPercentOfFloat'),
            'short_percent_outstanding': info.get('sharesPercentSharesOut'),
            'days_to_cover': info.get('shortRatio'),
            'avg_daily_volume': info.get('averageDailyVolume10Day'),
            'source': 'yfinance',
        }

    except Exception as e:
        logger.warning(f"Error fetching SI for {ticker}: {e}")
        return None


def store_short_interest(conn: sqlite3.Connection, data: Dict) -> bool:
    """
    Store short interest data in the database.
    Uses INSERT OR REPLACE to handle updates.
    """
    try:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT OR REPLACE INTO short_interest
            (ticker, settlement_date, short_interest, shares_outstanding,
             short_percent_float, short_percent_outstanding, days_to_cover,
             avg_daily_volume, source, last_updated)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
        ''', (
            data['ticker'],
            data['settlement_date'],
            data['short_interest'],
            data['shares_outstanding'],
            data['short_percent_float'],
            data['short_percent_outstanding'],
            data['days_to_cover'],
            data['avg_daily_volume'],
            data['source'],
        ))
        return True
    except Exception as e:
        logger.error(f"Error storing SI for {data['ticker']}: {e}")
        return False


def fetch_and_store(tickers: List[str], delay: float = 0.5) -> tuple:
    """
    Fetch and store short interest for a list of tickers.
    Returns (success_count, fail_count).
    """
    conn = sqlite3.connect(DB_PATH)

    # Ensure table exists
    conn.execute('''
        CREATE TABLE IF NOT EXISTS short_interest (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ticker TEXT NOT NULL,
            settlement_date TEXT NOT NULL,
            short_interest REAL,
            shares_outstanding REAL,
            short_percent_float REAL,
            short_percent_outstanding REAL,
            days_to_cover REAL,
            avg_daily_volume REAL,
            source TEXT,
            last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            UNIQUE(ticker, settlement_date)
        )
    ''')

    success = 0
    fail = 0

    for i, ticker in enumerate(tickers):
        logger.info(f"[{i+1}/{len(tickers)}] Fetching {ticker}...")

        data = get_short_interest_data(ticker)
        if data:
            if store_short_interest(conn, data):
                si_pct = data['short_percent_float']
                if si_pct:
                    logger.info(f"  ✓ {ticker}: SI={si_pct*100:.2f}%, Days={data['days_to_cover']:.1f}")
                else:
                    logger.info(f"  ✓ {ticker}: SI data stored")
                success += 1
            else:
                fail += 1
        else:
            logger.warning(f"  ✗ {ticker}: No SI data available")
            fail += 1

        # Rate limiting
        if delay > 0 and i < len(tickers) - 1:
            time.sleep(delay)

    conn.commit()
    conn.close()

    return success, fail


def get_all_tickers_from_db() -> List[str]:
    """Get all tickers from ticker_metadata that are stocks."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Get tickers that look like stocks (not indices, futures, etc.)
    cursor.execute('''
        SELECT DISTINCT ticker FROM ticker_metadata
        WHERE data_type = 'stock'
        AND ticker NOT LIKE '^%'
        AND ticker NOT LIKE '%=F'
        AND ticker NOT LIKE '%=X'
        ORDER BY ticker
    ''')

    tickers = [row[0] for row in cursor.fetchall()]
    conn.close()

    return tickers


def main():
    parser = argparse.ArgumentParser(description='Fetch short interest data')
    parser.add_argument('tickers', nargs='*', help='Specific tickers to fetch')
    parser.add_argument('--priority', action='store_true', help='Fetch priority tickers')
    parser.add_argument('--all', action='store_true', help='Fetch all tickers from database')
    parser.add_argument('--delay', type=float, default=0.5, help='Delay between requests (seconds)')

    args = parser.parse_args()

    if args.tickers:
        tickers = [t.upper() for t in args.tickers]
    elif args.priority:
        tickers = PRIORITY_TICKERS
    elif args.all:
        tickers = get_all_tickers_from_db()
        if not tickers:
            logger.error("No tickers found in database")
            return
    else:
        parser.print_help()
        return

    logger.info(f"Fetching short interest for {len(tickers)} tickers...")
    success, fail = fetch_and_store(tickers, delay=args.delay)

    logger.info(f"\nComplete: {success} succeeded, {fail} failed")


if __name__ == '__main__':
    main()
