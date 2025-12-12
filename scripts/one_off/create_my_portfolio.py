"""
Interactive script to create your first portfolio
"""
from portfolio_manager import PortfolioManager
from portfolio_valuation import PortfolioValuation
from datetime import date

def create_first_portfolio():
    """Create your first portfolio interactively."""

    pm = PortfolioManager()
    pv = PortfolioValuation()

    print("\n" + "="*60)
    print("CREATE YOUR FIRST PORTFOLIO")
    print("="*60)

    # Portfolio details
    name = input("\nPortfolio name (e.g., 'My Investment Portfolio'): ").strip()
    if not name:
        name = "My First Portfolio"
        print(f"Using default name: {name}")

    description = input("Description (optional): ").strip()

    initial_cash_input = input("Initial cash amount (default $100,000): ").strip()
    if initial_cash_input:
        try:
            initial_cash = float(initial_cash_input.replace(',', '').replace('$', ''))
        except:
            print("Invalid amount, using $100,000")
            initial_cash = 100000.0
    else:
        initial_cash = 100000.0

    # Create portfolio
    print(f"\nCreating portfolio '{name}' with ${initial_cash:,.2f}...")
    portfolio_id = pm.create_portfolio(
        name=name,
        description=description,
        initial_cash=initial_cash
    )
    print(f"✓ Portfolio created! ID: {portfolio_id}")

    # Add transactions
    print("\n" + "-"*60)
    print("ADD TRANSACTIONS")
    print("-"*60)
    print("\nLet's add some stock purchases. Press Enter to skip.")

    transactions_added = 0

    while True:
        print(f"\nTransaction #{transactions_added + 1}")
        ticker = input("  Ticker symbol (e.g., AAPL, MSFT) or Enter to finish: ").strip().upper()

        if not ticker:
            break

        # Get transaction details
        try:
            date_input = input("  Date (YYYY-MM-DD) or Enter for today: ").strip()
            if not date_input:
                date_input = date.today().isoformat()

            quantity = float(input("  Number of shares: ").strip())
            price = float(input("  Price per share: ").strip())
            fees_input = input("  Transaction fees (default $0): ").strip()
            fees = float(fees_input) if fees_input else 0.0

            # Add transaction
            pm.add_transaction(
                portfolio_id=portfolio_id,
                transaction_date=date_input,
                transaction_type="BUY",
                ticker=ticker,
                quantity=quantity,
                price=price,
                fees=fees
            )

            total_cost = quantity * price + fees
            print(f"  ✓ Bought {quantity} shares of {ticker} @ ${price:.2f} (Total: ${total_cost:,.2f})")
            transactions_added += 1

        except Exception as e:
            print(f"  ✗ Error: {e}")
            print("  Skipping this transaction...")

    if transactions_added == 0:
        print("\nNo transactions added. Portfolio created with cash only.")
    else:
        print(f"\n✓ Added {transactions_added} transaction(s)")

        # Calculate valuations
        print("\nCalculating portfolio valuations...")
        try:
            pv.backfill_valuations(portfolio_id=portfolio_id)
            print("✓ Valuations calculated")
        except Exception as e:
            print(f"Warning: Could not calculate valuations: {e}")

    # Show summary
    print("\n" + "="*60)
    print("PORTFOLIO SUMMARY")
    print("="*60)

    # Holdings
    holdings = pm.get_holdings(portfolio_id)
    cash = pm.get_cash_balance(portfolio_id)

    print(f"\nPortfolio: {name} (ID: {portfolio_id})")
    print(f"Cash Balance: ${cash:,.2f}")

    if holdings:
        print("\nHoldings:")
        for h in holdings:
            cost_basis = h['quantity'] * h['avg_cost']
            print(f"  {h['ticker']}: {h['quantity']} shares @ ${h['avg_cost']:.2f} avg cost (Total: ${cost_basis:,.2f})")
    else:
        print("\nNo holdings (cash only)")

    # Performance
    if transactions_added > 0:
        try:
            valuations = pv.get_valuation_history(portfolio_id)
            if valuations:
                latest = valuations[-1]
                print(f"\nCurrent Portfolio Value: ${latest['total_value']:,.2f}")
                if latest['cumulative_return'] is not None:
                    print(f"Total Return: {latest['cumulative_return']*100:.2f}%")
        except:
            pass

    print("\n" + "="*60)
    print("NEXT STEPS")
    print("="*60)
    print(f"""
Your portfolio has been created!

To view it:
    from portfolio_manager import PortfolioManager
    pm = PortfolioManager()
    pm.get_holdings({portfolio_id})

To add more transactions:
    pm.add_transaction(
        portfolio_id={portfolio_id},
        transaction_date="2025-01-15",
        transaction_type="BUY",
        ticker="AAPL",
        quantity=100,
        price=180.50,
        fees=5.00
    )

Via API:
    http://localhost:5000/api/portfolio/{portfolio_id}/holdings
    http://localhost:5000/api/portfolio/{portfolio_id}/valuations

See PORTFOLIO_QUICKSTART.md for more examples!
""")


if __name__ == "__main__":
    try:
        create_first_portfolio()
    except KeyboardInterrupt:
        print("\n\nCancelled by user.")
    except Exception as e:
        print(f"\n\nError: {e}")
        import traceback
        traceback.print_exc()
