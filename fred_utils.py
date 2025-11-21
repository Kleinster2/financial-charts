#!/usr/bin/env python
"""
Shared utilities for FRED (Federal Reserve Economic Data) operations.
"""
import pandas as pd


def download_from_fred(fred_code):
    """
    Download data from FRED.

    Args:
        fred_code: FRED series code (e.g., 'DGS10', 'RVXCLS')

    Returns:
        DataFrame with Date index and Close column, or None on error
    """
    url = f'https://fred.stlouisfed.org/graph/fredgraph.csv?id={fred_code}'

    try:
        df = pd.read_csv(url)
        df.columns = ['Date', 'Close']
        df['Date'] = pd.to_datetime(df['Date'])
        df.set_index('Date', inplace=True)
        df = df.dropna()
        return df
    except Exception as e:
        print(f"  ERROR: {str(e)[:50]}")
        return None
