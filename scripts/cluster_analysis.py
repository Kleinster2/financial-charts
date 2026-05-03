"""Cluster analysis for boutique advisory cohort.

Tests whether PWP, LAZ, EVR, MC, HLI, PJT constitute a statistical cluster
distinct from bulge brackets, mid-IBs, asset managers, insurance brokers, and
broad financials ETFs.

Three diagnostics:
  1. Pairwise daily-return correlation matrix
  2. Hierarchical clustering with 1-correlation distance
  3. PCA loadings on the candidate cohort

Outputs:
  investing/attachments/boutique-cluster-correlation-1y.png
  investing/attachments/boutique-cluster-correlation-2y.png
  investing/attachments/boutique-cluster-dendrogram-1y.png
  investing/attachments/boutique-cluster-pca-1y.png
  investing/attachments/boutique-cluster-results.txt  (text summary)
"""

from __future__ import annotations

import sqlite3
from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.cluster.hierarchy import dendrogram, fcluster, linkage
from scipy.spatial.distance import squareform
from sklearn.decomposition import PCA

ROOT = Path(__file__).resolve().parent.parent
DB = ROOT / "market_data.db"
ATT = ROOT / "investing" / "attachments"
ATT.mkdir(parents=True, exist_ok=True)

UNIVERSE = {
    "cluster": ["PWP", "LAZ", "EVR", "MC", "HLI", "PJT"],
    "bulge": ["GS", "MS", "JPM"],
    "mid_ib": ["SF", "RJF"],
    "alt_mgr": ["BX", "KKR"],
    "trad_mgr": ["TROW", "BEN"],
    "ins_brk": ["AON", "AJG", "BRO"],
    "etf": ["XLF", "KBE", "IWM", "SPY"],
}

GROUP_COLORS = {
    "cluster": "#2962FF",
    "bulge": "#000000",
    "mid_ib": "#7E57C2",
    "alt_mgr": "#FF6F00",
    "trad_mgr": "#FFA726",
    "ins_brk": "#26A69A",
    "etf": "#9E9E9E",
}


def load_returns(window_start: str, window_end: str = "2026-04-30") -> pd.DataFrame:
    """Return daily-return DataFrame for all tickers, columns=ticker."""
    tickers = [t for tks in UNIVERSE.values() for t in tks]
    placeholders = ",".join("?" for _ in tickers)
    sql = (
        "SELECT Date, Ticker, Close FROM prices_long "
        f"WHERE Ticker IN ({placeholders}) "
        "AND Date >= ? AND Date <= ? "
        "ORDER BY Date"
    )
    with sqlite3.connect(DB) as conn:
        df = pd.read_sql(sql, conn, params=tickers + [window_start, window_end])
    df["Date"] = pd.to_datetime(df["Date"])
    px = df.pivot(index="Date", columns="Ticker", values="Close").sort_index()
    rets = np.log(px / px.shift(1)).dropna(how="all")
    rets = rets[[t for t in tickers if t in rets.columns]]
    return rets


def ticker_group(ticker: str) -> str:
    for grp, tks in UNIVERSE.items():
        if ticker in tks:
            return grp
    return "other"


def color_for(ticker: str) -> str:
    return GROUP_COLORS.get(ticker_group(ticker), "#000000")


def correlation_matrix(rets: pd.DataFrame) -> pd.DataFrame:
    """Pairwise pearson correlation of daily log returns."""
    return rets.corr(method="pearson")


def plot_correlation_heatmap(
    corr: pd.DataFrame, out: Path, title: str, cluster_first: bool = True
) -> None:
    if cluster_first:
        order = []
        for grp in ["cluster", "mid_ib", "bulge", "alt_mgr", "trad_mgr", "ins_brk", "etf"]:
            for t in UNIVERSE[grp]:
                if t in corr.columns:
                    order.append(t)
        corr = corr.loc[order, order]

    fig, ax = plt.subplots(figsize=(11, 9))
    im = ax.imshow(corr.values, cmap="RdBu_r", vmin=-1, vmax=1, aspect="auto")
    ax.set_xticks(range(len(corr.columns)))
    ax.set_yticks(range(len(corr.index)))
    ax.set_xticklabels(corr.columns, rotation=90, fontsize=9)
    ax.set_yticklabels(corr.index, fontsize=9)

    for i, t in enumerate(corr.index):
        c = color_for(t)
        ax.get_yticklabels()[i].set_color(c)
        ax.get_xticklabels()[i].set_color(c)

    for i in range(corr.shape[0]):
        for j in range(corr.shape[1]):
            v = corr.values[i, j]
            ax.text(
                j, i, f"{v:.2f}", ha="center", va="center",
                fontsize=7, color="white" if abs(v) > 0.55 else "black",
            )
    ax.set_title(title, fontsize=11, pad=12)
    cbar = fig.colorbar(im, ax=ax, fraction=0.04, pad=0.02)
    cbar.set_label("Pearson r (daily log returns)")
    fig.tight_layout()
    fig.savefig(out, dpi=140, bbox_inches="tight")
    plt.close(fig)


def hierarchical_cluster(corr: pd.DataFrame, out: Path, title: str) -> dict:
    """Hierarchical clustering with 1-correlation distance, ward linkage."""
    dist = 1 - corr.abs()
    np.fill_diagonal(dist.values, 0)
    condensed = squareform(dist.values, checks=False)
    Z = linkage(condensed, method="average")

    fig, ax = plt.subplots(figsize=(12, 6))
    label_colors = [color_for(t) for t in corr.columns]
    dn = dendrogram(
        Z, labels=list(corr.columns), color_threshold=0.4,
        above_threshold_color="#999999", ax=ax,
    )
    ax.set_title(title, fontsize=11, pad=10)
    ax.set_ylabel("Distance (1 - |corr|)")
    for tick, lbl in zip(ax.get_xticklabels(), dn["ivl"]):
        tick.set_color(color_for(lbl))
    ax.axhline(0.4, color="gray", linestyle="--", linewidth=0.8, alpha=0.5)
    ax.text(0.99, 0.4, " threshold = 0.4", transform=ax.get_yaxis_transform(),
            ha="right", va="bottom", fontsize=8, color="gray")
    fig.tight_layout()
    fig.savefig(out, dpi=140, bbox_inches="tight")
    plt.close(fig)

    flat = fcluster(Z, t=0.4, criterion="distance")
    clusters: dict[int, list[str]] = {}
    for ticker, c in zip(corr.columns, flat):
        clusters.setdefault(int(c), []).append(ticker)
    return clusters


def pca_analysis(rets: pd.DataFrame, candidate: list[str], out: Path, title: str) -> dict:
    """Run PCA on the candidate cluster only; report PC1 explained variance and loadings."""
    sub = rets[candidate].dropna()
    standardized = (sub - sub.mean()) / sub.std()
    pca = PCA(n_components=min(5, len(candidate)))
    pca.fit(standardized)
    explained = pca.explained_variance_ratio_
    loadings = pd.DataFrame(
        pca.components_.T,
        index=candidate,
        columns=[f"PC{i+1}" for i in range(pca.n_components_)],
    )

    fig, axes = plt.subplots(1, 2, figsize=(13, 5))
    axes[0].bar(range(1, len(explained) + 1), explained * 100,
                color=["#2962FF"] + ["#999999"] * (len(explained) - 1))
    axes[0].set_xticks(range(1, len(explained) + 1))
    axes[0].set_xticklabels([f"PC{i+1}" for i in range(len(explained))])
    axes[0].set_ylabel("Explained variance (%)")
    axes[0].set_title(f"Scree — PC1 = {explained[0]*100:.1f}%")
    for i, v in enumerate(explained):
        axes[0].text(i + 1, v * 100 + 0.5, f"{v*100:.1f}%", ha="center", fontsize=9)

    pc1 = loadings["PC1"].sort_values(ascending=True)
    axes[1].barh(pc1.index, pc1.values, color="#2962FF")
    axes[1].axvline(0, color="black", linewidth=0.6)
    axes[1].set_xlabel("PC1 loading")
    axes[1].set_title("PC1 loadings — cluster cohesion factor")

    fig.suptitle(title, fontsize=11)
    fig.tight_layout()
    fig.savefig(out, dpi=140, bbox_inches="tight")
    plt.close(fig)

    return {"explained_variance_ratio": explained.tolist(), "loadings": loadings}


def avg_intra_vs_inter(corr: pd.DataFrame) -> dict:
    """For each pair of groups, compute average pairwise correlation."""
    groups = sorted({ticker_group(t) for t in corr.columns} - {"other"})
    out = {}
    for g1 in groups:
        for g2 in groups:
            ts1 = [t for t in UNIVERSE.get(g1, []) if t in corr.columns]
            ts2 = [t for t in UNIVERSE.get(g2, []) if t in corr.columns]
            vals = []
            for a in ts1:
                for b in ts2:
                    if a != b:
                        vals.append(corr.loc[a, b])
            if vals:
                out[(g1, g2)] = float(np.mean(vals))
    return out


def write_summary(
    rets_1y: pd.DataFrame,
    rets_2y: pd.DataFrame,
    corr_1y: pd.DataFrame,
    corr_2y: pd.DataFrame,
    clusters_1y: dict,
    pca_result: dict,
    intra_inter_1y: dict,
    out: Path,
) -> None:
    lines = []
    lines.append("BOUTIQUE ADVISORY CLUSTER ANALYSIS")
    lines.append(f"Window 1y: {rets_1y.index.min().date()} -> {rets_1y.index.max().date()} ({len(rets_1y)} obs)")
    lines.append(f"Window 2y: {rets_2y.index.min().date()} -> {rets_2y.index.max().date()} ({len(rets_2y)} obs)")
    lines.append(f"Universe: {len(rets_1y.columns)} tickers")
    lines.append("")

    lines.append("--- 1Y INTRA-CLUSTER PAIRWISE CORRELATIONS ---")
    cluster = [t for t in UNIVERSE["cluster"] if t in corr_1y.columns]
    sub = corr_1y.loc[cluster, cluster]
    lines.append(sub.round(2).to_string())
    upper = sub.values[np.triu_indices_from(sub, k=1)]
    lines.append(f"Average intra-cluster correlation: {upper.mean():.3f}")
    lines.append(f"Range: [{upper.min():.3f}, {upper.max():.3f}]")
    lines.append("")

    lines.append("--- AVG GROUP-PAIR CORRELATIONS (1Y) ---")
    groups = sorted({ticker_group(t) for t in corr_1y.columns} - {"other"})
    header = "             " + "  ".join(f"{g[:7]:>7}" for g in groups)
    lines.append(header)
    for g1 in groups:
        row = f"{g1[:11]:>11}  " + "  ".join(
            f"{intra_inter_1y.get((g1, g2), float('nan')):>7.3f}" for g2 in groups
        )
        lines.append(row)
    lines.append("")
    lines.append("Cluster vs others (intra=cluster-cluster avg shown for context):")
    cc = intra_inter_1y.get(("cluster", "cluster"), float("nan"))
    for g in groups:
        if g == "cluster":
            continue
        v = intra_inter_1y.get(("cluster", g), float("nan"))
        delta = cc - v
        lines.append(f"  cluster vs {g:<10}: {v:.3f}  (intra advantage: +{delta:.3f})")
    lines.append("")

    lines.append("--- HIERARCHICAL CLUSTERS (1Y, distance threshold 0.4) ---")
    for cid, members in sorted(clusters_1y.items()):
        lines.append(f"  Cluster {cid}: {', '.join(members)}")
    lines.append("")

    lines.append("--- PCA ON CANDIDATE COHORT (1Y) ---")
    lines.append("Explained variance ratio:")
    for i, v in enumerate(pca_result["explained_variance_ratio"], start=1):
        lines.append(f"  PC{i}: {v*100:.2f}%")
    lines.append("")
    lines.append("PC1 loadings:")
    lines.append(pca_result["loadings"]["PC1"].round(3).to_string())

    out.write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))


def main() -> None:
    rets_1y = load_returns("2025-05-01")
    rets_2y = load_returns("2024-05-01")

    rets_1y = rets_1y.dropna(thresh=int(0.95 * len(rets_1y.columns)))
    rets_2y = rets_2y.dropna(thresh=int(0.95 * len(rets_2y.columns)))

    corr_1y = correlation_matrix(rets_1y)
    corr_2y = correlation_matrix(rets_2y)

    plot_correlation_heatmap(
        corr_1y, ATT / "boutique-cluster-correlation-1y.png",
        "Daily-return correlation, 1Y (2025-05-01 to 2026-04-30)",
    )
    plot_correlation_heatmap(
        corr_2y, ATT / "boutique-cluster-correlation-2y.png",
        "Daily-return correlation, 2Y (2024-05-01 to 2026-04-30)",
    )

    clusters_1y = hierarchical_cluster(
        corr_1y, ATT / "boutique-cluster-dendrogram-1y.png",
        "Hierarchical clustering (1Y, average linkage on 1-|corr|)",
    )

    candidate = [t for t in UNIVERSE["cluster"] if t in corr_1y.columns]
    pca_result = pca_analysis(
        rets_1y, candidate, ATT / "boutique-cluster-pca-1y.png",
        "PCA on candidate cluster (1Y)",
    )

    intra_inter = avg_intra_vs_inter(corr_1y)
    write_summary(
        rets_1y, rets_2y, corr_1y, corr_2y, clusters_1y, pca_result,
        intra_inter, ATT / "boutique-cluster-results.txt",
    )


if __name__ == "__main__":
    main()
