#concept #finance #datacenter #ai

Financing model where GPUs serve as loan collateral. Pioneered by [[CoreWeave]] in Aug 2023.

---

## How it works

1. AI company needs GPUs but lacks capital
2. Lender finances GPU purchase
3. GPUs serve as collateral (first-lien)
4. Company pays debt service from GPU rental/inference revenue
5. If default, lender seizes and resells GPUs

**Key insight:** 75% of AI cloud spend = GPUs. Unlike software, hardware has tangible resale value.

---

## Market size

| Metric | Value |
|--------|-------|
| Market since 2024 | $10B+ |
| Effective rates | 11-14% |
| Typical term | 3-5 years |

---

## Why GPUs work as collateral

- **Tangible**: Physical assets with serial numbers
- **Liquid**: Secondary market developing (hyperscaler demand = price floor)
- **Known depreciation**: Unlike software, hardware follows predictable curves
- **High value density**: Single H100 = $25-40K, easy to track

---

## Key deals

| Deal | Amount | Date | Collateral |
|------|--------|------|------------|
| [[CoreWeave]] initial | $2.3B | Aug 2023 | H100 GPUs |
| [[CoreWeave]] main | $7.5B | May 2024 | GPU servers + SPV equity |
| [[xAI]] Colossus | $12.5B debt | Oct 2025 | GB200/GB300 chips |

See [[AI infrastructure deals]] for full capital stack details.

---

## Structure (CoreWeave model)

```
                    ┌─────────────────┐
                    │   Blackstone    │
                    │   + Magnetar    │
                    │   (Co-leads)    │
                    └────────┬────────┘
                             │ $7.5B debt
                             ▼
                    ┌─────────────────┐
                    │      SPV        │
                    │  (holds GPUs)   │
                    └────────┬────────┘
                             │ GPU lease
                             ▼
                    ┌─────────────────┐
                    │   CoreWeave     │
                    │  (operates)     │
                    └─────────────────┘
```

**Collateral**: First-lien on GPU servers + SPV equity
**Rate**: [[Benchmark]] + 4% (DDTL 3.0)

---

## "The Box" — CoreWeave's SPV mechanics (Davos, Jan 2026)

**Mike Intrator explained** the detailed mechanics at Barron's Davos interview. "The Box" is CoreWeave's internal term for their SPV.

**What goes in the Box:**
- GPUs (collateral)
- Offtake contract (e.g., 5-year Microsoft deal)
- Data center contract
- Power purchase agreement

**Waterfall** — money flows through the Box in priority order:
1. Power costs
2. Data center costs
3. Principal + interest
4. **Then** CoreWeave gets paid

**Key insight:** CoreWeave doesn't touch revenue until all obligations cleared. Debt amortizes within contract term.

**"The equity slug"** — Intrator's term for residual GPU value:
- After 5-year contract: debt paid off, CoreWeave owns GPUs outright
- "I want to own the equity slug... they have option value embedded in them"
- Contrary to depreciation critics, GPUs retain utility after contract

**Not speculative:** GPUs are pre-sold to counterparties (Microsoft, Meta) before purchase. Risk capital only goes to "the long pole" — physical data centers.

**"East Coast capital vs West Coast capital":**
- East Coast (debt): "Pay me my goddamn money back" — infrastructure financing
- West Coast (equity): Technology innovation, software layer
- CoreWeave uses both: equity for software, debt for hardware

---

## Risks

### For lenders

| Risk | Reality |
|------|---------|
| **Obsolescence** | GPU generations turn over every 18-24 months (Hopper → Blackwell → Rubin) |
| **Rental rate collapse** | Down 50-70% since peak — collateral value declining |
| **Resale market** | Still maturing, limited liquidity for large volumes |
| **Concentration** | Few borrowers (CoreWeave, xAI) = concentrated risk |

### Mitigations

- Negotiate depreciation schedules vs loan payoff
- Short financing terms (match to GPU useful life)
- Residual value buffers
- NVIDIA relationship (repurchase agreements, upgrade paths)

---

## NVIDIA's role

NVIDIA now invests equity alongside debt:

| Investment | Amount | Purpose |
|------------|--------|---------|
| CoreWeave (Apr 2023) | $100M | Early validation |
| CoreWeave IPO | ~6% stake | Ongoing support |
| xAI Colossus SPV | $2B | Financing its own hardware |

**Effect**: NVIDIA de-risks lenders by having skin in the game. Also ensures chip demand.

---

## Comparison to traditional asset-backed lending

| Metric | GPU financing | Auto loans | Equipment leasing |
|--------|--------------|------------|-------------------|
| Collateral value trend | Declining fast | Stable/slow decline | Varies |
| Secondary market | Nascent | Deep, liquid | Moderate |
| Obsolescence risk | High | Low | Moderate |
| Rates | 11-14% | 5-8% | 6-10% |

GPU financing commands premium rates due to higher risk.

---

## Investment implications

**Who benefits:**
- [[Blackstone]] — co-led CoreWeave facility
- Magnetar — co-led CoreWeave facility
- [[Apollo]] — xAI debt participant
- [[Private credit]] funds with AI exposure

**Who's at risk:**
- Lenders if GPU rental rates keep falling
- Borrowers if refinancing becomes difficult

---

## For theses

- [[AI infrastructure financing]] — one of several structures
- [[CoreWeave]] — pioneer, proof of concept
- [[xAI]] — largest GPU-collateral deal (Colossus)

---

*Updated 2026-02-02*

## Related

- [[AI infrastructure financing]] — broader context
- [[AI infrastructure deals]] — detailed case studies
- [[AI financing structures]] — alternative structure
- [[CoreWeave]] — pioneer ($7.5B Blackstone)
- [[xAI]] — Colossus ($12.5B debt portion)
- [[Blackstone]] — key lender
- [[Apollo]] — key lender
- [[NVIDIA]] — provides equity alongside debt
