#!/usr/bin/env python3
"""
Update market data and store it in the SQLite database.

This script is the stable entry point and orchestrator. It supports selecting
which asset groups to update via --assets and controls verbosity via --verbose/--quiet.
It delegates to:
 - download_all_assets.update_sp500_data() for stocks/ETFs/ADRs/FX/crypto
 - download_futures.update_futures_data() for futures

Interactive mode: Run without arguments to get a menu.
"""
import argparse
import sys
import time
from datetime import datetime

import subprocess

from constants import DB_PATH
from download_all_assets import update_sp500_data
from download_futures import update_futures_data
from cboe_iv_fetcher import CBOEImpliedVolatilityFetcher
from fetch_b3_yield_curve import fetch_historical_curves, update_database as update_b3_database
from update_fx_ny_close import get_fx_tickers_from_db, download_fx_at_ny_close, update_database as update_fx_database
from fetch_bcb_rates import fetch_all_bcb_rates, update_database as update_bcb_database
from update_fred_indicators import update_fred_indicators
from update_indices_from_fred import update_indices_from_fred


def update_fred_bonds(verbose: bool = True):
    """Update FRED corporate bond yields (AAA, BBB, High Yield, etc.)."""
    import pandas_datareader.data as web
    from datetime import timedelta
    import sqlite3
    import pandas as pd

    if verbose:
        print("\n" + "=" * 70)
        print("Updating FRED Corporate Bond Yields")
        print("=" * 70)

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

    conn = sqlite3.connect(DB_PATH)
    start = datetime.now() - timedelta(days=60)
    end = datetime.now()

    try:
        existing = pd.read_sql("SELECT * FROM fred_series", conn, parse_dates=["Date"]).set_index("Date")
    except:
        existing = pd.DataFrame()

    updated = 0
    for series_id, name in series_map.items():
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
            updated += 1
            if verbose:
                print(f"  Updated {series_id}")
        except Exception as e:
            if verbose:
                print(f"  Failed {series_id}: {e}")

    if not existing.empty:
        existing.index.name = "Date"
        existing.to_sql("fred_series", conn, if_exists="replace", index=True)

        # Add metadata
        for series_id, name in series_map.items():
            conn.execute("INSERT OR REPLACE INTO ticker_metadata (ticker, name) VALUES (?, ?)", (series_id, name))
        conn.commit()

    conn.close()

    if verbose:
        print(f"Updated {updated}/{len(series_map)} FRED bond series")
        print("=" * 70)


def update_eodhd_bonds(verbose: bool = True):
    """Update EODHD corporate bonds (AAPL, MSFT, AMZN, GOOGL, ORCL)."""
    import subprocess

    if verbose:
        print("\n" + "=" * 70)
        print("Updating EODHD Corporate Bonds (20 calls/day limit)")
        print("=" * 70)

    try:
        result = subprocess.run(
            [sys.executable, "download_eodhd_bonds.py"],
            timeout=120,
            capture_output=not verbose
        )
        if result.returncode != 0 and verbose:
            print("  EODHD bonds update failed (may have hit API limit)")
    except subprocess.TimeoutExpired:
        if verbose:
            print("  EODHD bonds update timed out")
    except FileNotFoundError:
        if verbose:
            print("  download_eodhd_bonds.py not found")
    except Exception as e:
        if verbose:
            print(f"  EODHD bonds update error: {e}")

    if verbose:
        print("=" * 70)


def update_iv_data(verbose: bool = True):
    """Update CBOE volatility indices (VIX, VXN, VXAPL, etc.)."""
    if verbose:
        print("\n" + "=" * 70)
        print("Updating CBOE Volatility Indices")
        print("=" * 70)

    fetcher = CBOEImpliedVolatilityFetcher()
    fetcher.init_database()

    # Fetch CBOE indices only (no calculated IV for individual stocks)
    if verbose:
        print("Fetching CBOE volatility indices...")
    cboe_results = fetcher.fetch_and_store_cboe_indices()

    cboe_success = sum(1 for v in cboe_results.values() if v is not None)

    if verbose:
        print(f"CBOE indices: {cboe_success}/{len(cboe_results)} successful")
        print("=" * 70)


def update_b3_yield_curve(verbose: bool = True):
    """Update Brazil DI yield curve from B3."""
    from datetime import timedelta

    if verbose:
        print("\n" + "=" * 70)
        print("Updating B3 DI Yield Curve")
        print("=" * 70)

    # Fetch last 10 days to catch any gaps
    end_date = datetime.now()
    start_date = end_date - timedelta(days=10)

    if verbose:
        print(f"Fetching B3 yield curves from {start_date.date()} to {end_date.date()}...")

    df = fetch_historical_curves(start_date, end_date, verbose=verbose)

    if not df.empty:
        update_b3_database(df, verbose=verbose)
    elif verbose:
        print("No B3 yield curve data fetched.")

    if verbose:
        print("=" * 70)


def update_fx_ny_close(verbose: bool = True):
    """Update FX and crypto prices to use 4pm EST (NY market close)."""
    if verbose:
        print("\n" + "=" * 70)
        print("Updating FX/Crypto to NY Close (4pm EST)")
        print("=" * 70)

    # Get FX and crypto tickers from database
    fx_tickers = get_fx_tickers_from_db(include_crypto=True)

    if verbose:
        print(f"Processing {len(fx_tickers)} FX/crypto tickers...")

    # Download last 5 days of hourly data and extract 4pm EST closes
    fx_df = download_fx_at_ny_close(fx_tickers, period='5d', verbose=verbose)

    if not fx_df.empty:
        update_fx_database(fx_df, verbose=verbose)
    elif verbose:
        print("No FX/crypto data to update.")

    if verbose:
        print("=" * 70)


def update_bcb_rates_data(verbose: bool = True):
    """Update Brazil central bank rates (SELIC, CDI)."""
    from datetime import timedelta

    if verbose:
        print("\n" + "=" * 70)
        print("Updating BCB Rates (SELIC, CDI)")
        print("=" * 70)

    # Fetch last 30 days
    end_date = datetime.now()
    start_date = end_date - timedelta(days=30)

    df = fetch_all_bcb_rates(start_date, end_date, verbose=verbose)

    if not df.empty:
        update_bcb_database(df, verbose=verbose)
    elif verbose:
        print("No BCB rates fetched.")

    if verbose:
        print("=" * 70)


def update_fred_data(verbose: bool = True):
    """Update FRED economic indicators (ECB rates, etc.)."""
    if verbose:
        print("\n" + "=" * 70)
        print("Updating FRED Economic Indicators")
        print("=" * 70)

    update_fred_indicators(lookback_days=60)

    if verbose:
        print("=" * 70)


def update_fred_indices_data(verbose: bool = True, lookback_days: int = 30):
    """Update FRED volatility indices (RVX, VXV, VXO, EVZ)."""
    if verbose:
        print("\n" + "=" * 70)
        print("Updating FRED Volatility Indices")
        print("=" * 70)

    update_indices_from_fred(lookback_days=lookback_days)

    if verbose:
        print("=" * 70)


def update_fundamentals_data(verbose: bool = True):
    """Update Alpha Vantage fundamentals (priority tickers)."""
    if verbose:
        print("\n" + "=" * 70)
        print("Updating Alpha Vantage Fundamentals")
        print("=" * 70)

    try:
        result = subprocess.run(
            [sys.executable, "fetch_fundamentals.py", "--refresh", "--priority", "--force"],
            timeout=900,  # 15 min timeout for rate-limited API
            capture_output=not verbose
        )
        if result.returncode != 0 and verbose:
            print("  Fundamentals update failed")
    except subprocess.TimeoutExpired:
        if verbose:
            print("  Fundamentals update timed out (15 min limit)")
    except FileNotFoundError:
        if verbose:
            print("  fetch_fundamentals.py not found")
    except Exception as e:
        if verbose:
            print(f"  Fundamentals update error: {e}")

    if verbose:
        print("=" * 70)


def show_interactive_menu():
    """Show interactive menu and return (mode, lookback_days, assets) or None to cancel."""
    print("\n" + "=" * 70)
    print("  MARKET DATA UPDATE")
    print("=" * 70)
    print(f"Database: {DB_PATH}")
    print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    print("  WARNING: Database contains irreplaceable data:")
    print("  - B3 DI yield curves (5,445 days of cleaned data)")
    print("  - Bond prices, portfolios, theses")
    print("  Use INCREMENTAL mode to protect historical data.")
    print("=" * 70)

    # Step 1: Update mode
    print("\n[1] Select update mode:")
    print("    1. Incremental (last 10 days) - RECOMMENDED, fast")
    print("    2. Incremental (last 30 days) - catches longer gaps")
    print("    3. Full history download - SLOW, can timeout")
    print("    4. Cancel")

    while True:
        choice = input("\nEnter choice [1-4] (default: 1): ").strip()
        if choice == "" or choice == "1":
            lookback_days = 10
            mode_desc = "Incremental (last 10 days)"
            break
        elif choice == "2":
            lookback_days = 30
            mode_desc = "Incremental (last 30 days)"
            break
        elif choice == "3":
            lookback_days = None
            mode_desc = "Full history"
            break
        elif choice == "4":
            print("Cancelled.")
            return None
        else:
            print("Invalid choice. Enter 1, 2, 3, or 4.")

    # Step 2: Asset selection
    print("\n[2] Select assets to update:")
    print("    1. All assets (stocks, ETFs, ADRs, FX, crypto, futures, IV, etc.)")
    print("    2. Core only (stocks, ETFs, ADRs)")
    print("    3. FX & Crypto only")
    print("    4. Futures only")
    print("    5. Supplemental only (IV, B3, BCB, FRED)")
    print("    6. Custom selection")
    print("    7. Cancel")

    all_assets = ["stocks", "etfs", "mutualfunds", "adrs", "fx", "crypto", "futures", "iv", "china", "korea", "brazil", "canada", "b3", "fxclose", "bcb", "fred", "fredbonds", "eodhdbonds", "fredindices", "fundamentals"]

    while True:
        choice = input("\nEnter choice [1-7] (default: 1): ").strip()
        if choice == "" or choice == "1":
            assets = all_assets
            assets_desc = "All assets"
            break
        elif choice == "2":
            assets = ["stocks", "etfs", "adrs"]
            assets_desc = "Core (stocks, ETFs, ADRs)"
            break
        elif choice == "3":
            assets = ["fx", "crypto", "fxclose"]
            assets_desc = "FX & Crypto"
            break
        elif choice == "4":
            assets = ["futures"]
            assets_desc = "Futures"
            break
        elif choice == "5":
            assets = ["iv", "b3", "bcb", "fred"]
            assets_desc = "Supplemental (IV, B3, BCB, FRED)"
            break
        elif choice == "6":
            print(f"\nAvailable: {', '.join(all_assets)}")
            custom = input("Enter assets (comma-separated): ").strip()
            assets = [a.strip().lower() for a in custom.split(",") if a.strip()]
            invalid = [a for a in assets if a not in all_assets]
            if invalid:
                print(f"Invalid assets: {', '.join(invalid)}")
                continue
            if not assets:
                print("No assets selected.")
                continue
            assets_desc = f"Custom ({', '.join(assets)})"
            break
        elif choice == "7":
            print("Cancelled.")
            return None
        else:
            print("Invalid choice. Enter 1-7.")

    # Step 3: Confirmation
    print("\n" + "-" * 70)
    print("CONFIRMATION:")
    print(f"  Mode:   {mode_desc}")
    print(f"  Assets: {assets_desc}")
    print("-" * 70)

    confirm = input("\nProceed? [Y/n]: ").strip().lower()
    if confirm in ("", "y", "yes"):
        return (lookback_days, assets)
    else:
        print("Cancelled.")
        return None


def run_update(assets_to_run: list, lookback_days: int = None, verbose: bool = True):
    """Execute the market data update with the given parameters."""
    print(f"\nUsing database: {DB_PATH}")
    print(f"Starting market data update at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Selected assets: {', '.join(assets_to_run)}")
    if lookback_days:
        print(f"Mode: Incremental (last {lookback_days} days)")
    else:
        print("Mode: Full history download")

    start = time.time()
    try:
        # Run equities/FX/crypto updater if requested
        special_assets = ("futures", "iv", "b3", "fxclose", "bcb", "fred", "fredbonds", "eodhdbonds", "fredindices", "fundamentals")
        non_special_assets = [a for a in assets_to_run if a not in special_assets]
        if non_special_assets:
            if verbose:
                print(f"\n[Orchestrator] Updating asset groups: {', '.join(non_special_assets)}")
            update_sp500_data(verbose=verbose, assets=non_special_assets, lookback_days=lookback_days)

        # Run futures updater if requested
        if "futures" in assets_to_run:
            if verbose:
                print("\n[Orchestrator] Updating asset group: futures")
            update_futures_data(verbose=verbose)

        # Run implied volatility updater if requested
        if "iv" in assets_to_run:
            if verbose:
                print("\n[Orchestrator] Updating implied volatility data")
            update_iv_data(verbose=verbose)

        # Run B3 yield curve updater if requested
        if "b3" in assets_to_run:
            if verbose:
                print("\n[Orchestrator] Updating B3 DI yield curve")
            update_b3_yield_curve(verbose=verbose)

        # Run FX/Crypto NY close updater if requested (corrects to 4pm EST)
        if "fxclose" in assets_to_run:
            if verbose:
                print("\n[Orchestrator] Updating FX/Crypto to NY close (4pm EST)")
            update_fx_ny_close(verbose=verbose)

        # Run BCB rates updater if requested (SELIC, CDI)
        if "bcb" in assets_to_run:
            if verbose:
                print("\n[Orchestrator] Updating BCB rates (SELIC, CDI)")
            update_bcb_rates_data(verbose=verbose)

        # Run FRED indicators updater if requested (ECB rates, etc.)
        if "fred" in assets_to_run:
            if verbose:
                print("\n[Orchestrator] Updating FRED economic indicators")
            update_fred_data(verbose=verbose)

        # Run FRED corporate bond yields updater if requested
        if "fredbonds" in assets_to_run:
            if verbose:
                print("\n[Orchestrator] Updating FRED corporate bond yields")
            update_fred_bonds(verbose=verbose)

        # Run EODHD corporate bonds updater if requested (20 calls/day limit)
        if "eodhdbonds" in assets_to_run:
            if verbose:
                print("\n[Orchestrator] Updating EODHD corporate bonds")
            update_eodhd_bonds(verbose=verbose)

        # Run FRED volatility indices updater if requested (RVX, VXV, etc.)
        if "fredindices" in assets_to_run:
            if verbose:
                print("\n[Orchestrator] Updating FRED volatility indices")
            update_fred_indices_data(verbose=verbose, lookback_days=lookback_days or 30)

        # Run Alpha Vantage fundamentals updater if requested (rate-limited)
        if "fundamentals" in assets_to_run:
            if verbose:
                print("\n[Orchestrator] Updating Alpha Vantage fundamentals")
            update_fundamentals_data(verbose=verbose)

        elapsed = time.time() - start
        print(f"\nUpdate completed in {elapsed/60:.1f} min")
    except KeyboardInterrupt:
        print("\nUpdate interrupted by user.")
        raise
    except Exception as e:
        print(f"\nError during update: {e}")
        raise


def run_status_report():
    """Run the data freshness status report."""
    result = subprocess.run([sys.executable, "scripts/diagnostics/status_report.py"])
    return result.returncode


def run_smoke_check():
    """Run the API smoke check (requires Flask server running)."""
    result = subprocess.run([sys.executable, "scripts/diagnostics/smoke_check.py"], timeout=30)
    return result.returncode


def main():
    # If no arguments provided, show interactive menu
    if len(sys.argv) == 1:
        result = show_interactive_menu()
        if result is None:
            sys.exit(0)
        lookback_days, assets_to_run = result
        run_update(assets_to_run, lookback_days=lookback_days, verbose=True)
        return

    parser = argparse.ArgumentParser(
        description="Build/update the market_data.db SQLite with daily prices/volumes.\n"
                    "Run without arguments for interactive mode.",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "-q", "--quiet", action="store_true", help="Reduce output verbosity"
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="Increase output verbosity"
    )
    parser.add_argument(
        "--lookback", type=int, default=None,
        help="Incremental update: only download last N days (recommended: 10)"
    )
    parser.add_argument(
        "--status", action="store_true",
        help="Show data freshness status only (no update)"
    )
    parser.add_argument(
        "--smoke-check", action="store_true",
        help="Run API smoke check after update (requires Flask server running)"
    )
    parser.add_argument(
        "--assets",
        nargs="+",
        choices=["all", "stocks", "etfs", "mutualfunds", "adrs", "fx", "crypto", "futures", "iv", "china", "korea", "brazil", "canada", "b3", "fxclose", "bcb", "fred", "fredbonds", "eodhdbonds", "fredindices", "fundamentals"],
        default=["all"],
        help=(
            "Asset groups to update. Use one or more of: all, stocks, etfs, mutualfunds, adrs, fx, crypto, futures, iv, china, korea, brazil, canada, b3, fxclose, bcb, fred, fredbonds, eodhdbonds, fredindices, fundamentals. "
            "Default: all"
        ),
    )
    args = parser.parse_args()

    # Handle --status mode (no update, just report)
    if args.status:
        sys.exit(run_status_report())

    verbose = args.verbose or (not args.quiet)

    # Resolve asset selection
    chosen = [a.lower() for a in args.assets]
    if "all" in chosen:
        assets_to_run = ["stocks", "etfs", "mutualfunds", "adrs", "fx", "crypto", "futures", "iv", "china", "korea", "brazil", "canada", "b3", "fxclose", "bcb", "fred", "fredbonds", "eodhdbonds", "fredindices", "fundamentals"]
    else:
        assets_to_run = chosen

    run_update(assets_to_run, lookback_days=args.lookback, verbose=verbose)

    # Run smoke check if requested
    if args.smoke_check:
        print("\n" + "=" * 70)
        print("Running API Smoke Check")
        print("=" * 70)
        try:
            returncode = run_smoke_check()
            if returncode != 0:
                print("Smoke check failed!")
                sys.exit(1)
        except subprocess.TimeoutExpired:
            print("Smoke check timed out (is the Flask server running?)")
        except FileNotFoundError:
            print("smoke_check.py not found")


if __name__ == "__main__":
    main()
