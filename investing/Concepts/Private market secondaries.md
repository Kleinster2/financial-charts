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

### AI company secondary pricing (Mar 2026)

| Company | Last round valuation | Secondary pricing | IPO status |
|---------|---------------------|-------------------|------------|
| [[SpaceX]] | $800B (Dec 2025 tender) | Premium — $588/share (Jan 2026 secondary) | IPO targeting $1.75T, summer 2026, raise up to $50B |
| [[OpenAI]] | $840B post-money (Feb 2026) | At/near round — $110B mega-round just closed | Amazon $35B tranche terminates if no IPO by Dec 2028 |
| [[Anthropic]] | $380B (Feb 2026 Series G) | Premium — $30B round at nearly 2x prior | IPO path expected |
| [[Anduril]] | ~$31B (2025) | Premium — SPVs offering at >2x last round | In talks to raise at nearly double last valuation |
| [[Stripe]] | $50B (2023) | Discount — stale round | — |

If SpaceX, OpenAI, and Anthropic achieve IPO valuations ~20% above their most recent private rounds, it would add more than $3 trillion to US equity markets — equivalent to adding another [[Microsoft]]. *(Bloomberg, Mar 11, 2026)*

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

## Pre-IPO SPV boom (2025-2026)

As [[SpaceX]], [[OpenAI]], and [[Anthropic]] approach potential IPOs at trillion-dollar-plus combined valuations, SPV activity has exploded — and so have the risks.

### Market size

| Metric | Value | Source |
|--------|-------|--------|
| SPV investment volume growth | 11x since 2021 | [[Caplight Technologies]] |
| SPV share of quarterly secondary volume | ~50% | Caplight |
| Total SPV investment (2025) | >$1.5B | Caplight |
| Brokered secondary market volume (2025) | $3.5B (Caplight-tracked) | Caplight |

*Caplight estimates they see one-third of the brokered private secondary market's activity — actual volumes likely 3x higher.*

### Fee structures

Close to 40% of SPVs investing in [[SpaceX]] and [[Anduril]] tracked by [[Caplight Technologies]] over the past three years have ongoing fees:

| Fee type | Average |
|----------|---------|
| Management fee | 1.2-1.5% |
| Carried interest | 13-15% |

Example: [[Vida Private Wealth]] pitched [[Anduril]] shares (Feb 2026) at >2x last round price plus 10% carry and 2% management fee. Anduril COO Matt Grimm said the firm wasn't on Anduril's cap table and Anduril had no open investment opportunities at the time.

### Clean SPVs vs layered SPVs

Clean SPV: Investors pool cash to directly invest in a startup. The SPV appears on the company's cap table alongside founders, employees, and vetted backers.

Layered SPV: An investor in an SPV turns around and creates their own SPV on top of it, collecting additional fees and carry. Then others do the same — creating bets on people betting on people betting on the roulette wheel.

| Type | 2025 volume (Caplight) | Notes |
|------|----------------------|-------|
| Clean SPVs | Majority of $3.5B | Direct cap table access |
| Layered SPVs | $227M | Virtually nonexistent two years ago |

As layers accumulate, fees compound and investors can be left with returns far below what the underlying stock delivers. The investor at layer 3 pays carry to their SPV manager, who pays carry to the layer 2 manager, who pays carry to the original SPV — all before anyone earns a return on the stock itself.

### Fraud cases

The gap between insatiable demand and tightly controlled supply has attracted criminal actors. Unlike public markets, SPV managers have no licensing requirement and investors have no easy way to verify that a fund actually holds the shares it claims.

| Case | Alleged fraud | Outcome |
|------|---------------|---------|
| Giovanni Pennetta / Sestante Capital (Manhattan) | Pitched access to [[Anduril]] and other private companies through NextGenTech Investments SPV. Didn't actually hold shares. Misappropriated >$10M to personal accounts | Pleaded guilty to wire fraud (Mar 5, 2026). Agreed to ≤97 months prison, $11.7M restitution, $12.5M forfeiture |
| Brooklyn scheme (3 defendants) | $65M scheme marketing pre-IPO investments falsely claimed to come directly from the companies | Three guilty pleas to securities fraud (Dec 2025) |

Manhattan US Attorney [[Jay Clayton]] (former SEC chairman): *"We look across all markets — public and private, debt and equity, retail and institutional — in our efforts to detect, deter and root out fraud."*

### Regulatory gap

Accredited investors ($200K income or $1M net worth) have fewer protections than retail. Layered SPVs would likely not survive regulatory scrutiny if aimed at retail, but accredited investors are assumed to be sophisticated enough to protect themselves — though many may not realize the structural risks they're taking.

### Issuer pushback: the void-declaration mechanism (May 11-12, 2026)

On May 11, 2026, [[Anthropic]] updated its public help-center notice on unauthorized stock sales — explicitly declaring all transfers not approved by its board of directors **void**, naming individual SPV operators and tokenization venues by name for the first time, and warning specifically against forward contracts and tokenized securities. [[OpenAI]] issued an identical-language notice on May 12. Both notices applied to common AND preferred stock and pointed to Delaware bylaw transfer restrictions as the legal basis.

The two notices together are the cleanest evidence the AI-lab issuer side has taken a coordinated stance against the SPV / perp / tokenized-equity complex that grew up around them through 2025-2026. The structural significance is in the word choice.

#### Void vs voidable — what Delaware corporate law actually does

The legal choice of "void" rather than "voidable" is the most aggressive Delaware stance an issuer can take:

| Designation | What it means | What downstream buyers retain |
|---|---|---|
| **Voidable** | Transfer is initially effective; issuer can later challenge it | Good-faith purchaser defenses, BFP doctrine, equitable estoppel may still apply |
| **Void** | Transfer is never effective in the first place | Most equitable defenses fall away — downstream chain of title is treated as having never existed |

In a voidable regime, a downstream SPV LP who bought "Anthropic exposure" in good faith from a layered intermediary could potentially recover via good-faith purchaser doctrine if the issuer challenges late. In a void regime, the same buyer has no claim — they paid for something that under Delaware bylaws never transferred title. The legal premium between *authorized* and *unauthorized* exposure widens dramatically under the void designation.

This matters operationally because most SPV and tokenized-equity products through 2025 had been structured on the assumption that issuer challenges would be slow, narrow, and discretionary — i.e. operating in a *de facto* voidable world even if bylaws said void. The May 11-12 announcements were the issuers publicly walking up to that assumption and severing it.

#### Anthropic's named blocklist (May 11, 2026)

Anthropic explicitly named eight unauthorized platforms:

- [[Open Door Partners]]
- [[Unicorns Exchange]]
- [[Pachamama Capital]]
- [[Lionheart Ventures]]
- [[Sydecar]]
- [[Upmarket]]
- New offerings on [[Forge Global]] and [[Hiive]]

Two of these — [[Forge Global]] and [[Hiive]] — are board-recognized infrastructure providers for *authorized* secondary transactions; the inclusion was specifically about *new* offerings on those platforms that lacked direct issuer sign-off. [[Forge Global]] disputed its inclusion publicly, stating it requires "explicit approval of the company" before facilitating transactions; [[Sydecar]] emphasized its administrative-only capacity; [[Hiive]] defended its compliance infrastructure. The platform-side response made clear the dispute is real and unresolved — not all named platforms accept that their offerings are unauthorized.

[[OpenAI]] named the same target categories (SPVs, tokenized interests, forward contracts) on May 12 but the source reporting does not enumerate OpenAI's specific named platforms.

#### Implied-valuation gap vs primary rounds

The void announcement landed against a tokenized-secondary backdrop where the implied valuations had decoupled materially from primary-round pricing:

| Venue type | Implied [[Anthropic]] valuation (May 11) | vs Feb $380B primary |
|---|---|---|
| Tokenized perp DEXs ([[Ventuals]], [[PreStocks]]) | ~$1.6T | ~4.2x |
| Off-chain secondary ([[Forge Global]]) | ~$1T | ~2.6x |
| Reported next primary round (TechCrunch, May 12) | ~$900B | ~2.4x |

The gap between the on-chain perp implied valuation ($1.6T) and the off-chain secondary platform price ($1T) within a single asset is the cleanest evidence available that the perp-DEX layer was running on retail FOMO rather than a price-discovery process anchored to real share inventory. The issuer announcement collapsed the legitimacy backstop on both layers simultaneously.

#### Market reaction

| Asset | May 11 / May 12 move | Mechanism |
|---|---|---|
| [[Destiny Tech100]] (DXYZ) | $71.24 close May 11 → $53.40 close May 12 (-25.05%) | Held [[Anthropic]] via single-security SPV (Feb 2026 deployment) — pure exposure to the void mechanism |
| [[OpenAI]] tokenized contracts | ~$1,400 → ~$900 (-36%) in 24h | Direct tokenized-equity exposure to the void announcement |

The DXYZ reaction is structurally important: the fund's [[Anthropic]] position is held via the single-security SPV structure that the Anthropic notice was specifically designed to invalidate (board-approved SPV positions are not voided; unauthorized SPV positions are). DXYZ's drawdown isn't a direct hit on its own position — it's the market repricing the *legitimacy premium* on retail-access vehicles whose structures rely on issuer-side tolerance of secondary plumbing that the issuer just publicly declared illegitimate.

#### Read for the broader market

The void mechanism is unilateral, fast, and operational in a way that prior issuer pushback was not. Earlier 2025-2026 actions (ROFR exercises, employee tender restrictions, blocking specific transactions) were transaction-by-transaction. The May 11-12 announcements declared a category-wide voidance, named platforms publicly, and were duplicated across two of the three trophy AI-lab issuers (Anthropic + OpenAI; [[SpaceX]] has not issued a parallel notice as of May 13). The third trophy issuer is the obvious tail risk for the SPV / tokenization industry — if SpaceX follows, the structural break is complete.

The downstream effect on listed retail-access vehicles ([[Destiny Tech100]], [[Fundrise]] VCX, [[Powerlaw Corp]]) depends on whether their underlying SPV positions are board-approved or unauthorized. Board-approved positions are unaffected; unauthorized positions are now exposed to legal void risk in addition to the existing premium-to-NAV compression risk. The vehicles that disclosed the *mechanism* of their underlying SPV positions (board-approved tender vs unauthorized secondary) will trade with that structural transparency baked in.

*Sources: [Anthropic Help Center — Unauthorized Anthropic Stock Sales and Investment Scams](https://support.claude.com/en/articles/13704655-unauthorized-anthropic-stock-sales-and-investment-scams); [TechCrunch — Anthropic warns investors against secondary platforms offering access to its shares](https://techcrunch.com/2026/05/12/anthropic-warns-investors-against-secondary-platforms-offering-access-to-its-shares/) (May 12, 2026); [Yahoo Finance / Bloomberg — Anthropic and OpenAI warn buyers: unauthorized AI startup shares may be worthless](https://finance.yahoo.com/markets/stocks/articles/anthropic-openai-warn-buyers-unauthorized-180743368.html); [Spendnode — Anthropic Voids Unauthorized Stock Trades as Tokens Imply $1.6T](https://www.spendnode.io/blog/anthropic-voids-unauthorized-stock-trades-1-6t-tokenized-may-2026/); local prices_long DXYZ verification May 1-12 2026.*

[[Lead Edge]] partner Zach Ullman: *"A lot of people think they own stock in SpaceX. I'm not sure what the actual percentage of people who do actually own that, at the end of the day, is."*

[[Torch Capital]] founder Jonathan Keidan on late-stage buying: *"It's the tail-end of traders who are just trying to capture that last piece of opportunity."* Hard to make the case that buying SpaceX private shares at this late stage delivers a 5x return.

[[Mayer Brown]] partner Anna Pinedo expects "many disgruntled people" given the proliferation of vehicles with esoteric, bespoke structures that are hard to generalize.

[[Caplight Technologies]] CEO Javier Avalos: *"We've been seeing a lot of cowboy-esque type of behavior where these groups are trying to build a track record."*

Anduril COO Matt Grimm on what happens when SPV promises meet an actual IPO liquidity event: *"It'll be really crippling for folks who had retirements planned, paying off their house, putting their kids through college based on the SpaceX IPO, and the returns come back either half what they thought they did or they never owned it at all."*

*Source: Bloomberg (Bailey Lipschultz), Mar 11, 2026*

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
- [[SPV financing]] — generic SPV structure (corporate debt isolation)
- [[Forge Global]] — secondary platform (FRGE)
- [[Carta]] — cap table + CartaX
- [[AngelList]] — SPV platform
- [[Caplight Technologies]] — private secondary market data provider, tracks SPV volume
- [[Thrive Capital]] — SPV syndicator (OpenAI)
- [[Lead Edge]] — growth firm, SPV/secondary buyer
- [[Torch Capital]] — early-stage VC, direct cap-table co-investments
- [[SpaceX]] — largest pre-IPO secondary market; IPO targeting $1.75T (summer 2026)
- [[OpenAI]] — $840B post-money, most active AI secondary market
- [[Anthropic]] — $380B, secondary demand
- [[Anduril]] — defense tech, heavy SPV activity despite no open investment opportunities
- [[Private Market Access]] — listed vehicles packaging secondaries for retail
