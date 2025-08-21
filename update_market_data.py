#!/usr/bin/env python3
"""
Update market data and store it in the SQLite database.

This is a thin wrapper around the internal updater function so that README
instructions can use a stable entry point (`update_market_data.py`).
"""
import argparse
import time
from datetime import datetime

from constants import DB_PATH
from download_sp500 import update_sp500_data


def main():
    parser = argparse.ArgumentParser(
        description="Build/update the market_data.db SQLite with daily prices/volumes."
    )
    parser.add_argument(
        "-q", "--quiet", action="store_true", help="Reduce output verbosity"
    )
    args = parser.parse_args()

    verbose = not args.quiet

    print(f"Using database: {DB_PATH}")
    print(
        f"Starting market data update at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    )
    start = time.time()
    try:
        update_sp500_data(verbose=verbose)
        elapsed = time.time() - start
        print(f"\n\u2713 Update completed in {elapsed/60:.1f} min")
    except KeyboardInterrupt:
        print("\nUpdate interrupted by user.")
        raise
    except Exception as e:
        print(f"\nError during update: {e}")
        raise


if __name__ == "__main__":
    main()
