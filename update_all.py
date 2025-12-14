"""
Unified daily update script for Market Data Workbench.

Combines all data update steps into a single command:
1. Yahoo Finance prices (stocks, ETFs) ~2 min
2. Futures prices (dedicated futures download) ~1 min
3. FRED indices (volatility) ~5 sec
4. FRED macro indicators ~10 sec
5. FRED corporate bond yields ~10 sec
6. EODHD corporate bonds (20 calls/day limit) ~30 sec
7. Alpha Vantage fundamentals (priority tickers only) ~2-12 min

Usage:
  python update_all.py              # Full update
  python update_all.py --quick      # Skip fundamentals and rate-limited APIs
  python update_all.py --status     # Data freshness dashboard (exits non-zero if stale)
  python update_all.py --smoke-check  # Run smoke check after update (requires server running)
"""

import subprocess
import sys
import time
from datetime import datetime


def run_step(name: str, command: list, timeout: int = 300, optional: bool = False) -> bool:
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
            if optional:
                print(f"\n[WARN] {name} failed (optional step, continuing)")
                return True  # Don't count optional failures
            print(f"\n[FAIL] {name} failed with code {result.returncode}")
            return False

    except subprocess.TimeoutExpired:
        print(f"\n[TIMEOUT] {name} exceeded {timeout}s timeout")
        return False
    except FileNotFoundError:
        if optional:
            print(f"\n[SKIP] {name} - script not found (optional)")
            return True
        print(f"\n[ERROR] {name} - script not found")
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
                        help='Skip fundamentals and rate-limited APIs (faster)')
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
    step_num = 0
    total_steps = 7 if not args.quick else 4

    if not args.fundamentals_only:
        # Step 1: Yahoo Finance prices (stocks, ETFs)
        step_num += 1
        results['Yahoo Finance'] = run_step(
            f"Step {step_num}/{total_steps}: Yahoo Finance (stocks, ETFs)",
            [sys.executable, 'update_market_data_fixed.py', '--batch-size', str(args.batch_size)],
            timeout=300  # 5 min timeout
        )

        # Step 2: Futures prices
        step_num += 1
        results['Futures'] = run_step(
            f"Step {step_num}/{total_steps}: Futures prices",
            [sys.executable, 'download_futures.py'],
            timeout=180  # 3 min timeout
        )

        # Step 3: FRED indices (volatility)
        step_num += 1
        results['FRED Indices'] = run_step(
            f"Step {step_num}/{total_steps}: FRED Indices (volatility)",
            [sys.executable, 'update_indices_from_fred.py', '--lookback', str(args.lookback)],
            timeout=60
        )

        # Step 4: FRED macro indicators
        step_num += 1
        results['FRED Macro'] = run_step(
            f"Step {step_num}/{total_steps}: FRED Macro Indicators",
            [sys.executable, 'update_fred_indicators.py', '--lookback', '60'],
            timeout=60
        )

    # Additional steps (unless --quick)
    if not args.quick and not args.fundamentals_only:
        # Step 5: FRED corporate bond yields
        step_num += 1
        results['FRED Bonds'] = run_step(
            f"Step {step_num}/{total_steps}: FRED Corporate Bond Yields",
            [sys.executable, '-c', '''
import pandas_datareader.data as web
from datetime import datetime, timedelta
import sqlite3
import pandas as pd

db_path = "market_data.db"
conn = sqlite3.connect(db_path)

series_map = {
    "BAMLC0A0CM": "ICE BofA US Corporate Index OAS",
    "BAMLC0A4CBBB": "ICE BofA BBB US Corporate Index OAS",
    "BAMLC0A1CAAA": "ICE BofA AAA US Corporate Index OAS",
    "BAMLH0A0HYM2": "ICE BofA US High Yield Index OAS",
    "AAA": "Moodys Aaa Corporate Bond Yield",
    "BAA": "Moodys Baa Corporate Bond Yield",
    "BAA10Y": "Moodys Baa-10Y Treasury Spread",
    "AAA10Y": "Moodys Aaa-10Y Treasury Spread",
    "BAMLC0A1CAAAEY": "ICE BofA AAA Corporate Effective Yield",
    "BAMLC0A2CAAEY": "ICE BofA AA Corporate Effective Yield",
    "BAMLC0A3CAEY": "ICE BofA A Corporate Effective Yield",
    "BAMLC0A4CBBBEY": "ICE BofA BBB Corporate Effective Yield",
    "BAMLH0A0HYM2EY": "ICE BofA High Yield Effective Yield",
    "BAMLC1A0C13YEY": "ICE BofA 1-3 Year Corporate Yield",
    "BAMLC2A0C35YEY": "ICE BofA 3-5 Year Corporate Yield",
    "BAMLC8A0C15PY": "ICE BofA 15+ Year Corporate Yield",
    "BAMLC0A2CAA": "ICE BofA AA Corporate Index OAS",
    "BAMLC0A3CA": "ICE BofA A Corporate Index OAS",
}

start = datetime.now() - timedelta(days=60)
end = datetime.now()

try:
    existing = pd.read_sql("SELECT * FROM fred_series", conn, parse_dates=["Date"]).set_index("Date")
except:
    existing = pd.DataFrame()

for series_id in series_map.keys():
    try:
        df = web.DataReader(series_id, "fred", start, end)
        df.columns = [series_id]
        if series_id in existing.columns:
            existing[series_id] = df[series_id].combine_first(existing[series_id])
        else:
            if existing.empty:
                existing = df
            else:
                existing[series_id] = df[series_id]
        print(f"Updated {series_id}")
    except Exception as e:
        print(f"Failed {series_id}: {e}")

existing.index.name = "Date"
existing.to_sql("fred_series", conn, if_exists="replace", index=True)
conn.close()
print("FRED bond yields updated")
'''],
            timeout=120
        )

        # Step 6: EODHD corporate bonds (rate-limited)
        step_num += 1
        results['EODHD Bonds'] = run_step(
            f"Step {step_num}/{total_steps}: EODHD Corporate Bonds (20/day limit)",
            [sys.executable, 'download_eodhd_bonds.py'],
            timeout=120,
            optional=True  # Don't fail entire update if API limit reached
        )

    # Step 7: Alpha Vantage fundamentals (unless --quick)
    if not args.quick:
        step_num += 1
        results['Fundamentals'] = run_step(
            f"Step {step_num}/{total_steps}: Alpha Vantage Fundamentals",
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
