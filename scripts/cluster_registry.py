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
                        survive each correction at alpha=0.05, and audits each
                        row's permutation resolution (Phipson-Smyth floor
                        1/(n_perm+1)) against the current Bonferroni cutoff —
                        the cutoff tightens as the registry grows, so a row's
                        n_perm can silently stop resolving it (UNRESOLVABLE /
                        AT-RISK flags; floor-pinned UNRESOLVABLE rows are
                        indeterminate, not fails).
  summary               One-line-per-cohort summary across all logged tests.

Usage:
  python scripts/cluster_registry.py list
  python scripts/cluster_registry.py correction --alpha 0.05
  python scripts/cluster_registry.py summary
"""

from __future__ import annotations

import argparse
import csv
import sys
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
    "definition_date",
    "oos_start",
    "oos_end",
    "oos_obs",
    "oos_intra",
    "oos_pc1_pct",
    "oos_vs_insample_ratio",
    "p_oos_random_basket",
    "oos_verdict",
    "p_vol_matched_intra",
    "p_vol_matched_pc1",
    "boundary_verdict",
    "boundary_n_below_threshold",
    "boundary_n_inside_envelope",
    "boundary_nearest_outsiders",
    "boundary_pool_size",
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
        "oos_obs", "oos_intra", "oos_pc1_pct", "oos_vs_insample_ratio",
        "p_oos_random_basket", "p_vol_matched_intra", "p_vol_matched_pc1",
        "boundary_n_below_threshold", "boundary_n_inside_envelope",
        "boundary_pool_size",
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
        defined=("definition_date", "last"),
        oos_verdict=("oos_verdict", "last"),
    ).reset_index()
    print(grouped.to_string(index=False))


def latest_p_rows(df: pd.DataFrame) -> pd.DataFrame:
    """One row per cohort: the LATEST row that carries a random-basket p-value.
    Dropping NaN p's before the dedup matters — a newer partial-diagnostic row
    (boundary sweep, holdout-only, threshold-only re-run) must not eclipse the
    cohort's p-carrying row and silently remove it from the FDR set."""
    return (
        df.dropna(subset=["p_random_basket_intra"])
        .sort_values("test_date")
        .drop_duplicates(subset=["cohort_name"], keep="last")
    )


def bonferroni_threshold(alpha: float, n_tests: int) -> float:
    return alpha / max(n_tests, 1)


def perm_floor(n_perm: float) -> float:
    """Phipson-Smyth floor: smallest p-value n_perm permutations can report, 1/(n_perm+1)."""
    if n_perm is None or np.isnan(n_perm) or n_perm <= 0:
        return float("nan")
    return 1.0 / (float(n_perm) + 1.0)


def min_nperm_for_cutoff(cutoff: float) -> int:
    """Smallest n_perm whose Phipson-Smyth floor sits at or below `cutoff`:
    1/(n+1) <= cutoff  <=>  n >= 1/cutoff - 1."""
    if cutoff <= 0 or np.isnan(cutoff):
        return -1
    return max(1, int(np.ceil(1.0 / cutoff)) - 1)


def is_floor_pinned(p: float, n_perm: float, rtol: float = 1e-6) -> bool:
    """True when the reported p equals the Phipson-Smyth floor — the observed
    statistic beat every draw, so the p is a resolution artifact (the true p
    may be far smaller), not an evidence measurement."""
    floor = perm_floor(n_perm)
    if np.isnan(floor) or p is None or np.isnan(p):
        return False
    return bool(np.isclose(p, floor, rtol=rtol, atol=0.0))


def nperm_adequacy(
    df: pd.DataFrame, alpha: float, n_tests: int, near_factor: float = 10.0,
) -> pd.DataFrame:
    """Per-row permutation-resolution audit against the current Bonferroni cutoff.

    The registry grows over time, so a permutation count that resolved the
    Bonferroni cutoff when a row was written can stop resolving it later —
    the cutoff is alpha/N and tightens with every new cohort, while the row's
    floor 1/(n_perm+1) is fixed at run time. Statuses:

      UNRESOLVABLE  floor > cutoff AND resolution could plausibly decide the
                    verdict: the row is floor-pinned, or its p sits within
                    near_factor x cutoff (a k-of-few estimate whose confidence
                    interval straddles the cutoff). The row can never pass
                    Bonferroni at this n_perm; a floor-pinned one is
                    INDETERMINATE (resolution failure), not "fail" — re-run
                    at higher n_perm before treating it as rejected. Rows with
                    floor > cutoff but p far above it fail on evidence, not
                    resolution, and stay "ok".
      AT-RISK       floor-pinned and floor > cutoff/2: resolves today, but
                    becomes UNRESOLVABLE once the registry reaches
                    N ~= alpha/floor cohorts.
      ok            resolution is adequate for this row at the current N.

    Expects columns cohort_name, p_random_basket_intra, n_permutations.
    Returns the same rows plus floor / floor_pinned / unresolvable_at_n /
    nperm_status columns (all rows, so callers can filter or count).
    """
    cutoff = bonferroni_threshold(alpha, n_tests)
    out = df.copy()
    floors, pinned, unresolvable_at, status = [], [], [], []
    for _, row in out.iterrows():
        n_perm = row.get("n_permutations", float("nan"))
        p = row.get("p_random_basket_intra", float("nan"))
        floor = perm_floor(n_perm)
        pin = is_floor_pinned(p, n_perm)
        floors.append(floor)
        pinned.append(pin)
        if np.isnan(floor):
            unresolvable_at.append(float("nan"))
            status.append("NO-NPERM")
        else:
            unresolvable_at.append(alpha / floor)
            near_cutoff = (not np.isnan(p)) and p <= near_factor * cutoff
            if floor > cutoff and (pin or near_cutoff):
                status.append("UNRESOLVABLE" + (" (floor-pinned: INDETERMINATE, not fail)" if pin else ""))
            elif pin and floor > cutoff / 2.0:
                status.append("AT-RISK")
            else:
                status.append("ok")
    out["floor"] = floors
    out["floor_pinned"] = pinned
    out["unresolvable_at_n"] = unresolvable_at
    out["nperm_status"] = status
    return out


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

    df = latest_p_rows(df)

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

    # Permutation-resolution audit: the Bonferroni cutoff tightens as the
    # registry grows, while each row's Phipson-Smyth floor is fixed at run
    # time — so old n_perm choices can silently stop resolving the correction.
    adequacy = nperm_adequacy(df, alpha, n_tests)
    flagged = adequacy[adequacy["nperm_status"] != "ok"]
    min_nperm = min_nperm_for_cutoff(bonf_threshold)
    print(f"\n--- n_perm ADEQUACY (permutation resolution vs Bonferroni cutoff) ---")
    print(f"Bonferroni cutoff at N={n_tests}: {bonf_threshold:.6f} — a row's floor 1/(n_perm+1) must sit at or below it.")
    print(f"Minimum adequate n_perm at this N: {min_nperm:,}. The 10,000 standard resolves registries up to N={int(alpha * 10001)}.")
    if flagged.empty:
        print("All rows resolve the current cutoff; no floor-pinned row is within 2x of it.")
    else:
        print(f"FLAGGED ({len(flagged)}):")
        for _, r in flagged.sort_values("floor", ascending=False).iterrows():
            n_perm = r["n_permutations"]
            n_perm_s = f"{int(n_perm):,}" if not np.isnan(n_perm) else "?"
            floor_s = f"{r['floor']:.6f}" if not np.isnan(r["floor"]) else "nan"
            at_n = r["unresolvable_at_n"]
            at_n_s = f"; unresolvable once registry N >= {int(at_n)}" if not np.isnan(at_n) else ""
            print(
                f"  {r['cohort_name'][:40]:<40} n_perm {n_perm_s:>7}  floor {floor_s}  "
                f"p {r['p_random_basket_intra']:.6f}  {r['nperm_status']}{at_n_s}"
            )
        print(f"Re-run flagged cohorts with cluster_permutation_test.py --n-perm 10000 (or >= {min_nperm:,}).")


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
    # Registry cohort names include CJK (e.g. 中特估); force UTF-8 stdout so
    # `correction`/`list`/`summary` don't crash on the default Windows cp1252.
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
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
