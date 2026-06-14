"""Threshold-stability scan for cluster validation.

The dendrogram cut threshold (1 - |corr| distance) is a free parameter. A
proposed cohort that returns as one cluster at threshold 0.4 but splits into
three sub-clusters at 0.35 (or merges with a comparator group at 0.5) has weak
boundary stability — the validation is sensitive to a knob the user picked.

This script sweeps thresholds from 0.20 to 0.70 in 0.05 steps and reports, at
each step:
  - Whether the candidate cohort is a single cluster
  - If not, how many sub-clusters the cohort splits into
  - What fraction of cohort tickers are in the largest sub-cluster
  - Whether any non-cohort tickers have joined the cohort's largest sub-cluster

The "stable range" is the contiguous band of thresholds where the cohort is
intact (all members in one cluster, no contamination). Stable ranges of width
>= 0.10 indicate the cluster boundary is robust to threshold choice. Stable
ranges of width < 0.05 indicate the cluster only exists at a specific cut.

Usage:
  python scripts/cluster_threshold_scan.py --primary RKLB
  python scripts/cluster_threshold_scan.py --primary MAG7
  python scripts/cluster_threshold_scan.py --config scripts/cluster_configs/wfe_quartet.yaml

Outputs (in investing/attachments/):
  {prefix}-threshold-scan.png   Line plot: threshold vs cluster-size and cohort-share
  {prefix}-threshold-scan.txt   Table of assignments at each threshold + stable range
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
from scipy.cluster.hierarchy import fcluster, linkage
from scipy.spatial.distance import squareform

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
    p.add_argument("--start", type=float, default=0.20)
    p.add_argument("--stop", type=float, default=0.70)
    p.add_argument("--step", type=float, default=0.05)
    return p.parse_args()


def assignments_at_threshold(corr: pd.DataFrame, threshold: float) -> dict[str, int]:
    dist = 1 - corr.abs()
    dist_arr = dist.to_numpy(copy=True)  # writeable: df.values is read-only under pandas CoW
    np.fill_diagonal(dist_arr, 0)
    condensed = squareform(dist_arr, checks=False)
    Z = linkage(condensed, method="average")
    flat = fcluster(Z, t=threshold, criterion="distance")
    return dict(zip(corr.columns, [int(c) for c in flat]))


def scan(corr: pd.DataFrame, cohort: list[str], thresholds: np.ndarray) -> pd.DataFrame:
    rows = []
    for t in thresholds:
        assn = assignments_at_threshold(corr, t)
        cohort_assignments = {c: assn[c] for c in cohort if c in assn}
        cluster_counts = pd.Series(list(cohort_assignments.values())).value_counts()
        n_subclusters = len(cluster_counts)
        largest_cluster_id = int(cluster_counts.index[0])
        largest_size = int(cluster_counts.iloc[0])
        cohort_share = largest_size / len(cohort)

        non_cohort_in_largest = [
            t for t, c in assn.items()
            if c == largest_cluster_id and t not in cohort
        ]

        rows.append({
            "threshold": round(float(t), 3),
            "n_subclusters": n_subclusters,
            "largest_subcluster_size": largest_size,
            "cohort_share_in_largest": round(cohort_share, 3),
            "intact": n_subclusters == 1 and len(non_cohort_in_largest) == 0,
            "contamination_count": len(non_cohort_in_largest),
            "contamination_names": ",".join(non_cohort_in_largest[:5]) + ("..." if len(non_cohort_in_largest) > 5 else ""),
            "n_total_clusters": len(set(assn.values())),
        })
    return pd.DataFrame(rows)


def find_stable_ranges(scan_df: pd.DataFrame) -> list[tuple[float, float]]:
    ranges = []
    current_start = None
    prev_t = None
    for _, row in scan_df.iterrows():
        if row["intact"]:
            if current_start is None:
                current_start = row["threshold"]
            prev_t = row["threshold"]
        else:
            if current_start is not None:
                ranges.append((current_start, prev_t))
                current_start = None
    if current_start is not None:
        ranges.append((current_start, prev_t))
    return ranges


def plot_scan(scan_df: pd.DataFrame, ranges: list[tuple[float, float]], n_cohort: int, out: Path, title: str) -> None:
    fig, axes = plt.subplots(2, 1, figsize=(11, 8), sharex=True)

    axes[0].plot(scan_df["threshold"], scan_df["cohort_share_in_largest"], marker="o", color="#2962FF", linewidth=2)
    axes[0].axhline(1.0, color="green", linestyle=":", linewidth=1, alpha=0.6, label="all-members threshold")
    axes[0].set_ylabel("Cohort share in largest sub-cluster")
    axes[0].set_ylim(0, 1.05)
    axes[0].set_title("Cohesion: 1.0 = all cohort members in one cluster")

    for lo, hi in ranges:
        axes[0].axvspan(lo - 0.025, hi + 0.025, alpha=0.15, color="green",
                        label=f"stable range [{lo:.2f}, {hi:.2f}]")
    axes[0].legend(fontsize=9, loc="lower right")

    axes[1].plot(scan_df["threshold"], scan_df["contamination_count"], marker="s", color="#D32F2F", linewidth=2, label="Non-cohort tickers in largest cluster")
    axes[1].plot(scan_df["threshold"], scan_df["n_subclusters"], marker="^", color="#FF6F00", linewidth=2, label="# sub-clusters cohort splits into")
    axes[1].set_ylabel("Count")
    axes[1].set_xlabel("Distance threshold (1 - |corr|)")
    axes[1].set_title("Contamination + fragmentation")
    axes[1].legend(fontsize=9)

    fig.suptitle(title, fontsize=11)
    fig.tight_layout()
    fig.savefig(out, dpi=140, bbox_inches="tight")
    plt.close(fig)


def write_summary(cfg: dict, scan_df: pd.DataFrame, ranges: list[tuple[float, float]], n_cohort: int, out: Path) -> None:
    lines = []
    lines.append(f"{cfg.get('name', cfg['prefix'])} THRESHOLD STABILITY SCAN")
    lines.append(f"Cohort size: {n_cohort}")
    lines.append("")
    lines.append("--- ASSIGNMENT TABLE ---")
    cols = ["threshold", "n_subclusters", "largest_subcluster_size", "cohort_share_in_largest", "contamination_count", "intact"]
    lines.append(scan_df[cols].to_string(index=False))
    lines.append("")

    lines.append("--- STABLE RANGES (intact cohort, no contamination) ---")
    if ranges:
        for lo, hi in ranges:
            width = hi - lo
            verdict = "WIDE" if width >= 0.10 else "NARROW" if width >= 0.05 else "POINT"
            lines.append(f"  [{lo:.2f}, {hi:.2f}]  width = {width:.2f}  ({verdict})")
        total_width = sum(hi - lo for lo, hi in ranges)
        lines.append(f"Total stable width: {total_width:.2f}")
    else:
        lines.append("  None — cohort never returns as a clean single cluster at any threshold.")
    lines.append("")

    lines.append("--- VERDICT ---")
    if not ranges:
        lines.append("BOUNDARY-DEPENDENT: cohort does not form a clean cluster at any threshold tested. Falsification candidate.")
    else:
        total_width = sum(hi - lo for lo, hi in ranges)
        if total_width >= 0.20:
            lines.append("ROBUST: cohort survives a wide range of thresholds; cluster boundary is not sensitive to threshold choice.")
        elif total_width >= 0.10:
            lines.append("MODERATELY ROBUST: cohort intact across multiple thresholds but with a finite stable range.")
        else:
            lines.append("FRAGILE: cohort intact only at narrow threshold band(s). Validation depends on threshold pick.")

    contaminated = scan_df[(~scan_df["intact"]) & (scan_df["contamination_count"] > 0)]
    if len(contaminated) > 0:
        lines.append("")
        lines.append("--- CONTAMINATION DETAIL (non-cohort names joining the cohort's largest cluster) ---")
        for _, row in contaminated.iterrows():
            if row["contamination_names"]:
                lines.append(f"  threshold {row['threshold']:.2f}: + {row['contamination_names']}")

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

    rets = load_returns(cfg["groups"], start_1y, window_end)
    rets = rets.dropna(thresh=int(0.95 * len(rets.columns)))
    cohort = [t for t in cfg["groups"]["cluster"]["tickers"] if t in rets.columns]
    corr = rets.corr()

    thresholds = np.round(np.arange(args.start, args.stop + args.step / 2, args.step), 3)
    scan_df = scan(corr, cohort, thresholds)
    ranges = find_stable_ranges(scan_df)

    prefix = cfg["prefix"]
    plot_scan(
        scan_df, ranges, len(cohort),
        ATT / f"{prefix}-threshold-scan.png",
        f"{cfg.get('name', prefix)} — threshold stability scan (1Y)",
    )
    write_summary(cfg, scan_df, ranges, len(cohort), ATT / f"{prefix}-threshold-scan.txt")

    try:
        from cluster_registry import append_record
        total_width = sum(hi - lo for lo, hi in ranges) if ranges else 0.0
        append_record({
            "test_date": str(date.today()),
            "primary": cfg.get("primary", ""),
            "cohort_name": cfg.get("name", cfg["prefix"]),
            "n_members": len(cohort),
            "threshold_stable_width": round(total_width, 3),
            "threshold_stable_ranges": ";".join(f"{lo:.2f}-{hi:.2f}" for lo, hi in ranges) if ranges else "none",
        })
    except Exception as e:
        print(f"(registry append skipped: {e})")


if __name__ == "__main__":
    main()
