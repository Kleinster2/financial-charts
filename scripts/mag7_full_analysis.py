"""Apply the Space pure-plays-style framework to the Mag 7 cohort.

Mag 7 hypothesis: per the existing mag7.yaml comment, Mag 7 is suspected to be a
"media construct" rather than a real cluster. Run the full diagnostic battery
to falsify (or validate) that hypothesis.

(a) Basic validation diagnostics + matched-methodology cross-cohort comparison
(b) Subset optimization — what sub-pair / sub-triple WOULD cluster within Mag 7
(c) Stability check across 3Y / 2Y / 1Y / YTD windows
(d) PC1 + PC2 + PC3 inspection
(e) Factor decomposition vs SPY / QQQ / SMH
"""
from __future__ import annotations
import sqlite3
from datetime import date, timedelta
from itertools import combinations
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.linear_model import LinearRegression

DB = Path(__file__).resolve().parent.parent / "market_data.db"
COHORT = ["AAPL", "MSFT", "GOOGL", "AMZN", "META", "NVDA", "TSLA"]
BENCHMARKS = ["SPY", "QQQ", "SMH", "XLK"]
END = date(2026, 5, 8)


def load(tickers, start, end):
    placeholders = ", ".join("?" for _ in tickers)
    sql = f"SELECT Date, Ticker, Close FROM prices_long WHERE Ticker IN ({placeholders}) AND Date BETWEEN ? AND ? ORDER BY Date"
    with sqlite3.connect(DB) as conn:
        df = pd.read_sql(sql, conn, params=tickers + [start, end])
    df["Date"] = pd.to_datetime(df["Date"])
    df = df.pivot(index="Date", columns="Ticker", values="Close")
    df = df.apply(pd.to_numeric, errors="coerce")
    return df.replace({0: np.nan})


# === (a) BASIC + (c) STABILITY ===
print("=" * 72)
print("(a) Basic validation + (c) stability across windows")
print("=" * 72)

start_3y = (END - timedelta(days=1095)).isoformat()
prices = load(COHORT + BENCHMARKS, start_3y, (END + timedelta(days=1)).isoformat())
rets = np.log(prices / prices.shift(1)).dropna()

WINDOWS = {
    "YTD 2026": date(2026, 1, 2),
    "1Y": END - timedelta(days=365),
    "2Y": END - timedelta(days=730),
    "3Y": END - timedelta(days=1095),
}

print(f"\n{'Window':<10} {'obs':>5} {'intra':>7} {'range':>14} {'PC1':>7} {'PC2':>7} {'vs SPY':>8} {'gap':>7}")
print("-" * 75)
for name, cutoff in WINDOWS.items():
    sub = rets.loc[rets.index >= pd.Timestamp(cutoff)]
    cohort_sub = sub[COHORT].dropna()
    if len(cohort_sub) < 30:
        print(f"{name:<10} insufficient data")
        continue
    corr = cohort_sub.corr()
    mask = np.triu(np.ones_like(corr, dtype=bool), k=1)
    pair_corrs = corr.where(mask).stack()
    intra = float(pair_corrs.mean())
    pmin, pmax = float(pair_corrs.min()), float(pair_corrs.max())
    pca = PCA(n_components=3)
    pca.fit(cohort_sub.values)
    pc1, pc2 = pca.explained_variance_ratio_[0], pca.explained_variance_ratio_[1]
    spy_rets = sub["SPY"].reindex(cohort_sub.index).fillna(0)
    cohort_avg = cohort_sub.mean(axis=1)
    vs_spy = cohort_avg.corr(spy_rets)
    gap = intra - vs_spy
    print(f"{name:<10} {len(cohort_sub):>5} {intra:>7.3f} [{pmin:.2f},{pmax:.2f}] {pc1:>7.1%} {pc2:>7.1%} {vs_spy:>8.3f} {gap:>+7.3f}")


# === (b) SUBSET OPTIMIZATION ===
print()
print("=" * 72)
print("(b) Within-Mag-7 subset optimization — does ANY sub-pair cluster?")
print("=" * 72)

cutoff_1y = pd.Timestamp(END - timedelta(days=365))
rets_1y = rets.loc[rets.index >= cutoff_1y]
full_basket = rets_1y[COHORT].mean(axis=1)

print(f"\nAll 21 pairs ranked by intra-correlation (the question: does any 2-name pair cluster?):")
print(f"{'Pair':<18} {'Intra-corr':>11} {'Sharpe':>8} {'Cum %':>10}")
pair_results = []
for combo in combinations(COHORT, 2):
    pair_rets = rets_1y[list(combo)]
    corr = pair_rets.iloc[:, 0].corr(pair_rets.iloc[:, 1])
    basket_pair = pair_rets.mean(axis=1)
    sharpe = (basket_pair.mean() * 252) / (basket_pair.std() * np.sqrt(252))
    cum_pct = (np.exp(basket_pair.sum()) - 1) * 100
    pair_results.append((combo, corr, sharpe, cum_pct))

for combo, corr, sharpe, cum in sorted(pair_results, key=lambda x: -x[1])[:7]:
    print(f"{', '.join(combo):<18} {corr:>11.3f} {sharpe:>8.2f} {cum:>+9.1f}%")

print(f"\nBottom-3 pairs (least correlated):")
for combo, corr, sharpe, cum in sorted(pair_results, key=lambda x: x[1])[:3]:
    print(f"{', '.join(combo):<18} {corr:>11.3f} {sharpe:>8.2f} {cum:>+9.1f}%")


# === (d) PC2 / PC3 INSPECTION ===
print()
print("=" * 72)
print("(d) PC2 / PC3 sub-structure within Mag 7")
print("=" * 72)

cohort_1y = rets_1y[COHORT].dropna()
pca = PCA(n_components=5)
pca.fit(cohort_1y.values)

print(f"\nExplained variance:")
for i in range(5):
    v = pca.explained_variance_ratio_[i]
    cum = pca.explained_variance_ratio_[:i+1].sum()
    print(f"  PC{i+1}: {v:.2%}  (cumulative: {cum:.2%})")

for pc_idx, pc_name in enumerate(["PC2", "PC3"]):
    print(f"\n{pc_name} loadings:")
    pc = pca.components_[pc_idx + 1]
    for t, w in sorted(zip(COHORT, pc), key=lambda x: -x[1]):
        print(f"  {t}: {w:+.4f}")


# === (e) FACTOR DECOMPOSITION ===
print()
print("=" * 72)
print("(e) Factor decomposition — basket vs broad-market benchmarks")
print("=" * 72)

rets_full = rets_1y.dropna()
basket = rets_full[COHORT].mean(axis=1)
X = rets_full[["SPY", "QQQ", "SMH", "XLK"]].values
y = basket.values

reg = LinearRegression()
reg.fit(X, y)
y_pred = reg.predict(X)
r2 = reg.score(X, y)
print(f"\nR-squared (var explained by SPY + QQQ + SMH + XLK): {r2:.1%}")
print(f"Residual variance (Mag 7-specific factor): {1 - r2:.1%}")
print(f"\nBetas:")
for f, b in zip(["SPY", "QQQ", "SMH", "XLK"], reg.coef_):
    print(f"  {f}: {b:+.3f}")
print(f"Intercept (annualized alpha): {reg.intercept_ * 252 * 100:+.1f}%")

# Per-name R² to QQQ alone (the canonical Mag 7 benchmark)
print(f"\nPer-name R² to QQQ alone:")
for t in COHORT:
    y_t = rets_full[t].values
    X_qqq = rets_full[["QQQ"]].values
    reg_t = LinearRegression()
    reg_t.fit(X_qqq, y_t)
    r2_t = reg_t.score(X_qqq, y_t)
    print(f"  {t}: R² = {r2_t:.1%}")
