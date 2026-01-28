#concept #fintech #private-markets #venturecapital

Trading private company shares before IPO. Includes employee sales, VC syndication SPVs, tender offers, and dedicated platforms.

For broader context, see [[Private markets]]. For retail derivatives, see [[Tokenized private shares]].

---

## Why secondaries exist

Private companies stay private longer → shareholders need liquidity:

| Stakeholder | Why they sell |
|-------------|---------------|
| **Employees** | Concentrated wealth, life events, taxes |
| **Early investors** | Return capital to LPs, rebalance |
| **Founders** | Diversification, personal liquidity |

| Stakeholder | Why they buy |
|-------------|--------------|
| **Late-stage VCs** | Access to hot deals they missed |
| **Institutions** | Pre-IPO positioning |
| **Family offices** | Direct exposure without fund fees |

---

## Transaction types

### 1. Direct secondary

Employee or early investor sells directly to buyer. Often brokered by platforms.

```
Employee → [Forge/EquityZen] → Buyer
```

### 2. Tender offer

Company-organized liquidity event. Usually at set price.

| Feature | Detail |
|---------|--------|
| Pricing | Company sets (often last round) |
| Volume | Pro-rata if oversubscribed |
| Approval | Company controls who buys |
| Frequency | Typically annual or at funding rounds |

**Example:** OpenAI tender offers let employees sell at round valuations.

### 3. VC syndication SPV

VC creates SPV to aggregate capital from multiple LPs for a single investment.

```
         ┌─────────────┐
         │  Thrive LP1 │──┐
         └─────────────┘  │
         ┌─────────────┐  │    ┌─────────┐    ┌─────────┐
         │  Thrive LP2 │──┼───▶│   SPV   │───▶│ OpenAI  │
         └─────────────┘  │    └─────────┘    └─────────┘
         ┌─────────────┐  │
         │  Thrive LP3 │──┘
         └─────────────┘
```

**Why SPV not direct?**
- Pool smaller checks into meaningful allocation
- Simplify cap table (one line item vs many)
- VC earns carry on SPV
- LPs get access they couldn't get alone

### 4. Fund secondaries (LP interests)

Selling LP stake in a VC fund, not individual company shares.

| Aspect | Company secondary | Fund secondary |
|--------|-------------------|----------------|
| What's sold | Shares in one company | LP interest in fund |
| Diversification | Single company | Portfolio |
| Pricing | Company-specific | NAV-based |
| Buyers | Institutions, family offices | Secondary funds (Lexington, Ardian) |

---

## Key platforms

| Platform | Focus | Model |
|----------|-------|-------|
| [[Forge Global]] | Secondary marketplace | Broker, ATS |
| **EquityZen** | Curated secondaries | Funds + direct |
| [[Carta]] (CartaX) | Cap table + liquidity | Integrated |
| **[[Nasdaq]] Private Market** | Tender offers | Company-sponsored |
| **Zanbato** | Institutional secondaries | Marketplace |
| [[AngelList]] | Syndicates + funds | SPV platform |

### Forge Global (FRGE)

| Metric | Value |
|--------|-------|
| Public | Yes (NASDAQ: FRGE) |
| Model | Broker + ATS |
| Volume | Billions annually |
| Focus | Pre-IPO secondaries |

### AngelList

| Metric | Value |
|--------|-------|
| Model | SPV-as-a-service |
| Users | Angels, small funds |
| Fee | ~$8K setup + carry |
| Innovation | Pioneered rolling funds |

---

## VC syndication SPVs

How VCs like [[Thrive Capital]] give LPs access to hot deals:

### Structure

| Component | Detail |
|-----------|--------|
| Vehicle | Delaware LLC (typically) |
| Manager | VC firm (Thrive, [[a16z]], etc.) |
| Investors | Existing LPs, strategic partners |
| Fees | 0-2% management + 20% carry |
| Minimum | $100K-$1M typically |
| Term | Matches underlying investment |

### Why VCs use SPVs

| Reason | Benefit |
|--------|---------|
| **Allocation overflow** | Round oversubscribed, SPV absorbs excess demand |
| **LP relationships** | Give top LPs access to best deals |
| **Economics** | Earn carry on SPV capital |
| **Cap table** | One entity vs. many individuals |
| **Speed** | Pre-organized capital deploys fast |

### Example: Thrive + OpenAI

[[Thrive Capital]] led OpenAI's $6.6B round. Likely structure:

- Thrive main fund: $X direct
- Thrive SPV: $Y from LPs wanting more exposure
- Total Thrive-affiliated: $1B+

SPV LPs get OpenAI exposure; Thrive earns carry on both.

---

## Pricing dynamics

### Discounts and premiums

| Scenario | Typical pricing |
|----------|-----------------|
| **Hot company, limited supply** | Premium to last round (10-30%) |
| **Distressed seller** | Discount (10-30%) |
| **Near IPO** | Premium (IPO pop anticipation) |
| **Stale round** | Discount (round was 12+ months ago) |
| **ROFR risk** | Discount (company may block) |

### AI company secondary pricing (Jan 2026)

| Company | Last round | Secondary pricing |
|---------|------------|-------------------|
| [[OpenAI]] | $157B (Oct 2024) | Premium — trading ~$250-300B implied |
| [[Anthropic]] | $60B | Premium — strong demand |
| [[SpaceX]] | ~$350B | Premium — perennial demand |
| [[Stripe]] | $50B (2023) | Discount — stale round |

### Price discovery challenges

- No public quotes
- Thin trading
- Information asymmetry
- Company approval required (ROFR)
- Varying share classes

---

## Right of First Refusal (ROFR)

Most private companies have ROFR on secondary sales:

| Stage | What happens |
|-------|--------------|
| 1 | Seller finds buyer, agrees on price |
| 2 | Seller notifies company |
| 3 | Company has 30 days to match or waive |
| 4 | If matched, company (or designee) buys |
| 5 | If waived, original buyer proceeds |

**Impact:** Companies can block sales to competitors, journalists, or just exercise to consolidate cap table.

**OpenAI:** Known to exercise ROFR frequently, controlling who owns shares.

---

## Employee considerations

### Why employees sell

| Reason | Detail |
|--------|--------|
| **Concentration** | 80%+ net worth in one stock |
| **Taxes** | Need cash for AMT on ISOs |
| **Life events** | House, divorce, illness |
| **Uncertainty** | [[Bird]] in hand vs. IPO timing |

### Typical restrictions

| Restriction | Detail |
|-------------|--------|
| **Lockup** | Can't sell for 6-12 months post-grant |
| **ROFR** | Company approval required |
| **Volume limits** | Max % of holdings per year |
| **Blackout periods** | No sales around funding rounds |
| **Buyer approval** | Company vets buyers |

---

## Investment implications

### For buyers

**Pros:**
- Pre-IPO access to best companies
- Potentially discounted entry
- Direct ownership (vs. fund exposure)

**Cons:**
- Illiquid
- Information disadvantage
- ROFR risk
- No voting rights (often)
- Unknown IPO timing

### For platforms

| Company | Thesis |
|---------|--------|
| [[Forge Global]] | Volume grows as companies stay private longer |
| [[Carta]] | Cap table integration → liquidity capture |

### For AI specifically

Secondary markets are how non-VCs access AI winners:
- [[OpenAI]] — not taking new investors at will
- [[Anthropic]] — rounds heavily oversubscribed
- Secondaries = only access point for many

---

## For theses

- [[Private markets]] — broader context
- [[Tokenized private shares]] — retail alternative (derivative)

---

*Created 2026-01-26*

## Related

- [[Private markets]] — broader context
- [[Tokenized private shares]] — retail derivative alternative
- [[SPV financing]] — generic SPV structure
- [[Forge Global]] — secondary platform (FRGE)
- [[Carta]] — cap table + CartaX
- [[AngelList]] — SPV platform
- [[Thrive Capital]] — SPV syndicator (OpenAI)
- [[OpenAI]] — most active AI secondary market
- [[Anthropic]] — secondary demand
