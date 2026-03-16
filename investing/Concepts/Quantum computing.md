#concept #quantum #technology

**Quantum computing** — next computing paradigm. Still pre-commercial but attracting significant investment. Multiple approaches competing, no clear winner.

---

## Why it matters for investors

| Factor | Status |
|--------|--------|
| Investment | Billions flowing (Microsoft, Google, [[IBM]], startups) |
| Timeline | Useful applications: 5-15 years (disputed) |
| Public plays | IonQ, Rigetti, D-Wave (all speculative) |
| Big tech exposure | Microsoft, Google, [[IBM]], Amazon (Braket) |
| Risk | High — scientific feasibility still debated for some approaches |

---

## Qubit approaches

| Approach | Players | Pros | Cons |
|----------|---------|------|------|
| **Superconducting** | [[IBM]], Google, Rigetti | Most mature, highest qubit counts | Error-prone, needs extreme cooling |
| **Trapped ion** | IonQ, [[Quantinuum]] | Lower error rates, longer coherence | Slower gate speeds, scaling challenges |
| **Topological** | Microsoft | Theoretically error-resistant | Unproven — MZMs not yet confirmed |
| **Photonic** | [[PsiQuantum]], Xanadu | Room temperature operation | Complex error correction |
| **Neutral atom** | QuEra, Atom Computing | Scalable, flexible | Early stage |
| **Quantum annealing** | D-Wave | Commercial today (optimization) | Not universal quantum computing |

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
| QuEra | Neutral atom | $100M+ | Harvard/MIT spinout |

### Going public

| Company | Approach | Valuation | Notes |
|---------|----------|-----------|-------|
| [[Infleqtion]] | Neutral atom | $1.8B | SPAC with Churchill Capital (INFQ), IQMP tenant |

---

## Dilution refrigerators — the hidden chokepoint

Superconducting qubits (the approach used by [[Google]], [[IBM]], Rigetti, and most quantum computers) only work at temperatures near absolute zero — around **10-15 millikelvin** (-459.67°F), colder than outer space. At any warmer temperature, thermal noise destroys fragile quantum states. The dilution refrigerator is the machine that makes this possible.

### How they work

A dilution refrigerator uses two isotopes of helium — helium-3 (³He) and helium-4 (⁴He) — mixed together. When helium-3 "dilutes" into helium-4, it absorbs heat at the quantum mechanical level (analogous to how evaporation cools skin, but at atomic scale). By cycling this process, the fridge extracts heat until reaching millikelvin temperatures. The quantum processor sits at the very bottom of the refrigerator — inside the iconic chandelier-like structures seen in quantum lab photos.

### Supply chain

| Supplier | Country | Notes |
|----------|---------|-------|
| **Bluefors** | Finland | Market leader, supplies Google, IBM |
| **Oxford Instruments** | UK | Legacy cryogenics maker |
| **Leiden Cryogenics** | Netherlands | Smaller specialist |

Each unit costs **$1-5M+**, takes months to build, and requires helium-3 — a rare isotope primarily sourced from nuclear weapons tritium decay. Global helium-3 supply is constrained (~30,000 liters/year, mostly from US and Russian weapons programs). This makes dilution refrigerators both expensive and geopolitically sensitive.

### Why it's a chokepoint

Every superconducting quantum computer needs one. When the US banned dilution refrigerator exports to [[China]], it targeted the physical foundation of China's quantum program. Without these machines, superconducting qubits can't operate — period.

**China's response:** Pan Jianwei's team at the Chinese Academy of Sciences independently built domestic dilution refrigerators to international standards after the ban. These now power the **Zuchongzhi** quantum processor series. See [[2026 Two Sessions]] for context on China's broader self-sufficiency push.

**Analogy:** Banning dilution refrigerators to China is like banning [[ASML]] lithography to China's chip industry — except dilution refrigerators are less complex than EUV tools, making domestic replication more feasible. The fact that China achieved this relatively quickly validates the "bottleneck → springboard" pattern.

---

## Investment thesis considerations

**Bull case:**
- Quantum advantage for drug discovery, materials, optimization, cryptography
- Whoever wins captures massive TAM
- Government funding (defense, national security)
- Could obsolete classical computing for specific workloads

**Bear case:**
- Timeline constantly pushed out ("10 years away" for 30 years)
- Error correction unsolved at scale
- Classical algorithms keep improving
- Most public pure-plays are cash-burning, pre-revenue
- Scientific feasibility still debated (Microsoft's topological approach)

**Realistic view:**
- Near-term: quantum as cloud service ([[IBM]], Amazon Braket) for experimentation
- Medium-term: hybrid classical-quantum for specific problems
- Long-term: fault-tolerant universal quantum computing (if achievable)

---

## Microsoft Majorana 1 (2025)

**Controversial topological approach:**

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

**Key quote:** "Fundamental physics does not respect the timelines set by big tech companies." — Henry Legg, University of St Andrews

**Investment read:** Microsoft's quantum bet is high-risk, high-reward. If topological qubits work, they leapfrog competitors. If not, years of investment wasted. Scientific consensus still skeptical.

---

## Illinois Quantum and Microelectronics Park (2025)

**Largest US quantum infrastructure project.** 128-acre campus in Chicago (former U.S. Steel South Works). $500M Illinois state funding.

| Tenant | Approach |
|--------|----------|
| [[PsiQuantum]] (anchor) | Photonic — building first US million-qubit system |
| [[IBM]] | Superconducting |
| [[Diraq]] | Silicon spin |
| [[Infleqtion]] | Neutral atom |
| [[Pasqal]] | Neutral atom |

Groundbreaking September 2025. Target completion 2028. Projected $20B+ economic impact.

**Significance:** Consolidates multiple quantum approaches in one location with government backing — could accelerate timelines if any approach achieves breakthrough.

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

At the [[2026 Two Sessions]], Pan Jianwei (Chinese Academy of Sciences) revealed that after the US banned dilution refrigerator exports to China, his team independently built domestic versions at international standards — now powering the **Zuchongzhi** quantum processor series.

This is the same "bottleneck → springboard" pattern seen in semiconductors ([[Huawei]] Kirin 9020, [[SMIC]] 7nm). The 15th Five-Year Plan (2026-2030) explicitly includes quantum technology commercialization as a priority, with deep integration of industry-academia-research.

**Implication:** Western quantum equipment exporters face the same long-term dynamic as semiconductor equipment makers — export controls create a protected market for Chinese domestic alternatives with state backing.

*Updated 2026-03-05*

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
- Bluefors — Finnish dilution refrigerator market leader
- Oxford Instruments — UK cryogenics supplier

### Cross-vault
- [Technologies: Quantum Computing](obsidian://open?vault=technologies&file=Quantum%20Computing) — qubit architectures, error correction, decoherence challenges

