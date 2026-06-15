---
aliases: [Foreign private issuer, FPI, FPIs, foreign issuer]
tags: [concept, securities, regulation, sec]
---

# Foreign private issuer

A foreign private issuer (FPI) is the [[SEC]] category for a non-US company that lists or registers securities in the US under a lighter disclosure regime than a domestic filer. The status is not cosmetic: it changes which forms a company files, which accounting standard it reports under, and therefore how clean and comparable its data is — which is why so many vault names that trade on US exchanges have patchy financials and GAAP-looking losses that are not operating losses. [[Aura Minerals|AUGO]] (British Virgin Islands) and [[Equinox Gold|EQX]] (Canada) are working examples: both file [[#What FPI status changes|6-K interims and IFRS annuals]] rather than 10-Qs and US GAAP, which is why the standard data vendors return empty quarterly and annual statements for them and why a filing-sourced manual insert is the only reliable path.

## The two-part test

FPI status is defined identically in Rule 405 (Securities Act) and Rule 3b-4 (Exchange Act). A non-US company qualifies if either:

- Shareholder test — 50% or less of its outstanding voting securities are held of record by US residents; or
- Business-contacts test — even if US residents hold more than 50%, the company still qualifies unless any one of these is true: a majority of its officers or directors are US citizens or residents, more than 50% of its assets are located in the US, or its business is principally administered in the US.

The practical effect is that a company can be run by Brazilians, incorporated in the British Virgin Islands, and traded mostly on [[Nasdaq]] — and still be an FPI, because the test turns on record holders and formal contacts, not on where the business actually operates.

## What FPI status changes

| Dimension | FPI | US domestic issuer |
|---|---|---|
| Annual report | Form 20-F, due 4 months after fiscal year-end | Form 10-K, 60–90 days |
| Interim reporting | Form 6-K — furnishes material info; no mandated quarterly | Form 10-Q each quarter |
| IPO registration | Form F-1 | Form S-1 |
| Accounting | [[IFRS]] as issued by the IASB, no US-[[GAAP]] reconciliation (or home GAAP with reconciliation) | US GAAP |
| Insider reporting | Exempt from Section 16 short-swing rules | Section 16 applies |
| Proxy / Reg FD | Exempt | Apply |
| Governance | May follow home-country practice (with disclosure) | Full exchange standards |

The two that matter most for analysis are the absence of a mandated quarterly statement (a 6-K is a furnishing, not a standardized 10-Q) and the IFRS option.

## Why it matters for analysis

FPI status is the hidden cause behind three recurring vault problems:

- Data gaps. Vendors such as Alpha Vantage key off the standardized 10-K/10-Q XBRL stream; FPIs file 20-F/6-K instead, so the vendor returns empty annual and quarterly statements. The fix is to anchor on the filing or a verified extract and insert manually — the lesson logged for [[Aura Minerals|AUGO]] and reprised for [[Equinox Gold|EQX]].
- GAAP-looking losses that are not operating losses. IFRS treats some items differently from US GAAP — most visibly financial-instrument and FX remeasurement, which flows through the income statement. [[Aura Minerals]]'s ~$416M non-cash finance line and IFRS net loss on a $459M operating profit is the canonical case.
- Thin comparability. No quarterly cadence and home-country governance make FPIs harder to track and to hold to the same standard as domestic peers.

## The 2025 SEC review

On June 4, 2025 the [[SEC]] unanimously published a concept release (33-11376) reassessing FPI eligibility, with the comment period closing September 8, 2025. The concern is precisely the pattern several vault names embody: FPIs are increasingly incorporated in low-disclosure jurisdictions (the British Virgin Islands, Cayman) and traded solely on US markets with no meaningful home-country regulatory oversight — so they get the lighter US regime without the home-country backstop the accommodations originally assumed. Any tightening (for example a market-listing or foreign-trading-volume requirement) would push some current FPIs toward full domestic-style reporting. No final rule had been adopted as of this note.

## In the vault

| Issuer | Domicile | Files | Why FPI matters |
|---|---|---|---|
| [[Aura Minerals]] (AUGO) | British Virgin Islands | 6-K / 20-F / F-1 | IFRS swap remeasurement drives a GAAP-look net loss; empty vendor statements |
| [[Equinox Gold]] (EQX) | Canada | 6-K interims | Same empty-annual data gap; manual insert required |
| China ADRs / cross-listings | Cayman / PRC | 20-F | IFRS or home GAAP, 20-F cadence; [[Holding Foreign Companies Accountable Act]] audit overlay |

## Synthesis

FPI is a structural lens, not a label: once you know a US-traded name is a foreign private issuer, you can predict its data shape (20-F/6-K, IFRS, no clean quarterly), anticipate the GAAP-vs-adjusted gap, and distrust the vendor feed in advance. The category also sits at a live regulatory edge — the 2025 SEC concept release targets exactly the BVI/Cayman-incorporated, US-only-traded issuers that have become common, so the accommodations that make these names cheap to list may narrow. The operating rule for the vault is simple: when a US ticker is an FPI, go to the filing, expect IFRS artifacts, and treat the empty vendor statement as the norm rather than an error.

## Related

- [[SEC]] — sets and is reviewing the FPI definition
- [[Aura Minerals]] / [[Aura Minerals securities note]] — the canonical IFRS-artifact case
- [[Equinox Gold]] — the second empty-annual case this session
- [[IFRS]] — the accounting option that produces the GAAP-look losses
- [[GAAP]] — the US baseline FPIs may avoid reconciling to
- [[Holding Foreign Companies Accountable Act]] — the audit-oversight overlay on foreign issuers
- [[Brazilian Depositary Receipts]] — the mirror image: a Brazilian wrapper on a foreign issuer, where FPI is the US wrapper
- [[Offshore investing for Brazilians]] — the route through which Brazilians buy these foreign issuers

---

*Created 2026-06-14. Definition from SEC Rule 405 / Rule 3b-4; 2025 review from the SEC Concept Release on Foreign Private Issuer Eligibility (33-11376, Jun 4 2025; comments closed Sep 8 2025) via Harvard Law CorpGov / Morgan Lewis / Sidley. Chart data not applicable: a securities-regulation concept, not a price series.*
