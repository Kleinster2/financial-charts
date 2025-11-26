# Corporate Bond Data Guide

Track individual corporate bonds from Apple, Microsoft, Amazon, and Google.

## Quick Start: Free Download from Investing.com

### Step 1: Download CSVs

Click each link, set date range to "Max", click "Download":

**Apple Bonds**
- [AAPL 4.45% 2044](https://www.investing.com/rates-bonds/aapl-4.45-06-may-2044-historical-data)
- [AAPL 3.85% 2043](https://www.investing.com/rates-bonds/aapl-3.85-04-may-2043-historical-data)
- [AAPL 3.00% 2027](https://www.investing.com/rates-bonds/aapl-3-20-jun-2027-historical-data)

**Microsoft Bonds**
- [MSFT 5.30% 2041](https://www.investing.com/rates-bonds/msft-5.3-08-feb-2041-historical-data)
- [MSFT 4.50% 2050](https://www.investing.com/rates-bonds/msft-4.5-01-feb-2050-historical-data)
- [MSFT 3.70% 2042](https://www.investing.com/rates-bonds/msft-3.7-17-aug-2042-historical-data)

**Amazon Bonds**
- [AMZN 3.95% 2052](https://www.investing.com/rates-bonds/amzn-3.95-22-apr-2052-historical-data)
- [AMZN 4.80% 2047](https://www.investing.com/rates-bonds/amzn-4.8-12-dec-2047-historical-data)

**Google/Alphabet Bonds**
- [GOOGL 1.10% 2027](https://www.investing.com/rates-bonds/googl-1.1-10-aug-2027-historical-data)
- [GOOGL 2.25% 2060](https://www.investing.com/rates-bonds/googl-2.25-01-aug-2060-historical-data)

Save CSVs to: `bond_csvs/`

### Step 2: Import to Database

```bash
python import_investing_bond_csvs.py
```

### Step 3: Verify

```bash
sqlite3 market_data.db "SELECT * FROM bond_prices_daily LIMIT 5;"
```

## Data Sources Comparison

| Source | Cost | API | Best For |
|--------|------|-----|----------|
| **Investing.com** | Free | No (manual) | Small scale, free |
| **EODHD** | $60/mo | Yes | Automated daily updates |
| **Corporate Bond ETFs** | Free | Yes (yfinance) | Already in system |
| **FINRA TRACE** | Free | No | Current prices only |
| **WRDS** | Free (academic) | Yes | Research with university access |

## Recommended Approach

### For Most Users: Use Bond ETFs (Free, Already Working)
- **LQD** - iShares Investment Grade Corporate
- **VCIT** - Vanguard Intermediate-Term Corporate
- **IGIB** - iShares Intermediate-Term Corporate

These hold the bonds you care about and are already in your database.

### For Individual Bonds: Investing.com (Free)
1. Download CSVs manually (10 min)
2. Import with script
3. Update weekly/monthly

### For Automated Updates: EODHD ($60/month)
```python
# Example CUSIPs
APPLE_BONDS = ['037833CR9', '037833EN6', '037833CK5']
MSFT_BONDS = ['594918BW3', '594918BV5']
AMZN_BONDS = ['023135BW5', '023135106']
GOOGL_BONDS = ['02079K107', '02079K305']
```

API: `https://eodhd.com/api/bond-fundamentals/{CUSIP}?api_token={TOKEN}`

## Other Sources

### Free
- **Empirasign**: https://www.empirasign.com/findabond/ - Search by CUSIP
- **FINRA TRACE**: http://finra-markets.morningstar.com/BondCenter/ - 15-min delayed

### Paid
- **Finnhub TRACE**: $3,000/month - Tick-level data
- **Cbonds**: Custom pricing - 900,000+ bonds
- **Xignite**: Enterprise pricing

### Academic
- **WRDS TRACE**: Free with university affiliation - Complete historical data

## Troubleshooting

**Download button not working**
- Try different browser
- Disable ad blockers
- Some bonds require free sign-in

**CSV not importing**
- Check file is in `bond_csvs/` folder
- Filename should contain ticker and coupon

**Want more bonds**
- Search Investing.com: `https://www.investing.com/rates-bonds/`
- URL pattern: `[ticker]-[coupon]-[maturity]-historical-data`
