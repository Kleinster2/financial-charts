"""
Portfolio Manager - Handle portfolio creation, transactions, and valuations
"""
import sqlite3
from datetime import datetime, date
from typing import List, Dict, Optional, Tuple
from constants import DB_PATH


class PortfolioManager:
    """Manage portfolios with transaction tracking and daily valuations."""

    def __init__(self, db_path: str = DB_PATH):
        self.db_path = db_path
        self._ensure_schema()

    def _ensure_schema(self):
        """Create portfolio tables if they don't exist."""
        import os
        schema_path = os.path.join(os.path.dirname(__file__), 'portfolio_schema.sql')

        if os.path.exists(schema_path):
            with open(schema_path, 'r') as f:
                schema = f.read()

            conn = sqlite3.connect(self.db_path)
            conn.executescript(schema)
            conn.commit()
            conn.close()
        else:
            print(f"Warning: portfolio_schema.sql not found at {schema_path}")

    def create_portfolio(self, name: str, description: str = "",
                        initial_cash: float = 100000.0,
                        currency: str = "USD") -> int:
        """Create a new portfolio."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        try:
            cursor.execute("""
                INSERT INTO portfolios (name, description, currency, initial_cash)
                VALUES (?, ?, ?, ?)
            """, (name, description, currency, initial_cash))

            portfolio_id = cursor.lastrowid

            # Create initial cash deposit transaction
            today = date.today().isoformat()
            cursor.execute("""
                INSERT INTO portfolio_transactions
                (portfolio_id, transaction_date, transaction_type, amount, notes)
                VALUES (?, ?, 'DEPOSIT', ?, 'Initial deposit')
            """, (portfolio_id, today, initial_cash))

            # Create initial valuation
            cursor.execute("""
                INSERT INTO portfolio_valuations_daily
                (portfolio_id, date, cash_balance, securities_value, total_value, cumulative_return)
                VALUES (?, ?, ?, 0, ?, 0)
            """, (portfolio_id, today, initial_cash, initial_cash))

            conn.commit()
            return portfolio_id
        finally:
            conn.close()

    def add_transaction(self, portfolio_id: int, transaction_date: str,
                       transaction_type: str, ticker: Optional[str] = None,
                       quantity: Optional[float] = None, price: Optional[float] = None,
                       amount: Optional[float] = None, fees: float = 0,
                       notes: str = "") -> int:
        """
        Add a transaction to the portfolio.

        Args:
            portfolio_id: Portfolio ID
            transaction_date: Date in YYYY-MM-DD format
            transaction_type: 'BUY', 'SELL', 'DEPOSIT', 'WITHDRAWAL', 'DIVIDEND'
            ticker: Stock ticker (required for BUY/SELL)
            quantity: Number of shares (required for BUY/SELL)
            price: Price per share (required for BUY/SELL)
            amount: Total amount for DEPOSIT/WITHDRAWAL/DIVIDEND
            fees: Transaction fees
            notes: Optional notes

        Returns:
            transaction_id
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        try:
            # Calculate amount if not provided
            if amount is None and transaction_type in ('BUY', 'SELL'):
                if quantity is None or price is None:
                    raise ValueError("quantity and price required for BUY/SELL")

                if transaction_type == 'BUY':
                    amount = -(quantity * price + fees)  # Cash out
                else:  # SELL
                    amount = quantity * price - fees  # Cash in

            # Insert transaction
            cursor.execute("""
                INSERT INTO portfolio_transactions
                (portfolio_id, transaction_date, transaction_type, ticker,
                 quantity, price, amount, fees, notes)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (portfolio_id, transaction_date, transaction_type, ticker,
                  quantity, price, amount, fees, notes))

            transaction_id = cursor.lastrowid

            # Update holdings for BUY/SELL
            if transaction_type in ('BUY', 'SELL'):
                self._update_holdings(cursor, portfolio_id, ticker,
                                    quantity if transaction_type == 'BUY' else -quantity,
                                    price, transaction_date)

            conn.commit()
            return transaction_id
        finally:
            conn.close()

    def _update_holdings(self, cursor: sqlite3.Cursor, portfolio_id: int,
                        ticker: str, quantity_delta: float, price: float,
                        transaction_date: str):
        """Update portfolio holdings after a transaction."""
        # Get current holding
        cursor.execute("""
            SELECT quantity, avg_cost, first_acquired
            FROM portfolio_holdings
            WHERE portfolio_id = ? AND ticker = ?
        """, (portfolio_id, ticker))

        result = cursor.fetchone()

        if result:
            current_qty, avg_cost, first_acquired = result
            new_qty = current_qty + quantity_delta

            if new_qty < -0.0001:  # Allow for floating point errors
                raise ValueError(f"Cannot sell {abs(quantity_delta)} shares of {ticker}. Only {current_qty} available.")

            if new_qty < 0.0001:  # Position closed
                cursor.execute("""
                    DELETE FROM portfolio_holdings
                    WHERE portfolio_id = ? AND ticker = ?
                """, (portfolio_id, ticker))
            else:
                # Update average cost for buys
                if quantity_delta > 0:  # Buy
                    new_avg_cost = ((current_qty * avg_cost) + (quantity_delta * price)) / new_qty
                else:  # Sell - keep same avg cost
                    new_avg_cost = avg_cost

                cursor.execute("""
                    UPDATE portfolio_holdings
                    SET quantity = ?, avg_cost = ?, last_updated = CURRENT_TIMESTAMP
                    WHERE portfolio_id = ? AND ticker = ?
                """, (new_qty, new_avg_cost, portfolio_id, ticker))
        else:
            # New holding
            if quantity_delta < 0:
                raise ValueError(f"Cannot sell {ticker} - no position exists")

            cursor.execute("""
                INSERT INTO portfolio_holdings
                (portfolio_id, ticker, quantity, avg_cost, first_acquired)
                VALUES (?, ?, ?, ?, ?)
            """, (portfolio_id, ticker, quantity_delta, price, transaction_date))

    def get_cash_balance(self, portfolio_id: int, as_of_date: Optional[str] = None) -> float:
        """Get current cash balance for a portfolio."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        if as_of_date:
            cursor.execute("""
                SELECT SUM(amount) FROM portfolio_transactions
                WHERE portfolio_id = ? AND transaction_date <= ?
            """, (portfolio_id, as_of_date))
        else:
            cursor.execute("""
                SELECT SUM(amount) FROM portfolio_transactions
                WHERE portfolio_id = ?
            """, (portfolio_id,))

        result = cursor.fetchone()
        conn.close()

        return result[0] if result[0] is not None else 0.0

    def get_holdings(self, portfolio_id: int) -> List[Dict]:
        """Get current holdings for a portfolio."""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        cursor.execute("""
            SELECT ticker, quantity, avg_cost, first_acquired, last_updated
            FROM portfolio_holdings
            WHERE portfolio_id = ?
            ORDER BY ticker
        """, (portfolio_id,))

        holdings = [dict(row) for row in cursor.fetchall()]
        conn.close()

        return holdings

    def get_transactions(self, portfolio_id: int,
                        start_date: Optional[str] = None,
                        end_date: Optional[str] = None) -> List[Dict]:
        """Get transaction history for a portfolio."""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        query = """
            SELECT transaction_id, transaction_date, transaction_type, ticker,
                   quantity, price, amount, fees, notes, created_at
            FROM portfolio_transactions
            WHERE portfolio_id = ?
        """
        params = [portfolio_id]

        if start_date:
            query += " AND transaction_date >= ?"
            params.append(start_date)

        if end_date:
            query += " AND transaction_date <= ?"
            params.append(end_date)

        query += " ORDER BY transaction_date DESC, transaction_id DESC"

        cursor.execute(query, params)
        transactions = [dict(row) for row in cursor.fetchall()]
        conn.close()

        return transactions

    def list_portfolios(self) -> List[Dict]:
        """List all portfolios."""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        cursor.execute("""
            SELECT portfolio_id, name, description, currency, initial_cash, created_at
            FROM portfolios
            ORDER BY name
        """)

        portfolios = [dict(row) for row in cursor.fetchall()]
        conn.close()

        return portfolios
