"""
Populate ETF names in ticker_metadata table for tooltip display
"""
import sqlite3
import os
from constants import DB_PATH, get_db_connection
import argparse
import re
from typing import Optional

# Optional: yfinance for auto-filling missing ETF names
try:
    import yfinance as yf
    _HAS_YF = True
except Exception:
    _HAS_YF = False

# Common ETF names mapping
ETF_NAMES = {
    'SPY': 'SPDR S&P 500 ETF Trust',
    'QQQ': 'Invesco QQQ Trust',
    'IWM': 'iShares Russell 2000 ETF',
    'DIA': 'SPDR Dow Jones Industrial Average ETF',
    'VTI': 'Vanguard Total Stock Market ETF',
    'VOO': 'Vanguard S&P 500 ETF',
    'EFA': 'iShares MSCI EAFE ETF',
    'EEM': 'iShares MSCI Emerging Markets ETF',
    'GLD': 'SPDR Gold Shares',
    'SLV': 'iShares Silver Trust',
    'XLF': 'Financial Select Sector SPDR Fund',
    'XLE': 'Energy Select Sector SPDR Fund', 
    'XLK': 'Technology Select Sector SPDR Fund',
    'XLV': 'Health Care Select Sector SPDR Fund',
    'XLI': 'Industrial Select Sector SPDR Fund',
    'XLY': 'Consumer Discretionary Select Sector SPDR',
    'XLP': 'Consumer Staples Select Sector SPDR',
    'XLU': 'Utilities Select Sector SPDR Fund',
    'XLB': 'Materials Select Sector SPDR Fund',
    'XLRE': 'Real Estate Select Sector SPDR Fund',
    'XLC': 'Communication Services Select Sector SPDR',
    'VNQ': 'Vanguard Real Estate ETF',
    'VEA': 'Vanguard FTSE Developed Markets ETF',
    'VWO': 'Vanguard FTSE Emerging Markets ETF',
    'AGG': 'iShares Core U.S. Aggregate Bond ETF',
    'TLT': 'iShares 20+ Year Treasury Bond ETF',
    'IEF': 'iShares 7-10 Year Treasury Bond ETF',
    'SHY': 'iShares 1-3 Year Treasury Bond ETF',
    'LQD': 'iShares iBoxx $ Investment Grade Corporate Bond ETF',
    'HYG': 'iShares iBoxx $ High Yield Corporate Bond ETF',
    'ARKK': 'ARK Innovation ETF',
    'ARKG': 'ARK Genomic Revolution ETF',
    'ARKQ': 'ARK Autonomous Technology & Robotics ETF',
    'ARKW': 'ARK Next Generation Internet ETF',
    'ARKF': 'ARK Fintech Innovation ETF',
    'ICLN': 'iShares Global Clean Energy ETF',
    'SOXX': 'iShares Semiconductor ETF',
    'IBB': 'iShares Biotechnology ETF',
    'VIG': 'Vanguard Dividend Appreciation ETF',
    'VYM': 'Vanguard High Dividend Yield ETF',
    'SCHD': 'Schwab US Dividend Equity ETF',
    'DVY': 'iShares Select Dividend ETF',
    'ALLW': 'SPDR MSCI ACWI Climate Action World ETF',
    'RSP': 'Invesco S&P 500 Equal Weight ETF',
    'SPLG': 'SPDR Portfolio S&P 500 ETF',
    'MDY': 'SPDR S&P MidCap 400 ETF Trust',
    'IJR': 'iShares Core S&P Small-Cap ETF',
    'MTUM': 'iShares MSCI USA Momentum Factor ETF',
    'VLUE': 'iShares MSCI USA Value Factor ETF',
    'QUAL': 'iShares MSCI USA Quality Factor ETF',
    'SPLV': 'Invesco S&P 500 Low Volatility ETF',
    # iShares style/factor
    'IWF': 'iShares Russell 1000 Growth ETF',
    'IWD': 'iShares Russell 1000 Value ETF',
    'IWO': 'iShares Russell 2000 Growth ETF',
    'IWN': 'iShares Russell 2000 Value ETF',
    'IEFA': 'iShares Core MSCI EAFE ETF',
    'SPEM': 'SPDR Portfolio Emerging Markets ETF',
    'TIP': 'iShares TIPS Bond ETF',
    'BND': 'Vanguard Total Bond Market ETF',
    'IEI': 'iShares 3-7 Year Treasury Bond ETF',
    'BIL': 'SPDR Bloomberg 1-3 Month T-Bill ETF',
    'SHV': 'iShares Short Treasury Bond ETF',
    'EMB': 'iShares J.P. Morgan USD Emerging Markets Bond ETF',
    'JNK': 'SPDR Bloomberg High Yield Bond ETF',
    'BNDX': 'Vanguard Total International Bond ETF',
    # Multi-asset / risk parity
    'RPAR': 'RPAR Risk Parity ETF',
    'AOR': 'iShares Core Growth Allocation ETF',
    'AOM': 'iShares Core Moderate Allocation ETF',
    'NTSX': 'WisdomTree U.S. Efficient Core Fund',
    'UPAR': 'UPAR Ultra Risk Parity ETF',
    # International developed and emerging broad
    'VUG': 'Vanguard Growth ETF',
    'VTV': 'Vanguard Value ETF',
    'VGT': 'Vanguard Information Technology ETF',
    'VB': 'Vanguard Small-Cap ETF',
    'VBR': 'Vanguard Small-Cap Value ETF',
    'IVV': 'iShares Core S&P 500 ETF',
    'VXUS': 'Vanguard Total International Stock ETF',
    'VT': 'Vanguard Total World Stock ETF',
    'VEU': 'Vanguard FTSE All-World ex-US ETF',
    'SCZ': 'iShares MSCI EAFE Small-Cap ETF',
    'DXJ': 'WisdomTree Japan Hedged Equity Fund',
    'HEDJ': 'WisdomTree Europe Hedged Equity Fund',
    'ASHR': 'Xtrackers Harvest CSI 300 China A-Shares ETF',
    'VGK': 'Vanguard FTSE Europe ETF',
    'VPL': 'Vanguard FTSE Pacific ETF',
    'VNQI': 'Vanguard Global ex-US Real Estate ETF',
    'VIGI': 'Vanguard International Dividend Appreciation ETF',
    'VSS': 'Vanguard FTSE All-World ex-US Small-Cap ETF',
    'IEMG': 'iShares Core MSCI Emerging Markets ETF',
    'EMQQ': 'EMQQ Emerging Markets Internet & Ecommerce ETF',
    'EEMV': 'iShares MSCI Emerging Markets Min Vol Factor ETF',
    'DGS': 'WisdomTree Emerging Markets SmallCap Dividend Fund',
    'DGRO': 'iShares Core Dividend Growth ETF',
    'DTD': 'WisdomTree U.S. Total Dividend ETF',
    'NOBL': 'ProShares S&P 500 Dividend Aristocrats ETF',
    'PFF': 'iShares Preferred & Income Securities ETF',
    'IGSB': 'iShares Short-Term Corporate Bond ETF',
    'IGIB': 'iShares Intermediate-Term Corporate Bond ETF',
    'EMLC': 'VanEck J.P. Morgan EM Local Currency Bond ETF',
    'GOVT': 'iShares U.S. Treasury Bond ETF',
    'IAGG': 'iShares Core International Aggregate Bond ETF',
    'MUB': 'iShares National Muni Bond ETF',
    # Country ETFs (developed)
    'EWJ': 'iShares MSCI Japan ETF',
    'EWU': 'iShares MSCI United Kingdom ETF',
    'EWG': 'iShares MSCI Germany ETF',
    'EWQ': 'iShares MSCI France ETF',
    'EWC': 'iShares MSCI Canada ETF',
    'EWA': 'iShares MSCI Australia ETF',
    'EWL': 'iShares MSCI Switzerland ETF',
    'EWS': 'iShares MSCI Singapore ETF',
    'EWI': 'iShares MSCI Italy ETF',
    'EWP': 'iShares MSCI Spain ETF',
    'EWN': 'iShares MSCI Netherlands ETF',
    'EWD': 'iShares MSCI Sweden ETF',
    'EWO': 'iShares MSCI Austria ETF',
    'EWH': 'iShares MSCI Hong Kong ETF',
    'EWK': 'iShares MSCI Belgium ETF',
    'EWM': 'iShares MSCI Malaysia ETF',
    'EDEN': 'iShares MSCI Denmark ETF',
    'EFNL': 'iShares MSCI Finland ETF',
    'EIRL': 'iShares MSCI Ireland ETF',
    'EIS': 'iShares MSCI Israel ETF',
    'ENZL': 'iShares MSCI New Zealand ETF',
    'ENOR': 'iShares MSCI Norway ETF',
    # Country ETFs (emerging/frontier)
    'EWT': 'iShares MSCI Taiwan ETF',
    'EWY': 'iShares MSCI South Korea ETF',
    'EZA': 'iShares MSCI South Africa ETF',
    'EWZ': 'iShares MSCI Brazil ETF',
    'EWW': 'iShares MSCI Mexico ETF',
    'TUR': 'iShares MSCI Turkey ETF',
    'THD': 'iShares MSCI Thailand ETF',
    'EPOL': 'iShares MSCI Poland ETF',
    'EIDO': 'iShares MSCI Indonesia ETF',
    'FM': 'iShares MSCI Frontier and Select EM ETF',
    'FXI': 'iShares China Large-Cap ETF',
    'GXC': 'SPDR S&P China ETF',
    'INDA': 'iShares MSCI India ETF',
    'RSX': 'VanEck Russia ETF',
    # Thematic and sector ETFs
    'TAN': 'Invesco Solar ETF',
    'LIT': 'Global X Lithium & Battery Tech ETF',
    'QCLN': 'First Trust NASDAQ Clean Edge Green Energy Index Fund',
    'PBW': 'Invesco WilderHill Clean Energy ETF',
    'FAN': 'First Trust Global Wind Energy ETF',
    'SMH': 'VanEck Semiconductor ETF',
    'PAVE': 'Global X U.S. Infrastructure Development ETF',
    'MJ': 'ETFMG Alternative Harvest ETF',
    'XME': 'SPDR S&P Metals & Mining ETF',
    'PICK': 'iShares MSCI Global Metals & Mining Producers ETF',
    'GDX': 'VanEck Gold Miners ETF',
    'GDXJ': 'VanEck Junior Gold Miners ETF',
    'SIL': 'Global X Silver Miners ETF',
    # Commodities, currencies, and inflation
    'USO': 'United States Oil Fund, LP',
    'DBA': 'Invesco DB Agriculture Fund',
    'BNO': 'United States Brent Oil Fund, LP',
    'UCO': 'ProShares Ultra Bloomberg Crude Oil',
    'UNG': 'United States Natural Gas Fund, LP',
    'UGA': 'United States Gasoline Fund, LP',
    'BOIL': 'ProShares Ultra Bloomberg Natural Gas',
    'KOLD': 'ProShares UltraShort Bloomberg Natural Gas',
    'IAU': 'iShares Gold Trust',
    'CPER': 'United States Copper Index Fund',
    'PPLT': 'abrdn Physical Platinum Shares ETF',
    'PALL': 'abrdn Physical Palladium Shares ETF',
    'DBC': 'Invesco DB Commodity Index Tracking Fund',
    'GSG': 'iShares S&P GSCI Commodity-Indexed Trust',
    'COMB': 'GraniteShares Bloomberg Commodity Broad Strategy No K-1 ETF',
    'COMT': 'iShares Commodities Select Strategy ETF',
    'PDBC': 'Invesco Optimum Yield Diversified Commodity Strategy No K-1 ETF',
    'WEAT': 'Teucrium Wheat Fund',
    'CORN': 'Teucrium Corn Fund',
    'SOYB': 'Teucrium Soybean Fund',
    'CANE': 'Teucrium Sugar Fund',
    'COCO': 'Teucrium Cocoa ETF',
    'COW': 'iPath Bloomberg Livestock Subindex Total Return ETN',
    'UUP': 'Invesco DB US Dollar Index Bullish Fund',
    'UDN': 'Invesco DB US Dollar Index Bearish Fund',
    'FXE': 'Invesco CurrencyShares Euro Trust',
    'FXB': 'Invesco CurrencyShares British Pound Sterling Trust',
    'FXY': 'Invesco CurrencyShares Japanese Yen Trust',
    'FXA': 'Invesco CurrencyShares Australian Dollar Trust',
    'FXC': 'Invesco CurrencyShares Canadian Dollar Trust',
    'FXF': 'Invesco CurrencyShares Swiss Franc Trust',
    'CYB': 'WisdomTree Chinese Yuan Strategy Fund',
    'RINF': 'ProShares Inflation Expectations ETF',
    # Leveraged ETFs
    'QLD': 'ProShares Ultra QQQ',
    'SSO': 'ProShares Ultra S&P500',
    'UPRO': 'ProShares UltraPro S&P500',
    'TQQQ': 'ProShares UltraPro QQQ',
    'SOXL': 'Direxion Daily Semiconductor Bull 3x Shares',
    'SPXL': 'Direxion Daily S&P 500 Bull 3x Shares',
    'TMF': 'Direxion Daily 20+ Year Treasury Bull 3x Shares',
    'TNA': 'Direxion Daily Small Cap Bull 3x Shares',
    'FAS': 'Direxion Daily Financial Bull 3x Shares',
    'ERX': 'Direxion Daily Energy Bull 2x Shares',
    'LABU': 'Direxion Daily S&P Biotech Bull 3x Shares',
    'NUGT': 'Direxion Daily Gold Miners Bull 2x Shares',
    'JNUG': 'Direxion Daily Junior Gold Miners Bull 2x Shares',
    # Inverse ETFs/ETNs
    'PSQ': 'ProShares Short QQQ',
    'SH': 'ProShares Short S&P500',
    'SDS': 'ProShares UltraShort S&P500',
    'SPXU': 'ProShares UltraPro Short S&P500',
    'SPXS': 'Direxion Daily S&P 500 Bear 3x Shares',
    'SQQQ': 'ProShares UltraPro Short QQQ',
    'SDOW': 'ProShares UltraPro Short Dow30',
    'SRTY': 'ProShares UltraPro Short Russell2000',
    'TZA': 'Direxion Daily Small Cap Bear 3x Shares',
    'FAZ': 'Direxion Daily Financial Bear 3x Shares',
    'ERY': 'Direxion Daily Energy Bear 2x Shares',
    'LABD': 'Direxion Daily S&P Biotech Bear 3x Shares',
    'DRIP': 'Direxion Daily S&P Oil & Gas Exp. & Prod. Bear 2x Shares',
    'DUST': 'Direxion Daily Gold Miners Bear 2x Shares',
    'JDST': 'Direxion Daily Junior Gold Miners Bear 2x Shares',
    'SCO': 'ProShares UltraShort Bloomberg Crude Oil',
    'VIXY': 'ProShares VIX Short-Term Futures ETF',
    'VXX': 'iPath Series B S&P 500 VIX Short-Term Futures ETN',
    'UVXY': 'ProShares Ultra VIX Short-Term Futures ETF',
    'SVXY': 'ProShares Short VIX Short-Term Futures ETF',
    # Crypto ETFs (spot and futures) and crypto industry
    'IBIT': 'iShares Bitcoin Trust',
    'FBTC': 'Fidelity Wise Origin Bitcoin ETF',
    'ARKB': 'ARK 21Shares Bitcoin ETF',
    'BITB': 'Bitwise Bitcoin ETF',
    'HODL': 'VanEck Bitcoin Trust',
    'BTCO': 'Invesco Galaxy Bitcoin ETF',
    'EZBC': 'Franklin Bitcoin ETF',
    'BRRR': 'Valkyrie Bitcoin Fund',
    'GBTC': 'Grayscale Bitcoin Trust',
    'BITO': 'ProShares Bitcoin Strategy ETF',
    'BTF': 'Valkyrie Bitcoin Strategy ETF',
    'XBTF': 'VanEck Bitcoin Strategy ETF',
    'BITI': 'ProShares Short Bitcoin Strategy ETF',
    'BLOK': 'Amplify Transformational Data Sharing ETF',
    'DAPP': 'VanEck Digital Transformation ETF',
    'BKCH': 'Global X Blockchain ETF',
    'BITQ': 'Bitwise Crypto Industry Innovators ETF',
}

def _yf_name_if_etf(ticker: str) -> Optional[str]:
    """Return a display name for ticker if it's an ETF per yfinance, else None.
    Uses longName then shortName. Requires yfinance to be available.
    """
    if not _HAS_YF:
        return None
    try:
        t = yf.Ticker(ticker)
        info = {}
        # Newer yfinance prefers get_info(); fall back to .info for older versions
        try:
            info = t.get_info()
        except Exception:
            try:
                info = t.info
            except Exception:
                info = {}
        qt = str(info.get('quoteType') or '').upper()
        name = (info.get('longName') or info.get('shortName') or info.get('displayName') or '').strip()
        if qt == 'ETF' or ('ETF' in name.upper()):
            return name if name else None
    except Exception:
        return None
    return None

def _get_data_range(cursor: sqlite3.Cursor, ticker: str):
    """Return (first_date, last_date, data_points) for a given ticker column."""
    cursor.execute(
        f"""
        SELECT 
            MIN(Date) as first_date,
            MAX(Date) as last_date,
            COUNT(*) as data_points
        FROM stock_prices_daily
        WHERE "{ticker}" IS NOT NULL
        """
    )
    row = cursor.fetchone()
    return row if row else (None, None, 0)

def _fallback_name_from_stock_metadata(cursor: sqlite3.Cursor, ticker: str) -> Optional[str]:
    """Fallback to legacy stock_metadata table for a display name if present."""
    try:
        cursor.execute("SELECT name FROM stock_metadata WHERE ticker = ?", (ticker,))
        row = cursor.fetchone()
        if row and row[0]:
            name = str(row[0]).strip()
            return name or None
    except Exception:
        return None
    return None

def main():
    parser = argparse.ArgumentParser(description="Populate ETF names into ticker_metadata."
                                     " Optionally auto-fill missing ETF names via yfinance.")
    parser.add_argument("--auto", action="store_true",
                        help="Auto-fill missing ETF names using yfinance for likely ETF tickers not in the hardcoded map.")
    parser.add_argument("--limit", type=int, default=50,
                        help="Maximum number of unknown tickers to attempt auto-fill for (to avoid rate limits).")
    parser.add_argument("--tickers", type=str, default="",
                        help="Comma/space-separated list of tickers to restrict updates/auto-fill to.")
    args = parser.parse_args()

    print("=== Populating ETF metadata ===")
    
    print(f"Using database: {DB_PATH}")
    if not os.path.exists(DB_PATH):
        print(f"Database not found: {DB_PATH}")
        return
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # First, check what ETFs exist in stock_prices_daily
    print("\n1. Checking ETFs in stock_prices_daily...")
    cursor.execute("PRAGMA table_info(stock_prices_daily)")
    columns = [col[1] for col in cursor.fetchall() if col[1] != 'Date']
    
    # Optional scope filter
    ticker_filter = None
    if args.tickers:
        parts = re.split(r"[\s,]+", args.tickers.strip())
        ticker_filter = {p.upper() for p in parts if p}
        print(f"Ticker filter applied: {sorted(list(ticker_filter))}")

    etfs_in_prices = [col for col in columns if col in ETF_NAMES and (not ticker_filter or col in ticker_filter)]
    print(f"Found {len(etfs_in_prices)} known ETFs in stock_prices_daily")
    
    # Update/insert ETF metadata
    print("\n2. Updating ticker_metadata with ETF names...")
    updated = 0
    inserted = 0
    
    for etf, name in ETF_NAMES.items():
        if ticker_filter and etf not in ticker_filter:
            continue
        if etf not in columns:
            continue  # Skip ETFs not in our database
            
        # Check if ticker exists in metadata
        cursor.execute("SELECT ticker, name FROM ticker_metadata WHERE ticker = ?", (etf,))
        result = cursor.fetchone()
        
        if result:
            # Update existing entry
            cursor.execute("""
                UPDATE ticker_metadata 
                SET name = ?, data_type = 'etf'
                WHERE ticker = ?
            """, (name, etf))
            updated += 1
            print(f"Updated {etf}: {name}")
        else:
            # Get data range for new entry
            cursor.execute(f"""
                SELECT 
                    MIN(Date) as first_date,
                    MAX(Date) as last_date,
                    COUNT(*) as data_points
                FROM stock_prices_daily
                WHERE "{etf}" IS NOT NULL
            """)
            date_result = cursor.fetchone()
            
            if date_result and date_result[2] > 0:
                # Insert new entry
                cursor.execute("""
                    INSERT INTO ticker_metadata 
                    (ticker, name, table_name, data_type, first_date, last_date, data_points)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                """, (etf, name, 'stock_prices_daily', 'etf', 
                      date_result[0], date_result[1], date_result[2]))
                inserted += 1
                print(f"Inserted {etf}: {name}")
    # --- Optional: Auto-fill missing ETF names via yfinance ---
    auto_updated = 0
    auto_inserted = 0
    if args.auto:
        print("\n2b. Auto-filling ETF names (yfinance)...")
        if not _HAS_YF:
            print("yfinance not available; skipping auto-fill.")
        else:
            # Candidates: symbols present in DB but not in hardcoded map and alphabetic (<=5 chars)
            unknown = [t for t in columns if t not in ETF_NAMES and t.isalpha() and len(t) <= 5]
            if ticker_filter:
                unknown = [t for t in unknown if t in ticker_filter]
            # Skip those that already have a non-empty name in ticker_metadata
            placeholders = ",".join(["?"] * len(unknown)) if unknown else None
            existing_named = set()
            if unknown:
                try:
                    cursor.execute(
                        f"SELECT ticker FROM ticker_metadata WHERE ticker IN ({placeholders}) AND COALESCE(NULLIF(name,''), NULL) IS NOT NULL",
                        unknown,
                    )
                    existing_named = {row[0] for row in cursor.fetchall()}
                except Exception:
                    existing_named = set()
            to_try = [t for t in unknown if t not in existing_named]
            if args.limit and args.limit > 0:
                to_try = to_try[: args.limit]
            print(f"Auto-fill candidates: {len(to_try)} (limited by --limit={args.limit})")
            for t in to_try:
                name = _yf_name_if_etf(t)
                dt = 'etf'
                if not name:
                    # Fallback to stock_metadata if possible
                    name = _fallback_name_from_stock_metadata(cursor, t)
                    dt = 'stock' if name else None
                if not name:
                    continue
                # Update or insert
                cursor.execute("SELECT ticker FROM ticker_metadata WHERE ticker = ?", (t,))
                exists = cursor.fetchone()
                if exists:
                    cursor.execute(
                        """
                        UPDATE ticker_metadata 
                        SET name = ?, data_type = ?
                        WHERE ticker = ?
                        """,
                        (name, dt, t),
                    )
                    auto_updated += 1
                    print(f"Auto-updated {t}: {name}")
                else:
                    first_date, last_date, data_points = _get_data_range(cursor, t)
                    if data_points and data_points > 0:
                        cursor.execute(
                            """
                            INSERT INTO ticker_metadata 
                            (ticker, name, table_name, data_type, first_date, last_date, data_points)
                            VALUES (?, ?, ?, ?, ?, ?, ?)
                            """,
                            (t, name, 'stock_prices_daily', dt or 'etf', first_date, last_date, data_points),
                        )
                        auto_inserted += 1
                        print(f"Auto-inserted {t}: {name}")
    
    conn.commit()
    
    print(f"\n=== Summary ===")
    print(f"Updated: {updated} ETFs")
    print(f"Inserted: {inserted} ETFs")
    print(f"Total ETFs with names: {updated + inserted}")
    if args.auto:
        print(f"Auto-filled updated: {auto_updated} ETFs")
        print(f"Auto-filled inserted: {auto_inserted} ETFs")
        print(f"Total after auto-fill: {updated + inserted + auto_updated + auto_inserted}")
    
    # Verify the update
    print("\n3. Verifying ETF metadata...")
    cursor.execute("""
        SELECT ticker, name 
        FROM ticker_metadata 
        WHERE data_type = 'etf' OR ticker IN ({})
        ORDER BY ticker
        LIMIT 10
    """.format(','.join(['?'] * len(list(ETF_NAMES.keys())[:10]))), 
        list(ETF_NAMES.keys())[:10])
    
    results = cursor.fetchall()
    if results:
        print("Sample ETF metadata:")
        for ticker, name in results:
            print(f"  {ticker}: {name}")
    
    conn.close()
    print("\n✓ ETF metadata population complete!")

if __name__ == "__main__":
    main()
