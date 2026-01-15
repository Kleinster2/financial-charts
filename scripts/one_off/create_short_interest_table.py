"""
Create database table for storing short interest time series data.

Short interest is reported by FINRA twice monthly (mid-month and end-of-month).
This table stores the historical SI data for charting and analysis.
"""

import sqlite3
import logging
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from constants import DB_PATH

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def create_short_interest_table():
    """Create table for short interest data"""

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Short Interest table - normalized format (one row per ticker per settlement date)
    cursor.execute('''
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

    # Create index for faster queries
    cursor.execute('''
        CREATE INDEX IF NOT EXISTS idx_short_interest_ticker
        ON short_interest(ticker)
    ''')

    cursor.execute('''
        CREATE INDEX IF NOT EXISTS idx_short_interest_date
        ON short_interest(settlement_date)
    ''')

    conn.commit()
    logger.info("✓ Created short_interest table")

    # Show table info
    cursor.execute("PRAGMA table_info(short_interest)")
    columns = cursor.fetchall()
    logger.info(f"Columns: {[c[1] for c in columns]}")

    conn.close()


if __name__ == '__main__':
    create_short_interest_table()
