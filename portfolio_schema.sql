-- Portfolio Management Schema
-- Supports multiple portfolios with transaction history and daily valuations

-- Portfolio master table
CREATE TABLE IF NOT EXISTS portfolios (
    portfolio_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    currency TEXT DEFAULT 'USD',
    initial_cash REAL DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Transaction log (buys, sells, deposits, withdrawals)
CREATE TABLE IF NOT EXISTS portfolio_transactions (
    transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
    portfolio_id INTEGER NOT NULL,
    transaction_date DATE NOT NULL,
    transaction_type TEXT NOT NULL, -- 'BUY', 'SELL', 'DEPOSIT', 'WITHDRAWAL', 'DIVIDEND'
    ticker TEXT,  -- NULL for cash transactions
    quantity REAL,  -- shares (positive for buy, negative for sell)
    price REAL,  -- price per share at transaction
    amount REAL NOT NULL,  -- total transaction amount (negative = cash out, positive = cash in)
    fees REAL DEFAULT 0,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (portfolio_id) REFERENCES portfolios(portfolio_id) ON DELETE CASCADE
);

-- Current holdings (materialized view updated after each transaction)
CREATE TABLE IF NOT EXISTS portfolio_holdings (
    holding_id INTEGER PRIMARY KEY AUTOINCREMENT,
    portfolio_id INTEGER NOT NULL,
    ticker TEXT NOT NULL,
    quantity REAL NOT NULL,  -- current shares held
    avg_cost REAL NOT NULL,  -- average cost basis per share
    first_acquired DATE,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(portfolio_id, ticker),
    FOREIGN KEY (portfolio_id) REFERENCES portfolios(portfolio_id) ON DELETE CASCADE
);

-- Daily portfolio valuations (mark-to-market)
CREATE TABLE IF NOT EXISTS portfolio_valuations_daily (
    valuation_id INTEGER PRIMARY KEY AUTOINCREMENT,
    portfolio_id INTEGER NOT NULL,
    date DATE NOT NULL,
    cash_balance REAL NOT NULL,
    securities_value REAL NOT NULL,  -- sum of all positions at market prices
    total_value REAL NOT NULL,  -- cash + securities
    daily_return REAL,  -- (total_value - prev_total_value) / prev_total_value
    cumulative_return REAL,  -- (total_value - initial_cash) / initial_cash
    UNIQUE(portfolio_id, date),
    FOREIGN KEY (portfolio_id) REFERENCES portfolios(portfolio_id) ON DELETE CASCADE
);

-- Daily holdings snapshot (for historical position tracking)
CREATE TABLE IF NOT EXISTS portfolio_holdings_daily (
    snapshot_id INTEGER PRIMARY KEY AUTOINCREMENT,
    portfolio_id INTEGER NOT NULL,
    date DATE NOT NULL,
    ticker TEXT NOT NULL,
    quantity REAL NOT NULL,
    price REAL NOT NULL,  -- closing price
    market_value REAL NOT NULL,  -- quantity * price
    cost_basis REAL NOT NULL,  -- avg_cost * quantity
    unrealized_pnl REAL NOT NULL,  -- market_value - cost_basis
    weight REAL,  -- position weight in portfolio (market_value / total_value)
    FOREIGN KEY (portfolio_id) REFERENCES portfolios(portfolio_id) ON DELETE CASCADE
);

-- Indices for performance
CREATE INDEX IF NOT EXISTS idx_transactions_portfolio_date ON portfolio_transactions(portfolio_id, transaction_date);
CREATE INDEX IF NOT EXISTS idx_holdings_portfolio ON portfolio_holdings(portfolio_id);
CREATE INDEX IF NOT EXISTS idx_valuations_portfolio_date ON portfolio_valuations_daily(portfolio_id, date);
CREATE INDEX IF NOT EXISTS idx_holdings_daily_portfolio_date ON portfolio_holdings_daily(portfolio_id, date);
