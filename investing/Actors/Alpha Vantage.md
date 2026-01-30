---
aliases: [Data Vantage]
---
#actor #fintech #data #usa #private

**Alpha Vantage** — Financial data API provider. Free tier for retail/hobbyist, premium for enterprise. Y Combinator backed.

---

## Why Alpha Vantage matters

Primary data source for this vault's fundamentals database. Provides:
- Company financials (income statement, balance sheet, cash flow)
- Earnings data (quarterly/annual EPS, surprises)
- Company overview (market cap, P/E, sector)
- Price data (though we use [[Yahoo Finance]] for prices)

---

## Coverage

| Category | Details |
|----------|---------|
| Stock tickers | 200,000+ across 20+ exchanges |
| Historical depth | 20+ years |
| Technical indicators | 50+ |
| Data types | Fundamentals, prices, forex, crypto, commodities |

**Licensed by NASDAQ** as official US market data provider.

---

## API limits

| Tier | Rate limit | Daily limit | Price |
|------|-----------|-------------|-------|
| Free | 5/minute | 25/day | $0 |
| Premium 75 | 75/minute | Unlimited | $50/mo |
| Premium 150 | 150/minute | Unlimited | $100/mo |
| Premium 300+ | 300-1200/min | Unlimited | $150-250/mo |

**This vault uses free tier** — sufficient for manual fundamentals fetches. Rate limiting built into `fetch_fundamentals.py` (12-second delay between calls).

---

## Integration in this project

\`\`\`bash
# Fetch fundamentals for a ticker
python fetch_fundamentals.py AAPL

# Check data freshness
python fetch_fundamentals.py --status

# Batch refresh (watch daily limit!)
python fetch_fundamentals.py --refresh --priority --limit 20
\`\`\`

**Daily limit handling:** `DailyLimitExceeded` exception added (Jan 2026) to stop gracefully when 500-call limit hit instead of churning through failed API calls.

---

## Limitations

**REITs return empty data** — Alpha Vantage has poor coverage for REITs (e.g., [[Digital Realty]], [[Equinix]]). Manual backfill from stockanalysis.com required.

**International coverage gaps** — Some non-US stocks return partial or no data.

---

## Company

| Detail | Value |
|--------|-------|
| Founded | 2017 |
| Founders | Olivier Porte, Steve Zheng |
| HQ | Boston, MA |
| Employees | ~8 |
| Backing | [[Y Combinator]] |

Started as grad school passion project, grew organically through developer adoption.

---

## Cap table / Funding

| Round | Date | Amount | Investors |
|-------|------|--------|-----------|
| YC | 2017 | ~$150K | [[Y Combinator]] |

*Small bootstrapped team. No known subsequent funding rounds. Likely revenue-funded via premium API subscriptions ($50-250/mo tiers).*

---

## MCP integration

Alpha Vantage launched official **Model Context Protocol (MCP) server** — allows AI assistants (Claude, Copilot, Cursor, ChatGPT) to query financial data via natural language.

---

## Related

- [[Yahoo Finance]] — alternative data source (used for prices)
- [[Y Combinator]] — investor
