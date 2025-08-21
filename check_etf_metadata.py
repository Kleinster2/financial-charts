import sqlite3
from constants import DB_PATH, get_db_connection

print(f"Using database: {DB_PATH}")

conn = get_db_connection()
cursor = conn.cursor()

# Check ETF metadata
print("=== ETF Metadata in ticker_metadata table ===")
cursor.execute("""
    SELECT ticker, name, data_type, data_points 
    FROM ticker_metadata 
    WHERE data_type = 'etf' 
    ORDER BY ticker
    LIMIT 20
""")
results = cursor.fetchall()

if results:
    for ticker, name, data_type, points in results:
        name_display = name if name else "(no name)"
        print(f"{ticker}: {name_display} ({points} data points)")
else:
    print("No ETF metadata found in ticker_metadata table")

# Count total ETFs
cursor.execute("SELECT COUNT(*) FROM ticker_metadata WHERE data_type = 'etf'")
total = cursor.fetchone()[0]
print(f"\nTotal ETFs in metadata: {total}")

# Check if we have any ETF names populated
cursor.execute("""
    SELECT COUNT(*) 
    FROM ticker_metadata 
    WHERE data_type = 'etf' AND name IS NOT NULL AND name != ''
""")
with_names = cursor.fetchone()[0]
print(f"ETFs with names: {with_names}")

# Sample some common ETFs to see if they have names
print("\n=== Common ETFs check ===")
common_etfs = ['SPY', 'QQQ', 'IWM', 'DIA', 'VTI', 'VOO', 'EFA', 'EEM', 'GLD', 'SLV']
for etf in common_etfs:
    cursor.execute("SELECT name FROM ticker_metadata WHERE ticker = ?", (etf,))
    result = cursor.fetchone()
    if result:
        name = result[0] if result[0] else "(no name)"
        print(f"{etf}: {name}")

conn.close()
