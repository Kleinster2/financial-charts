import yfinance as yf
import pandas as pd
import sqlite3
from datetime import datetime, timedelta

# --- CONFIG ---
# Include data starting from December 30th, 2022
START_DATE = "2022-12-30"
END_DATE = datetime.today().strftime("%Y-%m-%d")
# Actively traded ADR tickers (large-cap, high liquidity)
ADR_TICKERS = [
    "BABA", "TSM", "JD", "PDD", "NIO", "MELI", "TM", "SONY", "SAP", "ASML", "BP", "SHEL", "RIO", "TTE", "AZN", "VWAGY",
    "VALE", "PBR", "ITUB", "SHOP", "BNS", "BIDU", "NTES", "SE", "QFIN", "MUFG", "SKM", "KB",
    "INFY", "WIT", "IBN", "HDB", "ABEV", "UL", "HSBC", "NVS", "RHHBY", "UBS", "NXPI", "PHG", "DB", "SIEGY", "NSRGY"
]

DB_PATH = "sp500_data.db"
ETF_TICKERS = [
    # Core U.S. market benchmarks
    "SPY", "RSP", "VTI", "QQQ", "DIA", "IWM", "AGG", "GLD",

    # U.S. style / factor ETFs
    "MDY", "IJR", "MTUM", "VLUE", "QUAL", "SPLV",

    # Sector ETFs (GICS)
    "XLK", "XLF", "XLE", "XLV", "XLY", "XLB", "XLI", "XLC", "XLP", "XLRE", "XLU",

    # Broad international equity baskets
    "EFA", "EEM", "IEFA", "VWO",

    # Single-country developed market ETFs
    "EWJ", "EWU", "EWG", "EWQ", "EWC", "EWA", "EWL", "EWS", "EWI", "EWP", "EWN", "EWD", "EWO", "EWH", "EWK", "EWM",

    # Single-country emerging market ETFs
    "EWZ", "EWT", "EWY", "EWW", "EZA", "TUR", "THD", "EPOL", "EIDO", "FM", "FXI",

    # Fixed income & alternative asset ETFs
    "TLT", "HYG", "TIP", "LQD", "VNQ", "BIL", "CRWV",

    # Commodities, currencies & volatility
    "SLV", "USO", "DBA", "UUP", "UDN", "FXE", "FXB", "FXY", "FXA", "CYB", "FXC", "FXF", "DBC", "GSG", "COMB", "PDBC", "BNO", "UNG", "UGA", "KOLD", "BOIL", "IAU", "CPER", "PPLT", "PALL", "WEAT", "CORN", "SOYB", "CANE", "COCO", "COW", "PICK", "XME", "GDX", "GDXJ", "SIL", "RINF", "COMT",
    # Volatility indices (Yahoo '^' symbols) and ETNs
    "^VIX", "^VIX9D", "^VIX3M", "^VIX6M", "^VXD", "^VOLQ", "^VVIX", "^SKEW", 
    "VXX", "UVXY", "SVXY",
    # Additional fixed-income ETFs
    "BND", "IEF", "IEI", "SHY", "SHV", "EMB", "JNK", "BNDX",
    # Treasury yield index symbols (yields, not prices)
    "^IRX", "^FVX", "^TNX", "^TYX"
]


# --- Main function to orchestrate the download ---
def update_sp500_data():
    # 1. Get S&P 500 list and combine with ETFs
    print("Fetching S&P 500 company list...")
    try:
        sp500 = pd.read_html("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies")[0]
        sp500['Symbol'] = sp500['Symbol'].str.replace('.', '-', regex=False)
        sp500.rename(columns={'Symbol': 'ticker', 'Security': 'name', 'GICS Sector': 'sector'}, inplace=True)
        all_tickers = sorted(list(set(sp500['ticker'].tolist() + ETF_TICKERS + ADR_TICKERS)))
    except Exception as e:
        raise SystemExit(f"Failed to fetch S&P 500 list: {e}")

    # 2. Determine what needs to be downloaded
    conn = sqlite3.connect(DB_PATH)
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='stock_prices_daily';")
        table_exists = cursor.fetchone() is not None

        existing_df = pd.DataFrame()
        if table_exists:
            existing_df = pd.read_sql("SELECT * FROM stock_prices_daily", conn, parse_dates=['Date']).set_index('Date')

        # 3. Download data in a fault-tolerant way
        print(f"Downloading/updating data for {len(all_tickers)} securities...")
        # Use yfinance's grouping to handle failed downloads gracefully
        data = yf.download(all_tickers, start=START_DATE, end=END_DATE, auto_adjust=True, group_by='ticker')

        if data.empty:
            print("No data returned from Yahoo Finance.")
            return

        # 4. Process downloaded data ticker by ticker
        processed_dfs = []
        for ticker in all_tickers:
            if ticker in data and not data[ticker].empty:
                # Extract just the 'Close' price and rename the series to the ticker
                close_series = data[ticker][['Close']].rename(columns={'Close': ticker})
                processed_dfs.append(close_series)
            else:
                print(f"- Warning: Could not download data for {ticker}. It will be skipped.")

        if not processed_dfs:
            print("Data processing failed for all tickers.")
            return

        # 5. Combine all processed dataframes into one
        new_data_df = pd.concat(processed_dfs, axis=1)
        new_data_df.index = pd.to_datetime(new_data_df.index)

        # 6. Merge with existing data, giving precedence to new data
        if not existing_df.empty:
            # Align columns to ensure safe combination
            existing_cols = existing_df.columns
            new_cols = new_data_df.columns
            combined_cols = sorted(list(set(existing_cols) | set(new_cols)))
            
            existing_df = existing_df.reindex(columns=combined_cols)
            new_data_df = new_data_df.reindex(columns=combined_cols)
            
            combined_df = new_data_df.combine_first(existing_df)
        else:
            combined_df = new_data_df

        # 7. Save to database
        print("Saving data to database...")
        combined_df.to_sql("stock_prices_daily", conn, if_exists="replace")
        sp500.to_sql("stock_metadata", conn, if_exists="replace", index=False)
        print(f"Database updated. Now contains {combined_df.shape[1]} securities with {combined_df.shape[0]} daily prices.")

    finally:
        conn.close()

if __name__ == "__main__":
    update_sp500_data()
