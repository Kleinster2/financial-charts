"""
Portfolio API routes for Flask application
"""
import sys
import os
from flask import Blueprint, jsonify, request

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from portfolio_manager import PortfolioManager
from portfolio_valuation import PortfolioValuation

# Create blueprint
portfolio_bp = Blueprint('portfolio', __name__, url_prefix='/api/portfolio')

# Initialize managers
pm = PortfolioManager()
pv = PortfolioValuation()


@portfolio_bp.route('/list', methods=['GET'])
def list_portfolios():
    """Get list of all portfolios."""
    try:
        portfolios = pm.list_portfolios()
        return jsonify(portfolios)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@portfolio_bp.route('/create', methods=['POST'])
def create_portfolio():
    """Create a new portfolio."""
    try:
        data = request.json
        portfolio_id = pm.create_portfolio(
            name=data['name'],
            description=data.get('description', ''),
            initial_cash=data.get('initial_cash', 100000.0),
            currency=data.get('currency', 'USD')
        )
        return jsonify({'portfolio_id': portfolio_id, 'success': True})
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@portfolio_bp.route('/<int:portfolio_id>/holdings', methods=['GET'])
def get_holdings(portfolio_id):
    """Get current holdings for a portfolio."""
    try:
        holdings = pm.get_holdings(portfolio_id)
        cash = pm.get_cash_balance(portfolio_id)
        return jsonify({'holdings': holdings, 'cash': cash})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@portfolio_bp.route('/<int:portfolio_id>/transactions', methods=['GET'])
def get_transactions(portfolio_id):
    """Get transaction history for a portfolio."""
    try:
        start_date = request.args.get('start_date')
        end_date = request.args.get('end_date')

        transactions = pm.get_transactions(
            portfolio_id=portfolio_id,
            start_date=start_date,
            end_date=end_date
        )
        return jsonify(transactions)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@portfolio_bp.route('/<int:portfolio_id>/transaction', methods=['POST'])
def add_transaction(portfolio_id):
    """Add a transaction to a portfolio."""
    try:
        data = request.json

        transaction_id = pm.add_transaction(
            portfolio_id=portfolio_id,
            transaction_date=data['transaction_date'],
            transaction_type=data['transaction_type'],
            ticker=data.get('ticker'),
            quantity=data.get('quantity'),
            price=data.get('price'),
            amount=data.get('amount'),
            fees=data.get('fees', 0),
            notes=data.get('notes', '')
        )

        # Recalculate valuations from transaction date forward
        pv.backfill_valuations(
            portfolio_id=portfolio_id,
            start_date=data['transaction_date']
        )

        return jsonify({'transaction_id': transaction_id, 'success': True})
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@portfolio_bp.route('/<int:portfolio_id>/valuations', methods=['GET'])
def get_valuations(portfolio_id):
    """Get valuation history for a portfolio."""
    try:
        start_date = request.args.get('start_date')
        end_date = request.args.get('end_date')

        valuations = pv.get_valuation_history(
            portfolio_id=portfolio_id,
            start_date=start_date,
            end_date=end_date
        )

        # Format for charting (same format as stock prices)
        # Return array of {time, value} objects
        chart_data = []

        for v in valuations:
            # Convert date string to timestamp
            from datetime import datetime
            dt = datetime.strptime(v['date'].split()[0], '%Y-%m-%d')
            timestamp = int(dt.timestamp())

            chart_data.append({
                'time': timestamp,
                'value': v['total_value']
            })

        return jsonify(chart_data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@portfolio_bp.route('/<int:portfolio_id>/recalculate', methods=['POST'])
def recalculate_valuations(portfolio_id):
    """Recalculate all valuations for a portfolio."""
    try:
        data = request.json
        start_date = data.get('start_date')
        end_date = data.get('end_date')

        pv.backfill_valuations(
            portfolio_id=portfolio_id,
            start_date=start_date,
            end_date=end_date
        )

        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@portfolio_bp.route('/<int:portfolio_id>/performance', methods=['GET'])
def get_performance(portfolio_id):
    """Get portfolio performance metrics."""
    try:
        valuations = pv.get_valuation_history(portfolio_id)

        if not valuations:
            return jsonify({'error': 'No valuation data'}), 404

        latest = valuations[-1]
        first = valuations[0]

        # Calculate performance metrics
        metrics = {
            'current_value': latest['total_value'],
            'cash_balance': latest['cash_balance'],
            'securities_value': latest['securities_value'],
            'total_return': latest['cumulative_return'] * 100,
            'total_return_dollars': latest['total_value'] - first['total_value'],
            'num_days': len(valuations),
            'start_date': first['date'],
            'end_date': latest['date']
        }

        # Calculate volatility (annualized)
        daily_returns = [v['daily_return'] for v in valuations if v['daily_return'] is not None]
        if daily_returns:
            import numpy as np
            volatility = np.std(daily_returns) * np.sqrt(252)  # Annualized
            metrics['volatility'] = volatility * 100
        else:
            metrics['volatility'] = 0

        return jsonify(metrics)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
