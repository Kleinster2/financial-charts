---
aliases: [credit ratings, rating agencies, fallen angel, rising star, investment grade, junk bond, speculative grade]
tags: [concept]
---

**Credit rating mechanics** — how [[S&P Global]], [[Moody's]], and [[Fitch Ratings|Fitch]] assign, signal, and change corporate credit ratings, and the market consequences that follow.

---

## The scale

| Quality | S&P | Moody's | Fitch |
|---------|-----|---------|-------|
| Highest | AAA | Aaa | AAA |
| High | AA+ / AA / AA- | Aa1 / Aa2 / Aa3 | AA+ / AA / AA- |
| Upper medium | A+ / A / A- | A1 / A2 / A3 | A+ / A / A- |
| Lower medium | BBB+ / BBB / BBB- | Baa1 / Baa2 / Baa3 | BBB+ / BBB / BBB- |
| *IG / HY boundary* | | | |
| Speculative | BB+ / BB / BB- | Ba1 / Ba2 / Ba3 | BB+ / BB / BB- |
| Highly speculative | B+ / B / B- | B1 / B2 / B3 | B+ / B / B- |
| Substantial risk | CCC+ / CCC / CCC- | Caa1 / Caa2 / Caa3 | CCC+ / CCC / CCC- |
| Near default | CC / C | Ca / C | CC / C |
| Default | D / SD | — (uses Ca/C) | D / RD |

S&P and Fitch use +/- modifiers. Moody's uses 1/2/3 (1 = top of band, 3 = bottom). S&P uses SD (selective default); Fitch uses RD (restricted default). Moody's has no explicit D rating — defaults sit at Ca/C.

Market share: [[S&P Global]] ~50%, [[Moody's]] ~32%, [[Fitch Ratings|Fitch]] ~15%. The three control ~95% of global ratings.

---

## The IG/HY boundary

The line falls at BBB- / Baa3 — identical credit quality across all three agencies. Below that is speculative grade ("junk" or "high yield").

This boundary is hardcoded into:
- Regulatory frameworks (Basel bank capital requirements treat IG and HY differently)
- Insurance and pension fund mandates (many restricted to IG only)
- Index methodology (Bloomberg IG Corporate Bond Index, ICE BofA indices)
- Central bank collateral eligibility (Fed and ECB repo programs use rating thresholds)

The BBB corridor (BBB+ through BBB-) has grown from ~33% of the IG market in 2007 to ~50% by the mid-2020s. This concentration makes the boundary a systemic concern — even a modest recession-driven downgrade cycle could push hundreds of billions across the line.

---

## Outlook → watch → action pipeline

Rating changes follow a signaling sequence, though agencies can skip steps on sudden events.

### Outlooks

Express the agency's view of likely direction over 12-24 months:

| Outlook | Meaning | Historical conversion rate |
|---------|---------|--------------------------|
| Stable | No change expected | — |
| Positive | Upgrade possible | ~25% within 12 months; ~35% within 24 months |
| Negative | Downgrade possible | ~33% within 12 months; ~45% within 24 months |
| Developing | Could go either way | Assigned during M&A, restructurings |

Negative outlooks convert at higher rates than positive — agencies are more likely to follow through on deterioration warnings.

### CreditWatch / Rating Watch / Review

More urgent than an outlook change. Signals a rating action is likely within 90 days.

| Agency | Term | Typical resolution |
|--------|------|-------------------|
| [[S&P Global]] | CreditWatch (Positive/Negative/Developing) | ~90 days |
| [[Fitch Ratings]] | Rating Watch (Positive/Negative/Evolving) | ~90 days, up to 6 months |
| [[Moody's]] | Review for Upgrade/Downgrade/Direction Uncertain | ~90 days |

CreditWatch Negative converts to actual downgrade ~65-75% of the time — far higher than a negative outlook.

### The sequence

1. Outlook change (e.g., Stable → Negative) — early warning, 12-24 month horizon
2. CreditWatch/Review placement — near-term warning, ~90 days
3. Rating action — actual upgrade or downgrade

Agencies can skip directly to a multi-notch downgrade on sudden events (fraud, covenant breach, sovereign crisis) without prior signals.

---

## What triggers rating actions

Agencies publish sector-specific criteria. The most commonly cited metrics:

### Leverage

| Metric | Typical IG range | HY warning zone |
|--------|-----------------|-----------------|
| Total Debt / EBITDA | 2.5-3.5x (BBB industrial) | >4x sustained |
| FFO / Total Debt | >20% | <12-15% |
| LTV (holding companies, REITs) | <40% | >55-60% |

### Coverage

| Metric | Typical IG minimum | HY territory |
|--------|-------------------|--------------|
| EBITDA / Interest Expense | 4x+ (solid BBB) | <3x concerning; <2x deep HY |
| (FFO - Capex) / Debt | Positive, sustainable | Persistently negative |

### Qualitative factors

- Business profile: market position, diversification, competitive advantage
- Management and governance: financial policy track record, leverage targets
- Sovereign ceiling: corporate ratings rarely exceed the sovereign (exceptions for diversified multinationals)
- Event risk: M&A, LBOs, activism, litigation

When a company publicly commits to a leverage target (e.g., "below 3x net debt/EBITDA") and then does a debt-funded acquisition pushing to 4.5x, that breach of stated financial policy accelerates agency response.

---

## Consequences of downgrades

### Borrowing costs

| Move | Typical spread impact |
|------|----------------------|
| One-notch downgrade within IG (e.g., A → A-) | +10-25 bps |
| Negative outlook change (no rating move) | +5-15 bps |
| IG → HY crossing (BBB- → BB+) | +150-300+ bps |

### Covenant triggers

- Pricing grids: bank credit facility rates step up on downgrades (typically +12.5-25 bps per notch)
- Collateral posting: derivatives agreements may require additional collateral below a threshold (the mechanism that destroyed [[AIG]] in 2008 — $14.5B collateral call triggered the $182B Fed bailout)
- Change-of-control puts: some indentures let bondholders put bonds at par if rating drops below IG combined with a control event
- Acceleration: rare but exists — some agreements allow lenders to demand immediate repayment

### CDS spreads

CDS markets price credit risk continuously and often move before the rating action — by the time the agency acts, 50-70% of the widening may already have occurred. But the actual downgrade triggers a further leg from mechanical effects (forced selling, index exclusion).

| Rating tier | Typical CDS spread range |
|-------------|------------------------|
| IG name | 50-80 bps |
| Same name after crossing to HY | 200-400 bps |

---

## Fallen angels

A fallen angel is an issuer downgraded from investment grade to speculative grade.

### The mechanical cascade

1. Rating action — agency cuts below BBB-/Baa3
2. Index removal — bonds exit IG indices at next monthly rebalancing
3. Forced selling — IG-only mandates (insurers, pensions, many mutual funds, central bank reserve managers) must sell regardless of price
4. Price dislocation — bonds can trade 10-20+ points below par during the transition
5. HY index inclusion — bonds enter HY indices; HY and crossover funds begin buying
6. Recovery — fallen angel bonds historically recover within 3-12 months and outperform original-issue HY

### Scale

- Near-zero in benign years; $200B+ globally in 2020 (COVID — [[Ford]], [[Occidental Petroleum]], Kraft Heinz, Marks & Spencer, Renault)
- The 2020 wave prompted the Fed to expand its Secondary Market Corporate Credit Facility to include recently fallen angels — a first — to prevent mechanical selling from creating a systemic feedback loop

### Dedicated strategies

- VanEck Fallen Angel High Yield Bond ETF (ANGL) and similar funds buy the dislocation, hold for recovery
- Historically above-average risk-adjusted returns within HY — the selling is forced/mechanical, not fundamental

---

## Rising stars

The reverse: an HY issuer upgraded to IG.

### Mechanics

1. Deleveraging or business improvement drives the upgrade
2. Bonds enter IG indices — new buyer base opens (IG-only mandates)
3. Spread compression of 100-200+ bps as the much larger IG investor pool accumulates
4. Markets front-run: BB+ credits with positive outlook often trade at spreads tighter than typical BB+ — active managers take "crossover" positions anticipating the upgrade

---

## Split ratings

Agencies frequently disagree by one or more notches.

### Index rules

| Index family | Rule |
|-------------|------|
| Bloomberg indices | Middle rating of three; lower of two; sole rating if only one |
| ICE BofA indices | Similar middle-rating approach for most families |

Example: S&P BBB-, Moody's Ba1, Fitch BBB- → middle is BBB- → stays in IG index. One more downgrade from either S&P or Fitch flips the middle to HY.

### Regulatory treatment

- Basel (bank capital): standardized approach uses second-best of available ratings
- NAIC (US insurance): lower of the top two ratings determines capital charges

Issuers at the boundary may maintain ratings from only two agencies, dropping the harsher one. This "ratings shopping" is a known dynamic.

---

## Notching

Rating differences between parent and subsidiary, or between debt classes.

### Structural subordination

Holding company senior unsecured debt is typically 1-2 notches below the operating subsidiary. HoldCo creditors have claims on equity stakes in subsidiaries; OpCo creditors have direct claims on operating assets.

Gap widens (2-3 notches) when the holding company carries significant HoldCo-level debt or operates in a regulated industry where the regulator may ring-fence subsidiary assets.

### Debt-level notching within an issuer

| Debt class | Typical notching vs issuer rating |
|-----------|----------------------------------|
| Senior secured | +1 to +2 notches |
| Senior unsecured | Equal to issuer rating |
| Subordinated | -1 to -2 notches |
| Preferred / hybrid | -2 to -3 notches (IG issuers) |

---

## Historical examples

### [[Ford]] — fallen angel and rising star

~$35B in bonds reclassified to HY in March 2020 — largest fallen angel in corporate bond history at the time. All three agencies cut to BB+/Ba2. Regained IG in 2023-2024 ([[Fitch Ratings|Fitch]] and [[S&P Global]] to BBB- in Nov 2023; [[Moody's]] to Baa3 in 2024). Bonds compressed significantly as rising-star flows materialized.

### [[GE]] — multi-year slide from AAA

Held AAA for decades. Lost it in 2009 (GE Capital exposure), then slid: A+ (2015) → A (2017) → BBB+ (Oct 2018, S&P 3-notch cut). CDS traded at BB-equivalent levels. Never actually fell to HY — divested BioPharma to [[Danaher]] ($21.4B), reduced leverage, ultimately broke into three companies ([[GE Vernova]], GE Aerospace, GE HealthCare). Textbook BBB cliff risk.

### [[AT&T]] — peak BBB corridor concern

Net debt peaked ~$180B after [[Time Warner]] acquisition ($85B, 2018). Debt/EBITDA 3.0-3.5x — within IG parameters but with little headroom. Largest non-financial corporate borrower in the world. A hypothetical downgrade would have been the largest fallen angel ever, with systemic implications for HY index capacity. Spun off WarnerMedia (merged with Discovery, 2022) to deleverage.

### [[AIG]] — the collateral trigger cascade (2008)

CDS portfolio had collateral posting tied to credit rating. Multi-notch downgrade in September 2008 triggered ~$14.5B collateral call AIG could not meet. Led to $85B Fed bailout (later $182B). Textbook example of rating-contingent covenants creating a liquidity death spiral.

### [[Occidental Petroleum]] — COVID fallen angel

BBB-/Baa3 going into 2020, already stretched after $38B Anadarko acquisition (2019). Oil price crash triggered downgrades to HY. Recovered on oil rebound and [[Berkshire Hathaway]] equity/preferred investment.

---

## Default rates by rating

Cumulative 5-year default rates (approximate, from agency transition studies):

| Rating tier | 5-year cumulative default |
|-------------|--------------------------|
| AAA | ~0% |
| AA | ~0.1% |
| A | ~0.3% |
| BBB | 0.5-1% |
| BB | 5-8% |
| B | 15-25% |
| CCC/C | 40-50%+ |

The IG/HY boundary is genuinely meaningful — not an arbitrary line. Default probability rises exponentially below it.

---

## Agency business model

All three are paid by the issuer, not by investors. This conflict of interest was central to the 2008 crisis (agencies maintained IG ratings on structured products that were functionally worthless). Dodd-Frank (2010) imposed additional SEC oversight but the issuer-pays model persists. Investor-pays agencies (Egan-Jones) exist but have negligible market share.

---

## Quick stats

| Metric | Value |
|--------|-------|
| Agencies | [[S&P Global]], [[Moody's]], [[Fitch Ratings]] (~95% market share) |
| IG/HY boundary | BBB- / Baa3 |
| BBB share of IG market | ~50% (up from ~33% in 2007) |
| Outlook → downgrade conversion | ~33% within 12 months |
| CreditWatch → downgrade conversion | ~65-75% |
| IG → HY spread impact | +150-300+ bps |

---

## Related

- [[S&P Global]] — largest rating agency (~50% share)
- [[Moody's]] — second largest (~32% share)
- [[Fitch Ratings]] — third largest (~15% share)
- [[Credit spreads]] — market pricing of credit risk
- [[Credit markets]] — broader credit market context
- [[SoftBank]] — BB+ negative outlook, LTV-driven downgrade risk
- [[Oracle]] — BBB/Baa2 negative outlook, AI capex leverage
- [[Ford]] — fallen angel (2020) → rising star (2023-24)
- [[GE]] — multi-year slide from AAA, never fell to HY
- [[AT&T]] — peak BBB corridor concern, delevered via spinoff
- [[AIG]] — collateral trigger cascade (2008)
- [[Occidental Petroleum]] — COVID fallen angel
- [[Amazon bonds]] — AA-/A1, IG reference point
- [[Apple bonds]] — Aaa, highest-rated tech issuer

*Created 2026-03-31*
