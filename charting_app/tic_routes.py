"""
TIC (Treasury International Capital) data routes.
Routes: /api/tic/flows, /api/tic/holdings
"""
import logging
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Blueprint, jsonify, request
from constants import get_db_connection

logger = logging.getLogger(__name__)

tic_bp = Blueprint('tic', __name__)


@tic_bp.route('/api/tic/flows')
def get_tic_flows():
    """Get aggregate net foreign flows by asset class.

    Query params:
        rolling: Rolling window in months (default 12)
        country: Filter by country (default: Grand Total)

    Returns: {series_name: [{time, value}, ...], ...}
    """
    rolling = int(request.args.get('rolling', 12))
    country = request.args.get('country', 'Grand Total')

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT date,
                   treasury_net_flow,
                   agency_net_flow,
                   corporate_net_flow,
                   equity_net_flow,
                   total_net_flow
            FROM tic_flows
            WHERE country = ?
              AND total_net_flow IS NOT NULL
            ORDER BY date
        """, (country,))

        rows = cursor.fetchall()
        conn.close()

        if not rows:
            return jsonify({'error': f'No flow data for country: {country}'}), 404

        # Build series
        dates = []
        treasury = []
        agency = []
        corporate = []
        equity = []
        total = []

        for row in rows:
            # LW Charts accepts YYYY-MM-DD strings
            ts = row['date'][:10]

            dates.append(ts)
            treasury.append(row['treasury_net_flow'])
            agency.append(row['agency_net_flow'])
            corporate.append(row['corporate_net_flow'])
            equity.append(row['equity_net_flow'])
            total.append(row['total_net_flow'])

        # Apply rolling sum (convert millions to billions)
        def rolling_sum(values, window):
            result = []
            for i in range(len(values)):
                if i < window - 1:
                    result.append(None)
                else:
                    window_vals = [v for v in values[i - window + 1:i + 1] if v is not None]
                    if not window_vals:
                        result.append(None)
                    else:
                        result.append(round(sum(window_vals) / 1000, 2))
            return result

        treasury_r = rolling_sum(treasury, rolling)
        agency_r = rolling_sum(agency, rolling)
        corporate_r = rolling_sum(corporate, rolling)
        equity_r = rolling_sum(equity, rolling)
        total_r = rolling_sum(total, rolling)

        def to_series(dates, values):
            return [{'time': d, 'value': v} for d, v in zip(dates, values) if v is not None]

        result = {
            'Treasury': to_series(dates, treasury_r),
            'Agency': to_series(dates, agency_r),
            'Corporate': to_series(dates, corporate_r),
            'Equity': to_series(dates, equity_r),
            'Total': to_series(dates, total_r),
            'meta': {
                'rolling_months': rolling,
                'country': country,
                'unit': 'billions_usd',
                'data_points': len(rows),
            }
        }

        logger.info(f"/api/tic/flows: {len(rows)} rows, rolling={rolling}, country={country}")
        return jsonify(result)

    except Exception as e:
        logger.error(f"/api/tic/flows: Error: {e}")
        return jsonify({'error': str(e)}), 500


@tic_bp.route('/api/tic/holdings')
def get_tic_holdings():
    """Get Treasury holdings time series by country.

    Query params:
        countries: Comma-separated country names (default: top 5)
        limit: Max countries if not specified (default 5)

    Returns: {country_name: [{time, value}, ...], ...}
    """
    countries_param = request.args.get('countries', '')
    limit = int(request.args.get('limit', 5))

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        if countries_param:
            countries = [c.strip() for c in countries_param.split(',')]
        else:
            # Get top N holders by latest value
            cursor.execute("""
                SELECT country FROM tic_holdings
                WHERE date = (SELECT MAX(date) FROM tic_holdings)
                AND country != 'Grand Total'
                AND country NOT LIKE 'Of which%'
                AND country NOT LIKE 'Of Which%'
                AND country NOT LIKE '  %'
                AND country != 'All Other'
                AND holdings_billions IS NOT NULL
                ORDER BY holdings_billions DESC
                LIMIT ?
            """, (limit,))
            countries = [row['country'] for row in cursor.fetchall()]

        if not countries:
            conn.close()
            return jsonify({'error': 'No countries found'}), 404

        # Normalize country names for display
        name_map = {
            'China, Mainland': 'China',
            'Korea, South': 'South Korea',
            'United Kingdom': 'UK',
        }

        result = {}
        for country in countries:
            cursor.execute("""
                SELECT date, holdings_billions FROM tic_holdings
                WHERE country = ?
                ORDER BY date
            """, (country,))

            rows = cursor.fetchall()
            display_name = name_map.get(country, country)
            result[display_name] = [
                {'time': row['date'][:10], 'value': row['holdings_billions']}
                for row in rows if row['holdings_billions'] is not None
            ]

        conn.close()

        result['meta'] = {
            'countries': countries,
            'unit': 'billions_usd',
        }

        logger.info(f"/api/tic/holdings: {len(countries)} countries")
        return jsonify(result)

    except Exception as e:
        logger.error(f"/api/tic/holdings: Error: {e}")
        return jsonify({'error': str(e)}), 500
