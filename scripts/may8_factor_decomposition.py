"""May 8 2026 factor vs idiosyncratic decomposition for the Space pure-plays cohort.

For each name, decompose the May 8 single-session log return into:
  - Factor component (PC1 loading × PC1 score on May 8)
  - Idiosyncratic component (residual)

Tells us which names participated as the factor predicted, and which moved more
or less than basket-level co-movement would explain.
"""
from __future__ import annotations
import sqlite3
from datetime import date, timedelta
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.decomposition import PCA

DB = Path(__file__).resolve().parent.parent / "market_data.db"
COHORT = ["RKLB", "RDW", "LUNR", "BKSY", "ASTS", "SPIR", "PL"]
END = date(2026, 5, 8)
START = (END - timedelta(days=365)).isoformat()


def load(tickers, start, end):
    placeholders = ", ".join("?" for _ in tickers)
    sql = f"SELECT Date, Ticker, Close FROM prices_long WHERE Ticker IN ({placeholders}) AND Date BETWEEN ? AND ? ORDER BY Date"
    with sqlite3.connect(DB) as conn:
        df = pd.read_sql(sql, conn, params=tickers + [start, end])
    df["Date"] = pd.to_datetime(df["Date"])
    df = df.pivot(index="Date", columns="Ticker", values="Close")
    df = df.apply(pd.to_numeric, errors="coerce")
    return df.replace({0: np.nan})


prices = load(COHORT, START, (END + timedelta(days=1)).isoformat())
rets = np.log(prices / prices.shift(1)).dropna()

# Fit PCA on 1Y returns
pca = PCA(n_components=3)
pca.fit(rets.values)
pc1_load = pca.components_[0]
if pc1_load.mean() < 0:
    pc1_load = -pc1_load
pc1_var = pca.explained_variance_ratio_[0]

# May 8 returns
may8 = rets.loc["2026-05-08"]

# PC1 score on May 8 (projection of May 8 return vector onto PC1)
pc1_score_may8 = float(may8.values @ pc1_load)

# Decompose each name's return
print("MAY 8 2026 FACTOR DECOMPOSITION")
print(f"PC1 score on May 8: {pc1_score_may8:.4f}")
print(f"PC1 explained variance (1Y): {pc1_var:.1%}")
print()
print(f"{'Ticker':<8} {'Actual %':>10} {'Loading':>10} {'Factor %':>10} {'Idio %':>10} {'Idio share':>12}")
print("-" * 65)

results = []
for t in COHORT:
    actual_log = float(may8[t])
    actual_pct = (np.exp(actual_log) - 1) * 100
    loading = pc1_load[COHORT.index(t)]
    factor_log = loading * pc1_score_may8
    factor_pct = (np.exp(factor_log) - 1) * 100
    idio_log = actual_log - factor_log
    idio_pct = (np.exp(idio_log) - 1) * 100
    idio_share = abs(idio_log) / (abs(factor_log) + abs(idio_log)) * 100
    results.append((t, actual_pct, loading, factor_pct, idio_pct, idio_share))
    print(f"{t:<8} {actual_pct:>+10.2f} {loading:>+10.4f} {factor_pct:>+10.2f} {idio_pct:>+10.2f} {idio_share:>11.1f}%")

# Aggregate stats
total_basket_log = float(may8.mean())
total_basket_pct = (np.exp(total_basket_log) - 1) * 100
factor_explains = float(np.var([loading * pc1_score_may8 for loading in pc1_load])) / float(np.var(may8.values))

print()
print(f"Basket equal-weighted move: {total_basket_pct:+.2f}%")
print(f"PC1 explains {factor_explains:.1%} of May 8 cross-sectional variance")
