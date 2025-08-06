import yfinance as yf
import pandas as pd
import sqlite3
from datetime import datetime, timedelta

# --- CONFIG ---
# Include data starting from December 30th, 2022
START_DATE = "2019-12-31"
END_DATE = datetime.today().strftime("%Y-%m-%d")
# Actively traded ADR tickers (large-cap, high liquidity)
ADR_TICKERS = [
    "BABA", "TSM", "JD", "PDD", "NIO", "MELI", "TM", "SONY", "SAP", "ASML", "BP", "SHEL", "RIO", "TTE", "AZN", "VWAGY",
    "VALE", "PBR", "ITUB", "SHOP", "BNS", "BIDU", "NTES", "SE", "QFIN", "MUFG", "SKM", "KB",
    "INFY", "WIT", "IBN", "HDB", "ABEV", "UL", "HSBC", "NVS", "RHHBY", "UBS", "NXPI", "PHG", "DB", "SIEGY", "NSRGY", "FIG",
]

DB_PATH = "sp500_data.db"
ETF_TICKERS = [
    # Core U.S. market benchmarks
    "SPY", "RSP", "VTI", "QQQ", "DIA", "IWM",
    # U.S. style / factor ETFs
    "MDY", "IJR", "MTUM", "VLUE", "QUAL", "SPLV",
    # Sector ETFs (GICS)
    "XLK", "XLF", "XLE", "XLV", "XLY", "XLB", "XLI", "XLC", "XLP", "XLRE", "XLU",
    # Broad international equity baskets
    "EFA", "EEM", "IEFA", "VWO",
    # Single-country developed market ETFs
    "EWZ", "EWW", "EWJ", "EWU", "EWG", "EWQ", "EWC", "EWA", "EWL", "EWS", "EWI", "EWP", "EWN", "EWD", "EWO", "EWH", "EWK", "EWM", "EDEN", "EFNL", "EIRL", "EIS", "ENZL", "ENOR",
    # Single-country emerging market ETFs
    "EWZ", "EWT", "EWY", "EWW", "EZA", "TUR", "THD", "EPOL", "EIDO", "FM", "FXI",
    # Fixed income & alternative asset ETFs
    "TLT", "HYG", "TIP", "LQD", "VNQ", "BIL", "AGG", "BND", "IEF", "IEI", "SHY", "SHV", "EMB", "JNK", "BNDX",
    # Multi-asset / risk parity ETFs
    "ALLW", "RPAR", "AOR", "AOM", "NTSX", "UPAR", "PARR",
    # Commodities, currencies & volatility
    "GLD","SLV", "USO", "DBA", "UUP", "UDN", "FXE", "FXB", "FXY", "FXA", "CYB", "FXC", "FXF", "DBC", "GSG", "COMB", "PDBC", "BNO", "UNG", "UGA", "KOLD", "BOIL", "IAU", "CPER", "PPLT", "PALL", "WEAT", "CORN", "SOYB", "CANE", "COCO", "COW", "PICK", "XME", "GDX", "GDXJ", "SIL", "RINF", "COMT",
    # Volatility indices (Yahoo '^' symbols) and ETNs
    "^VIX", "^VIX9D", "^VIX1D", "^VIX3M", "^VIX6M", "^VXV", "^VXMT", "^VXD", "^VOLQ", "^VVIX", "^SKEW", "^VXST", "VXX", "UVXY", "SVXY", "^VXN", "^RVX", "^VXO", "^GVZ", "^OVX", "^EVZ", "^VXEEM", "^VXEFA", "^VXEWZ", "^VXFXI", "^VXAZN", "^VXAPL", "^VXGOG", "^VXIBM", "^VXGS", "^VXXLE", "^VXSLV", "^VXTLT", "^VXHYG",
    # Treasury yield index symbols (yields, not prices)
    "^IRX", "^FVX", "^TNX", "^TYX"
]

# --- High-profile non-S&P 500 U.S. stocks to track ---
OTHER_HIGH_PROFILE_STOCKS = [
    "ABNB","COIN","DDOG","DOCU","HOOD","NET","OKTA","PLTR","RBLX","SHOP","SNOW","SOFI","SQ","UBER","ZM",
    "BYND","CELH","CPNG","DASH","FSR","LCID","NU","RIVN","TOST","U","UPST", "CRWV", "FIG",
    # Data Centers
    "AJBU", "DBRG", "CONE", "QTS", "DTCR", "SRVR", "GDS",
]

# --- Foreign exchange tickers (major + EM pairs via Yahoo '=X') ---
FX_TICKERS = [
    # Major USD pairs
    "EURUSD=X", "GBPUSD=X", "USDJPY=X", "USDCHF=X", "AUDUSD=X", "NZDUSD=X", "USDCAD=X",
    # Major crosses
    "EURJPY=X", "EURGBP=X", "EURCHF=X", "GBPJPY=X",
    # Emerging-market USD pairs
    "USDBRL=X", "USDMXN=X", "USDZAR=X", "USDTRY=X", "USDINR=X", "USDIDR=X", "USDCNY=X", "USDHKD=X", 
    "USDKRW=X", "USDRUB=X", "USDCOP=X", "USDCLP=X", "USDPHP=X", "USDTHB=X", "USDPLN=X", "USDHUF=X", 
    "USDCZK=X", "USDRON=X", "USDILS=X",
    # Precious metals as currencies
    "XAUUSD=X", "XAGUSD=X", "XPTUSD=X", "XPDUSD=X",
]

# --- Additional FX-like tickers (extra crosses, indices) ---
ADDITIONAL_FX_TICKERS = [
    # Extra USD crosses
    "USDSGD=X", "USDSEK=X", "USDNOK=X", "USDISK=X", "USDTWD=X", "USDARS=X", "USDSAR=X", "USDAED=X",
    "USDKZT=X", "USDVND=X", "USDKWD=X",
    # Non-USD major crosses
    "AUDJPY=X", "CADJPY=X", "CHFJPY=X", "EURCAD=X", "EURAUD=X", "EURNOK=X", "EURNZD=X", "EURSEK=X", "GBPCAD=X", "GBPAUD=X",
    # Currency indices
    "^DXY", "^BXY", "^EURUSD", "^EURJPY"
]

# --- Top-50 crypto tickers (approximate) ---
CRYPTO_TICKERS = [
    "BTC-USD", "ETH-USD", "USDT-USD", "USDC-USD", "BNB-USD", "XRP-USD", "SOL-USD", "ADA-USD", "DOGE-USD", "TON-USD",
    "TRX-USD", "AVAX-USD", "SHIB-USD", "DOT-USD", "MATIC-USD", "LINK-USD", "ATOM-USD", "LTC-USD", "BCH-USD", "UNI-USD",
    "XLM-USD", "ETC-USD", "FIL-USD", "ICP-USD", "APT-USD", "HBAR-USD", "ARB-USD", "MKR-USD", "VET-USD", "NEAR-USD",
    "OP-USD", "IMX-USD", "KAS-USD", "RNDR-USD", "AAVE-USD", "LDO-USD", "ALGO-USD", "QNT-USD", "EGLD-USD", "SAND-USD",
    "AXS-USD", "XTZ-USD", "THETA-USD", "MANA-USD", "GRT-USD", "CHZ-USD", "FLOW-USD", "XEC-USD", "DASH-USD"
]


# --- Utility: Fetch Brazilian Ibovespa tickers ---

def get_ibovespa_tickers():
    """Return a list of Ibovespa constituent tickers formatted for Yahoo Finance (ending with '.SA').
    Tries to scrape the Wikipedia Ibovespa page; if that fails, falls back to a static list captured July 2025.
    """
    try:
        tables = pd.read_html("https://en.wikipedia.org/wiki/Ibovespa")
        for tbl in tables:
            # The column may be named either 'Ticker' or 'Code' depending on Wiki revision
            candidate_cols = [col for col in tbl.columns if str(col).lower() in ("ticker", "code")]
            if candidate_cols:
                col = candidate_cols[0]
                tickers = (
                    tbl[col]
                    .astype(str)
                    .str.strip()
                    .str.upper()
                    .str.replace(r"\\.B3$", "", regex=True)
                    + ".SA"
                )
                # Filter out invalid entries such as nan or ''
                tickers = [t for t in tickers.unique().tolist() if t and t != "NAN.SA"]
                if tickers:
                    return tickers
    except Exception as e:
        print(f"Warning: Could not scrape Ibovespa constituents: {e}. Falling back to static list.")

    # Static fallback list (Ibovespa July 2025)
    return [
        "ABEV3.SA","AZUL4.SA","B3SA3.SA","BBAS3.SA","BBDC3.SA","BBDC4.SA","BBSE3.SA","BEEF3.SA","BPAC11.SA",
        "BRAP4.SA","BRFS3.SA","BRKM5.SA","BRML3.SA","CCRO3.SA","CIEL3.SA","CMIG4.SA","COGN3.SA","CPFE3.SA",
        "CPLE6.SA","CSAN3.SA","CSNA3.SA","CVCB3.SA","CYRE3.SA","EGIE3.SA","ELET3.SA","ELET6.SA","EMBR3.SA",
        "ENBR3.SA","ENEV3.SA","ENGI11.SA","EQTL3.SA","FLRY3.SA","GGBR4.SA","GOAU4.SA","GOLL4.SA","HAPV3.SA",
        "HGTX3.SA","HYPE3.SA","IGTI11.SA","IRBR3.SA","ITSA4.SA","ITUB4.SA","JBSS3.SA","JHSF3.SA","KLBN11.SA",
        "LREN3.SA","MGLU3.SA","MRFG3.SA","MRVE3.SA","MULT3.SA","NEOE3.SA","PETR3.SA","PETR4.SA","PRIO3.SA",
        "QUAL3.SA","RAIL3.SA","RENT3.SA","SANB11.SA","SBSP3.SA","SULA11.SA","SUZB3.SA","TAEE11.SA","TIMP3.SA",
        "TOTS3.SA","UGPA3.SA","USIM5.SA","VALE3.SA","VIVT3.SA","WEGE3.SA","YDUQ3.SA",
    ]


# --- Main function to orchestrate the download ---
def update_sp500_data():
    # 1. Get S&P 500 list and combine with ETFs
    print("Fetching S&P 500 company list...")
    try:
        sp500 = pd.read_html("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies")[0]
        sp500['Symbol'] = sp500['Symbol'].str.replace('.', '-', regex=False)
        sp500.rename(columns={'Symbol': 'ticker', 'Security': 'name', 'GICS Sector': 'sector'}, inplace=True)
        # 1b. Get Ibovespa tickers (Brazil)
        ibov_tickers = get_ibovespa_tickers()
        print(f"Fetched {len(ibov_tickers)} Ibovespa tickers.")
        all_tickers = sorted(list(set(sp500['ticker'].tolist() + ibov_tickers + ETF_TICKERS + ADR_TICKERS + OTHER_HIGH_PROFILE_STOCKS + FX_TICKERS + ADDITIONAL_FX_TICKERS + CRYPTO_TICKERS)))
    except Exception as e:
        raise SystemExit(f"Failed to fetch S&P 500 list: {e}")

    # 2. Determine what needs to be downloaded
    conn = sqlite3.connect(DB_PATH)
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='stock_prices_daily';")
        table_exists = cursor.fetchone() is not None

        # Load existing data (if any) from the daily prices table
        existing_df = pd.DataFrame()
        if table_exists:
            # Read without date parsing first so that an empty table doesn’t raise a KeyError
            existing_df = pd.read_sql("SELECT * FROM stock_prices_daily", conn)
            if not existing_df.empty and 'Date' in existing_df.columns:
                # Only parse dates and set the index when data actually exists and has a 'Date' column
                existing_df['Date'] = pd.to_datetime(existing_df['Date'])
                existing_df.set_index('Date', inplace=True)

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

        # 6b. Restrict to current ticker universe only
        combined_df = combined_df.reindex(columns=all_tickers)

        # 7. Save to database
        print("Saving data to database...")
        combined_df.astype(float).to_sql("stock_prices_daily", conn, if_exists="replace")
        sp500.to_sql("stock_metadata", conn, if_exists="replace", index=False)
        print(f"Database updated. Now contains {combined_df.shape[1]} securities with {combined_df.shape[0]} daily prices.")

    finally:
        conn.close()

if __name__ == "__main__":
    update_sp500_data()
