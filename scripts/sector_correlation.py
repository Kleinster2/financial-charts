#!/usr/bin/env python
"""
Calculate correlation metrics for a sector grouping.

Usage:
    python scripts/sector_correlation.py MU SNDK WDC
    python scripts/sector_correlation.py --start 2024-01-01 NVDA AMD AVGO MRVL
"""

import argparse
import sqlite3
import pandas as pd
import numpy as np
from pathlib import Path

def calculate_sector_correlation(tickers, start_date='2024-01-01'):
    """Calculate correlation metrics for a set of tickers."""
    
    db_path = Path(__file__).parent.parent / 'market_data.db'
    conn = sqlite3.connect(db_path)
    
    # Build query
    ticker_cols = ', '.join([f'"{t}"' for t in tickers])
    query = f'SELECT Date, {ticker_cols} FROM stock_prices_daily WHERE Date >= "{start_date}" ORDER BY Date'
    
    try:
        df = pd.read_sql(query, conn)
    except Exception as e:
        print(f"Error: {e}")
        return None
    
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.set_index('Date')
    
    # Drop columns with all NaN
    df = df.dropna(axis=1, how='all')
    available = list(df.columns)
    missing = [t for t in tickers if t not in available]
    
    if missing:
        print(f"Warning: Missing tickers: {missing}")
    
    if len(available) < 2:
        print("Error: Need at least 2 tickers with data")
        return None
    
    # Calculate returns
    returns = df.pct_change().dropna()
    corr = returns.corr()
    
    # Get pairwise correlations
    mask = np.triu(np.ones_like(corr, dtype=bool), k=1)
    pairs = corr.where(mask).stack()
    
    avg_corr = pairs.mean()
    min_corr = pairs.min()
    max_corr = pairs.max()
    
    # Interpretation
    if avg_corr >= 0.60:
        interp = "Strong (tight sector)"
    elif avg_corr >= 0.40:
        interp = "Moderate (valid sector)"
    elif avg_corr >= 0.25:
        interp = "Weak (loose grouping)"
    else:
        interp = "Very weak (not a sector)"
    
    # Output
    print(f"\n=== SECTOR CORRELATION ANALYSIS ===")
    print(f"Tickers: {', '.join(available)}")
    print(f"Period: {start_date} to present")
    print(f"")
    print(f"## Correlation structure")
    print(f"")
    print(f"| Metric | Value | Interpretation |")
    print(f"|--------|-------|----------------|")
    print(f"| **Avg correlation** | **{avg_corr:.2f}** | {interp} |")
    print(f"| Range | {min_corr:.2f} - {max_corr:.2f} | Loosest to tightest pair |")
    print(f"| Period | {start_date} to present | |")
    print(f"")
    print(f"**Pairwise detail:**")
    print(f"| Pair | Correlation |")
    print(f"|------|-------------|")
    
    for (t1, t2), val in pairs.items():
        print(f"| {t1} - {t2} | {val:.2f} |")
    
    return avg_corr


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Calculate sector correlation')
    parser.add_argument('tickers', nargs='+', help='Ticker symbols')
    parser.add_argument('--start', default='2024-01-01', help='Start date (YYYY-MM-DD)')
    
    args = parser.parse_args()
    calculate_sector_correlation(args.tickers, args.start)
