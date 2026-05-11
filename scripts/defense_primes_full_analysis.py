"""Apply the Space pure-plays-style framework to the Defense primes cohort.

Two cohort variants tested:
- 7-name: LMT, RTX, NOC, GD, HII, LHX, LDOS (existing note, partial validation)
- 6-name core: same without LDOS (test if removing IT-services singleton tightens)
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
COHORT_7 = ["LMT", "RTX", "NOC", "GD", "HII", "LHX", "LDOS"]
COHORT_6 = ["LMT", "RTX", "NOC", "GD", "HII", "LHX"]
BENCHMARKS = ["SPY", "ITA", "XLI", "XAR"]
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


# === STABILITY ACROSS WINDOWS ===
print("=" * 72)
print("Stability across windows — 6-name core cohort")
print("=" * 72)

start_3y = (END - timedelta(days=1095)).isoformat()
prices = load(COHORT_7 + ["BA"] + BENCHMARKS, start_3y, (END + timedelta(days=1)).isoformat())
rets = np.log(prices / prices.shift(1)).dropna()

WINDOWS = {
    "YTD 2026": date(2026, 1, 2),
    "1Y": END - timedelta(days=365),
    "2Y": END - timedelta(days=730),
    "3Y": END - timedelta(days=1095),
}

print(f"\n{'Window':<10} {'obs':>5} {'intra':>7} {'range':>14} {'PC1':>7} {'PC2':>7} {'vs BA':>8} {'gap':>7}")
print("-" * 75)
for name, cutoff in WINDOWS.items():
    sub = rets.loc[rets.index >= pd.Timestamp(cutoff)]
    cohort_sub = sub[COHORT_6].dropna()
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
    if "BA" in sub.columns:
        ba_rets = sub["BA"].reindex(cohort_sub.index).fillna(0)
        cohort_avg = cohort_sub.mean(axis=1)
        vs_ba = cohort_avg.corr(ba_rets)
        gap = intra - vs_ba
        print(f"{name:<10} {len(cohort_sub):>5} {intra:>7.3f} [{pmin:.2f},{pmax:.2f}] {pc1:>7.1%} {pc2:>7.1%} {vs_ba:>8.3f} {gap:>+7.3f}")


# === PC2 / PC3 INSPECTION ===
print()
print("=" * 72)
print("PC2 / PC3 sub-structure (6-name core)")
print("=" * 72)

cutoff_1y = pd.Timestamp(END - timedelta(days=365))
rets_1y = rets.loc[rets.index >= cutoff_1y]
cohort_1y = rets_1y[COHORT_6].dropna()
pca = PCA(n_components=5)
pca.fit(cohort_1y.values)

print(f"\nExplained variance:")
for i in range(5):
    v = pca.explained_variance_ratio_[i]
    cum = pca.explained_variance_ratio_[:i+1].sum()
    print(f"  PC{i+1}: {v:.2%}  (cumulative: {cum:.2%})")

for pc_idx, pc_name in enumerate(["PC1", "PC2", "PC3"]):
    print(f"\n{pc_name} loadings:")
    pc = pca.components_[pc_idx]
    if pc.mean() < 0 and pc_idx == 0:
        pc = -pc
    for t, w in sorted(zip(COHORT_6, pc), key=lambda x: -x[1]):
        print(f"  {t}: {w:+.4f}")


# === SUBSET OPTIMIZATION ===
print()
print("=" * 72)
print("Subset optimization (6-name core)")
print("=" * 72)

full_basket = rets_1y[COHORT_6].mean(axis=1)
pair_results = []
for combo in combinations(COHORT_6, 2):
    pair_rets = rets_1y[list(combo)]
    corr = pair_rets.iloc[:, 0].corr(pair_rets.iloc[:, 1])
    basket_pair = pair_rets.mean(axis=1)
    tracking_corr = basket_pair.corr(full_basket)
    sharpe = (basket_pair.mean() * 252) / (basket_pair.std() * np.sqrt(252))
    cum_pct = (np.exp(basket_pair.sum()) - 1) * 100
    pair_results.append((combo, corr, tracking_corr, sharpe, cum_pct))

print(f"\nTop 5 pairs by tracking correlation to basket:")
print(f"{'Pair':<14} {'Intra':>7} {'Track':>7} {'Sharpe':>8} {'Cum %':>10}")
for combo, corr, track, sharpe, cum in sorted(pair_results, key=lambda x: -x[2])[:5]:
    print(f"{', '.join(combo):<14} {corr:>7.3f} {track:>7.3f} {sharpe:>8.2f} {cum:>+9.1f}%")

print(f"\nTop 5 pairs by Sharpe:")
for combo, corr, track, sharpe, cum in sorted(pair_results, key=lambda x: -x[3])[:5]:
    print(f"{', '.join(combo):<14} {corr:>7.3f} {track:>7.3f} {sharpe:>8.2f} {cum:>+9.1f}%")


# === FACTOR DECOMPOSITION ===
print()
print("=" * 72)
print("Factor decomposition (6-name core vs benchmarks)")
print("=" * 72)

rets_full = rets_1y.dropna()
basket = rets_full[COHORT_6].mean(axis=1)

for factor_set, label in [
    (["SPY"], "SPY only"),
    (["ITA"], "ITA only (aero+def ETF)"),
    (["ITA", "SPY"], "ITA + SPY"),
    (["ITA", "XAR"], "ITA + XAR (defense ETF pair)"),
    (["SPY", "ITA", "XLI"], "SPY + ITA + XLI (industrials)"),
]:
    if not all(f in rets_full.columns for f in factor_set):
        print(f"  {label}: missing factor — skip")
        continue
    X = rets_full[factor_set].values
    y = basket.values
    reg = LinearRegression()
    reg.fit(X, y)
    r2 = reg.score(X, y)
    beta_strs = [f"{f}={b:+.2f}" for f, b in zip(factor_set, reg.coef_)]
    print(f"  {label}: R² = {r2:.1%}, betas: {', '.join(beta_strs)}")


# === COMPLEMENT TEST + PER-NAME RETURNS ===
print()
print("=" * 72)
print("Complement test + per-name 1Y returns")
print("=" * 72)

# Top tracking pair
top_pair = sorted(pair_results, key=lambda x: -x[2])[0][0]
print(f"\nTop tracking pair: {top_pair}")
complement = [t for t in COHORT_6 if t not in top_pair]
top_rets = rets_1y[list(top_pair)].mean(axis=1)
comp_rets = rets_1y[complement].mean(axis=1)

def stats(r):
    return {
        "cum": (np.exp(r.sum()) - 1) * 100,
        "vol": r.std() * np.sqrt(252) * 100,
        "sharpe": (r.mean() * 252) / (r.std() * np.sqrt(252)),
    }

ts = stats(top_rets)
fs = stats(full_basket)
cs = stats(comp_rets)
print(f"\n  {'Metric':<20} {'Top 2':>12} {'Full 6':>10} {'Complement 4':>14}")
print("-" * 60)
print(f"  {'Cum return %':<20} {ts['cum']:>+11.1f}% {fs['cum']:>+9.1f}% {cs['cum']:>+13.1f}%")
print(f"  {'Annualized vol':<20} {ts['vol']:>11.1f}% {fs['vol']:>9.1f}% {cs['vol']:>13.1f}%")
print(f"  {'Sharpe':<20} {ts['sharpe']:>12.2f} {fs['sharpe']:>10.2f} {cs['sharpe']:>14.2f}")

print(f"\nPer-name 1Y cumulative return:")
for t in COHORT_6:
    r_t = rets_1y[t]
    cum_t = (np.exp(r_t.sum()) - 1) * 100
    in_top = "(in top pair)" if t in top_pair else ""
    print(f"  {t:<6} {cum_t:>+9.1f}%  {in_top}")
print(f"  LDOS (excluded from 6-core)  {(np.exp(rets_1y['LDOS'].sum()) - 1) * 100:>+9.1f}%")
