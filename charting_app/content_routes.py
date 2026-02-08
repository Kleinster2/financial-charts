"""
Content and utility routes.
Routes: /sandbox/, /api/workspace, /api/commentary, /api/etf/series
"""
import sqlite3
import json
import os
import sys
import logging
import subprocess
from pathlib import Path

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Blueprint, jsonify, request, send_from_directory
import pandas as pd
from constants import (get_db_connection, WORKSPACE_FILENAME, WORKSPACE_TEMP_SUFFIX)
from helpers import basedir

logger = logging.getLogger(__name__)

content_bp = Blueprint('content', __name__)


def trigger_workspace_backup():
    """Trigger automatic workspace backup via backup_workspace.py script"""
    try:
        backup_script = Path(__file__).parent.parent / 'backup_workspace.py'
        if not backup_script.exists():
            logger.warning(f"Backup script not found at {backup_script}")
            return False

        result = subprocess.run(
            [sys.executable, str(backup_script), 'backup'],
            capture_output=True,
            text=True,
            timeout=10
        )

        if result.returncode == 0:
            logger.info(f"Automatic backup completed: {result.stdout.strip()}")
            return True
        else:
            logger.warning(f"Backup script returned error: {result.stderr.strip()}")
            return False
    except subprocess.TimeoutExpired:
        logger.error("Backup script timed out")
        return False
    except Exception as e:
        logger.error(f"Failed to trigger backup: {e}")
        return False


# Sandbox static serving
@content_bp.route('/sandbox/')
@content_bp.route('/sandbox/<path:filename>')
def sandbox_static(filename='index.html'):
    sandbox_dir = os.path.abspath(os.path.join(basedir, '..', 'charting_sandbox'))
    return send_from_directory(sandbox_dir, filename)


# --- Workspace Persistence API ---
@content_bp.route('/api/workspace', methods=['GET', 'POST'])
def workspace():
    """Persist or retrieve the multi-chart workspace layout.
    The workspace is stored as JSON in a file so it survives server restarts
    and is shared across browser origins/ports.
    """
    workspace_path = os.path.join(basedir, WORKSPACE_FILENAME)

    if request.method == 'POST':
        try:
            state = request.get_json(force=True) or []
            # Determine schema and counts
            if isinstance(state, dict) and 'cards' in state:
                items = len(state.get('cards') or [])
                schema = 'object'
            else:
                # Legacy: array of cards
                items = len(state) if isinstance(state, list) else 0
                schema = 'array'
            logger.info(f"/api/workspace POST schema={schema} items={items}")

            # Write atomically by first dumping to a temp file
            temp_file = WORKSPACE_FILENAME + WORKSPACE_TEMP_SUFFIX
            with open(temp_file, 'w', encoding='utf-8') as fh:
                json.dump(state, fh)
            os.replace(temp_file, workspace_path)

            # Trigger automatic backup after successful save
            trigger_workspace_backup()

            return jsonify({'status': 'saved', 'items': items, 'schema': schema}), 200
        except Exception as e:
            logger.error(f"Failed to save workspace: {e}")
            return jsonify({'error': 'failed to save'}), 500

    # GET
    if os.path.exists(workspace_path):
        try:
            with open(workspace_path, 'r', encoding='utf-8') as fh:
                state = json.load(fh)
        except Exception as e:
            logger.error(f"Failed to read workspace file: {e}")
            state = []
    else:
        state = []
    return jsonify(state)


# --- Lightweight commentary endpoint ---
@content_bp.route('/api/commentary')
def commentary():
    """Return rule-based text summary for each requested ticker.
    Query params:
        tickers: comma-separated symbols
        from, to: unix seconds (optional)
    """
    tickers_param = request.args.get('tickers', '')
    if not tickers_param:
        return jsonify({}), 400

    tickers = [t.strip().upper() for t in tickers_param.split(',') if t.strip()]
    try:
        t_from = int(request.args.get('from', 0))
    except ValueError:
        t_from = 0
    try:
        t_to = int(request.args.get('to', 10**12))
    except ValueError:
        t_to = 10**12

    conn = get_db_connection()
    safe_cols = '"' + '", "'.join(tickers) + '"'
    query = f'SELECT Date, {safe_cols} FROM stock_prices_daily ORDER BY Date ASC'
    df = pd.read_sql_query(query, conn, parse_dates=['Date'])
    conn.close()

    # Limit range
    ts = (df['Date'].astype('int64') // 10**9)
    df = df[(ts >= t_from) & (ts <= t_to)].set_index('Date')

    out = {}
    for t in tickers:
        series = df[t].dropna()
        if series.empty:
            out[t] = 'No data for selected period.'
            continue
        start, end = series.iloc[[0, -1]]
        pct = (end / start - 1) * 100
        peak_date = series.idxmax().date()
        trough_date = series.idxmin().date()
        direction = 'rose' if pct > 0 else 'fell'
        out[t] = (f'From {series.index[0].date()} to {series.index[-1].date()}, '
                  f'{t} {direction} {pct:+.1f} %. Peak on {peak_date}, low on {trough_date}.')
    return jsonify(out)


# --- ETF series endpoint (Option A) ---
@content_bp.route('/api/etf/series')
def etf_series():
    """Return derived ETF series like portfolio value and shares outstanding.
    Query params:
        etf: e.g., 'ALLW' (required)
        metrics: comma-separated subset of ['value','shares'] (default 'value,shares')
        from: ISO date YYYY-MM-DD (optional)
        to: ISO date YYYY-MM-DD (optional)
    Response JSON keys present only for requested metrics.
    Each series is a list of {time: <unix_sec>, value: <number>}.
    """
    try:
        etf = (request.args.get('etf', '') or '').strip().upper()
        if not etf:
            return jsonify({'error': 'etf is required'}), 400

        metrics_param = request.args.get('metrics', 'value,shares')
        allowed = {'value', 'shares'}
        metrics = {m.strip().lower() for m in metrics_param.split(',') if m.strip().lower() in allowed}
        if not metrics:
            metrics = {'value'}

        from_str = request.args.get('from')
        to_str = request.args.get('to')

        conn = get_db_connection()

        # Aggregate portfolio value by snapshot_date
        q_hold = (
            "SELECT snapshot_date as Date, SUM(market_value) as total_value "
            "FROM etf_holdings_daily "
            "WHERE etf = ? "
            "GROUP BY snapshot_date "
            "ORDER BY snapshot_date ASC"
        )
        df_hold = pd.read_sql_query(q_hold, conn, params=[etf], parse_dates=['Date'])

        # Filter by date range if provided
        if not df_hold.empty and (from_str or to_str):
            if from_str:
                try:
                    start_ts = pd.to_datetime(from_str)
                    df_hold = df_hold[df_hold['Date'] >= start_ts]
                except Exception:
                    pass
            if to_str:
                try:
                    end_ts = pd.to_datetime(to_str)
                    df_hold = df_hold[df_hold['Date'] <= end_ts]
                except Exception:
                    pass

        result = {}

        # Metric: portfolio value over time
        if 'value' in metrics:
            if df_hold.empty:
                result['value'] = []
            else:
                tmp = df_hold.copy()
                tmp['time'] = (tmp['Date'].astype('int64') // 10**9).astype(int)
                result['value'] = (
                    tmp[['time', 'total_value']]
                    .rename(columns={'total_value': 'value'})
                    .to_dict(orient='records')
                )

        # Metric: shares outstanding = total_value / price
        if 'shares' in metrics:
            shares_series = []
            if not df_hold.empty:
                # Check price column exists for ETF
                try:
                    cols = {row['name'] for row in conn.execute("PRAGMA table_info(stock_prices_daily)").fetchall()}
                except sqlite3.OperationalError:
                    cols = set()
                logger.info(f"/api/etf/series shares: df_hold rows={len(df_hold)}; price_col_exists={etf in cols}")
                if etf in cols:
                    q_price = f'SELECT Date, "{etf}" as price FROM stock_prices_daily ORDER BY Date ASC'
                    df_price = pd.read_sql_query(q_price, conn, parse_dates=['Date'])
                    logger.info(f"/api/etf/series shares: df_price rows={len(df_price)}")
                    if not df_price.empty:
                        if from_str or to_str:
                            if from_str:
                                try:
                                    start_ts = pd.to_datetime(from_str)
                                    df_price = df_price[df_price['Date'] >= start_ts]
                                except Exception:
                                    pass
                            if to_str:
                                try:
                                    end_ts = pd.to_datetime(to_str)
                                    df_price = df_price[df_price['Date'] <= end_ts]
                                except Exception:
                                    pass
                        # Use asof merge to tolerate non-trading-day snapshots; align to previous available price (up to 5 days back)
                        df_hold_sorted = df_hold[['Date', 'total_value']].sort_values('Date')
                        df_price_sorted = df_price[['Date', 'price']].sort_values('Date')
                        try:
                            df_m = pd.merge_asof(
                                df_hold_sorted,
                                df_price_sorted,
                                on='Date',
                                direction='backward',
                                tolerance=pd.Timedelta('5D')
                            )
                        except Exception as me:
                            logger.warning(f"/api/etf/series shares: merge_asof failed ({me}); falling back to inner merge")
                            df_m = pd.merge(df_hold_sorted, df_price_sorted, on='Date', how='inner')
                        df_m = df_m[df_m['price'].notna()]
                        logger.info(f"/api/etf/series shares: merged rows={len(df_m)}")
                        if not df_m.empty:
                            df_m['shares'] = df_m['total_value'] / df_m['price']
                            df_m['time'] = (df_m['Date'].astype('int64') // 10**9).astype(int)
                            shares_series = (
                                df_m[['time', 'shares']]
                                .rename(columns={'shares': 'value'})
                                .to_dict(orient='records')
                            )
                            logger.info(f"/api/etf/series shares: output points={len(shares_series)}")
            result['shares'] = shares_series

        conn.close()
        return jsonify(result)
    except Exception as e:
        logger.error(f"/api/etf/series error: {e}")
        return jsonify({'error': 'failed to compute series'}), 500
