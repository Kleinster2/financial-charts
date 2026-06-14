---
aliases: [Defense IT, GovCon IT, Government IT contractors, Defense services]
---
#sector #defense #it #cybersecurity #government

# Defense IT Services

Government and defense IT services contractors. Distinct from hardware primes — services-based business model with cost-plus contracts, civilian agency exposure, and recurring revenue. Trades as a tight cluster (0.61 correlation).

![[defense-it-services-sector-chart.png]]
*LDOS and CACI outperforming. All four move together — validated as distinct sub-sector from hardware primes.*

---

## Correlation structure

| Metric | Value | Interpretation |
|--------|-------|----------------|
| Avg correlation | 0.61 | Strong (tight sector) |
| Range | 0.56 - 0.65 | LDOS-BAH to LDOS-CACI |
| vs Hardware primes | ~0.35 | Distinct clusters |
| Period | 2024-01 to present | |

Pairwise detail:
| Pair | Correlation |
|------|-------------|
| LDOS - CACI | 0.65 |
| LDOS - SAIC | 0.63 |
| SAIC - CACI | 0.62 |
| BAH - SAIC | 0.61 |
| BAH - CACI | 0.58 |
| LDOS - BAH | 0.56 |

IT Services trades distinctly from hardware primes — different business model (labor vs product), different margins, different cycle.

---

## Cluster validation

> [!success] Cluster status: validated — moderate, distinct from the hardware primes (June 2026)
> The four listed GovCon-IT pure-plays ([[Leidos]], [[Booz Allen Hamilton]], [[CACI]], [[SAIC]]) form a real single-factor cluster: intra-corr 0.604, PC1 70.4%, rejecting the independence, random-basket and vol-matched nulls (p = 0.0001 / 0.0004 / 0.0001). Hierarchical clustering separates them cleanly from the hardware primes ([[Defense primes basket\|LMT/RTX/NOC/GD/LHX]], intra-advantage +0.310) and from commercial IT-services ([[Accenture]]/[[Cognizant]], +0.296). This resolves the pattern-7 boundary question left open by [[Defense primes basket]]: [[Leidos]] is not a sector orphan — it is a core member of this cohort, which is exactly why it dragged the hardware-primes validation. Two caveats: cohesion is regime-sensitive (holdout WEAKENED 0.85; tighter in budget-up years, looser in the 2024 DOGE-scrutiny dispersion) and the boundary extends to KBR (the dendrogram's natural fifth member) while [[Parsons]] stays out. See below.

This formalizes the informal "Correlation structure" numbers above. Same DoD-customer end-market as the hardware primes, but a distinct factor: IT-services trade on the labor and recompete cycle (cost-plus, clearance-gated headcount), the primes on the product and program cycle — and the math puts +0.310 of intra-advantage between them.

### Diagnostics summary

| Diagnostic | Value | Read |
|---|---|---|
| Intra-cluster corr (1Y) | 0.604 [0.522–0.748] | Moderate–strong, single factor |
| PC1 explained variance | 70.4% (PC2 14.0%) | Single-factor |
| Random-basket p (10k) | 0.0004 | Beats random 4-picks (null mean 0.149) |
| Vol-matched p (10k) | 0.0001 | Real factor, not shared vol |
| Holdout ratio (2Y split) | 0.85 — WEAKENED | Train 0.707 / test 0.599; off the 2024 peak |
| Threshold clean band | [0.44, 0.48], width 0.04 | FRAGILE — KBR joins just above (extends, not breaks) |
| Intra-adv vs hardware primes | +0.310 | The LDOS-exclusion finding — distinct factor |
| Intra-adv vs commercial IT | +0.296 | Distinct from [[Accenture]]/[[Cognizant]] |
| Intra-adv vs [[SPY]]/[[ITA]] | +0.420 | Strongly market-uncorrelated |

1Y daily log returns through 2026-06-12 (214 obs), threshold 0.5. Config: `scripts/cluster_configs/defense_it.yaml`; registry row 2026-06-13. Terminology: [[Cohort, cluster, basket]].

### Boundary — distinct from the primes, extends to KBR

![[defense-it-cluster-dendrogram-1y.png]]
*Hierarchical clustering at 0.5. The four GovCon-IT names cluster together and pull in KBR; the hardware primes (LMT/RTX/NOC/GD/LHX) form a separate cluster, commercial IT ([[Accenture]]/[[Cognizant]]) a third, and [[Parsons]] sits alone. LDOS clusters with IT-services, not the primes — the clean answer to the [[Defense primes basket]] exclusion.*

The threshold scan finds a clean four-name band at [0.44, 0.48] (width 0.04, fragile); one step looser KBR joins, then [[Parsons]]. So the cohort is real but its exact membership is a boundary call — four names tight, or five with KBR. Unlike a falsification, the contaminator is a same-business cousin, not a foreign sector.

### Topology — two service pairs

| Join step | Names | Distance (1-\|corr\|) | Read |
|---|---|---|---|
| 1 | BAH + SAIC | 0.252 | Consulting / IT-modernization pair |
| 2 | LDOS + CACI | 0.383 | C5ISR / cyber / ISR pair |
| 3 | (BAH+SAIC) + (LDOS+CACI) | 0.435 | The two pairs merge |

The cohort is two service-model pairs: [[Booz Allen Hamilton]]+[[SAIC]] (broad consulting and IT modernization) and [[Leidos]]+[[CACI]] (C5ISR, cyber, ISR), bridging at join distance 0.435.

### PC1 index weights

![[defense-it-cluster-pca-1y.png]]
*PCA scree and PC1 loadings. PC1 explains 70.4% with near-identical loadings (0.47–0.52) — a clean single factor with no outlier.*

| Ticker | PC1 loading | Loading weight | Ann vol | Raw PC1-mimic weight |
|---|---|---|---|---|
| LDOS | 0.497 | 24.9% | 31.5% | 28.6% |
| BAH | 0.510 | 25.5% | 41.6% | 22.3% |
| CACI | 0.473 | 23.7% | 33.1% | 25.9% |
| SAIC | 0.519 | 26.0% | 40.6% | 23.2% |

Topology and the PC1-mimic basket barely diverge here — the loadings are nearly equal, so the raw PC1-mimic weights tilt only modestly toward the lower-volatility names ([[Leidos]] 28.6% at 31.5% vol versus [[Booz Allen Hamilton]] 22.3% at 41.6%). A near-equal-weighted basket reproduces the factor.

### Distinctness

![[defense-it-cluster-correlation-1y.png]]
*1Y pairwise correlation heatmap. The four GovCon-IT names form a warm block, visibly cooler against the hardware primes and commercial IT.*

### Historical tightness evolution

![[defense-it-cluster-rolling-tightness-90d.png]]
*Rolling 90-day cohesion since 2021 — durable but regime-sensitive: tight in budget-expansion years (0.745 in 2022, 0.696 in 2025), looser in the 2024 DOGE contract-scrutiny dispersion (0.526).*

| Window | Avg intra-corr | PC1 | Final join distance |
|---|---|---|---|
| 2022 | 0.745 | 80.9% | 0.290 |
| 2024 | 0.526 | 64.6% | 0.509 |
| 2025 | 0.696 | 77.4% | 0.349 |
| Latest 90d | 0.679 | 76.0% | 0.371 |

*Durable but regime-sensitive: the cluster never falls below ~0.53 and re-tightens with budget visibility, but it is not a single-regime factor like the tightest cohorts. The 2Y holdout (0.85, WEAKENED) reflects the same erosion from the 2024–25 peak.*

### The read-through

- Two factors in one end-market. The DoD-customer umbrella holds a hardware-prime factor ([[Defense primes basket]], product/program cycle) and a separate GovCon-IT factor (labor/recompete cycle), +0.310 apart. A "defense" sleeve that mixes them is two positions, not one.
- LDOS's home, resolved. [[Leidos]] anchors this cohort (highest PC1-mimic weight); its exclusion from the hardware primes was correct and now has a constructive answer — it belongs here.
- Membership is four-or-five. KBR is the dendrogram's natural fifth member; [[Parsons]] is not. The tradeable cohort is [[Leidos]]/[[Booz Allen Hamilton]]/[[CACI]]/[[SAIC]], optionally with KBR.

Method and terminology: `docs/cluster-validation.md`, [[Cohort, cluster, basket]], [[Vault cluster taxonomy]]. Post-definition OOS re-validation is queued for the July 2026 quarterly pass (definition date 2026-06-13).

---

## Market size

| Segment | 2024 | 2033E | CAGR |
|---------|------|-------|------|
| Federal IT spending | >$100B | — | — |
| Defense cybersecurity | $30B | $79B | 11.4% |
| Internal security | $52B | $77B (2031) | 6.6% |

North America = 42% of global defense cyber market.

---

## Key players

### Public companies

| Company | Ticker | Revenue | Employees | Specialization |
|---------|--------|---------|-----------|----------------|
| [[Leidos]] | LDOS | ~$16B | ~47K | ISR, cyber, logistics, health IT |
| [[Booz Allen Hamilton]] | BAH | $12B | ~33K | AI, analytics, cyber, consulting |
| [[General Dynamics IT]] | (part of GD) | ~$10B+ | — | Zero-trust, cloud, managed services |
| [[SAIC]] | SAIC | ~$8B | ~24K | IT modernization, cloud, systems integration |
| [[CACI]] | CACI | $8.6B | ~24K | C5ISR, cyber, space tech |

### Private companies

| Company | Owner | Revenue | Employees | Notes |
|---------|-------|---------|-----------|-------|
| [[Peraton]] | [[Veritas Capital]] | — | ~22K | Cyber, space, classified |
| [[ManTech]] | [[Carlyle Group]] | ~$2.6B | ~10K | Cyber, data/AI, enterprise IT |
| Accenture Federal | [[Accenture]] | — | — | Civilian-heavy |

---

## Booz Allen Hamilton

Largest AI supplier to U.S. government.

| Metric | Value |
|--------|-------|
| Revenue (FY Mar 2025) | $12.0B (+12% YoY) |
| Net income | $935M (+56% YoY) |
| Backlog | $38B (Jun 2025) |
| AI revenue | ~$800M |

Segment mix (FY24):
- Defense: 47% (fastest growing, +20% YoY)
- Civil: 34%
- Intelligence: 17%

---

## Business model

| Characteristic | Implication |
|----------------|-------------|
| Cost-plus contracts | Stable margins, limited upside |
| Labor-intensive | Revenue = headcount × bill rate |
| Clearance moat | TS/SCI workforce hard to replicate |
| Recompete risk | 3-5 year contract cycles |
| Backlog visibility | Multi-year revenue predictability |

Margins: Operating margins typically 7-10% (lower than hardware primes at 10-12%).

---

## Growth drivers

| Driver | Detail |
|--------|--------|
| IT modernization | Legacy system replacement, cloud migration |
| Cybersecurity | Zero-trust mandates, threat escalation |
| AI/ML adoption | Booz Allen leads, others catching up |
| Classified programs | Intelligence community expansion |
| DoD budget growth | FY25 $850B → FY27 $1.5T proposed |

---

## Recent major contracts

| Date | Contractor | Contract | Value |
|------|------------|----------|-------|
| Jan 2026 | [[General Dynamics IT]] | Navy C5ISR modernization | $988M |
| Sep 2025 | [[General Dynamics IT]] | STRATCOM modernization | $1.5B |
| Sep 2025 | [[ManTech]] | SOUTHCOM IT services | $910M |
| Mar 2025 | [[SAIC]] | Army ASTRO software | $1.8B |
| 2025 | [[CACI]], [[Peraton]] | Defense contracts | $2.2B combined |

---

## M&A activity

Consolidation ongoing — scale matters for large recompetes.

| Date | Acquirer | Target | Value | Rationale |
|------|----------|--------|-------|-----------|
| May 2025 | [[Leidos]] | Kudu Dynamics | $300M | AI-enabled offensive cyber |
| Dec 2025 | [[ManTech]] | Elder Research | — | Data science |
| 2025 | [[CACI]] | Space-tech deal | $2.6B | Space capabilities |
| Sep 2022 | [[Carlyle Group]] | [[ManTech]] | $4.2B | Take-private |

---

## Competitive dynamics

| Factor | Winners | Losers |
|--------|---------|--------|
| AI capabilities | Booz Allen, Palantir | Legacy IT shops |
| Clearance workforce | Incumbents | New entrants |
| Scale for large IDIQs | Leidos, GDIT | Small contractors |
| Agile M&A | Private (Peraton, ManTech) | Slower public cos |
| Price aggression | PE-backed | Public margin pressure |

PE ownership advantage: Private companies (Peraton/Veritas, ManTech/Carlyle) can bid aggressively without quarterly earnings pressure.

---

## Sector KPIs

| Metric | Definition | Target | Why it matters |
|--------|------------|--------|----------------|
| Book-to-Bill | Awards / Revenue | >1.0x | Backlog growth |
| Backlog | Funded + unfunded | Growing | Revenue visibility |
| Organic growth | Ex-M&A revenue growth | 5-10% | Underlying demand |
| EBITDA margin | EBITDA / Revenue | 10-12% | Profitability |
| Attrition | Employee turnover | <15% | Clearance retention |

---

## Risks

| Risk | Impact |
|------|--------|
| Recompete losses | Revenue cliffs |
| DOGE efficiency | Contract scrutiny, cuts |
| Clearance processing delays | Hiring constraints |
| Wage inflation | Margin compression |
| Protest culture | Award delays |

---

## vs Hardware primes

| Factor | IT Services | Hardware Primes |
|--------|-------------|-----------------|
| Revenue model | Labor hours | Product sales |
| Margins | 7-10% operating | 10-12% operating |
| Capital intensity | Low | High |
| Cycle length | 3-5 year contracts | 10-20 year programs |
| Visibility | Backlog | Backlog + multi-decade |
| Customer | DoD + civilian + IC | Primarily DoD |

---

## Investment considerations

Bull case:
- Structural IT modernization demand
- Cybersecurity spending durable
- AI adoption accelerating (Booz Allen leads)
- Budget growth tailwind

Bear case:
- [[DOGE]] contract scrutiny
- Recompete risk always present
- Margin pressure from PE-backed competitors
- Labor market for cleared talent

---

## Related

Companies:
- [[Leidos]] — largest by revenue
- [[Booz Allen Hamilton]] — AI leader
- [[SAIC]] — IT modernization
- [[CACI]] — C5ISR, space
- [[ManTech]] — Carlyle-owned, cyber/AI
- [[Peraton]] — Veritas-owned, classified
- [[General Dynamics IT]] — part of GD
- [[Palantir]] — AI analytics (different model)

Investors:
- [[Carlyle Group]] — owns ManTech
- [[Veritas Capital]] — owns Peraton

Sectors:
- [[Defense]] — parent sector
- [[Cybersecurity]] — overlapping capability

Concepts:
- [[DOGE]] — efficiency risk
- [[Agentic AI]] — transformation driver

*Created 2026-01-28*
