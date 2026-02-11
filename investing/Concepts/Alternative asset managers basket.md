---
aliases: [ALTM, Alt managers basket, Private credit basket]
tags: [basket/internal, ai, disruption, alt-managers]
---

# Alternative asset managers basket

Alternative asset manager stocks that sold off heavily during the [[Claude Cowork disruption February 2026|SaaSpocalypse]] Wave 1 (Feb 3-5) despite not being intermediaries. The market initially treated them as part of the "AI replaces financial services" trade — indiscriminate selling before sorting intermediaries from asset owners.

They bounced back ~50% of the drop by Feb 10 as the market distinguished originators/asset owners from advisory middlemen. Tracked as a control group against [[AI financial disintermediation basket|AIFD]] (stayed down) and [[AI workflow disruption basket|AIWD]] (stayed down worse).

---

## Constituents

Move-weighted from Feb 2-5 Wave 1 selloff. Bigger drop = higher weight.

| Ticker | Company | Weight | Feb 2-5 move |
|--------|---------|--------|--------------|
| ARES | [[Ares Management]] | 27% | -16.8% |
| KKR | [[KKR]] | 21% | -13.3% |
| OWL | [[Blue Owl]] | 21% | -13.3% |
| BX | [[Blackstone]] | 16% | -10.2% |
| APO | [[Apollo]] | 8% | -5.3% |
| BAM | [[Brookfield]] | 7% | -4.1% |

Total: 100% — 6 constituents, move-weighted

### Why track this?

These firms originate and hold assets (direct lending, PE, real estate, infrastructure). There's no advisory layer for AI to disintermediate — they're capital allocators, not distributors. But the Feb 3-5 selloff proves the market can lump them in with genuine intermediaries during panic. If another AI catalyst hits financial services, ALTM will likely sell off again before recovering.

### Excluded

| Ticker | Company | Why excluded |
|--------|---------|-------------|
| MS | [[Morgan Stanley]] | Diversified bank — wealth management diluted by IB/trading (-2.4% on Feb 10 vs pure-plays at -7 to -9%) |
| GS | [[Goldman Sachs]] | Same — alt management is one division among many |
| CG | [[Carlyle]] | Insufficient price data for weighting period |

### Database tickers

```
ARES, KKR, OWL, BX, APO, BAM
```

---

## Index methodology

- Ticker: ALTM
- Weighting: Move-weighted (Feb 2-5 selloff magnitude = weight)
- Base date: Feb 2, 2026 = 100 (last trading day before Wave 1)
- History: July 2021 – present
- Calculation: Price return
- Script: `scripts/create_altm_index.py --store`

---

## Behaviour pattern

| Period | ALTM | AIFD | AIWD | SPY |
|--------|------|------|------|-----|
| Wave 1 (Feb 2-5) | -12.5% | ~flat | -18% | -2.6% |
| Wave 2-3 (Feb 9-10) | ~flat | -8% | continued decline | -1% |
| Net (Feb 2-10) | -7% | -8% | -20%+ | -3% |

Pattern: ALTM sells off with the first wave (beta + confusion), then recovers as market sorts real intermediation targets from asset owners. AIWD and AIFD stay down because those are thesis hits, not beta hits.

---

## Tracking thesis

This basket tests:
1. Contagion risk — do alt managers get dragged into future AI disruption selloffs?
2. Recovery speed — how quickly does the market sort originators from intermediaries?
3. Convergence risk — if AI starts replacing capital allocation (not just advisory), ALTM becomes a real target, not just collateral damage

Watch for:
- AI tools entering direct lending, underwriting, deal sourcing
- Alt manager earnings mentioning AI fee pressure
- Correlation between ALTM and AIFD on future AI catalysts — if it stays high, the market isn't differentiating

---

## Related

- [[AI financial disintermediation basket]] — the real intermediation targets
- [[AI workflow disruption basket]] — software/data targets
- [[AI disintermediation]] — thesis driving all three baskets
- [[PE software talent drain]] — the deeper reason ALTM sold off: PE portfolio software risk
- [[Alternative asset manager]] — concept note
- [[Alternative Managers]] — sector note
- [[Claude Cowork disruption February 2026]] — Wave 1 catalyst that hit ALTM
- [[Ares Management]] — highest-weight constituent
- [[KKR]] — second-highest weight
- [[Blackstone]] — largest AUM constituent

*Created 2026-02-11*
