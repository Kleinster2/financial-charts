import sqlite3
import time
import pandas as pd
import os
import sys
from flask import Flask, jsonify, render_template, request, redirect, send_from_directory
from flask_cors import CORS
import logging
import numpy as np
import json

# Configure logging to output to stdout for easier debugging
logging.basicConfig(
    level=logging.INFO,
    stream=sys.stdout,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

app = Flask(__name__)
CORS(app)

@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '-1'
    # Allow cross-origin requests (e.g., sandbox running on :5500)
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
    return response

@app.context_processor
def inject_now():
    return {'now': time.time()}

# Get the absolute path of the directory containing this script (charting_app)
basedir = os.path.abspath(os.path.dirname(__file__))
# Construct the absolute path to the database in the parent directory
DB_PATH = os.path.join(basedir, '..', 'sp500_data.db')

# --- Start of Diagnostic Logging ---
app.logger.info(f"SCRIPT_DIR: {basedir}")
app.logger.info(f"DB_PATH: {DB_PATH}")
if not os.path.exists(DB_PATH):
    app.logger.error("FATAL: DATABASE NOT FOUND AT THE CALCULATED PATH!")
else:
    app.logger.info("SUCCESS: Database file was found at the path.")
# --- End of Diagnostic Logging ---

def get_db_connection():
    """Establishes a connection to the SQLite database."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    """Redirect root to sandbox UI"""
    return redirect('/sandbox/')

# Sandbox static serving
@app.route('/sandbox/')
@app.route('/sandbox/<path:filename>')
def sandbox_static(filename='index.html'):
    sandbox_dir = os.path.abspath(os.path.join(basedir, '..', 'charting_sandbox'))
    return send_from_directory(sandbox_dir, filename)

@app.route('/api/tickers')
def get_tickers():
    """Provides a sorted list of all available tickers from the database."""
    app.logger.info("Request received for /api/tickers")
    try:
        conn = get_db_connection()
        tickers_set = set()

        # Collect columns from stock table
        try:
            cursor = conn.execute("PRAGMA table_info(stock_prices_daily)")
            tickers_set.update(row['name'] for row in cursor.fetchall() if row['name'] != 'Date')
        except sqlite3.OperationalError:
            app.logger.warning("Table 'stock_prices_daily' not found.")

        # Collect columns from futures table
        try:
            cursor = conn.execute("PRAGMA table_info(futures_prices_daily)")
            tickers_set.update(row['name'] for row in cursor.fetchall() if row['name'] != 'Date')
        except sqlite3.OperationalError:
            app.logger.warning("Table 'futures_prices_daily' not found.")

        conn.close()
        tickers = sorted(tickers_set)
        app.logger.info(f"Found {len(tickers)} tickers across stock and futures tables.")
        if not tickers:
            app.logger.warning("WARNING: Ticker list is empty. Check if table 'stock_prices_daily' exists and is populated.")
        return jsonify(sorted(tickers))
    except Exception as e:
        app.logger.error(f"An error occurred in get_tickers: {e}")
        return jsonify([]), 500

@app.route('/api/metadata')
def get_metadata():
    """Return a mapping of ticker -> company name for provided tickers"""
    tickers_str = request.args.get('tickers', '')
    tickers = [t.strip().upper() for t in tickers_str.split(',') if t.strip()]
    # Empty query → empty JSON
    if not tickers:
        return jsonify({})

    try:
        conn = get_db_connection()
        placeholders = ','.join(['?'] * len(tickers))
        query = f"SELECT ticker, name FROM stock_metadata WHERE ticker IN ({placeholders})"
        df = pd.read_sql(query, conn, params=tickers)
        conn.close()
        # Build dict; if name NULL fallback to ticker
        mapping = {row['ticker']: (row['name'] or row['ticker']) for _, row in df.iterrows()}
        return jsonify(mapping)
    except Exception as e:
        app.logger.error(f"/api/metadata error: {e}")
        return jsonify({}), 500


@app.route('/api/data')
def get_data():
    """Provides raw historical price data for a list of tickers."""
    tickers_str = request.args.get('tickers')
    if not tickers_str:
        return jsonify({'error': 'At least one ticker is required'}), 400

    tickers = [t.strip().upper() for t in tickers_str.split(',') if t.strip()]
    
    conn = get_db_connection()

    # Determine which tickers belong to which table
    stock_cols, futures_cols = set(), set()
    try:
        cursor = conn.execute("PRAGMA table_info(stock_prices_daily)")
        stock_cols = {row['name'] for row in cursor.fetchall()}
    except sqlite3.OperationalError:
        pass
    try:
        cursor = conn.execute("PRAGMA table_info(futures_prices_daily)")
        futures_cols = {row['name'] for row in cursor.fetchall()}
    except sqlite3.OperationalError:
        pass

    stock_sel = [t for t in tickers if t in stock_cols]
    futures_sel = [t for t in tickers if t in futures_cols]

    df_list = []
    if stock_sel:
        cols = '\", \"'.join(stock_sel)
        q = f'SELECT Date, "{cols}" FROM stock_prices_daily ORDER BY Date ASC'
        df_stock = pd.read_sql_query(q, conn, parse_dates=['Date']).set_index('Date')
        df_list.append(df_stock)
    if futures_sel:
        cols = '\", \"'.join(futures_sel)
        q = f'SELECT Date, "{cols}" FROM futures_prices_daily ORDER BY Date ASC'
        df_fut = pd.read_sql_query(q, conn, parse_dates=['Date']).set_index('Date')
        df_list.append(df_fut)

    conn.close()

    if not df_list:
        # Return empty arrays for requested tickers when no data is found
        return jsonify({t: [] for t in tickers}), 200

    df = pd.concat(df_list, axis=1)

    # The frontend now expects raw data. It also expects 'time' as a UNIX timestamp.
    df['time'] = (df.index.astype(int) / 10**9).astype(int)

    chart_data = {}
    for ticker in tickers:
        if ticker in df.columns:
            temp_df = df[['time', ticker]].copy()
            temp_df.rename(columns={ticker: 'value'}, inplace=True)
            # Convert NaN to None, which becomes JSON's `null`.
            # This allows the chart to render gaps for missing data.
            temp_df['value'] = temp_df['value'].replace({np.nan: None})
            chart_data[ticker] = temp_df.to_dict(orient='records')
        else:
            chart_data[ticker] = []

    return jsonify(chart_data)




# --- Workspace Persistence API ---
@app.route('/api/workspace', methods=['GET', 'POST'])
def workspace():
    """Persist or retrieve the multi-chart workspace layout.
    The workspace is stored as JSON in a file so it survives server restarts
    and is shared across browser origins/ports.
    """
    workspace_path = os.path.join(basedir, 'workspace.json')

    if request.method == 'POST':
        try:
            state = request.get_json(force=True) or []
            # Write atomically by first dumping to a temp file
            tmp_path = workspace_path + '.tmp'
            with open(tmp_path, 'w', encoding='utf-8') as fh:
                json.dump(state, fh)
            os.replace(tmp_path, workspace_path)
            return jsonify({'status': 'saved', 'items': len(state)}), 200
        except Exception as e:
            app.logger.error(f"Failed to save workspace: {e}")
            return jsonify({'error': 'failed to save'}), 500

    # GET
    if os.path.exists(workspace_path):
        try:
            with open(workspace_path, 'r', encoding='utf-8') as fh:
                state = json.load(fh)
        except Exception as e:
            app.logger.error(f"Failed to read workspace file: {e}")
            state = []
    else:
        state = []
    return jsonify(state)


# --- Lightweight commentary endpoint ---
@app.route('/api/commentary')
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
    ts = (df['Date'].astype(int) // 10**9)
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
@app.route('/api/etf/series')
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
                tmp['time'] = (tmp['Date'].astype(int) // 10**9).astype(int)
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
                app.logger.info(f"/api/etf/series shares: df_hold rows={len(df_hold)}; price_col_exists={etf in cols}")
                if etf in cols:
                    q_price = f'SELECT Date, "{etf}" as price FROM stock_prices_daily ORDER BY Date ASC'
                    df_price = pd.read_sql_query(q_price, conn, parse_dates=['Date'])
                    app.logger.info(f"/api/etf/series shares: df_price rows={len(df_price)}")
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
                            app.logger.warning(f"/api/etf/series shares: merge_asof failed ({me}); falling back to inner merge")
                            df_m = pd.merge(df_hold_sorted, df_price_sorted, on='Date', how='inner')
                        df_m = df_m[df_m['price'].notna()]
                        app.logger.info(f"/api/etf/series shares: merged rows={len(df_m)}")
                        if not df_m.empty:
                            df_m['shares'] = df_m['total_value'] / df_m['price']
                            df_m['time'] = (df_m['Date'].astype(int) // 10**9).astype(int)
                            shares_series = (
                                df_m[['time', 'shares']]
                                .rename(columns={'shares': 'value'})
                                .to_dict(orient='records')
                            )
                            app.logger.info(f"/api/etf/series shares: output points={len(shares_series)}")
            result['shares'] = shares_series

        conn.close()
        return jsonify(result)
    except Exception as e:
        app.logger.error(f"/api/etf/series error: {e}")
        return jsonify({'error': 'failed to compute series'}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
