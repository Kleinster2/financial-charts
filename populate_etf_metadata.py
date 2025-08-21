"""
Populate ETF names in ticker_metadata table for tooltip display
"""
import sqlite3
import os
from constants import DB_PATH, get_db_connection

# Common ETF names mapping
ETF_NAMES = {
    'SPY': 'SPDR S&P 500 ETF Trust',
    'QQQ': 'Invesco QQQ Trust',
    'IWM': 'iShares Russell 2000 ETF',
    'DIA': 'SPDR Dow Jones Industrial Average ETF',
    'VTI': 'Vanguard Total Stock Market ETF',
    'VOO': 'Vanguard S&P 500 ETF',
    'EFA': 'iShares MSCI EAFE ETF',
    'EEM': 'iShares MSCI Emerging Markets ETF',
    'GLD': 'SPDR Gold Shares',
    'SLV': 'iShares Silver Trust',
    'XLF': 'Financial Select Sector SPDR Fund',
    'XLE': 'Energy Select Sector SPDR Fund', 
    'XLK': 'Technology Select Sector SPDR Fund',
    'XLV': 'Health Care Select Sector SPDR Fund',
    'XLI': 'Industrial Select Sector SPDR Fund',
    'XLY': 'Consumer Discretionary Select Sector SPDR',
    'XLP': 'Consumer Staples Select Sector SPDR',
    'XLU': 'Utilities Select Sector SPDR Fund',
    'XLB': 'Materials Select Sector SPDR Fund',
    'XLRE': 'Real Estate Select Sector SPDR Fund',
    'XLC': 'Communication Services Select Sector SPDR',
    'VNQ': 'Vanguard Real Estate ETF',
    'VEA': 'Vanguard FTSE Developed Markets ETF',
    'VWO': 'Vanguard FTSE Emerging Markets ETF',
    'AGG': 'iShares Core U.S. Aggregate Bond ETF',
    'TLT': 'iShares 20+ Year Treasury Bond ETF',
    'IEF': 'iShares 7-10 Year Treasury Bond ETF',
    'SHY': 'iShares 1-3 Year Treasury Bond ETF',
    'LQD': 'iShares iBoxx $ Investment Grade Corporate Bond ETF',
    'HYG': 'iShares iBoxx $ High Yield Corporate Bond ETF',
    'ARKK': 'ARK Innovation ETF',
    'ARKG': 'ARK Genomic Revolution ETF',
    'ARKQ': 'ARK Autonomous Technology & Robotics ETF',
    'ARKW': 'ARK Next Generation Internet ETF',
    'ARKF': 'ARK Fintech Innovation ETF',
    'ICLN': 'iShares Global Clean Energy ETF',
    'SOXX': 'iShares Semiconductor ETF',
    'IBB': 'iShares Biotechnology ETF',
    'VIG': 'Vanguard Dividend Appreciation ETF',
    'VYM': 'Vanguard High Dividend Yield ETF',
    'SCHD': 'Schwab US Dividend Equity ETF',
    'DVY': 'iShares Select Dividend ETF',
    'ALLW': 'SPDR MSCI ACWI Climate Action World ETF',
}

def main():
    print("=== Populating ETF metadata ===")
    
    print(f"Using database: {DB_PATH}")
    if not os.path.exists(DB_PATH):
        print(f"Database not found: {DB_PATH}")
        return
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # First, check what ETFs exist in stock_prices_daily
    print("\n1. Checking ETFs in stock_prices_daily...")
    cursor.execute("PRAGMA table_info(stock_prices_daily)")
    columns = [col[1] for col in cursor.fetchall() if col[1] != 'Date']
    
    etfs_in_prices = [col for col in columns if col in ETF_NAMES]
    print(f"Found {len(etfs_in_prices)} known ETFs in stock_prices_daily")
    
    # Update/insert ETF metadata
    print("\n2. Updating ticker_metadata with ETF names...")
    updated = 0
    inserted = 0
    
    for etf, name in ETF_NAMES.items():
        if etf not in columns:
            continue  # Skip ETFs not in our database
            
        # Check if ticker exists in metadata
        cursor.execute("SELECT ticker, name FROM ticker_metadata WHERE ticker = ?", (etf,))
        result = cursor.fetchone()
        
        if result:
            # Update existing entry
            cursor.execute("""
                UPDATE ticker_metadata 
                SET name = ?, data_type = 'etf'
                WHERE ticker = ?
            """, (name, etf))
            updated += 1
            print(f"Updated {etf}: {name}")
        else:
            # Get data range for new entry
            cursor.execute(f"""
                SELECT 
                    MIN(Date) as first_date,
                    MAX(Date) as last_date,
                    COUNT(*) as data_points
                FROM stock_prices_daily
                WHERE "{etf}" IS NOT NULL
            """)
            date_result = cursor.fetchone()
            
            if date_result and date_result[2] > 0:
                # Insert new entry
                cursor.execute("""
                    INSERT INTO ticker_metadata 
                    (ticker, name, table_name, data_type, first_date, last_date, data_points)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                """, (etf, name, 'stock_prices_daily', 'etf', 
                      date_result[0], date_result[1], date_result[2]))
                inserted += 1
                print(f"Inserted {etf}: {name}")
    
    conn.commit()
    
    print(f"\n=== Summary ===")
    print(f"Updated: {updated} ETFs")
    print(f"Inserted: {inserted} ETFs")
    print(f"Total ETFs with names: {updated + inserted}")
    
    # Verify the update
    print("\n3. Verifying ETF metadata...")
    cursor.execute("""
        SELECT ticker, name 
        FROM ticker_metadata 
        WHERE data_type = 'etf' OR ticker IN ({})
        ORDER BY ticker
        LIMIT 10
    """.format(','.join(['?'] * len(list(ETF_NAMES.keys())[:10]))), 
        list(ETF_NAMES.keys())[:10])
    
    results = cursor.fetchall()
    if results:
        print("Sample ETF metadata:")
        for ticker, name in results:
            print(f"  {ticker}: {name}")
    
    conn.close()
    print("\n✓ ETF metadata population complete!")

if __name__ == "__main__":
    main()
