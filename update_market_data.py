#!/usr/bin/env python3
"""
Update market data and store it in the SQLite database.

This script is the stable entry point and orchestrator. It supports selecting
which asset groups to update via --assets and controls verbosity via --verbose/--quiet.
It delegates to:
 - download_all_assets.update_sp500_data() for stocks/ETFs/ADRs/FX/crypto
 - download_futures.update_futures_data() for futures
"""
import argparse
import time
from datetime import datetime

from constants import DB_PATH
from download_all_assets import update_sp500_data
from download_futures import update_futures_data
from cboe_iv_fetcher import CBOEImpliedVolatilityFetcher


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


def main():
    parser = argparse.ArgumentParser(
        description="Build/update the market_data.db SQLite with daily prices/volumes."
    )
    parser.add_argument(
        "-q", "--quiet", action="store_true", help="Reduce output verbosity"
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="Increase output verbosity"
    )
    parser.add_argument(
        "--assets",
        nargs="+",
        choices=["all", "stocks", "etfs", "adrs", "fx", "crypto", "futures", "iv", "china", "korea", "brazil"],
        default=["all"],
        help=(
            "Asset groups to update. Use one or more of: all, stocks, etfs, adrs, fx, crypto, futures, iv, china, korea, brazil. "
            "Default: all"
        ),
    )
    args = parser.parse_args()

    verbose = args.verbose or (not args.quiet)

    # Resolve asset selection
    chosen = [a.lower() for a in args.assets]
    if "all" in chosen:
        assets_to_run = ["stocks", "etfs", "adrs", "fx", "crypto", "futures", "iv", "china", "korea", "brazil"]
    else:
        assets_to_run = chosen

    print(f"Using database: {DB_PATH}")
    print(
        f"Starting market data update at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    )
    print(f"Selected assets: {', '.join(assets_to_run)}")
    start = time.time()
    try:
        # Run equities/FX/crypto updater if requested
        non_fut_assets = [a for a in assets_to_run if a not in ("futures", "iv")]
        if non_fut_assets:
            if verbose:
                print(f"\n[Orchestrator] Updating asset groups: {', '.join(non_fut_assets)}")
            update_sp500_data(verbose=verbose, assets=non_fut_assets)

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

        elapsed = time.time() - start
        print(f"\nUpdate completed in {elapsed/60:.1f} min")
    except KeyboardInterrupt:
        print("\nUpdate interrupted by user.")
        raise
    except Exception as e:
        print(f"\nError during update: {e}")
        raise


if __name__ == "__main__":
    main()
