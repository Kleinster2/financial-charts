"""Cluster validation registry: log every cluster test + apply multiple-testing correction.

Every run of cluster_permutation_test.py, cluster_holdout_test.py, and
cluster_threshold_scan.py appends a row to scripts/cluster_registry.csv. The
registry is the cross-cohort log of every diagnostic ever computed against the
vault's cluster-validation framework.

The append step from the test scripts is best-effort and silently skipped on
error, so the analysis tools work standalone. When the registry is available,
it accumulates a single source of truth across runs.

Subcommands:
  list                  Show all registry entries (newest first)
  append-manual         Append a row from CLI args (rarely needed; tests auto-append)
  correction            Apply Bonferroni + Benjamini-Hochberg correction to the
                        p-values in the active registry. Reports which clusters
                        survive each correction at alpha=0.05.
  summary               One-line-per-cohort summary across all logged tests.

Usage:
  python scripts/cluster_registry.py list
  python scripts/cluster_registry.py correction --alpha 0.05
  python scripts/cluster_registry.py summary
"""

from __future__ import annotations

import argparse
import csv
from datetime import date
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
REGISTRY = Path(__file__).resolve().parent / "cluster_registry.csv"

COLUMNS = [
    "test_date",
    "primary",
    "cohort_name",
    "n_members",
    "window_start",
    "window_end",
    "intra_corr_1y",
    "pc1_variance_pct",
    "p_independence_intra",
    "p_random_basket_intra",
    "p_random_basket_pc1",
    "n_permutations",
    "holdout_window",
    "train_intra",
    "test_intra",
    "train_pc1_pct",
    "test_pc1_pct",
    "stability_ratio",
    "threshold_stable_width",
    "threshold_stable_ranges",
]


def append_record(record: dict) -> None:
    """Append-or-merge a record to the registry.
    Rows are keyed by (test_date, cohort_name). If a matching row exists, this
    call overwrites only the columns present in `record`, preserving earlier
    diagnostics on the same row. New diagnostics on the same day land together
    in one row instead of producing N partial rows."""
    existing = []
    if REGISTRY.exists():
        with REGISTRY.open("r", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            existing = list(reader)

    key = (str(record.get("test_date", "")), str(record.get("cohort_name", "")))
    merged_existing = []
    matched = False
    for prev in existing:
        prev_key = (prev.get("test_date", ""), prev.get("cohort_name", ""))
        if prev_key == key:
            matched = True
            row = {col: prev.get(col, "") for col in COLUMNS}
            for k, v in record.items():
                if v is None or v == "":
                    continue
                row[k] = v
            merged_existing.append(row)
        else:
            merged_existing.append({col: prev.get(col, "") for col in COLUMNS})

    if not matched:
        merged_existing.append({col: record.get(col, "") for col in COLUMNS})

    with REGISTRY.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=COLUMNS)
        writer.writeheader()
        for row in merged_existing:
            writer.writerow(row)


def load_registry() -> pd.DataFrame:
    if not REGISTRY.exists():
        return pd.DataFrame(columns=COLUMNS)
    df = pd.read_csv(REGISTRY, dtype=str)
    for col in COLUMNS:
        if col not in df.columns:
            df[col] = ""
    numeric_cols = [
        "n_members", "intra_corr_1y", "pc1_variance_pct",
        "p_independence_intra", "p_random_basket_intra", "p_random_basket_pc1",
        "n_permutations", "train_intra", "test_intra", "train_pc1_pct",
        "test_pc1_pct", "stability_ratio", "threshold_stable_width",
    ]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    return df


def cmd_list(args: argparse.Namespace) -> None:
    df = load_registry()
    if df.empty:
        print("Registry empty.")
        return
    df = df.sort_values("test_date", ascending=False)
    cols = ["test_date", "primary", "cohort_name", "n_members", "intra_corr_1y",
            "pc1_variance_pct", "p_random_basket_intra", "stability_ratio",
            "threshold_stable_width"]
    print(df[cols].to_string(index=False))


def cmd_summary(args: argparse.Namespace) -> None:
    df = load_registry()
    if df.empty:
        print("Registry empty.")
        return
    df = df.sort_values("test_date")
    grouped = df.groupby("cohort_name").agg(
        primary=("primary", "last"),
        n_members=("n_members", "last"),
        last_test=("test_date", "max"),
        intra_corr=("intra_corr_1y", "last"),
        pc1_pct=("pc1_variance_pct", "last"),
        p_rb_intra=("p_random_basket_intra", "min"),
        stability=("stability_ratio", "last"),
        thresh_width=("threshold_stable_width", "last"),
    ).reset_index()
    print(grouped.to_string(index=False))


def bonferroni_threshold(alpha: float, n_tests: int) -> float:
    return alpha / max(n_tests, 1)


def benjamini_hochberg_threshold(p_values: list[float], alpha: float) -> tuple[float, list[bool]]:
    arr = np.array([p for p in p_values if not np.isnan(p)])
    if len(arr) == 0:
        return float("nan"), []
    n = len(arr)
    order = np.argsort(arr)
    sorted_p = arr[order]
    bh_line = np.arange(1, n + 1) * alpha / n
    below = sorted_p <= bh_line
    if not below.any():
        threshold = 0.0
    else:
        k = np.where(below)[0].max()
        threshold = sorted_p[k]
    reject = arr <= threshold
    full = []
    arr_idx = 0
    for p in p_values:
        if np.isnan(p):
            full.append(False)
        else:
            full.append(bool(reject[arr_idx]))
            arr_idx += 1
    return float(threshold), full


def cmd_correction(args: argparse.Namespace) -> None:
    df = load_registry()
    if df.empty:
        print("Registry empty — nothing to correct.")
        return

    df = df.sort_values("test_date").drop_duplicates(subset=["cohort_name"], keep="last")
    df = df.dropna(subset=["p_random_basket_intra"])

    if df.empty:
        print("No random-basket p-values in registry (run cluster_permutation_test.py with --null random-basket first).")
        return

    p_values = df["p_random_basket_intra"].tolist()
    n_tests = len(p_values)
    alpha = args.alpha

    bonf_threshold = bonferroni_threshold(alpha, n_tests)
    bh_threshold, bh_reject = benjamini_hochberg_threshold(p_values, alpha)

    df = df.copy()
    df["bonferroni_pass"] = df["p_random_basket_intra"] <= bonf_threshold
    df["bh_pass"] = bh_reject
    df["uncorrected_pass"] = df["p_random_basket_intra"] <= alpha

    print(f"Multiple-testing correction over {n_tests} unique cohorts in registry")
    print(f"Alpha: {alpha}")
    print(f"Bonferroni threshold: {bonf_threshold:.6f}  (alpha / N tests)")
    print(f"Benjamini-Hochberg threshold: {bh_threshold:.6f}  (FDR control at alpha)")
    print()

    cols = ["cohort_name", "p_random_basket_intra", "uncorrected_pass", "bonferroni_pass", "bh_pass"]
    print(df[cols].sort_values("p_random_basket_intra").to_string(index=False))
    print()

    uncorrected_n = int(df["uncorrected_pass"].sum())
    bonf_n = int(df["bonferroni_pass"].sum())
    bh_n = int(df["bh_pass"].sum())
    print(f"Pass uncorrected (p < {alpha}):       {uncorrected_n} / {n_tests}")
    print(f"Pass Bonferroni:                    {bonf_n} / {n_tests}")
    print(f"Pass Benjamini-Hochberg (FDR):      {bh_n} / {n_tests}")
    if uncorrected_n > bh_n:
        expected_false = max(0, uncorrected_n - bh_n)
        print(f"\n~{expected_false} of the uncorrected passes are likely false discoveries after FDR control.")


def cmd_append_manual(args: argparse.Namespace) -> None:
    record = {
        "test_date": args.test_date or str(date.today()),
        "primary": args.primary or "",
        "cohort_name": args.cohort_name,
        "n_members": args.n_members,
        "intra_corr_1y": args.intra_corr,
        "pc1_variance_pct": args.pc1_pct,
        "p_random_basket_intra": args.p_random_basket,
    }
    append_record(record)
    print(f"Appended: {record}")


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    sub = p.add_subparsers(dest="cmd", required=True)

    sub.add_parser("list", help="Show all registry entries")
    sub.add_parser("summary", help="One-row-per-cohort summary")

    c = sub.add_parser("correction", help="Multiple-testing correction across logged cohorts")
    c.add_argument("--alpha", type=float, default=0.05)

    m = sub.add_parser("append-manual", help="Manually append a record")
    m.add_argument("--test-date")
    m.add_argument("--primary")
    m.add_argument("--cohort-name", required=True)
    m.add_argument("--n-members", type=int, required=True)
    m.add_argument("--intra-corr", type=float, required=True)
    m.add_argument("--pc1-pct", type=float)
    m.add_argument("--p-random-basket", type=float)

    return p.parse_args()


def main() -> None:
    args = parse_args()
    if args.cmd == "list":
        cmd_list(args)
    elif args.cmd == "summary":
        cmd_summary(args)
    elif args.cmd == "correction":
        cmd_correction(args)
    elif args.cmd == "append-manual":
        cmd_append_manual(args)


if __name__ == "__main__":
    main()
