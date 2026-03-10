"""
Income statement Sankey flow diagram route.
Route: /api/chart/sankey
"""
import io
import logging
import traceback
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import plotly.graph_objects as go
from flask import Blueprint, jsonify, request, Response
import pandas as pd
from constants import get_db_connection, HTTP_BAD_REQUEST, HTTP_NOT_FOUND, HTTP_INTERNAL_ERROR, resolve_ticker_alias

logger = logging.getLogger(__name__)

sankey_bp = Blueprint('sankey', __name__)


def _fmt(value):
    """Format a number as $X.XB or $X.XM."""
    if abs(value) >= 1e9:
        return f"${value / 1e9:.1f}B"
    elif abs(value) >= 1e6:
        return f"${value / 1e6:.0f}M"
    else:
        return f"${value:,.0f}"


@sankey_bp.route('/api/chart/sankey')
def get_sankey_chart():
    """Generate an income statement Sankey flow diagram (PNG).

    Query params:
        ticker: Stock ticker (required), e.g., AAPL
        period: annual or quarterly (optional, default annual)
        date: Specific fiscal_date_ending (optional, defaults to latest)
        width: Image width in pixels (optional, default 1200)
        height: Image height in pixels (optional, default 700)

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

        # Derived
        has_opex_detail = rd > 0 or sga > 0
        has_below_detail = interest > 0 or tax > 0
        total_opex = gross_profit - operating_income
        other_opex = max(0, total_opex - rd - sga) if has_opex_detail else total_opex
        total_below = operating_income - net_income
        other_below = max(0, total_below - interest - tax) if has_below_detail else total_below

        # Build Sankey nodes and links
        # Node indices
        nodes = []
        node_colors = []
        links_source = []
        links_target = []
        links_value = []
        links_color = []

        # Color palette
        c_revenue = '#2962FF'       # blue
        c_gross = '#26A69A'         # teal
        c_operating = '#66BB6A'     # green
        c_net = '#2962FF'           # blue
        c_cost = '#EF5350'          # red
        c_cost_flow = 'rgba(239, 83, 80, 0.35)'
        c_profit_flow = 'rgba(38, 166, 154, 0.35)'
        c_net_flow = 'rgba(41, 98, 255, 0.35)'

        # Nodes: Revenue(0) -> COGS(1), Gross Profit(2) -> [R&D(3), SG&A(4), Other OpEx(5)], Op Income(6) -> [Interest(7), Tax(8), Other(9)], Net Income(10)
        # We'll build dynamically based on data availability

        idx = 0
        NODE_REVENUE = idx; idx += 1
        nodes.append(f"Revenue\n{_fmt(revenue)}")
        node_colors.append(c_revenue)

        NODE_COGS = idx; idx += 1
        nodes.append(f"COGS\n{_fmt(cogs)}")
        node_colors.append(c_cost)

        NODE_GROSS = idx; idx += 1
        nodes.append(f"Gross Profit\n{_fmt(gross_profit)}")
        node_colors.append(c_gross)

        # Revenue -> COGS
        links_source.append(NODE_REVENUE)
        links_target.append(NODE_COGS)
        links_value.append(cogs)
        links_color.append(c_cost_flow)

        # Revenue -> Gross Profit
        links_source.append(NODE_REVENUE)
        links_target.append(NODE_GROSS)
        links_value.append(gross_profit)
        links_color.append(c_profit_flow)

        # OpEx breakdown
        if has_opex_detail:
            if rd > 0:
                NODE_RD = idx; idx += 1
                nodes.append(f"R&D\n{_fmt(rd)}")
                node_colors.append(c_cost)
                links_source.append(NODE_GROSS)
                links_target.append(NODE_RD)
                links_value.append(rd)
                links_color.append(c_cost_flow)

            if sga > 0:
                NODE_SGA = idx; idx += 1
                nodes.append(f"SG&A\n{_fmt(sga)}")
                node_colors.append(c_cost)
                links_source.append(NODE_GROSS)
                links_target.append(NODE_SGA)
                links_value.append(sga)
                links_color.append(c_cost_flow)

            if other_opex > revenue * 0.005:
                NODE_OTHER_OPEX = idx; idx += 1
                nodes.append(f"Other OpEx\n{_fmt(other_opex)}")
                node_colors.append(c_cost)
                links_source.append(NODE_GROSS)
                links_target.append(NODE_OTHER_OPEX)
                links_value.append(other_opex)
                links_color.append(c_cost_flow)
        else:
            if total_opex > 0:
                NODE_OPEX = idx; idx += 1
                nodes.append(f"OpEx\n{_fmt(total_opex)}")
                node_colors.append(c_cost)
                links_source.append(NODE_GROSS)
                links_target.append(NODE_OPEX)
                links_value.append(total_opex)
                links_color.append(c_cost_flow)

        NODE_OPINCOME = idx; idx += 1
        nodes.append(f"Operating Income\n{_fmt(operating_income)}")
        node_colors.append(c_operating)

        # Gross Profit -> Operating Income
        links_source.append(NODE_GROSS)
        links_target.append(NODE_OPINCOME)
        links_value.append(operating_income)
        links_color.append(c_profit_flow)

        # Below-the-line breakdown
        if has_below_detail:
            if interest > 0:
                NODE_INTEREST = idx; idx += 1
                nodes.append(f"Interest\n{_fmt(interest)}")
                node_colors.append(c_cost)
                links_source.append(NODE_OPINCOME)
                links_target.append(NODE_INTEREST)
                links_value.append(interest)
                links_color.append(c_cost_flow)

            if tax > 0:
                NODE_TAX = idx; idx += 1
                nodes.append(f"Tax\n{_fmt(tax)}")
                node_colors.append(c_cost)
                links_source.append(NODE_OPINCOME)
                links_target.append(NODE_TAX)
                links_value.append(tax)
                links_color.append(c_cost_flow)

            if other_below > revenue * 0.005:
                NODE_OTHER_BELOW = idx; idx += 1
                nodes.append(f"Other\n{_fmt(other_below)}")
                node_colors.append(c_cost)
                links_source.append(NODE_OPINCOME)
                links_target.append(NODE_OTHER_BELOW)
                links_value.append(other_below)
                links_color.append(c_cost_flow)
        else:
            if total_below > 0:
                NODE_BELOW = idx; idx += 1
                nodes.append(f"Tax & Other\n{_fmt(total_below)}")
                node_colors.append(c_cost)
                links_source.append(NODE_OPINCOME)
                links_target.append(NODE_BELOW)
                links_value.append(total_below)
                links_color.append(c_cost_flow)

        NODE_NET = idx; idx += 1
        nodes.append(f"Net Income\n{_fmt(net_income)}")
        node_colors.append(c_net)

        # Operating Income -> Net Income
        links_source.append(NODE_OPINCOME)
        links_target.append(NODE_NET)
        links_value.append(net_income)
        links_color.append(c_net_flow)

        # Build Sankey figure
        fig = go.Figure(data=[go.Sankey(
            arrangement='snap',
            node=dict(
                pad=35,
                thickness=35,
                line=dict(color='white', width=2),
                label=nodes,
                color=node_colors,
            ),
            link=dict(
                source=links_source,
                target=links_target,
                value=links_value,
                color=links_color,
            )
        )])

        # Margin annotations
        gross_margin = gross_profit / revenue * 100 if revenue else 0
        op_margin = operating_income / revenue * 100 if revenue else 0
        net_margin = net_income / revenue * 100 if revenue else 0

        period_label = 'FY' if period == 'annual' else 'Q'
        fig.update_layout(
            title=dict(
                text=f"{ticker} Income Statement — {period_label} {fiscal_date}<br>"
                     f"<span style='font-size:14px;color:#666'>"
                     f"Gross: {gross_margin:.1f}% | Operating: {op_margin:.1f}% | Net: {net_margin:.1f}%</span>",
                font=dict(size=20, color='#333'),
                x=0.5,
                xanchor='center',
            ),
            font=dict(size=13, color='#333'),
            paper_bgcolor='white',
            plot_bgcolor='white',
            width=width,
            height=height,
            margin=dict(l=20, r=20, t=80, b=30),
            annotations=[
                dict(
                    text="Financial Charts",
                    xref="paper", yref="paper",
                    x=0.99, y=0.01,
                    showarrow=False,
                    font=dict(size=11, color='rgba(0,0,0,0.2)'),
                    xanchor='right',
                )
            ]
        )

        # Export to PNG
        img_bytes = fig.to_image(format='png', scale=2, engine='kaleido')

        return Response(img_bytes, mimetype='image/png')

    except Exception as e:
        logger.error(f"Sankey chart error: {e}")
        traceback.print_exc()
        return jsonify({'error': str(e)}), HTTP_INTERNAL_ERROR
