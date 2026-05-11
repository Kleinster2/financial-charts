"""Three more analyses on the Space pure-plays cohort:

(b) Pre/post Nov 2025 regime cluster comparison — quantify the structural shift
    that the rolling PC1 chart hinted at.

(j) Best Sharpe 2-name pair search — what's the optimal pair regardless of
    factor-tracking constraint?

(a) Event-study decomposition — for each major catalyst day, decompose cohort
    moves into factor + idiosyncratic.
"""
from __future__ import annotations
import sqlite3
from datetime import date, timedelta
from itertools import combinations
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.decomposition import PCA

DB = Path(__file__).resolve().parent.parent / "market_data.db"
COHORT = ["RKLB", "RDW", "LUNR", "BKSY", "ASTS", "SPIR", "PL"]
END = date(2026, 5, 8)


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


# === (b) PRE/POST NOV 2025 REGIME COMPARISON ===
print("=" * 72)
print("(b) Pre/post Nov 2025 regime cluster comparison")
print("=" * 72)

# Pre-regime: 1Y ending 2025-10-31
# Post-regime: from 2025-12-01 through 2026-05-08
prices = load(COHORT, "2024-01-01", (END + timedelta(days=1)).isoformat())
rets = np.log(prices / prices.shift(1)).dropna()

pre_window = rets.loc[(rets.index >= pd.Timestamp("2024-11-01")) & (rets.index <= pd.Timestamp("2025-10-31"))]
post_window = rets.loc[rets.index >= pd.Timestamp("2025-12-01")]


def cluster_metrics(window_rets: pd.DataFrame, label: str) -> None:
    sub = window_rets[COHORT].dropna()
    corr = sub.corr()
    mask = np.triu(np.ones_like(corr, dtype=bool), k=1)
    pair_corrs = corr.where(mask).stack()
    intra = float(pair_corrs.mean())
    intra_min = float(pair_corrs.min())
    intra_max = float(pair_corrs.max())
    pca = PCA(n_components=3)
    pca.fit(sub.values)
    print(f"\n{label} ({len(sub)} obs, {sub.index.min().date()} to {sub.index.max().date()}):")
    print(f"  Intra-cluster avg correlation: {intra:.3f}  range [{intra_min:.2f}, {intra_max:.2f}]")
    print(f"  PC1 explained variance: {pca.explained_variance_ratio_[0]:.1%}")
    print(f"  PC2 explained variance: {pca.explained_variance_ratio_[1]:.1%}")
    print(f"  Cohort cumulative log return: {window_rets[COHORT].mean(axis=1).sum():+.2%}")
    return intra, pca.explained_variance_ratio_[0]


pre_intra, pre_pc1 = cluster_metrics(pre_window, "PRE-regime (Nov 2024 - Oct 2025)")
post_intra, post_pc1 = cluster_metrics(post_window, "POST-regime (Dec 2025 - May 2026)")
print(f"\nIntra-correlation change: {pre_intra:.3f} -> {post_intra:.3f}  ({post_intra-pre_intra:+.3f})")
print(f"PC1 variance change: {pre_pc1:.1%} -> {post_pc1:.1%}  ({(post_pc1-pre_pc1)*100:+.1f}pp)")


# === (j) BEST SHARPE PAIR ===
print()
print("=" * 72)
print("(j) Best Sharpe 2-name pair (1Y) regardless of factor-tracking constraint")
print("=" * 72)

cutoff_1y = pd.Timestamp(END - timedelta(days=365))
rets_1y = rets.loc[rets.index >= cutoff_1y]

results = []
for combo in combinations(COHORT, 2):
    pair_rets = rets_1y[list(combo)].mean(axis=1)
    pair_sharpe = (pair_rets.mean() * 252) / (pair_rets.std() * np.sqrt(252))
    pair_cum = (np.exp(pair_rets.sum()) - 1) * 100
    pair_vol = pair_rets.std() * np.sqrt(252) * 100
    basket = rets_1y[COHORT].mean(axis=1)
    corr = pair_rets.corr(basket)
    results.append((combo, pair_sharpe, pair_cum, pair_vol, corr))

print(f"\nAll 21 pairs ranked by Sharpe:")
print(f"{'Pair':<20} {'Sharpe':>8} {'Cum %':>10} {'Vol %':>8} {'Corr to basket':>16}")
for combo, sharpe, cum, vol, corr in sorted(results, key=lambda x: -x[1]):
    print(f"{', '.join(combo):<20} {sharpe:>8.2f} {cum:>+9.1f}% {vol:>7.1f}% {corr:>15.3f}")


# === (a) EVENT STUDY ===
print()
print("=" * 72)
print("(a) Event-study factor decomposition for key catalyst days")
print("=" * 72)

# Fit PCA on 1Y window for stable loadings
cohort_rets_1y = rets_1y[COHORT].dropna()
pca = PCA(n_components=3)
pca.fit(cohort_rets_1y.values)
pc1_load = pca.components_[0]
if pc1_load.mean() < 0:
    pc1_load = -pc1_load

# Key catalyst dates (closest available trading day if exact date missing)
events = {
    "2026-05-08": "RKLB Q1 record + Motiv + Golden Dome SBI selection (basket rally)",
    "2026-05-07": "Cohort drawdown day before RKLB earnings rally",
    "2026-04-10": "Anthropic Managed Agents selloff (SaaS shock day)",
    "2026-03-25": "SpaceX IPO filing reportedly imminent (The Information)",
    "2026-02-27": "Iran war / Operation Epic Fury kicks off",
    "2025-12-11": "Musk confirms 2026 SpaceX IPO 'accurate' (CNBC)",
    "2025-11-29": "USSF awards first Golden Dome SBI prototype contracts",
    "2025-11-17": "Cohort drawdown trough (per earlier analysis)",
}

print(f"\n{'Date':<12} {'Basket %':>10} {'PC1 score':>10}  Description")
print("-" * 100)
for date_str, desc in events.items():
    try:
        day_rets = rets.loc[pd.Timestamp(date_str)]
    except KeyError:
        # Fallback: try the closest preceding trading day
        idx = rets.index[rets.index >= pd.Timestamp(date_str)]
        if len(idx) == 0:
            continue
        day_rets = rets.loc[idx[0]]
        date_str_actual = idx[0].strftime("%Y-%m-%d")
    else:
        date_str_actual = date_str
    basket_pct = (np.exp(day_rets[COHORT].mean()) - 1) * 100
    pc1_score = float(day_rets[COHORT].values @ pc1_load)
    print(f"{date_str_actual:<12} {basket_pct:>+9.2f}% {pc1_score:>10.4f}  {desc[:75]}")

# Detailed factor decomposition for the largest single-day moves
print(f"\n\nFactor decomposition for the three largest +PC1 cohort days in 1Y:")
basket_log = rets_1y[COHORT].mean(axis=1)
top_days = basket_log.nlargest(5).index
for d in top_days:
    day_r = rets.loc[d]
    basket_pct = (np.exp(day_r[COHORT].mean()) - 1) * 100
    print(f"\n{d.strftime('%Y-%m-%d')}: basket {basket_pct:+.2f}%")
    print(f"  {'Ticker':<8} {'Actual %':>10} {'Factor %':>10} {'Idio %':>10}")
    pc1_score = float(day_r[COHORT].values @ pc1_load)
    for i, t in enumerate(COHORT):
        actual_log = float(day_r[t])
        actual_pct = (np.exp(actual_log) - 1) * 100
        factor_log = pc1_load[i] * pc1_score
        factor_pct = (np.exp(factor_log) - 1) * 100
        idio_pct = actual_pct - factor_pct
        print(f"  {t:<8} {actual_pct:>+9.2f}% {factor_pct:>+9.2f}% {idio_pct:>+9.2f}%")
