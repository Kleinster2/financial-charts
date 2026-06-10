"""Out-of-sample holdout test for cluster validation.

Splits the analysis window temporally into older-half train + newer-half test
(no random shuffling — temporal order is preserved to test regime durability).
Computes intra-cluster correlation, PC1 explained variance, and pairwise-corr
range on each half independently, then reports the stability ratio.

A real cluster should retain its cohesion across regimes. A cohort whose
intra-corr collapses between train and test is a single-regime artifact, not a
durable factor.

Usage:
  python scripts/cluster_holdout_test.py --primary RKLB
  python scripts/cluster_holdout_test.py --primary MAG7 --window 2y
  python scripts/cluster_holdout_test.py --config scripts/cluster_configs/rklb.yaml --window 3y

Window options:
  1y (default): split 1Y window into two 6mo halves
  2y:           split 2Y window into two 1Y halves
  3y:           split 3Y window into two 18mo halves

Outputs (in investing/attachments/):
  {prefix}-holdout.png    Side-by-side bar chart of train vs test diagnostics
  {prefix}-holdout.txt    Numeric summary + stability verdict

Interpretation:
  test_intra / train_intra >= 0.85  : stable cluster (durable factor)
  test_intra / train_intra 0.60-0.85: weakened cluster (factor present but eroding)
  test_intra / train_intra < 0.60   : regime-dependent (no durable cluster)
  test_intra > train_intra          : strengthening cluster (often institutional basket forming)
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

from cluster_analysis import (
    ATT,
    latest_weekday,
    load_returns,
    resolve_config,
)

WINDOW_DAYS = {"1y": 365, "2y": 730, "3y": 1095}


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    p.add_argument("--config", type=Path)
    p.add_argument("--primary")
    p.add_argument("--prefix")
    p.add_argument("--threshold", type=float)
    p.add_argument("--window", choices=list(WINDOW_DAYS.keys()), default="2y")
    return p.parse_args()


def diagnostics(rets: pd.DataFrame, candidate: list[str]) -> dict:
    sub = rets[candidate].dropna()
    if len(sub) < 30:
        return {"n_obs": len(sub), "intra": float("nan"), "pc1": float("nan"),
                "corr_min": float("nan"), "corr_max": float("nan"), "corr_range": float("nan")}
    corr = sub.corr().values
    upper = corr[np.triu_indices_from(corr, k=1)]
    standardized = (sub - sub.mean()) / sub.std()
    pca = PCA(n_components=min(5, len(candidate)))
    pca.fit(standardized)
    return {
        "n_obs": len(sub),
        "intra": float(upper.mean()),
        "pc1": float(pca.explained_variance_ratio_[0]),
        "corr_min": float(upper.min()),
        "corr_max": float(upper.max()),
        "corr_range": float(upper.max() - upper.min()),
        "loadings": pd.Series(pca.components_[0], index=candidate),
    }


def split_window(end_date: date, window_days: int) -> tuple[str, str, str]:
    start = end_date - timedelta(days=window_days)
    mid = end_date - timedelta(days=window_days // 2)
    return start.isoformat(), mid.isoformat(), end_date.isoformat()


def plot_holdout(
    train_d: dict, test_d: dict, candidate: list[str], out: Path, title: str,
) -> None:
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))

    labels = ["Intra-corr", "PC1 variance"]
    train_vals = [train_d["intra"], train_d["pc1"]]
    test_vals = [test_d["intra"], test_d["pc1"]]
    x = np.arange(len(labels))
    w = 0.35
    axes[0].bar(x - w / 2, train_vals, w, color="#999999", label="Train (older half)")
    axes[0].bar(x + w / 2, test_vals, w, color="#2962FF", label="Test (newer half)")
    axes[0].set_xticks(x)
    axes[0].set_xticklabels(labels)
    axes[0].set_ylim(0, 1)
    axes[0].set_ylabel("Value")
    axes[0].set_title("Train vs test diagnostics")
    axes[0].legend(fontsize=9)
    for i, (tr, te) in enumerate(zip(train_vals, test_vals)):
        axes[0].text(i - w / 2, tr + 0.01, f"{tr:.3f}", ha="center", fontsize=8)
        axes[0].text(i + w / 2, te + 0.01, f"{te:.3f}", ha="center", fontsize=8)

    axes[1].bar(x - w / 2, [train_d["corr_min"], train_d["corr_max"]], w, color="#999999", label="Train")
    axes[1].bar(x + w / 2, [test_d["corr_min"], test_d["corr_max"]], w, color="#2962FF", label="Test")
    axes[1].set_xticks(x)
    axes[1].set_xticklabels(["Min pairwise", "Max pairwise"])
    axes[1].set_ylabel("Correlation")
    axes[1].set_ylim(0, 1)
    axes[1].set_title("Pairwise-corr range")
    axes[1].legend(fontsize=9)

    if "loadings" in train_d and "loadings" in test_d:
        idx = np.arange(len(candidate))
        axes[2].bar(idx - w / 2, train_d["loadings"].values, w, color="#999999", label="Train")
        axes[2].bar(idx + w / 2, test_d["loadings"].values, w, color="#2962FF", label="Test")
        axes[2].set_xticks(idx)
        axes[2].set_xticklabels(candidate, rotation=45, ha="right", fontsize=8)
        axes[2].set_ylabel("PC1 loading")
        axes[2].axhline(0, color="black", linewidth=0.5)
        axes[2].set_title("PC1 loadings (sign + magnitude)")
        axes[2].legend(fontsize=9)

    fig.suptitle(title, fontsize=11)
    fig.tight_layout()
    fig.savefig(out, dpi=140, bbox_inches="tight")
    plt.close(fig)


def stability_verdict(train_intra: float, test_intra: float) -> str:
    if np.isnan(train_intra) or np.isnan(test_intra) or train_intra <= 0:
        return "INDETERMINATE — insufficient data"
    ratio = test_intra / train_intra
    if ratio >= 1.10:
        return f"STRENGTHENING — test/train ratio {ratio:.2f} (basket consolidating; check for regime shift in the train half)"
    if ratio >= 0.85:
        return f"STABLE — test/train ratio {ratio:.2f} (durable cluster across regimes)"
    if ratio >= 0.60:
        return f"WEAKENED — test/train ratio {ratio:.2f} (factor present but eroding)"
    return f"REGIME-DEPENDENT — test/train ratio {ratio:.2f} (cluster does not survive holdout)"


def loading_stability(train_loadings: pd.Series, test_loadings: pd.Series) -> float:
    """Correlation of PC1 loadings across halves, sign-aligned.

    PCA component signs are arbitrary per fit, so without alignment a perfect
    factor match can read as -1.0. Test loadings are flipped when their dot
    product with the train loadings is negative (2026-06-09 audit, item 7)."""
    if train_loadings.std() == 0 or test_loadings.std() == 0:
        return float("nan")
    if float(np.dot(train_loadings, test_loadings)) < 0:
        test_loadings = -test_loadings
    return float(train_loadings.corr(test_loadings))


def write_summary(
    cfg: dict, candidate: list[str], window: str,
    train_d: dict, test_d: dict,
    train_window: tuple, test_window: tuple, out: Path,
) -> None:
    lines = []
    lines.append(f"{cfg.get('name', cfg['prefix'])} HOLDOUT TEST")
    lines.append(f"Cohort: {', '.join(candidate)} (N={len(candidate)})")
    lines.append(f"Window: {window}, split temporally at midpoint")
    lines.append(f"Train: {train_window[0]} -> {train_window[1]} ({train_d['n_obs']} obs)")
    lines.append(f"Test:  {test_window[0]} -> {test_window[1]} ({test_d['n_obs']} obs)")
    lines.append("")

    lines.append("--- TRAIN HALF (older) ---")
    lines.append(f"Intra-correlation:    {train_d['intra']:.4f}")
    lines.append(f"PC1 explained var:    {train_d['pc1']*100:.2f}%")
    lines.append(f"Pairwise range:       [{train_d['corr_min']:.3f}, {train_d['corr_max']:.3f}]")
    lines.append("")

    lines.append("--- TEST HALF (newer) ---")
    lines.append(f"Intra-correlation:    {test_d['intra']:.4f}")
    lines.append(f"PC1 explained var:    {test_d['pc1']*100:.2f}%")
    lines.append(f"Pairwise range:       [{test_d['corr_min']:.3f}, {test_d['corr_max']:.3f}]")
    lines.append("")

    lines.append("--- STABILITY DIAGNOSTICS ---")
    intra_delta = test_d["intra"] - train_d["intra"]
    pc1_delta = test_d["pc1"] - train_d["pc1"]
    lines.append(f"Intra-corr delta:     {intra_delta:+.4f}   (test - train)")
    lines.append(f"PC1 variance delta:   {pc1_delta*100:+.2f}pp")
    if "loadings" in train_d and "loadings" in test_d:
        loadings_corr = loading_stability(train_d["loadings"], test_d["loadings"])
        lines.append(f"PC1 loadings corr:    {loadings_corr:.4f}    (1.0 = identical factor structure)")
    lines.append("")
    lines.append(f"VERDICT: {stability_verdict(train_d['intra'], test_d['intra'])}")

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
    days = WINDOW_DAYS[args.window]
    start, mid, end = split_window(end_date, days)

    rets_full = load_returns({"cluster": cfg["groups"]["cluster"]}, start, end)
    rets_full = rets_full.dropna(thresh=int(0.95 * len(rets_full.columns)))
    candidate = [t for t in cfg["groups"]["cluster"]["tickers"] if t in rets_full.columns]

    train_rets = rets_full[rets_full.index < mid]
    test_rets = rets_full[rets_full.index >= mid]

    train_d = diagnostics(train_rets, candidate)
    test_d = diagnostics(test_rets, candidate)

    prefix = cfg["prefix"]
    plot_holdout(
        train_d, test_d, candidate,
        ATT / f"{prefix}-holdout.png",
        f"{cfg.get('name', prefix)} — holdout ({args.window} split at {mid})",
    )
    write_summary(
        cfg, candidate, args.window, train_d, test_d,
        (start, mid), (mid, end),
        ATT / f"{prefix}-holdout.txt",
    )

    try:
        from cluster_registry import append_record
        append_record({
            "test_date": str(date.today()),
            "primary": cfg.get("primary", ""),
            "cohort_name": cfg.get("name", cfg["prefix"]),
            "n_members": len(candidate),
            "holdout_window": args.window,
            "train_intra": round(train_d["intra"], 4),
            "test_intra": round(test_d["intra"], 4),
            "train_pc1_pct": round(train_d["pc1"] * 100, 2),
            "test_pc1_pct": round(test_d["pc1"] * 100, 2),
            "stability_ratio": round(test_d["intra"] / train_d["intra"], 4) if train_d["intra"] > 0 else None,
        })
    except Exception as e:
        print(f"(registry append skipped: {e})")


if __name__ == "__main__":
    main()
