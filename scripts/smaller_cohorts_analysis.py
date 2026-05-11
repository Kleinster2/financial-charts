"""Apply stability + PC2/PC3 + factor decomposition + subset analysis to the
smaller validated cohorts that haven't yet had the full framework treatment:

- WFE (N=4): ASML, AMAT, KLAC, LRCX
- AI Compute (N=3): TSM, NVDA, AMD
- US Memory (N=3): MU, SNDK, WDC
- Korea Memory (N=2): Samsung (005930.KS), SK Hynix (000660.KS)

At N=2-4 some diagnostics are limited (PC2 less informative, subset enumeration
small). Run what's meaningful at each cohort size.
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
END = date(2026, 5, 8)

COHORTS = {
    "WFE": {
        "tickers": ["ASML", "AMAT", "KLAC", "LRCX"],
        "benchmarks": ["SOXX", "SMH", "SPY"],
    },
    "AI Compute": {
        "tickers": ["TSM", "NVDA", "AMD"],
        "benchmarks": ["SOXX", "SMH", "SPY", "QQQ"],
    },
    "US Memory": {
        "tickers": ["MU", "SNDK", "WDC"],
        "benchmarks": ["SOXX", "SMH", "SPY"],
    },
    "Korea Memory": {
        "tickers": ["005930.KS", "000660.KS"],
        "benchmarks": ["EWY", "SOXX", "SMH", "SPY"],
    },
}


def load(tickers, start, end):
    placeholders = ", ".join("?" for _ in tickers)
    sql = f"SELECT Date, Ticker, Close FROM prices_long WHERE Ticker IN ({placeholders}) AND Date BETWEEN ? AND ? ORDER BY Date"
    with sqlite3.connect(DB) as conn:
        df = pd.read_sql(sql, conn, params=tickers + [start, end])
    df["Date"] = pd.to_datetime(df["Date"])
    df = df.pivot(index="Date", columns="Ticker", values="Close")
    df = df.apply(pd.to_numeric, errors="coerce")
    return df.replace({0: np.nan})


WINDOWS = {
    "YTD 2026": date(2026, 1, 2),
    "1Y": END - timedelta(days=365),
    "2Y": END - timedelta(days=730),
    "3Y": END - timedelta(days=1095),
}


def stats_for_cohort(name, cohort_def):
    print("\n" + "=" * 72)
    print(f"{name} cohort (N={len(cohort_def['tickers'])})")
    print("=" * 72)

    tickers = cohort_def["tickers"]
    benchmarks = cohort_def["benchmarks"]
    start_3y = (END - timedelta(days=1095)).isoformat()
    prices = load(tickers + benchmarks, start_3y, (END + timedelta(days=1)).isoformat())
    rets = np.log(prices / prices.shift(1)).dropna()

    print(f"\n--- Stability across windows ---")
    print(f"{'Window':<10} {'obs':>5} {'intra':>7} {'PC1':>7} {'vs SPY':>9} {'gap':>7}")
    for label, cutoff in WINDOWS.items():
        sub = rets.loc[rets.index >= pd.Timestamp(cutoff)]
        cohort_sub = sub[tickers].dropna()
        if len(cohort_sub) < 30:
            print(f"{label:<10} insufficient")
            continue
        if len(tickers) >= 2:
            corr = cohort_sub.corr()
            mask = np.triu(np.ones_like(corr, dtype=bool), k=1)
            pair_corrs = corr.where(mask).stack()
            intra = float(pair_corrs.mean())
        else:
            intra = 1.0
        if len(tickers) >= 2:
            pca = PCA(n_components=min(3, len(tickers)))
            pca.fit(cohort_sub.values)
            pc1 = pca.explained_variance_ratio_[0]
        else:
            pc1 = 1.0
        if "SPY" in sub.columns:
            spy_rets = sub["SPY"].reindex(cohort_sub.index).fillna(0)
            cohort_avg = cohort_sub.mean(axis=1)
            vs_spy = cohort_avg.corr(spy_rets)
            gap = intra - vs_spy
            print(f"{label:<10} {len(cohort_sub):>5} {intra:>7.3f} {pc1:>7.1%} {vs_spy:>9.3f} {gap:>+7.3f}")

    cutoff_1y = pd.Timestamp(END - timedelta(days=365))
    rets_1y = rets.loc[rets.index >= cutoff_1y]
    cohort_1y = rets_1y[tickers].dropna()

    if len(tickers) >= 3:
        print(f"\n--- PC2 / PC3 loadings (1Y) ---")
        pca = PCA(n_components=min(5, len(tickers)))
        pca.fit(cohort_1y.values)
        for i in range(min(3, len(tickers))):
            v = pca.explained_variance_ratio_[i]
            cum = pca.explained_variance_ratio_[:i+1].sum()
            print(f"PC{i+1}: {v:.2%}  (cum: {cum:.2%})")
        for pc_idx in [0, 1, 2]:
            if pc_idx >= len(pca.components_):
                break
            print(f"\nPC{pc_idx+1} loadings:")
            pc = pca.components_[pc_idx]
            if pc.mean() < 0 and pc_idx == 0:
                pc = -pc
            for t, w in sorted(zip(tickers, pc), key=lambda x: -x[1]):
                print(f"  {t}: {w:+.4f}")

    print(f"\n--- Factor decomposition vs benchmarks (1Y) ---")
    rets_full = rets_1y.dropna()
    if len(rets_full) >= 30 and len(tickers) >= 2:
        basket = rets_full[tickers].mean(axis=1)
        for factor_set in [
            [benchmarks[0]],
            benchmarks[:2],
            benchmarks,
        ]:
            valid_factors = [f for f in factor_set if f in rets_full.columns]
            if len(valid_factors) < len(factor_set):
                continue
            X = rets_full[valid_factors].values
            y = basket.values
            reg = LinearRegression()
            reg.fit(X, y)
            r2 = reg.score(X, y)
            beta_strs = [f"{f}={b:+.2f}" for f, b in zip(valid_factors, reg.coef_)]
            print(f"  vs {'+'.join(valid_factors)}: R² = {r2:.1%}, betas: {', '.join(beta_strs)}, residual = {1-r2:.1%}")

    if len(tickers) >= 3:
        print(f"\n--- Subset optimization ---")
        full_basket = rets_1y[tickers].mean(axis=1)
        pair_results = []
        for combo in combinations(tickers, 2):
            pair_rets = rets_1y[list(combo)]
            corr = pair_rets.iloc[:, 0].corr(pair_rets.iloc[:, 1])
            basket_pair = pair_rets.mean(axis=1)
            tracking_corr = basket_pair.corr(full_basket)
            sharpe = (basket_pair.mean() * 252) / (basket_pair.std() * np.sqrt(252))
            cum = (np.exp(basket_pair.sum()) - 1) * 100
            pair_results.append((combo, corr, tracking_corr, sharpe, cum))

        print(f"{'Pair':<14} {'Intra':>7} {'Track':>7} {'Sharpe':>8} {'Cum %':>10}")
        for combo, corr, track, sharpe, cum in sorted(pair_results, key=lambda x: -x[2]):
            print(f"{', '.join(combo):<14} {corr:>7.3f} {track:>7.3f} {sharpe:>8.2f} {cum:>+9.1f}%")

        print(f"\nPer-name 1Y cumulative return:")
        for t in tickers:
            r_t = rets_1y[t]
            cum_t = (np.exp(r_t.sum()) - 1) * 100
            print(f"  {t:<10} {cum_t:>+9.1f}%")


for name, cd in COHORTS.items():
    stats_for_cohort(name, cd)
