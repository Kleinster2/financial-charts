#concept #demand #ai #datacenter

Capital expenditure by the Big 5 hyperscalers (Amazon, Google, Meta, Microsoft, Oracle) and Tier 2 neoclouds (CoreWeave, Lambda, Crusoe) on AI infrastructure — the primary demand signal for semiconductors.

---

## The chart

![[hyperscaler-capex.png]]

*Solid lines = actual quarterly capex; dotted = forecasts based on company guidance and analyst estimates*

---

## Quarterly trajectory

| Hyperscaler | Q3 2019 | Q3 2025 | Multiple |
|-------------|---------|---------|----------|
| **AMZN** | $4.7B | $35.1B | **7.5x** |
| **GOOG** | $6.7B | $24.0B | **3.6x** |
| **META** | $3.5B | $18.8B | **5.4x** |
| **MSFT** | $3.4B | $19.4B | **5.7x** |
| **Big 4 Total** | $18.3B | **$97.3B** | **5.3x** |

Oracle not shown (fiscal year ends May, quarters don't align).

---

## 2025 guidance

| Hyperscaler | FY2025 Guidance | Notes |
|-------------|-----------------|-------|
| **AMZN** | $125B | Calendar year |
| **GOOG** | $91-93B | Calendar year, raised 3x |
| **META** | $70-72B | Calendar year |
| **MSFT** | ~$80B | Fiscal year ends June |
| **ORCL** | ~$50B | Fiscal year ends May, raised from $35B |

---

## 2026 forecasts

| Hyperscaler | 2026 Estimate | Source |
|-------------|---------------|--------|
| **AMZN** | ~$150B | CFO: "will grow in 2026" |
| **GOOG** | ~$115B | CFO: "significant increase" |
| **META** | ~$100B | CFO: "notably larger" |
| **MSFT** | $121-140B | Jefferies, Cantor |
| **ORCL** | ~$50B+ | Already at $50B for FY26 |

**Aggregate forecasts (Big 5):**

| Source | 2025 | 2026 | YoY |
|--------|------|------|-----|
| CreditSights | ~$443B | **~$602B** | +36% |
| Goldman Sachs | — | **$527B+** | — |

~75% of 2026 capex (~$450B) is AI infrastructure.

---

## Oracle: fastest growth, most stress

Oracle is ramping fastest but showing financial strain:

| Metric | Value |
|--------|-------|
| FY25 capex | $21.2B |
| FY26 capex guidance | **$50B** (raised from $35B) |
| YoY growth | **2.4x** |
| Capital intensity | **57%** of revenue (highest) |
| Q2 FY26 FCF | **-$10B** |
| RPO backlog | $523B (+$68B in one quarter) |

**Credit concerns:** Oracle's CDS spreads widened to 125+ bps — levels not seen since 2009. Bonds trade like junk despite Baa2/BBB ratings.

**Why:** OpenAI/Stargate ($300B commitment), Meta and NVIDIA contracts driving backlog.

---

## Tier 2: Neoclouds

GPU-native cloud providers built for AI workloads. Smaller than hyperscalers but growing fast.

### CoreWeave (CRWV)

| Metric | Value |
|--------|-------|
| 2025 capex | $12-14B |
| 2026 capex | **$30B+** (doubling) |
| Revenue backlog | $55.6B |
| Contracted power | 2.9 GW |
| Debt/equity | **4.8x** |

Largest neocloud. GPU-collateralized debt model unprecedented in tech. $14B Meta deal anchors backlog.

### Other neoclouds

| Player | Status | Notes |
|--------|--------|-------|
| **Lambda Labs** | Private | Developer-first, modular ML stack |
| **Crusoe** | Private | 45GW pipeline (ambitious), energy partnerships |
| **Nebius** | Public (NBIS) | Yandex spin-off, European focus |
| **Together AI** | Private | Training/inference platform |

**Cost breakdown (per Nebius):**
- GPUs: **80%** of spending
- DC buildout: 18-20%
- Land/power: ~1%

### Neocloud risk

Early 2026 sentiment shifting from "build it and they will come" to ROIC focus. CoreWeave trading at discount to 2025 highs. Lambda/Together IPO windows narrowing.

See [[CoreWeave]] for detailed analysis.

---

## Financing the buildout

Hyperscalers are using multiple structures:

| Structure | Example |
|-----------|---------|
| Corporate bonds | Meta $30B IG offering (2025) |
| Private credit | Meta $30B SPV with Blue Owl |
| Project finance | GPU leasing, DC sale-leasebacks |
| Off-balance-sheet | Meta Hyperion ($50B Louisiana DC) |

Morgan Stanley estimates $1.5T total AI financing needed, $800B via private credit by 2028.

See [[AI infrastructure financing]] for details.

---

## What it means

**For semiconductors:**
```
Hyperscaler $ → NVIDIA/AMD → TSMC → SK Hynix (HBM) → OSAT
```

Every dollar of capex flows through the chip supply chain. $600B in 2026 = unprecedented demand.

**For power:**
- 1GW data center costs ~$50B
- Big 5 adding 10+ GW capacity
- See [[Power constraints]], [[BYOP]]

**For credit markets:**
- Hyperscalers issuing record debt
- Oracle showing stress despite IG ratings
- Risk of overbuilding if AI demand disappoints

---

## For theses

- [[Long TSMC]] — hyperscaler capex = TSMC revenue
- [[Long memory]] — every GPU needs HBM
- [[AI infrastructure financing]] — credit market implications

---

## Related

- [[AI hyperscalers]] — the players
- [[Amazon]], [[Google]], [[Meta]], [[Microsoft]], [[Oracle]] — Big 5 notes
- [[CoreWeave]] — largest neocloud
- [[AI infrastructure financing]] — how it's funded
- [[Power constraints]] — physical limits
- [[BYOP]] — bring your own power trend
- [[GPU deployment bottleneck]] — shipped ≠ deployed

*Created 2026-01-20*
