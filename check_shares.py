#!/usr/bin/env python3
"""Check if shares data exists in ALLW holdings."""

import sqlite3

conn = sqlite3.connect('sp500_data.db')

# Get all ALLW data for 2025-08-06
query = """
SELECT ticker, shares, weight, market_value 
FROM etf_holdings_daily 
WHERE etf = 'ALLW' AND snapshot_date = '2025-08-06'
ORDER BY weight DESC
"""

df = conn.execute(query).fetchall()

print("ALLW Holdings for 2025-08-06:")
print("-" * 60)
print(f"{'Ticker':<10} {'Shares':>15} {'Weight':>10} {'Market Value':>15}")
print("-" * 60)

for ticker, shares, weight, market_value in df:
    shares_str = f"{shares:,.0f}" if shares is not None else "NULL"
    weight_str = f"{weight*100:.2f}%" if weight is not None else "NULL"
    mv_str = f"${market_value:,.0f}" if market_value is not None else "NULL"
    print(f"{ticker:<10} {shares_str:>15} {weight_str:>10} {mv_str:>15}")

# Count nulls
nulls_shares = sum(1 for t, s, w, m in df if s is None)
nulls_mv = sum(1 for t, s, w, m in df if m is None)

print("-" * 60)
print(f"Total positions: {len(df)}")
print(f"Positions with NULL shares: {nulls_shares}")
print(f"Positions with NULL market_value: {nulls_mv}")

conn.close()
