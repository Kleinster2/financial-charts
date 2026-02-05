# AI Workflow Disruption (AIWD)

Synthetic index tracking stocks exposed to AI disruption of white-collar workflows. Thesis: companies whose core business involves structured knowledge work—legal research, financial analysis, IT services, advertising creative—face margin compression or displacement as LLMs commoditize their labor arbitrage.

**Ticker:** `AIWD` (synthetic, base = 100 on 2026-02-03)

---

## Constituents

### Legal & Data Analytics (60%)

| Ticker | Company | Weight | Exposure |
|--------|---------|--------|----------|
| TRI | [[Thomson Reuters]] | 15% | Legal research, Westlaw |
| RELX | [[RELX]] | 15% | LexisNexis, legal/regulatory |
| WKL.AS | [[Wolters Kluwer]] | 10% | Tax, legal, compliance software |
| LZ | [[LegalZoom]] | 5% | Consumer legal services |
| FDS | [[FactSet]] | 10% | Financial data terminals |
| MORN | [[Morningstar]] | 5% | Investment research |

### Indian IT Services (25%)

| Ticker | Company | Weight | Exposure |
|--------|---------|--------|----------|
| INFY | [[Infosys]] | 10% | IT outsourcing, BPO |
| TCS.NS | [[TCS]] | 10% | IT services, consulting |
| HCLTECH.NS | [[HCL Tech]] | 5% | IT services |

### Advertising (15%)

| Ticker | Company | Weight | Exposure |
|--------|---------|--------|----------|
| OMC | [[Omnicom]] | 7.5% | Agency creative, media buying |
| PUB.PA | [[Publicis]] | 7.5% | Agency creative, Epsilon data |

---

## Thesis

These companies monetize structured knowledge work through labor arbitrage:
- **Legal/data firms** sell access to information + analyst interpretation
- **Indian IT** sells low-cost engineering and back-office labor
- **Ad agencies** sell creative production and media planning

LLMs threaten each model:
1. Legal research becomes near-instant, reducing billable hours
2. Code generation and document automation shrink outsourcing TAM
3. AI creative tools commoditize ad production

**Not a pure short thesis.** Some names (TRI, RELX) have pricing power and switching costs. Others (LZ, Indian IT) face more direct substitution risk. The basket tracks the aggregate exposure.

---

## Performance

![[aiwd-vs-spy.png]]
*AIWD basket down ~17% vs SPY +50% since Jan 2024. The ~65pp spread reflects market pricing AI disruption risk into these names—particularly sharp drawdowns in Indian IT and ad agencies through late 2025.*

## Usage

```bash
# Recalculate and store
python scripts/create_aiwd_index.py --store

# Chart vs S&P 500
curl "http://localhost:5000/api/chart/lw?tickers=AIWD,SPY&normalize=true&start=2024-01-01"
```

---

## Related

- [[AI and professional services]]
- [[India]] — IT services exposure
- [[Agentic AI]] — automation of knowledge work
