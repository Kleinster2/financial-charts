"""
Utility functions for automatic metadata management.
Fetches and cleans company names from yfinance.
"""

import sqlite3
import yfinance as yf
from constants import DB_PATH
from typing import List, Optional
import logging

logger = logging.getLogger(__name__)


def clean_company_name(name: str) -> str:
    """
    Remove corporate suffixes and clean up company names.

    Args:
        name: Raw company name from yfinance

    Returns:
        Cleaned company name
    """
    if not name:
        return name

    # Suffixes to remove (order matters - remove longer ones first)
    suffixes = [
        ' Corporation',
        ' Incorporated',
        ' Company',
        ' Corp.',
        ' Corp',
        ' Inc.',
        ' Inc',
        ' Limited',
        ' Ltd.',
        ' Ltd',
        ' Co.',
        ' Co',
        ' PLC',
        ' N.V.',
        ' SE',
        ' AG',
        ' S.A.',
        ' Holdings',
        ' Hldgs',
        ' Hldg.',
        ' Hldg',
        ' Group',
    ]

    cleaned = name

    # Remove suffixes
    for suffix in suffixes:
        if cleaned.endswith(suffix):
            cleaned = cleaned[:-len(suffix)].strip()

    # Remove trailing commas
    while cleaned.endswith(','):
        cleaned = cleaned[:-1].strip()

    # Remove "& Co." patterns
    if ' & Co.' in cleaned:
        cleaned = cleaned.replace(' & Co.', '').strip()
    if ' & Co' in cleaned:
        cleaned = cleaned.replace(' & Co', '').strip()

    # Remove dangling ampersands
    if cleaned.endswith(' &'):
        cleaned = cleaned[:-2].strip()

    return cleaned


def fetch_ticker_metadata(ticker: str) -> Optional[dict]:
    """
    Fetch metadata for a single ticker from yfinance.

    Args:
        ticker: Stock ticker symbol

    Returns:
        Dictionary with cleaned metadata or None if fetch fails
    """
    try:
        stock = yf.Ticker(ticker)
        info = stock.info

        raw_name = info.get('longName') or info.get('shortName', ticker)
        cleaned_name = clean_company_name(raw_name)

        return {
            'ticker': ticker,
            'name': cleaned_name,
            'table_name': 'stock_prices_daily',
            'data_type': 'stock'
        }
    except Exception as e:
        logger.warning(f"Failed to fetch metadata for {ticker}: {e}")
        return None


def update_ticker_metadata(tickers: List[str], db_path: str = None) -> dict:
    """
    Fetch and update metadata for multiple tickers.

    Args:
        tickers: List of ticker symbols
        db_path: Path to SQLite database (default: constants.DB_PATH)

    Returns:
        Dictionary with counts of successful/failed updates
    """
    if db_path is None:
        db_path = DB_PATH

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    successful = 0
    failed = 0
    skipped = 0

    for ticker in tickers:
        try:
            # Check if metadata already exists
            cursor.execute(
                "SELECT name FROM ticker_metadata WHERE ticker = ?",
                (ticker,)
            )
            existing = cursor.fetchone()

            if existing:
                logger.debug(f"Metadata already exists for {ticker}, skipping")
                skipped += 1
                continue

            # Fetch metadata
            metadata = fetch_ticker_metadata(ticker)

            if not metadata:
                failed += 1
                continue

            # Get data statistics from price table
            cursor.execute(f'''
                SELECT MIN(Date), MAX(Date), COUNT(*)
                FROM stock_prices_daily
                WHERE "{ticker}" IS NOT NULL
            ''')
            result = cursor.fetchone()

            if result and result[0]:
                first_date, last_date, data_points = result

                # Insert metadata
                cursor.execute('''
                    INSERT OR REPLACE INTO ticker_metadata
                    (ticker, name, table_name, data_type, first_date, last_date, data_points)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                ''', (
                    metadata['ticker'],
                    metadata['name'],
                    metadata['table_name'],
                    metadata['data_type'],
                    first_date,
                    last_date,
                    data_points
                ))

                logger.info(f"Added metadata for {ticker}: {metadata['name']}")
                successful += 1
            else:
                logger.warning(f"No price data found for {ticker}")
                failed += 1

        except Exception as e:
            logger.error(f"Error updating metadata for {ticker}: {e}")
            failed += 1

    conn.commit()
    conn.close()

    return {
        'successful': successful,
        'failed': failed,
        'skipped': skipped
    }


def auto_update_new_tickers(db_path: str = None) -> dict:
    """
    Automatically find tickers with data but no metadata and update them.

    Args:
        db_path: Path to SQLite database (default: constants.DB_PATH)

    Returns:
        Dictionary with update statistics
    """
    if db_path is None:
        db_path = DB_PATH

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Get all column names from price table
    cursor.execute("PRAGMA table_info(stock_prices_daily);")
    all_columns = [row[1] for row in cursor.fetchall() if row[1] != 'Date']

    # Get existing tickers in metadata
    cursor.execute("SELECT ticker FROM ticker_metadata")
    existing_tickers = {row[0] for row in cursor.fetchall()}

    # Find tickers without metadata
    new_tickers = [t for t in all_columns if t not in existing_tickers]

    conn.close()

    logger.info(f"Found {len(new_tickers)} tickers without metadata")

    if new_tickers:
        return update_ticker_metadata(new_tickers, db_path)

    return {'successful': 0, 'failed': 0, 'skipped': 0}
