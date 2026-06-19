"""
Fetch and store fundamental data from Alpha Vantage.
Usage:
  python fetch_fundamentals.py AAPL MSFT TSLA         # Fetch for specific tickers
  python fetch_fundamentals.py --all                  # Fetch for all tickers in database
  python fetch_fundamentals.py --refresh              # Only refresh stale data (default 90 days)
  python fetch_fundamentals.py --refresh --days 30    # Custom staleness threshold
  python fetch_fundamentals.py --priority             # Refresh priority tickers only
"""

import sys
import sqlite3
import logging
import argparse
from datetime import datetime, timedelta
from typing import Optional, Tuple, Dict, List
from alpha_vantage_fetcher import AlphaVantageClient, DailyLimitExceeded
from constants import DB_PATH

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Priority tickers to refresh more frequently (top 20)
PRIORITY_TICKERS = [
    'AAPL', 'MSFT', 'NVDA', 'GOOG', 'AMZN', 'META', 'TSLA', 'AMD', 'AVGO', 'TSM',
    'COIN', 'DDOG', 'MELI', 'PLTR', 'QCOM', 'RBLX', 'SHOP', 'SNOW', 'SOFI', 'UBER'
]

# Extended coverage - well-known stocks worth tracking (100 more)
EXTENDED_TICKERS = [
    # Mega caps
    'BRK-B', 'V', 'MA', 'JNJ', 'WMT', 'JPM', 'PG', 'UNH', 'HD', 'BAC',
    'XOM', 'CVX', 'PFE', 'ABBV', 'KO', 'PEP', 'MRK', 'COST', 'TMO', 'CSCO',
    # Tech & Growth
    'NFLX', 'ADBE', 'CRM', 'ORCL', 'INTC', 'IBM', 'NOW', 'INTU', 'PANW', 'CRWD',
    'NET', 'MDB', 'ABNB', 'SQ', 'PYPL', 'ANET', 'GTLB', 'ZS', 'OKTA', 'SPOT',
    # Financials
    'GS', 'MS', 'C', 'WFC', 'BLK', 'SCHW', 'AXP', 'CME', 'ICE', 'SPGI',
    # Healthcare
    'LLY', 'ABT', 'BMY', 'AMGN', 'GILD', 'ISRG', 'VRTX', 'REGN', 'MDT', 'DHR',
    # Industrial & Energy
    'CAT', 'DE', 'HON', 'UNP', 'UPS', 'BA', 'LMT', 'RTX', 'GE', 'SLB',
    # Consumer
    'DIS', 'NKE', 'SBUX', 'MCD', 'LOW', 'TGT', 'TJX', 'LULU', 'CMG', 'YUM',
    # EV & Clean Energy
    'RIVN', 'LCID', 'NIO', 'LI', 'ENPH', 'FSLR', 'RUN', 'SEDG', 'PLUG', 'BE',
    # Semiconductors
    'MU', 'LRCX', 'KLAC', 'MRVL', 'ON', 'NXPI', 'ADI', 'TXN', 'ASML', 'ARM',
]


def get_current_fiscal_quarter() -> Tuple[int, int]:
    """
    Get the most recently completed fiscal quarter.
    Returns (year, quarter) e.g., (2025, 3) for Q3 2025.

    Most companies report ~45 days after quarter end, so we look back 45 days.
    """
    today = datetime.now()
    # Look back 45 days to find the quarter that should have reported by now
    report_date = today - timedelta(days=45)

    quarter = (report_date.month - 1) // 3 + 1
    year = report_date.year

    return year, quarter


def quarter_end_date(year: int, quarter: int) -> str:
    """Get the last day of a fiscal quarter as string YYYY-MM-DD"""
    quarter_ends = {1: '03-31', 2: '06-30', 3: '09-30', 4: '12-31'}
    return f"{year}-{quarter_ends[quarter]}"


def get_ticker_freshness(ticker: str, conn: sqlite3.Connection) -> Dict:
    """
    Check how fresh a ticker's data is across all tables.
    Returns dict with last_updated timestamps and latest fiscal dates.
    """
    cursor = conn.cursor()
    result = {
        'has_data': False,
        'overview_updated': None,
        'market_cap': None,
        'earnings_updated': None,
        'latest_earnings_quarter': None,
        'income_updated': None,
        'latest_income_quarter': None,
    }

    # Check company_overview (also fetch market_cap to detect placeholder data)
    cursor.execute(
        "SELECT last_updated, market_cap FROM company_overview WHERE ticker = ?", (ticker,)
    )
    row = cursor.fetchone()
    if row:
        result['has_data'] = True
        result['overview_updated'] = row[0]
        result['market_cap'] = row[1]

    # Check earnings_quarterly - get both last_updated and latest fiscal date
    cursor.execute("""
        SELECT MAX(last_updated), MAX(fiscal_date_ending)
        FROM earnings_quarterly WHERE ticker = ?
    """, (ticker,))
    row = cursor.fetchone()
    if row and row[0]:
        result['earnings_updated'] = row[0]
        result['latest_earnings_quarter'] = row[1]

    # Check income_statement_quarterly
    cursor.execute("""
        SELECT MAX(last_updated), MAX(fiscal_date_ending)
        FROM income_statement_quarterly WHERE ticker = ?
    """, (ticker,))
    row = cursor.fetchone()
    if row and row[0]:
        result['income_updated'] = row[0]
        result['latest_income_quarter'] = row[1]

    return result


def needs_refresh(ticker: str, conn: sqlite3.Connection,
                  max_age_days: int = 90,
                  is_priority: bool = False) -> Tuple[bool, str]:
    """
    Determine if a ticker needs to be refreshed.

    Args:
        ticker: The ticker symbol
        conn: Database connection
        max_age_days: Max age before data is considered stale (default 90)
        is_priority: If True, use shorter threshold (14 days) to catch new earnings faster

    Returns:
        (needs_refresh: bool, reason: str)

    Refresh reasons:
        - 'no_data': Ticker has no fundamental data
        - 'placeholder': Data exists but has placeholder values (market_cap = 0)
        - 'stale': Data is older than max_age_days
        - 'priority_stale': Priority ticker data older than 14 days (may have new earnings)
        - 'missing_quarter': Latest expected quarter is missing
        - 'fresh': Data is up to date (no refresh needed)
    """
    freshness = get_ticker_freshness(ticker, conn)

    # No data at all - needs full fetch
    if not freshness['has_data']:
        return True, 'no_data'

    # Check if data has placeholder values (market_cap = 0 or None)
    # This detects rows inserted with default/empty values that need real data
    market_cap = freshness.get('market_cap')
    if market_cap is None or market_cap == 0:
        return True, 'placeholder (market_cap = 0)'

    # Check if data is stale based on last_updated
    if freshness['overview_updated']:
        try:
            last_updated = datetime.fromisoformat(freshness['overview_updated'].replace('Z', '+00:00'))
            if isinstance(last_updated, datetime):
                # Handle timezone-naive comparison
                last_updated = last_updated.replace(tzinfo=None)
            age_days = (datetime.now() - last_updated).days

            # Priority tickers use shorter threshold to catch new earnings faster
            # (companies report quarterly, so 14 days ensures we catch updates)
            if is_priority and age_days > 14:
                return True, f'priority_stale ({age_days} days old, priority threshold: 14 days)'

            if age_days > max_age_days:
                return True, f'stale ({age_days} days old)'
        except (ValueError, TypeError):
            pass

    # Check if we're missing the most recent expected quarter
    current_year, current_quarter = get_current_fiscal_quarter()
    expected_quarter_end = quarter_end_date(current_year, current_quarter)

    if freshness['latest_earnings_quarter']:
        if freshness['latest_earnings_quarter'] < expected_quarter_end:
            return True, f"missing_quarter (have {freshness['latest_earnings_quarter']}, expect {expected_quarter_end})"

    return False, 'fresh'


def check_all_tickers_freshness(conn: sqlite3.Connection,
                                 max_age_days: int = 90) -> Dict[str, List[str]]:
    """
    Check freshness of all tickers with existing data.
    Returns dict categorizing tickers by refresh status.
    """
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT ticker FROM company_overview")
    tickers = [row[0] for row in cursor.fetchall()]

    result = {'fresh': [], 'stale': [], 'priority_stale': [], 'missing_quarter': [], 'placeholder': [], 'no_data': []}

    for ticker in tickers:
        # Check with priority flag for tickers in PRIORITY_TICKERS
        is_priority = ticker in PRIORITY_TICKERS
        needs, reason = needs_refresh(ticker, conn, max_age_days, is_priority=is_priority)
        if not needs:
            result['fresh'].append(ticker)
        elif 'priority_stale' in reason:
            result['priority_stale'].append(ticker)
        elif 'stale' in reason:
            result['stale'].append(ticker)
        elif 'missing_quarter' in reason:
            result['missing_quarter'].append(ticker)
        elif 'placeholder' in reason:
            result['placeholder'].append(ticker)
        else:
            result['no_data'].append(ticker)

    return result


def safe_float(value, default=0.0):
    """Safely convert value to float, handling None, 'None', empty strings, etc."""
    if value is None or value == '' or value == 'None':
        return default
    try:
        return float(value)
    except (ValueError, TypeError):
        return default


def store_company_overview(ticker: str, data: dict, conn: sqlite3.Connection):
    """Store company overview data"""
    if not data:
        logger.warning(f"No overview data for {ticker}")
        return

    cursor = conn.cursor()

    # Map API fields to database columns
    cursor.execute('''
        INSERT OR REPLACE INTO company_overview (
            ticker, name, description, sector, industry,
            market_cap, pe_ratio, peg_ratio, eps, dividend_yield, beta,
            week_52_high, week_52_low, moving_avg_50, moving_avg_200,
            shares_outstanding, profit_margin, operating_margin,
            return_on_assets, return_on_equity, revenue, revenue_per_share,
            quarterly_revenue_growth, gross_profit, ebitda, diluted_eps,
            quarterly_earnings_growth, analyst_target_price,
            trailing_pe, forward_pe, price_to_sales, price_to_book,
            ev_to_revenue, ev_to_ebitda
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        ticker,
        data.get('Name'),
        data.get('Description'),
        data.get('Sector'),
        data.get('Industry'),
        safe_float(data.get('MarketCapitalization')),
        safe_float(data.get('PERatio')),
        safe_float(data.get('PEGRatio')),
        safe_float(data.get('EPS')),
        safe_float(data.get('DividendYield')),
        safe_float(data.get('Beta')),
        safe_float(data.get('52WeekHigh')),
        safe_float(data.get('52WeekLow')),
        safe_float(data.get('50DayMovingAverage')),
        safe_float(data.get('200DayMovingAverage')),
        safe_float(data.get('SharesOutstanding')),
        safe_float(data.get('ProfitMargin')),
        safe_float(data.get('OperatingMarginTTM')),
        safe_float(data.get('ReturnOnAssetsTTM')),
        safe_float(data.get('ReturnOnEquityTTM')),
        safe_float(data.get('RevenueTTM')),
        safe_float(data.get('RevenuePerShareTTM')),
        safe_float(data.get('QuarterlyRevenueGrowthYOY')),
        safe_float(data.get('GrossProfitTTM')),
        safe_float(data.get('EBITDA')),
        safe_float(data.get('DilutedEPSTTM')),
        safe_float(data.get('QuarterlyEarningsGrowthYOY')),
        safe_float(data.get('AnalystTargetPrice')),
        safe_float(data.get('TrailingPE')),
        safe_float(data.get('ForwardPE')),
        safe_float(data.get('PriceToSalesRatioTTM')),
        safe_float(data.get('PriceToBookRatio')),
        safe_float(data.get('EVToRevenue')),
        safe_float(data.get('EVToEBITDA')),
    ))

    conn.commit()
    logger.info(f"✓ Stored overview for {ticker}")


def store_earnings(ticker: str, data: dict, conn: sqlite3.Connection):
    """Store earnings data (quarterly and annual)"""
    if not data:
        logger.warning(f"No earnings data for {ticker}")
        return

    cursor = conn.cursor()

    # Quarterly earnings
    if 'quarterlyEarnings' in data:
        for earning in data['quarterlyEarnings']:
            cursor.execute('''
                INSERT OR REPLACE INTO earnings_quarterly (
                    ticker, fiscal_date_ending, reported_date, reported_eps,
                    estimated_eps, surprise, surprise_percentage
                ) VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (
                ticker,
                earning.get('fiscalDateEnding'),
                earning.get('reportedDate'),
                safe_float(earning.get('reportedEPS')),
                safe_float(earning.get('estimatedEPS')),
                safe_float(earning.get('surprise')),
                safe_float(earning.get('surprisePercentage')),
            ))

    # Annual earnings
    if 'annualEarnings' in data:
        for earning in data['annualEarnings']:
            cursor.execute('''
                INSERT OR REPLACE INTO earnings_annual (
                    ticker, fiscal_date_ending, reported_eps
                ) VALUES (?, ?, ?)
            ''', (
                ticker,
                earning.get('fiscalDateEnding'),
                safe_float(earning.get('reportedEPS')),
            ))

    conn.commit()
    logger.info(f"✓ Stored earnings for {ticker}")


def store_income_statement(ticker: str, data: dict, conn: sqlite3.Connection):
    """Store income statement data"""
    if not data:
        logger.warning(f"No income statement data for {ticker}")
        return

    cursor = conn.cursor()

    # Quarterly
    if 'quarterlyReports' in data:
        for report in data['quarterlyReports']:
            cursor.execute('''
                INSERT OR REPLACE INTO income_statement_quarterly (
                    ticker, fiscal_date_ending, total_revenue, cost_of_revenue,
                    gross_profit, operating_expenses, operating_income, ebitda, net_income, eps
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                ticker,
                report.get('fiscalDateEnding'),
                safe_float(report.get('totalRevenue')),
                safe_float(report.get('costOfRevenue')),
                safe_float(report.get('grossProfit')),
                safe_float(report.get('operatingExpenses')),
                safe_float(report.get('operatingIncome')),
                safe_float(report.get('ebitda')),
                safe_float(report.get('netIncome')),
                safe_float(report.get('reportedEPS')),
            ))

    # Annual
    if 'annualReports' in data:
        for report in data['annualReports']:
            cursor.execute('''
                INSERT OR REPLACE INTO income_statement_annual (
                    ticker, fiscal_date_ending, total_revenue, cost_of_revenue,
                    gross_profit, operating_expenses, operating_income, ebitda, net_income, eps
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                ticker,
                report.get('fiscalDateEnding'),
                safe_float(report.get('totalRevenue')),
                safe_float(report.get('costOfRevenue')),
                safe_float(report.get('grossProfit')),
                safe_float(report.get('operatingExpenses')),
                safe_float(report.get('operatingIncome')),
                safe_float(report.get('ebitda')),
                safe_float(report.get('netIncome')),
                safe_float(report.get('reportedEPS')),
            ))

    conn.commit()
    logger.info(f"✓ Stored income statement for {ticker}")


def store_balance_sheet(ticker: str, data: dict, conn: sqlite3.Connection):
    """Store balance sheet data"""
    if not data:
        logger.warning(f"No balance sheet data for {ticker}")
        return

    cursor = conn.cursor()

    # Quarterly
    if 'quarterlyReports' in data:
        for report in data['quarterlyReports']:
            cursor.execute('''
                INSERT OR REPLACE INTO balance_sheet_quarterly (
                    ticker, fiscal_date_ending, total_assets, total_current_assets,
                    cash_and_equivalents, total_liabilities, total_current_liabilities,
                    total_shareholder_equity, retained_earnings, common_stock
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                ticker,
                report.get('fiscalDateEnding'),
                safe_float(report.get('totalAssets')),
                safe_float(report.get('totalCurrentAssets')),
                safe_float(report.get('cashAndCashEquivalentsAtCarryingValue')),
                safe_float(report.get('totalLiabilities')),
                safe_float(report.get('totalCurrentLiabilities')),
                safe_float(report.get('totalShareholderEquity')),
                safe_float(report.get('retainedEarnings')),
                safe_float(report.get('commonStock')),
            ))

    # Annual
    if 'annualReports' in data:
        for report in data['annualReports']:
            cursor.execute('''
                INSERT OR REPLACE INTO balance_sheet_annual (
                    ticker, fiscal_date_ending, total_assets, total_current_assets,
                    cash_and_equivalents, total_liabilities, total_current_liabilities,
                    total_shareholder_equity, retained_earnings, common_stock
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                ticker,
                report.get('fiscalDateEnding'),
                safe_float(report.get('totalAssets')),
                safe_float(report.get('totalCurrentAssets')),
                safe_float(report.get('cashAndCashEquivalentsAtCarryingValue')),
                safe_float(report.get('totalLiabilities')),
                safe_float(report.get('totalCurrentLiabilities')),
                safe_float(report.get('totalShareholderEquity')),
                safe_float(report.get('retainedEarnings')),
                safe_float(report.get('commonStock')),
            ))

    conn.commit()
    logger.info(f"✓ Stored balance sheet for {ticker}")


def store_cash_flow(ticker: str, data: dict, conn: sqlite3.Connection):
    """Store cash flow data"""
    if not data:
        logger.warning(f"No cash flow data for {ticker}")
        return

    cursor = conn.cursor()

    # Quarterly
    if 'quarterlyReports' in data:
        for report in data['quarterlyReports']:
            operating_cf = safe_float(report.get('operatingCashflow'))
            capex = safe_float(report.get('capitalExpenditures'))
            free_cf = operating_cf - abs(capex)  # FCF = Operating CF - CapEx

            cursor.execute('''
                INSERT OR REPLACE INTO cash_flow_quarterly (
                    ticker, fiscal_date_ending, operating_cashflow,
                    capital_expenditures, free_cash_flow, dividend_payout
                ) VALUES (?, ?, ?, ?, ?, ?)
            ''', (
                ticker,
                report.get('fiscalDateEnding'),
                operating_cf,
                capex,
                free_cf,
                safe_float(report.get('dividendPayout')),
            ))

    # Annual
    if 'annualReports' in data:
        for report in data['annualReports']:
            operating_cf = safe_float(report.get('operatingCashflow'))
            capex = safe_float(report.get('capitalExpenditures'))
            free_cf = operating_cf - abs(capex)

            cursor.execute('''
                INSERT OR REPLACE INTO cash_flow_annual (
                    ticker, fiscal_date_ending, operating_cashflow,
                    capital_expenditures, free_cash_flow, dividend_payout
                ) VALUES (?, ?, ?, ?, ?, ?)
            ''', (
                ticker,
                report.get('fiscalDateEnding'),
                operating_cf,
                capex,
                free_cf,
                safe_float(report.get('dividendPayout')),
            ))

    conn.commit()
    logger.info(f"✓ Stored cash flow for {ticker}")


def fetch_and_store_ticker(ticker: str, client: AlphaVantageClient, conn: sqlite3.Connection):
    """Fetch all fundamental data for a ticker and store in database"""
    logger.info(f"\n{'='*60}")
    logger.info(f"Fetching fundamentals for {ticker}")
    logger.info(f"{'='*60}")

    try:
        # Get all fundamental data (WARNING: 5 API calls!)
        data = client.get_all_fundamentals(ticker)

        # Store each type
        store_company_overview(ticker, data.get('overview', {}), conn)
        store_earnings(ticker, data.get('earnings', {}), conn)
        store_income_statement(ticker, data.get('income_statement', {}), conn)
        store_balance_sheet(ticker, data.get('balance_sheet', {}), conn)
        store_cash_flow(ticker, data.get('cash_flow', {}), conn)

        logger.info(f"✓ Successfully stored all fundamental data for {ticker}")

    except Exception as e:
        logger.error(f"Failed to fetch/store fundamentals for {ticker}: {e}")


def get_all_tickers_from_db():
    """Get list of all unique tickers from the database"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Get tickers from metadata table
    cursor.execute("SELECT DISTINCT ticker FROM ticker_metadata ORDER BY ticker")
    tickers = [row[0] for row in cursor.fetchall()]

    conn.close()
    return tickers


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description='Fetch fundamental data from Alpha Vantage',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python fetch_fundamentals.py AAPL MSFT TSLA       # Fetch specific tickers
  python fetch_fundamentals.py --refresh --priority # Refresh stale priority tickers
  python fetch_fundamentals.py --extended           # Fetch 100 well-known stocks
  python fetch_fundamentals.py --priority --extended # All 120 tracked stocks
  python fetch_fundamentals.py --status             # Show data freshness report
        """
    )

    parser.add_argument('tickers', nargs='*', help='Ticker symbols to fetch')
    parser.add_argument('--all', action='store_true',
                        help='Fetch for all tickers in database')
    parser.add_argument('--refresh', action='store_true',
                        help='Only refresh stale data (skip fresh tickers)')
    parser.add_argument('--priority', action='store_true',
                        help='Only refresh priority tickers (top 20)')
    parser.add_argument('--extended', action='store_true',
                        help='Include extended tickers (100 more well-known stocks)')
    parser.add_argument('--days', type=int, default=90,
                        help='Max age in days before data is considered stale (default: 90)')
    parser.add_argument('--status', action='store_true',
                        help='Show freshness status without fetching')
    parser.add_argument('--force', action='store_true',
                        help='Force refresh even if data is fresh')
    parser.add_argument('--limit', type=int, default=None,
                        help='Limit number of tickers to process (for daily quota management)')

    args = parser.parse_args()

    conn = sqlite3.connect(DB_PATH)

    # Status mode - just show freshness report
    if args.status:
        logger.info("Checking data freshness...")
        freshness = check_all_tickers_freshness(conn, args.days)
        current_year, current_quarter = get_current_fiscal_quarter()

        print(f"\n{'='*60}")
        print(f"FUNDAMENTAL DATA FRESHNESS REPORT")
        print(f"Expected quarter: Q{current_quarter} {current_year} ({quarter_end_date(current_year, current_quarter)})")
        print(f"Staleness threshold: {args.days} days (priority tickers: 14 days)")
        print(f"{'='*60}\n")

        print(f"[OK]     Fresh:            {len(freshness['fresh'])} tickers")
        print(f"[PRIO]   Priority stale:   {len(freshness['priority_stale'])} tickers (>14 days old)")
        print(f"[STALE]  Stale:            {len(freshness['stale'])} tickers (>{args.days} days old)")
        print(f"[MISS]   Missing quarter:  {len(freshness['missing_quarter'])} tickers")
        print(f"[EMPTY]  Placeholder:      {len(freshness['placeholder'])} tickers")
        print(f"[NONE]   No data:          {len(freshness['no_data'])} tickers")

        if freshness['priority_stale']:
            print(f"\nPriority tickers need refresh (>14 days): {', '.join(freshness['priority_stale'][:20])}")
            if len(freshness['priority_stale']) > 20:
                print(f"  ... and {len(freshness['priority_stale']) - 20} more")

        if freshness['stale']:
            print(f"\nStale tickers (>{args.days} days): {', '.join(freshness['stale'][:20])}")
            if len(freshness['stale']) > 20:
                print(f"  ... and {len(freshness['stale']) - 20} more")

        if freshness['missing_quarter']:
            print(f"\nMissing current quarter: {', '.join(freshness['missing_quarter'][:20])}")
            if len(freshness['missing_quarter']) > 20:
                print(f"  ... and {len(freshness['missing_quarter']) - 20} more")

        if freshness['placeholder']:
            print(f"\nPlaceholder data (market_cap = 0): {', '.join(freshness['placeholder'][:20])}")
            if len(freshness['placeholder']) > 20:
                print(f"  ... and {len(freshness['placeholder']) - 20} more")

        needs_refresh_count = len(freshness['priority_stale']) + len(freshness['stale']) + len(freshness['missing_quarter']) + len(freshness['placeholder'])
        api_calls_needed = needs_refresh_count * 5
        print(f"\n{'='*60}")
        print(f"To refresh all stale data: {needs_refresh_count} tickers x 5 calls = {api_calls_needed} API calls")
        print(f"Free tier daily limit: 500 calls")
        print(f"{'='*60}")

        conn.close()
        return

    # Determine which tickers to fetch
    if args.priority and args.extended:
        tickers = list(set(PRIORITY_TICKERS + EXTENDED_TICKERS))
        logger.info(f"Processing {len(tickers)} tickers (priority + extended)")
    elif args.priority:
        tickers = PRIORITY_TICKERS
        logger.info(f"Processing {len(tickers)} priority tickers")
    elif args.extended:
        tickers = EXTENDED_TICKERS
        logger.info(f"Processing {len(tickers)} extended tickers")
    elif args.all:
        tickers = get_all_tickers_from_db()
        logger.info(f"Processing ALL {len(tickers)} tickers in database")
    elif args.tickers:
        tickers = [t.strip().upper() for t in args.tickers]
        logger.info(f"Processing {len(tickers)} tickers: {', '.join(tickers)}")
    else:
        parser.print_help()
        conn.close()
        return

    # Filter to only stale tickers if --refresh mode
    if args.refresh and not args.force:
        logger.info(f"Checking which tickers need refresh (threshold: {args.days} days, priority: 14 days)...")
        tickers_to_fetch = []
        skipped = []

        for ticker in tickers:
            # Priority tickers use shorter threshold (14 days) to catch new earnings
            is_priority = ticker in PRIORITY_TICKERS
            needs, reason = needs_refresh(ticker, conn, args.days, is_priority=is_priority)
            if needs:
                tickers_to_fetch.append((ticker, reason))
            else:
                skipped.append(ticker)

        if skipped:
            logger.info(f"Skipping {len(skipped)} fresh tickers: {', '.join(skipped[:10])}")
            if len(skipped) > 10:
                logger.info(f"  ... and {len(skipped) - 10} more")

        if not tickers_to_fetch:
            logger.info("All tickers are fresh! Nothing to refresh.")
            conn.close()
            return

        logger.info(f"\nWill refresh {len(tickers_to_fetch)} tickers:")
        for ticker, reason in tickers_to_fetch[:10]:
            logger.info(f"  {ticker}: {reason}")
        if len(tickers_to_fetch) > 10:
            logger.info(f"  ... and {len(tickers_to_fetch) - 10} more")

        tickers = [t[0] for t in tickers_to_fetch]

    # Apply limit if specified
    if args.limit and len(tickers) > args.limit:
        logger.info(f"Limiting to {args.limit} tickers (of {len(tickers)} total)")
        tickers = tickers[:args.limit]

    # Calculate API calls
    total_calls = len(tickers) * 5
    logger.info(f"\n{'='*60}")
    logger.info(f"API USAGE ESTIMATE")
    logger.info(f"{'='*60}")
    logger.info(f"Tickers to process: {len(tickers)}")
    logger.info(f"API calls needed:   {total_calls}")
    logger.info(f"Free tier limit:    500/day, 5/minute")

    if total_calls > 500:
        logger.warning(f"WARNING: This exceeds the daily free tier limit!")
        logger.warning(f"Consider using --limit {500 // 5} to stay within quota")

    if not args.force and len(tickers) > 10:
        confirm = input(f"\nProceed with {len(tickers)} tickers ({total_calls} API calls)? (yes/no): ")
        if confirm.lower() != 'yes':
            logger.info("Aborted")
            conn.close()
            return

    # Initialize client
    client = AlphaVantageClient()

    # Track stats
    success_count = 0
    fail_count = 0
    stopped_early = False

    # Fetch and store each ticker
    for i, ticker in enumerate(tickers, 1):
        logger.info(f"\nProgress: {i}/{len(tickers)} (API calls: {i*5}/{total_calls})")
        try:
            fetch_and_store_ticker(ticker, client, conn)
            success_count += 1
        except DailyLimitExceeded as e:
            logger.error(f"\n{'='*60}")
            logger.error(f"DAILY LIMIT REACHED - STOPPING")
            logger.error(f"{'='*60}")
            logger.error(f"{e}")
            logger.error(f"Completed {success_count} tickers before limit. Try again tomorrow.")
            stopped_early = True
            break
        except Exception as e:
            logger.error(f"Failed {ticker}: {e}")
            fail_count += 1

    conn.close()

    logger.info(f"\n{'='*60}")
    logger.info(f"COMPLETED" if not stopped_early else "STOPPED (daily limit)")
    logger.info(f"{'='*60}")
    logger.info(f"Success: {success_count}")
    logger.info(f"Failed:  {fail_count}")
    logger.info(f"API calls used: ~{success_count * 5}")
    if stopped_early:
        remaining = len(tickers) - success_count - fail_count
        logger.info(f"Remaining: {remaining} tickers (try again tomorrow)")


if __name__ == '__main__':
    main()
