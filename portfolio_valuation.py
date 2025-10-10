"""
Portfolio Valuation - Daily mark-to-market calculations
"""
import sqlite3
from datetime import datetime, date, timedelta
from typing import List, Dict, Optional
from constants import DB_PATH


class PortfolioValuation:
    """Calculate and store daily portfolio valuations."""

    def __init__(self, db_path: str = DB_PATH):
        self.db_path = db_path

    def calculate_daily_valuation(self, portfolio_id: int, valuation_date: str):
        """
        Calculate portfolio valuation for a specific date.

        This performs mark-to-market on all holdings using closing prices.
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        try:
            # Get cash balance as of this date
            cursor.execute("""
                SELECT SUM(amount) FROM portfolio_transactions
                WHERE portfolio_id = ? AND transaction_date <= ?
            """, (portfolio_id, valuation_date))

            cash_balance = cursor.fetchone()[0] or 0.0

            # Get holdings as of this date (reconstructed from transactions)
            holdings = self._get_holdings_as_of_date(cursor, portfolio_id, valuation_date)

            if not holdings:
                # No holdings, only cash
                total_value = cash_balance
                cursor.execute("""
                    INSERT OR REPLACE INTO portfolio_valuations_daily
                    (portfolio_id, date, cash_balance, securities_value, total_value)
                    VALUES (?, ?, ?, 0, ?)
                """, (portfolio_id, valuation_date, cash_balance, total_value))

                conn.commit()
                return

            # Get prices for all tickers
            tickers = list(holdings.keys())
            prices = self._get_prices(cursor, tickers, valuation_date)

            # Skip this date if we don't have prices for all tickers
            missing_prices = [t for t in tickers if t not in prices]
            if missing_prices:
                print(f"Warning: No price for {', '.join(missing_prices)} on {valuation_date}, skipping")
                return

            # Calculate securities value and save holdings snapshot
            securities_value = 0.0
            holdings_data = []

            for ticker, (quantity, avg_cost) in holdings.items():
                price = prices[ticker]
                market_value = quantity * price
                cost_basis = quantity * avg_cost
                unrealized_pnl = market_value - cost_basis
                securities_value += market_value

                holdings_data.append((
                    portfolio_id, valuation_date, ticker, quantity, price,
                    market_value, cost_basis, unrealized_pnl
                ))

            total_value = cash_balance + securities_value

            # Calculate returns
            cursor.execute("""
                SELECT total_value FROM portfolio_valuations_daily
                WHERE portfolio_id = ? AND date < ?
                ORDER BY date DESC LIMIT 1
            """, (portfolio_id, valuation_date))

            prev_result = cursor.fetchone()
            daily_return = None
            if prev_result and prev_result[0]:
                prev_value = prev_result[0]
                daily_return = (total_value - prev_value) / prev_value if prev_value else 0

            # Get initial cash to calculate cumulative return
            cursor.execute("""
                SELECT initial_cash FROM portfolios WHERE portfolio_id = ?
            """, (portfolio_id,))
            initial_cash = cursor.fetchone()[0]
            cumulative_return = (total_value - initial_cash) / initial_cash if initial_cash else 0

            # Save valuation
            cursor.execute("""
                INSERT OR REPLACE INTO portfolio_valuations_daily
                (portfolio_id, date, cash_balance, securities_value, total_value,
                 daily_return, cumulative_return)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (portfolio_id, valuation_date, cash_balance, securities_value,
                  total_value, daily_return, cumulative_return))

            # Save holdings snapshot
            cursor.execute("""
                DELETE FROM portfolio_holdings_daily
                WHERE portfolio_id = ? AND date = ?
            """, (portfolio_id, valuation_date))

            # Calculate weights
            total_securities = securities_value if securities_value > 0 else 1
            for holding in holdings_data:
                weight = holding[5] / total_value  # market_value / total_value
                cursor.execute("""
                    INSERT INTO portfolio_holdings_daily
                    (portfolio_id, date, ticker, quantity, price, market_value,
                     cost_basis, unrealized_pnl, weight)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, holding + (weight,))

            conn.commit()

        finally:
            conn.close()

    def _get_holdings_as_of_date(self, cursor: sqlite3.Cursor,
                                 portfolio_id: int, as_of_date: str) -> Dict[str, tuple]:
        """
        Reconstruct holdings as of a specific date from transaction history.

        Returns:
            Dict[ticker, (quantity, avg_cost)]
        """
        cursor.execute("""
            SELECT ticker, transaction_type, quantity, price
            FROM portfolio_transactions
            WHERE portfolio_id = ?
              AND transaction_date <= ?
              AND transaction_type IN ('BUY', 'SELL')
            ORDER BY transaction_date, transaction_id
        """, (portfolio_id, as_of_date))

        holdings = {}  # ticker -> (quantity, avg_cost)

        for ticker, trans_type, quantity, price in cursor.fetchall():
            if ticker not in holdings:
                holdings[ticker] = [0.0, 0.0]  # [quantity, avg_cost]

            current_qty, avg_cost = holdings[ticker]

            if trans_type == 'BUY':
                new_qty = current_qty + quantity
                new_avg_cost = ((current_qty * avg_cost) + (quantity * price)) / new_qty if new_qty > 0 else price
                holdings[ticker] = [new_qty, new_avg_cost]
            elif trans_type == 'SELL':
                new_qty = current_qty - quantity
                if new_qty < -0.0001:
                    raise ValueError(f"Invalid holdings for {ticker} on {as_of_date}")
                holdings[ticker] = [new_qty, avg_cost]

        # Remove zero positions
        return {ticker: tuple(data) for ticker, data in holdings.items() if data[0] > 0.0001}

    def _get_prices(self, cursor: sqlite3.Cursor, tickers: List[str],
                   price_date: str) -> Dict[str, float]:
        """Get closing prices for tickers on a specific date."""
        if not tickers:
            return {}

        # Try exact date first
        placeholders = ','.join(['?' for _ in tickers])
        query = f"""
            SELECT * FROM stock_prices_daily WHERE date = ?
        """

        cursor.execute(query, (price_date,))
        row = cursor.fetchone()

        if row:
            # Get column names
            cursor.execute("SELECT * FROM stock_prices_daily LIMIT 0")
            columns = [desc[0] for desc in cursor.description]

            prices = {}
            for ticker in tickers:
                if ticker in columns:
                    idx = columns.index(ticker)
                    price = row[idx]
                    if price is not None:
                        prices[ticker] = price

            return prices

        # If no data for exact date, try previous trading day
        cursor.execute("""
            SELECT date FROM stock_prices_daily WHERE date < ? ORDER BY date DESC LIMIT 1
        """, (price_date,))

        prev_date = cursor.fetchone()
        if prev_date:
            return self._get_prices(cursor, tickers, prev_date[0])

        return {}

    def backfill_valuations(self, portfolio_id: int,
                           start_date: Optional[str] = None,
                           end_date: Optional[str] = None):
        """
        Calculate valuations for all dates in range.

        Args:
            portfolio_id: Portfolio ID
            start_date: Start date (default: first transaction date)
            end_date: End date (default: today)
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        # Get date range
        if not start_date:
            cursor.execute("""
                SELECT MIN(transaction_date) FROM portfolio_transactions
                WHERE portfolio_id = ?
            """, (portfolio_id,))
            start_date = cursor.fetchone()[0]

        if not end_date:
            end_date = date.today().isoformat()

        conn.close()

        if not start_date:
            print(f"No transactions found for portfolio {portfolio_id}")
            return

        # Get all trading dates in range
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT DISTINCT date FROM stock_prices_daily
            WHERE date >= ? AND date <= ?
            ORDER BY date
        """, (start_date, end_date))

        trading_dates = [row[0] for row in cursor.fetchall()]
        conn.close()

        print(f"Calculating valuations for {len(trading_dates)} dates...")

        for i, trade_date in enumerate(trading_dates):
            if (i + 1) % 50 == 0:
                print(f"Progress: {i+1}/{len(trading_dates)}")

            self.calculate_daily_valuation(portfolio_id, trade_date)

        print(f"Completed valuation backfill for portfolio {portfolio_id}")

    def get_valuation_history(self, portfolio_id: int,
                             start_date: Optional[str] = None,
                             end_date: Optional[str] = None) -> List[Dict]:
        """Get historical valuations for a portfolio."""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        query = """
            SELECT date, cash_balance, securities_value, total_value,
                   daily_return, cumulative_return
            FROM portfolio_valuations_daily
            WHERE portfolio_id = ?
        """
        params = [portfolio_id]

        if start_date:
            query += " AND date >= ?"
            params.append(start_date)

        if end_date:
            query += " AND date <= ?"
            params.append(end_date)

        query += " ORDER BY date"

        cursor.execute(query, params)
        valuations = [dict(row) for row in cursor.fetchall()]
        conn.close()

        return valuations
