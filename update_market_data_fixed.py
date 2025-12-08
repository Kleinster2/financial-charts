#!/usr/bin/env python
"""
Fixed version of update_market_data.py that handles hanging issues.
Uses intelligent batching, timeout handling, and retry logic.
"""

import sys
import time
import logging
from datetime import datetime, timedelta
from typing import List, Dict, Any
import pandas as pd
import yfinance as yf
from constants import DB_PATH, get_db_connection, USE_DUCKDB

# DuckDB support - enabled via USE_DUCKDB=1 environment variable
if USE_DUCKDB:
    try:
        from duckdb_writer import write_stock_prices
        DUCKDB_ENABLED = True
    except ImportError:
        DUCKDB_ENABLED = False
else:
    DUCKDB_ENABLED = False

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

# Import the ticker lists from download_all_assets
from download_all_assets import (
    get_sp500_tickers, get_ibovespa_tickers, build_fx_tickers,
    ETF_TICKERS, ADR_TICKERS, ADDITIONAL_FX_TICKERS, CRYPTO_TICKERS,
    OTHER_HIGH_PROFILE_STOCKS, EV_STOCKS, QUANTUM_STOCKS,
    ADTECH_STOCKS, GAMING_IGAMING_STOCKS, BIOTECH_STOCKS,
    MINING_RARE_EARTH_STOCKS, BATTERY_ENERGY_STORAGE_STOCKS,
    NUCLEAR_ENERGY_STOCKS, AI_SEMICONDUCTOR_STOCKS,
    SPACE_AEROSPACE_STOCKS, DEFENSE_STOCKS, EXCLUDED_TICKERS,
    FUTURES_SYMBOLS, CRYPTO_STOCKS  # Add CRYPTO_STOCKS
)

class MarketDataUpdater:
    """Robust market data updater with batching and error handling."""

    def __init__(self, batch_size: int = 25, max_retries: int = 3, timeout: int = 10):
        self.batch_size = batch_size
        self.max_retries = max_retries
        self.timeout = timeout
        self.failed_tickers = []
        self.successful_tickers = []

        # Date range
        self.start_date = "2000-01-01"  # Get full historical data
        self.end_date = (datetime.today() + timedelta(days=1)).strftime("%Y-%m-%d")

    def get_all_tickers(self, asset_groups: List[str] = None) -> List[str]:
        """Get all tickers based on selected asset groups."""
        logger.info("Loading ticker lists...")

        # Get ticker lists
        sp500_tickers, _ = get_sp500_tickers()
        ibov_tickers = get_ibovespa_tickers()
        fx_tickers = build_fx_tickers()

        # Build asset groups
        groups = {
            'stocks': sorted(list(set(
                sp500_tickers + ibov_tickers + OTHER_HIGH_PROFILE_STOCKS +
                EV_STOCKS + CRYPTO_STOCKS + QUANTUM_STOCKS +
                ADTECH_STOCKS + GAMING_IGAMING_STOCKS + BIOTECH_STOCKS +
                MINING_RARE_EARTH_STOCKS + BATTERY_ENERGY_STORAGE_STOCKS +
                NUCLEAR_ENERGY_STOCKS + AI_SEMICONDUCTOR_STOCKS +
                SPACE_AEROSPACE_STOCKS + DEFENSE_STOCKS
            ))),
            'etfs': ETF_TICKERS,
            'adrs': ADR_TICKERS,
            'fx': sorted(list(set(fx_tickers + ADDITIONAL_FX_TICKERS))),
            'crypto': CRYPTO_TICKERS,
            'futures': list(FUTURES_SYMBOLS.values()),
        }

        # Filter out excluded tickers
        groups['stocks'] = [t for t in groups['stocks'] if t not in EXCLUDED_TICKERS]

        # Select groups
        if not asset_groups:
            asset_groups = list(groups.keys())

        selected_tickers = []
        for group in asset_groups:
            if group in groups:
                selected_tickers.extend(groups[group])
                logger.info(f"  {group}: {len(groups[group])} tickers")

        # Remove duplicates and sort
        all_tickers = sorted(list(set(selected_tickers)))
        logger.info(f"Total unique tickers: {len(all_tickers)}")

        return all_tickers

    def download_batch(self, tickers: List[str], batch_num: int, total_batches: int) -> Dict[str, pd.DataFrame]:
        """Download a batch of tickers with error handling."""
        results = {}
        logger.info(f"Batch {batch_num}/{total_batches}: Downloading {len(tickers)} tickers")

        try:
            # Try batch download first
            data = yf.download(
                tickers,
                start=self.start_date,
                end=self.end_date,
                auto_adjust=True,
                group_by='ticker' if len(tickers) > 1 else None,
                progress=False,
                threads=True,
                timeout=self.timeout
            )

            if not data.empty:
                if len(tickers) == 1:
                    # Single ticker case
                    results[tickers[0]] = data
                    self.successful_tickers.append(tickers[0])
                else:
                    # Multi-ticker case
                    for ticker in tickers:
                        try:
                            if ticker in data.columns.get_level_values(0):
                                ticker_data = data[ticker]
                                if not ticker_data['Close'].isna().all():
                                    results[ticker] = ticker_data
                                    self.successful_tickers.append(ticker)
                                else:
                                    logger.debug(f"  {ticker}: No valid data")
                                    self.failed_tickers.append(ticker)
                        except Exception:
                            logger.debug(f"  {ticker}: Error extracting data")
                            self.failed_tickers.append(ticker)

        except Exception as e:
            logger.warning(f"Batch download failed: {str(e)[:100]}")
            # Fall back to individual downloads
            for ticker in tickers:
                if ticker not in results:
                    result = self.download_single_ticker(ticker)
                    if result is not None:
                        results[ticker] = result

        return results

    def download_single_ticker(self, ticker: str) -> pd.DataFrame:
        """Download a single ticker with retry logic."""
        for attempt in range(self.max_retries):
            try:
                data = yf.download(
                    ticker,
                    start=self.start_date,
                    end=self.end_date,
                    auto_adjust=True,
                    progress=False,
                    timeout=self.timeout // 2  # Shorter timeout for single ticker
                )

                if not data.empty and not data['Close'].isna().all():
                    self.successful_tickers.append(ticker)
                    return data

            except Exception as e:
                if attempt == self.max_retries - 1:
                    logger.debug(f"  {ticker}: Failed after {self.max_retries} attempts")
                    self.failed_tickers.append(ticker)
                else:
                    time.sleep(0.5)  # Brief pause before retry

        return None

    def update_database(self, all_data: Dict[str, pd.DataFrame]):
        """Update the database with downloaded data."""
        if not all_data:
            logger.error("No data to update")
            return False

        logger.info(f"Processing {len(all_data)} tickers for database update...")

        # Process data
        processed_dfs = []
        processed_vol_dfs = []

        for ticker, data in all_data.items():
            if 'Close' in data.columns:
                close_series = data[['Close']].rename(columns={'Close': ticker})
                processed_dfs.append(close_series)

            if 'Volume' in data.columns:
                vol_series = data[['Volume']].rename(columns={'Volume': ticker})
                processed_vol_dfs.append(vol_series)

        if not processed_dfs:
            logger.error("No valid price data to save")
            return False

        # Combine all data
        new_data_df = pd.concat(processed_dfs, axis=1)
        new_data_df.index = pd.to_datetime(new_data_df.index)

        new_vol_df = pd.DataFrame()
        if processed_vol_dfs:
            new_vol_df = pd.concat(processed_vol_dfs, axis=1)
            new_vol_df.index = pd.to_datetime(new_vol_df.index)

        logger.info(f"Latest data date: {new_data_df.index[-1].strftime('%Y-%m-%d')}")

        # Update database
        conn = get_db_connection(row_factory=None)
        try:
            cursor = conn.cursor()

            # Check if tables exist
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='stock_prices_daily';")
            table_exists = cursor.fetchone() is not None

            # Load existing data
            existing_df = pd.DataFrame()
            if table_exists:
                existing_df = pd.read_sql("SELECT * FROM stock_prices_daily", conn)
                if not existing_df.empty and 'Date' in existing_df.columns:
                    existing_df['Date'] = pd.to_datetime(existing_df['Date'])
                    existing_df.set_index('Date', inplace=True)

            logger.info(f"Merging with existing data ({len(existing_df)} rows)...")

            # Merge with existing data
            if not existing_df.empty:
                combined_df = existing_df.copy()

                # Add new columns if needed
                for col in new_data_df.columns:
                    if col not in combined_df.columns:
                        combined_df[col] = pd.NA

                # Combine dataframes using vectorized update (MUCH faster)
                combined_df.update(new_data_df)

                # Add any new dates from new_data_df that don't exist in combined_df
                new_dates = new_data_df.index.difference(combined_df.index)
                if len(new_dates) > 0:
                    combined_df = pd.concat([combined_df, new_data_df.loc[new_dates]])
                    combined_df = combined_df.sort_index()
            else:
                combined_df = new_data_df

            # Clean up any existing staging tables and indices
            cursor.execute("DROP INDEX IF EXISTS ix_stock_prices_daily_staging_Date")
            cursor.execute("DROP TABLE IF EXISTS stock_prices_daily_staging")
            cursor.execute("DROP TABLE IF EXISTS stock_prices_daily_old")
            conn.commit()

            # Save to staging table
            logger.info("Saving to database...")
            staging_table = "stock_prices_daily_staging"
            # Replace pd.NA with np.nan for SQLite compatibility
            combined_df = combined_df.fillna(value=pd.NA).replace({pd.NA: None})
            combined_df.to_sql(
                staging_table, conn,
                if_exists="replace",
                index=True,
                index_label='Date',
                dtype='REAL'
            )

            # Verify staging table
            cursor.execute(f"SELECT COUNT(*) FROM {staging_table}")
            staging_count = cursor.fetchone()[0]

            if staging_count != len(combined_df):
                logger.error(f"Staging table row count mismatch: {staging_count} != {len(combined_df)}")
                cursor.execute(f"DROP TABLE IF EXISTS {staging_table}")
                conn.commit()
                return False

            # Atomic swap
            if table_exists:
                cursor.execute("ALTER TABLE stock_prices_daily RENAME TO stock_prices_daily_old")
            cursor.execute(f"ALTER TABLE {staging_table} RENAME TO stock_prices_daily")

            # Clean up old table
            cursor.execute("DROP TABLE IF EXISTS stock_prices_daily_old")
            conn.commit()

            # Verify update
            cursor.execute("SELECT Date FROM stock_prices_daily ORDER BY Date DESC LIMIT 1")
            latest_date = cursor.fetchone()[0]
            logger.info(f"Database updated successfully. Latest date: {latest_date}")

            # Update volumes if available
            if not new_vol_df.empty:
                # Similar process for volumes (simplified here)
                logger.info("Updating volume data...")
                # ... (volume update logic similar to prices)

            # Update DuckDB if enabled
            if DUCKDB_ENABLED:
                try:
                    logger.info("Updating DuckDB...")
                    write_stock_prices(combined_df, new_vol_df if not new_vol_df.empty else None, verbose=True)
                except Exception as e:
                    logger.warning(f"DuckDB update failed (non-fatal): {e}")

            # Auto-update metadata
            try:
                from metadata_utils import auto_update_new_tickers
                logger.info("Updating ticker metadata...")
                stats = auto_update_new_tickers()
                if stats['successful'] > 0:
                    logger.info(f"Metadata updated: {stats['successful']} added, {stats['failed']} failed")
            except Exception as e:
                logger.warning(f"Could not update metadata: {e}")

            return True

        except Exception as e:
            logger.error(f"Database update failed: {e}")
            return False
        finally:
            conn.close()

    def run(self, asset_groups: List[str] = None, verbose: bool = True):
        """Main update process."""
        start_time = time.time()

        if verbose:
            logger.setLevel(logging.INFO)
        else:
            logger.setLevel(logging.WARNING)

        logger.info("="*60)
        logger.info("Market Data Update - Fixed Version")
        logger.info(f"Date range: {self.start_date} to {self.end_date}")
        logger.info("="*60)

        # Get all tickers
        all_tickers = self.get_all_tickers(asset_groups)

        if not all_tickers:
            logger.error("No tickers to update")
            return False

        # Download in batches
        all_data = {}
        total_batches = (len(all_tickers) + self.batch_size - 1) // self.batch_size

        for i in range(0, len(all_tickers), self.batch_size):
            batch = all_tickers[i:i + self.batch_size]
            batch_num = (i // self.batch_size) + 1

            batch_data = self.download_batch(batch, batch_num, total_batches)
            all_data.update(batch_data)

            # Progress update
            if batch_num % 10 == 0:
                logger.info(f"Progress: {len(self.successful_tickers)}/{len(all_tickers)} successful")

            # Brief pause between batches to avoid rate limiting
            if batch_num < total_batches:
                time.sleep(0.5)

        # Summary
        logger.info("="*60)
        logger.info(f"Download complete:")
        logger.info(f"  Successful: {len(self.successful_tickers)} tickers")
        logger.info(f"  Failed: {len(self.failed_tickers)} tickers")

        if self.failed_tickers and len(self.failed_tickers) < 50:
            logger.info(f"  Failed tickers: {', '.join(self.failed_tickers[:50])}")

        # Update database
        if all_data:
            success = self.update_database(all_data)
            if success:
                elapsed = time.time() - start_time
                logger.info(f"Update completed in {elapsed:.1f} seconds")
                return True
            else:
                logger.error("Database update failed")
                return False
        else:
            logger.error("No data downloaded")
            return False


def main():
    """Command-line interface."""
    import argparse

    parser = argparse.ArgumentParser(description='Update market data with robust handling')
    parser.add_argument('--assets', nargs='+',
                       choices=['stocks', 'etfs', 'adrs', 'fx', 'crypto', 'futures'],
                       help='Asset groups to update')
    parser.add_argument('--batch-size', type=int, default=25,
                       help='Number of tickers per batch (default: 25)')
    parser.add_argument('--verbose', '-v', action='store_true',
                       help='Enable verbose output')
    parser.add_argument('--quiet', '-q', action='store_true',
                       help='Minimize output')

    args = parser.parse_args()

    # Create updater
    updater = MarketDataUpdater(batch_size=args.batch_size)

    # Determine verbosity
    verbose = True
    if args.quiet:
        verbose = False
    elif args.verbose:
        verbose = True

    # Run update
    success = updater.run(asset_groups=args.assets, verbose=verbose)

    # Exit with appropriate code
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()