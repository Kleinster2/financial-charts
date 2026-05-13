"""Batch driver: run cluster_permutation_test + cluster_threshold_scan + cluster_holdout_test
on every config in scripts/cluster_configs/ and accumulate results into the registry.

Tolerates per-cohort failures (skips and continues). Prints one line per config with status.
After all configs run, prints the multi-test correction.

Usage:
  python scripts/cluster_registry_populate.py
  python scripts/cluster_registry_populate.py --n-perm 1000   # faster
  python scripts/cluster_registry_populate.py --skip-holdout  # permutation + threshold only
"""

from __future__ import annotations

import argparse
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONFIG_DIR = Path(__file__).resolve().parent / "cluster_configs"


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser()
    p.add_argument("--n-perm", type=int, default=2000)
    p.add_argument("--skip-holdout", action="store_true")
    p.add_argument("--skip-permutation", action="store_true")
    p.add_argument("--skip-threshold", action="store_true")
    return p.parse_args()


def run_one(label: str, cmd: list[str]) -> tuple[bool, float]:
    t0 = time.time()
    result = subprocess.run(cmd, capture_output=True, text=True, cwd=ROOT)
    elapsed = time.time() - t0
    ok = result.returncode == 0
    if not ok:
        print(f"    {label} FAILED ({elapsed:.1f}s): {result.stderr.strip().splitlines()[-1] if result.stderr.strip() else 'no stderr'}")
    else:
        print(f"    {label} ok ({elapsed:.1f}s)")
    return ok, elapsed


def main() -> None:
    args = parse_args()
    configs = sorted(CONFIG_DIR.glob("*.yaml"))
    print(f"Found {len(configs)} configs in {CONFIG_DIR}")
    print()

    total_t0 = time.time()
    summary = []
    for i, cfg in enumerate(configs, start=1):
        print(f"[{i}/{len(configs)}] {cfg.name}")
        result = {"config": cfg.name, "permutation": None, "threshold": None, "holdout": None}

        if not args.skip_permutation:
            ok, _ = run_one("permutation",
                ["python", "scripts/cluster_permutation_test.py", "--config", str(cfg),
                 "--n-perm", str(args.n_perm), "--null", "random-basket"])
            result["permutation"] = ok

        if not args.skip_threshold:
            ok, _ = run_one("threshold-scan",
                ["python", "scripts/cluster_threshold_scan.py", "--config", str(cfg)])
            result["threshold"] = ok

        if not args.skip_holdout:
            ok, _ = run_one("holdout (2y)",
                ["python", "scripts/cluster_holdout_test.py", "--config", str(cfg), "--window", "2y"])
            result["holdout"] = ok

        summary.append(result)

    total = time.time() - total_t0
    print()
    print(f"Total elapsed: {total/60:.1f} min")
    print()
    print("--- per-config status ---")
    for r in summary:
        p = "ok" if r["permutation"] else ("skip" if r["permutation"] is None else "FAIL")
        t = "ok" if r["threshold"] else ("skip" if r["threshold"] is None else "FAIL")
        h = "ok" if r["holdout"] else ("skip" if r["holdout"] is None else "FAIL")
        print(f"  {r['config']:<35} perm={p:<4}  thresh={t:<4}  holdout={h}")

    print()
    print("Run `python scripts/cluster_registry.py correction --alpha 0.05` for the cross-cohort multi-test view.")


if __name__ == "__main__":
    main()
