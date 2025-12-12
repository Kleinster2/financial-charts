"""
Unified daily update script for Market Data Workbench.

Combines all data update steps into a single command:
1. Yahoo Finance prices (stocks, ETFs, futures) ~2 min
2. FRED indices (volatility) ~5 sec
3. FRED macro indicators ~10 sec
4. Alpha Vantage fundamentals (priority tickers only) ~2-12 min

Usage:
  python update_all.py              # Full update
  python update_all.py --quick      # Skip fundamentals
  python update_all.py --status     # Data freshness dashboard (exits non-zero if stale)
  python update_all.py --smoke-check  # Run smoke check after update (requires server running)
"""

import subprocess
import sys
import time
from datetime import datetime


def run_step(name: str, command: list, timeout: int = 300) -> bool:
    """Run a subprocess and return success status."""
    print(f"\n{'='*60}")
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {name}")
    print(f"{'='*60}")
    print(f"Running: {' '.join(command)}\n")

    start = time.time()
    try:
        result = subprocess.run(
            command,
            timeout=timeout,
            capture_output=False,  # Show output in real-time
        )
        elapsed = time.time() - start

        if result.returncode == 0:
            print(f"\n[OK] {name} completed in {elapsed:.1f}s")
            return True
        else:
            print(f"\n[FAIL] {name} failed with code {result.returncode}")
            return False

    except subprocess.TimeoutExpired:
        print(f"\n[TIMEOUT] {name} exceeded {timeout}s timeout")
        return False
    except Exception as e:
        print(f"\n[ERROR] {name}: {e}")
        return False


def main():
    import argparse

    parser = argparse.ArgumentParser(
        description='Unified daily update for Market Data Workbench'
    )
    parser.add_argument('--quick', action='store_true',
                        help='Skip fundamentals update (faster)')
    parser.add_argument('--status', action='store_true',
                        help='Show data freshness status only')
    parser.add_argument('--fundamentals-only', action='store_true',
                        help='Only update fundamentals')
    parser.add_argument('--batch-size', type=int, default=20,
                        help='Batch size for Yahoo Finance downloads (default: 20)')
    parser.add_argument('--lookback', type=int, default=30,
                        help='Days to look back for FRED updates (default: 30)')
    parser.add_argument('--smoke-check', action='store_true',
                        help='Run smoke check after update (requires Flask server running)')

    args = parser.parse_args()

    # Status mode (no banner, just run report)
    if args.status:
        result = subprocess.run([sys.executable, 'scripts/diagnostics/status_report.py'])
        sys.exit(result.returncode)

    print(f"""
{'='*60}
  MARKET DATA WORKBENCH - DAILY UPDATE
  {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
{'='*60}
""")

    results = {}
    start_time = time.time()

    if not args.fundamentals_only:
        # Step 1: Yahoo Finance prices
        results['Yahoo Finance'] = run_step(
            "Step 1/4: Yahoo Finance (stocks, ETFs, futures)",
            [sys.executable, 'update_market_data_fixed.py', '--batch-size', str(args.batch_size)],
            timeout=300  # 5 min timeout
        )

        # Step 2: FRED indices
        results['FRED Indices'] = run_step(
            "Step 2/4: FRED Indices (volatility)",
            [sys.executable, 'update_indices_from_fred.py', '--lookback', str(args.lookback)],
            timeout=60
        )

        # Step 3: FRED macro indicators
        results['FRED Macro'] = run_step(
            "Step 3/4: FRED Macro Indicators",
            [sys.executable, 'update_fred_indicators.py', '--lookback', '60'],
            timeout=60
        )

    # Step 4: Alpha Vantage fundamentals (unless --quick)
    if not args.quick:
        results['Fundamentals'] = run_step(
            "Step 4/4: Alpha Vantage Fundamentals (priority tickers)",
            [sys.executable, 'fetch_fundamentals.py', '--refresh', '--priority', '--force'],
            timeout=900  # 15 min timeout for rate-limited API
        )
    else:
        print("\n[SKIP] Fundamentals update (--quick mode)")

    # Optional smoke check (requires Flask server running)
    if args.smoke_check:
        results['Smoke Check'] = run_step(
            "Smoke Check: API verification",
            [sys.executable, 'scripts/diagnostics/smoke_check.py'],
            timeout=30
        )

    # Summary
    total_time = time.time() - start_time

    print(f"""
{'='*60}
  UPDATE COMPLETE
{'='*60}
  Total time: {total_time:.1f}s ({total_time/60:.1f} min)

  Results:
""")

    for step, success in results.items():
        status = "[OK]  " if success else "[FAIL]"
        print(f"    {status} {step}")

    failed = [k for k, v in results.items() if not v]
    if failed:
        print(f"\n  WARNING: {len(failed)} step(s) failed: {', '.join(failed)}")
        if 'Smoke Check' in failed:
            print("           (Smoke check requires Flask server running)")
        sys.exit(1)
    else:
        print("\n  All steps completed successfully!")


if __name__ == '__main__':
    main()
