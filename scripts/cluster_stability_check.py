"""Quick stability check for the Space pure-plays cluster across 1Y, 2Y, 3Y, YTD windows."""
from __future__ import annotations
import sqlite3
from datetime import date, timedelta
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.decomposition import PCA

DB = Path(__file__).resolve().parent.parent / "market_data.db"
COHORT = ["RKLB", "RDW", "LUNR", "BKSY", "ASTS", "SPIR", "PL"]
DEFENSE = ["LMT", "RTX", "NOC", "LHX"]
END = date(2026, 5, 7)

WINDOWS = {
    "YTD 2026": (date(2026, 1, 2).isoformat(), END.isoformat()),
    "1Y": ((END - timedelta(days=365)).isoformat(), END.isoformat()),
    "2Y": ((END - timedelta(days=730)).isoformat(), END.isoformat()),
    "3Y": ((END - timedelta(days=1095)).isoformat(), END.isoformat()),
}


def load_returns(tickers: list[str], start: str, end: str) -> pd.DataFrame:
    cols = ", ".join(f'"{t}"' for t in tickers)
    sql = f"SELECT Date, {cols} FROM stock_prices_daily WHERE Date BETWEEN ? AND ? ORDER BY Date"
    with sqlite3.connect(DB) as conn:
        df = pd.read_sql(sql, conn, params=[start, end])
    df["Date"] = pd.to_datetime(df["Date"])
    df = df.set_index("Date")
    df = df.replace({0: np.nan})
    rets = np.log(df / df.shift(1)).dropna(how="all")
    return rets


def diagnostic(rets: pd.DataFrame, tickers: list[str]) -> dict:
    sub = rets[tickers].dropna()
    corr = sub.corr()
    mask = np.triu(np.ones_like(corr, dtype=bool), k=1)
    pair_corrs = corr.where(mask).stack()
    intra = float(pair_corrs.mean())
    intra_min = float(pair_corrs.min())
    intra_max = float(pair_corrs.max())
    pca = PCA(n_components=min(5, len(tickers)))
    pca.fit(sub.values)
    pc1 = float(pca.explained_variance_ratio_[0])
    pc2 = float(pca.explained_variance_ratio_[1]) if len(pca.explained_variance_ratio_) > 1 else 0.0
    return {
        "obs": len(sub),
        "intra_avg": intra,
        "intra_min": intra_min,
        "intra_max": intra_max,
        "pc1": pc1,
        "pc2": pc2,
    }


def cross_corr(rets: pd.DataFrame, group_a: list[str], group_b: list[str]) -> float:
    rets_clean = rets[group_a + group_b].dropna()
    if len(rets_clean) < 30:
        return float("nan")
    corr = rets_clean.corr()
    pairs = [corr.loc[a, b] for a in group_a for b in group_b]
    return float(np.mean(pairs))


print(f"{'Window':<12} {'obs':>5} {'intra':>7} {'range':>14} {'PC1':>7} {'PC2':>7} {'vs def':>8} {'gap':>7}")
print("-" * 80)
for name, (start, end) in WINDOWS.items():
    rets = load_returns(COHORT + DEFENSE, start, end)
    if len(rets) < 30:
        print(f"{name:<12} {len(rets):>5}  -- insufficient data --")
        continue
    d = diagnostic(rets, COHORT)
    vs_def = cross_corr(rets, COHORT, DEFENSE)
    gap = d["intra_avg"] - vs_def
    print(
        f"{name:<12} {d['obs']:>5} "
        f"{d['intra_avg']:>7.3f} [{d['intra_min']:.2f},{d['intra_max']:.2f}] "
        f"{d['pc1']:>7.1%} {d['pc2']:>7.1%} "
        f"{vs_def:>8.3f} {gap:>+7.3f}"
    )
