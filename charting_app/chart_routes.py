"""
Chart image generation routes.
Routes: /api/chart/image, /api/chart/lw, /api/chart/segment
"""
import io
import json
import logging
import traceback
import sys
import os
from datetime import datetime, timedelta

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

from flask import Blueprint, jsonify, request, Response
import pandas as pd
from constants import (get_db_connection, HTTP_BAD_REQUEST, HTTP_NOT_FOUND,
                      HTTP_INTERNAL_ERROR, resolve_ticker_alias)
from helpers import basedir, _check_playwright, fiscal_to_calendar_quarter

logger = logging.getLogger(__name__)

chart_bp = Blueprint('chart', __name__)


# --- Chart Image Export Endpoint ---
@chart_bp.route('/api/chart/image')
def get_chart_image():
    """Generate a chart image (PNG) for given ticker(s).

    Query params:
        ticker: Stock ticker (required), e.g., AAPL
        start: Start date (optional), e.g., 2024-01-01
        end: End date (optional), e.g., 2025-01-01
        title: Chart title (optional)
        width: Image width in inches (optional, default 10)
        height: Image height in inches (optional, default 6)

    Returns: PNG image
    """
    ticker = request.args.get('ticker', '').strip().upper()
    if not ticker:
        return jsonify({'error': 'ticker parameter required'}), HTTP_BAD_REQUEST

    # Resolve alias
    ticker = resolve_ticker_alias(ticker)

    start_date = request.args.get('start', '')
    end_date = request.args.get('end', '')
    title = request.args.get('title', ticker)
    width = float(request.args.get('width', 10))
    height = float(request.args.get('height', 6))
    log_scale = request.args.get('log', '').lower() in ('true', '1', 'yes')
    label = request.args.get('label', ticker)
    markers = request.args.get('markers', '').lower() in ('true', '1', 'yes')
    point_labels_raw = request.args.get('point_labels', '')  # comma-separated labels for each data point

    try:
        conn = get_db_connection()

        # Wide format table: Date column + ticker columns
        # Check if ticker column exists in stock_prices_daily or futures_prices_daily
        cursor = conn.cursor()
        cursor.execute("PRAGMA table_info(stock_prices_daily)")
        stock_columns = [row[1] for row in cursor.fetchall()]

        cursor.execute("PRAGMA table_info(futures_prices_daily)")
        futures_columns = [row[1] for row in cursor.fetchall()]

        if ticker in stock_columns:
            source_table = 'stock_prices_daily'
        elif ticker in futures_columns:
            source_table = 'futures_prices_daily'
        else:
            conn.close()
            return jsonify({'error': f'Ticker {ticker} not found in database'}), HTTP_NOT_FOUND

        # Build query for wide format
        query = f'SELECT Date, "{ticker}" FROM {source_table} WHERE "{ticker}" IS NOT NULL'
        params = []

        if start_date:
            query += " AND Date >= ?"
            params.append(start_date)
        if end_date:
            query += " AND Date <= ?"
            params.append(end_date)

        query += " ORDER BY Date"

        df = pd.read_sql_query(query, conn, params=params)
        conn.close()

        if df.empty:
            return jsonify({'error': f'No data found for {ticker}'}), HTTP_NOT_FOUND

        # Rename columns
        df.columns = ['Date', 'Close']
        df['Date'] = pd.to_datetime(df['Date'])
        df['Close'] = pd.to_numeric(df['Close'], errors='coerce')
        df = df.dropna()

        # Create chart
        fig, ax = plt.subplots(figsize=(width, height))
        fig.patch.set_facecolor('#ffffff')
        ax.set_facecolor('#ffffff')
        ax.plot(df['Date'], df['Close'], linewidth=3, color='#2962FF')

        # Markers and point labels
        if markers or point_labels_raw:
            ax.scatter(df['Date'], df['Close'], color='#2962FF', s=60, zorder=4,
                       edgecolors='white', linewidths=0.8)

        if point_labels_raw:
            point_labels_list = [l.strip() for l in point_labels_raw.split(',')]
            n = len(df)
            for i, (_, row) in enumerate(df.iterrows()):
                if i < len(point_labels_list) and point_labels_list[i]:
                    text = point_labels_list[i]
                    price = row['Close']
                    # Alternate left/right, horizontally aligned with dot
                    if i % 2 == 0:
                        xytext, ha = (12, 0), 'left'
                    else:
                        xytext, ha = (-12, 0), 'right'
                    ax.annotate(text, (row['Date'], price),
                                textcoords='offset points', xytext=xytext,
                                fontsize=12, color='#555', ha=ha, va='center')

        # Log scale if requested
        if log_scale:
            ax.set_yscale('log')
            ax.yaxis.set_major_formatter(plt.FuncFormatter(
                lambda x, p: f'${x:,.0f}' if x >= 1 else f'${x:.2f}'))

        # Style
        ax.set_xlabel('')
        ax.grid(True, alpha=0.3, color='#ddd', which='major')
        if log_scale:
            ax.grid(True, alpha=0.15, color='#eee', which='minor')
        ax.tick_params(colors='#333', labelsize=18)
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
        ax.xaxis.set_major_locator(mdates.AutoDateLocator())
        ax.yaxis.tick_right()
        ax.yaxis.set_label_position('right')
        ax.spines['top'].set_visible(False)
        ax.spines['left'].set_visible(False)
        ax.spines['right'].set_color('#ccc')
        ax.spines['bottom'].set_color('#ccc')

        # Reference grid lines
        if log_scale:
            ax.axhline(y=1000, color='#bbb', linewidth=1, linestyle='--', zorder=1)
        fig.autofmt_xdate()

        # Legend label
        ax.text(0.02, 0.95, label, transform=ax.transAxes,
                fontsize=24, fontweight=600, color='#2962FF', va='top', ha='left',
                bbox=dict(boxstyle='round,pad=0.4', facecolor=(1, 1, 1, 0.9), edgecolor='none'))

        # Last date
        last_date = df['Date'].iloc[-1]
        date_str = last_date.strftime('%b %d, %Y')
        ax.text(0.02, 0.87, date_str, transform=ax.transAxes,
                fontsize=16, color='#666', va='top', ha='left')

        # Watermark
        ax.text(0.99, 0.01, 'Financial Charts', transform=ax.transAxes, fontsize=13,
                color=(0, 0, 0, 0.3), va='bottom', ha='right')

        # Add price annotation (skip if point_labels already label everything)
        last_price = df['Close'].iloc[-1]
        if not point_labels_raw:
            ax.annotate(f'${last_price:.2f}', xy=(last_date, last_price),
                       xytext=(10, 0), textcoords='offset points',
                       fontsize=16, fontweight='bold', color='#2962FF')

        plt.tight_layout()

        # Save to buffer
        buf = io.BytesIO()
        fig.savefig(buf, format='png', dpi=150, bbox_inches='tight',
                   facecolor='white', edgecolor='none')
        buf.seek(0)
        plt.close(fig)

        return Response(buf.getvalue(), mimetype='image/png')

    except Exception as e:
        logger.error(f"Chart image error: {e}")
        traceback.print_exc()
        return jsonify({'error': str(e)}), HTTP_INTERNAL_ERROR


# --- Lightweight Charts Image Export Endpoint ---
# Requires: pip install playwright && playwright install chromium

@chart_bp.route('/api/chart/lw')
def get_chart_lw():
    """Generate a chart image using Lightweight Charts (same style as dashboard).

    Query params:
        tickers: Comma-separated tickers (required), e.g., AAPL,MSFT
        start: Start date (optional), e.g., 2024-01-01
        end: End date (optional), e.g., 2025-01-01
        title: Chart title (optional)
        width: Image width in pixels (optional, default 1200)
        height: Image height in pixels (optional, default 600)
        show_title: Show title on chart (optional, default true)
        show_last_date: Show last data date in bottom-left (optional, default true)
        normalize: Rebase all tickers to 0% at start (optional, default false)
        metrics: Fundamentals metrics to chart instead of price (optional)
                 Options: revenue, netIncome, eps, fcf, operatingIncome, ebitda, grossProfit
        forecast_start: Date to begin dotted forecast line (optional), e.g., 2026-01-01
        labels: Custom legend labels (optional), e.g., SMH_1_44X:SMH 1.44x Lev,NVDA:NVIDIA
        sort_by_last: Sort series by last value, high to low (optional, default false)
        primary: Primary ticker to assign first color (optional), e.g., AAPL

    Returns: PNG image
    """
    if not _check_playwright():
        return jsonify({
            'error': 'Playwright not installed. Run: pip install playwright && playwright install chromium'
        }), HTTP_INTERNAL_ERROR

    from playwright.sync_api import sync_playwright

    tickers_param = request.args.get('tickers', '').strip().upper()
    product_param_early = request.args.get('product', '').strip()  # Check early for product mode

    # tickers required unless in product mode
    if not tickers_param and not product_param_early:
        return jsonify({'error': 'tickers parameter required (or use product parameter)'}), HTTP_BAD_REQUEST

    # Parse and resolve tickers (may be empty for product mode)
    tickers = [resolve_ticker_alias(t.strip()) for t in tickers_param.split(',') if t.strip()] if tickers_param else []

    start_date = request.args.get('start', '')
    end_date = request.args.get('end', '')
    title = request.args.get('title', ', '.join(tickers) if tickers else product_param_early or 'Chart')
    width = int(request.args.get('width', 1200))
    height = int(request.args.get('height', 800))
    show_title = request.args.get('show_title', 'false').lower() == 'true'
    show_last_date = request.args.get('show_last_date', 'true').lower() != 'false'
    normalize = request.args.get('normalize', 'false').lower() == 'true'

    # Default to 8 years for normalized charts if no start date specified
    if normalize and not start_date:
        start_date = (datetime.now() - timedelta(days=8*365)).strftime('%Y-%m-%d')
    forecast_start = request.args.get('forecast_start', '').strip()  # Date to start dotted forecast line
    labels_param = request.args.get('labels', '').strip()  # Custom legend labels: TICKER:Label,TICKER2:Label2
    show_last_value = request.args.get('show_last_value', 'false').lower() == 'true'  # Show last price label on chart
    sort_by_last = request.args.get('sort_by_last', 'false').lower() == 'true'  # Sort series by last value (high to low)
    primary_ticker = request.args.get('primary', '').strip().upper()  # Primary ticker gets first color (index 0)
    dual_axis = request.args.get('dual_axis', 'false').lower() == 'true'  # Put non-primary tickers on left y-axis

    # Parse custom labels
    labels = {}
    if labels_param:
        for pair in labels_param.split(','):
            if ':' in pair:
                key, val = pair.split(':', 1)
                labels[key.strip().upper()] = val.strip()

    overlay_param = request.args.get('overlay', '').strip().lower()  # e.g., overlay=si for short interest

    metrics_param = request.args.get('metrics', '').strip().lower()
    combine_panes = request.args.get('combine', 'false').lower() == 'true'  # Combine multiple metrics into single pane
    product_param = product_param_early  # Already parsed above
    product_metrics_param = request.args.get('product_metrics', '').strip().lower()  # e.g., global_mau,revenue

    # Product metrics mapping
    product_metric_map = {
        'global_mau': ('Global MAU', 'M'),
        'us_mau': ('US MAU', 'M'),
        'revenue': ('Revenue', 'B'),
        'dau': ('DAU', 'M'),
        'memory_gb': ('Memory', 'GB'),
        'bandwidth_tb': ('Bandwidth', 'TB/s'),
    }

    # Handle product metrics (e.g., TikTok MAU/DAU/Revenue)
    if product_param and product_metrics_param:
        prod_metrics = [m.strip() for m in product_metrics_param.split(',') if m.strip() in product_metric_map]
        if not prod_metrics:
            return jsonify({'error': f'No valid product metrics. Options: {", ".join(product_metric_map.keys())}'}), HTTP_BAD_REQUEST

        try:
            conn = get_db_connection()
            chart_data = {}

            for metric in prod_metrics:
                label, unit = product_metric_map[metric]
                series_name = f"{product_param} {label}"

                query = """
                    SELECT date, value
                    FROM product_metrics
                    WHERE product = ? AND metric = ?
                """
                params = [product_param, metric]
                if start_date:
                    query += " AND date >= ?"
                    params.append(start_date)
                if end_date:
                    query += " AND date <= ?"
                    params.append(end_date)
                query += " ORDER BY date ASC"

                df = pd.read_sql(query, conn, params=params)

                if not df.empty:
                    data_points = []
                    for _, row in df.iterrows():
                        try:
                            date_str = pd.to_datetime(row['date']).strftime('%Y-%m-%d')
                            value = row['value']
                            if pd.notna(value):
                                data_points.append({'time': date_str, 'value': float(value)})
                        except Exception:
                            continue
                    if data_points:
                        chart_data[series_name] = data_points

            conn.close()

            if not chart_data:
                return jsonify({'error': f'No product metrics data found for {product_param}'}), HTTP_NOT_FOUND

            # Build pane groups for multi-metric charts
            pane_groups = {}
            if len(prod_metrics) > 1:
                for metric in prod_metrics:
                    label, _ = product_metric_map[metric]
                    matching_series = [s for s in chart_data.keys() if label in s]
                    if matching_series:
                        pane_groups[label] = matching_series

            # Update title if not custom
            if title == ', '.join(tickers):
                metric_labels = [product_metric_map[m][0] for m in prod_metrics]
                title = f"{product_param} — {', '.join(metric_labels)}"

            chart_config = {
                'data': chart_data,
                'title': title,
                'width': width,
                'height': height,
                'showTitle': show_title,
                'showLastDate': show_last_date,
                'showLastValue': show_last_value,
                'normalize': normalize,
                'isFundamentals': True,  # Use bar chart style
                'forecastStart': forecast_start if forecast_start else None,
                'labels': labels if labels else None,
                'separatePanes': len(prod_metrics) > 1,
                'paneGroups': pane_groups if pane_groups else None
            }

            # Render with Playwright
            from playwright.sync_api import sync_playwright
            template_path = os.path.join(basedir, 'templates', 'chart_render.html')

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
            logger.error(f"Product metrics chart error: {e}")
            traceback.print_exc()
            return jsonify({'error': str(e)}), HTTP_INTERNAL_ERROR

    # Fundamentals metric mapping
    metric_map = {
        'revenue': ('income_statement_quarterly', 'total_revenue', 'Revenue'),
        'netincome': ('income_statement_quarterly', 'net_income', 'Net Income'),
        'eps': ('earnings_quarterly', 'reported_eps', 'EPS'),
        'fcf': ('cash_flow_quarterly', 'free_cash_flow', 'Free Cash Flow'),
        'ocf': ('cash_flow_quarterly', 'operating_cashflow', 'Operating CF'),
        'operatingincome': ('income_statement_quarterly', 'operating_income', 'Op Income'),
        'ebitda': ('income_statement_quarterly', 'ebitda', 'EBITDA'),
        'grossprofit': ('income_statement_quarterly', 'gross_profit', 'Gross Profit'),
        'capex': ('cash_flow_quarterly', 'capital_expenditures', 'CapEx'),
        'dividends': ('cash_flow_quarterly', 'dividend_payout', 'Dividends'),
        'buybacks': ('cash_flow_quarterly', 'share_repurchases', 'Buybacks'),
        'cash': ('balance_sheet_quarterly', 'IFNULL(cash_and_equivalents,0) + IFNULL(short_term_investments,0)', 'Cash Position'),
        'employees': ('employee_count', 'employees', 'Employees'),
    }

    # If metrics specified, fetch fundamentals instead of price
    if metrics_param:
        metrics = [m.strip() for m in metrics_param.split(',') if m.strip() in metric_map]
        if not metrics:
            return jsonify({'error': f'No valid metrics. Options: {", ".join(metric_map.keys())}'}), HTTP_BAD_REQUEST

        try:
            conn = get_db_connection()
            chart_data = {}

            for ticker in tickers:
                for metric in metrics:
                    table, column, label = metric_map[metric]
                    series_name = f"{ticker} {label}" if len(tickers) > 1 or len(metrics) > 1 else label

                    # Build query with optional date filters (alias column as 'metric_value' for expressions)
                    # Skip date('now') filter if forecast_start is provided (allows future forecast data)
                    query = f"""
                        SELECT fiscal_date_ending, ({column}) as metric_value
                        FROM {table}
                        WHERE ticker = ?
                    """
                    if not forecast_start:
                        query += " AND fiscal_date_ending <= date('now')"
                    params = [ticker]
                    if start_date:
                        query += " AND fiscal_date_ending >= ?"
                        params.append(start_date)
                    if end_date:
                        query += " AND fiscal_date_ending <= ?"
                        params.append(end_date)
                    query += " ORDER BY fiscal_date_ending ASC"
                    df = pd.read_sql(query, conn, params=params)

                    if not df.empty:
                        data_points = []
                        for _, row in df.iterrows():
                            try:
                                date_str = fiscal_to_calendar_quarter(row['fiscal_date_ending'])
                                value = row['metric_value']
                                if pd.notna(value) and value != 0:
                                    data_points.append({'time': date_str, 'value': float(value)})
                            except Exception:
                                continue
                        if data_points:
                            chart_data[series_name] = data_points

            conn.close()

            if not chart_data:
                return jsonify({'error': 'No fundamentals data found'}), HTTP_NOT_FOUND

            # Sort series by last value (high to low) if requested
            if sort_by_last and chart_data:
                def get_last_value(series_name):
                    points = chart_data.get(series_name, [])
                    if not points:
                        return float('-inf')
                    return points[-1]['value'] if points else float('-inf')

                sorted_names = sorted(chart_data.keys(), key=get_last_value, reverse=True)
                chart_data = {n: chart_data[n] for n in sorted_names}

            # Ensure primary ticker series are first (gets color index 0)
            # For fundamentals, series names include metric (e.g., "AAPL Revenue")
            if primary_ticker and chart_data:
                primary_series = [n for n in chart_data.keys() if n.startswith(primary_ticker)]
                other_series = [n for n in chart_data.keys() if not n.startswith(primary_ticker)]
                if primary_series:
                    chart_data = {**{n: chart_data[n] for n in primary_series},
                                  **{n: chart_data[n] for n in other_series}}

            # Update title if not custom
            if title == ', '.join(tickers):
                metric_labels = [metric_map[m][2] for m in metrics]
                title = f"{', '.join(tickers)} — {', '.join(metric_labels)}"

            # Build pane groups for multi-metric charts (separate panes for each metric)
            pane_groups = {}
            if len(metrics) > 1:
                for metric in metrics:
                    label = metric_map[metric][2]
                    # Find all series for this metric
                    matching_series = [s for s in chart_data.keys() if label in s]
                    if matching_series:
                        pane_groups[label] = matching_series

            chart_config = {
                'data': chart_data,
                'title': title,
                'width': width,
                'height': height,
                'showTitle': show_title,
                'showLastDate': show_last_date,
                'showLastValue': show_last_value,
                'normalize': normalize,
                'isFundamentals': True,
                'forecastStart': forecast_start if forecast_start else None,
                'labels': labels if labels else None,
                'separatePanes': len(metrics) > 1 and not combine_panes,
                'paneGroups': pane_groups if (pane_groups and not combine_panes) else None
            }

            # Render with Playwright
            from playwright.sync_api import sync_playwright
            template_path = os.path.join(basedir, 'templates', 'chart_render.html')

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
            logger.error(f"Fundamentals chart error: {e}")
            traceback.print_exc()
            return jsonify({'error': str(e)}), HTTP_INTERNAL_ERROR

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # Get available columns from all wide-format price tables
        stock_cols = set()
        futures_cols = set()
        fred_cols = set()
        for tbl, col_set in [('stock_prices_daily', stock_cols),
                             ('futures_prices_daily', futures_cols),
                             ('fred_series', fred_cols)]:
            try:
                cursor.execute(f"PRAGMA table_info({tbl})")
                col_set.update(row[1] for row in cursor.fetchall())
            except Exception:
                pass

        # Assign each ticker to its source table
        table_tickers = {}  # table_name -> [ticker, ...]
        for t in tickers:
            if t in futures_cols and t.endswith('=F'):
                table_tickers.setdefault('futures_prices_daily', []).append(t)
            elif t in stock_cols:
                table_tickers.setdefault('stock_prices_daily', []).append(t)
            elif t in futures_cols:
                table_tickers.setdefault('futures_prices_daily', []).append(t)
            elif t in fred_cols:
                table_tickers.setdefault('fred_series', []).append(t)

        valid_tickers = [t for group in table_tickers.values() for t in group]
        if not valid_tickers:
            conn.close()
            return jsonify({'error': f'No valid tickers found. Requested: {tickers}'}), HTTP_NOT_FOUND

        # Query each table and merge on Date
        dfs = []
        for table_name, t_list in table_tickers.items():
            columns_sql = ', '.join([f'"{t}"' for t in t_list])
            query = f'SELECT Date, {columns_sql} FROM {table_name} WHERE 1=1'
            params = []
            if start_date:
                query += " AND Date >= ?"
                params.append(start_date)
            if end_date:
                query += " AND Date <= ?"
                params.append(end_date)
            query += " ORDER BY Date"
            dfs.append(pd.read_sql_query(query, conn, params=params))

        conn.close()

        if len(dfs) == 1:
            df = dfs[0]
        else:
            # Normalize Date columns to date-only strings for merge
            for d in dfs:
                d['Date'] = pd.to_datetime(d['Date']).dt.strftime('%Y-%m-%d')
            df = dfs[0]
            for d in dfs[1:]:
                df = df.merge(d, on='Date', how='outer')
            df = df.sort_values('Date').reset_index(drop=True)

        if df.empty:
            return jsonify({'error': 'No data found for specified tickers/date range'}), HTTP_NOT_FOUND

        # Convert to chart data format: { AAPL: [{time, value}, ...], MSFT: [...] }
        # Use date strings (YYYY-MM-DD) which Lightweight Charts handles well
        chart_data = {}
        seen_dates = set()  # Track dates to skip duplicates
        for ticker in valid_tickers:
            ticker_df = df[['Date', ticker]].dropna()
            if not ticker_df.empty:
                ticker_points = []
                for _, row in ticker_df.iterrows():
                    # Convert to date string, skip duplicates
                    date_str = pd.to_datetime(row['Date']).strftime('%Y-%m-%d')
                    date_key = (ticker, date_str)
                    if date_key not in seen_dates:
                        seen_dates.add(date_key)
                        ticker_points.append({
                            'time': date_str,
                            'value': float(row[ticker])
                        })
                if ticker_points:
                    chart_data[ticker] = ticker_points

        if not chart_data:
            return jsonify({'error': 'No valid data after processing'}), HTTP_NOT_FOUND

        # Sort series by last value (high to low) if requested
        if sort_by_last and chart_data:
            # For normalized charts, find common start date (latest start across all tickers)
            # This matches the JavaScript normalization logic in chart_render.html
            common_start = None
            if normalize:
                start_dates = []
                for ticker, points in chart_data.items():
                    if points:
                        start_dates.append(points[0]['time'])
                if start_dates:
                    common_start = max(start_dates)  # Latest start = common start

            def get_sort_value(ticker):
                points = chart_data.get(ticker, [])
                if not points or len(points) < 2:
                    return float('-inf')
                if normalize and common_start:
                    # Find value at common start date (first point >= common_start)
                    base_val = None
                    for p in points:
                        if p['time'] >= common_start:
                            base_val = p['value']
                            break
                    last_val = points[-1]['value']
                    if base_val and base_val != 0:
                        return ((last_val - base_val) / base_val) * 100
                    return float('-inf')
                else:
                    # For raw charts, sort by last value
                    return points[-1]['value']

            sorted_tickers = sorted(chart_data.keys(), key=get_sort_value, reverse=True)
            chart_data = {t: chart_data[t] for t in sorted_tickers}

        # Ensure primary ticker is first (gets color index 0)
        if primary_ticker and primary_ticker in chart_data:
            chart_data = {primary_ticker: chart_data[primary_ticker],
                          **{t: v for t, v in chart_data.items() if t != primary_ticker}}

        # Fetch overlay data (short interest)
        overlay_config = None
        if overlay_param == 'si' and chart_data:
            try:
                si_conn = get_db_connection()
                si_cursor = si_conn.cursor()
                overlay_data = {}

                for ticker in chart_data.keys():
                    si_cursor.execute('''
                        SELECT settlement_date, short_percent_float
                        FROM short_interest
                        WHERE ticker = ? AND short_percent_float IS NOT NULL
                        ORDER BY settlement_date ASC
                    ''', (ticker,))
                    si_rows = si_cursor.fetchall()

                    if not si_rows:
                        continue

                    # Build SI lookup: list of (date, value as percentage)
                    # DB stores as ratio (0.05 = 5%), convert to percentage for display
                    si_points = [(row[0], float(row[1]) * 100) for row in si_rows]

                    # Forward-fill: for each price date, find most recent SI value
                    price_dates = [pt['time'] for pt in chart_data[ticker]]
                    filled_points = []
                    si_idx = 0

                    for price_date in price_dates:
                        # Advance si_idx to the last SI point <= price_date
                        while si_idx < len(si_points) - 1 and si_points[si_idx + 1][0] <= price_date:
                            si_idx += 1

                        # Only include if we have an SI point at or before this date
                        if si_points[si_idx][0] <= price_date:
                            filled_points.append({
                                'time': price_date,
                                'value': si_points[si_idx][1]
                            })

                    if filled_points:
                        series_label = f"{ticker} SI%" if len(chart_data) > 1 else "SI %"
                        overlay_data[series_label] = filled_points

                si_conn.close()

                if overlay_data:
                    overlay_config = {
                        'type': 'si',
                        'data': overlay_data,
                        'label': 'SI % Float'
                    }
            except Exception as e:
                logger.warning(f"Failed to fetch SI overlay data: {e}")

        # Prepare config for the HTML template
        chart_config = {
            'data': chart_data,
            'title': title,
            'width': width,
            'height': height,
            'showTitle': show_title,
            'showLastDate': show_last_date,
            'showLastValue': show_last_value,
            'normalize': normalize,
            'forecastStart': forecast_start if forecast_start else None,
            'labels': labels if labels else None,
            'overlay': overlay_config,
            'dualAxis': dual_axis,
            'primaryTicker': primary_ticker if primary_ticker else None
        }
        # Get the HTML template path
        template_path = os.path.join(basedir, 'templates', 'chart_render.html')
        if not os.path.exists(template_path):
            return jsonify({'error': 'Chart template not found'}), HTTP_INTERNAL_ERROR

        # Render with Playwright
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page(viewport={'width': width, 'height': height})

            # Load the HTML template
            page.goto(f'file://{template_path}')

            # Inject the chart configuration and render
            page.evaluate(f'''
                window.CHART_CONFIG = {json.dumps(chart_config)};
                renderChart(window.CHART_CONFIG);
            ''')

            # Wait for chart to render
            page.wait_for_function('window.chartReady === true', timeout=10000)

            # Small delay for any animations to complete
            page.wait_for_timeout(200)

            # Take screenshot
            screenshot_bytes = page.screenshot(type='png')

            browser.close()

        return Response(screenshot_bytes, mimetype='image/png')

    except Exception as e:
        logger.error(f"Lightweight Charts image error: {e}")
        traceback.print_exc()
        return jsonify({'error': str(e)}), HTTP_INTERNAL_ERROR


@chart_bp.route('/api/chart/segment')
def get_chart_segment():
    """Generate segment-level charts from segment_quarterly table.

    Query params:
        ticker: Ticker symbol (required), e.g., GOOGL
        segments: Comma-separated segments (required), e.g., cloud,services
        metric: Metric to chart (required): revenue, operating_income, margin
        width: Image width (optional, default 1200)
        height: Image height (optional, default 600)
        title: Chart title (optional)
        chart_type: line or bar (optional, default line)

    Returns: PNG image
    """
    if not _check_playwright():
        return jsonify({
            'error': 'Playwright not installed. Run: pip install playwright && playwright install chromium'
        }), HTTP_INTERNAL_ERROR

    from playwright.sync_api import sync_playwright

    ticker = request.args.get('ticker', '').strip().upper()
    if not ticker:
        return jsonify({'error': 'ticker parameter required'}), HTTP_BAD_REQUEST

    segments_param = request.args.get('segments', '').strip().lower()
    if not segments_param:
        return jsonify({'error': 'segments parameter required'}), HTTP_BAD_REQUEST

    metric = request.args.get('metric', '').strip().lower()
    if not metric:
        return jsonify({'error': 'metric parameter required (revenue, operating_income, margin)'}), HTTP_BAD_REQUEST

    segments = [s.strip() for s in segments_param.split(',') if s.strip()]
    width = int(request.args.get('width', 1200))
    height = int(request.args.get('height', 600))
    title = request.args.get('title', '')
    chart_type = request.args.get('chart_type', 'line').lower()

    # Metric labels
    metric_labels = {
        'revenue': 'Revenue ($B)',
        'operating_income': 'Operating Income ($B)',
        'margin': 'Margin (%)',
    }

    try:
        conn = get_db_connection()
        chart_data = {}

        for segment in segments:
            display_name = segment.replace('_', ' ').title()

            query = """
                SELECT fiscal_date_ending, value
                FROM segment_quarterly
                WHERE ticker = ? AND segment = ? AND metric = ?
                ORDER BY fiscal_date_ending ASC
            """
            df = pd.read_sql(query, conn, params=[ticker, segment, metric])

            if not df.empty:
                data_points = []
                for _, row in df.iterrows():
                    try:
                        date_str = pd.to_datetime(row['fiscal_date_ending']).strftime('%Y-%m-%d')
                        value = row['value']
                        if pd.notna(value):
                            data_points.append({'time': date_str, 'value': float(value)})
                    except Exception:
                        continue
                if data_points:
                    chart_data[display_name] = data_points

        conn.close()

        if not chart_data:
            return jsonify({'error': f'No segment data found for {ticker}'}), HTTP_NOT_FOUND

        # Build title if not provided
        if not title:
            metric_label = metric_labels.get(metric, metric.title())
            title = f"{ticker} — {metric_label}"

        chart_config = {
            'data': chart_data,
            'title': title,
            'width': width,
            'height': height,
            'showTitle': False,
            'showLastDate': True,
            'showLastValue': False,
            'normalize': False,
            'isFundamentals': chart_type == 'bar',
            'forecastStart': None,
            'labels': None,
        }

        # Render with Playwright
        template_path = os.path.join(basedir, 'templates', 'chart_render.html')

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
        logger.error(f"Segment chart error: {e}")
        traceback.print_exc()
        return jsonify({'error': str(e)}), HTTP_INTERNAL_ERROR
