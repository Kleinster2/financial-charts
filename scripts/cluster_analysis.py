"""Cluster validation for vault actor notes.

Tests whether a candidate cohort of public-company tickers constitutes a
statistically distinct cluster, and what exactly the cluster contains, using
four diagnostics on daily log returns:

  1. Pairwise return correlation matrix (heatmap, 1Y + 2Y windows)
  2. Hierarchical clustering with 1-|corr| distance (dendrogram)
  3. PCA on the candidate cohort (scree + PC1 loadings)
  4. 90-day rolling tightness history (avg corr, PC1, core/satellite)

Usage:
  python scripts/cluster_analysis.py --config scripts/cluster_configs/boutique_advisory.yaml
  python scripts/cluster_analysis.py --primary PWP  # auto-loads scripts/cluster_configs/pwp.yaml

YAML config schema (see scripts/cluster_configs/boutique_advisory.yaml for full example):
  name: Boutique advisory
  primary: PWP                   # optional; used in output prefix if --prefix not set
  prefix: boutique-cluster       # output filename stem
  threshold: 0.4                 # dendrogram cut threshold (1-|corr| distance)
  window_end: 2026-04-30         # optional; defaults to latest weekday
  history_start: 2020-01-01      # optional; defaults to 2020-01-01
  groups:
    cluster:
      color: "#2962FF"           # cluster always blue per actor convention
      tickers: [PWP, LAZ, EVR, MC, HLI, PJT]
    <other_group_name>:
      color: "#000000"
      tickers: [GS, MS, JPM]

Outputs (saved to investing/attachments/{prefix}-*.png and -results.txt):
  {prefix}-correlation-1y.png
  {prefix}-correlation-2y.png
  {prefix}-dendrogram-1y.png
  {prefix}-pca-1y.png
  {prefix}-rolling-tightness-90d.png
  {prefix}-results.txt

See docs/cluster-validation.md for the full standard, when to run, and how to
interpret the output.
"""

from __future__ import annotations

import argparse
import sqlite3
import sys
from datetime import date, timedelta
from pathlib import Path

# Windows consoles default to cp1252; printing a non-ASCII cohort name (e.g.
# the CJK "中特估") raises UnicodeEncodeError. In the test scripts that crash
# happens *before* the registry row is written, so the row silently never lands
# (exit 0 — it looks like it ran). Reconfigure stdout/stderr to UTF-8 on import
# so every script in the cluster family (all import from this module) is safe.
for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import yaml
from scipy.cluster.hierarchy import dendrogram, fcluster, linkage
from scipy.spatial.distance import squareform
from sklearn.decomposition import PCA

ROOT = Path(__file__).resolve().parent.parent
DB = ROOT / "market_data.db"
ATT = ROOT / "investing" / "attachments"
CONFIG_DIR = Path(__file__).resolve().parent / "cluster_configs"
ATT.mkdir(parents=True, exist_ok=True)


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    p.add_argument("--config", type=Path, help="Path to YAML config file")
    p.add_argument("--primary", help="Primary actor ticker; auto-loads scripts/cluster_configs/{ticker.lower()}.yaml")
    p.add_argument("--prefix", help="Override output prefix")
    p.add_argument("--threshold", type=float, help="Override dendrogram cut threshold")
    return p.parse_args()


def resolve_config(args: argparse.Namespace) -> dict:
    if args.config:
        path = args.config
    elif args.primary:
        path = CONFIG_DIR / f"{args.primary.lower()}.yaml"
    else:
        raise SystemExit(
            "Provide --config PATH or --primary TICKER (auto-loads scripts/cluster_configs/{ticker}.yaml)"
        )
    if not path.exists():
        raise SystemExit(f"Config not found: {path}")
    with path.open("r", encoding="utf-8") as f:
        cfg = yaml.safe_load(f)
    if args.prefix:
        cfg["prefix"] = args.prefix
    if args.threshold is not None:
        cfg["threshold"] = args.threshold
    cfg.setdefault("threshold", 0.4)
    if "prefix" not in cfg:
        primary = cfg.get("primary") or args.primary
        if not primary:
            raise SystemExit("Config must include 'prefix' or 'primary'")
        cfg["prefix"] = f"{primary.lower()}-cluster"
    return cfg


def latest_weekday() -> str:
    d = date.today()
    while d.weekday() >= 5:
        d -= timedelta(days=1)
    return d.isoformat()


def load_returns(universe: dict, window_start: str, window_end: str) -> pd.DataFrame:
    tickers = [t for grp in universe.values() for t in grp["tickers"]]
    placeholders = ",".join("?" for _ in tickers)
    sql = (
        "SELECT Date, Ticker, Close FROM prices_long "
        f"WHERE Ticker IN ({placeholders}) "
        "AND date(Date) >= date(?) AND date(Date) <= date(?) "
        "ORDER BY Date"
    )
    with sqlite3.connect(DB) as conn:
        df = pd.read_sql(sql, conn, params=tickers + [window_start, window_end])
    df["Date"] = pd.to_datetime(df["Date"])
    px = df.pivot(index="Date", columns="Ticker", values="Close").sort_index()
    rets = np.log(px / px.shift(1)).dropna(how="all")
    return rets[[t for t in tickers if t in rets.columns]]


def ticker_group(ticker: str, universe: dict) -> str:
    for grp, spec in universe.items():
        if ticker in spec["tickers"]:
            return grp
    return "other"


def color_for(ticker: str, universe: dict) -> str:
    grp = ticker_group(ticker, universe)
    if grp == "other":
        return "#000000"
    return universe[grp].get("color", "#000000")


def correlation_matrix(rets: pd.DataFrame) -> pd.DataFrame:
    return rets.corr(method="pearson")


def plot_correlation_heatmap(
    corr: pd.DataFrame, universe: dict, group_order: list[str], out: Path, title: str
) -> None:
    order = [t for grp in group_order for t in universe[grp]["tickers"] if t in corr.columns]
    corr = corr.loc[order, order]

    fig, ax = plt.subplots(figsize=(max(8, 0.45 * len(order)), max(7, 0.4 * len(order))))
    im = ax.imshow(corr.values, cmap="RdBu_r", vmin=-1, vmax=1, aspect="auto")
    ax.set_xticks(range(len(corr.columns)))
    ax.set_yticks(range(len(corr.index)))
    ax.set_xticklabels(corr.columns, rotation=90, fontsize=9)
    ax.set_yticklabels(corr.index, fontsize=9)

    for i, t in enumerate(corr.index):
        c = color_for(t, universe)
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


def hierarchical_cluster(corr: pd.DataFrame, universe: dict, threshold: float, out: Path, title: str) -> dict:
    dist = 1 - corr.abs()
    dist_arr = dist.to_numpy(copy=True)  # writeable: df.values is read-only under pandas CoW
    np.fill_diagonal(dist_arr, 0)
    condensed = squareform(dist_arr, checks=False)
    Z = linkage(condensed, method="average")

    fig, ax = plt.subplots(figsize=(max(10, 0.55 * len(corr.columns)), 6))
    dn = dendrogram(
        Z, labels=list(corr.columns), color_threshold=threshold,
        above_threshold_color="#999999", ax=ax,
    )
    ax.set_title(title, fontsize=11, pad=10)
    ax.set_ylabel("Distance (1 - |corr|)")
    for tick, lbl in zip(ax.get_xticklabels(), dn["ivl"]):
        tick.set_color(color_for(lbl, universe))
    ax.axhline(threshold, color="gray", linestyle="--", linewidth=0.8, alpha=0.5)
    ax.text(0.99, threshold, f" threshold = {threshold}", transform=ax.get_yaxis_transform(),
            ha="right", va="bottom", fontsize=8, color="gray")
    fig.tight_layout()
    fig.savefig(out, dpi=140, bbox_inches="tight")
    plt.close(fig)

    flat = fcluster(Z, t=threshold, criterion="distance")
    clusters: dict[int, list[str]] = {}
    for ticker, c in zip(corr.columns, flat):
        clusters.setdefault(int(c), []).append(ticker)
    return clusters


def pca_analysis(rets: pd.DataFrame, candidate: list[str], out: Path, title: str) -> dict:
    sub = rets[candidate].dropna()
    if len(sub) < 30:
        raise SystemExit(f"PCA requires >=30 obs across all {len(candidate)} candidate tickers; got {len(sub)}")
    daily_vol = sub.std()
    zero_vol = daily_vol[daily_vol == 0].index.tolist()
    if zero_vol:
        raise SystemExit(
            f"PCA aborted: zero-variance return series in window for {', '.join(zero_vol)} "
            "(halted ticker or duplicated prices?)"
        )
    standardized = (sub - sub.mean()) / daily_vol
    pca = PCA(n_components=min(5, len(candidate)))
    pca.fit(standardized)
    explained = pca.explained_variance_ratio_
    loadings = pd.DataFrame(
        pca.components_.T, index=candidate,
        columns=[f"PC{i+1}" for i in range(pca.n_components_)],
    )
    if loadings["PC1"].mean() < 0:
        loadings["PC1"] = -loadings["PC1"]

    pc1 = loadings["PC1"]
    loading_weights = pc1 / pc1.sum()
    raw_mimic = pc1 / daily_vol.replace(0, np.nan)
    raw_mimic_weights = raw_mimic / raw_mimic.sum()
    pc1_weights = pd.DataFrame(
        {
            "PC1 loading": pc1,
            "Loading weight": loading_weights,
            "Ann vol": daily_vol * np.sqrt(252),
            "Raw PC1-mimic weight": raw_mimic_weights,
        }
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

    return {
        "explained_variance_ratio": explained.tolist(),
        "loadings": loadings,
        "pc1_weights": pc1_weights,
    }


def candidate_join_distances(corr: pd.DataFrame, candidate: list[str]) -> pd.DataFrame:
    sub = corr.loc[candidate, candidate].dropna(axis=0, how="any").dropna(axis=1, how="any")
    tickers = list(sub.columns)
    if len(tickers) < 2:
        return pd.DataFrame(columns=["Step", "Left", "Right", "Distance", "Members"])

    dist = 1 - sub.abs()
    dist_arr = dist.to_numpy(copy=True)  # writeable: df.values is read-only under pandas CoW
    np.fill_diagonal(dist_arr, 0)
    Z = linkage(squareform(dist_arr, checks=False), method="average")

    clusters: dict[int, list[str]] = {i: [ticker] for i, ticker in enumerate(tickers)}
    rows = []
    for step, (left_idx, right_idx, distance, _count) in enumerate(Z, start=1):
        left = clusters[int(left_idx)]
        right = clusters[int(right_idx)]
        members = left + right
        rows.append(
            {
                "Step": step,
                "Left": "+".join(left),
                "Right": "+".join(right),
                "Distance": float(distance),
                "Members": "+".join(members),
            }
        )
        clusters[len(tickers) + step - 1] = members

    return pd.DataFrame(rows)


def rolling_tightness_analysis(
    rets: pd.DataFrame,
    candidate: list[str],
    out: Path,
    window: int = 90,
) -> pd.DataFrame:
    sub = rets[candidate].dropna()
    if len(sub) < window:
        return pd.DataFrame(
            columns=[
                "Avg corr",
                "PC1",
                "Core corr",
                "Satellite corr",
                "Final join distance",
            ]
        )

    core = candidate[1:] if len(candidate) > 3 else candidate
    satellite = candidate[0] if len(candidate) > 3 else None
    rows = []
    n_skipped_windows = 0

    for end_i in range(window, len(sub) + 1):
        w = sub.iloc[end_i - window:end_i]
        if (w.std() == 0).any():
            n_skipped_windows += 1
            continue
        corr = w.corr()
        upper = corr.values[np.triu_indices_from(corr, k=1)]

        standardized = (w - w.mean()) / w.std()
        pca = PCA(n_components=min(5, len(candidate)))
        pca.fit(standardized)

        dist = 1 - corr.abs()
        dist_arr = dist.to_numpy(copy=True)  # writeable: df.values is read-only under pandas CoW
        np.fill_diagonal(dist_arr, 0)
        Z = linkage(squareform(dist_arr, checks=False), method="average")

        core_corr = np.nan
        if len(core) >= 2 and all(t in corr.columns for t in core):
            core_sub = corr.loc[core, core].values
            core_upper = core_sub[np.triu_indices_from(core_sub, k=1)]
            core_corr = float(core_upper.mean())

        satellite_corr = np.nan
        if satellite and all(t in corr.columns for t in [satellite] + core):
            satellite_corr = float(np.mean([corr.loc[satellite, t] for t in core]))

        rows.append(
            {
                "Date": w.index[-1],
                "Avg corr": float(upper.mean()),
                "PC1": float(pca.explained_variance_ratio_[0]),
                "Core corr": core_corr,
                "Satellite corr": satellite_corr,
                "Final join distance": float(Z[-1, 2]),
            }
        )

    if n_skipped_windows:
        print(f"Rolling tightness: skipped {n_skipped_windows} window(s) containing a zero-variance series")
    rolling = pd.DataFrame(rows).set_index("Date")

    fig, axes = plt.subplots(2, 1, figsize=(11, 7), sharex=True)
    axes[0].plot(rolling.index, rolling["Avg corr"], color="#2962FF", linewidth=2.0, label="Avg intra-corr")
    axes[0].plot(rolling.index, rolling["PC1"], color="#E91E63", linewidth=1.8, label="PC1 share")
    if "Core corr" in rolling:
        axes[0].plot(rolling.index, rolling["Core corr"], color="#4CAF50", linewidth=1.4, alpha=0.9, label="Core corr")
    if "Satellite corr" in rolling:
        axes[0].plot(
            rolling.index,
            rolling["Satellite corr"],
            color="#FF9800",
            linewidth=1.4,
            alpha=0.9,
            label="Satellite-to-core corr",
        )
    axes[0].set_ylim(0, 1)
    axes[0].set_ylabel("Correlation / PC1")
    axes[0].set_title(f"{window}-day rolling cluster tightness", loc="left", fontsize=12)
    axes[0].grid(True, alpha=0.25)
    axes[0].legend(loc="lower left", fontsize=9, ncol=2, frameon=False)

    axes[1].plot(
        rolling.index,
        rolling["Final join distance"],
        color="#6D4C41",
        linewidth=2.0,
        label="Final candidate join distance",
    )
    axes[1].set_ylabel("1 - |corr|")
    axes[1].grid(True, alpha=0.25)
    axes[1].legend(loc="upper left", fontsize=9, frameon=False)

    fig.tight_layout()
    fig.savefig(out, dpi=140, bbox_inches="tight")
    plt.close(fig)

    return rolling


def weekly_cross_check(rets: pd.DataFrame, candidate: list[str]) -> dict | None:
    """Weekly-return robustness check for asynchronous closes (audit item 7).

    Daily correlations between markets with non-overlapping trading hours are
    structurally depressed (the non-synchronous trading problem); weekly log
    returns (calendar-week sums) restore most of the overlap. A weekly
    intra-correlation materially above daily flags an async-close artifact —
    a cross-region cohort that is tighter than its daily numbers suggest —
    not a weaker cluster."""
    if len(candidate) < 2:
        return None
    sub = rets[candidate].dropna(how="all")
    weekly = sub.resample("W-FRI").sum(min_count=3).dropna()
    if len(weekly) < 20 or (weekly.std() == 0).any():
        return None
    corr = weekly.corr()
    upper = corr.values[np.triu_indices_from(corr, k=1)]
    standardized = (weekly - weekly.mean()) / weekly.std()
    pca = PCA(n_components=min(5, len(candidate)))
    pca.fit(standardized)
    return {
        "n_weeks": len(weekly),
        "intra": float(upper.mean()),
        "pc1": float(pca.explained_variance_ratio_[0]),
    }


def avg_group_pair_correlations(corr: pd.DataFrame, universe: dict) -> dict:
    out = {}
    groups = list(universe.keys())
    for g1 in groups:
        for g2 in groups:
            ts1 = [t for t in universe[g1]["tickers"] if t in corr.columns]
            ts2 = [t for t in universe[g2]["tickers"] if t in corr.columns]
            vals = []
            for a in ts1:
                for b in ts2:
                    if a != b:
                        vals.append(corr.loc[a, b])
            if vals:
                out[(g1, g2)] = float(np.mean(vals))
    return out


def write_summary(
    cfg: dict, rets_1y: pd.DataFrame, rets_2y: pd.DataFrame,
    corr_1y: pd.DataFrame, clusters_1y: dict, pca_result: dict,
    group_pair_corrs: dict, out: Path, rolling_tightness: pd.DataFrame | None = None,
    weekly: dict | None = None,
) -> None:
    lines = []
    lines.append(f"{cfg.get('name', cfg['prefix'])} CLUSTER ANALYSIS")
    lines.append(f"Window 1y: {rets_1y.index.min().date()} -> {rets_1y.index.max().date()} ({len(rets_1y)} obs)")
    lines.append(f"Window 2y: {rets_2y.index.min().date()} -> {rets_2y.index.max().date()} ({len(rets_2y)} obs)")
    lines.append(f"Universe: {len(rets_1y.columns)} tickers across {len(cfg['groups'])} groups")
    configured = [t for grp in cfg["groups"].values() for t in grp["tickers"]]
    missing = [t for t in configured if t not in rets_1y.columns]
    if missing:
        lines.append(f"WARNING — configured but EXCLUDED (no usable data in 1Y window): {', '.join(missing)}")
    lines.append(f"Dendrogram cut threshold: {cfg['threshold']}")
    lines.append("")

    lines.append("--- 1Y INTRA-CLUSTER PAIRWISE CORRELATIONS ---")
    cluster = [t for t in cfg["groups"]["cluster"]["tickers"] if t in corr_1y.columns]
    sub = corr_1y.loc[cluster, cluster]
    lines.append(sub.round(2).to_string())
    upper = sub.values[np.triu_indices_from(sub, k=1)]
    if upper.size:
        lines.append(f"Average intra-cluster correlation: {upper.mean():.3f}")
        lines.append(f"Range: [{upper.min():.3f}, {upper.max():.3f}]")
    lines.append("")

    lines.append("--- AVG GROUP-PAIR CORRELATIONS (1Y) ---")
    groups = list(cfg["groups"].keys())
    header = "             " + "  ".join(f"{g[:7]:>7}" for g in groups)
    lines.append(header)
    for g1 in groups:
        row = f"{g1[:11]:>11}  " + "  ".join(
            f"{group_pair_corrs.get((g1, g2), float('nan')):>7.3f}" for g2 in groups
        )
        lines.append(row)
    lines.append("")
    cc = group_pair_corrs.get(("cluster", "cluster"), float("nan"))
    if not np.isnan(cc):
        lines.append("Cluster vs others:")
        for g in groups:
            if g == "cluster":
                continue
            v = group_pair_corrs.get(("cluster", g), float("nan"))
            if not np.isnan(v):
                lines.append(f"  cluster vs {g:<10}: {v:.3f}  (intra advantage: +{cc - v:.3f})")
        lines.append("")

    lines.append(f"--- HIERARCHICAL CLUSTERS (1Y, distance threshold {cfg['threshold']}) ---")
    for cid, members in sorted(clusters_1y.items()):
        lines.append(f"  Cluster {cid}: {', '.join(members)}")
    lines.append("")

    join_distances = candidate_join_distances(corr_1y, cluster)
    if not join_distances.empty:
        lines.append("--- CANDIDATE JOIN DISTANCES (1Y, average linkage, distance = 1-|corr|) ---")
        join_display = join_distances.copy()
        join_display["Distance"] = join_display["Distance"].map(lambda x: f"{x:.3f}")
        lines.append(join_display.to_string(index=False))
        lines.append("")

    lines.append("--- PCA ON CANDIDATE COHORT (1Y) ---")
    lines.append("Explained variance ratio:")
    for i, v in enumerate(pca_result["explained_variance_ratio"], start=1):
        lines.append(f"  PC{i}: {v*100:.2f}%")
    lines.append("")
    lines.append("PC1 loadings:")
    lines.append(pca_result["loadings"]["PC1"].round(3).to_string())
    lines.append("")
    lines.append("--- PC1 INDEX WEIGHTS (1Y) ---")
    lines.append("PCA is run on standardized daily log returns. Raw PC1-mimic weights scale PC1 loading by inverse realized volatility.")
    pc1_weight_display = pca_result["pc1_weights"].copy()
    pc1_weight_display["PC1 loading"] = pc1_weight_display["PC1 loading"].map(lambda x: f"{x:.3f}")
    pc1_weight_display["Loading weight"] = pc1_weight_display["Loading weight"].map(lambda x: f"{x*100:.2f}%")
    pc1_weight_display["Ann vol"] = pc1_weight_display["Ann vol"].map(lambda x: f"{x*100:.2f}%")
    pc1_weight_display["Raw PC1-mimic weight"] = pc1_weight_display["Raw PC1-mimic weight"].map(
        lambda x: f"{x*100:.2f}%"
    )
    lines.append(pc1_weight_display.to_string())

    if weekly is not None and upper.size:
        lines.append("")
        lines.append("--- WEEKLY-RETURN CROSS-CHECK (1Y, async-close robustness) ---")
        daily_intra = float(upper.mean())
        daily_pc1 = pca_result["explained_variance_ratio"][0]
        lines.append(
            f"Weeks: {weekly['n_weeks']}   "
            f"Weekly intra-corr: {weekly['intra']:.3f} (daily {daily_intra:.3f})   "
            f"Weekly PC1: {weekly['pc1']*100:.1f}% (daily {daily_pc1*100:.1f}%)"
        )
        if weekly["intra"] - daily_intra > 0.10:
            lines.append(
                "NOTE: weekly intra-corr exceeds daily by >0.10 — asynchronous closes are "
                "depressing the daily numbers (cross-region cohort); the weekly reading is "
                "the better estimate of economic co-movement."
            )

    if rolling_tightness is not None and not rolling_tightness.empty:
        lines.append("")
        lines.append("--- HISTORICAL TIGHTNESS EVOLUTION (90D ROLLING) ---")
        by_year = rolling_tightness.groupby(rolling_tightness.index.year).agg(
            {
                "Avg corr": "median",
                "PC1": "median",
                "Core corr": "median",
                "Satellite corr": "median",
                "Final join distance": "median",
            }
        )
        hist_display = by_year.copy()
        for col in ["Avg corr", "Core corr", "Satellite corr", "Final join distance"]:
            hist_display[col] = hist_display[col].map(lambda x: f"{x:.3f}")
        hist_display["PC1"] = hist_display["PC1"].map(lambda x: f"{x*100:.1f}%")
        lines.append(hist_display.to_string())

        latest = rolling_tightness.iloc[-1]
        lines.append("")
        lines.append(
            "Latest 90D: "
            f"avg corr {latest['Avg corr']:.3f}, "
            f"PC1 {latest['PC1']*100:.1f}%, "
            f"core corr {latest['Core corr']:.3f}, "
            f"satellite corr {latest['Satellite corr']:.3f}, "
            f"final join distance {latest['Final join distance']:.3f}"
        )

    out.write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))


def main() -> None:
    args = parse_args()
    cfg = resolve_config(args)

    if "cluster" not in cfg["groups"]:
        raise SystemExit("Config must define a 'cluster' group (the candidate cohort being validated)")

    window_end = cfg.get("window_end") or latest_weekday()
    if isinstance(window_end, date):
        end_date = window_end
        window_end = end_date.isoformat()
    else:
        end_date = date.fromisoformat(window_end)
    start_1y = (end_date - timedelta(days=365)).isoformat()
    start_2y = (end_date - timedelta(days=730)).isoformat()

    rets_1y = load_returns(cfg["groups"], start_1y, window_end)
    rets_2y = load_returns(cfg["groups"], start_2y, window_end)
    rets_1y = rets_1y.dropna(thresh=int(0.95 * len(rets_1y.columns)))
    rets_2y = rets_2y.dropna(thresh=int(0.95 * len(rets_2y.columns)))
    configured = [t for grp in cfg["groups"].values() for t in grp["tickers"]]
    missing = [t for t in configured if t not in rets_1y.columns]
    if missing:
        print(
            f"WARNING: {len(missing)} configured ticker(s) have no usable data in the 1Y window "
            f"and are EXCLUDED: {', '.join(missing)}"
        )
    history_start = cfg.get("history_start", "2020-01-01")
    if isinstance(history_start, date):
        history_start = history_start.isoformat()
    history_groups = {"cluster": cfg["groups"]["cluster"]}
    rets_history = load_returns(history_groups, history_start, window_end)

    corr_1y = correlation_matrix(rets_1y)
    corr_2y = correlation_matrix(rets_2y)

    prefix = cfg["prefix"]
    group_order = list(cfg["groups"].keys())

    plot_correlation_heatmap(
        corr_1y, cfg["groups"], group_order,
        ATT / f"{prefix}-correlation-1y.png",
        f"Daily-return correlation, 1Y ({start_1y} to {window_end})",
    )
    plot_correlation_heatmap(
        corr_2y, cfg["groups"], group_order,
        ATT / f"{prefix}-correlation-2y.png",
        f"Daily-return correlation, 2Y ({start_2y} to {window_end})",
    )

    clusters_1y = hierarchical_cluster(
        corr_1y, cfg["groups"], cfg["threshold"],
        ATT / f"{prefix}-dendrogram-1y.png",
        f"Hierarchical clustering (1Y, average linkage on 1-|corr|)",
    )

    candidate = [t for t in cfg["groups"]["cluster"]["tickers"] if t in corr_1y.columns]
    pca_result = pca_analysis(
        rets_1y, candidate,
        ATT / f"{prefix}-pca-1y.png",
        f"PCA on candidate cluster (1Y)",
    )
    rolling_tightness = rolling_tightness_analysis(
        rets_history,
        candidate,
        ATT / f"{prefix}-rolling-tightness-90d.png",
        window=90,
    )

    group_pair_corrs = avg_group_pair_correlations(corr_1y, cfg["groups"])
    weekly = weekly_cross_check(rets_1y, candidate)
    write_summary(
        cfg, rets_1y, rets_2y, corr_1y, clusters_1y, pca_result,
        group_pair_corrs, ATT / f"{prefix}-results.txt", rolling_tightness,
        weekly=weekly,
    )


if __name__ == "__main__":
    main()
