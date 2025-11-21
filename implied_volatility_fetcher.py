"""
Implied Volatility Data Fetcher using Alpha Vantage Options API.
Fetches at-the-money (ATM) options data and implied volatility for specific stocks.
"""

import os
import requests
import time
import sqlite3
from typing import Dict, List, Optional, Tuple
from datetime import datetime, timedelta
from dotenv import load_dotenv
import logging

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# API Configuration
ALPHA_VANTAGE_API_KEY = os.getenv('ALPHA_VANTAGE_API_KEY')
BASE_URL = 'https://www.alphavantage.co/query'

# Rate limiting: Alpha Vantage free tier allows 5 API calls per minute, 500 per day
RATE_LIMIT_DELAY = 12  # seconds between calls


class ImpliedVolatilityFetcher:
    """Fetcher for implied volatility data from Alpha Vantage"""

    def __init__(self, api_key: Optional[str] = None, db_path: Optional[str] = None):
        self.api_key = api_key or ALPHA_VANTAGE_API_KEY
        if not self.api_key:
            raise ValueError("Alpha Vantage API key not found. Set ALPHA_VANTAGE_API_KEY in .env file")

        self.db_path = db_path or 'market_data.db'
        self.last_call_time = 0

    def _rate_limit(self):
        """Enforce rate limiting"""
        elapsed = time.time() - self.last_call_time
        if elapsed < RATE_LIMIT_DELAY:
            sleep_time = RATE_LIMIT_DELAY - elapsed
            logger.info(f"Rate limiting: sleeping for {sleep_time:.1f}s")
            time.sleep(sleep_time)
        self.last_call_time = time.time()

    def _make_request(self, params: Dict) -> Dict:
        """Make API request with error handling"""
        self._rate_limit()

        params['apikey'] = self.api_key

        try:
            response = requests.get(BASE_URL, params=params, timeout=30)
            response.raise_for_status()
            data = response.json()

            # Check for API errors
            if 'Error Message' in data:
                logger.error(f"API Error: {data['Error Message']}")
                return {}

            if 'Note' in data:
                logger.warning(f"API Note (rate limit?): {data['Note']}")
                return {}

            return data

        except requests.exceptions.RequestException as e:
            logger.error(f"Request failed: {e}")
            return {}

    def get_options_data(self, symbol: str) -> Dict:
        """
        Get options chain data for a symbol.
        Returns options data including strike prices, expiration dates, and implied volatility.
        """
        params = {
            'function': 'HISTORICAL_OPTIONS',
            'symbol': symbol,
            'date': datetime.now().strftime('%Y-%m-%d')
        }
        logger.info(f"Fetching options data for {symbol}")
        return self._make_request(params)

    def calculate_atm_iv(self, options_data: Dict, current_price: float) -> Tuple[Optional[float], Optional[float]]:
        """
        Calculate at-the-money implied volatility from options data.
        Returns (call_iv, put_iv) tuple.
        """
        if not options_data or 'data' not in options_data:
            return None, None

        options = options_data.get('data', [])
        if not options:
            return None, None

        # Find ATM options (closest to current price)
        atm_call = None
        atm_put = None
        min_call_diff = float('inf')
        min_put_diff = float('inf')

        for option in options:
            try:
                strike = float(option.get('strike', 0))
                option_type = option.get('type', '').lower()
                iv = option.get('implied_volatility')

                if iv is None:
                    continue

                iv = float(iv)
                diff = abs(strike - current_price)

                if option_type == 'call' and diff < min_call_diff:
                    min_call_diff = diff
                    atm_call = iv
                elif option_type == 'put' and diff < min_put_diff:
                    min_put_diff = diff
                    atm_put = iv

            except (ValueError, TypeError) as e:
                logger.debug(f"Error parsing option data: {e}")
                continue

        return atm_call, atm_put

    def get_stock_iv(self, symbol: str, current_price: Optional[float] = None) -> Dict:
        """
        Get implied volatility for a stock.
        If current_price is not provided, fetches it from the API.

        Returns dict with:
        - symbol: stock ticker
        - date: current date
        - call_iv: ATM call implied volatility
        - put_iv: ATM put implied volatility
        - average_iv: average of call and put IV
        """
        # Get current price if not provided
        if current_price is None:
            price_data = self._get_current_price(symbol)
            current_price = price_data.get('price')

            if current_price is None:
                logger.error(f"Could not fetch current price for {symbol}")
                return {}

        # Get options data
        options_data = self.get_options_data(symbol)

        if not options_data:
            logger.error(f"No options data available for {symbol}")
            return {}

        # Calculate ATM IV
        call_iv, put_iv = self.calculate_atm_iv(options_data, current_price)

        if call_iv is None and put_iv is None:
            logger.warning(f"Could not calculate IV for {symbol}")
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
            'current_price': current_price,
            'call_iv': call_iv,
            'put_iv': put_iv,
            'average_iv': avg_iv
        }

    def _get_current_price(self, symbol: str) -> Dict:
        """Get current price for a symbol using GLOBAL_QUOTE endpoint"""
        params = {
            'function': 'GLOBAL_QUOTE',
            'symbol': symbol
        }

        logger.info(f"Fetching current price for {symbol}")
        data = self._make_request(params)

        quote = data.get('Global Quote', {})
        price_str = quote.get('05. price')

        if price_str:
            try:
                return {'price': float(price_str)}
            except ValueError:
                pass

        return {}

    def init_database(self):
        """Initialize database tables for implied volatility data"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        # Create table for implied volatility time series
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS implied_volatility_daily (
                date TEXT NOT NULL,
                ticker TEXT NOT NULL,
                call_iv REAL,
                put_iv REAL,
                average_iv REAL,
                current_price REAL,
                PRIMARY KEY (date, ticker)
            )
        ''')

        # Create index for faster queries
        cursor.execute('''
            CREATE INDEX IF NOT EXISTS idx_iv_ticker
            ON implied_volatility_daily(ticker)
        ''')

        cursor.execute('''
            CREATE INDEX IF NOT EXISTS idx_iv_date
            ON implied_volatility_daily(date)
        ''')

        conn.commit()
        conn.close()
        logger.info("Database initialized for implied volatility data")

    def save_to_database(self, iv_data: Dict) -> bool:
        """Save implied volatility data to database"""
        if not iv_data or 'symbol' not in iv_data:
            logger.error("Invalid IV data, cannot save to database")
            return False

        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()

            cursor.execute('''
                INSERT OR REPLACE INTO implied_volatility_daily
                (date, ticker, call_iv, put_iv, average_iv, current_price)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (
                iv_data['date'],
                iv_data['symbol'],
                iv_data.get('call_iv'),
                iv_data.get('put_iv'),
                iv_data.get('average_iv'),
                iv_data.get('current_price')
            ))

            conn.commit()
            conn.close()
            logger.info(f"Saved IV data for {iv_data['symbol']} to database")
            return True

        except sqlite3.Error as e:
            logger.error(f"Database error: {e}")
            return False

    def fetch_and_store_iv(self, symbols: List[str]) -> Dict[str, Dict]:
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
                    self.save_to_database(iv_data)
                    results[symbol] = iv_data
                    logger.info(f"✓ {symbol}: avg_iv={iv_data.get('average_iv', 'N/A'):.4f}")
                else:
                    logger.warning(f"✗ {symbol}: No IV data available")
                    results[symbol] = None

            except Exception as e:
                logger.error(f"Error processing {symbol}: {e}")
                results[symbol] = None

        return results

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
                SELECT date, call_iv, put_iv, average_iv, current_price
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
                    'current_price': row[4]
                }
                for row in rows
            ]

        except sqlite3.Error as e:
            logger.error(f"Database error: {e}")
            return []


def test_fetcher():
    """Test the implied volatility fetcher"""
    fetcher = ImpliedVolatilityFetcher()

    # Initialize database
    fetcher.init_database()

    # Test with popular stocks
    test_symbols = ['AAPL', 'MSFT', 'GOOGL', 'TSLA', 'SPY']

    print(f"\n{'='*70}")
    print(f"Testing Implied Volatility Fetcher with {len(test_symbols)} symbols")
    print(f"{'='*70}\n")

    results = fetcher.fetch_and_store_iv(test_symbols)

    print(f"\n{'='*70}")
    print("Results Summary:")
    print(f"{'='*70}\n")

    for symbol, data in results.items():
        if data:
            print(f"{symbol:6s} | IV: {data.get('average_iv', 0):.4f} | "
                  f"Call: {data.get('call_iv', 0) or 'N/A'} | "
                  f"Put: {data.get('put_iv', 0) or 'N/A'} | "
                  f"Price: ${data.get('current_price', 0):.2f}")
        else:
            print(f"{symbol:6s} | No data available")


if __name__ == '__main__':
    test_fetcher()
