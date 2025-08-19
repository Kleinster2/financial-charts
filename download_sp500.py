import yfinance as yf
import pandas as pd
import sqlite3
from datetime import datetime, timedelta
import time
import requests
from bs4 import BeautifulSoup

# Import constants
from constants import (DB_FILENAME, DEFAULT_START_DATE, BATCH_SIZE, 
                      RETRY_LIMIT, RETRY_DELAY, TICKER_CATEGORIES,
                      FUTURES_SYMBOLS)

# --- CONFIG ---
# Include data starting from December 30th, 2022
START_DATE = DEFAULT_START_DATE
END_DATE = datetime.today().strftime("%Y-%m-%d")

# These lists should be maintained separately as they're not static
# For now we'll keep them here but could move to a config file later
ADR_TICKERS = [
    'BABA', 'TSM', 'NVO', 'ASML', 'TCEHY', 'TM', 'SAP', 'PDD', 'SHEL',
    'HDBNY', 'AZN', 'BHP', 'SNY', 'HMC', 'NVS', 'TD', 'TTE', 'UL', 'RY',
    'MUFG', 'BP', 'GSK', 'SONY', 'RIO', 'BTI', 'HSBC', 'ENB', 'CNI', 'DEO',
    'SMFG', 'CP', 'SHOP', 'SE', 'IBKR', 'CHKP', 'NICE', 'GLBE', 'CPNG',
    'NU', 'STLA', 'FSLR', 'GRAB', 'ZIM', 'MBAVU', 'OZON', 'XPEV', 'LI', 'NIO',
    'BILI', 'NTES', 'JD', 'BIDU', 'BGNE', 'VIPS', 'IQ', 'WB', 'TME', 'TAL',
    'EDU', 'BZ', 'GOTU', 'YMM', 'DADA', 'SOHU', 'LU', 'FINV', 'API', 'QFIN',
    'ATHM', 'GOOG', 'MSFT', 'AAPL', 'AMZN', 'META', 'NVDA', 'SPY', 'QQQ', 'BTC-USD',
    'ETH-USD', 'LTC-USD'
]

ETF_TICKERS = [
    'XLF', 'XLE', 'XLU', 'XLI', 'XLV', 'XLY', 'XLP', 'XLK', 'XLRE', 'XLB', 'XLC',
    'VIG', 'VUG', 'VTV', 'VYM', 'VGT', 'VNQ', 'VB', 'VBR', 'VOO', 'IVV', 'VTI',
    'VWO', 'VEA', 'VXUS', 'VT', 'AGG', 'BND', 'TLT', 'IEF', 'SHY', 'LQD', 'HYG',
    'MUB', 'TIP', 'GLD', 'IAU', 'SLV', 'PDBC', 'DBC', 'USO', 'UNG', 'GDX', 'GDXJ',
    'EWJ', 'EWZ', 'EWY', 'EWG', 'EWU', 'EWC', 'EWA', 'EWT', 'EWH', 'EWW', 'EWP',
    'EWI', 'EWS', 'FXI', 'INDA', 'RSX', 'ARKG', 'ARKK', 'ARKW', 'ARKQ', 'ARKF',
    'ICLN', 'TAN', 'LIT', 'QCLN', 'PBW', 'FAN', 'SOXX', 'SMH', 'PAVE', 'MJ',
    'DIA', 'IWM', 'IWF', 'IWD', 'IWO', 'IWN', 'MDY', 'VEU', 'SCZ', 'DXJ', 'HEDJ',
    'ASHR', 'VGK', 'VPL', 'VNQI', 'VIGI', 'VSS', 'IEMG', 'EEM', 'EMQQ', 'FM',
    'EEMV', 'DGS', 'DGRO', 'DTD', 'DVY', 'NOBL', 'PFF', 'IGSB', 'IGIB', 'EMB',
    'EMLC', 'GOVT', 'IAGG', 'QLD', 'SSO', 'UPRO', 'TQQQ', 'SOXL', 'SPXL', 'TMF',
    'TNA', 'FAS', 'ERX', 'LABU', 'NUGT', 'JNUG', 'UGAZ', 'UCO', 'BOIL', 'KOLD',
    'PSQ', 'SH', 'SDS', 'SPXU', 'SPXS', 'SQQQ', 'SDOW', 'SRTY', 'TZA', 'FAZ',
    'ERY', 'LABD', 'DRIP', 'DUST', 'JDST', 'DGAZ', 'SCO', 'VXX', 'VIXY', 'UVXY',
    'SVXY', 'SPX', 'NDX', 'RUT', 'DJI', 'GSPC', 'IXIC', 'RUI', 'VIX'
]

# Core indices with the ^prefix
core_indices = TICKER_CATEGORIES['CORE_INDICES']
# Volatility indices
volatility_indices = TICKER_CATEGORIES['VOLATILITY_INDICES']
# Other indices and rates
other_indices = TICKER_CATEGORIES['TREASURY_YIELDS']
# Additional FX tickers (extra crosses, indices)
ADDITIONAL_FX_TICKERS = [
    # Extra USD crosses
    "USDSGD=X", "USDSEK=X", "USDNOK=X", "USDISK=X", "USDTWD=X", "USDARS=X", "USDSAR=X", "USDAED=X",
    "USDKZT=X", "USDVND=X", "USDKWD=X",
    # Non-USD major crosses
    "AUDJPY=X", "CADJPY=X", "CHFJPY=X", "EURCAD=X", "EURAUD=X", "EURNOK=X", "EURNZD=X", "EURSEK=X", "GBPCAD=X", "GBPAUD=X",
    # Currency indices
    "^DXY", "^BXY"
]

# Top-crypto tickers
CRYPTO_TICKERS = [
    "BTC-USD", "ETH-USD", "BNB-USD", "XRP-USD", "SOL-USD", "ADA-USD", "DOGE-USD", "TON-USD",
    "TRX-USD", "AVAX-USD", "SHIB-USD", "DOT-USD", "MATIC-USD", "LINK-USD", "ATOM-USD", "LTC-USD", "BCH-USD", "UNI-USD",
    "XLM-USD", "ETC-USD", "FIL-USD", "ICP-USD", "APT-USD", "HBAR-USD", "ARB-USD", "MKR-USD", "VET-USD", "NEAR-USD",
    "OP-USD", "IMX-USD", "KAS-USD", "RNDR-USD", "AAVE-USD", "LDO-USD", "ALGO-USD", "QNT-USD", "EGLD-USD", "SAND-USD",
    "AXS-USD", "XTZ-USD", "THETA-USD", "MANA-USD", "GRT-USD", "CHZ-USD", "FLOW-USD", "XEC-USD", "DASH-USD", "HYPE-USD"
]

# High-profile non-S&P 500 U.S. stocks to track
OTHER_HIGH_PROFILE_STOCKS = [
    "ABNB","COIN","DDOG","DOCU","HOOD","NET","OKTA","PLTR","RBLX","SHOP","SNOW","SOFI","SQ","UBER","ZM",
    "BYND","CELH","CPNG","DASH","FSR","LCID","MSTR","NU","RIVN","TOST","U","UPST", "CRWV", "FIG", "PSKY",
    # Data Centers
    "AJBU", "DBRG", "CONE", "QTS", "DTCR", "SRVR", "GDS", "GIGA",
    # Crypto / Blockchain
    "CRCL", "CRON",
]

# Crypto ETFs (spot, futures, blockchain)
# -- Bitcoin spot ETFs
bitcoin_spot_etfs = [
    "IBIT", "FBTC", "ARKB", "BITB", "HODL", "BTCO", "EZBC", "BRRR", "GBTC",
]
# -- Bitcoin futures/inverse ETFs
bitcoin_futures_etfs = [
    "BITO", "BTF", "XBTF", "BITI",
]
# -- Blockchain/crypto industry ETFs
blockchain_etfs = [
    "BLOK", "DAPP", "BKCH", "BITQ",
]
# Crypto-exposed equities (miners, exchanges, infrastructure)
CRYPTO_STOCKS = [
    # Miners
    "RIOT", "MARA", "HUT", "HIVE", "BITF", "CIFR", "CORZ", "IREN", "WULF", "CLSK", "BTBT", "SDIG", "CAN",
    # Platforms / infra
    "BKKT",
]

# Foreign exchange tickers (major + EM pairs)
def build_fx_tickers():
    major_currencies = TICKER_CATEGORIES['MAJOR_CURRENCIES']
    emerging_currencies = TICKER_CATEGORIES['EMERGING_CURRENCIES']
    fx = []
    # All major crosses, both directions (excludes self-crosses automatically)
    fx += make_pairs(major_currencies, major_currencies)
    # USD-EM pairs, both directions
    fx += make_pairs(["USD"], emerging_currencies)
    fx += make_pairs(emerging_currencies, ["USD"])
    # Precious metals as currencies
    fx += ["XAUUSD=X", "XAGUSD=X", "XPTUSD=X", "XPDUSD=X"]
    return unique_preserve(fx)

def make_pairs(bases, quotes, suffix="=X"):
    """Generate Yahoo FX tickers like 'EURUSD=X' for all base-quote combos where base != quote."""
    return [f"{b}{q}{suffix}" for b in bases for q in quotes if b != q]

def unique_preserve(seq):
    seen = set()
    out = []
    for s in seq:
        if s not in seen:
            seen.add(s)
            out.append(s)
    return out

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
def update_sp500_data(verbose: bool = True):
    # 1. Get S&P 500 list and combine with ETFs
    def vprint(*args, **kwargs):
        if verbose:
            print(*args, **kwargs)

    vprint("Fetching S&P 500 company list...")
    try:
        sp500 = pd.read_html("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies")[0]
        sp500['Symbol'] = sp500['Symbol'].str.replace('.', '-', regex=False)
        sp500.rename(columns={'Symbol': 'ticker', 'Security': 'name', 'GICS Sector': 'sector'}, inplace=True)
        # 1b. Get Ibovespa tickers (Brazil)
        ibov_tickers = get_ibovespa_tickers()
        vprint(f"Fetched {len(ibov_tickers)} Ibovespa tickers.")
        vprint(f"FX tickers generated: {len(build_fx_tickers())}; additional FX-like: {len(ADDITIONAL_FX_TICKERS)}")
        all_tickers = sorted(list(set(
            sp500['ticker'].tolist()
            + ibov_tickers
            + ETF_TICKERS
            + ADR_TICKERS
            + OTHER_HIGH_PROFILE_STOCKS
            + CRYPTO_STOCKS
            + build_fx_tickers()
            + ADDITIONAL_FX_TICKERS
            + CRYPTO_TICKERS
        )))
    except Exception as e:
        raise SystemExit(f"Failed to fetch S&P 500 list: {e}")

    # 2. Determine what needs to be downloaded
    conn = sqlite3.connect(DB_FILENAME)
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='stock_prices_daily';")
        table_exists = cursor.fetchone() is not None
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='stock_volumes_daily';")
        vol_table_exists = cursor.fetchone() is not None

        # Load existing data (if any) from the daily prices table
        existing_df = pd.DataFrame()
        existing_vol_df = pd.DataFrame()
        if table_exists:
            # Read without date parsing first so that an empty table doesn’t raise a KeyError
            existing_df = pd.read_sql("SELECT * FROM stock_prices_daily", conn)
            if not existing_df.empty and 'Date' in existing_df.columns:
                # Robust date parsing to handle mixed formats (e.g., "YYYY-MM-DD" and locale-specific)
                def _safe_parse(s):
                    try:
                        return pd.to_datetime(s, format="%Y-%m-%d", errors="raise")
                    except Exception:
                        # Fallback: let pandas infer or treat dayfirst as needed; coerce invalid to NaT
                        return pd.to_datetime(s, errors="coerce", dayfirst=False)
                existing_df['Date'] = existing_df['Date'].apply(_safe_parse)
                existing_df.dropna(subset=['Date'], inplace=True)
                existing_df.set_index('Date', inplace=True)
        if vol_table_exists:
            existing_vol_df = pd.read_sql("SELECT * FROM stock_volumes_daily", conn)
            if not existing_vol_df.empty and 'Date' in existing_vol_df.columns:
                existing_vol_df['Date'] = pd.to_datetime(existing_vol_df['Date'])
                existing_vol_df.set_index('Date', inplace=True)

        # 3. Download data in a fault-tolerant way
        vprint(f"Downloading/updating data for {len(all_tickers)} securities...")
        # Use yfinance's grouping to handle failed downloads gracefully
        data = yf.download(all_tickers, start=START_DATE, end=END_DATE, auto_adjust=True, group_by='ticker')

        if data.empty:
            print("No data returned from Yahoo Finance.")
            return

        # 4. Process downloaded data ticker by ticker
        processed_dfs = []
        processed_vol_dfs = []
        for ticker in all_tickers:
            if ticker in data and not data[ticker].empty:
                # Extract just the 'Close' price and rename the series to the ticker
                close_series = data[ticker][['Close']].rename(columns={'Close': ticker})
                processed_dfs.append(close_series)
                # Extract 'Volume' where available
                if 'Volume' in data[ticker].columns:
                    vol_series = data[ticker][['Volume']].rename(columns={'Volume': ticker})
                    processed_vol_dfs.append(vol_series)
            else:
                print(f"- Warning: Could not download data for {ticker}. It will be skipped.")

        if not processed_dfs:
            print("Data processing failed for all tickers.")
            return

        # 5. Combine all processed dataframes into one (prices)
        new_data_df = pd.concat(processed_dfs, axis=1)
        new_data_df.index = pd.to_datetime(new_data_df.index)
        # 5b. Combine volumes (if any)
        new_vol_df = pd.DataFrame()
        if processed_vol_dfs:
            new_vol_df = pd.concat(processed_vol_dfs, axis=1)
            new_vol_df.index = pd.to_datetime(new_vol_df.index)

        # 6. Merge with existing data, giving precedence to new data (prices)
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

        # 6b. Restrict to current ticker universe only (prices)
        combined_df = combined_df.reindex(columns=all_tickers)

        # 6c. Merge volumes with existing (if available), giving precedence to new volume data
        combined_vol_df = pd.DataFrame()
        if not new_vol_df.empty or not existing_vol_df.empty:
            if new_vol_df.empty:
                combined_vol_df = existing_vol_df.copy()
            elif existing_vol_df.empty:
                combined_vol_df = new_vol_df.copy()
            else:
                existing_vol_cols = existing_vol_df.columns
                new_vol_cols = new_vol_df.columns
                combined_vol_cols = sorted(list(set(existing_vol_cols) | set(new_vol_cols)))
                existing_vol_df = existing_vol_df.reindex(columns=combined_vol_cols)
                new_vol_df = new_vol_df.reindex(columns=combined_vol_cols)
                combined_vol_df = new_vol_df.combine_first(existing_vol_df)
            # Restrict to current ticker universe only
            combined_vol_df = combined_vol_df.reindex(columns=all_tickers)

        # 7. Save to database
        vprint("Saving data to database...")
        # Ensure index name for proper DB column naming
        index_label = combined_df.index.name or 'Date'
        combined_df.astype(float).to_sql("stock_prices_daily", conn, if_exists="replace", index=True, index_label=index_label)
        if not combined_vol_df.empty:
            combined_vol_df.astype(float).to_sql("stock_volumes_daily", conn, if_exists="replace", index=True, index_label=index_label)
        sp500.to_sql("stock_metadata", conn, if_exists="replace", index=False)
        vprint(f"Database updated. Now contains {combined_df.shape[1]} securities with {combined_df.shape[0]} daily prices.")

    finally:
        conn.close()

if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]
    verbose = True
    if any(a in ("--quiet", "-q") for a in argv):
        verbose = False
    if any(a in ("--verbose", "-v") for a in argv):
        verbose = True
    update_sp500_data(verbose=verbose)
