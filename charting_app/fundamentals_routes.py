"""
Fundamentals API routes.
Routes: /api/revenue, /api/fundamentals/overview, /api/fundamentals/earnings,
        /api/fundamentals/income, /api/fundamentals/balance, /api/fundamentals/cashflow,
        /api/fundamentals/chart
"""
import logging
import sys
import os
from datetime import datetime

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Blueprint, jsonify, request
import pandas as pd
from constants import (get_db_connection, HTTP_BAD_REQUEST, resolve_ticker_alias)

logger = logging.getLogger(__name__)

fundamentals_bp = Blueprint('fundamentals', __name__)


@fundamentals_bp.route('/api/revenue')
def api_revenue():
    """
    Fetch quarterly revenue data for requested tickers.
    Query params: ?tickers=AAPL,MSFT,TSLA
    Returns: { "AAPL": [{time: unix_ts, value: revenue}, ...], "MSFT": [...], ... }

    DB-first: queries income_statement_quarterly.total_revenue.
    Falls back to Alpha Vantage (if API key available), then yfinance if DB is empty.
    """
    import yfinance as yf

    ticker_param = request.args.get('tickers', '')
    if not ticker_param:
        return jsonify({'error': 'No tickers provided'}), HTTP_BAD_REQUEST

    tickers = [t.strip().upper() for t in ticker_param.split(',') if t.strip()]
    if not tickers:
        return jsonify({'error': 'No valid tickers'}), HTTP_BAD_REQUEST

    # Resolve ticker aliases (e.g., GOOGL -> GOOG for fundamentals)
    # Keep mapping to return data under original requested ticker
    alias_map = {}  # original -> canonical
    canonical_tickers = []
    for t in tickers:
        canonical = resolve_ticker_alias(t)
        if canonical != t:
            alias_map[t] = canonical
            logger.info(f"/api/revenue: aliased {t} -> {canonical}")
        canonical_tickers.append(canonical)

    # Dedupe canonical tickers (e.g., if user requests both GOOG and GOOGL)
    unique_canonical = list(dict.fromkeys(canonical_tickers))

    logger.info(f"/api/revenue: requested tickers={tickers}, canonical={unique_canonical}")

    # Check for Alpha Vantage API key (accept both env var names, prefer ALPHA_VANTAGE_API_KEY)
    alpha_vantage_key = os.environ.get('ALPHA_VANTAGE_API_KEY') or os.environ.get('ALPHAVANTAGE_API_KEY')
    use_alpha_vantage = alpha_vantage_key is not None

    result = {}

    def fetch_all_from_db(symbols):
        """Batch fetch quarterly revenue from local database for all tickers at once"""
        db_results = {s: None for s in symbols}
        try:
            conn = get_db_connection()
            placeholders = ','.join('?' * len(symbols))
            query = f"""
                SELECT ticker, fiscal_date_ending, total_revenue
                FROM income_statement_quarterly
                WHERE ticker IN ({placeholders})
                ORDER BY ticker, fiscal_date_ending ASC
            """
            df = pd.read_sql(query, conn, params=symbols)
            conn.close()

            if df.empty:
                return db_results

            # Group by ticker
            for ticker in symbols:
                ticker_df = df[df['ticker'] == ticker]
                if ticker_df.empty:
                    continue

                data_points = []
                for _, row in ticker_df.iterrows():
                    try:
                        date = pd.to_datetime(row['fiscal_date_ending'])
                        unix_ts = int(date.timestamp())
                        value = row['total_revenue']
                        if pd.notna(value) and value != 0:
                            data_points.append({'time': unix_ts, 'value': float(value)})
                    except Exception as e:
                        logger.warning(f"/api/revenue: Error parsing DB row for {ticker}: {e}")
                        continue

                if data_points:
                    db_results[ticker] = data_points
                    logger.info(f"/api/revenue: {ticker} returned {len(data_points)} quarters from DB")

            return db_results

        except Exception as e:
            logger.error(f"/api/revenue: DB batch error: {e}")
            return db_results

    # Lazy-initialize Alpha Vantage client (reuses hardened client with proper rate limiting)
    av_client = None
    if use_alpha_vantage:
        try:
            from alpha_vantage_fetcher import AlphaVantageClient
            av_client = AlphaVantageClient(api_key=alpha_vantage_key)
        except Exception as e:
            logger.warning(f"/api/revenue: Could not initialize AlphaVantageClient: {e}")

    def fetch_from_alpha_vantage(symbol):
        """Fetch quarterly revenue from Alpha Vantage using hardened client (12s rate limit + retry)"""
        if not av_client:
            return None

        try:
            # Use the hardened client which handles rate limiting and retries
            data = av_client.get_income_statement(symbol)

            if not data:
                logger.warning(f"/api/revenue: No data from Alpha Vantage for {symbol}")
                return None

            quarterly_reports = data.get('quarterlyReports', [])
            if not quarterly_reports:
                logger.warning(f"/api/revenue: No quarterly reports from Alpha Vantage for {symbol}")
                return None

            data_points = []
            for report in quarterly_reports:
                try:
                    fiscal_date = report.get('fiscalDateEnding')  # YYYY-MM-DD string
                    total_revenue = report.get('totalRevenue')

                    if not fiscal_date or not total_revenue:
                        continue

                    # Parse date string (YYYY-MM-DD)
                    date_obj = datetime.strptime(fiscal_date, '%Y-%m-%d')
                    unix_ts = int(date_obj.timestamp())
                    revenue_val = float(total_revenue)

                    # Include original date string for DB persistence (avoids timezone edge cases)
                    data_points.append({'time': unix_ts, 'value': revenue_val, 'date': fiscal_date})
                except (ValueError, TypeError) as e:
                    logger.warning(f"/api/revenue: Error parsing Alpha Vantage data for {symbol}: {e}")
                    continue

            # Sort by time (oldest first)
            data_points.sort(key=lambda x: x['time'])
            logger.info(f"/api/revenue: {symbol} returned {len(data_points)} quarters from Alpha Vantage")
            return data_points

        except Exception as e:
            logger.error(f"/api/revenue: Alpha Vantage error for {symbol}: {e}")
            return None

    def fetch_from_yfinance(symbol):
        """Fetch quarterly revenue from yfinance (last 5 quarters only)"""
        try:
            ticker = yf.Ticker(symbol)
            quarterly = ticker.quarterly_financials

            if quarterly is None or quarterly.empty:
                logger.warning(f"/api/revenue: No financials from yfinance for {symbol}")
                return []

            if 'Total Revenue' not in quarterly.index:
                logger.warning(f"/api/revenue: No Total Revenue from yfinance for {symbol}")
                return []

            revenue_series = quarterly.loc['Total Revenue']

            # Convert to list of {time, value} dicts
            data_points = []
            for date, value in revenue_series.items():
                try:
                    # Convert pandas timestamp to unix timestamp
                    unix_ts = int(date.timestamp())
                    # Extract date string (YYYY-MM-DD) for DB persistence
                    date_str = date.strftime('%Y-%m-%d')
                    # Convert value to float, handle None/NaN
                    revenue_val = float(value) if pd.notna(value) else None
                    if revenue_val is not None:
                        data_points.append({'time': unix_ts, 'value': revenue_val, 'date': date_str})
                except Exception as e:
                    logger.warning(f"/api/revenue: Error processing yfinance data for {symbol}: {e}")
                    continue

            # Sort by time (oldest first)
            data_points.sort(key=lambda x: x['time'])
            logger.info(f"/api/revenue: {symbol} returned {len(data_points)} quarters from yfinance")
            return data_points

        except Exception as e:
            logger.error(f"/api/revenue: yfinance error for {symbol}: {e}")
            return []

    # Batch fetch from DB first (single query for canonical tickers)
    db_data = fetch_all_from_db(unique_canonical)

    # Identify which canonical tickers need external API fallback
    missing_canonical = [t for t in unique_canonical if db_data.get(t) is None]

    if missing_canonical:
        logger.info(f"/api/revenue: DB hits={len(unique_canonical) - len(missing_canonical)}, misses={len(missing_canonical)}: {missing_canonical}")
    else:
        logger.info(f"/api/revenue: All {len(unique_canonical)} canonical tickers found in DB")

    def persist_revenue_to_db(symbol, data_points):
        """Persist fetched revenue data to income_statement_quarterly for future DB hits"""
        if not data_points:
            return
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            inserted = 0
            for point in data_points:
                try:
                    # Use original date string if available (avoids timezone edge cases)
                    # Fall back to UTC conversion from timestamp if not present
                    fiscal_date = point.get('date') or datetime.utcfromtimestamp(point['time']).strftime('%Y-%m-%d')
                    # INSERT OR IGNORE to avoid duplicates (UNIQUE constraint on ticker, fiscal_date_ending)
                    cursor.execute('''
                        INSERT OR IGNORE INTO income_statement_quarterly
                        (ticker, fiscal_date_ending, total_revenue)
                        VALUES (?, ?, ?)
                    ''', (symbol, fiscal_date, point['value']))
                    if cursor.rowcount > 0:
                        inserted += 1
                except Exception as e:
                    logger.warning(f"/api/revenue: Error persisting row for {symbol}: {e}")
            conn.commit()
            conn.close()
            if inserted > 0:
                logger.info(f"/api/revenue: Persisted {inserted} new quarters for {symbol} to DB")
        except Exception as e:
            logger.error(f"/api/revenue: Error persisting {symbol} to DB: {e}")

    # Fallback to external APIs only for missing canonical tickers
    for symbol in missing_canonical:
        data = None

        # Try Alpha Vantage if client available (handles its own 12s rate limiting)
        if av_client:
            data = fetch_from_alpha_vantage(symbol)

        # Fall back to yfinance if still no data
        if data is None or len(data) == 0:
            logger.info(f"/api/revenue: Falling back to yfinance for {symbol}")
            data = fetch_from_yfinance(symbol)

        # Persist successful fetches to DB for future cache hits
        if data and len(data) > 0:
            persist_revenue_to_db(symbol, data)

        db_data[symbol] = data if data else []

    # Build final result (strip internal 'date' field, return only {time, value})
    # Map canonical data back to original requested tickers
    for i, original_ticker in enumerate(tickers):
        canonical = canonical_tickers[i]
        raw_data = db_data.get(canonical) or []
        result[original_ticker] = [{'time': p['time'], 'value': p['value']} for p in raw_data]

    return jsonify(result)


@fundamentals_bp.route('/api/fundamentals/overview')
def get_fundamental_overview():
    """
    Get company overview / fundamental metrics for one or more tickers.
    Query params: ?tickers=AAPL,MSFT,TSLA
    Returns: {AAPL: {...}, MSFT: {...}, ...}
    """
    tickers_str = request.args.get('tickers', '')
    if not tickers_str:
        return jsonify({'error': 'Missing tickers parameter'}), HTTP_BAD_REQUEST

    tickers = [t.strip().upper() for t in tickers_str.split(',') if t.strip()]
    if not tickers:
        return jsonify({'error': 'No valid tickers provided'}), HTTP_BAD_REQUEST

    # Resolve ticker aliases (e.g., GOOGL -> GOOG)
    canonical_map = {t: resolve_ticker_alias(t) for t in tickers}

    conn = get_db_connection()
    result = {}

    for ticker in tickers:
        db_ticker = canonical_map[ticker]
        if db_ticker != ticker:
            logger.info(f"/api/fundamentals/overview: aliased {ticker} -> {db_ticker}")

        try:
            query = "SELECT * FROM company_overview WHERE ticker = ?"
            df = pd.read_sql(query, conn, params=(db_ticker,))

            if df.empty:
                logger.warning(f"/api/fundamentals/overview: No data for {db_ticker}")
                result[ticker] = None
            else:
                # Convert to dict, excluding last_updated
                data = df.iloc[0].to_dict()
                if 'last_updated' in data:
                    del data['last_updated']
                result[ticker] = data

        except Exception as e:
            logger.error(f"/api/fundamentals/overview: Error for {db_ticker}: {e}")
            result[ticker] = None

    conn.close()
    return jsonify(result)


@fundamentals_bp.route('/api/fundamentals/earnings')
def get_fundamental_earnings():
    """
    Get quarterly earnings data for one or more tickers.
    Query params: ?tickers=AAPL,MSFT&period=quarterly (or annual)
    Returns: {AAPL: [{fiscalDateEnding, reportedEPS, estimatedEPS, ...}, ...], ...}
    """
    tickers_str = request.args.get('tickers', '')
    period = request.args.get('period', 'quarterly').lower()

    if not tickers_str:
        return jsonify({'error': 'Missing tickers parameter'}), HTTP_BAD_REQUEST

    if period not in ['quarterly', 'annual']:
        return jsonify({'error': 'Period must be quarterly or annual'}), HTTP_BAD_REQUEST

    tickers = [t.strip().upper() for t in tickers_str.split(',') if t.strip()]
    if not tickers:
        return jsonify({'error': 'No valid tickers provided'}), HTTP_BAD_REQUEST

    # Resolve ticker aliases (e.g., GOOGL -> GOOG)
    canonical_map = {t: resolve_ticker_alias(t) for t in tickers}

    table_name = f'earnings_{period}'
    conn = get_db_connection()
    result = {}

    for ticker in tickers:
        db_ticker = canonical_map[ticker]
        if db_ticker != ticker:
            logger.info(f"/api/fundamentals/earnings: aliased {ticker} -> {db_ticker}")

        try:
            query = f"SELECT * FROM {table_name} WHERE ticker = ? ORDER BY fiscal_date_ending DESC"
            df = pd.read_sql(query, conn, params=(db_ticker,))

            if df.empty:
                logger.warning(f"/api/fundamentals/earnings: No {period} data for {db_ticker}")
                result[ticker] = []
            else:
                # Convert to list of dicts
                data = df.to_dict('records')
                # Remove id and last_updated fields
                for row in data:
                    row.pop('id', None)
                    row.pop('last_updated', None)
                result[ticker] = data

        except Exception as e:
            logger.error(f"/api/fundamentals/earnings: Error for {db_ticker}: {e}")
            result[ticker] = []

    conn.close()
    return jsonify(result)


@fundamentals_bp.route('/api/fundamentals/income')
def get_fundamental_income():
    """
    Get income statement data for one or more tickers.
    Query params: ?tickers=AAPL,MSFT&period=quarterly (or annual)
    Returns: {AAPL: [{fiscalDateEnding, totalRevenue, netIncome, ...}, ...], ...}
    """
    tickers_str = request.args.get('tickers', '')
    period = request.args.get('period', 'quarterly').lower()

    if not tickers_str:
        return jsonify({'error': 'Missing tickers parameter'}), HTTP_BAD_REQUEST

    if period not in ['quarterly', 'annual']:
        return jsonify({'error': 'Period must be quarterly or annual'}), HTTP_BAD_REQUEST

    tickers = [t.strip().upper() for t in tickers_str.split(',') if t.strip()]
    if not tickers:
        return jsonify({'error': 'No valid tickers provided'}), HTTP_BAD_REQUEST

    # Resolve ticker aliases (e.g., GOOGL -> GOOG)
    canonical_map = {t: resolve_ticker_alias(t) for t in tickers}

    table_name = f'income_statement_{period}'
    conn = get_db_connection()
    result = {}

    for ticker in tickers:
        db_ticker = canonical_map[ticker]
        if db_ticker != ticker:
            logger.info(f"/api/fundamentals/income: aliased {ticker} -> {db_ticker}")

        try:
            query = f"SELECT * FROM {table_name} WHERE ticker = ? ORDER BY fiscal_date_ending DESC"
            df = pd.read_sql(query, conn, params=(db_ticker,))

            if df.empty:
                logger.warning(f"/api/fundamentals/income: No {period} data for {db_ticker}")
                result[ticker] = []
            else:
                data = df.to_dict('records')
                for row in data:
                    row.pop('id', None)
                    row.pop('last_updated', None)
                result[ticker] = data

        except Exception as e:
            logger.error(f"/api/fundamentals/income: Error for {db_ticker}: {e}")
            result[ticker] = []

    conn.close()
    return jsonify(result)


@fundamentals_bp.route('/api/fundamentals/balance')
def get_fundamental_balance():
    """
    Get balance sheet data for one or more tickers.
    Query params: ?tickers=AAPL,MSFT&period=quarterly (or annual)
    Returns: {AAPL: [{fiscalDateEnding, totalAssets, totalLiabilities, ...}, ...], ...}
    """
    tickers_str = request.args.get('tickers', '')
    period = request.args.get('period', 'quarterly').lower()

    if not tickers_str:
        return jsonify({'error': 'Missing tickers parameter'}), HTTP_BAD_REQUEST

    if period not in ['quarterly', 'annual']:
        return jsonify({'error': 'Period must be quarterly or annual'}), HTTP_BAD_REQUEST

    tickers = [t.strip().upper() for t in tickers_str.split(',') if t.strip()]
    if not tickers:
        return jsonify({'error': 'No valid tickers provided'}), HTTP_BAD_REQUEST

    # Resolve ticker aliases (e.g., GOOGL -> GOOG)
    canonical_map = {t: resolve_ticker_alias(t) for t in tickers}

    table_name = f'balance_sheet_{period}'
    conn = get_db_connection()
    result = {}

    for ticker in tickers:
        db_ticker = canonical_map[ticker]
        if db_ticker != ticker:
            logger.info(f"/api/fundamentals/balance: aliased {ticker} -> {db_ticker}")
        try:
            query = f"SELECT * FROM {table_name} WHERE ticker = ? ORDER BY fiscal_date_ending DESC"
            df = pd.read_sql(query, conn, params=(db_ticker,))

            if df.empty:
                logger.warning(f"/api/fundamentals/balance: No {period} data for {db_ticker}")
                result[ticker] = []
            else:
                data = df.to_dict('records')
                for row in data:
                    row.pop('id', None)
                    row.pop('last_updated', None)
                result[ticker] = data

        except Exception as e:
            logger.error(f"/api/fundamentals/balance: Error for {db_ticker}: {e}")
            result[ticker] = []

    conn.close()
    return jsonify(result)


@fundamentals_bp.route('/api/fundamentals/cashflow')
def get_fundamental_cashflow():
    """
    Get cash flow data for one or more tickers.
    Query params: ?tickers=AAPL,MSFT&period=quarterly (or annual)
    Returns: {AAPL: [{fiscalDateEnding, operatingCashflow, freeCashFlow, ...}, ...], ...}
    """
    tickers_str = request.args.get('tickers', '')
    period = request.args.get('period', 'quarterly').lower()

    if not tickers_str:
        return jsonify({'error': 'Missing tickers parameter'}), HTTP_BAD_REQUEST

    if period not in ['quarterly', 'annual']:
        return jsonify({'error': 'Period must be quarterly or annual'}), HTTP_BAD_REQUEST

    tickers = [t.strip().upper() for t in tickers_str.split(',') if t.strip()]
    if not tickers:
        return jsonify({'error': 'No valid tickers provided'}), HTTP_BAD_REQUEST

    # Resolve ticker aliases (e.g., GOOGL -> GOOG)
    canonical_map = {t: resolve_ticker_alias(t) for t in tickers}

    table_name = f'cash_flow_{period}'
    conn = get_db_connection()
    result = {}

    for ticker in tickers:
        db_ticker = canonical_map[ticker]
        if db_ticker != ticker:
            logger.info(f"/api/fundamentals/cashflow: aliased {ticker} -> {db_ticker}")
        try:
            query = f"SELECT * FROM {table_name} WHERE ticker = ? ORDER BY fiscal_date_ending DESC"
            df = pd.read_sql(query, conn, params=(db_ticker,))

            if df.empty:
                logger.warning(f"/api/fundamentals/cashflow: No {period} data for {db_ticker}")
                result[ticker] = []
            else:
                data = df.to_dict('records')
                for row in data:
                    row.pop('id', None)
                    row.pop('last_updated', None)
                result[ticker] = data

        except Exception as e:
            logger.error(f"/api/fundamentals/cashflow: Error for {db_ticker}: {e}")
            result[ticker] = []

    conn.close()
    return jsonify(result)


@fundamentals_bp.route('/api/fundamentals/chart')
def get_fundamentals_chart_data():
    """
    Get fundamental metrics formatted for charting (quarterly time series).
    Query params: ?tickers=AAPL,MSFT&metrics=revenue,netIncome,eps,fcf
    Returns: {AAPL: {revenue: [{time, value}, ...], netIncome: [...], ...}, ...}
    """
    tickers_str = request.args.get('tickers', '')
    metrics_str = request.args.get('metrics', 'revenue,netIncome,eps,fcf')

    if not tickers_str:
        return jsonify({'error': 'Missing tickers parameter'}), HTTP_BAD_REQUEST

    tickers = [t.strip().upper() for t in tickers_str.split(',') if t.strip()]
    metrics = [m.strip().lower() for m in metrics_str.split(',') if m.strip()]

    if not tickers:
        return jsonify({'error': 'No valid tickers provided'}), HTTP_BAD_REQUEST

    # Resolve ticker aliases (e.g., GOOGL -> GOOG)
    canonical_map = {t: resolve_ticker_alias(t) for t in tickers}

    conn = get_db_connection()
    result = {}

    # Metric mapping: metric_name -> (table, column, label)
    metric_map = {
        'revenue': ('income_statement_quarterly', 'total_revenue', 'Revenue'),
        'netincome': ('income_statement_quarterly', 'net_income', 'Net Income'),
        'eps': ('earnings_quarterly', 'reported_eps', 'EPS'),
        'fcf': ('cash_flow_quarterly', 'free_cash_flow', 'Free Cash Flow'),
        'operatingincome': ('income_statement_quarterly', 'operating_income', 'Operating Income'),
        'ebitda': ('income_statement_quarterly', 'ebitda', 'EBITDA'),
        'grossprofit': ('income_statement_quarterly', 'gross_profit', 'Gross Profit'),
        'operatingcashflow': ('cash_flow_quarterly', 'operating_cashflow', 'Operating Cash Flow'),
        'capex': ('cash_flow_quarterly', 'capital_expenditures', 'Capital Expenditures')
    }

    for ticker in tickers:
        # Use canonical ticker for DB query
        db_ticker = canonical_map[ticker]
        if db_ticker != ticker:
            logger.info(f"/api/fundamentals/chart: aliased {ticker} -> {db_ticker}")
        ticker_data = {}

        for metric in metrics:
            if metric not in metric_map:
                logger.warning(f"/api/fundamentals/chart: Unknown metric '{metric}'")
                continue

            table, column, label = metric_map[metric]

            try:
                query = f"""
                    SELECT fiscal_date_ending, {column}
                    FROM {table}
                    WHERE ticker = ?
                    ORDER BY fiscal_date_ending ASC
                """
                df = pd.read_sql(query, conn, params=(db_ticker,))

                if df.empty:
                    ticker_data[metric] = []
                else:
                    # Convert to chart format: [{time: unix_timestamp, value: number}, ...]
                    data_points = []
                    for _, row in df.iterrows():
                        try:
                            # Parse date and convert to unix timestamp
                            date = pd.to_datetime(row['fiscal_date_ending'])
                            unix_ts = int(date.timestamp())

                            value = row[column]
                            if pd.notna(value) and value != 0:
                                data_points.append({
                                    'time': unix_ts,
                                    'value': float(value)
                                })
                        except Exception as e:
                            logger.warning(f"/api/fundamentals/chart: Error parsing row for {ticker} {metric}: {e}")
                            continue

                    ticker_data[metric] = data_points
                    logger.info(f"/api/fundamentals/chart: {ticker} {metric} returned {len(data_points)} quarters")

            except Exception as e:
                logger.error(f"/api/fundamentals/chart: Error for {ticker} {metric}: {e}")
                ticker_data[metric] = []

        result[ticker] = ticker_data

    conn.close()
    return jsonify(result)
