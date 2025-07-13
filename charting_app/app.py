import sqlite3
import time
import pandas as pd
import os
import sys
from flask import Flask, jsonify, render_template, request
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

@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '-1'
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
    """Serves the main HTML page."""
    return render_template('index.html')

@app.route('/api/tickers')
def get_tickers():
    """Provides a sorted list of all available tickers from the database."""
    app.logger.info("Request received for /api/tickers")
    try:
        conn = get_db_connection()
        cursor = conn.execute("PRAGMA table_info(stock_prices_daily)")
        all_columns = cursor.fetchall()
        tickers = [row['name'] for row in all_columns if row['name'] != 'Date']
        conn.close()
        app.logger.info(f"Found {len(tickers)} tickers.")
        if not tickers:
            app.logger.warning("WARNING: Ticker list is empty. Check if table 'stock_prices_daily' exists and is populated.")
        return jsonify(sorted(tickers))
    except Exception as e:
        app.logger.error(f"An error occurred in get_tickers: {e}")
        return jsonify([]), 500

@app.route('/api/data')
def get_data():
    """Provides raw historical price data for a list of tickers."""
    tickers_str = request.args.get('tickers')
    if not tickers_str:
        return jsonify({'error': 'At least one ticker is required'}), 400

    tickers = [ticker.strip().upper() for ticker in tickers_str.split(',')]
    
    conn = get_db_connection()
    # Ensure ticker names are quoted to handle potential special characters
    safe_tickers = '", "'.join(tickers)
    # Fetch all data for the requested tickers, ordered by date
    query = f'SELECT Date, "{safe_tickers}" FROM stock_prices_daily ORDER BY Date ASC'
    df = pd.read_sql_query(query, conn, index_col='Date', parse_dates=['Date'])
    conn.close()

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

if __name__ == '__main__':
    app.run(debug=True, port=5000)
