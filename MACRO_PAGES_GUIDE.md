# Macro Indicator Pages Guide

## Overview

**5 new pages (49-53)** added to your charting workspace with **18 charts** displaying **31 FRED economic indicators**. These provide comprehensive macro context for market analysis.

## Page Breakdown

### Page 49: Macro Dashboard
**The go-to page for recession signals and market context**

**Charts:**
1. **Treasury Yield Curve** (DGS2, DGS10, DGS30)
   - Shows interest rate environment across maturities
   - Flattening curve = slowing growth expectations

2. **Yield Curve Spread** (T10Y2Y)
   - **KEY RECESSION INDICATOR**
   - Negative = inversion = recession typically follows within 12-18 months
   - Historical inversions: 2006 (→2008 crisis), 2019 (→2020 recession), 2022 (→?)

3. **Inflation Measures** (CPIAUCSL, CPILFESL, T5YIE)
   - Headline CPI vs Core CPI (less volatile)
   - T5YIE = market's inflation expectations
   - Fed targets 2% inflation

4. **Credit Spreads** (BAMLH0A0HYM2, BAMLC0A0CM)
   - High yield spread >1000bp = severe credit stress
   - Widens during recessions/crises (2008, 2020)

### Page 50: Labor Market
**Track employment health - key Fed mandate**

**Charts:**
1. **Unemployment Rates** (UNRATE, U6RATE)
   - U3 (UNRATE) = headline unemployment
   - U6 = includes underemployed + marginally attached
   - Fed targets "maximum employment" (~4% U3)

2. **Nonfarm Payrolls** (PAYEMS)
   - Monthly job gains/losses (in thousands)
   - +200k/month = healthy growth
   - Negative = recession territory

3. **Labor Force Participation** (CIVPART)
   - % of working-age population employed or seeking work
   - Declined post-2008 and COVID
   - Affects "maximum employment" calculation

### Page 51: Economic Activity
**Real economy performance indicators**

**Charts:**
1. **GDP & Real GDP** (GDP, GDPC1)
   - Nominal GDP vs inflation-adjusted real GDP
   - Quarterly updates
   - 2 consecutive negative quarters = technical recession

2. **Consumer Sentiment** (UMCSENT)
   - University of Michigan survey
   - Leading indicator (sentiment drops before spending)
   - Falls sharply before recessions

3. **Retail Sales** (RSXFS)
   - Monthly consumer spending
   - 70% of US economy
   - Decline = weakening growth

### Page 52: Fed Policy
**Monetary policy tracking - QE/QT, rates, liquidity**

**Charts:**
1. **Federal Funds Rate** (FEDFUNDS, DFEDTARU, DFEDTARL)
   - Effective rate vs target range
   - FEDFUNDS lags (monthly data)
   - Targets are real-time

2. **Fed Balance Sheet** (WALCL)
   - Total Fed assets (trillions)
   - Rising = QE (quantitative easing)
   - Falling = QT (quantitative tightening)
   - Peaked at $9T in 2022, now declining

3. **Overnight Reverse Repo** (RRPONTSYD)
   - Parking lot for excess bank reserves
   - High levels = tight liquidity
   - Peaked at $2.5T in 2023

4. **Treasury General Account** (WTREGEN)
   - US government's checking account at Fed
   - Depletes = liquidity injected into system
   - Refills = liquidity drained

### Page 53: Financial Stress
**Crisis detection - credit stress, volatility, systemic risk**

**Charts:**
1. **Financial Stress Index** (STLFSI4)
   - St. Louis Fed composite measure
   - Spikes during crises (2008, 2020)
   - Elevated = systemic stress

2. **Credit Spreads** (BAMLH0A0HYM2, BAMLC0A0CM)
   - Same as Macro Dashboard
   - High yield >1000bp = crisis territory

3. **VIX vs Financial Stress** (^VIX, STLFSI4)
   - **Dual y-axis chart**
   - Correlates during crises
   - VIX = options-implied volatility
   - STLFSI4 = broader systemic stress

4. **TED Spread** (TEDRATE)
   - LIBOR - T-Bill (discontinued 2022)
   - Was key credit stress indicator
   - Historical reference only

## Key Recession Indicators

**Classic warning signs** (check these regularly):

1. **T10Y2Y < 0** (yield curve inversion)
2. **STLFSI4 > 1** (elevated financial stress)
3. **BAMLH0A0HYM2 > 1000** (credit market stress)
4. **UNRATE rising** (unemployment trending up)
5. **UMCSENT falling** (consumer confidence dropping)
6. **2 consecutive negative GDP quarters** (technical recession)

## Using These Pages

### Cross-Page Analysis

**Recession Watch:**
- Page 49 (T10Y2Y inversion) + Page 50 (rising UNRATE) + Page 53 (STLFSI4 spike) = red alert

**Fed Policy Impact:**
- Page 52 (WALCL, FEDFUNDS) → affects Page 49 (yields, spreads)
- Rate hikes → flattens yield curve, widens credit spreads

**Market Context:**
- Page 53 (VIX spike) often coincides with Page 49 (credit spreads widening)
- Labor weakness (Page 50) leads to sentiment drop (Page 51)

### Overlay with Stock Charts

**Combine macro + equity pages:**
- S&P 500 (^GSPC) vs T10Y2Y (yield curve)
- Tech stocks vs FEDFUNDS (rate sensitivity)
- Banks vs BAMLH0A0HYM2 (credit exposure)
- Retail vs RSXFS (consumer spending)

## Data Update Frequencies

| Indicator | Frequency | Lag | Example |
|-----------|-----------|-----|---------|
| DGS2, DGS10, DGS30 | Daily | 1 day | Treasury yields |
| BAMLH0A0HYM2 | Daily | 1 day | Credit spreads |
| FEDFUNDS | Monthly | 1 month | Effective Fed rate |
| DFEDTARU/L | Daily | Real-time | Target rates |
| CPIAUCSL, CPILFESL | Monthly | 2 weeks | CPI releases |
| UNRATE, PAYEMS | Monthly | 1 week | Jobs report |
| GDP, GDPC1 | Quarterly | 1 month | GDP releases |
| UMCSENT | Monthly | Real-time | Survey data |
| WALCL, RRPONTSYD | Weekly | 1 day | Fed H.4.1 report |

## Historical Context

**Major events visible in these charts:**

- **2000-2001**: Dot-com recession (yield curve inversion, rising unemployment)
- **2008-2009**: Financial crisis (massive credit spread widening, STLFSI4 spike, VIX >80)
- **2020**: COVID recession (brief but severe - all indicators spiked)
- **2022-2023**: Rapid Fed tightening (WALCL declining, FEDFUNDS 0→5.5%)
- **2022 Q1-Q3**: Yield curve inversion (recession call ongoing)

## Tips

1. **Check Page 49 first** - Macro Dashboard gives quick overview
2. **Watch T10Y2Y closely** - Most reliable recession predictor
3. **STLFSI4 spikes = pay attention** - Often precedes market stress
4. **Credit spreads lead stocks** - Widening spreads warn of equity weakness
5. **Labor market lags** - Unemployment rises AFTER recession starts
6. **Fed follows data** - Rate decisions based on CPI + UNRATE
7. **Monthly data = patience** - CPI, payrolls, GDP update slowly

## Color Coding

**Consistent colors across pages:**
- **Red/Orange** = Risk/stress indicators (spreads, unemployment, VIX)
- **Blue/Teal** = Rates/yields (treasury rates, inflation expectations)
- **Green** = Growth indicators (GDP, payrolls, retail sales)
- **Purple** = Volatility/sentiment (consumer sentiment, stress index)

## Accessing the Pages

In your charting app:
```
Page 49: Macro Dashboard
Page 50: Labor Market
Page 51: Economic Activity
Page 52: Fed Policy
Page 53: Financial Stress
```

Use the page navigation at the top of the app to switch between pages.

## Maintenance

These pages use the 31 FRED indicators you already downloaded. Daily updates via:
```bash
python update_fred_indicators.py --lookback 60
```

All indicators will stay current automatically.

---

**Created:** 2025-11-21
**Total Charts:** 18
**Total Indicators:** 31 FRED series + ^VIX
**Page Range:** 49-53
**Historical Span:** 1939-2025 (86 years!)
