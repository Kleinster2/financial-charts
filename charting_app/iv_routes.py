"""
Implied volatility API routes.
Routes: /api/iv/stock, /api/iv/cboe, /api/iv/latest
"""
import logging
import sys
import os
from datetime import datetime, timedelta

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Blueprint, jsonify, request
from constants import get_db_connection, HTTP_BAD_REQUEST

logger = logging.getLogger(__name__)

iv_bp = Blueprint('iv', __name__)


@iv_bp.route('/api/iv/stock')
def get_stock_implied_volatility():
    """
    Get implied volatility data for stocks.
    Query params: ?tickers=AAPL,MSFT&days=30
    Returns: {AAPL: [{date, call_iv, put_iv, average_iv, current_price}, ...], ...}
    """
    tickers_str = request.args.get('tickers', '')
    days = request.args.get('days', '30')

    if not tickers_str:
        return jsonify({'error': 'Missing tickers parameter'}), HTTP_BAD_REQUEST

    tickers = [t.strip().upper() for t in tickers_str.split(',') if t.strip()]

    try:
        days = int(days)
    except ValueError:
        return jsonify({'error': 'Invalid days parameter'}), HTTP_BAD_REQUEST

    if not tickers:
        return jsonify({'error': 'No valid tickers provided'}), HTTP_BAD_REQUEST

    conn = get_db_connection()
    cursor = conn.cursor()
    result = {}

    start_date = (datetime.now() - timedelta(days=days)).strftime('%Y-%m-%d')

    for ticker in tickers:
        try:
            cursor.execute('''
                SELECT date, call_iv, put_iv, average_iv, current_price, expiration
                FROM implied_volatility_daily
                WHERE ticker = ? AND date >= ?
                ORDER BY date ASC
            ''', (ticker, start_date))

            rows = cursor.fetchall()
            data_points = []

            for row in rows:
                # Convert date to unix timestamp for charting
                date_obj = datetime.strptime(row[0], '%Y-%m-%d')
                timestamp = int(date_obj.timestamp())

                data_points.append({
                    'time': timestamp,
                    'date': row[0],
                    'call_iv': row[1],
                    'put_iv': row[2],
                    'average_iv': row[3],
                    'current_price': row[4],
                    'expiration': row[5]
                })

            result[ticker] = data_points
            logger.info(f"/api/iv/stock: {ticker} returned {len(data_points)} data points")

        except Exception as e:
            logger.error(f"/api/iv/stock: Error for {ticker}: {e}")
            result[ticker] = []

    conn.close()
    return jsonify(result)


@iv_bp.route('/api/iv/cboe')
def get_cboe_indices():
    """
    Get CBOE volatility indices (VIX, VXN, VXD).
    Query params: ?symbols=^VIX,^VXN&days=30
    Returns: {^VIX: [{date, value}, ...], ^VXN: [{date, value}, ...], ...}
    """
    symbols_str = request.args.get('symbols', '^VIX,^VXN,^VXD')
    days = request.args.get('days', '30')

    symbols = [s.strip() for s in symbols_str.split(',') if s.strip()]

    try:
        days = int(days)
    except ValueError:
        return jsonify({'error': 'Invalid days parameter'}), HTTP_BAD_REQUEST

    if not symbols:
        return jsonify({'error': 'No valid symbols provided'}), HTTP_BAD_REQUEST

    conn = get_db_connection()
    cursor = conn.cursor()
    result = {}

    start_date = (datetime.now() - timedelta(days=days)).strftime('%Y-%m-%d')

    for symbol in symbols:
        try:
            cursor.execute('''
                SELECT date, value, description
                FROM cboe_indices_daily
                WHERE symbol = ? AND date >= ?
                ORDER BY date ASC
            ''', (symbol, start_date))

            rows = cursor.fetchall()
            data_points = []

            for row in rows:
                # Convert date to unix timestamp for charting
                date_obj = datetime.strptime(row[0], '%Y-%m-%d')
                timestamp = int(date_obj.timestamp())

                data_points.append({
                    'time': timestamp,
                    'date': row[0],
                    'value': row[1],
                    'description': row[2]
                })

            result[symbol] = data_points
            logger.info(f"/api/iv/cboe: {symbol} returned {len(data_points)} data points")

        except Exception as e:
            logger.error(f"/api/iv/cboe: Error for {symbol}: {e}")
            result[symbol] = []

    conn.close()
    return jsonify(result)


@iv_bp.route('/api/iv/latest')
def get_latest_iv():
    """
    Get latest implied volatility values for tickers.
    Query params: ?tickers=AAPL,MSFT
    Returns: {AAPL: {date, call_iv, put_iv, average_iv, current_price}, ...}
    """
    tickers_str = request.args.get('tickers', '')

    if not tickers_str:
        return jsonify({'error': 'Missing tickers parameter'}), HTTP_BAD_REQUEST

    tickers = [t.strip().upper() for t in tickers_str.split(',') if t.strip()]

    if not tickers:
        return jsonify({'error': 'No valid tickers provided'}), HTTP_BAD_REQUEST

    conn = get_db_connection()
    cursor = conn.cursor()
    result = {}

    for ticker in tickers:
        try:
            cursor.execute('''
                SELECT date, call_iv, put_iv, average_iv, current_price, expiration
                FROM implied_volatility_daily
                WHERE ticker = ?
                ORDER BY date DESC
                LIMIT 1
            ''', (ticker,))

            row = cursor.fetchone()

            if row:
                result[ticker] = {
                    'date': row[0],
                    'call_iv': row[1],
                    'put_iv': row[2],
                    'average_iv': row[3],
                    'current_price': row[4],
                    'expiration': row[5]
                }
            else:
                result[ticker] = None

            logger.info(f"/api/iv/latest: {ticker} returned {('data' if row else 'no data')}")

        except Exception as e:
            logger.error(f"/api/iv/latest: Error for {ticker}: {e}")
            result[ticker] = None

    conn.close()
    return jsonify(result)
