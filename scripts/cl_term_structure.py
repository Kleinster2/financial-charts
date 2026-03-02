#!/usr/bin/env python3
"""
Build CL crude oil continuous contract series (CL1, CL2, CL3, ..., CL6)
by rolling through individual monthly contracts from yfinance.

Produces a historical chart showing the term structure over time.
Contango = deferred > front (CL6 above CL1). Backwardation = opposite.

Usage:
    python scripts/cl_term_structure.py                    # chart from 2020
    python scripts/cl_term_structure.py --start 2023-01-01 # custom start
    python scripts/cl_term_structure.py --spread           # plot CL6-CL1 spread
"""
import argparse
import os
import sys
from datetime import datetime, timedelta

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import pandas as pd
import yfinance as yf

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                          "investing", "attachments")

# CL month codes: F=Jan, G=Feb, H=Mar, J=Apr, K=May, M=Jun,
#                 N=Jul, Q=Aug, U=Sep, V=Oct, X=Nov, Z=Dec
MONTH_CODES = ['F', 'G', 'H', 'J', 'K', 'M', 'N', 'Q', 'U', 'V', 'X', 'Z']
MONTH_NAMES = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
               'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']


def contract_ticker(month_idx, year):
    """Build yfinance ticker for a CL contract. month_idx: 0=Jan, 11=Dec."""
    return f"CL{MONTH_CODES[month_idx]}{year % 100:02d}.NYM"


def approx_expiry(month_idx, year):
    """Approximate CL expiry: ~20th of the month before delivery month."""
    # Delivery month
    del_month = month_idx + 1  # 1-indexed
    del_year = year
    # Month before delivery
    exp_month = del_month - 1
    exp_year = del_year
    if exp_month < 1:
        exp_month = 12
        exp_year -= 1
    return datetime(exp_year, exp_month, 20)


def build_contract_list(start_year, end_year):
    """Build list of (ticker, delivery_month_idx, delivery_year, approx_expiry)."""
    contracts = []
    for y in range(start_year, end_year + 1):
        for m in range(12):
            ticker = contract_ticker(m, y)
            exp = approx_expiry(m, y)
            contracts.append((ticker, m, y, exp))
    return contracts


def download_contracts(contracts):
    """Download price history for all contracts. Returns dict of ticker -> Series."""
    tickers = [c[0] for c in contracts]
    print(f"Downloading {len(tickers)} CL contracts...")
    # Download in batch
    data = yf.download(tickers, period="max", progress=True, group_by="ticker")

    series = {}
    for t in tickers:
        try:
            if len(tickers) == 1:
                s = data["Close"].dropna()
            else:
                s = data[t]["Close"].dropna()
            if len(s) > 0:
                series[t] = s
        except (KeyError, TypeError):
            pass
    print(f"Got data for {len(series)} contracts")
    return series


def build_continuous(contracts, series, n_months=6):
    """
    For each trading date, identify which contracts are CL1 through CL{n_months}
    based on approximate expiry dates. Returns DataFrame with CL1..CL{n} columns.
    """
    # Get union of all dates
    all_dates = sorted(set().union(*(s.index for s in series.values())))

    result = {f"CL{i+1}": [] for i in range(n_months)}
    result_dates = []

    for date in all_dates:
        dt = pd.Timestamp(date).to_pydatetime()
        # Find contracts that haven't expired yet, sorted by expiry
        active = [(c[0], c[3]) for c in contracts
                  if c[3] > dt and c[0] in series]
        active.sort(key=lambda x: x[1])

        if len(active) < n_months:
            continue

        row_valid = True
        row = {}
        for i in range(n_months):
            ticker = active[i][0]
            s = series[ticker]
            if date in s.index:
                row[f"CL{i+1}"] = float(s.loc[date])
            else:
                row_valid = False
                break

        if row_valid:
            result_dates.append(date)
            for k, v in row.items():
                result[k].append(v)

    df = pd.DataFrame(result, index=pd.DatetimeIndex(result_dates))
    return df


def plot_term_structure(df, start_date, output_path):
    """Plot CL1-CL6 continuous series."""
    df = df[df.index >= start_date]

    fig, ax = plt.subplots(figsize=(14, 7))

    colors = ['#2962FF', '#E91E63', '#4CAF50', '#FF9800', '#9C27B0', '#00BCD4']
    for i, col in enumerate(df.columns):
        ax.plot(df.index, df[col], color=colors[i % len(colors)],
                linewidth=1.5, label=col, alpha=0.85)

    ax.set_ylabel("$/barrel", fontsize=12)
    ax.legend(fontsize=11, loc='upper left')
    ax.grid(True, alpha=0.3)
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=3))
    fig.autofmt_xdate()

    # Shade contango (CL6 > CL1) vs backwardation
    ax.fill_between(df.index, df['CL1'], df['CL6'],
                    where=df['CL6'] > df['CL1'],
                    alpha=0.08, color='red', label='_contango')
    ax.fill_between(df.index, df['CL1'], df['CL6'],
                    where=df['CL6'] <= df['CL1'],
                    alpha=0.08, color='green', label='_backwardation')

    plt.tight_layout()
    fig.savefig(output_path, dpi=150, bbox_inches='tight')
    plt.close(fig)
    print(f"Saved: {output_path} ({os.path.getsize(output_path):,} bytes)")


def plot_spread(df, start_date, output_path):
    """Plot CL6-CL1 spread (positive = contango, negative = backwardation)."""
    df = df[df.index >= start_date].copy()
    df['spread'] = df['CL6'] - df['CL1']

    fig, ax = plt.subplots(figsize=(14, 5))

    ax.fill_between(df.index, 0, df['spread'],
                    where=df['spread'] >= 0,
                    color='#E53935', alpha=0.4, label='Contango')
    ax.fill_between(df.index, 0, df['spread'],
                    where=df['spread'] < 0,
                    color='#43A047', alpha=0.4, label='Backwardation')
    ax.plot(df.index, df['spread'], color='#333333', linewidth=1)
    ax.axhline(0, color='black', linewidth=0.8)

    ax.set_ylabel("CL6 − CL1 ($/barrel)", fontsize=12)
    ax.legend(fontsize=11)
    ax.grid(True, alpha=0.3)
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=3))
    fig.autofmt_xdate()

    plt.tight_layout()
    fig.savefig(output_path, dpi=150, bbox_inches='tight')
    plt.close(fig)
    print(f"Saved: {output_path} ({os.path.getsize(output_path):,} bytes)")


def main():
    parser = argparse.ArgumentParser(description="CL crude oil term structure chart")
    parser.add_argument("--start", default="2020-01-01", help="Chart start date")
    parser.add_argument("--spread", action="store_true", help="Also plot CL6-CL1 spread")
    parser.add_argument("--months", type=int, default=6, help="Number of forward months")
    args = parser.parse_args()

    start_date = pd.Timestamp(args.start)
    start_year = max(start_date.year - 1, 2017)
    end_year = datetime.now().year + 3

    contracts = build_contract_list(start_year, end_year)
    series = download_contracts(contracts)
    df = build_continuous(contracts, series, n_months=args.months)
    print(f"Built continuous series: {len(df)} trading days, {df.columns.tolist()}")

    out_path = os.path.join(OUTPUT_DIR, "cl-term-structure.png")
    plot_term_structure(df, start_date, out_path)

    if args.spread:
        spread_path = os.path.join(OUTPUT_DIR, "cl-contango-spread.png")
        plot_spread(df, start_date, spread_path)


if __name__ == "__main__":
    main()
