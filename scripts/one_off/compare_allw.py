import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent.parent.parent))
#!/usr/bin/env python3
"""Compare ALLW holdings between two dates."""

import sqlite3
import pandas as pd
from constants import DB_PATH, get_db_connection

def compare_allw_snapshots(date1: str, date2: str):
    """Compare ALLW holdings between two snapshot dates."""
    
    print(f"Using database: {DB_PATH}")
    conn = get_db_connection(row_factory=None)
    
    # Query holdings for both dates (including shares to detect flows)
    query = 'SELECT ticker, name, weight, shares FROM etf_holdings_daily WHERE etf = ? AND snapshot_date = ?'
    df1 = pd.read_sql_query(query, conn, params=('ALLW', date1))
    df2 = pd.read_sql_query(query, conn, params=('ALLW', date2))
    conn.close()
    
    if df1.empty:
        print(f"No data found for {date1}")
        return
    if df2.empty:
        print(f"No data found for {date2}")
        return
    
    # Convert weights and shares to numeric
    df1['weight'] = pd.to_numeric(df1['weight'], errors='coerce').fillna(0.0)
    df2['weight'] = pd.to_numeric(df2['weight'], errors='coerce').fillna(0.0)
    df1['shares'] = pd.to_numeric(df1['shares'], errors='coerce').fillna(0.0)
    df2['shares'] = pd.to_numeric(df2['shares'], errors='coerce').fillna(0.0)
    
    # Set ticker as index
    df1.set_index('ticker', inplace=True)
    df2.set_index('ticker', inplace=True)
    
    # Find added/removed positions
    tickers1 = set(df1.index)
    tickers2 = set(df2.index)
    added = sorted(tickers2 - tickers1)
    removed = sorted(tickers1 - tickers2)
    common = sorted(tickers1 & tickers2)
    
    # Calculate weight and share changes for common positions
    changes = []
    share_changes = []
    for ticker in common:
        w1 = df1.loc[ticker, 'weight'] * 100
        w2 = df2.loc[ticker, 'weight'] * 100
        s1 = df1.loc[ticker, 'shares']
        s2 = df2.loc[ticker, 'shares']
        delta_w = w2 - w1
        delta_s = s2 - s1
        pct_s = (delta_s / s1 * 100) if s1 > 0 else 0
        changes.append((ticker, w1, w2, delta_w))
        share_changes.append((ticker, s1, s2, delta_s, pct_s))
    
    # Sort by absolute change
    changes.sort(key=lambda x: abs(x[3]), reverse=True)
    
    # Print results
    print(f"\n=== ALLW Holdings Comparison: {date1} vs {date2} ===\n")
    
    print(f"Position count: {len(df1)} → {len(df2)} ({len(df2)-len(df1):+d})")
    print(f"Total weight: {df1['weight'].sum()*100:.2f}% → {df2['weight'].sum()*100:.2f}%\n")
    
    if added:
        print(f"Added positions ({len(added)}):")
        for ticker in added[:5]:
            print(f"  + {ticker}: {df2.loc[ticker, 'weight']*100:.2f}%")
        if len(added) > 5:
            print(f"  ... and {len(added)-5} more\n")
    else:
        print("No positions added\n")
    
    if removed:
        print(f"Removed positions ({len(removed)}):")
        for ticker in removed[:5]:
            print(f"  - {ticker}: {df1.loc[ticker, 'weight']*100:.2f}%")
        if len(removed) > 5:
            print(f"  ... and {len(removed)-5} more\n")
    else:
        print("No positions removed\n")
    
    if changes:
        print("Top weight changes:")
        for ticker, w1, w2, delta in changes[:10]:
            print(f"  {ticker}: {w1:.2f}% → {w2:.2f}% ({delta:+.2f}%)")
    
    # Analyze flows by looking at share changes
    print("\n=== Flow Analysis (Share Changes) ===\n")
    
    # Sort by absolute percentage share change
    share_changes.sort(key=lambda x: abs(x[4]), reverse=True)
    
    # Check if shares changed uniformly (indicating flows)
    non_zero_changes = [sc for sc in share_changes if abs(sc[3]) > 0.01]
    
    if non_zero_changes:
        # Calculate average percentage change in shares for major positions
        major_positions = [sc for sc in share_changes if sc[1] > 100]  # positions with >100 shares
        if major_positions:
            avg_pct_change = sum(sc[4] for sc in major_positions) / len(major_positions)
            
            if abs(avg_pct_change) > 0.1:  # More than 0.1% change
                if avg_pct_change > 0:
                    print(f"📈 INFLOWS DETECTED: Average share increase of {avg_pct_change:.2f}% across major positions")
                else:
                    print(f"📉 OUTFLOWS DETECTED: Average share decrease of {avg_pct_change:.2f}% across major positions")
            else:
                print("🔄 NO SIGNIFICANT FLOWS: Share changes are minimal (likely just rounding/settlement)")
        
        print("\nTop share changes:")
        for ticker, s1, s2, delta_s, pct_s in non_zero_changes[:10]:
            print(f"  {ticker}: {s1:,.0f} → {s2:,.0f} shares ({delta_s:+,.0f}, {pct_s:+.2f}%)")
    else:
        print("No significant share changes detected - positions appear static")

if __name__ == "__main__":
    compare_allw_snapshots('2025-08-05', '2025-08-06')
