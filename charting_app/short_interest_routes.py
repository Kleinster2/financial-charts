"""
Short interest API routes.
Routes: /api/short-interest, /api/short-interest/latest
"""
import logging
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Blueprint, jsonify, request
from constants import get_db_connection, HTTP_BAD_REQUEST, resolve_ticker_alias

logger = logging.getLogger(__name__)

short_interest_bp = Blueprint('short_interest', __name__)


@short_interest_bp.route('/api/short-interest')
def get_short_interest():
    """
    Get short interest data for one or more tickers.
    Query params: ?tickers=AAPL,MSFT&limit=10
    Returns: {AAPL: [{settlement_date, short_percent_float, days_to_cover, ...}, ...], ...}
    """
    tickers_str = request.args.get('tickers', '')
    limit = request.args.get('limit', '10')

    if not tickers_str:
        return jsonify({'error': 'Missing tickers parameter'}), HTTP_BAD_REQUEST

    tickers = [t.strip().upper() for t in tickers_str.split(',') if t.strip()]
    if not tickers:
        return jsonify({'error': 'No valid tickers provided'}), HTTP_BAD_REQUEST

    try:
        limit = int(limit)
    except ValueError:
        return jsonify({'error': 'Invalid limit parameter'}), HTTP_BAD_REQUEST

    # Resolve ticker aliases
    canonical_map = {t: resolve_ticker_alias(t) for t in tickers}

    conn = get_db_connection()
    cursor = conn.cursor()
    result = {}

    for ticker in tickers:
        db_ticker = canonical_map[ticker]
        if db_ticker != ticker:
            logger.info(f"/api/short-interest: aliased {ticker} -> {db_ticker}")

        try:
            cursor.execute('''
                SELECT settlement_date, short_interest, shares_outstanding,
                       short_percent_float, short_percent_outstanding,
                       days_to_cover, avg_daily_volume, source
                FROM short_interest
                WHERE ticker = ?
                ORDER BY settlement_date DESC
                LIMIT ?
            ''', (db_ticker, limit))

            rows = cursor.fetchall()
            data_points = []

            for row in rows:
                data_points.append({
                    'settlementDate': row[0],
                    'shortInterest': row[1],
                    'sharesOutstanding': row[2],
                    'shortPercentFloat': row[3],
                    'shortPercentOutstanding': row[4],
                    'daysToCover': row[5],
                    'avgDailyVolume': row[6],
                    'source': row[7]
                })

            # Reverse to chronological order for charting
            data_points.reverse()
            result[ticker] = data_points

        except Exception as e:
            logger.error(f"/api/short-interest: Error for {db_ticker}: {e}")
            result[ticker] = []

    conn.close()
    return jsonify(result)


@short_interest_bp.route('/api/short-interest/latest')
def get_short_interest_latest():
    """
    Get latest short interest data for multiple tickers (for dashboard/overview).
    Query params: ?tickers=AAPL,MSFT or no params for all
    Returns: [{ticker, settlementDate, shortPercentFloat, daysToCover, ...}, ...]
    """
    tickers_str = request.args.get('tickers', '')

    conn = get_db_connection()
    cursor = conn.cursor()

    if tickers_str:
        tickers = [t.strip().upper() for t in tickers_str.split(',') if t.strip()]
        placeholders = ','.join('?' * len(tickers))
        query = f'''
            SELECT si.ticker, si.settlement_date, si.short_interest,
                   si.shares_outstanding, si.short_percent_float,
                   si.short_percent_outstanding, si.days_to_cover,
                   si.avg_daily_volume, si.source
            FROM short_interest si
            INNER JOIN (
                SELECT ticker, MAX(settlement_date) as max_date
                FROM short_interest
                WHERE ticker IN ({placeholders})
                GROUP BY ticker
            ) latest ON si.ticker = latest.ticker AND si.settlement_date = latest.max_date
            ORDER BY si.short_percent_float DESC
        '''
        cursor.execute(query, tickers)
    else:
        # Get all tickers with SI data
        cursor.execute('''
            SELECT si.ticker, si.settlement_date, si.short_interest,
                   si.shares_outstanding, si.short_percent_float,
                   si.short_percent_outstanding, si.days_to_cover,
                   si.avg_daily_volume, si.source
            FROM short_interest si
            INNER JOIN (
                SELECT ticker, MAX(settlement_date) as max_date
                FROM short_interest
                GROUP BY ticker
            ) latest ON si.ticker = latest.ticker AND si.settlement_date = latest.max_date
            ORDER BY si.short_percent_float DESC
        ''')

    rows = cursor.fetchall()
    result = []

    for row in rows:
        result.append({
            'ticker': row[0],
            'settlementDate': row[1],
            'shortInterest': row[2],
            'sharesOutstanding': row[3],
            'shortPercentFloat': row[4],
            'shortPercentOutstanding': row[5],
            'daysToCover': row[6],
            'avgDailyVolume': row[7],
            'source': row[8]
        })

    conn.close()
    return jsonify(result)
