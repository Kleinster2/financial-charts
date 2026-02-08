"""
Diagnostic and health-check routes.
Routes: /, /api/health, /api/diag, /api/diag_reduce, /api/diag_series
"""
import sqlite3
import time
import logging
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Blueprint, jsonify, request, redirect
import pandas as pd
from constants import DB_PATH, get_db_connection
from helpers import get_table_columns, _schema_cache, _schema_cache_time

logger = logging.getLogger(__name__)

diag_bp = Blueprint('diag', __name__)


@diag_bp.route('/')
def index():
    """Redirect root to sandbox UI"""
    return redirect('/sandbox/')


@diag_bp.route('/api/health')
def health():
    """Health check endpoint for monitoring."""
    try:
        # Test database connection
        conn = get_db_connection()
        cursor = conn.execute("SELECT COUNT(*) FROM sqlite_master WHERE type='table'")
        table_count = cursor.fetchone()[0]
        conn.close()

        return jsonify({
            'status': 'healthy',
            'timestamp': time.time(),
            'database': 'connected',
            'table_count': table_count,
            'cache_size': len(_schema_cache),
            'cache_age': time.time() - _schema_cache_time if _schema_cache_time > 0 else None
        }), 200
    except Exception as e:
        logger.error(f"Health check failed: {e}")
        return jsonify({
            'status': 'unhealthy',
            'timestamp': time.time(),
            'error': str(e)
        }), 503


@diag_bp.route('/api/diag')
def diag():
    """Return DB path and the server-observed value for a given ticker/date.
    Query params:
        ticker: symbol (default '^VXD')
        date: YYYY-MM-DD (default '2021-07-13')
    """
    ticker = (request.args.get('ticker') or '^VXD').strip().upper()
    date = (request.args.get('date') or '2021-07-13').strip()

    conn = None
    try:
        conn = get_db_connection()
        # Column presence
        try:
            stock_cols = {row['name'] for row in conn.execute("PRAGMA table_info(stock_prices_daily)").fetchall()}
        except sqlite3.OperationalError:
            stock_cols = set()
        try:
            futures_cols = {row['name'] for row in conn.execute("PRAGMA table_info(futures_prices_daily)").fetchall()}
        except sqlite3.OperationalError:
            futures_cols = set()

        table = None
        # Check futures table first for =F tickers (has more recent data)
        if ticker in futures_cols and ticker.endswith('=F'):
            table = 'futures_prices_daily'
        elif ticker in stock_cols:
            table = 'stock_prices_daily'
        elif ticker in futures_cols:
            table = 'futures_prices_daily'

        value = None
        row_count = None
        all_vals = []
        if table:
            row = conn.execute(f'SELECT "{ticker}" FROM {table} WHERE Date = ?', (date,)).fetchone()
            value = row[0] if row else None
            try:
                row_count = conn.execute(f'SELECT COUNT(1) FROM {table} WHERE Date = ?', (date,)).fetchone()[0]
                all_vals = [r[0] for r in conn.execute(f'SELECT "{ticker}" FROM {table} WHERE Date = ?', (date,)).fetchall()]
            except Exception:
                pass

        return jsonify({
            'db_path': DB_PATH,
            'ticker': ticker,
            'date': date,
            'table': table,
            'stock_has_col': ticker in stock_cols,
            'futures_has_col': ticker in futures_cols,
            'value': value,
            'row_count_for_date': row_count,
            'all_values_for_date': all_vals
        }), 200
    except Exception as e:
        return jsonify({'error': str(e), 'db_path': DB_PATH}), 500
    finally:
        if conn is not None:
            conn.close()


# Diagnostic: run the same transform as /api/data for a single ticker
@diag_bp.route('/api/diag_reduce')
def diag_reduce():
    ticker = (request.args.get('ticker') or '^VXD').strip().upper()
    conn = get_db_connection()
    try:
        # Detect table
        try:
            stock_cols = {row['name'] for row in conn.execute("PRAGMA table_info(stock_prices_daily)").fetchall()}
        except sqlite3.OperationalError:
            stock_cols = set()
        try:
            fut_cols = {row['name'] for row in conn.execute("PRAGMA table_info(futures_prices_daily)").fetchall()}
        except sqlite3.OperationalError:
            fut_cols = set()
        # Check futures table first for =F tickers (has more recent data)
        if ticker in fut_cols and ticker.endswith('=F'):
            table = 'futures_prices_daily'
        elif ticker in stock_cols:
            table = 'stock_prices_daily'
        elif ticker in fut_cols:
            table = 'futures_prices_daily'
        else:
            return jsonify({'error': 'ticker not found', 'db_path': DB_PATH}), 404
        q = (
            f'SELECT date(Date) AS Date, MAX("{ticker}") as value '
            f'FROM {table} '
            f'WHERE "{ticker}" IS NOT NULL '
            f'GROUP BY date(Date) '
            f'ORDER BY date(Date) ASC'
        )
        df = pd.read_sql_query(q, conn, parse_dates=['Date'])
        if df.empty:
            return jsonify({'ticker': ticker, 'records': []})
        df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
        df = df.dropna(subset=['Date', 'value'])
        df['value'] = pd.to_numeric(df['value'], errors='coerce')
        df = df.dropna(subset=['value'])
        df = df.sort_values('Date')
        day = df['Date'].dt.normalize()
        df = df.assign(Date=day).groupby('Date', as_index=False)['value'].median()
        df['time'] = (df['Date'].astype('int64') // 10**9).astype(int)
        records = df[['time', 'value']].to_dict(orient='records')
        return jsonify({'ticker': ticker, 'records': records, 'db_path': DB_PATH})
    finally:
        conn.close()


# Diagnostic: return raw rows for a single ticker between dates using same SQL as /api/data
@diag_bp.route('/api/diag_series')
def diag_series():
    ticker = (request.args.get('ticker') or '^VXD').strip().upper()
    frm = (request.args.get('from') or '2021-07-09').strip()
    to = (request.args.get('to') or '2021-07-16').strip()

    conn = get_db_connection()
    try:
        # Detect table
        try:
            stock_cols = {row['name'] for row in conn.execute("PRAGMA table_info(stock_prices_daily)").fetchall()}
        except sqlite3.OperationalError:
            stock_cols = set()
        try:
            fut_cols = {row['name'] for row in conn.execute("PRAGMA table_info(futures_prices_daily)").fetchall()}
        except sqlite3.OperationalError:
            fut_cols = set()

        # Check futures table first for =F tickers (has more recent data)
        if ticker in fut_cols and ticker.endswith('=F'):
            table = 'futures_prices_daily'
        elif ticker in stock_cols:
            table = 'stock_prices_daily'
        elif ticker in fut_cols:
            table = 'futures_prices_daily'
        else:
            return jsonify({'error': 'ticker not found in DB', 'db_path': DB_PATH}), 404

        q = f'SELECT Date, "{ticker}" as value FROM {table} WHERE "{ticker}" IS NOT NULL ORDER BY Date ASC'
        df = pd.read_sql_query(q, conn, parse_dates=['Date'])
        df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
        df = df.dropna(subset=['Date'])
        mask = (df['Date'] >= pd.to_datetime(frm)) & (df['Date'] <= pd.to_datetime(to))
        sub = df.loc[mask].copy()
        # Return all rows as strings for Date
        sub['Date'] = sub['Date'].dt.strftime('%Y-%m-%d')
        return jsonify({
            'db_path': DB_PATH,
            'ticker': ticker,
            'table': table,
            'from': frm,
            'to': to,
            'rows': sub.to_dict(orient='records'),
            'row_count': int(len(sub))
        })
    finally:
        conn.close()
