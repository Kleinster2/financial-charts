"""
Income statement waterfall chart route.
Route: /api/chart/waterfall
"""
import io
import logging
import traceback
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np

from flask import Blueprint, jsonify, request, Response
import pandas as pd
from constants import get_db_connection, HTTP_BAD_REQUEST, HTTP_NOT_FOUND, HTTP_INTERNAL_ERROR, resolve_ticker_alias

logger = logging.getLogger(__name__)

waterfall_bp = Blueprint('waterfall', __name__)


def _format_billions(value):
    """Format a number as $X.XB or $X.XM."""
    if abs(value) >= 1e9:
        return f"${value / 1e9:.1f}B"
    elif abs(value) >= 1e6:
        return f"${value / 1e6:.0f}M"
    else:
        return f"${value:,.0f}"


def _pct_of_revenue(value, revenue):
    """Return percentage of revenue string."""
    if revenue and revenue != 0:
        return f"{value / revenue * 100:.0f}%"
    return ""


@waterfall_bp.route('/api/chart/waterfall')
def get_waterfall_chart():
    """Generate an income statement waterfall chart (PNG).

    Query params:
        ticker: Stock ticker (required), e.g., AAPL
        period: annual or quarterly (optional, default annual)
        date: Specific fiscal_date_ending (optional, defaults to latest)
        width: Image width in inches (optional, default 12)
        height: Image height in inches (optional, default 7)

    Returns: PNG image

    The chart shows the flow from Revenue -> Gross Profit -> Operating Income -> Net Income,
    with cost bars showing what reduces each level.
    """
    ticker = request.args.get('ticker', '').strip().upper()
    if not ticker:
        return jsonify({'error': 'ticker parameter required'}), HTTP_BAD_REQUEST

    ticker = resolve_ticker_alias(ticker)
    period = request.args.get('period', 'annual').lower()
    date_param = request.args.get('date', '')
    width = float(request.args.get('width', 12))
    height = float(request.args.get('height', 7))

    if period not in ('annual', 'quarterly'):
        return jsonify({'error': 'period must be annual or quarterly'}), HTTP_BAD_REQUEST

    table = f'income_statement_{period}'

    try:
        conn = get_db_connection()

        if date_param:
            query = f"""SELECT fiscal_date_ending, total_revenue, cost_of_revenue,
                        gross_profit, operating_income, net_income
                        FROM {table} WHERE ticker = ? AND fiscal_date_ending = ?
                        LIMIT 1"""
            df = pd.read_sql(query, conn, params=(ticker, date_param))
        else:
            query = f"""SELECT fiscal_date_ending, total_revenue, cost_of_revenue,
                        gross_profit, operating_income, net_income
                        FROM {table} WHERE ticker = ?
                        ORDER BY fiscal_date_ending DESC LIMIT 1"""
            df = pd.read_sql(query, conn, params=(ticker,))

        conn.close()

        if df.empty:
            return jsonify({'error': f'No income statement data for {ticker}'}), HTTP_NOT_FOUND

        row = df.iloc[0]
        fiscal_date = row['fiscal_date_ending']
        revenue = float(row['total_revenue']) if pd.notna(row['total_revenue']) else 0
        cogs = float(row['cost_of_revenue']) if pd.notna(row['cost_of_revenue']) else 0
        gross_profit = float(row['gross_profit']) if pd.notna(row['gross_profit']) else 0
        operating_income = float(row['operating_income']) if pd.notna(row['operating_income']) else 0
        net_income = float(row['net_income']) if pd.notna(row['net_income']) else 0

        # Derived values
        # OpEx = Gross Profit - Operating Income (includes R&D, SG&A, etc.)
        opex = gross_profit - operating_income
        # Below-the-line = Operating Income - Net Income (interest, taxes, other)
        below_line = operating_income - net_income

        # If gross_profit is 0 but we have revenue and cogs, calculate it
        if gross_profit == 0 and revenue > 0 and cogs > 0:
            gross_profit = revenue - cogs

        # Build waterfall data
        # Bars: Revenue (positive), COGS (negative), Gross Profit (subtotal),
        #        OpEx (negative), Operating Income (subtotal),
        #        Below-line (negative), Net Income (final)
        labels = ['Revenue', 'COGS', 'Gross\nProfit', 'OpEx', 'Operating\nIncome',
                  'Tax &\nOther', 'Net\nIncome']
        values = [revenue, -cogs, gross_profit, -opex, operating_income,
                  -below_line, net_income]
        # For waterfall positioning
        # "total" bars start from 0; "delta" bars stack from previous total
        bar_types = ['total', 'delta', 'total', 'delta', 'total', 'delta', 'total']

        # Colors
        color_positive = '#2962FF'  # blue - totals/revenue
        color_subtotal = '#26A69A'  # teal - intermediate totals
        color_negative = '#EF5350'  # red - costs
        color_final = '#2962FF'     # blue - net income

        colors = []
        for i, (val, btype) in enumerate(zip(values, bar_types)):
            if i == 0:  # Revenue
                colors.append(color_positive)
            elif i == len(values) - 1:  # Net Income
                colors.append(color_final)
            elif btype == 'total':  # Subtotals (Gross Profit, Operating Income)
                colors.append(color_subtotal)
            else:  # Costs (negative deltas)
                colors.append(color_negative)

        # Calculate bar bottoms for waterfall effect
        bottoms = []
        bar_heights = []
        for i, (val, btype) in enumerate(zip(values, bar_types)):
            if btype == 'total':
                bottoms.append(0)
                bar_heights.append(val)
            else:
                # Delta bar: hangs from previous total
                prev_total = values[i - 1] if bar_types[i - 1] == 'total' else bottoms[i - 1] + bar_heights[i - 1]
                # For negative deltas, the bar goes down from the previous total
                actual_val = abs(val)
                bottom = prev_total - actual_val
                bottoms.append(bottom)
                bar_heights.append(actual_val)

        # Create figure
        fig, ax = plt.subplots(figsize=(width, height))
        fig.patch.set_facecolor('#ffffff')
        ax.set_facecolor('#ffffff')

        x = np.arange(len(labels))
        bar_width = 0.6

        bars = ax.bar(x, bar_heights, bar_width, bottom=bottoms, color=colors,
                      edgecolor='white', linewidth=1.5, zorder=3)

        # Add value labels on bars
        for i, (bar, val, btype) in enumerate(zip(bars, values, bar_types)):
            display_val = _format_billions(abs(val))
            pct = _pct_of_revenue(abs(val), revenue) if i > 0 else ""

            # Position label
            bar_top = bottoms[i] + bar_heights[i]
            bar_bottom = bottoms[i]

            if btype == 'total' or i == 0:
                # Label above the bar
                label_y = bar_top
                va = 'bottom'
            else:
                # Cost bars: label in the middle of the bar
                label_y = (bar_top + bar_bottom) / 2
                va = 'center'

            # Main value
            ax.text(x[i], label_y + (revenue * 0.01 if va == 'bottom' else 0),
                    display_val, ha='center', va=va,
                    fontsize=13, fontweight='bold', color='#333')

            # Percentage below main value (for cost items)
            if pct and i > 0:
                if va == 'bottom':
                    ax.text(x[i], label_y + revenue * 0.04, pct,
                            ha='center', va='bottom', fontsize=11, color='#666')
                else:
                    ax.text(x[i], label_y - (revenue * 0.03), pct,
                            ha='center', va='center', fontsize=11, color='#666')

        # Connector lines between bars
        for i in range(len(labels) - 1):
            if bar_types[i] == 'total' and bar_types[i + 1] == 'delta':
                # Line from top of total to top of delta
                y_line = bottoms[i] + bar_heights[i]
                ax.plot([x[i] + bar_width / 2, x[i + 1] - bar_width / 2],
                        [y_line, y_line], color='#999', linewidth=1,
                        linestyle='--', zorder=2)
            elif bar_types[i] == 'delta' and bar_types[i + 1] == 'total':
                # Line from bottom of delta to top of next total
                y_line = bottoms[i]
                ax.plot([x[i] + bar_width / 2, x[i + 1] - bar_width / 2],
                        [y_line, y_line], color='#999', linewidth=1,
                        linestyle='--', zorder=2)

        # Style
        ax.set_xticks(x)
        ax.set_xticklabels(labels, fontsize=13, color='#333')
        ax.set_xlim(-0.5, len(labels) - 0.5)

        # Y-axis formatting
        ax.yaxis.set_major_formatter(mticker.FuncFormatter(
            lambda val, pos: _format_billions(val)))
        ax.yaxis.tick_right()
        ax.yaxis.set_label_position('right')
        ax.tick_params(axis='y', labelsize=12, colors='#666')

        # Grid
        ax.grid(True, axis='y', alpha=0.2, color='#ddd', zorder=1)
        ax.set_axisbelow(True)

        # Spines
        ax.spines['top'].set_visible(False)
        ax.spines['left'].set_visible(False)
        ax.spines['right'].set_color('#ccc')
        ax.spines['bottom'].set_color('#ccc')

        # Title
        period_label = 'FY' if period == 'annual' else 'Q'
        ax.set_title(f'{ticker} Income Statement Waterfall — {period_label} {fiscal_date}',
                     fontsize=16, fontweight='bold', color='#333', pad=15)

        # Margin annotations
        gross_margin = gross_profit / revenue * 100 if revenue else 0
        op_margin = operating_income / revenue * 100 if revenue else 0
        net_margin = net_income / revenue * 100 if revenue else 0

        margin_text = f"Gross: {gross_margin:.1f}%  |  Operating: {op_margin:.1f}%  |  Net: {net_margin:.1f}%"
        ax.text(0.5, -0.12, margin_text, transform=ax.transAxes,
                ha='center', fontsize=12, color='#666')

        # Watermark
        ax.text(0.99, 0.01, 'Financial Charts', transform=ax.transAxes, fontsize=11,
                color=(0, 0, 0, 0.2), va='bottom', ha='right')

        plt.tight_layout()
        plt.subplots_adjust(bottom=0.15)

        # Save to buffer
        buf = io.BytesIO()
        fig.savefig(buf, format='png', dpi=150, bbox_inches='tight',
                    facecolor='white', edgecolor='none')
        buf.seek(0)
        plt.close(fig)

        return Response(buf.getvalue(), mimetype='image/png')

    except Exception as e:
        logger.error(f"Waterfall chart error: {e}")
        traceback.print_exc()
        return jsonify({'error': str(e)}), HTTP_INTERNAL_ERROR
