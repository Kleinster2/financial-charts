"""
CBOE Implied Volatility Data Fetcher using yfinance.
Fetches options data and calculates at-the-money implied volatility for stocks.
Also provides access to VIX and other CBOE volatility indices.
"""

import sqlite3
from typing import Dict, List, Optional, Tuple
from datetime import datetime, timedelta
import logging
import yfinance as yf
import pandas as pd
import numpy as np
from constants import DB_PATH

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class CBOEImpliedVolatilityFetcher:
    """Fetcher for implied volatility data using yfinance"""

    def __init__(self, db_path: Optional[str] = None):
        self.db_path = db_path or DB_PATH

    def get_stock_iv(self, symbol: str) -> Dict:
        """
        Get implied volatility for a stock using yfinance options data.

        Returns dict with:
        - symbol: stock ticker
        - date: current date
        - current_price: current stock price
        - call_iv: ATM call implied volatility
        - put_iv: ATM put implied volatility
        - average_iv: average of call and put IV
        - expiration: options expiration date used
        """
        try:
            ticker = yf.Ticker(symbol)

            # Get current price
            hist = ticker.history(period='1d')
            if hist.empty:
                logger.error(f"No price data available for {symbol}")
                return {}

            current_price = hist['Close'].iloc[-1]

            # Get available expiration dates
            expirations = ticker.options

            if not expirations:
                logger.warning(f"No options available for {symbol}")
                return {}

            # Use the nearest expiration date (typically most liquid)
            nearest_expiry = expirations[0]

            # Get options chain
            opt_chain = ticker.option_chain(nearest_expiry)

            if opt_chain.calls.empty and opt_chain.puts.empty:
                logger.warning(f"No options data for {symbol}")
                return {}

            # Calculate ATM IV for calls
            call_iv = self._find_atm_iv(opt_chain.calls, current_price)

            # Calculate ATM IV for puts
            put_iv = self._find_atm_iv(opt_chain.puts, current_price)

            if call_iv is None and put_iv is None:
                logger.warning(f"Could not find ATM IV for {symbol}")
                return {}

            # Calculate average IV
            if call_iv is not None and put_iv is not None:
                avg_iv = (call_iv + put_iv) / 2
            elif call_iv is not None:
                avg_iv = call_iv
            else:
                avg_iv = put_iv

            return {
                'symbol': symbol,
                'date': datetime.now().strftime('%Y-%m-%d'),
                'current_price': float(current_price),
                'call_iv': float(call_iv) if call_iv is not None else None,
                'put_iv': float(put_iv) if put_iv is not None else None,
                'average_iv': float(avg_iv),
                'expiration': nearest_expiry
            }

        except Exception as e:
            logger.error(f"Error fetching IV for {symbol}: {e}")
            return {}

    def _find_atm_iv(self, options_df: pd.DataFrame, current_price: float) -> Optional[float]:
        """
        Find the at-the-money implied volatility from options dataframe.
        Returns the IV of the option with strike closest to current price.
        """
        if options_df.empty or 'impliedVolatility' not in options_df.columns:
            return None

        # Filter out options with zero or NaN IV
        valid_options = options_df[
            (options_df['impliedVolatility'].notna()) &
            (options_df['impliedVolatility'] > 0)
        ].copy()

        if valid_options.empty:
            return None

        # Find the strike closest to current price
        valid_options['strike_diff'] = abs(valid_options['strike'] - current_price)
        atm_option = valid_options.loc[valid_options['strike_diff'].idxmin()]

        return atm_option['impliedVolatility']

    def get_vix(self) -> Dict:
        """
        Get current VIX (CBOE Volatility Index) value.
        VIX represents the market's expectation of 30-day forward-looking volatility.
        """
        try:
            vix = yf.Ticker('^VIX')
            hist = vix.history(period='5d')

            if hist.empty:
                logger.error("No VIX data available")
                return {}

            latest_date = hist.index[-1].strftime('%Y-%m-%d')
            latest_value = float(hist['Close'].iloc[-1])

            return {
                'symbol': 'VIX',
                'date': latest_date,
                'value': latest_value,
                'description': 'CBOE Volatility Index (S&P 500 30-day implied volatility)'
            }

        except Exception as e:
            logger.error(f"Error fetching VIX: {e}")
            return {}

    def get_cboe_indices(self) -> Dict[str, Dict]:
        """
        Get various CBOE volatility indices.
        Returns dict mapping index symbol to data.
        """
        indices = {
            '^VIX': 'CBOE Volatility Index (S&P 500)',
            '^VXN': 'CBOE Nasdaq-100 Volatility Index',
            '^VXD': 'CBOE DJIA Volatility Index',
            '^RVX': 'CBOE Russell 2000 Volatility Index',
            '^VXAPL': 'CBOE Apple VIX Index',
            '^VXAZN': 'CBOE Amazon VIX Index',
            '^VXGOG': 'CBOE Google VIX Index',
            '^VXGS': 'CBOE Goldman Sachs VIX Index',
            '^VXIBM': 'CBOE IBM VIX Index'
        }

        results = {}

        for symbol, description in indices.items():
            try:
                ticker = yf.Ticker(symbol)
                hist = ticker.history(period='5d')

                if not hist.empty:
                    latest_date = hist.index[-1].strftime('%Y-%m-%d')
                    latest_value = float(hist['Close'].iloc[-1])

                    results[symbol] = {
                        'symbol': symbol,
                        'date': latest_date,
                        'value': latest_value,
                        'description': description
                    }
                    logger.info(f"✓ {symbol}: {latest_value:.2f}")
                else:
                    logger.warning(f"✗ {symbol}: No data available")

            except Exception as e:
                logger.error(f"Error fetching {symbol}: {e}")

        return results

    def init_database(self):
        """Initialize database tables for implied volatility data"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        # Create table for stock implied volatility time series
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS implied_volatility_daily (
                date TEXT NOT NULL,
                ticker TEXT NOT NULL,
                call_iv REAL,
                put_iv REAL,
                average_iv REAL,
                current_price REAL,
                expiration TEXT,
                PRIMARY KEY (date, ticker)
            )
        ''')

        # Create table for VIX and CBOE indices
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS cboe_indices_daily (
                date TEXT NOT NULL,
                symbol TEXT NOT NULL,
                value REAL NOT NULL,
                description TEXT,
                PRIMARY KEY (date, symbol)
            )
        ''')

        # Create indices for faster queries
        cursor.execute('''
            CREATE INDEX IF NOT EXISTS idx_iv_ticker
            ON implied_volatility_daily(ticker)
        ''')

        cursor.execute('''
            CREATE INDEX IF NOT EXISTS idx_iv_date
            ON implied_volatility_daily(date)
        ''')

        cursor.execute('''
            CREATE INDEX IF NOT EXISTS idx_cboe_symbol
            ON cboe_indices_daily(symbol)
        ''')

        conn.commit()
        conn.close()
        logger.info("Database initialized for implied volatility data")

    def save_stock_iv_to_database(self, iv_data: Dict) -> bool:
        """Save stock implied volatility data to database"""
        if not iv_data or 'symbol' not in iv_data:
            logger.error("Invalid IV data, cannot save to database")
            return False

        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()

            cursor.execute('''
                INSERT OR REPLACE INTO implied_volatility_daily
                (date, ticker, call_iv, put_iv, average_iv, current_price, expiration)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (
                iv_data['date'],
                iv_data['symbol'],
                iv_data.get('call_iv'),
                iv_data.get('put_iv'),
                iv_data.get('average_iv'),
                iv_data.get('current_price'),
                iv_data.get('expiration')
            ))

            conn.commit()
            conn.close()
            logger.info(f"Saved IV data for {iv_data['symbol']} to database")
            return True

        except sqlite3.Error as e:
            logger.error(f"Database error: {e}")
            return False

    def save_cboe_index_to_database(self, index_data: Dict) -> bool:
        """Save CBOE index data to database"""
        if not index_data or 'symbol' not in index_data:
            logger.error("Invalid index data, cannot save to database")
            return False

        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()

            cursor.execute('''
                INSERT OR REPLACE INTO cboe_indices_daily
                (date, symbol, value, description)
                VALUES (?, ?, ?, ?)
            ''', (
                index_data['date'],
                index_data['symbol'],
                index_data['value'],
                index_data.get('description')
            ))

            conn.commit()
            conn.close()
            logger.info(f"Saved {index_data['symbol']} data to database")
            return True

        except sqlite3.Error as e:
            logger.error(f"Database error: {e}")
            return False

    def fetch_and_store_stock_iv(self, symbols: List[str]) -> Dict[str, Dict]:
        """
        Fetch implied volatility for multiple symbols and store in database.
        Returns dict mapping symbol to IV data.
        """
        results = {}

        for symbol in symbols:
            logger.info(f"Processing {symbol}...")

            try:
                iv_data = self.get_stock_iv(symbol)

                if iv_data:
                    self.save_stock_iv_to_database(iv_data)
                    results[symbol] = iv_data
                    logger.info(f"✓ {symbol}: avg_iv={iv_data.get('average_iv', 'N/A'):.4f} "
                              f"(exp: {iv_data.get('expiration', 'N/A')})")
                else:
                    logger.warning(f"✗ {symbol}: No IV data available")
                    results[symbol] = None

            except Exception as e:
                logger.error(f"Error processing {symbol}: {e}")
                results[symbol] = None

        return results

    def fetch_and_store_cboe_indices(self) -> Dict[str, Dict]:
        """
        Fetch CBOE volatility indices and store in database.
        Returns dict mapping symbol to index data.
        """
        # Mapping from CBOE index symbols to stock tickers
        cboe_to_stock = {
            '^VXAPL': 'AAPL',
            '^VXAZN': 'AMZN',
            '^VXGOG': 'GOOGL',
            '^VXGS': 'GS',
            '^VXIBM': 'IBM'
        }

        indices_data = self.get_cboe_indices()

        for symbol, data in indices_data.items():
            # Save to cboe_indices_daily table
            self.save_cboe_index_to_database(data)

            # Save ALL CBOE indices to stock_prices_daily table (unified architecture)
            # Keep as percentage (27.56) for wide table
            iv_value = data['value']

            try:
                conn = sqlite3.connect(self.db_path)
                cursor = conn.cursor()

                # Update wide table column for this ticker
                # Note: Date must already exist (from price updates)
                cursor.execute(f'''
                    UPDATE stock_prices_daily
                    SET "{symbol}" = ?
                    WHERE DATE(Date) = ?
                ''', (
                    iv_value,
                    data['date']
                ))

                rows_updated = cursor.rowcount

                # If date doesn't exist yet, insert new row
                if rows_updated == 0:
                    cursor.execute(f'''
                        INSERT INTO stock_prices_daily (Date, "{symbol}")
                        VALUES (?, ?)
                    ''', (
                        data['date'],
                        iv_value
                    ))
                    logger.info(f"Inserted new date {data['date']} with {symbol} = {iv_value}")
                else:
                    logger.info(f"Updated {symbol} = {iv_value} for date {data['date']}")

                conn.commit()
                conn.close()

            except sqlite3.Error as e:
                logger.error(f"Error saving {symbol} to wide table: {e}")

        return indices_data

    def get_iv_history(self, symbol: str, days: int = 30) -> List[Dict]:
        """
        Retrieve historical implied volatility data from database.
        Returns list of dicts with date and IV values.
        """
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()

            start_date = (datetime.now() - timedelta(days=days)).strftime('%Y-%m-%d')

            cursor.execute('''
                SELECT date, call_iv, put_iv, average_iv, current_price, expiration
                FROM implied_volatility_daily
                WHERE ticker = ? AND date >= ?
                ORDER BY date ASC
            ''', (symbol, start_date))

            rows = cursor.fetchall()
            conn.close()

            return [
                {
                    'date': row[0],
                    'call_iv': row[1],
                    'put_iv': row[2],
                    'average_iv': row[3],
                    'current_price': row[4],
                    'expiration': row[5]
                }
                for row in rows
            ]

        except sqlite3.Error as e:
            logger.error(f"Database error: {e}")
            return []

    def get_cboe_index_history(self, symbol: str, days: int = 30) -> List[Dict]:
        """
        Retrieve historical CBOE index data from database.
        Returns list of dicts with date and values.
        """
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()

            start_date = (datetime.now() - timedelta(days=days)).strftime('%Y-%m-%d')

            cursor.execute('''
                SELECT date, value, description
                FROM cboe_indices_daily
                WHERE symbol = ? AND date >= ?
                ORDER BY date ASC
            ''', (symbol, start_date))

            rows = cursor.fetchall()
            conn.close()

            return [
                {
                    'date': row[0],
                    'value': row[1],
                    'description': row[2]
                }
                for row in rows
            ]

        except sqlite3.Error as e:
            logger.error(f"Database error: {e}")
            return []


def test_fetcher():
    """Test the CBOE implied volatility fetcher"""
    fetcher = CBOEImpliedVolatilityFetcher()

    # Initialize database
    fetcher.init_database()

    print(f"\n{'='*70}")
    print("Testing CBOE Implied Volatility Fetcher")
    print(f"{'='*70}\n")

    # Test 1: Fetch CBOE indices (VIX, etc.)
    print("1. Fetching CBOE Volatility Indices:")
    print("-" * 70)
    indices = fetcher.fetch_and_store_cboe_indices()

    for symbol, data in indices.items():
        if data:
            print(f"{symbol:6s} | Value: {data['value']:6.2f} | {data.get('description', '')}")

    # Test 2: Fetch stock implied volatility
    print(f"\n2. Fetching Stock Implied Volatility:")
    print("-" * 70)
    test_symbols = ['AAPL', 'MSFT', 'TSLA', 'SPY', 'QQQ']
    stock_results = fetcher.fetch_and_store_stock_iv(test_symbols)

    print(f"\n{'='*70}")
    print("Results Summary:")
    print(f"{'='*70}\n")

    for symbol, data in stock_results.items():
        if data:
            print(f"{symbol:6s} | IV: {data.get('average_iv', 0):.4f} | "
                  f"Call: {data.get('call_iv') or 'N/A':.4f} | "
                  f"Put: {data.get('put_iv') or 'N/A':.4f} | "
                  f"Price: ${data.get('current_price', 0):.2f} | "
                  f"Exp: {data.get('expiration', 'N/A')}")
        else:
            print(f"{symbol:6s} | No data available")

    print(f"\n{'='*70}")


if __name__ == '__main__':
    test_fetcher()
