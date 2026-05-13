"""Permutation tests for cluster validation diagnostics.

Two nulls are tested by default:

  1. Independence null  (--null independence)
     Shuffle each ticker's return series independently, preserving its marginals
     but breaking the cross-ticker time alignment. Tests "are the series moving
     together at all?" This is a weak null — almost any group of stocks beats it.

  2. Random-basket null (--null random-basket)
     Repeatedly sample N=|cohort| tickers from a universe (default: union of
     all non-cluster groups in the config) and compute their intra-correlation
     and PC1 variance. Tests "could the observed cohesion arise from a random
     N-pick of comparable names?" This is the meaningful null for a cluster
     identity claim.

  Default (--null both) runs both and reports p-values for each.

Block-bootstrap variant (--block-size N>1) shuffles in blocks rather than
individual days, preserving short-range autocorrelation (independence null only).

Universe for random-basket null (in priority order):
  --universe-file path.txt   one ticker per line, comments with #
  Union of non-cluster groups from the YAML config  (default)

Usage:
  python scripts/cluster_permutation_test.py --primary RKLB
  python scripts/cluster_permutation_test.py --primary MAG7 --n-perm 20000
  python scripts/cluster_permutation_test.py --primary RKLB --null random-basket
  python scripts/cluster_permutation_test.py --primary RKLB --universe-file scripts/universes/large_cap_us.txt

Outputs (in investing/attachments/):
  {prefix}-permutation.png    Null distributions + observed markers (one per null)
  {prefix}-permutation.txt    Numeric summary (p-values, percentiles, decision)

Interpretation:
  Independence null:  rejection (p<0.001) just confirms the series co-move at all.
                      Almost every cohort passes this. Necessary but not sufficient.
  Random-basket null: rejection (p<0.05) means the cohort is more cohesive than
                      a random N-pick from the same universe. This is the test
                      that distinguishes a real cluster from a random basket.
"""

from __future__ import annotations

import argparse
from datetime import date, timedelta
from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA

import sqlite3

from cluster_analysis import (
    ATT,
    DB,
    latest_weekday,
    load_returns,
    resolve_config,
)


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    p.add_argument("--config", type=Path)
    p.add_argument("--primary")
    p.add_argument("--prefix")
    p.add_argument("--threshold", type=float)
    p.add_argument("--n-perm", type=int, default=10000, help="Number of permutations (default 10000)")
    p.add_argument("--block-size", type=int, default=1, help="Block size for independence-null block bootstrap (default 1)")
    p.add_argument(
        "--null", choices=["independence", "random-basket", "both"], default="both",
        help="Which null to test (default both)",
    )
    p.add_argument("--universe-file", type=Path, help="Random-basket universe file (one ticker per line)")
    p.add_argument(
        "--universe-from-config", action="store_true",
        help="Use union of non-cluster config groups as the random-basket universe (default: pull from DB ticker_metadata where data_type='stock')",
    )
    p.add_argument("--seed", type=int, default=42)
    return p.parse_args()


def intra_correlation(rets: pd.DataFrame, candidate: list[str]) -> float:
    sub = rets[candidate].dropna()
    if sub.empty or (sub.std() == 0).any():
        return float("nan")
    corr = sub.corr().values
    upper = corr[np.triu_indices_from(corr, k=1)]
    return float(upper.mean())


def pc1_explained_variance(rets: pd.DataFrame, candidate: list[str]) -> float:
    sub = rets[candidate].dropna()
    stds = sub.std()
    if (stds == 0).any() or sub.empty:
        return float("nan")
    standardized = (sub - sub.mean()) / stds
    pca = PCA(n_components=min(5, len(candidate)))
    pca.fit(standardized)
    return float(pca.explained_variance_ratio_[0])


def block_shuffle(series: np.ndarray, block_size: int, rng: np.random.Generator) -> np.ndarray:
    if block_size <= 1:
        idx = rng.permutation(len(series))
        return series[idx]
    n = len(series)
    n_blocks = int(np.ceil(n / block_size))
    starts = rng.integers(0, n - block_size + 1, size=n_blocks)
    out = np.concatenate([series[s : s + block_size] for s in starts])
    return out[:n]


def permute_panel(rets: pd.DataFrame, candidate: list[str], block_size: int, rng: np.random.Generator) -> pd.DataFrame:
    permuted = {}
    for t in candidate:
        col = rets[t].dropna().values
        permuted[t] = block_shuffle(col, block_size, rng)
    min_len = min(len(v) for v in permuted.values())
    return pd.DataFrame({t: v[:min_len] for t, v in permuted.items()})


def run_independence_null(rets: pd.DataFrame, candidate: list[str], n_perm: int, block_size: int, seed: int):
    rng = np.random.default_rng(seed)
    intra_null = np.empty(n_perm)
    pc1_null = np.empty(n_perm)
    for i in range(n_perm):
        perm = permute_panel(rets, candidate, block_size, rng)
        intra_null[i] = intra_correlation(perm, candidate)
        pc1_null[i] = pc1_explained_variance(perm, candidate)
        if (i + 1) % max(1, n_perm // 10) == 0:
            print(f"  independence permutation {i+1}/{n_perm}")
    return intra_null, pc1_null


def load_universe_file(path: Path) -> list[str]:
    tickers = []
    for line in path.read_text(encoding="utf-8").splitlines():
        s = line.strip()
        if s and not s.startswith("#"):
            tickers.append(s.split()[0].upper())
    return tickers


def default_universe_from_config(cfg: dict) -> list[str]:
    out = []
    for grp_name, spec in cfg["groups"].items():
        if grp_name == "cluster":
            continue
        out.extend(spec["tickers"])
    return list(dict.fromkeys(out))


def default_universe_from_db(window_start: str, window_end: str, min_obs: int = 200) -> list[str]:
    sql = """
        SELECT Ticker, COUNT(*) AS n
        FROM prices_long
        WHERE Date >= ? AND Date <= ?
        GROUP BY Ticker
        HAVING n >= ?
        ORDER BY Ticker
    """
    with sqlite3.connect(DB) as conn:
        rows = conn.execute(sql, (window_start, window_end, min_obs)).fetchall()
    return [r[0] for r in rows]


def load_universe_returns(universe: list[str], window_start: str, window_end: str, min_obs: int) -> pd.DataFrame:
    """Load wide-format returns for a large ticker universe without dropping rows.
    Keeps NaNs in place; per-sample assembly drops rows missing any sampled ticker."""
    if not universe:
        return pd.DataFrame()
    placeholders = ",".join("?" for _ in universe)
    sql = (
        f"SELECT Date, Ticker, Close FROM prices_long "
        f"WHERE Ticker IN ({placeholders}) AND Date >= ? AND Date <= ? ORDER BY Date"
    )
    with sqlite3.connect(DB) as conn:
        df = pd.read_sql(sql, conn, params=universe + [window_start, window_end])
    df["Date"] = pd.to_datetime(df["Date"])
    px = df.pivot(index="Date", columns="Ticker", values="Close").sort_index()
    rets = np.log(px / px.shift(1))
    keep = [t for t in rets.columns if rets[t].dropna().size >= min_obs]
    return rets[keep]


def run_random_basket_null(
    universe_rets: pd.DataFrame, cohort_n: int, n_perm: int, seed: int,
):
    rng = np.random.default_rng(seed + 1)
    intra_null = np.empty(n_perm)
    pc1_null = np.empty(n_perm)
    pool = list(universe_rets.columns)
    if len(pool) < cohort_n:
        raise SystemExit(
            f"Universe has only {len(pool)} usable tickers; need >= {cohort_n}. "
            "Provide --universe-file with more tickers or expand comparator groups in the config."
        )
    n_skipped = 0
    for i in range(n_perm):
        sample = list(rng.choice(pool, size=cohort_n, replace=False))
        sub = universe_rets[sample].dropna()
        if len(sub) < 30 or (sub.std() == 0).any():
            n_skipped += 1
            intra_null[i] = np.nan
            pc1_null[i] = np.nan
            continue
        intra_null[i] = intra_correlation(universe_rets, sample)
        pc1_null[i] = pc1_explained_variance(universe_rets, sample)
        if (i + 1) % max(1, n_perm // 10) == 0:
            print(f"  random-basket sample {i+1}/{n_perm}  (pool size {len(pool)}, skipped {n_skipped})")
    intra_null = intra_null[~np.isnan(intra_null)]
    pc1_null = pc1_null[~np.isnan(pc1_null)]
    return intra_null, pc1_null


def p_value_right_tail(observed: float, null_dist: np.ndarray) -> float:
    return float((null_dist >= observed).mean())


def _hist_panel(ax, null_dist, observed, label, xlabel, p_val):
    ax.hist(null_dist, bins=60, color="#999999", edgecolor="white", alpha=0.8)
    ax.axvline(observed, color="#2962FF", linewidth=2.5, label=f"observed = {observed:.3f}")
    ax.axvline(np.quantile(null_dist, 0.95), color="#FF6F00", linestyle="--", linewidth=1, label="null 95th pct")
    ax.axvline(np.quantile(null_dist, 0.99), color="#D32F2F", linestyle="--", linewidth=1, label="null 99th pct")
    ax.set_xlabel(xlabel)
    ax.set_ylabel("Count")
    ax.set_title(f"{label}: p = {p_val:.4f}")
    ax.legend(fontsize=8, loc="upper left")


def plot_null_distributions(
    results: dict, intra_obs: float, pc1_obs: float, out: Path, title: str,
) -> None:
    n_rows = len(results)
    fig, axes = plt.subplots(n_rows, 2, figsize=(13, 4.5 * n_rows), squeeze=False)
    for row, (null_name, r) in enumerate(results.items()):
        _hist_panel(
            axes[row, 0], r["intra_null"], intra_obs,
            f"[{null_name}] intra-corr", "Intra-cluster correlation", r["p_intra"],
        )
        _hist_panel(
            axes[row, 1], r["pc1_null"] * 100, pc1_obs * 100,
            f"[{null_name}] PC1 variance", "PC1 explained variance (%)", r["p_pc1"],
        )
    fig.suptitle(title, fontsize=11)
    fig.tight_layout()
    fig.savefig(out, dpi=140, bbox_inches="tight")
    plt.close(fig)


def _verdict(p: float, null_label: str) -> str:
    if p < 0.001:
        return f"REJECTS {null_label} null at p < 0.001"
    if p < 0.01:
        return f"REJECTS {null_label} null at p < 0.01"
    if p < 0.05:
        return f"REJECTS {null_label} null at p < 0.05"
    return f"FAILS to reject {null_label} null (p >= 0.05)"


def _null_section(label: str, r: dict) -> list[str]:
    lines = []
    lines.append(f"--- {label.upper()} NULL ---")
    lines.append(f"Permutations: {len(r['intra_null'])}")
    if "extra" in r:
        for k, v in r["extra"].items():
            lines.append(f"{k}: {v}")
    lines.append("Intra-cluster correlation:")
    lines.append(f"  Null mean:        {r['intra_null'].mean():.4f}")
    lines.append(f"  Null 95th pct:    {np.quantile(r['intra_null'], 0.95):.4f}")
    lines.append(f"  Null 99th pct:    {np.quantile(r['intra_null'], 0.99):.4f}")
    lines.append(f"  p-value (right):  {r['p_intra']:.6f}    -> {_verdict(r['p_intra'], label)}")
    lines.append("PC1 explained variance:")
    lines.append(f"  Null mean:        {r['pc1_null'].mean()*100:.2f}%")
    lines.append(f"  Null 95th pct:    {np.quantile(r['pc1_null'], 0.95)*100:.2f}%")
    lines.append(f"  Null 99th pct:    {np.quantile(r['pc1_null'], 0.99)*100:.2f}%")
    lines.append(f"  p-value (right):  {r['p_pc1']:.6f}    -> {_verdict(r['p_pc1'], label)}")
    lines.append("")
    return lines


def write_summary(
    cfg: dict, candidate: list[str], rets: pd.DataFrame,
    intra_obs: float, pc1_obs: float, results: dict, out: Path,
) -> None:
    lines = []
    lines.append(f"{cfg.get('name', cfg['prefix'])} PERMUTATION TESTS")
    lines.append(f"Window: {rets.index.min().date()} -> {rets.index.max().date()} ({len(rets)} obs)")
    lines.append(f"Candidate cohort: {', '.join(candidate)} (N={len(candidate)})")
    lines.append(f"Observed intra-corr: {intra_obs:.4f}    Observed PC1: {pc1_obs*100:.2f}%")
    lines.append("")

    for null_name, r in results.items():
        lines.extend(_null_section(null_name, r))

    lines.append("--- INTERPRETATION ---")
    if "independence" in results:
        ri = results["independence"]
        if ri["p_intra"] < 0.05 and ri["p_pc1"] < 0.05:
            lines.append("Independence null rejected: the cohort series co-move (necessary, not sufficient).")
        else:
            lines.append("Independence null NOT rejected: cohort co-movement is consistent with chance — falsification on the weak null.")
    if "random-basket" in results:
        rb = results["random-basket"]
        if rb["p_intra"] < 0.05 and rb["p_pc1"] < 0.05:
            lines.append("Random-basket null rejected: cohort is more cohesive than a random N-pick from the same universe. This is the meaningful pass.")
        elif rb["p_intra"] < 0.05 or rb["p_pc1"] < 0.05:
            lines.append("Random-basket null partially rejected: one diagnostic passes, one does not. Cohort cohesion is borderline relative to comparable random baskets.")
        else:
            lines.append("Random-basket null NOT rejected: cohort cohesion is indistinguishable from a random N-pick of comparable names. Cluster claim is falsified at conventional significance.")

    out.write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))


def main() -> None:
    args = parse_args()
    cfg = resolve_config(args)

    if "cluster" not in cfg["groups"]:
        raise SystemExit("Config must define a 'cluster' group")

    window_end = cfg.get("window_end") or latest_weekday()
    if isinstance(window_end, date):
        window_end = window_end.isoformat()
    end_date = date.fromisoformat(window_end)
    start_1y = (end_date - timedelta(days=365)).isoformat()

    cohort_universe = {"cluster": cfg["groups"]["cluster"]}
    rets = load_returns(cohort_universe, start_1y, window_end)
    rets = rets.dropna(thresh=int(0.95 * len(rets.columns)))
    candidate = [t for t in cfg["groups"]["cluster"]["tickers"] if t in rets.columns]

    intra_obs = intra_correlation(rets, candidate)
    pc1_obs = pc1_explained_variance(rets, candidate)
    print(f"Observed intra-corr = {intra_obs:.4f}, PC1 = {pc1_obs*100:.2f}%")

    results = {}

    if args.null in ("independence", "both"):
        print(f"Running {args.n_perm} independence-null permutations (block size {args.block_size})...")
        intra_null, pc1_null = run_independence_null(rets, candidate, args.n_perm, args.block_size, args.seed)
        results["independence"] = {
            "intra_null": intra_null,
            "pc1_null": pc1_null,
            "p_intra": p_value_right_tail(intra_obs, intra_null),
            "p_pc1": p_value_right_tail(pc1_obs, pc1_null),
            "extra": {"Block size": args.block_size},
        }

    if args.null in ("random-basket", "both"):
        if args.universe_file:
            universe = load_universe_file(args.universe_file)
            universe_source = f"file: {args.universe_file}"
        elif args.universe_from_config:
            universe = default_universe_from_config(cfg)
            universe_source = "union of non-cluster groups in config"
        else:
            universe = default_universe_from_db(start_1y, window_end)
            universe_source = f"DB prices_long ({len(universe)} tickers with >=200 obs in window)"

        universe = [t for t in universe if t not in candidate]
        min_obs = int(0.8 * len(rets))
        universe_rets = load_universe_returns(universe, start_1y, window_end, min_obs)
        print(f"Running {args.n_perm} random-basket permutations (pool of {len(universe_rets.columns)} tickers from {universe_source})...")
        intra_null, pc1_null = run_random_basket_null(universe_rets, len(candidate), args.n_perm, args.seed)
        results["random-basket"] = {
            "intra_null": intra_null,
            "pc1_null": pc1_null,
            "p_intra": p_value_right_tail(intra_obs, intra_null),
            "p_pc1": p_value_right_tail(pc1_obs, pc1_null),
            "extra": {"Universe source": universe_source, "Pool size": len(universe_rets.columns)},
        }

    prefix = cfg["prefix"]
    plot_null_distributions(
        results, intra_obs, pc1_obs,
        ATT / f"{prefix}-permutation.png",
        f"{cfg.get('name', prefix)} — null distributions ({args.n_perm} permutations per null)",
    )
    write_summary(
        cfg, candidate, rets, intra_obs, pc1_obs, results,
        ATT / f"{prefix}-permutation.txt",
    )

    try:
        from cluster_registry import append_record
        append_record({
            "test_date": str(date.today()),
            "primary": cfg.get("primary", ""),
            "cohort_name": cfg.get("name", cfg["prefix"]),
            "n_members": len(candidate),
            "window_start": start_1y,
            "window_end": window_end,
            "intra_corr_1y": round(intra_obs, 4),
            "pc1_variance_pct": round(pc1_obs * 100, 2),
            "p_independence_intra": results.get("independence", {}).get("p_intra"),
            "p_random_basket_intra": results.get("random-basket", {}).get("p_intra"),
            "p_random_basket_pc1": results.get("random-basket", {}).get("p_pc1"),
            "n_permutations": args.n_perm,
        })
    except Exception as e:
        print(f"(registry append skipped: {e})")


if __name__ == "__main__":
    main()
