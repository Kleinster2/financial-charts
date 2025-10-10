"""
Example script demonstrating portfolio management functionality
"""
from portfolio_manager import PortfolioManager
from portfolio_valuation import PortfolioValuation


def demo_portfolio():
    """Create a sample portfolio with transactions and calculate valuations."""

    pm = PortfolioManager()
    pv = PortfolioValuation()

    # Create a new portfolio
    print("Creating portfolio...")
    portfolio_id = pm.create_portfolio(
        name="My Tech Portfolio",
        description="Long-term tech stock investments",
        initial_cash=100000.0
    )
    print(f"Created portfolio ID: {portfolio_id}")

    # Add some buy transactions
    print("\nAdding transactions...")

    # Buy AAPL on 2025-01-02
    pm.add_transaction(
        portfolio_id=portfolio_id,
        transaction_date="2025-01-02",
        transaction_type="BUY",
        ticker="AAPL",
        quantity=100,
        price=180.50,
        fees=5.00,
        notes="Initial AAPL purchase"
    )
    print("Bought 100 AAPL @ $180.50")

    # Buy MSFT on 2025-01-05
    pm.add_transaction(
        portfolio_id=portfolio_id,
        transaction_date="2025-01-05",
        transaction_type="BUY",
        ticker="MSFT",
        quantity=50,
        price=375.25,
        fees=5.00,
        notes="Initial MSFT purchase"
    )
    print("Bought 50 MSFT @ $375.25")

    # Buy more AAPL on 2025-02-01
    pm.add_transaction(
        portfolio_id=portfolio_id,
        transaction_date="2025-02-01",
        transaction_type="BUY",
        ticker="AAPL",
        quantity=50,
        price=185.00,
        fees=5.00,
        notes="Added to AAPL position"
    )
    print("Bought 50 more AAPL @ $185.00")

    # Sell some MSFT on 2025-03-01
    pm.add_transaction(
        portfolio_id=portfolio_id,
        transaction_date="2025-03-01",
        transaction_type="SELL",
        ticker="MSFT",
        quantity=20,
        price=390.00,
        fees=5.00,
        notes="Partial MSFT sale"
    )
    print("Sold 20 MSFT @ $390.00")

    # Show current holdings
    print("\nCurrent Holdings:")
    holdings = pm.get_holdings(portfolio_id)
    for h in holdings:
        print(f"  {h['ticker']}: {h['quantity']} shares @ avg cost ${h['avg_cost']:.2f}")

    # Show cash balance
    cash = pm.get_cash_balance(portfolio_id)
    print(f"\nCash Balance: ${cash:,.2f}")

    # Calculate valuations
    print("\nCalculating historical valuations...")
    pv.backfill_valuations(
        portfolio_id=portfolio_id,
        start_date="2025-01-02",
        end_date="2025-03-31"
    )

    # Show recent valuations
    print("\nRecent Valuations:")
    valuations = pv.get_valuation_history(
        portfolio_id=portfolio_id,
        start_date="2025-03-25",
        end_date="2025-03-31"
    )

    for v in valuations:
        daily_ret = v['daily_return'] * 100 if v['daily_return'] else 0
        cum_ret = v['cumulative_return'] * 100 if v['cumulative_return'] else 0
        print(f"  {v['date']}: ${v['total_value']:,.2f} "
              f"(Daily: {daily_ret:+.2f}%, Cumulative: {cum_ret:+.2f}%)")

    # Show all transactions
    print("\nTransaction History:")
    transactions = pm.get_transactions(portfolio_id)
    for t in transactions[:10]:  # Show last 10
        if t['transaction_type'] in ('BUY', 'SELL'):
            print(f"  {t['transaction_date']}: {t['transaction_type']} "
                  f"{t['quantity']} {t['ticker']} @ ${t['price']:.2f}")
        else:
            print(f"  {t['transaction_date']}: {t['transaction_type']} ${t['amount']:,.2f}")


if __name__ == "__main__":
    demo_portfolio()
