import yfinance as yf
t=yf.Ticker("HLAG.DE")
h=t.history(period="5d", interval="1d", auto_adjust=False)
if len(h)>0:
    for idx, row in h.iterrows():
        print(f"{idx.date()}\t{row['Close']:.2f}")
else:
    print("No data for HLAG.DE")
