"""
Intraday chart routes — 30-minute candle charts for ETFs and Hyperliquid perps.

Endpoints:
  /api/chart/intraday   — line chart overlay of intraday candles (PNG)
  /api/chart/intraday/funding — funding rate chart (PNG)
"""

import os
import sys
import json
import sqlite3
import logging
from datetime import datetime, timezone, timedelta

from flask import Blueprint, request, Response, jsonify

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from constants import DB_PATH
from helpers import basedir

logger = logging.getLogger(__name__)
intraday_bp = Blueprint('intraday_bp', __name__)

HTTP_BAD_REQUEST = 400
HTTP_INTERNAL_ERROR = 500

# Color palette matching chart_routes.py
COLORS = [
    '#2962FF', '#E91E63', '#00BCD4', '#FF9800',
    '#4CAF50', '#9C27B0', '#795548', '#607D8B',
]


def _query_candles(conn, ticker, start_ts, end_ts, interval='30m'):
    """Query candle data from the appropriate table based on ticker prefix."""
    if ticker.startswith('HL:'):
        table = 'perp_candles'
    else:
        table = 'intraday_candles'

    rows = conn.execute(f'''
        SELECT timestamp, close FROM {table}
        WHERE ticker = ? AND interval = ? AND timestamp >= ? AND timestamp <= ?
        ORDER BY timestamp ASC
    ''', (ticker, interval, start_ts, end_ts)).fetchall()

    return rows


def _query_funding(conn, ticker, start_ts, end_ts):
    """Query funding rate data."""
    rows = conn.execute('''
        SELECT timestamp, funding_rate, premium FROM perp_funding_rates
        WHERE ticker = ? AND timestamp >= ? AND timestamp <= ?
        ORDER BY timestamp ASC
    ''', (ticker, start_ts, end_ts)).fetchall()
    return rows


def _ts_to_epoch(ts_str):
    """Convert 'YYYY-MM-DD HH:MM:SS' UTC string to Unix epoch seconds."""
    dt = datetime.strptime(ts_str, '%Y-%m-%d %H:%M:%S').replace(tzinfo=timezone.utc)
    return int(dt.timestamp())


@intraday_bp.route('/api/chart/intraday')
def get_intraday_chart():
    """
    Intraday line chart overlay.

    Params:
        tickers: comma-separated (e.g., SPY,HL:SP500 or GLD,HL:GOLD)
        days: lookback in days (default: 7)
        normalize: true/false (default: false)
        primary: ticker to color blue (default: first ticker)
        interval: candle interval (default: 30m)
        width/height: chart dimensions
        title: chart title
        labels: custom labels (TICKER:Label,TICKER2:Label2)
    """
    tickers_param = request.args.get('tickers', '')
    if not tickers_param:
        return jsonify({'error': 'tickers parameter required'}), HTTP_BAD_REQUEST

    tickers = [t.strip() for t in tickers_param.split(',') if t.strip()]
    days = int(request.args.get('days', 7))
    normalize = request.args.get('normalize', 'false').lower() == 'true'
    primary = request.args.get('primary', tickers[0] if tickers else None)
    interval = request.args.get('interval', '30m')
    width = int(request.args.get('width', 1200))
    height = int(request.args.get('height', 800))
    title = request.args.get('title', '')
    show_title = bool(title)

    # Parse custom labels
    labels = {}
    labels_param = request.args.get('labels', '')
    if labels_param:
        for pair in labels_param.split(','):
            if ':' in pair:
                k, v = pair.split(':', 1)
                labels[k.strip()] = v.strip()

    # Time range
    now = datetime.now(timezone.utc)
    start = now - timedelta(days=days)
    start_str = start.strftime('%Y-%m-%d %H:%M:%S')
    end_str = now.strftime('%Y-%m-%d %H:%M:%S')

    # Reorder so primary is first (gets blue)
    if primary and primary in tickers:
        tickers.remove(primary)
        tickers.insert(0, primary)

    # Fetch data
    conn = sqlite3.connect(DB_PATH)
    chart_data = {}

    for ticker in tickers:
        rows = _query_candles(conn, ticker, start_str, end_str, interval)
        if rows:
            points = [{'time': _ts_to_epoch(r[0]), 'value': float(r[1])}
                      for r in rows if r[1] is not None]
            if points:
                chart_data[ticker] = points

    conn.close()

    if not chart_data:
        return jsonify({'error': 'No data found for specified tickers'}), HTTP_BAD_REQUEST

    # Build config
    chart_config = {
        'data': chart_data,
        'title': title,
        'width': width,
        'height': height,
        'showTitle': show_title,
        'showLastDate': False,
        'showLastValue': True,
        'normalize': normalize,
        'forecastStart': None,
        'labels': labels if labels else None,
        'overlay': None,
        'dualAxis': False,
        'primaryTicker': primary,
        'isIntraday': True,
    }

    # Render with Playwright
    template_path = os.path.join(basedir, 'templates', 'chart_render.html')
    if not os.path.exists(template_path):
        return jsonify({'error': 'Chart template not found'}), HTTP_INTERNAL_ERROR

    try:
        from playwright.sync_api import sync_playwright

        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page(viewport={'width': width, 'height': height})
            page.goto(f'file://{template_path}')
            page.evaluate(f'''
                window.CHART_CONFIG = {json.dumps(chart_config)};
                renderChart(window.CHART_CONFIG);
            ''')
            page.wait_for_function('window.chartReady === true', timeout=10000)
            page.wait_for_timeout(200)
            screenshot_bytes = page.screenshot(type='png')
            browser.close()

        return Response(screenshot_bytes, mimetype='image/png')
    except Exception as e:
        logger.error(f"Intraday chart render failed: {e}", exc_info=True)
        return jsonify({'error': str(e)}), HTTP_INTERNAL_ERROR


@intraday_bp.route('/api/chart/intraday/funding')
def get_funding_chart():
    """
    Funding rate chart for Hyperliquid perps.

    Params:
        tickers: comma-separated HL: tickers (e.g., HL:SP500,HL:CL)
        days: lookback (default: 7)
        width/height: chart dimensions
    """
    tickers_param = request.args.get('tickers', '')
    if not tickers_param:
        return jsonify({'error': 'tickers parameter required'}), HTTP_BAD_REQUEST

    tickers = [t.strip() for t in tickers_param.split(',') if t.strip()]
    days = int(request.args.get('days', 7))
    width = int(request.args.get('width', 1200))
    height = int(request.args.get('height', 600))

    now = datetime.now(timezone.utc)
    start = now - timedelta(days=days)
    start_str = start.strftime('%Y-%m-%d %H:%M:%S')
    end_str = now.strftime('%Y-%m-%d %H:%M:%S')

    conn = sqlite3.connect(DB_PATH)
    chart_data = {}

    for ticker in tickers:
        rows = _query_funding(conn, ticker, start_str, end_str)
        if rows:
            # Convert funding rate to bps/hour for readability
            # Raw rate is per-hour decimal (e.g., 0.0001 = 1 bps/hr)
            # Drop extreme outliers (> 10 bps/hr = ~88% annualized)
            points = []
            for r in rows:
                if r[1] is None:
                    continue
                bps = round(float(r[1]) * 10000, 2)  # convert to basis points
                if abs(bps) > 10:
                    continue  # drop outliers rather than clip
                points.append({'time': _ts_to_epoch(r[0]), 'value': bps})
            if points:
                chart_data[ticker] = points

    conn.close()

    if not chart_data:
        return jsonify({'error': 'No funding data found'}), HTTP_BAD_REQUEST

    chart_config = {
        'data': chart_data,
        'title': 'Funding Rate (bps/hour)',
        'width': width,
        'height': height,
        'showTitle': True,
        'showLastDate': False,
        'showLastValue': True,
        'normalize': False,
        'forecastStart': None,
        'labels': None,
        'overlay': None,
        'dualAxis': False,
        'primaryTicker': tickers[0] if tickers else None,
        'isIntraday': True,
    }

    template_path = os.path.join(basedir, 'templates', 'chart_render.html')
    if not os.path.exists(template_path):
        return jsonify({'error': 'Chart template not found'}), HTTP_INTERNAL_ERROR

    try:
        from playwright.sync_api import sync_playwright

        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page(viewport={'width': width, 'height': height})
            page.goto(f'file://{template_path}')
            page.evaluate(f'''
                window.CHART_CONFIG = {json.dumps(chart_config)};
                renderChart(window.CHART_CONFIG);
            ''')
            page.wait_for_function('window.chartReady === true', timeout=10000)
            page.wait_for_timeout(200)
            screenshot_bytes = page.screenshot(type='png')
            browser.close()

        return Response(screenshot_bytes, mimetype='image/png')
    except Exception as e:
        logger.error(f"Funding chart render failed: {e}", exc_info=True)
        return jsonify({'error': str(e)}), HTTP_INTERNAL_ERROR
