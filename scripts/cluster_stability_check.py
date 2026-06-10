"""Cluster stability check across YTD / 1Y / 2Y / 3Y windows.

For a cohort defined in a scripts/cluster_configs/*.yaml config, computes
intra-cluster correlation, pairwise range, standardized PC1/PC2 explained
variance, cross-correlation to a control group, and the intra-vs-control gap
on each window. A stable or widening gap across windows is the cleanest
evidence the cluster has a durable identity distinct from its nearest
neighbor (see docs/cluster-validation.md, "Stability check across windows").

History (2026-06-09 audit remediation): this script previously read the
deprecated wide table stock_prices_daily with a hardcoded Space pure-plays
cohort and end date, and ran PCA on non-standardized returns (PC1 dominated
by the highest-vol name). It now uses canonical prices_long via
cluster_analysis.load_returns, the shared YAML config schema, and
standardized PCA consistent with the rest of the suite.

Usage:
  python scripts/cluster_stability_check.py --primary RKLB
  python scripts/cluster_stability_check.py --config scripts/cluster_configs/rklb.yaml
  python scripts/cluster_stability_check.py --primary RKLB --control defense_primes

Outputs:
  Console table + investing/attachments/{prefix}-stability-windows.txt
"""

from __future__ import annotations

import argparse
from datetime import date, timedelta
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.decomposition import PCA

from cluster_analysis import (
    ATT,
    latest_weekday,
    load_returns,
    resolve_config,
)


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    p.add_argument("--config", type=Path)
    p.add_argument("--primary")
    p.add_argument("--prefix")
    p.add_argument("--threshold", type=float, help="(unused — resolve_config compat)")
    p.add_argument("--control", help="Config group to compare against (default: first non-cluster group)")
    return p.parse_args()


def diagnostic(rets: pd.DataFrame, tickers: list[str]) -> dict | None:
    sub = rets[tickers].dropna()
    if len(sub) < 30:
        return None
    stds = sub.std()
    if (stds == 0).any():
        return None
    corr = sub.corr()
    mask = np.triu(np.ones_like(corr, dtype=bool), k=1)
    pair_corrs = corr.where(mask).stack()
    standardized = (sub - sub.mean()) / stds
    pca = PCA(n_components=min(5, len(tickers)))
    pca.fit(standardized)
    evr = pca.explained_variance_ratio_
    return {
        "obs": len(sub),
        "intra_avg": float(pair_corrs.mean()),
        "intra_min": float(pair_corrs.min()),
        "intra_max": float(pair_corrs.max()),
        "pc1": float(evr[0]),
        "pc2": float(evr[1]) if len(evr) > 1 else 0.0,
    }


def cross_corr(rets: pd.DataFrame, group_a: list[str], group_b: list[str]) -> float:
    cols = [t for t in group_a + group_b if t in rets.columns]
    rets_clean = rets[cols].dropna()
    if len(rets_clean) < 30:
        return float("nan")
    corr = rets_clean.corr()
    pairs = [
        corr.loc[a, b]
        for a in group_a if a in corr.index
        for b in group_b if b in corr.columns
    ]
    return float(np.mean(pairs)) if pairs else float("nan")


def main() -> None:
    args = parse_args()
    cfg = resolve_config(args)
    if "cluster" not in cfg["groups"]:
        raise SystemExit("Config must define a 'cluster' group")

    cohort = cfg["groups"]["cluster"]["tickers"]
    non_cluster = [g for g in cfg["groups"] if g != "cluster"]
    if args.control:
        if args.control not in cfg["groups"]:
            raise SystemExit(f"--control {args.control} not a config group; available: {', '.join(non_cluster)}")
        control_name = args.control
    elif non_cluster:
        control_name = non_cluster[0]
    else:
        control_name = None
    control = cfg["groups"][control_name]["tickers"] if control_name else []

    window_end = cfg.get("window_end") or latest_weekday()
    if isinstance(window_end, date):
        window_end = window_end.isoformat()
    end_date = date.fromisoformat(window_end)

    windows = {
        f"YTD {end_date.year}": (date(end_date.year, 1, 2).isoformat(), window_end),
        "1Y": ((end_date - timedelta(days=365)).isoformat(), window_end),
        "2Y": ((end_date - timedelta(days=730)).isoformat(), window_end),
        "3Y": ((end_date - timedelta(days=1095)).isoformat(), window_end),
    }

    groups = {"cluster": cfg["groups"]["cluster"]}
    if control_name:
        groups[control_name] = cfg["groups"][control_name]

    lines = []
    title = f"{cfg.get('name', cfg['prefix'])} STABILITY CHECK (windows ending {window_end}"
    title += f", control: {control_name})" if control_name else ", no control)"
    lines.append(title)
    header = (
        f"{'Window':<12} {'obs':>5} {'intra':>7} {'range':>14} {'PC1':>7} {'PC2':>7} "
        f"{'vs ctl':>8} {'gap':>7}"
    )
    lines.append(header)
    lines.append("-" * len(header))

    warned_missing = False
    for name, (start, end) in windows.items():
        rets = load_returns(groups, start, end)
        present = [t for t in cohort if t in rets.columns]
        missing = [t for t in cohort if t not in rets.columns]
        if missing and not warned_missing:
            print(f"WARNING: cluster ticker(s) with no data, EXCLUDED from all windows shown: {', '.join(missing)}")
            lines.append(f"WARNING — configured but EXCLUDED (no data): {', '.join(missing)}")
            warned_missing = True
        d = diagnostic(rets, present) if len(present) >= 2 else None
        if d is None:
            lines.append(f"{name:<12} {len(rets):>5}  -- insufficient data --")
            continue
        vs_ctl = cross_corr(rets, present, control) if control else float("nan")
        gap = d["intra_avg"] - vs_ctl if not np.isnan(vs_ctl) else float("nan")
        lines.append(
            f"{name:<12} {d['obs']:>5} "
            f"{d['intra_avg']:>7.3f} [{d['intra_min']:.2f},{d['intra_max']:.2f}] "
            f"{d['pc1']:>7.1%} {d['pc2']:>7.1%} "
            f"{vs_ctl:>8.3f} {gap:>+7.3f}"
        )

    out = ATT / f"{cfg['prefix']}-stability-windows.txt"
    out.write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))
    print(f"\nSaved: {out}")


if __name__ == "__main__":
    main()
