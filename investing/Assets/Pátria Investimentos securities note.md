---
aliases:
  - PAX securities
  - Patria securities note
tags:
  - asset
  - securities
  - equity
  - brazil
  - public
---

#asset #securities #equity #brazil #public

Securities companion to [[Pátria Investimentos]] — price history, peer-relative performance and correlation structure for NASDAQ: PAX. See the actor note for the business, financials and full cluster validation.

## Instrument

| Field | Value |
|-------|-------|
| Listing | NASDAQ: PAX (Class A common shares) |
| Structure | Dual-class — Class A (public, one vote) and Class B (founders/partners, super-voting) |
| Currency | USD (firm reports in USD; underlying exposure is largely BRL/LatAm) |
| IPO | January 26, 2021 — 34.6M Class A shares at $17.00 ([[Blackstone]] a selling holder) |
| Domicile | Grand Cayman |

## Price chain

| Point | Date | Price | Note |
|-------|------|-------|------|
| IPO price | 2021-01-26 | $17.00 | $625M raised; Blackstone partial exit |
| First close | 2021-01-22* | $15.72 | Weak debut below IPO price |
| All-time low | 2025-04-08 | $9.13 | April 2025 tariff-shock / EM risk-off trough |
| Recent high | 2026-01-08 | $17.15 | Back to IPO level on the 2025 re-rating |
| Last | 2026-06-09 | $11.47 | ~33% below the $17 IPO price five years on |

*First DB close stamps the trading debut; IPO pricing was $17.00.

Despite fee-earning AUM growth of 38% and FRE compounding double digits, PAX trades below its IPO price — the gap between business growth and share performance is the listed-alt multiple compression plus a persistent EM/Brazil discount.

## Peer-relative performance

![[pax-vs-bx-kkr-apo-cg-price-chart.png]]
*PAX (blue) vs US alt managers [[Blackstone\|BX]], [[KKR]], [[Apollo Global Management\|APO]], [[Carlyle Group\|CG]], normalized to IPO (Jan 2021 = 100, log scale). PAX has materially lagged the US complex over the period — the divergence the cluster work quantifies: PAX is a Brazil/EM-beta name, not a US-alt co-mover.*

## Correlation structure

The cohort correlation matrix and full hierarchical/PCA diagnostics live in the [[Pátria Investimentos]] cluster-validation section. Headline: PAX's pairwise 1-year correlations are uniformly moderate — [[KKR]] 0.56, [[EWZ]] 0.50, [[Blackstone\|BX]] 0.49, [[SPY]] 0.49, [[XLF]] 0.45 — so it tracks the US alts only marginally more than the broad market and is not captured by a Brazil factor either. Those low absolute correlations make PAX a hierarchical singleton (join distance 0.494, lowest PC1 loading 0.262): a genuine low-correlation diversifier, not a co-mover of the "alt-manager beta."

## Related

- [[Pátria Investimentos]] — actor note (business, financials, cluster validation)
- [[Blackstone]] — minority holder and US-alt comparator
- [[Brazil]] — EM factor driver

*Created 2026-06-11 alongside the Pátria deepdive. Price data from market_data.db (NASDAQ close).*
