---
aliases: [TLH, tax loss harvesting, tax-loss selling, loss harvesting]
tags: [concept, tax, portfolio-management, wealth-management]
---

**Tax-loss harvesting** — selling securities at a loss to offset realized capital gains, reducing tax liability while maintaining portfolio exposure by replacing sold positions with correlated substitutes. Once a manual end-of-year exercise for advisors, TLH has been automated by robo-advisors and [[Direct indexing|direct indexing]] platforms into a continuous, algorithmic process that generates 1-2% annualized after-tax alpha for taxable accounts. The practice is now the primary selling point for [[Separately Managed Accounts]] and the main reason direct indexing assets are growing at 12%+ CAGR.

---

## The story

The logic is straightforward. If you hold a stock that's declined below your purchase price, selling it crystallizes a capital loss. That loss offsets realized gains elsewhere in the portfolio — or from other sources (real estate sales, exercised options, business income). If losses exceed gains in a given year, up to $3,000 can offset ordinary income, with the remainder carried forward indefinitely. The government effectively co-finances your losses today in exchange for a lower cost basis (and therefore higher future gains) on replacement positions. It's a tax deferral, not a tax elimination — but the time value of the deferred tax payment, compounded over decades, is real money.

The value of each harvested dollar depends on what it offsets. Short-term capital gains are taxed as ordinary income — up to 37% federal for the top bracket. Long-term gains (held >1 year) are taxed at a maximum 20%. On top of both, the 3.8% Net Investment Income Tax (NIIT) applies to investment income above $200K (single) / $250K (married filing jointly). A harvested loss offsetting short-term gains saves 40.8 cents per dollar at the top federal rate; offsetting long-term gains saves 23.8 cents. State taxes amplify the gap further: [[California]] at 13.3% (no preferential long-term rate) pushes the combined short-term rate above 54%, while [[Texas]] and [[Florida]] add nothing. The alpha estimates that providers publish are almost always federal-only — actual after-tax value varies enormously by state of residence.

The practice is as old as the tax code. Wealthy investors have always sold losers in December. What changed is frequency and granularity. Before technology made it feasible, an advisor might scan a portfolio quarterly, identify a few losing positions, sell them, and wait 31 days before buying back. The operational cost — commissions, spread costs, tracking periods — limited TLH to large accounts with dedicated advisors.

[[Wealthfront]] and [[Betterment]] changed the economics starting around 2012-2013. By automating TLH across their entire AUM, they turned a bespoke wealth-management service into a mass-market feature available at $500 minimums. The algorithm runs daily: scan every position, identify lots with unrealized losses exceeding a threshold (typically the transaction cost), sell, immediately buy a correlated substitute to maintain exposure, track the 30-day wash sale window, and swap back when permitted. Wealthfront's published data shows their TLH algorithm harvesting losses on average 10-12 times per year per account — something no human advisor would attempt.

Direct indexing took this to its logical endpoint. Instead of holding an [[S&P 500]] [[ETF]] (one security, one cost basis), you hold the ~500 individual component stocks. On any given day, dozens of positions are underwater even in a rising market. Each can be harvested independently while substituting a correlated stock to maintain sector and factor exposure. The granularity is transformative: a 500-position portfolio has 500 independent harvesting opportunities versus one for the equivalent ETF. [[Parametric]] (owned by [[Morgan Stanley]], the largest direct indexing manager at ~$400B+), [[Aperio]] (acquired by [[BlackRock]] in 2021), and [[Fidelity]] (FidFolios, $5K minimum with fractional shares) all built their direct indexing platforms around TLH as the core value proposition.

The substitution step introduces a cost the providers rarely emphasize: tracking error. Selling Pepsi and buying Coca-Cola maintains consumer staples exposure, but the two stocks are not identical — different revenue mixes, margin profiles, dividend yields, factor loadings. Across hundreds of substitutions per year, these mismatches accumulate into measurable performance drag versus a pure index hold. Studies estimate 0.2-0.5% annualized tracking error for well-managed direct indexing portfolios, eating into the 1-2% tax alpha. The net benefit is real but narrower than the headline figures suggest, and the tracking error is permanent while the tax alpha decays.

The tax alpha estimates vary, but the direction is consistent. Academic studies (most cite Arnott, Berkin & Ye's work) estimate 1-2% annualized benefit for a top-bracket investor in the early years of a new portfolio. [[Vanguard]]'s 2023 research suggests 0.73-1.09% per year. [[Wealthfront]] publishes ~2% for its highest-bracket clients. [[Charles Schwab]]'s Personalized Indexing claims 1-1.5%. The variance depends on market volatility (more volatility = more harvesting opportunities), portfolio turnover, tax bracket, and — critically — time horizon.

This time dimension is where the honest complexity lives. TLH is a deferral mechanism, not a free lunch. Every harvested loss resets the cost basis of the replacement security lower. When the replacement is eventually sold (or the investor dies — at which point the step-up in basis at death eliminates deferred gains entirely), the deferred tax comes due. In the early years of a portfolio, TLH generates substantial alpha because there are many "virgin" losses to harvest. Over time, as cost bases ratchet down across the portfolio, fewer positions sit below their purchase price, and the harvesting opportunities diminish. Parametric's own research shows tax alpha decaying from ~1.5% in year 1 to ~0.5% by year 10 for a stable portfolio. The strategy works best for new money, high-volatility periods, and portfolios with regular contributions (new money = new cost bases = fresh harvesting opportunities).

The constraint that shapes the entire practice is the wash sale rule. [[IRS]] Section 1091 disallows a loss deduction if a "substantially identical" security is purchased within 30 days before or after the sale. The rule is clear for identical securities: sell AAPL, buy AAPL within 30 days, and the loss is disallowed (it gets added to the replacement's cost basis instead). But "substantially identical" has never been precisely defined by the IRS for non-identical securities. Is selling the [[Vanguard]] S&P 500 ETF (VOO) and buying the [[iShares]] S&P 500 ETF (IVV) a wash sale? They track the same index. The IRS has offered no formal guidance. Industry practice is aggressive: ETFs from different providers tracking the same index are treated as not substantially identical, and individual stock substitutions (selling Pepsi, buying Coca-Cola) are clearly permitted. The ambiguity has never been tested in court.

The wash sale rule also creates a coordination nightmare for investors with multiple accounts. A loss harvested in a taxable SMA is disallowed if the same security is purchased within 30 days in the investor's IRA, 401(k), spouse's accounts, or other brokerage accounts. Most direct indexing platforms can't see the investor's other accounts, creating a real risk of inadvertent wash sales. The operational burden of cross-account coordination — which the SMA manager must handle — is a genuine cost that rarely appears in marketing materials.

Crypto occupied a TLH loophole until recently. The wash sale rule historically applied only to "securities" and "stock" — digital assets weren't classified as either. Crypto investors could sell at a loss and immediately repurchase the same token, harvesting the loss without waiting 30 days. The Inflation Reduction Act of 2022 and subsequent IRS guidance closed this by treating digital assets as subject to wash sale rules starting in 2025, though enforcement mechanics remain uncertain.

At scale, TLH creates a visible market footprint. Automated algorithms managing trillions in AUM all run the same logic: sell losers, buy substitutes. The selling concentrates in December (year-end optimization) and during sharp drawdowns (the most productive harvesting windows). This crowding depresses prices on recent losers beyond what fundamentals justify and creates the January effect — one of the oldest documented anomalies in equity markets. Small-cap stocks, which are disproportionately represented among the losers being harvested (lower liquidity, higher volatility, more individual-investor ownership), snap back in January as TLH selling pressure abates. The anomaly has been documented since the 1940s but persists, partly because the tax incentive that creates it is structural. The [[Sector rotation]] note tracks how tax-loss selling in January 2026 accelerated rotation out of AI/Mag 7 into small-caps.

For most taxable investors above ~$100K, the question isn't whether TLH works — the math is clear. The question is whether the after-tax alpha (decaying over time) exceeds the all-in cost of the vehicle delivering it: SMA management fees (0.20-0.50%), advisory fees, the operational burden of wash sale coordination, and the complexity of tax reporting (a 500-position direct indexing portfolio generates hundreds of realized transactions per year). For high-bracket investors with new taxable money, the answer is usually yes. For long-held portfolios with deeply embedded gains, the marginal benefit shrinks considerably.

---

## Reference

### Tax alpha estimates

| Source | Estimated annual alpha | Notes |
|--------|----------------------|-------|
| Arnott, Berkin & Ye (academic) | 1-2% | Top bracket, new portfolio, high volatility |
| [[Vanguard]] (2023) | 0.73-1.09% | Depends on turnover and volatility |
| [[Wealthfront]] (published) | ~2% | Highest bracket clients |
| [[Charles Schwab]] | 1-1.5% | Personalized Indexing product |
| [[Parametric]] (internal) | ~1.5% yr 1, ~0.5% yr 10 | Decay curve on stable portfolios |
| Tracking error drag | -0.2% to -0.5% | Substitution cost, offsets gross alpha |

### Effective tax rates on harvested losses (top bracket, 2025)

| Gain type offset | Federal rate | NIIT | Combined federal | With CA (13.3%) | With TX/FL (0%) |
|-----------------|-------------|------|-----------------|----------------|----------------|
| Short-term | 37% | 3.8% | 40.8% | 54.1% | 40.8% |
| Long-term | 20% | 3.8% | 23.8% | 37.1% | 23.8% |
| Ordinary income ($3K limit) | 37% | — | 37% | 50.3% | 37% |

### Key rules

| Rule | Detail |
|------|--------|
| Wash sale window | 30 days before or after the sale |
| "Substantially identical" | Same security = clear; same-index ETFs from different providers = industry treats as non-identical (untested) |
| Loss carryforward | Losses exceeding gains: $3,000 offsets ordinary income per year, remainder carries forward indefinitely |
| Step-up at death | Unrealized gains eliminated at death via cost basis step-up — makes TLH deferral permanent if investor dies before selling |
| Cross-account scope | Applies across all accounts of the taxpayer and spouse: taxable, IRA, 401(k), other brokerage |
| Crypto | Subject to wash sale rules starting 2025 (previously exempt) |

### Harvesting mechanics

1. Identify lots with unrealized losses exceeding transaction cost threshold
2. Sell the losing lot
3. Immediately purchase a correlated but not "substantially identical" substitute (e.g., sell PEP → buy KO; sell VOO → buy IVV)
4. Maintain sector/factor exposure — portfolio drift must stay within tracking error tolerance
5. Track the 31-day window; swap back to original if preferred after window expires
6. Coordinate across all investor accounts to avoid wash sale disallowance

### Direct indexing providers

| Provider | Parent | AUM | Minimum | Fee |
|----------|--------|-----|---------|-----|
| [[Parametric]] | [[Morgan Stanley]] | ~$400B+ | Varies | Institutional |
| [[Aperio]] | [[BlackRock]] | — | — | Institutional |
| Schwab Personalized Indexing | [[Charles Schwab]] | — | — | 0.40% (0.35% >$2M) |
| FidFolios | [[Fidelity]] | — | $5K | — |
| Personalized Indexing | [[Vanguard]] | — | — | — |
| [[Wealthfront]] | — | $80B+ (total) | $500 | 0.25% |
| [[Betterment]] | — | — | $0 | 0.25% |

---

## Related

- [[Separately Managed Accounts]] — primary vehicle for personalized TLH
- [[Direct indexing]] — automated TLH at individual stock level
- [[ETF]] — alternative structure (fund-level TLH only)
- [[Wealthfront]] — pioneer of automated mass-market TLH
- [[Betterment]] — early robo-advisor TLH provider
- [[Parametric]] — largest direct indexing manager
- [[Charles Schwab]] — Schwab Personalized Indexing
- [[Fidelity]] — FidFolios ($5K minimum)
- [[Sector rotation]] — references tax-loss selling as rotation catalyst
