import yfinance as yf

for ticker in ['ORCL', 'AAPL', 'NVDA', 'AMZN']:
    t = yf.Ticker(ticker)
    print(f"\n=== {ticker} ===")
    
    # Check for segment data
    try:
        if hasattr(t, 'revenue_estimate'):
            print("revenue_estimate:", t.revenue_estimate)
    except: pass
    
    try:
        info = t.info
        # Look for segment-related fields
        seg_keys = [k for k in info.keys() if 'segment' in k.lower() or 'revenue' in k.lower()]
        print("Segment-related keys:", seg_keys)
    except Exception as e:
        print(f"info error: {e}")
    
    try:
        # Some yfinance versions have .financials with more detail
        q = t.quarterly_financials
        if q is not None and not q.empty:
            rev_rows = [idx for idx in q.index if 'revenue' in idx.lower()]
            print("Revenue-related rows:", rev_rows)
    except Exception as e:
        print(f"financials error: {e}")
    
    try:
        # Check income_stmt (newer yfinance)
        if hasattr(t, 'income_stmt'):
            stmt = t.income_stmt
            if stmt is not None and not stmt.empty:
                rev_rows = [idx for idx in stmt.index if 'revenue' in idx.lower() or 'segment' in idx.lower()]
                print("income_stmt revenue rows:", rev_rows)
    except Exception as e:
        print(f"income_stmt error: {e}")
