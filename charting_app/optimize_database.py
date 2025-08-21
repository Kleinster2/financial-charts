"""
Database migration script to add indexes and metadata table for improved performance.
Run this script to optimize the SQLite market data database.
"""

import sqlite3
import os
import sys
import logging
from datetime import datetime

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Import centralized DB helpers
basedir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.join(basedir, '..'))
from constants import DB_PATH, get_db_connection

def create_indexes(conn):
    """Create indexes for commonly queried columns."""
    cursor = conn.cursor()
    
    indexes = [
        # Price data indexes
        ("idx_stock_prices_date", "stock_prices_daily", "Date"),
        ("idx_futures_prices_date", "futures_prices_daily", "Date"),
        
        # Volume data indexes
        ("idx_stock_volumes_date", "stock_volumes_daily", "Date"),
        ("idx_futures_volumes_date", "futures_volumes_daily", "Date"),
        
        # ETF data indexes (daily holdings)
        ("idx_etf_holdings_daily_date", "etf_holdings_daily", "snapshot_date"),
        ("idx_etf_holdings_daily_etf", "etf_holdings_daily", "etf"),
        ("idx_etf_holdings_daily_composite", "etf_holdings_daily", "snapshot_date, etf"),
        
        # Metadata indexes
        ("idx_stock_metadata_ticker", "stock_metadata", "ticker"),
        ("idx_ticker_metadata_ticker", "ticker_metadata", "ticker"),
    ]
    
    for index_name, table_name, columns in indexes:
        try:
            # Check if table exists
            cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name= ?", (table_name,))
            if not cursor.fetchone():
                logging.warning(f"Table {table_name} does not exist, skipping index {index_name}")
                continue
            
            # Check if index already exists
            cursor.execute(f"SELECT name FROM sqlite_master WHERE type='index' AND name= ?", (index_name,))
            if cursor.fetchone():
                logging.info(f"Index {index_name} already exists, skipping")
                continue
            
            # Create index
            sql = f"CREATE INDEX {index_name} ON {table_name}({columns})"
            cursor.execute(sql)
            logging.info(f"Created index: {index_name} on {table_name}({columns})")
            
        except sqlite3.Error as e:
            logging.error(f"Failed to create index {index_name}: {e}")
    
    conn.commit()

def create_ticker_metadata_table(conn):
    """Create a comprehensive ticker metadata table."""
    cursor = conn.cursor()
    
    # Check if table already exists
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='ticker_metadata'")
    if cursor.fetchone():
        logging.info("ticker_metadata table already exists")
        return
    
    # Create the metadata table
    cursor.execute("""
        CREATE TABLE ticker_metadata (
            ticker TEXT PRIMARY KEY,
            name TEXT,
            table_name TEXT NOT NULL,
            data_type TEXT NOT NULL,  -- 'stock', 'etf', 'future', 'fx', 'crypto'
            exchange TEXT,
            sector TEXT,
            industry TEXT,
            first_date DATE,
            last_date DATE,
            data_points INTEGER,
            last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            active BOOLEAN DEFAULT 1,
            notes TEXT
        )
    """)
    
    logging.info("Created ticker_metadata table")
    
    # Populate with existing data
    populate_ticker_metadata(conn)
    
    conn.commit()

def populate_ticker_metadata(conn):
    """Populate the ticker metadata table with existing data."""
    cursor = conn.cursor()
    
    # Clear existing data
    cursor.execute("DELETE FROM ticker_metadata")
    
    # Get all tables with ticker data
    tables_info = [
        ('stock_prices_daily', 'stock'),
        ('futures_prices_daily', 'future'),
    ]
    
    for table_name, data_type in tables_info:
        try:
            # Check if table exists
            cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name= ?", (table_name,))
            if not cursor.fetchone():
                continue
            
            # Get all columns (tickers) from the table
            cursor.execute(f"PRAGMA table_info({table_name})")
            columns = cursor.fetchall()
            
            for col in columns:
                ticker = col[1]  # Column name is the ticker
                if ticker == 'Date':
                    continue
                
                # Get date range and count for this ticker
                cursor.execute(f"""
                    SELECT 
                        MIN(Date) as first_date,
                        MAX(Date) as last_date,
                        COUNT(*) as data_points
                    FROM {table_name}
                    WHERE "{ticker}" IS NOT NULL
                """)
                
                result = cursor.fetchone()
                if result and result[2] > 0:  # Has data points
                    # Get name from stock_metadata if available
                    name = None
                    if data_type == 'stock':
                        cursor.execute("SELECT name FROM stock_metadata WHERE ticker = ?", (ticker,))
                        name_result = cursor.fetchone()
                        if name_result:
                            name = name_result[0]
                    
                    # Insert into ticker_metadata
                    cursor.execute("""
                        INSERT OR REPLACE INTO ticker_metadata 
                        (ticker, name, table_name, data_type, first_date, last_date, data_points)
                        VALUES (?, ?, ?, ?, ?, ?, ?)
                    """, (ticker, name, table_name, data_type, result[0], result[1], result[2]))
                    
                    logging.info(f"Added metadata for {ticker} ({data_type}): {result[2]} data points")
        
        except sqlite3.Error as e:
            logging.error(f"Error processing table {table_name}: {e}")
    
    # Add ETF metadata
    try:
        cursor.execute("SELECT DISTINCT etf FROM etf_holdings_daily")
        etfs = cursor.fetchall()
        for (etf,) in etfs:
            cursor.execute("""
                SELECT 
                    MIN(snapshot_date) as first_date,
                    MAX(snapshot_date) as last_date,
                    COUNT(DISTINCT snapshot_date) as data_points
                FROM etf_holdings_daily
                WHERE etf = ?
            """, (etf,))
            
            result = cursor.fetchone()
            if result and result[2] > 0:
                cursor.execute("""
                    INSERT OR REPLACE INTO ticker_metadata 
                    (ticker, table_name, data_type, first_date, last_date, data_points)
                    VALUES (?, ?, ?, ?, ?, ?)
                """, (etf, 'etf_holdings_daily', 'etf', result[0], result[1], result[2]))
                
                logging.info(f"Added metadata for ETF {etf}: {result[2]} data points")
    
    except sqlite3.Error as e:
        logging.error(f"Error processing ETF data: {e}")
    
    conn.commit()
    
    # Show summary
    cursor.execute("SELECT COUNT(*), data_type FROM ticker_metadata GROUP BY data_type")
    for count, dtype in cursor.fetchall():
        logging.info(f"Added {count} {dtype} tickers to metadata")

def analyze_database(conn):
    """Run ANALYZE to update SQLite statistics."""
    cursor = conn.cursor()
    cursor.execute("ANALYZE")
    logging.info("Updated database statistics with ANALYZE")
    conn.commit()

def main():
    """Main migration function."""
    logging.info(f"Starting database optimization for: {DB_PATH}")
    
    if not os.path.exists(DB_PATH):
        logging.error(f"Database not found at {DB_PATH}")
        sys.exit(1)
    
    try:
        # Connect to database
        conn = get_db_connection(row_factory=sqlite3.Row)
        
        # Run migrations
        logging.info("Creating indexes...")
        create_indexes(conn)
        
        logging.info("Creating ticker metadata table...")
        create_ticker_metadata_table(conn)
        
        logging.info("Analyzing database...")
        analyze_database(conn)
        
        # Get database size
        cursor = conn.cursor()
        cursor.execute("SELECT page_count * page_size as size FROM pragma_page_count(), pragma_page_size()")
        size_bytes = cursor.fetchone()[0]
        size_mb = size_bytes / (1024 * 1024)
        logging.info(f"Database size: {size_mb:.2f} MB")
        
        conn.close()
        logging.info("Database optimization completed successfully!")
        
    except sqlite3.Error as e:
        logging.error(f"Database error: {e}")
        sys.exit(1)
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
