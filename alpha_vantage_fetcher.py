"""
Alpha Vantage API client for fetching fundamental data.
Handles company financials, earnings, balance sheets, income statements, etc.
"""

import json
import os
import time
from typing import Dict, Optional

from dotenv import load_dotenv
import logging

from http_utils import FetchError, fetch_with_retry

# Load environment variables
load_dotenv()

# Configure logging - only set basicConfig if no handlers exist (avoids overriding Flask/app logging)
logger = logging.getLogger(__name__)
if not logging.root.handlers:
    logging.basicConfig(level=logging.INFO)

# API Configuration
ALPHA_VANTAGE_API_KEY = os.getenv('ALPHA_VANTAGE_API_KEY')
BASE_URL = 'https://www.alphavantage.co/query'

# Rate limiting: Alpha Vantage free tier allows 5 API calls per minute, 500 per day
RATE_LIMIT_DELAY = 12  # seconds between calls


class DailyLimitExceeded(Exception):
    """Raised when Alpha Vantage daily API limit (500 calls) is hit"""
    pass


class AlphaVantageClient:
    """Client for Alpha Vantage API"""

    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or ALPHA_VANTAGE_API_KEY
        if not self.api_key:
            raise ValueError("Alpha Vantage API key not found. Set ALPHA_VANTAGE_API_KEY in .env file")
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
        """Make API request with retry/backoff and error handling"""
        self._rate_limit()

        params['apikey'] = self.api_key

        try:
            text = fetch_with_retry(
                BASE_URL,
                params=params,
                retries=3,
                backoff=2.0,
                timeout=30.0,
            )
            data = json.loads(text)

            # Check for API errors
            if 'Error Message' in data:
                logger.error(f"API Error: {data['Error Message']}")
                return {}

            if 'Note' in data:
                note = data['Note']
                logger.warning(f"API Note: {note}")
                # Check if this is a daily limit (vs per-minute limit)
                if '500 calls per day' in note or 'daily' in note.lower():
                    raise DailyLimitExceeded(f"Alpha Vantage daily limit reached: {note}")
                return {}

            return data

        except FetchError as e:
            logger.error(f"Request failed after retries: {e}")
            return {}
        except json.JSONDecodeError as e:
            logger.error(f"JSON parse error: {e}")
            return {}

    def get_company_overview(self, symbol: str) -> Dict:
        """
        Get company overview including fundamental data.
        Returns: MarketCap, EBITDA, PE Ratio, PEG Ratio, etc.
        """
        params = {
            'function': 'OVERVIEW',
            'symbol': symbol
        }
        logger.info(f"Fetching company overview for {symbol}")
        return self._make_request(params)

    def get_income_statement(self, symbol: str) -> Dict:
        """
        Get annual and quarterly income statements.
        Returns: Revenue, NetIncome, EPS, etc.
        """
        params = {
            'function': 'INCOME_STATEMENT',
            'symbol': symbol
        }
        logger.info(f"Fetching income statement for {symbol}")
        return self._make_request(params)

    def get_balance_sheet(self, symbol: str) -> Dict:
        """
        Get annual and quarterly balance sheets.
        Returns: Assets, Liabilities, Equity, etc.
        """
        params = {
            'function': 'BALANCE_SHEET',
            'symbol': symbol
        }
        logger.info(f"Fetching balance sheet for {symbol}")
        return self._make_request(params)

    def get_cash_flow(self, symbol: str) -> Dict:
        """
        Get annual and quarterly cash flow statements.
        Returns: Operating, Investing, Financing cash flows
        """
        params = {
            'function': 'CASH_FLOW',
            'symbol': symbol
        }
        logger.info(f"Fetching cash flow for {symbol}")
        return self._make_request(params)

    def get_earnings(self, symbol: str) -> Dict:
        """
        Get quarterly and annual earnings (EPS).
        Returns: Reported EPS, Estimated EPS, Surprise %
        """
        params = {
            'function': 'EARNINGS',
            'symbol': symbol
        }
        logger.info(f"Fetching earnings for {symbol}")
        return self._make_request(params)

    def get_all_fundamentals(self, symbol: str) -> Dict:
        """
        Fetch all fundamental data for a symbol.
        WARNING: Makes 5 API calls, which is the entire free tier minute limit!
        """
        logger.info(f"Fetching ALL fundamental data for {symbol}")

        return {
            'overview': self.get_company_overview(symbol),
            'income_statement': self.get_income_statement(symbol),
            'balance_sheet': self.get_balance_sheet(symbol),
            'cash_flow': self.get_cash_flow(symbol),
            'earnings': self.get_earnings(symbol)
        }


def test_client():
    """Test the Alpha Vantage client"""
    client = AlphaVantageClient()

    # Test with a well-known stock
    symbol = 'AAPL'

    print(f"\n{'='*60}")
    print(f"Testing Alpha Vantage API with {symbol}")
    print(f"{'='*60}\n")

    # Get company overview
    overview = client.get_company_overview(symbol)
    if overview:
        print(f"Company: {overview.get('Name', 'N/A')}")
        print(f"Sector: {overview.get('Sector', 'N/A')}")
        print(f"Market Cap: ${overview.get('MarketCapitalization', 'N/A')}")
        print(f"P/E Ratio: {overview.get('PERatio', 'N/A')}")
        print(f"EPS: ${overview.get('EPS', 'N/A')}")

    # Get earnings
    earnings = client.get_earnings(symbol)
    if earnings and 'quarterlyEarnings' in earnings:
        latest = earnings['quarterlyEarnings'][0]
        print(f"\nLatest Quarterly Earnings:")
        print(f"  Date: {latest.get('fiscalDateEnding', 'N/A')}")
        print(f"  Reported EPS: ${latest.get('reportedEPS', 'N/A')}")
        print(f"  Estimated EPS: ${latest.get('estimatedEPS', 'N/A')}")
        print(f"  Surprise: {latest.get('surprise', 'N/A')}")


if __name__ == '__main__':
    test_client()
