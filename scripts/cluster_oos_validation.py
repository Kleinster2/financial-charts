"""Post-definition out-of-sample re-validation for cluster cohorts.

Closes the discovery-bias hole identified in docs/cluster-validation-audit-2026-06-09.md
(Tier 3, finding 8): permutation, holdout, and threshold-scan all interrogate the
window in which a cohort was noticed — none can catch selection-on-the-dependent-
variable. This pass validates each cohort on returns strictly AFTER its definition
date, data nobody peeked at when drawing the boundary.

Definition date per cohort = the date its YAML config was first committed to git
(override with a `definition_date:` key in the config). The first OOS return lands
on the first trading day after that date.

Per cohort, on the post-definition window:
  - OOS intra-correlation and standardized PC1 explained variance
  - Ratio of OOS intra-corr to the in-sample baseline (1Y window ending at the
    definition date, recomputed fresh)
  - Random-basket p-value against the cleaned stock-only null on the SAME OOS
    window (null baskets face the same short window, so validity holds at any
    length — only power is limited)

Verdict bands (ratio = OOS intra / in-sample intra):
  >= 1.10  OOS-STRENGTHENING     0.60-0.85  OOS-WEAKENED
  0.85-1.10 OOS-CONFIRMED        < 0.60     OOS-FAILED
  < --min-obs OOS returns        INSUFFICIENT_HISTORY (definition date still logged)
  < 40 OOS returns               verdict prefixed PRELIMINARY (low power)

Results append to scripts/cluster_registry.csv (merging into today's row per
cohort) and a consolidated table lands in investing/attachments/.

Cadence: run quarterly alongside `cluster_registry.py correction`. Cohorts stay
PRELIMINARY until they accumulate ~2 months of post-definition history.

Usage:
  python scripts/cluster_oos_validation.py --all
  python scripts/cluster_oos_validation.py --primary RKLB
  python scripts/cluster_oos_validation.py --config scripts/cluster_configs/rklb.yaml --n-perm 20000
"""

from __future__ import annotations

import argparse
import subprocess
from datetime import date, timedelta
from pathlib import Path

import numpy as np
import yaml

from cluster_analysis import ATT, CONFIG_DIR, ROOT, latest_weekday, load_returns
from cluster_permutation_test import (
    default_universe_from_db,
    intra_correlation,
    load_universe_returns,
    pc1_explained_variance,
    run_random_basket_null,
)

PRELIMINARY_OBS = 40


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    p.add_argument("--all", action="store_true", help="Run every config in scripts/cluster_configs/")
    p.add_argument("--config", type=Path)
    p.add_argument("--primary")
    p.add_argument("--n-perm", type=int, default=10000)
    p.add_argument("--min-obs", type=int, default=15, help="Minimum OOS return obs to grade at all (default 15)")
    p.add_argument("--seed", type=int, default=42)
    return p.parse_args()


def config_definition_date(path: Path, cfg: dict) -> str | None:
    """YAML `definition_date:` override wins; else first git add date of the config."""
    override = cfg.get("definition_date")
    if override:
        return override.isoformat() if isinstance(override, date) else str(override)
    rel = path.resolve().relative_to(ROOT).as_posix()
    out = subprocess.run(
        ["git", "-C", str(ROOT), "log", "--diff-filter=A", "--format=%aI", "--", rel],
        capture_output=True, text=True,
    )
    lines = [s for s in out.stdout.splitlines() if s.strip()]
    return lines[-1][:10] if lines else None


def p_right_tail(observed: float, null_dist: np.ndarray) -> float:
    if null_dist.size == 0 or np.isnan(observed):
        return float("nan")
    return float((1 + (null_dist >= observed).sum()) / (1 + null_dist.size))


def grade(ratio: float, oos_obs: int) -> str:
    if np.isnan(ratio):
        return "INDETERMINATE"
    if ratio >= 1.10:
        band = "OOS-STRENGTHENING"
    elif ratio >= 0.85:
        band = "OOS-CONFIRMED"
    elif ratio >= 0.60:
        band = "OOS-WEAKENED"
    else:
        band = "OOS-FAILED"
    return f"PRELIMINARY {band}" if oos_obs < PRELIMINARY_OBS else band


def validate_cohort(path: Path, n_perm: int, min_obs: int, seed: int) -> dict | None:
    with path.open("r", encoding="utf-8") as f:
        cfg = yaml.safe_load(f)
    if "cluster" not in cfg.get("groups", {}):
        print(f"SKIP {path.name}: no 'cluster' group")
        return None
    name = cfg.get("name", path.stem)
    tickers = cfg["groups"]["cluster"]["tickers"]

    def_date = config_definition_date(path, cfg)
    if not def_date:
        print(f"SKIP {path.name}: no definition date (uncommitted config without definition_date key)")
        return None

    end = latest_weekday()
    in_start = (date.fromisoformat(def_date) - timedelta(days=365)).isoformat()
    grp = {"cluster": cfg["groups"]["cluster"]}

    rets_in = load_returns(grp, in_start, def_date)
    rets_in = rets_in.dropna(thresh=int(0.95 * len(rets_in.columns))) if len(rets_in.columns) else rets_in
    rets_oos = load_returns(grp, def_date, end)
    rets_oos = rets_oos.dropna(thresh=int(0.95 * len(rets_oos.columns))) if len(rets_oos.columns) else rets_oos

    candidate = [t for t in tickers if t in rets_in.columns and t in rets_oos.columns]
    missing = [t for t in tickers if t not in candidate]
    if missing:
        print(f"WARNING {name}: ticker(s) missing from in-sample or OOS window, EXCLUDED: {', '.join(missing)}")
    if len(candidate) < 2:
        print(f"SKIP {path.name}: fewer than 2 usable tickers")
        return None

    in_intra = intra_correlation(rets_in, candidate)
    sub_oos = rets_oos[candidate].dropna()
    oos_obs = len(sub_oos)

    rec: dict = {
        "name": name,
        "primary": cfg.get("primary", ""),
        "n": len(candidate),
        "definition_date": def_date,
        "oos_end": end,
        "oos_obs": oos_obs,
        "in_intra": in_intra,
        "oos_start": str(sub_oos.index.min().date()) if oos_obs else "",
        "oos_intra": float("nan"),
        "oos_pc1": float("nan"),
        "ratio": float("nan"),
        "p_oos": float("nan"),
    }

    if oos_obs < min_obs:
        rec["verdict"] = f"INSUFFICIENT_HISTORY ({oos_obs} obs < {min_obs})"
        return rec

    rec["oos_intra"] = intra_correlation(rets_oos, candidate)
    rec["oos_pc1"] = pc1_explained_variance(rets_oos, candidate)
    rec["ratio"] = rec["oos_intra"] / in_intra if in_intra and in_intra > 0 else float("nan")

    sample_min = max(10, int(0.8 * oos_obs))
    universe = default_universe_from_db(def_date, end, min_obs=max(10, int(0.8 * (oos_obs + 1))))
    universe = [t for t in universe if t not in candidate]
    universe_rets = load_universe_returns(universe, def_date, end, min_obs=sample_min)
    print(f"{name}: OOS {rec['oos_start']} -> {end} ({oos_obs} obs), null pool {len(universe_rets.columns)} stocks")
    intra_null, _pc1_null = run_random_basket_null(
        universe_rets, len(candidate), n_perm, seed, min_obs=sample_min,
    )
    rec["p_oos"] = p_right_tail(rec["oos_intra"], intra_null)
    rec["verdict"] = grade(rec["ratio"], oos_obs)
    return rec


def write_outputs(records: list[dict], n_perm: int, out: Path) -> None:
    lines = []
    lines.append(f"POST-DEFINITION OUT-OF-SAMPLE RE-VALIDATION — {date.today().isoformat()}")
    lines.append(f"Null: random {'{N}'}-baskets from cleaned stock-only pool on each cohort's OOS window, {n_perm} draws, Phipson-Smyth p.")
    lines.append("Definition date = first git commit of the cohort's YAML config (data after it was never peeked at).")
    lines.append(f"Verdicts on ratio = OOS intra / in-sample intra; < {PRELIMINARY_OBS} obs = PRELIMINARY.")
    lines.append("")
    header = (
        f"{'Cohort':<42} {'N':>2} {'defined':>10} {'obs':>4} {'in-intra':>8} "
        f"{'oos-intra':>9} {'ratio':>6} {'oos-PC1':>8} {'p-oos':>7}  verdict"
    )
    lines.append(header)
    lines.append("-" * len(header))
    for r in sorted(records, key=lambda x: (x["verdict"], x["name"])):
        lines.append(
            f"{r['name'][:42]:<42} {r['n']:>2} {r['definition_date']:>10} {r['oos_obs']:>4} "
            f"{r['in_intra']:>8.3f} {r['oos_intra']:>9.3f} {r['ratio']:>6.2f} "
            f"{r['oos_pc1']*100 if not np.isnan(r['oos_pc1']) else float('nan'):>7.1f}% {r['p_oos']:>7.4f}  {r['verdict']}"
        )
    lines.append("")
    counts: dict[str, int] = {}
    for r in records:
        key = r["verdict"].replace("PRELIMINARY ", "")
        key = "INSUFFICIENT_HISTORY" if key.startswith("INSUFFICIENT") else key
        counts[key] = counts.get(key, 0) + 1
    lines.append("Verdict counts: " + ", ".join(f"{k} {v}" for k, v in sorted(counts.items())))
    out.write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))
    print(f"\nSaved: {out}")


def main() -> None:
    args = parse_args()
    if args.all:
        paths = sorted(CONFIG_DIR.glob("*.yaml"))
    elif args.config:
        paths = [args.config]
    elif args.primary:
        paths = [CONFIG_DIR / f"{args.primary.lower()}.yaml"]
    else:
        raise SystemExit("Provide --all, --config PATH, or --primary TICKER")

    records = []
    for path in paths:
        rec = validate_cohort(path, args.n_perm, args.min_obs, args.seed)
        if rec is None:
            continue
        records.append(rec)
        try:
            from cluster_registry import append_record
            append_record({
                "test_date": str(date.today()),
                "primary": rec["primary"],
                "cohort_name": rec["name"],
                "n_members": rec["n"],
                "definition_date": rec["definition_date"],
                "oos_start": rec["oos_start"],
                "oos_end": rec["oos_end"],
                "oos_obs": rec["oos_obs"],
                "oos_intra": round(rec["oos_intra"], 4) if not np.isnan(rec["oos_intra"]) else None,
                "oos_pc1_pct": round(rec["oos_pc1"] * 100, 2) if not np.isnan(rec["oos_pc1"]) else None,
                "oos_vs_insample_ratio": round(rec["ratio"], 4) if not np.isnan(rec["ratio"]) else None,
                "p_oos_random_basket": round(rec["p_oos"], 6) if not np.isnan(rec["p_oos"]) else None,
                "oos_verdict": rec["verdict"],
            })
        except Exception as e:
            print(f"(registry append skipped: {e})")

    if records:
        write_outputs(records, args.n_perm, ATT / f"cluster-oos-validation-{date.today().isoformat()}.txt")


if __name__ == "__main__":
    main()
