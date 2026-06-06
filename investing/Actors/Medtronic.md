---
aliases: [MDT]
---
#actor #healthcare #medtech #usa #public

**Medtronic** (NYSE: MDT) — World's largest pure-play medical device company. Pacemakers, insulin pumps, surgical robotics, neuromodulation. Founded 1949 in Minneapolis, now headquartered in Dublin (Irish tax inversion).

---

## Sector correlation

| Sector | ETF | Correlation |
|--------|-----|-------------|
| [[Healthcare]] | XLV | 0.70 |
| Financials | XLF | 0.53 |
| [[Consumer Staples]] | XLP | 0.52 |
| *S&P 500* | *SPY* | *0.47* |

MDT trades as a core Healthcare name (XLV r = 0.70).

---

## Quick stats

| Metric | Value |
|--------|-------|
| Ticker | MDT |
| Market cap | ~$124B (Jan 2026) |
| Revenue (FY26) | $36.4B |
| Employees | ~95,000 |
| Fiscal year end | April |
| Founded | 1949 |
| HQ | Dublin, Ireland (operations in Minneapolis) |

---

## Why Medtronic matters

Medical device bellwether. Medtronic manufactures over half of all pacemakers implanted worldwide. Its technologies treat 70+ health conditions across cardiac, neurological, diabetes, and surgical markets. When procedure volumes or device innovation cycles shift, Medtronic is the first to reflect it.

Pulsed field ablation leader. The company's cardiac ablation solutions grew 71% in Q2 FY26 on strength of PFA portfolio (Sphere-9, PulseSelect, Affela). PFA is displacing traditional RF ablation for atrial fibrillation.

---

## Business segments

| Segment | Q4 FY26 Revenue | Reported / organic growth | Products |
|---------|-----------------|--------|----------|
| Cardiovascular | $3.797B | +13.8% / +10.1% | Pacemakers, ICDs, heart valves, PFA |
| Neuroscience | $2.751B | +5.0% / +3.0% | Neuromodulation, spine, brain therapies |
| Medical Surgical | $2.388B | +8.0% / +5.1% | Surgical tools, patient monitoring |
| Diabetes | $837M | +15.0% / +8.1% | Insulin pumps, CGM |

Cardiovascular remains the acceleration engine. Q4 Cardiac Ablation Solutions revenue grew 78% globally, including 124% U.S. growth, as the PFA portfolio kept taking share.

---

## Key products

| Product | Category | Status |
|---------|----------|--------|
| Sphere-9 | PFA catheter | Market leader in ablation |
| Hugo | Surgical robot | FDA clearance expected 2026 |
| Symplicity | Renal denervation | Hypertension treatment |
| MiniMed 780G | Insulin pump | Automated insulin delivery |
| AltaViva | Neuromodulation | Incontinence treatment |

---

## Diabetes spinoff

Medtronic announced plans to spin off its Diabetes segment, expected to close by late 2026. The unit generates ~$2.5B annually (~8% of revenue) but competes against larger players like [[Abbott]] (Libre CGM) and [[Eli Lilly]]/[[Novo Nordisk]] (GLP-1s reducing insulin demand).

---

## Financials (recent)

![[medtronic-fundamentals-chart.png]]

*The fundamentals chart now has MDT history backfilled from Alpha Vantage, with the FY26 rows source-enriched from Medtronic's Jun. 3 release so GAAP EPS, R&D, SG&A, interest, tax, and D&A are populated.*

![[medtronic-sankey.png]]

*FY26 Sankey: the annual model highlights Medtronic's 65.0% gross margin and the SG&A-heavy medtech cost base.*

![[mdt-q4-fy2026-waterfall.png]]

*Q4 FY26 GAAP waterfall: $9.807B revenue, 65.4% gross margin, 19.1% operating margin, and 12.7% net margin.*

| Period | Revenue | GAAP net income | GAAP diluted EPS | Growth / guidance |
|--------|---------|-----------------|------------------|-------------------|
| Q4 FY26 | $9.807B | $1.243B | $0.96 | +9.9% reported, +6.6% organic revenue |
| FY26 | $36.364B | $4.801B | $3.73 | +8.4% reported, +5.8% organic revenue |
| FY27 guide | — | — | — | +6.75% to +7.25% organic revenue growth |

Q4 non-GAAP EPS was $1.55 and FY26 non-GAAP EPS was $5.53. For database comparability, `income_statement_quarterly` and `income_statement_annual` use GAAP diluted EPS and Medtronic-attributable net income. The FY26 Q4 and annual rows are dated `2026-04-30` to match the local DB's month-end convention, even though the release says the fiscal year ended April 24, 2026.

Stock reaction: MDT closed at $73.75 on Jun. 2, $77.95 on Jun. 3, $81.93 on Jun. 4, and $81.67 on Jun. 5. That is a +5.7% earnings-day reaction and +10.0% over the three closes following the release, making MDT one of the cleaner positive outliers in the Jun. 3-5 scan.

---

## Q4 FY26 read-through

Medtronic delivered the strongest annual revenue growth in a decade, but the quality of the print is more specific than a generic medtech beat:

- PFA is the real growth vector: Cardiac Ablation Solutions grew 78% globally and 124% in the U.S., supporting the pulsed-field-ablation leadership thesis.
- Diabetes is still growing before separation: Q4 Diabetes revenue grew 15.0% reported and 8.1% organic, despite the pending separation and GLP-1 overhang.
- FY27 guidance points to acceleration rather than one-quarter catch-up: management guided to 6.75-7.25% organic revenue growth, including the 53rd week and the Diabetes business for the full fiscal year.
- Margin caveat: Q4 non-GAAP operating margin fell 230 bps despite the top-line beat, with management calling out the MiniMed / [[Blackstone]] payment and tariffs as headwinds.

*Sources: [Medtronic Q4/FY2026 results release](https://news.medtronic.com/2026-06-03-Medtronic-reports-fourth-quarter-and-full-year-fiscal-2026-results-delivers-highest-annual-revenue-growth-in-10-years), Jun. 3 2026; SEC Form 10-Q for fiscal quarter ended Jan. 23 2026, parsed locally with `python scripts/parse_sec_filing.py MDT --save logs\mdt_sec_latest.txt`.*

---

## Investment considerations

### Bull case

- Cardiovascular growth re-accelerating (PFA, structural heart)
- Hugo surgical robot could unlock new TAM
- Diabetes spinoff simplifies story
- Trading at discount to peers

### Bear case

- GLP-1 drugs reducing diabetes device demand
- Hugo late vs [[Intuitive Surgical]]
- Ireland HQ complicates tax situation
- Medtech growth structurally slower than pharma

---

## Related

### Securities

- [[Medtronic securities note]]

### Actors and themes

- [[Healthcare]] — sector hub
- [[Abbott]] — CGM competitor (Libre)
- [[Boston Scientific]] — medtech peer
- [[Intuitive Surgical]] — surgical robotics leader
- [[Eli Lilly]] · [[Novo Nordisk]] — GLP-1 impact on diabetes devices

---

*Created 2026-01-28*
