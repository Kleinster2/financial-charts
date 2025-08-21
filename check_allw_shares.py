"""
check_allw_shares.py

Query the database to find the number of ALLW shares outstanding.
"""

import sqlite3
from pathlib import Path
from constants import DB_PATH, get_db_connection

def get_allw_shares_outstanding():
    db_path = Path(DB_PATH)
    print(f"Using database: {db_path}")

    if not db_path.exists():
        print(f"Error: Database not found at {db_path}")
        return
    
    try:
        conn = get_db_connection(row_factory=None)
        cursor = conn.cursor()
        
        # Get the two most recent dates with price data
        cursor.execute("""
            SELECT Date, ALLW 
            FROM stock_prices_daily 
            WHERE ALLW IS NOT NULL 
            ORDER BY Date DESC 
            LIMIT 2
        """)
        
        price_data = cursor.fetchall()
        if not price_data:
            print("Could not find price data for ALLW in the database.")
            return
            
        # Latest day
        latest_date, latest_price = price_data[0]
        
        # Get the most recent portfolio values for both days
        cursor.execute("""
            SELECT snapshot_date, SUM(market_value) as total_value
            FROM etf_holdings_daily
            WHERE etf = 'ALLW' 
            AND snapshot_date IN (
                SELECT DISTINCT snapshot_date 
                FROM etf_holdings_daily 
                WHERE etf = 'ALLW'
                ORDER BY snapshot_date DESC 
                LIMIT 2
            )
            GROUP BY snapshot_date
            ORDER BY snapshot_date DESC
        """)
        
        portfolio_data = {date: value for date, value in cursor.fetchall()}
        
        # Convert portfolio dates to datetime.date for comparison
        portfolio_dates = {}
        for date_str, value in portfolio_data.items():
            portfolio_dates[date_str] = value
        
        # Sort portfolio dates to get the most recent two
        sorted_dates = sorted(portfolio_dates.keys(), reverse=True)
        
        if len(sorted_dates) > 0:
            # Get the latest portfolio data
            latest_portfolio_date = sorted_dates[0]
            total_value = portfolio_data[latest_portfolio_date]
            shares_outstanding = total_value / latest_price
            
            print(f"\n=== {latest_date} ===")
            print(f"- ALLW Price: ${latest_price:.2f}")
            print(f"- Portfolio Value: ${total_value:,.2f}")
            print(f"- Estimated Shares Outstanding: {shares_outstanding:,.0f}")
            
            # Previous day data if available
            if len(price_data) > 1 and len(sorted_dates) > 1:
                prev_date, prev_price = price_data[1]
                prev_portfolio_date = sorted_dates[1]
                prev_total = portfolio_data[prev_portfolio_date]
                prev_shares = prev_total / prev_price
                
                print(f"\n=== {str(prev_date).split()[0]} ===")
                print(f"- ALLW Price: ${prev_price:.2f}")
                print(f"- Portfolio Value: ${prev_total:,.2f}")
                print(f"- Estimated Shares Outstanding: {prev_shares:,.0f}")
                
                # Calculate changes
                if prev_shares > 0:
                    shares_change = shares_outstanding - prev_shares
                    pct_change = (shares_change / prev_shares) * 100
                    print(f"\nDay-over-Day Change:")
                    print(f"- Shares: {shares_change:+,.0f} ({pct_change:+.2f}%)")
                    print(f"- Portfolio Value: ${(total_value - prev_total):+,.2f}")
                    print(f"- Share Price: ${(latest_price - prev_price):+.2f}")
            else:
                print("Insufficient data to calculate shares outstanding.")
        else:
            print("Could not find matching portfolio data for the price dates.")
        
    except Exception as e:
        print(f"Error querying database: {e}")
    finally:
        if 'conn' in locals():
            conn.close()

if __name__ == "__main__":
    get_allw_shares_outstanding()
