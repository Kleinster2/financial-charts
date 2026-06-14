#concept #quantum #technology

**Quantum computing** — next computing paradigm. Still pre-commercial but attracting significant investment. Multiple approaches competing, no clear winner.

---

![[quantum-computing-chart.png]]
*Quantum-computing public proxies remain high-volatility speculative exposures; the chart is a market-signal artifact, not evidence that any one technical path has crossed into durable commercial use.*

## Synthesis

Quantum computing is still a pre-commercial option on future compute and cryptography disruption. The investable edge is less "own the winner now" than tracking which technical path gains credible replication, which supply-chain chokepoints such as dilution refrigeration capture spend, and whether public pure-plays dilute before revenue catches up. [[Microsoft]]'s topological bet remains the asymmetric branch: huge payoff if validated, major credibility loss if independent replication fails.

## Why it matters for investors

| Factor | Status |
|--------|--------|
| Investment | Billions flowing ([[Microsoft]], Google, [[IBM]], startups) |
| Timeline | Useful applications: 5-15 years (disputed) |
| Public plays | IonQ, Rigetti, D-Wave (all speculative) |
| Big tech exposure | [[Microsoft]], Google, [[IBM]], Amazon (Braket) |
| Risk | High — scientific feasibility still debated for some approaches |

---

## Qubit approaches

| Approach | Players | Pros | Cons |
|----------|---------|------|------|
| Superconducting | [[IBM]], Google, Rigetti | Most mature, highest qubit counts | Error-prone, needs extreme cooling |
| Trapped ion | IonQ, [[Quantinuum]] | Lower error rates, longer coherence | Slower gate speeds, scaling challenges |
| Topological | [[Microsoft]] | Theoretically error-resistant | Unproven — MZMs not yet confirmed |
| Photonic | [[PsiQuantum]], Xanadu | Room temperature operation | Complex error correction |
| Neutral atom | QuEra, Atom Computing | Scalable, flexible | Early stage |
| Quantum annealing | D-Wave | Commercial today (optimization) | Not universal quantum computing |

---

## Key players

### Big tech

| Company | Approach | Status |
|---------|----------|--------|
| [[Microsoft]] | Topological (Majorana) | Majorana 1 chip (2025), controversial |
| [[Google]] | Superconducting | Willow chip, "quantum supremacy" claims |
| [[IBM]] | Superconducting | 1000+ qubits, Qiskit ecosystem |
| [[Amazon]] | Braket (cloud access) | Platform play, not building own hardware |

### Public pure-plays

| Company | Ticker | Approach | Market cap | Notes |
|---------|--------|----------|------------|-------|
| IonQ | IONQ | Trapped ion | ~$7B | Most valuable pure-play |
| Rigetti | RGTI | Superconducting | ~$3B | Integrated hardware + cloud |
| D-Wave | QBTS | Quantum annealing | ~$2B | Only commercial quantum (narrow use) |

### Private

| Company | Approach | Funding | Notes |
|---------|----------|---------|-------|
| [[PsiQuantum]] | Photonic | $2.3B+ | [[GlobalFoundries]] partnership, [[Illinois Quantum and Microelectronics Park\|IQMP]] anchor |
| [[Quantinuum]] | Trapped ion | [[Honeywell]] spinoff | Merged with Cambridge Quantum |
| [[Pasqal]] | Neutral atom | $215M+ | French, Nobel founder, IQMP tenant |
| [[Diraq]] | Silicon spin | A$150M+ | Australian, CMOS-compatible, IQMP tenant |
| QuEra | Neutral atom | $100M+ | [[Harvard]]/[[MIT]] spinout |

### Going public

| Company | Approach | Valuation | Notes |
|---------|----------|-----------|-------|
| [[Infleqtion]] | Neutral atom | $1.8B | [[SPAC]] with Churchill Capital (INFQ), IQMP tenant |

---

## Dilution refrigerators — the hidden chokepoint

Superconducting qubits (the approach used by [[Google]], [[IBM]], Rigetti, and most quantum computers) only work at temperatures near absolute zero — around 10-15 millikelvin (-459.67°F), colder than outer space. At any warmer temperature, thermal noise destroys fragile quantum states. The dilution refrigerator is the machine that makes this possible.

### How they work

A dilution refrigerator uses two isotopes of helium — helium-3 (³He) and helium-4 (⁴He) — mixed together. When helium-3 "dilutes" into helium-4, it absorbs heat at the quantum mechanical level (analogous to how evaporation cools skin, but at atomic scale). By cycling this process, the fridge extracts heat until reaching millikelvin temperatures. The quantum processor sits at the very bottom of the refrigerator — inside the iconic chandelier-like structures seen in quantum lab photos.

### Supply chain

| Supplier | Country | Notes |
|----------|---------|-------|
| Bluefors | [[Finland]] | Market leader, supplies Google, IBM |
| Oxford Instruments | [[UK]] | Legacy cryogenics maker |
| Leiden Cryogenics | [[Netherlands]] | Smaller specialist |

Each unit costs $1-5M+, takes months to build, and requires helium-3 — a rare isotope primarily sourced from nuclear weapons tritium decay. Global helium-3 supply is constrained (~30,000 liters/year, mostly from US and Russian weapons programs). This makes dilution refrigerators both expensive and geopolitically sensitive.

### Why it's a chokepoint

Every superconducting quantum computer needs one. When the US banned dilution refrigerator exports to [[China]], it targeted the physical foundation of China's quantum program. Without these machines, superconducting qubits can't operate — period.

China's response: Pan Jianwei's team at the [[Chinese Academy of Sciences]] independently built domestic dilution refrigerators to international standards after the ban. These now power the Zuchongzhi quantum processor series. See [[2026 Two Sessions]] for context on China's broader self-sufficiency push.

Analogy: Banning dilution refrigerators to China is like banning [[ASML]] lithography to China's chip industry — except dilution refrigerators are less complex than EUV tools, making domestic replication more feasible. The fact that China achieved this relatively quickly validates the "bottleneck → springboard" pattern.

---

## Investment thesis considerations

Bull case:
- Quantum advantage for drug discovery, materials, optimization, cryptography
- Whoever wins captures massive TAM
- Government funding (defense, national security)
- Could obsolete classical computing for specific workloads

Bear case:
- Timeline constantly pushed out ("10 years away" for 30 years)
- Error correction unsolved at scale
- Classical algorithms keep improving
- Most public pure-plays are cash-burning, pre-revenue
- Scientific feasibility still debated (Microsoft's topological approach)

Realistic view:
- Near-term: quantum as cloud service ([[IBM]], Amazon Braket) for experimentation
- Medium-term: hybrid classical-quantum for specific problems
- Long-term: fault-tolerant universal quantum computing (if achievable)

---

## Microsoft Majorana 1 (2025)

Controversial topological approach:

| Detail | Value |
|--------|-------|
| Chip | Majorana 1 (Feb 2025) |
| Approach | Topological qubits via Majorana zero modes (MZMs) |
| Theory | MZMs are inherently error-resistant |
| Controversy | Nature editorial: "results do not represent evidence for MZMs" |
| Microsoft claim | Opposite — says it proves topological qubits work |
| Track record | 2021 Nature paper retracted; 2023 experiment criticized |
| Progress | July 2025 data "more indicative" per Cornell researcher |
| Next step | DARPA Quantum Benchmarking Initiative finalist |

Key quote: "Fundamental physics does not respect the timelines set by big tech companies." — Henry Legg, University of St Andrews

Investment read: Microsoft's quantum bet is high-risk, high-reward. If topological qubits work, they leapfrog competitors. If not, years of investment wasted. Scientific consensus still skeptical.

---

## Illinois Quantum and Microelectronics Park (2025)

Largest US quantum infrastructure project. 128-acre campus in [[Chicago]] (former U.S. Steel South Works). $500M Illinois state funding.

| Tenant | Approach |
|--------|----------|
| [[PsiQuantum]] (anchor) | Photonic — building first US million-qubit system |
| [[IBM]] | Superconducting |
| [[Diraq]] | Silicon spin |
| [[Infleqtion]] | Neutral atom |
| [[Pasqal]] | Neutral atom |

Groundbreaking September 2025. [[Target]] completion 2028. Projected $20B+ economic impact.

Significance: Consolidates multiple quantum approaches in one location with government backing — could accelerate timelines if any approach achieves breakthrough.

See [[Illinois Quantum and Microelectronics Park]] for details.

---

## What to watch

| [[Signal]] | Bullish | Bearish |
|--------|---------|---------|
| Error rates | Decreasing below threshold | Plateau |
| Qubit counts | Scaling with quality | Quantity without quality |
| Commercial applications | Real revenue | Perpetual "demos" |
| Microsoft MZM proof | Independent replication | Continued skepticism |
| Google/[[IBM]] roadmaps | On track | Delays |
| IQMP progress | Tenants hitting milestones | Delays, tenant departures |

---

## China: sanction-driven self-sufficiency (March 2026)

At the [[2026 Two Sessions]], Pan Jianwei ([[Chinese Academy of Sciences]]) revealed that after the US banned dilution refrigerator exports to China, his team independently built domestic versions at international standards — now powering the Zuchongzhi quantum processor series.

This is the same "bottleneck → springboard" pattern seen in semiconductors ([[Huawei]] [[Kirin]] 9020, [[SMIC]] 7nm). The 15th Five-Year Plan (2026-2030) explicitly includes quantum technology commercialization as a priority, with deep integration of industry-academia-research.

Implication: Western quantum equipment exporters face the same long-term dynamic as semiconductor equipment makers — export controls create a protected market for Chinese domestic alternatives with state backing.

*Updated 2026-03-05*

---

## All-In E222 update (Apr 3) — Bitcoin threat timeline

*Data from [[All-In Podcast]] Episode 222, April 3, 2026*

Timeline acceleration: [[Chamath Palihapitiya|Chamath]]: Functional quantum chip now 5-7 years away, accelerated from previous estimates of 25-30 years. Major compression of expected timeline.

Shor algorithm optimization: Oded Regev (NYU, 2023) published improved Shor algorithm work — quantum operations required reduced from 28 million to 500,000. Order-of-magnitude efficiency improvement brings practical quantum cryptography attack within reach.

Market positioning: Betting markets pricing quantum computers "within spitting distance of industrial scale" — suggesting commercial viability approaching faster than academic consensus.

Bitcoin honeypot thesis: [[Bitcoin]] and cryptocurrency represent "obvious honeypot" target for first practical quantum computer deployment — encrypted wallets containing hundreds of billions in value create immediate economic incentive.

Non-state actor threat: Key risk: non-state actor (criminal organization, rogue nation) could use quantum computer to drain crypto markets first, then publicly announce that encryption is broken — maximizing profit before revealing capability.

Bitcoin encryption history: Bitcoin community has migrated encryption schemes before in early days, proving technical adaptability. However, current quantum threat represents "big technological lift" requiring changes across:
- All wallet software
- Transaction flow processing
- Network validation nodes
- Consensus mechanisms

5-7 year window: Chamath's warning: "You have 5-7 years to get your shit in order." Timeline for crypto ecosystem to implement quantum-resistant cryptography before practical quantum computers become available.

Investment implications: Quantum computing advancement creates both opportunity (quantum companies, quantum-safe cryptography) and existential threat (current blockchain/crypto infrastructure vulnerable).

---

## Cluster validation

> [!success] Cluster status: validated — the tightest pure-narrative factor (June 2026)
> The four listed quantum pure-plays trade as one extremely tight, strengthening factor: [[IonQ]] (IONQ), [[Rigetti Computing]] (RGTI), [[D-Wave Quantum]] (QBTS) and [[Quantum Computing Inc]] (QUBT) intra-correlate 0.837 (weekly 0.833), PC1 87.8%, rejecting the independence, random-basket and vol-matched nulls all at the 0.0001 floor — the vol-matched pass is decisive given the extreme 97–112% annualized volatility: this is a real quantum factor, not just "high-vol names move together." It is ROBUST across thresholds (intact with zero contamination over [0.20, 0.40]) and STRENGTHENING out of sample (holdout ratio 1.16). Distinct on every axis: +0.188 vs unprofitable-growth (ARKK), +0.282 vs small-cap (IWM), +0.363 vs the market, and +0.589 vs the diversified quantum incumbent [[IBM]] — the big quantum player trades nothing like the pure-plays. The defining feature is the dramatic consolidation: intra-corr rose 0.23 (2022) → 0.47 → 0.50 → 0.70 → 0.87 (2026) as quantum became a defined thematic/ETF trade. See below.

This is the mirror image of [[GLP-1 receptor agonists#Cluster validation|GLP-1 / obesity]], the cleanest matched pair in the vault's cluster set. GLP-1 falsified (weekly correlation 0.004) because each name carries a dominant non-theme business — a pipeline, a franchise — that decouples it. The quantum pure-plays have no fundamental anchor at all: no commercialized revenue, nothing idiosyncratic to pull them apart. So they collapse onto a single axis and become the tightest factor in the set. The counterintuitive law the pair establishes: the absence of fundamentals is what lets a narrative cohere into a tradeable factor — a theme is a cluster precisely when its members have nothing else to trade on.

### Diagnostics summary

| Diagnostic | Value | Read |
|---|---|---|
| Intra-cluster corr (1Y) | 0.837 [0.797–0.897] | Among the tightest in the vault set; weekly 0.833 |
| PC1 explained variance | 87.8% | Near single-factor; equal loadings |
| Independence null p | 0.0001 | Series co-move |
| Random-basket null p | 0.0001 | Beats a random 4-pick at the floor |
| Vol-matched null p | 0.0001 | Real beyond shared (extreme) vol — the decisive pass |
| Holdout (2Y split) | STRENGTHENING 1.16 | Consolidating; loadings corr 0.54 |
| Threshold stable width | 0.20 [0.20–0.40] | ROBUST — zero contamination |
| Intra-adv vs growth (ARKK) | +0.188 | Distinct from unprofitable-growth beta |
| Intra-adv vs small-cap (IWM) | +0.282 | Distinct from small-cap beta |
| Intra-adv vs incumbent (IBM) | +0.589 | The diversified quantum incumbent trades separately |

1Y daily log returns through 2026-06-12, threshold 0.5. All US-listed (synchronous). RGTI/QBTS are 2022 de-SPACs; the 1Y window is well after both deals, so price history is clean. Config: `scripts/cluster_configs/quantum_computing.yaml`; registry row 2026-06-14. Terminology: [[Cohort, cluster, basket]].

### Boundary — a clean cluster, adjacent to risk-on growth

![[quantum-cluster-dendrogram-1y.png]]
*Hierarchical clustering at 0.5. The four quantum names form one tight cluster. At this loose cut they sit with the risk-on growth/small-cap complex (ARKK/IWM/SPY) — but the threshold scan shows they are intact and clean on their own across [0.20, 0.40]; ARKK/IWM/SPY only join at 0.45+. [[IBM]] sits entirely apart. The cohort is a distinct quantum factor adjacent to, but separable from, unprofitable-growth beta.*

The threshold scan is ROBUST: the four names are a single intact cluster with zero contamination from 0.20 to 0.40, and only at 0.45 — a loose cut for a cohort whose internal correlation is 0.84 — do the growth/small-cap/market ETFs join. The quantum cohort is its own factor, with risk-on growth as its nearest neighbor.

### Topology — four interchangeable lottery tickets

| Join step | Names | Distance (1-\|corr\|) | Read |
|---|---|---|---|
| 1 | RGTI + QBTS | 0.103 | Tightest pair (corr 0.90) |
| 2 | QUBT + (RGTI+QBTS) | 0.163 | The photonic micro-cap joins inside the cluster |
| 3 | IONQ + rest | 0.182 | The anchor pure-play closes the cohort |

All four names join below distance 0.182 (correlation above 0.82) — there is no core-and-satellite structure, just four interchangeable expressions of one trade. That [[Quantum Computing Inc]], the smallest and least-fundamentally-grounded name, sits fully inside the cluster (joins at 0.163) is the clearest evidence the cohort is a sentiment factor, not a fundamentals one.

### PC1 index weights

![[quantum-cluster-pca-1y.png]]
*PCA on the cohort. PC1 explains 87.8% with near-identical loadings (0.49–0.51) — a clean, equal-weighted single factor. Note the volatilities: 97–112% annualized, the highest-beta cohort in the vault set.*

| Ticker | PC1 loading | Loading weight | Ann vol | Raw PC1-mimic weight |
|---|---|---|---|---|
| IonQ (IONQ) | 0.491 | 24.6% | 96.9% | 26.7% |
| Rigetti (RGTI) | 0.508 | 25.4% | 110.4% | 24.3% |
| D-Wave (QBTS) | 0.507 | 25.4% | 112.4% | 23.8% |
| QCI (QUBT) | 0.494 | 24.7% | 103.0% | 25.3% |

Loadings and vols are so uniform that the PC1-mimic basket is essentially equal-weighted — there is no calm anchor and no dominant name. The whole cohort is one extreme-volatility quantum-sentiment bet.

### Distinctness

![[quantum-cluster-correlation-1y.png]]
*1Y pairwise correlation heatmap. The quantum block is uniformly hot (0.80–0.90). It is warm against ARKK (shared risk-on/unprofitable-growth DNA) but distinctly cooler against [[IBM]] and the broad market — a quantum factor on top of growth beta.*

The cohort is distinct from its nearest neighbor (unprofitable growth, +0.188 vs ARKK) and overwhelmingly distinct from the diversified incumbent (+0.589 vs [[IBM]]). The investable read: this is a quantum-sentiment factor, more concentrated than ARKK and entirely separate from the way the big-tech quantum players ([[IBM]], [[Google]], [[Microsoft]]) trade.

### Historical tightness evolution

![[quantum-cluster-rolling-tightness-90d.png]]
*Rolling 90-day cohesion, 2022–2026. A textbook consolidation: from barely-correlated post-SPAC names (0.23 in 2022) to a near-single stock (0.87 in 2026, PC1 90%) as quantum became a defined thematic/ETF/retail trade and basket-level flows came to dominate single-name news.*

| Window | Avg intra-corr | PC1 | Final join distance |
|---|---|---|---|
| 2022 | 0.229 | 43.3% | 0.860 |
| 2023 | 0.474 | 60.7% | 0.570 |
| 2024 | 0.503 | 62.8% | 0.543 |
| 2025 | 0.698 | 77.6% | 0.383 |
| 2026 | 0.872 | 90.4% | 0.157 |

*Strengthening, not durable-yet: the cohort has tightened every year and is now nearly a single stock, the signature of institutional/retail basket formation rather than a long-standing structural factor. The risk is symmetric — a thematic momentum unwind would hit all four identically.*

### The read-through

- Quantum is one trade, four ways. The pure-plays are interchangeable (all join below 0.18, equal PC1 loadings) — owning one is owning the cohort. There is no diversification within the basket; a quantum-sentiment move hits all four together.
- It is a real factor, not just growth beta. Distinct from ARKK (+0.188) and the market (+0.363), and a clean cluster at tight thresholds — the quantum names have their own sentiment factor on top of risk-on growth.
- The pure-plays are not the incumbents. +0.589 vs [[IBM]] — the listed quantum trade is the revenue-less pure-plays, which trade on narrative; the diversified players ([[IBM]], [[Google]], [[Microsoft]]) trade on their core businesses and are not part of the factor.
- Highest-beta, momentum-formed cohort in the set. At 97–112% vol and a 0.23 → 0.87 consolidation, this is a thematic-momentum basket — position sizing dominates, and the cohesion that makes it a clean factor also makes an unwind symmetric across all four names.

Method and terminology: `docs/cluster-validation.md`, [[Cohort, cluster, basket]], [[Vault cluster taxonomy]]. Post-definition OOS re-validation queued for the next quarterly pass (definition date 2026-06-14).

---

## Related

- [[Illinois Quantum and Microelectronics Park]] — major US infrastructure project
- [[Chicago Quantum Exchange]] — regional hub
- [[PsiQuantum]] — photonic, IQMP anchor
- [[Infleqtion]] — neutral atom, going public (INFQ)
- [[Pasqal]] — neutral atom, French
- [[Diraq]] — silicon spin, Australian
- [[Microsoft]] — player (topological qubits, Majorana 1)
- [[Google]] — player (superconducting, Willow)
- [[Amazon]] — player (Braket cloud platform)
- [[IBM]] — player (superconducting, IQMP partner)
- [[2026 Two Sessions]] — China quantum self-sufficiency push, dilution refrigerator independence
- [[Thermodynamic computing]] — adjacent physics-based probabilistic-computing concept
- Bluefors — Finnish dilution refrigerator market leader
- Oxford Instruments — [[UK]] cryogenics supplier

### Cross-vault
- [Technologies: Quantum Computing](obsidian://open?vault=technologies&file=Quantum%20Computing) — qubit architectures, error correction, decoherence challenges

