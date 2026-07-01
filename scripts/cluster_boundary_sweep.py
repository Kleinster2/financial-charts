"""Full-universe boundary sweep for cluster validation.

Closes audit finding 3 (docs/cluster-validation-audit-2026-06-09.md): the
dendrogram boundary test and the threshold scan only see the tickers listed
in the YAML config, so "the cohort isolates as a clean cluster" was always
config-relative — a cohort could be inseparable from 50 names nobody put in
the config and still scan "intact, no contamination". This sweep asks the
market-relative question: of ALL names in the cleaned US-common-stock
universe (the same pool the random-basket null draws from), which would join
the candidate cohort below the dendrogram cut?

Method (average-linkage semantics, matching cluster_analysis):
  For each pool name x outside the config, the average-linkage distance from
  x to the cohort C is mean over members m of (1 - |corr(x, m)|) — exactly
  the join distance x would have if added singly to the candidate list and
  the dendrogram re-run. This automates the manual procedure documented in
  docs/cluster-validation.md ("add it to the candidate list, re-run, check
  whether the dendrogram includes it below the threshold") for every pool
  name at once. Two reference points:

    threshold   the config's dendrogram cut. An outsider at or below it
                would be merged into the cohort's flat cluster at the cut.
    envelope    the candidate cohort's own final internal merge distance.
                An outsider strictly inside it is closer to the cohort than
                the cohort's loosest member.

Verdicts (outsiders only — config control groups are known neighbors and are
reported separately as calibration rows, never as contamination):

  BOUNDARY-CLEAN         no outsider at or below the threshold
  BOUNDARY-PERMEABLE     outsider(s) at or below the threshold but outside
                         the internal envelope: the cut-level cluster would
                         include them; the separability claim weakens
  BOUNDARY-CONTAMINATED  outsider(s) strictly inside the internal envelope:
                         the config boundary is wrong — a missing member or
                         a false cohort

Each outsider also carries its correlation to the cohort's standardized PC1
factor score — the "would this name load on the cluster factor" view.

Non-US cohorts: the pool is US-synchronous, so daily cross-correlations to a
foreign-listed cohort are async-depressed and every join distance is
overstated (outsiders look farther than they are). The sweep prints a loud
caveat and should be read as approximate; lean on same-market controls.

Usage:
  python scripts/cluster_boundary_sweep.py --primary RKLB
  python scripts/cluster_boundary_sweep.py --config scripts/cluster_configs/wfe_quartet.yaml
  python scripts/cluster_boundary_sweep.py --primary RKLB --top 40
  python scripts/cluster_boundary_sweep.py --primary RKLB --universe-file scripts/universes/us_common_stocks.txt

Outputs (in investing/attachments/):
  {prefix}-boundary-sweep.txt    ranked outsider table + calibration rows + verdict
  {prefix}-boundary-sweep.png    top-N join distances vs threshold + envelope

Registry: appends boundary_verdict, boundary_n_below_threshold,
boundary_n_inside_envelope, boundary_nearest_outsiders, boundary_pool_size
to scripts/cluster_registry.csv.
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
    candidate_join_distances,
    latest_weekday,
    load_returns,
    resolve_config,
)
from cluster_permutation_test import (
    default_universe_from_db,
    is_us_common_stock_ticker,
    load_universe_file,
    load_universe_returns,
)


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    p.add_argument("--config", type=Path)
    p.add_argument("--primary")
    p.add_argument("--prefix")
    p.add_argument("--threshold", type=float)
    p.add_argument("--top", type=int, default=25, help="Rows in the ranked outsider table (default 25)")
    p.add_argument("--universe-file", type=Path, help="Universe file (one ticker per line); default: cleaned stock pool from DB")
    return p.parse_args()


def pc1_factor_series(rets: pd.DataFrame, candidate: list[str]) -> pd.Series:
    """Standardized-PC1 factor score series for the candidate cohort.
    Sign-fixed so the mean loading is positive (PCA signs are arbitrary per fit)."""
    sub = rets[candidate].dropna()
    stds = sub.std()
    zero_vol = stds[stds == 0].index.tolist()
    if zero_vol:
        raise SystemExit(
            f"PC1 factor aborted: zero-variance return series in window for {', '.join(zero_vol)}"
        )
    standardized = (sub - sub.mean()) / stds
    pca = PCA(n_components=1)
    pca.fit(standardized)
    w = pd.Series(pca.components_[0], index=candidate)
    if w.mean() < 0:
        w = -w
    return standardized @ w


def boundary_distances(rets: pd.DataFrame, candidate: list[str], others: list[str]) -> pd.DataFrame:
    """Average-linkage join distance from each `others` name to the cohort.

    join_dist_avg = 1 - mean(|corr(x, member)|) is the average-linkage
    distance between singleton x and the cohort — the height at which x
    would join the candidate-only dendrogram if added to the list alone.
    join_dist_min = 1 - max(|corr|) is the single-linkage view (nearest
    member), reported for interpretation only.
    """
    others = [t for t in others if t in rets.columns]
    corrs = pd.DataFrame(index=others, columns=candidate, dtype=float)
    for m in candidate:
        corrs[m] = rets[others].corrwith(rets[m])
    abs_corr = corrs.abs()
    valid = abs_corr.dropna(how="all")
    out = pd.DataFrame(
        {
            "avg_abs_corr": valid.mean(axis=1),
            "join_dist_avg": 1 - valid.mean(axis=1),
            "join_dist_min": 1 - valid.max(axis=1),
            "nearest_member": valid.idxmax(axis=1),
        }
    )
    return out.sort_values("join_dist_avg")


def internal_envelope(rets: pd.DataFrame, candidate: list[str]) -> float:
    """The candidate cohort's final internal merge distance (its loosest
    member's join height). NaN for cohorts with fewer than 2 usable names."""
    sub = rets[candidate].dropna()
    if len(candidate) < 2 or sub.empty:
        return float("nan")
    joins = candidate_join_distances(sub.corr(), candidate)
    if joins.empty:
        return float("nan")
    return float(joins["Distance"].iloc[-1])


def classify_boundary(outsider_dist: pd.Series, threshold: float, envelope: float) -> tuple[str, int, int]:
    """Verdict from outsider join distances. Threshold uses <= (fcluster's
    criterion="distance" merges at cophenetic distance <= t); the envelope
    uses strict < ("closer than the loosest member")."""
    below = int((outsider_dist <= threshold).sum())
    inside = 0 if np.isnan(envelope) else int((outsider_dist < envelope).sum())
    if inside > 0:
        return "BOUNDARY-CONTAMINATED", below, inside
    if below > 0:
        return "BOUNDARY-PERMEABLE", below, inside
    return "BOUNDARY-CLEAN", below, inside


def plot_boundary(
    dist_df: pd.DataFrame, group_of: dict[str, str], threshold: float, envelope: float,
    out: Path, title: str, top: int = 25,
) -> None:
    shown = dist_df.head(top).iloc[::-1]  # closest at the top of the barh
    colors = ["#616161" if group_of.get(t) is None else "#7E57C2" for t in shown.index]
    fig, ax = plt.subplots(figsize=(9, max(5, 0.32 * len(shown))))
    ax.barh(range(len(shown)), shown["join_dist_avg"].values, color=colors, alpha=0.85)
    ax.set_yticks(range(len(shown)))
    labels = [
        t if group_of.get(t) is None else f"{t} [{group_of[t]}]"
        for t in shown.index
    ]
    ax.set_yticklabels(labels, fontsize=8)
    ax.axvline(threshold, color="#D32F2F", linestyle="--", linewidth=1.2, label=f"threshold = {threshold}")
    if not np.isnan(envelope):
        ax.axvline(envelope, color="#2962FF", linestyle="--", linewidth=1.2, label=f"cohort envelope = {envelope:.3f}")
    ax.set_xlabel("Average-linkage join distance to cohort (1 - mean |corr|)")
    ax.set_title(title, fontsize=10, pad=10)
    ax.legend(fontsize=8, loc="lower right")
    fig.tight_layout()
    fig.savefig(out, dpi=140, bbox_inches="tight")
    plt.close(fig)


def _fmt_row(t: str, r: pd.Series, factor_corr: float, threshold: float, envelope: float, tag: str) -> str:
    flags = []
    if not np.isnan(envelope) and r["join_dist_avg"] < envelope:
        flags.append("INSIDE ENVELOPE")
    elif r["join_dist_avg"] <= threshold:
        flags.append("below cut")
    flag = ("  << " + ", ".join(flags)) if flags else ""
    fc = f"{factor_corr:+.3f}" if not np.isnan(factor_corr) else "   na"
    return (
        f"  {t:<8} {tag:<14} d_avg {r['join_dist_avg']:.3f}  d_min {r['join_dist_min']:.3f} "
        f"(nearest {r['nearest_member']:<6})  PC1-corr {fc}{flag}"
    )


def main() -> None:
    args = parse_args()
    cfg = resolve_config(args)
    if "cluster" not in cfg["groups"]:
        raise SystemExit("Config must define a 'cluster' group")
    threshold = cfg["threshold"]

    window_end = cfg.get("window_end") or latest_weekday()
    if isinstance(window_end, date):
        window_end = window_end.isoformat()
    end_date = date.fromisoformat(window_end)
    start_1y = (end_date - timedelta(days=365)).isoformat()

    # Cohort + config controls (controls are calibration rows, not outsiders).
    config_rets = load_returns(cfg["groups"], start_1y, window_end)
    config_rets = config_rets.dropna(thresh=int(0.95 * len(config_rets.columns)))
    configured = cfg["groups"]["cluster"]["tickers"]
    candidate = [t for t in configured if t in config_rets.columns]
    missing = [t for t in configured if t not in candidate]
    if missing:
        print(
            f"WARNING: {len(missing)} cluster ticker(s) have no usable data in the window "
            f"and are EXCLUDED: {', '.join(missing)}. Sweeping against {len(candidate)} of "
            f"{len(configured)} configured names."
        )
    if len(candidate) < 2:
        print("NOTE: fewer than 2 usable cohort names — envelope undefined, sweep runs threshold-only.")

    all_config_tickers = {t for grp in cfg["groups"].values() for t in grp["tickers"]}
    group_of = {
        t: grp for grp, spec in cfg["groups"].items() if grp != "cluster" for t in spec["tickers"]
    }

    foreign = [t for t in candidate if not is_us_common_stock_ticker(t)]
    if foreign:
        print(
            f"CAVEAT: cohort has non-US listings ({', '.join(foreign)}). The pool is "
            "US-synchronous, so every join distance to the cohort is async-depressed "
            "(overstated). Read the sweep as approximate; lean on same-market controls."
        )

    # Universe pool = cleaned stock universe minus every config ticker.
    if args.universe_file:
        universe = load_universe_file(args.universe_file)
        universe_source = f"file: {args.universe_file}"
    else:
        universe = default_universe_from_db(start_1y, window_end)
        universe_source = "DB prices_long, stock/equity-typed, US-listed"
    pool = [t for t in universe if t not in all_config_tickers]
    min_obs = int(0.8 * len(config_rets))
    universe_rets = load_universe_returns(pool, start_1y, window_end, min_obs)
    pool_size = len(universe_rets.columns)
    if pool_size == 0:
        raise SystemExit("Universe pool is empty after filters — check the DB or --universe-file.")
    print(f"Sweeping {pool_size} pool names from {universe_source} against {len(candidate)}-name cohort...")

    rets_all = pd.concat([config_rets, universe_rets], axis=1)
    rets_all = rets_all.loc[:, ~rets_all.columns.duplicated()]

    outsiders = boundary_distances(rets_all, candidate, list(universe_rets.columns))
    controls = boundary_distances(rets_all, candidate, [t for t in group_of if t in rets_all.columns])
    envelope = internal_envelope(config_rets, candidate)
    verdict, n_below, n_inside = classify_boundary(outsiders["join_dist_avg"], threshold, envelope)

    factor = pc1_factor_series(config_rets, candidate)
    factor_corr_out = rets_all[list(outsiders.index)].corrwith(factor)
    factor_corr_ctl = rets_all[list(controls.index)].corrwith(factor) if not controls.empty else pd.Series(dtype=float)

    prefix = cfg["prefix"]
    name = cfg.get("name", prefix)

    # Text artifact
    lines = []
    lines.append(f"{name} FULL-UNIVERSE BOUNDARY SWEEP")
    lines.append(f"Window: {rets_all.index.min().date()} -> {rets_all.index.max().date()}")
    lines.append(f"Cohort (N={len(candidate)}): {', '.join(candidate)}")
    if missing:
        lines.append(f"WARNING — configured but EXCLUDED (no usable data in window): {', '.join(missing)}")
    if foreign:
        lines.append(
            f"CAVEAT — non-US cohort listings ({', '.join(foreign)}): US-synchronous pool, join "
            "distances async-depressed (overstated); sweep is approximate."
        )
    lines.append(f"Pool: {pool_size} names ({universe_source}); every config ticker excluded from outsider set")
    lines.append(f"Dendrogram threshold: {threshold}")
    lines.append(
        f"Cohort internal envelope (final internal merge): "
        + (f"{envelope:.3f}" if not np.isnan(envelope) else "undefined (single-name candidate)")
    )
    lines.append("")
    lines.append(f"VERDICT: {verdict}")
    lines.append(f"  Outsiders at or below threshold {threshold}: {n_below}")
    lines.append(f"  Outsiders strictly inside the envelope:  {n_inside}")
    lines.append("")
    lines.append(f"--- NEAREST {min(args.top, len(outsiders))} OUTSIDERS (of {pool_size}) ---")
    for t, r in outsiders.head(args.top).iterrows():
        lines.append(_fmt_row(t, r, float(factor_corr_out.get(t, np.nan)), threshold, envelope, "outsider"))
    if not controls.empty:
        lines.append("")
        lines.append("--- CONFIG CONTROL GROUPS (calibration — known neighbors, never contamination) ---")
        for t, r in controls.iterrows():
            tag = group_of.get(t, "control")
            lines.append(_fmt_row(t, r, float(factor_corr_ctl.get(t, np.nan)), threshold, envelope, tag))
    lines.append("")
    lines.append("--- INTERPRETATION ---")
    if verdict == "BOUNDARY-CLEAN":
        lines.append(
            "No name outside the config would join the cohort at the cut: the boundary is "
            "market-relative, not just config-relative. The threshold scan's isolation result "
            "holds against the full universe."
        )
    elif verdict == "BOUNDARY-PERMEABLE":
        lines.append(
            f"{n_below} outside name(s) would merge into the cohort's flat cluster at the cut. "
            "The cohort is real but its cut-level boundary is permeable: either these names belong "
            "in the cohort (re-run the validation with them added) or the separability claim should "
            "be stated at a tighter threshold."
        )
    else:
        lines.append(
            f"{n_inside} outside name(s) sit closer to the cohort than its own loosest member. "
            "The config boundary is wrong as drawn: treat each as a missing-member candidate "
            "(add to the cluster group and re-validate) or accept that the cohort is not a "
            "standalone factor."
        )

    txt_path = ATT / f"{prefix}-boundary-sweep.txt"
    txt_path.write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))

    # Chart: outsiders + controls interleaved by distance
    combined = pd.concat([outsiders, controls]).sort_values("join_dist_avg")
    plot_boundary(
        combined, group_of, threshold, envelope,
        ATT / f"{prefix}-boundary-sweep.png",
        f"{name} — full-universe boundary sweep ({pool_size}-name pool; controls tagged [group])",
        top=args.top,
    )
    print(f"\nArtifacts: {txt_path}")
    print(f"           {ATT / f'{prefix}-boundary-sweep.png'}")

    nearest = "; ".join(f"{t}:{r['join_dist_avg']:.3f}" for t, r in outsiders.head(3).iterrows())
    try:
        from cluster_registry import append_record
        append_record({
            "test_date": str(date.today()),
            "primary": cfg.get("primary", ""),
            "cohort_name": name,
            "n_members": len(candidate),
            "window_start": start_1y,
            "window_end": window_end,
            "boundary_verdict": verdict,
            "boundary_n_below_threshold": n_below,
            "boundary_n_inside_envelope": n_inside,
            "boundary_nearest_outsiders": nearest,
            "boundary_pool_size": pool_size,
        })
    except Exception as e:
        print(f"(registry append skipped: {e})")


if __name__ == "__main__":
    main()
