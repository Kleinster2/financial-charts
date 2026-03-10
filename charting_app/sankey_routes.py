"""
Income statement Sankey flow diagram route using D3.js + Playwright.
Route: /api/chart/sankey
"""
import json
import logging
import traceback
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Blueprint, jsonify, request, Response
import pandas as pd
from constants import get_db_connection, HTTP_BAD_REQUEST, HTTP_NOT_FOUND, HTTP_INTERNAL_ERROR, resolve_ticker_alias
from helpers import basedir

logger = logging.getLogger(__name__)

sankey_bp = Blueprint('sankey', __name__)


@sankey_bp.route('/api/chart/sankey')
def get_sankey_chart():
    """Generate an income statement Sankey flow diagram (PNG).

    Query params:
        ticker: Stock ticker (required)
        period: annual or quarterly (default annual)
        date: Specific fiscal_date_ending (optional, defaults to latest)
        width: Image width in pixels (default 1400)
        height: Image height in pixels (default 800)

    Returns: PNG image
    """
    ticker = request.args.get('ticker', '').strip().upper()
    if not ticker:
        return jsonify({'error': 'ticker parameter required'}), HTTP_BAD_REQUEST

    ticker = resolve_ticker_alias(ticker)
    period = request.args.get('period', 'annual').lower()
    date_param = request.args.get('date', '')
    width = int(request.args.get('width', 1400))
    height = int(request.args.get('height', 800))

    if period not in ('annual', 'quarterly'):
        return jsonify({'error': 'period must be annual or quarterly'}), HTTP_BAD_REQUEST

    table = f'income_statement_{period}'

    try:
        conn = get_db_connection()

        cols = """fiscal_date_ending, total_revenue, cost_of_revenue,
                  gross_profit, operating_income, net_income,
                  research_and_development, selling_general_administrative,
                  interest_expense, income_tax_expense"""

        if date_param:
            query = f"SELECT {cols} FROM {table} WHERE ticker = ? AND fiscal_date_ending = ? LIMIT 1"
            df = pd.read_sql(query, conn, params=(ticker, date_param))
        else:
            query = f"SELECT {cols} FROM {table} WHERE ticker = ? ORDER BY fiscal_date_ending DESC LIMIT 1"
            df = pd.read_sql(query, conn, params=(ticker,))

        conn.close()

        if df.empty:
            return jsonify({'error': f'No income statement data for {ticker}'}), HTTP_NOT_FOUND

        row = df.iloc[0]
        fiscal_date = row['fiscal_date_ending']

        def _val(col):
            return float(row[col]) if col in row.index and pd.notna(row[col]) else 0

        revenue = _val('total_revenue')
        cogs = _val('cost_of_revenue')
        gross_profit = _val('gross_profit')
        operating_income = _val('operating_income')
        net_income = _val('net_income')
        rd = _val('research_and_development')
        sga = _val('selling_general_administrative')
        interest = _val('interest_expense')
        tax = _val('income_tax_expense')

        if gross_profit == 0 and revenue > 0 and cogs > 0:
            gross_profit = revenue - cogs

        has_opex_detail = rd > 0 or sga > 0
        has_below_detail = interest > 0 or tax > 0
        total_opex = gross_profit - operating_income
        other_opex = max(0, total_opex - rd - sga) if has_opex_detail else total_opex
        total_below = operating_income - net_income
        other_below = max(0, total_below - interest - tax) if has_below_detail else total_below

        # Build nodes with column assignments
        # Col 0: Revenue
        # Col 1: COGS, Gross Profit
        # Col 2: OpEx items, Operating Income
        # Col 3: Below-line items, Net Income
        nodes = [
            {'id': 'revenue', 'name': 'Revenue', 'value': revenue, 'nodeType': 'revenue', 'col': 0},
            {'id': 'cogs', 'name': 'COGS', 'value': cogs, 'nodeType': 'cost', 'col': 1},
            {'id': 'gross', 'name': 'Gross Profit', 'value': gross_profit, 'nodeType': 'gross', 'col': 1},
        ]

        # Links: ORDER MATTERS — costs first, then profit (so costs stack on top in the ribbon layout)
        links = [
            {'source': 'revenue', 'target': 'cogs', 'value': cogs, 'type': 'cost'},
            {'source': 'revenue', 'target': 'gross', 'value': gross_profit, 'type': 'profit'},
        ]

        # Column 2: OpEx breakdown
        if has_opex_detail:
            if rd > 0:
                nodes.append({'id': 'rd', 'name': 'R&D', 'value': rd, 'nodeType': 'cost', 'col': 2})
                links.append({'source': 'gross', 'target': 'rd', 'value': rd, 'type': 'cost'})
            if sga > 0:
                nodes.append({'id': 'sga', 'name': 'SG&A', 'value': sga, 'nodeType': 'cost', 'col': 2})
                links.append({'source': 'gross', 'target': 'sga', 'value': sga, 'type': 'cost'})
            if other_opex > revenue * 0.005:
                nodes.append({'id': 'other_opex', 'name': 'Other OpEx', 'value': other_opex, 'nodeType': 'cost', 'col': 2})
                links.append({'source': 'gross', 'target': 'other_opex', 'value': other_opex, 'type': 'cost'})
        else:
            if total_opex > 0:
                nodes.append({'id': 'opex', 'name': 'OpEx', 'value': total_opex, 'nodeType': 'cost', 'col': 2})
                links.append({'source': 'gross', 'target': 'opex', 'value': total_opex, 'type': 'cost'})

        nodes.append({'id': 'operating', 'name': 'Operating Income', 'value': operating_income, 'nodeType': 'operating', 'col': 2})
        links.append({'source': 'gross', 'target': 'operating', 'value': operating_income, 'type': 'profit'})

        # Column 3: Below-the-line
        if has_below_detail:
            if interest > 0:
                nodes.append({'id': 'interest', 'name': 'Interest', 'value': interest, 'nodeType': 'cost', 'col': 3})
                links.append({'source': 'operating', 'target': 'interest', 'value': interest, 'type': 'cost'})
            if tax > 0:
                nodes.append({'id': 'tax', 'name': 'Tax', 'value': tax, 'nodeType': 'cost', 'col': 3})
                links.append({'source': 'operating', 'target': 'tax', 'value': tax, 'type': 'cost'})
            if other_below > revenue * 0.005:
                nodes.append({'id': 'other_below', 'name': 'Other', 'value': other_below, 'nodeType': 'cost', 'col': 3})
                links.append({'source': 'operating', 'target': 'other_below', 'value': other_below, 'type': 'cost'})
        else:
            if total_below > 0:
                nodes.append({'id': 'below', 'name': 'Tax & Other', 'value': total_below, 'nodeType': 'cost', 'col': 3})
                links.append({'source': 'operating', 'target': 'below', 'value': total_below, 'type': 'cost'})

        nodes.append({'id': 'net', 'name': 'Net Income', 'value': net_income, 'nodeType': 'net', 'col': 3})
        links.append({'source': 'operating', 'target': 'net', 'value': net_income, 'type': 'net'})

        # Margins
        gross_margin = gross_profit / revenue * 100 if revenue else 0
        op_margin = operating_income / revenue * 100 if revenue else 0
        net_margin = net_income / revenue * 100 if revenue else 0

        period_label = 'FY' if period == 'annual' else 'Q'
        title = f"{ticker} Income Statement — {period_label} {fiscal_date}"
        margin_summary = f"Gross: {gross_margin:.1f}%  |  Operating: {op_margin:.1f}%  |  Net: {net_margin:.1f}%"

        config = {
            'nodes': nodes,
            'links': links,
            'title': title,
            'marginSummary': margin_summary,
            'width': width,
            'height': height,
        }

        # Read HTML template
        template_path = os.path.join(basedir, 'templates', 'sankey_render.html')
        with open(template_path, 'r', encoding='utf-8') as f:
            html_template = f.read()

        # Inject config
        config_json = json.dumps(config)
        html = html_template.replace(
            'if (window.SANKEY_CONFIG) render(window.SANKEY_CONFIG);',
            f'window.SANKEY_CONFIG = {config_json}; render(window.SANKEY_CONFIG);'
        )

        # Render with Playwright
        from playwright.sync_api import sync_playwright
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page(viewport={'width': width, 'height': height})
            page.set_content(html)
            page.wait_for_function('window.chartReady === true', timeout=10000)
            img_bytes = page.screenshot(type='png')
            browser.close()

        return Response(img_bytes, mimetype='image/png')

    except Exception as e:
        logger.error(f"Sankey chart error: {e}")
        traceback.print_exc()
        return jsonify({'error': str(e)}), HTTP_INTERNAL_ERROR
