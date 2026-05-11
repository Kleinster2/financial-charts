"""Three-part analysis on the Space pure-plays cohort:

1. RDW + LUNR factor-clean hypothesis — does the 2-name pair replicate the
   7-name basket factor?

2. Optimal subsets — for every 2-name and 3-name subset, compute tracking
   correlation to the full equal-weighted basket. Find the minimum-name
   expression that captures the factor.

3. PC2 pair-trade backtest — long the PC2-positive sleeve (data: SPIR/PL/BKSY)
   short the PC2-negative sleeve (hardware: RKLB/RDW/LUNR/ASTS). Has the
   realized return spread matched the PC2 implication?
"""
from __future__ import annotations
import sqlite3
from datetime import date, timedelta
from itertools import combinations
from pathlib import Path

import numpy as np
import pandas as pd

DB = Path(__file__).resolve().parent.parent / "market_data.db"
COHORT = ["RKLB", "RDW", "LUNR", "BKSY", "ASTS", "SPIR", "PL"]
DATA_SLEEVE = ["SPIR", "PL", "BKSY"]
HARDWARE_SLEEVE = ["RKLB", "RDW", "LUNR", "ASTS"]
END = date(2026, 5, 8)
START = (END - timedelta(days=365)).isoformat()


def load(tickers, start, end):
    ph = ",".join("?" * len(tickers))
    sql = (
        f"SELECT Date, Ticker, Close FROM prices_long "
        f"WHERE Ticker IN ({ph}) AND Date BETWEEN ? AND ? ORDER BY Date"
    )
    with sqlite3.connect(DB) as conn:
        df = pd.read_sql(sql, conn, params=tickers + [start, end])
    df["Date"] = pd.to_datetime(df["Date"])
    df = df.pivot(index="Date", columns="Ticker", values="Close")
    df = df.apply(pd.to_numeric, errors="coerce")
    return df.replace({0: np.nan})


prices = load(COHORT, START, (END + timedelta(days=1)).isoformat())
rets = np.log(prices / prices.shift(1)).dropna()
basket = rets[COHORT].mean(axis=1)

# === 1. RDW + LUNR PAIR ===
print("=" * 72)
print("1. RDW + LUNR factor-clean hypothesis")
print("=" * 72)

pair = rets[["RDW", "LUNR"]].mean(axis=1)
corr = pair.corr(basket)
tracking_err = (pair - basket).std() * np.sqrt(252)
basket_vol = basket.std() * np.sqrt(252)
pair_vol = pair.std() * np.sqrt(252)
pair_cum = (np.exp(pair.cumsum()) - 1) * 100
basket_cum = (np.exp(basket.cumsum()) - 1) * 100

print(f"  Correlation to basket:    {corr:.4f}")
print(f"  Tracking error (annualized): {tracking_err:.2%}")
print(f"  Pair annualized vol:       {pair_vol:.2%}")
print(f"  Basket annualized vol:     {basket_vol:.2%}")
print(f"  Pair cumulative return:    {pair_cum.iloc[-1]:+.1f}%")
print(f"  Basket cumulative return:  {basket_cum.iloc[-1]:+.1f}%")

# === 2. OPTIMAL SUBSETS ===
print()
print("=" * 72)
print("2. Optimal subsets — tracking correlation to full 7-name basket")
print("=" * 72)

results_2 = []
for combo in combinations(COHORT, 2):
    sub = rets[list(combo)].mean(axis=1)
    c = sub.corr(basket)
    te = (sub - basket).std() * np.sqrt(252)
    results_2.append((combo, c, te))

results_3 = []
for combo in combinations(COHORT, 3):
    sub = rets[list(combo)].mean(axis=1)
    c = sub.corr(basket)
    te = (sub - basket).std() * np.sqrt(252)
    results_3.append((combo, c, te))

print(f"\nTop 5 2-name subsets by correlation to basket:")
print(f"{'Pair':<20} {'Correlation':>12} {'Tracking Err':>14}")
for combo, c, te in sorted(results_2, key=lambda x: -x[1])[:5]:
    print(f"{', '.join(combo):<20} {c:>12.4f} {te:>13.2%}")

print(f"\nBottom 3 2-name subsets (worst factor proxies):")
for combo, c, te in sorted(results_2, key=lambda x: x[1])[:3]:
    print(f"{', '.join(combo):<20} {c:>12.4f} {te:>13.2%}")

print(f"\nTop 5 3-name subsets by correlation to basket:")
for combo, c, te in sorted(results_3, key=lambda x: -x[1])[:5]:
    print(f"{', '.join(combo):<20} {c:>12.4f} {te:>13.2%}")

# === 3. PC2 PAIR TRADE ===
print()
print("=" * 72)
print("3. PC2 pair-trade backtest — data sleeve vs hardware sleeve")
print("=" * 72)

data_basket = rets[DATA_SLEEVE].mean(axis=1)
hw_basket = rets[HARDWARE_SLEEVE].mean(axis=1)
pair_spread = data_basket - hw_basket  # long data, short hardware
spread_cum = pair_spread.cumsum() * 100  # cumulative log-spread in percent

data_cum = (np.exp(data_basket.cumsum()) - 1) * 100
hw_cum = (np.exp(hw_basket.cumsum()) - 1) * 100

print(f"  Data sleeve (SPIR, PL, BKSY) cumulative return:    {data_cum.iloc[-1]:+.1f}%")
print(f"  Hardware sleeve (RKLB, RDW, LUNR, ASTS) cum return: {hw_cum.iloc[-1]:+.1f}%")
print(f"  Long data / short hardware spread (log %):          {spread_cum.iloc[-1]:+.1f}%")
print(f"  Spread vol (annualized):                            {pair_spread.std() * np.sqrt(252):.2%}")
print(f"  Spread Sharpe (annualized):                         {(pair_spread.mean() * 252) / (pair_spread.std() * np.sqrt(252)):.2f}")

# Identify periods of biggest spread movement
worst_30d_for_data = pair_spread.rolling(30).sum().idxmin()
best_30d_for_data = pair_spread.rolling(30).sum().idxmax()
print(f"\n  Best 30-day spread (data outperformed):  {best_30d_for_data.strftime('%Y-%m-%d')} (cumulative +{pair_spread.rolling(30).sum().max() * 100:.1f}%)")
print(f"  Worst 30-day spread (hardware outperformed): {worst_30d_for_data.strftime('%Y-%m-%d')} (cumulative {pair_spread.rolling(30).sum().min() * 100:.1f}%)")
