"""
check_allw_value.py

Query the database to get the total value of the ALLW portfolio.
Prints the total market value and number of holdings for the latest snapshot.
"""

import sqlite3
from pathlib import Path

def get_allw_value():
    db_path = Path(__file__).parent / "sp500_data.db"
    
    if not db_path.exists():
        print(f"Error: Database not found at {db_path}")
        return
    
    try:
        conn = sqlite3.connect(str(db_path))
        cursor = conn.cursor()
        
        # Get the two most recent snapshot dates
        cursor.execute("""
            SELECT DISTINCT snapshot_date 
            FROM etf_holdings_daily 
            WHERE etf = 'ALLW'
            ORDER BY snapshot_date DESC 
            LIMIT 2
        """)
        
        dates = cursor.fetchall()
        if not dates:
            print("No ALLW holdings data found in the database.")
            return
            
        latest_date = dates[0][0]
        prev_date = dates[1][0] if len(dates) > 1 else None
        
        # Get the sum of market values for the latest date
        cursor.execute("""
            SELECT 
                SUM(market_value) as total_value,
                COUNT(*) as num_holdings
            FROM etf_holdings_daily
            WHERE etf = 'ALLW' AND snapshot_date = ?
        """, (latest_date,))
        
        total_value, num_holdings = cursor.fetchone()
        
        if total_value is None:
            print(f"No holdings found for ALLW on {latest_date}")
            return
            
        print(f"\n=== ALLW Portfolio as of {latest_date} ===")
        print(f"- Total Market Value: ${total_value:,.2f}")
        print(f"- Number of Holdings: {num_holdings:,}")
        
        # Get previous day's value if available
        if prev_date:
            cursor.execute("""
                SELECT SUM(market_value) as total_value
                FROM etf_holdings_daily
                WHERE etf = 'ALLW' AND snapshot_date = ?
            """, (prev_date,))
            
            prev_total = cursor.fetchone()[0]
            if prev_total:
                change = total_value - prev_total
                pct_change = (change / prev_total) * 100
                print(f"\n=== Previous Day ({prev_date}) ===")
                print(f"- Total Market Value: ${prev_total:,.2f}")
                print(f"- Day-over-Day Change: ${change:+,.2f} ({pct_change:+.2f}%)")
        
        # Get top 5 holdings by weight
        cursor.execute("""
            SELECT ticker, name, weight, market_value
            FROM etf_holdings_daily
            WHERE etf = 'ALLW' AND snapshot_date = ?
            ORDER BY weight DESC
            LIMIT 5
        """, (latest_date,))
        
        print("\nTop 5 Holdings by Weight:")
        for ticker, name, weight, mv in cursor.fetchall():
            print(f"- {ticker}: {name} ({weight*100:.2f}%, ${mv:,.2f})")
        
    except Exception as e:
        print(f"Error querying database: {e}")
    finally:
        if 'conn' in locals():
            conn.close()

if __name__ == "__main__":
    get_allw_value()
