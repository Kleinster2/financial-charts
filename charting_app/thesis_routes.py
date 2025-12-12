"""
Investment Thesis Tracker API Routes
Provides endpoints for managing investment theses, tracking performance, and journaling.
"""

import sys
import os

# Add parent directory to path for constants import
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from flask import Blueprint, jsonify, request
import sqlite3
from datetime import datetime
from constants import DB_PATH

thesis_bp = Blueprint('thesis', __name__)


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def get_current_price(ticker):
    """Get the latest price for a ticker from stock_prices_daily"""
    try:
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute(f'SELECT "{ticker}" FROM stock_prices_daily WHERE "{ticker}" IS NOT NULL ORDER BY Date DESC LIMIT 1')
        row = cursor.fetchone()
        conn.close()
        return row[0] if row else None
    except:
        return None

def calculate_pnl(entry_price, current_price, direction='long'):
    """Calculate P&L percentage"""
    if not entry_price or not current_price:
        return None
    if direction == 'long':
        return ((current_price - entry_price) / entry_price) * 100
    else:  # short
        return ((entry_price - current_price) / entry_price) * 100


# ============== THESIS CRUD ==============

@thesis_bp.route('/api/theses', methods=['GET'])
def list_theses():
    """List all theses with optional filtering"""
    status = request.args.get('status')  # idea, active, closed, won, lost
    category = request.args.get('category')
    ticker = request.args.get('ticker')

    conn = get_db()
    cursor = conn.cursor()

    query = 'SELECT * FROM investment_theses WHERE 1=1'
    params = []

    if status:
        query += ' AND status = ?'
        params.append(status)
    if category:
        query += ' AND category = ?'
        params.append(category)
    if ticker:
        query += ' AND tickers LIKE ?'
        params.append(f'%{ticker}%')

    query += ' ORDER BY updated_at DESC'

    cursor.execute(query, params)
    rows = cursor.fetchall()

    theses = []
    for row in rows:
        thesis = dict(row)

        # Update current price and P&L for active theses
        if thesis['status'] == 'active' and thesis['tickers'] and thesis['entry_price']:
            primary_ticker = thesis['tickers'].split(',')[0].strip()
            current_price = get_current_price(primary_ticker)
            if current_price:
                thesis['current_price'] = current_price
                thesis['pnl_percent'] = calculate_pnl(
                    thesis['entry_price'],
                    current_price,
                    thesis.get('direction', 'long')
                )

        theses.append(thesis)

    conn.close()
    return jsonify(theses)


@thesis_bp.route('/api/theses', methods=['POST'])
def create_thesis():
    """Create a new thesis"""
    data = request.json

    conn = get_db()
    cursor = conn.cursor()

    now = datetime.now().isoformat()
    cursor.execute('''
        INSERT INTO investment_theses
        (title, thesis, category, tickers, page_id, status, conviction, direction,
         entry_date, entry_price, target_price, stop_loss, position_size, notes, tags,
         created_at, updated_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        data.get('title'),
        data.get('thesis'),
        data.get('category'),
        data.get('tickers'),
        data.get('page_id'),
        data.get('status', 'idea'),
        data.get('conviction', 'medium'),
        data.get('direction', 'long'),
        data.get('entry_date'),
        data.get('entry_price'),
        data.get('target_price'),
        data.get('stop_loss'),
        data.get('position_size'),
        data.get('notes'),
        data.get('tags'),
        now,
        now
    ))

    thesis_id = cursor.lastrowid
    conn.commit()
    conn.close()

    return jsonify({'id': thesis_id, 'message': 'Thesis created'}), 201


@thesis_bp.route('/api/theses/<int:thesis_id>', methods=['GET'])
def get_thesis(thesis_id):
    """Get a single thesis with its updates"""
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM investment_theses WHERE id = ?', (thesis_id,))
    row = cursor.fetchone()

    if not row:
        conn.close()
        return jsonify({'error': 'Thesis not found'}), 404

    thesis = dict(row)

    # Get updates/journal entries
    cursor.execute('SELECT * FROM thesis_updates WHERE thesis_id = ? ORDER BY created_at DESC', (thesis_id,))
    updates = [dict(r) for r in cursor.fetchall()]
    thesis['updates'] = updates

    # Update current price
    if thesis['tickers'] and thesis['entry_price']:
        primary_ticker = thesis['tickers'].split(',')[0].strip()
        current_price = get_current_price(primary_ticker)
        if current_price:
            thesis['current_price'] = current_price
            thesis['pnl_percent'] = calculate_pnl(
                thesis['entry_price'],
                current_price,
                thesis.get('direction', 'long')
            )

    conn.close()
    return jsonify(thesis)


@thesis_bp.route('/api/theses/<int:thesis_id>', methods=['PUT'])
def update_thesis(thesis_id):
    """Update a thesis"""
    data = request.json

    conn = get_db()
    cursor = conn.cursor()

    # Build dynamic update query
    fields = []
    values = []

    for field in ['title', 'thesis', 'category', 'tickers', 'page_id', 'status',
                  'conviction', 'direction', 'entry_date', 'entry_price',
                  'target_price', 'stop_loss', 'position_size', 'exit_date',
                  'exit_price', 'pnl_percent', 'outcome', 'notes', 'tags']:
        if field in data:
            fields.append(f'{field} = ?')
            values.append(data[field])

    if not fields:
        return jsonify({'error': 'No fields to update'}), 400

    fields.append('updated_at = ?')
    values.append(datetime.now().isoformat())
    values.append(thesis_id)

    query = f'UPDATE investment_theses SET {", ".join(fields)} WHERE id = ?'
    cursor.execute(query, values)

    conn.commit()
    conn.close()

    return jsonify({'message': 'Thesis updated'})


@thesis_bp.route('/api/theses/<int:thesis_id>', methods=['DELETE'])
def delete_thesis(thesis_id):
    """Delete a thesis and its updates"""
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute('DELETE FROM thesis_updates WHERE thesis_id = ?', (thesis_id,))
    cursor.execute('DELETE FROM investment_theses WHERE id = ?', (thesis_id,))

    conn.commit()
    conn.close()

    return jsonify({'message': 'Thesis deleted'})


# ============== THESIS UPDATES/JOURNAL ==============

@thesis_bp.route('/api/theses/<int:thesis_id>/updates', methods=['POST'])
def add_update(thesis_id):
    """Add a journal entry/update to a thesis"""
    data = request.json

    # Get current price for the primary ticker
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute('SELECT tickers FROM investment_theses WHERE id = ?', (thesis_id,))
    row = cursor.fetchone()

    price_at_update = None
    if row and row['tickers']:
        primary_ticker = row['tickers'].split(',')[0].strip()
        price_at_update = get_current_price(primary_ticker)

    cursor.execute('''
        INSERT INTO thesis_updates (thesis_id, update_type, content, price_at_update)
        VALUES (?, ?, ?, ?)
    ''', (
        thesis_id,
        data.get('update_type', 'note'),  # note, entry, exit, adjustment, alert
        data.get('content'),
        price_at_update
    ))

    # Update the thesis updated_at
    cursor.execute('UPDATE investment_theses SET updated_at = ? WHERE id = ?',
                   (datetime.now().isoformat(), thesis_id))

    conn.commit()
    conn.close()

    return jsonify({'message': 'Update added'}), 201


# ============== THESIS ACTIONS ==============

@thesis_bp.route('/api/theses/<int:thesis_id>/activate', methods=['POST'])
def activate_thesis(thesis_id):
    """Activate a thesis (move from idea to active)"""
    data = request.json

    conn = get_db()
    cursor = conn.cursor()

    entry_price = data.get('entry_price')
    entry_date = data.get('entry_date', datetime.now().strftime('%Y-%m-%d'))

    # If no entry price provided, try to get current price
    if not entry_price:
        cursor.execute('SELECT tickers FROM investment_theses WHERE id = ?', (thesis_id,))
        row = cursor.fetchone()
        if row and row['tickers']:
            primary_ticker = row['tickers'].split(',')[0].strip()
            entry_price = get_current_price(primary_ticker)

    cursor.execute('''
        UPDATE investment_theses
        SET status = 'active', entry_date = ?, entry_price = ?, updated_at = ?
        WHERE id = ?
    ''', (entry_date, entry_price, datetime.now().isoformat(), thesis_id))

    # Add journal entry
    cursor.execute('''
        INSERT INTO thesis_updates (thesis_id, update_type, content, price_at_update)
        VALUES (?, 'entry', 'Position entered', ?)
    ''', (thesis_id, entry_price))

    conn.commit()
    conn.close()

    return jsonify({'message': 'Thesis activated', 'entry_price': entry_price})


@thesis_bp.route('/api/theses/<int:thesis_id>/close', methods=['POST'])
def close_thesis(thesis_id):
    """Close a thesis (record exit)"""
    data = request.json

    conn = get_db()
    cursor = conn.cursor()

    # Get thesis details
    cursor.execute('SELECT * FROM investment_theses WHERE id = ?', (thesis_id,))
    row = cursor.fetchone()
    if not row:
        conn.close()
        return jsonify({'error': 'Thesis not found'}), 404
    thesis = dict(row)

    exit_price = data.get('exit_price')
    exit_date = data.get('exit_date', datetime.now().strftime('%Y-%m-%d'))
    outcome = data.get('outcome')  # won, lost, breakeven

    # If no exit price provided, get current price
    if not exit_price and thesis['tickers']:
        primary_ticker = thesis['tickers'].split(',')[0].strip()
        exit_price = get_current_price(primary_ticker)

    # Calculate P&L
    pnl = calculate_pnl(thesis['entry_price'], exit_price, thesis.get('direction', 'long'))

    # Determine outcome if not provided
    if not outcome:
        if pnl and pnl > 1:
            outcome = 'won'
        elif pnl and pnl < -1:
            outcome = 'lost'
        else:
            outcome = 'breakeven'

    cursor.execute('''
        UPDATE investment_theses
        SET status = 'closed', exit_date = ?, exit_price = ?, pnl_percent = ?, outcome = ?, updated_at = ?
        WHERE id = ?
    ''', (exit_date, exit_price, pnl, outcome, datetime.now().isoformat(), thesis_id))

    # Add journal entry
    cursor.execute('''
        INSERT INTO thesis_updates (thesis_id, update_type, content, price_at_update)
        VALUES (?, 'exit', ?, ?)
    ''', (thesis_id, f'Position closed - {outcome} ({pnl:.1f}%)' if pnl else 'Position closed', exit_price))

    conn.commit()
    conn.close()

    return jsonify({'message': 'Thesis closed', 'pnl_percent': pnl, 'outcome': outcome})


# ============== DASHBOARD/SUMMARY ==============

@thesis_bp.route('/api/theses/summary', methods=['GET'])
def thesis_summary():
    """Get summary statistics for all theses"""
    conn = get_db()
    cursor = conn.cursor()

    # Count by status
    cursor.execute('''
        SELECT status, COUNT(*) as count
        FROM investment_theses
        GROUP BY status
    ''')
    status_counts = {row['status']: row['count'] for row in cursor.fetchall()}

    # Win/loss stats for closed theses
    cursor.execute('''
        SELECT outcome, COUNT(*) as count, AVG(pnl_percent) as avg_pnl
        FROM investment_theses
        WHERE status = 'closed' AND outcome IS NOT NULL
        GROUP BY outcome
    ''')
    outcome_stats = {row['outcome']: {'count': row['count'], 'avg_pnl': row['avg_pnl']}
                     for row in cursor.fetchall()}

    # Active theses with current P&L
    cursor.execute('SELECT * FROM investment_theses WHERE status = "active"')
    active_theses = []
    total_active_pnl = 0

    for row in cursor.fetchall():
        thesis = dict(row)
        if thesis['tickers'] and thesis['entry_price']:
            primary_ticker = thesis['tickers'].split(',')[0].strip()
            current_price = get_current_price(primary_ticker)
            if current_price:
                pnl = calculate_pnl(thesis['entry_price'], current_price, thesis.get('direction', 'long'))
                thesis['current_price'] = current_price
                thesis['pnl_percent'] = pnl
                if pnl:
                    total_active_pnl += pnl
        active_theses.append(thesis)

    # Theses needing attention (near stop loss or target)
    alerts = []
    for thesis in active_theses:
        if thesis.get('current_price') and thesis.get('stop_loss'):
            if thesis['direction'] == 'long' and thesis['current_price'] <= thesis['stop_loss'] * 1.05:
                alerts.append({'thesis_id': thesis['id'], 'title': thesis['title'], 'alert': 'Near stop loss'})
            elif thesis['direction'] == 'short' and thesis['current_price'] >= thesis['stop_loss'] * 0.95:
                alerts.append({'thesis_id': thesis['id'], 'title': thesis['title'], 'alert': 'Near stop loss'})

        if thesis.get('current_price') and thesis.get('target_price'):
            if thesis['direction'] == 'long' and thesis['current_price'] >= thesis['target_price'] * 0.95:
                alerts.append({'thesis_id': thesis['id'], 'title': thesis['title'], 'alert': 'Near target'})
            elif thesis['direction'] == 'short' and thesis['current_price'] <= thesis['target_price'] * 1.05:
                alerts.append({'thesis_id': thesis['id'], 'title': thesis['title'], 'alert': 'Near target'})

    conn.close()

    return jsonify({
        'status_counts': status_counts,
        'outcome_stats': outcome_stats,
        'active_count': len(active_theses),
        'total_active_pnl': total_active_pnl,
        'alerts': alerts
    })


# ============== CATEGORIES ==============

@thesis_bp.route('/api/theses/categories', methods=['GET'])
def list_categories():
    """List all unique categories"""
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute('SELECT DISTINCT category FROM investment_theses WHERE category IS NOT NULL ORDER BY category')
    categories = [row['category'] for row in cursor.fetchall()]

    conn.close()
    return jsonify(categories)


# ============== PERFORMANCE TRACKING ==============

def parse_tickers_with_weights(tickers_str):
    """Parse tickers string with optional weights.

    Formats supported:
    - "ICE,CME,DKNG" -> equal weights
    - "ICE:40,CME:30,DKNG:30" -> custom weights (should sum to 100)
    - "ICE:40,CME,DKNG" -> mixed (unweighted get equal share of remainder)

    Returns list of (ticker, weight) tuples where weights sum to 1.0
    """
    if not tickers_str:
        return []

    parts = [p.strip() for p in tickers_str.split(',')]
    parsed = []
    total_explicit_weight = 0
    unweighted_count = 0

    for part in parts:
        if ':' in part:
            ticker, weight = part.split(':', 1)
            weight = float(weight) / 100  # Convert percentage to decimal
            parsed.append((ticker.strip(), weight))
            total_explicit_weight += weight
        else:
            parsed.append((part.strip(), None))
            unweighted_count += 1

    # Distribute remaining weight to unweighted tickers
    if unweighted_count > 0:
        remaining = max(0, 1.0 - total_explicit_weight)
        equal_share = remaining / unweighted_count
        parsed = [(t, w if w is not None else equal_share) for t, w in parsed]

    # Normalize if weights don't sum to 1
    total = sum(w for _, w in parsed)
    if total > 0 and abs(total - 1.0) > 0.01:
        parsed = [(t, w / total) for t, w in parsed]

    return parsed


def get_price_history(ticker, start_date, end_date=None):
    """Get price history for a ticker between dates.

    Returns list of (date, price) tuples.
    """
    conn = get_db()
    cursor = conn.cursor()

    query = f'SELECT Date, "{ticker}" FROM stock_prices_daily WHERE "{ticker}" IS NOT NULL AND Date >= ?'
    params = [start_date]

    if end_date:
        query += ' AND Date <= ?'
        params.append(end_date)

    query += ' ORDER BY Date'

    try:
        cursor.execute(query, params)
        rows = cursor.fetchall()
        conn.close()
        return [(row['Date'], row[ticker]) for row in rows]
    except:
        conn.close()
        return []


@thesis_bp.route('/api/theses/<int:thesis_id>/performance', methods=['GET'])
def get_thesis_performance(thesis_id):
    """Get historical P&L performance for a thesis.

    Query params:
    - start: Start date (default: entry_date)
    - end: End date (default: today or exit_date)

    Returns time series of weighted P&L across all tickers.
    """
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM investment_theses WHERE id = ?', (thesis_id,))
    row = cursor.fetchone()
    conn.close()

    if not row:
        return jsonify({'error': 'Thesis not found'}), 404

    thesis = dict(row)

    if not thesis['tickers']:
        return jsonify({'error': 'No tickers defined for thesis'}), 400

    # Parse tickers with weights
    ticker_weights = parse_tickers_with_weights(thesis['tickers'])

    # Determine date range
    start_date = request.args.get('start') or thesis.get('entry_date')
    end_date = request.args.get('end') or thesis.get('exit_date')

    if not start_date:
        return jsonify({'error': 'No start date (entry_date not set)'}), 400

    # Get price history for each ticker
    ticker_histories = {}
    entry_prices = {}

    for ticker, weight in ticker_weights:
        history = get_price_history(ticker, start_date, end_date)
        if history:
            ticker_histories[ticker] = {date: price for date, price in history}
            # Use first available price as entry price for this ticker
            entry_prices[ticker] = history[0][1]

    if not ticker_histories:
        return jsonify({'error': 'No price data found for tickers'}), 404

    # Build unified date series
    all_dates = set()
    for hist in ticker_histories.values():
        all_dates.update(hist.keys())
    all_dates = sorted(all_dates)

    # Calculate weighted P&L for each date
    direction = thesis.get('direction', 'long')
    performance = []
    last_prices = dict(entry_prices)  # Track last known price for each ticker

    for date in all_dates:
        weighted_pnl = 0
        total_weight = 0
        ticker_details = []

        for ticker, weight in ticker_weights:
            if ticker in ticker_histories:
                # Use current price or last known price
                if date in ticker_histories[ticker]:
                    price = ticker_histories[ticker][date]
                    last_prices[ticker] = price
                else:
                    price = last_prices.get(ticker)

                if price and ticker in entry_prices:
                    entry = entry_prices[ticker]
                    if direction == 'long':
                        pnl = ((price - entry) / entry) * 100
                    else:
                        pnl = ((entry - price) / entry) * 100

                    weighted_pnl += pnl * weight
                    total_weight += weight
                    ticker_details.append({
                        'ticker': ticker,
                        'weight': round(weight * 100, 1),
                        'price': round(price, 2),
                        'pnl_percent': round(pnl, 2)
                    })

        if total_weight > 0:
            performance.append({
                'date': date,
                'weighted_pnl_percent': round(weighted_pnl, 2),
                'tickers': ticker_details
            })

    return jsonify({
        'thesis_id': thesis_id,
        'title': thesis['title'],
        'direction': direction,
        'start_date': start_date,
        'end_date': end_date or 'present',
        'ticker_weights': [{'ticker': t, 'weight': round(w * 100, 1)} for t, w in ticker_weights],
        'performance': performance
    })
