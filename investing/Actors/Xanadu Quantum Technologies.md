---
aliases: [Xanadu, Xanadu Quantum, XNDU]
tags: [actor, company, quantum-computing, canada, ipo]
ticker: XNDU
exchange: Nasdaq / TSX
---

# Xanadu Quantum Technologies

Toronto-based photonic [[Quantum computing|quantum computing]] company that went public on March 27, 2026 via deSPAC merger with Crane Harbor Acquisition Corp., becoming the first pure-play photonic quantum computing company to trade publicly. Ticker XNDU on both [[Nasdaq]] and [[TSX]]. Implied valuation ~US$3.1B. The company's differentiator is using photons (light) instead of superconducting qubits, enabling room-temperature operation — no cryogenic cooling required. Founded 2016 by Christian Weedbrook (PhD physics, University of Queensland) in [[Toronto]].

The investment case rests on two questions: can photonic quantum computing scale to fault tolerance before superconducting approaches (pursued by [[Google]], [[IBM]], [[Microsoft]]) get there first, and does the room-temperature advantage translate into a meaningful cost and deployment moat? The company has ~260 employees, ~US$275M raised pre-IPO, and no revenue runway — this is a deep-tech bet on a 2029-2030 quantum data center timeline. The CAD$390M in potential [[Canada|Canadian]] and [[Ontario]] government support (Project OPTIMISM) is a substantial non-dilutive catalyst if it closes, but remains subject to due diligence.

---

## Quick stats

| Metric | Value |
|--------|-------|
| CEO | Christian Weedbrook (Founder) |
| HQ | [[Toronto]], [[Canada]] |
| Founded | 2016 |
| Employees | ~260 |
| Ticker | XNDU ([[Nasdaq]] / [[TSX]]) |
| IPO date | March 27, 2026 |
| IPO mechanism | deSPAC (Crane Harbor Acquisition Corp.) |
| Implied valuation | ~US$3.1B |
| IPO proceeds | ~US$302M |
| Gov't support | Up to CAD$390M (Project OPTIMISM, pending) |
| Total pre-IPO funding | ~US$275M |
| Approach | Photonic quantum computing (room temperature) |
| Key software | PennyLane (open-source quantum ML library) |
| DARPA | Stage B of Quantum Benchmarking Initiative ($15M) |

---

## Funding rounds

| Date | Round | Amount | Lead / Key Investors | Notes |
|------|-------|--------|---------------------|-------|
| May 2018 | Seed | CAD$9M | [[OMERS]] Ventures | Golden Ventures, Real Ventures |
| Jun 2019 | Series A | CAD$32M | [[Bessemer Venture Partners]] | |
| May 2021 | Series B | $100M | Bessemer Venture Partners | OMERS Ventures, [[Goldman Sachs]], [[In-Q-Tel]] |
| Nov 2022 | Series C | $100M | Georgian | Bessemer, BDC Capital. Valued at ~$1B (unicorn) |
| Nov 2025 | deSPAC announced | — | Crane Harbor Acquisition Corp. | Merger to go public |
| Mar 2026 | IPO (deSPAC close) | ~$302M | Public markets | Opened ~$14, closed $16.03 on day one |

The $302M IPO proceeds were lower than the initially targeted ~$500M due to SPAC redemptions — a common pattern in deSPAC transactions. [[In-Q-Tel]] (CIA's venture arm) participation in the Series B signals US intelligence community interest in the photonic approach.

---

## Technology

Xanadu's approach uses silicon photonics to build quantum processors that manipulate squeezed light states — encoding quantum information in photons rather than the electron-based superconducting qubits used by [[Google]] (Sycamore/Willow), [[IBM]] (Eagle/Heron), and others. Three structural advantages:

1. Room-temperature operation — no dilution refrigerators at millikelvin temperatures. Dramatically reduces infrastructure cost and enables deployment in conventional data center environments.
2. Modular and networkable — photonic qubits can be linked via standard fiber optic infrastructure, enabling distributed quantum computing architectures. The company's stated target: one million qubits through modular scaling.
3. Semiconductor compatibility — photonic chips can be fabricated using existing silicon processes, potentially enabling mass production through established foundries.

### Key milestones

| Date | Milestone |
|------|-----------|
| Sep 2020 | X8 photonic quantum processor — 8-mode, first public cloud access to photonic QC |
| Jun 2022 | Borealis — 216-mode squeezed-state processor, achieved quantum advantage in Gaussian boson sampling |
| Feb 2025 | Aurora prototype — first universal photonic quantum computer, 12 qubits |
| Jun 2025 | First on-chip error-resistant photonic qubit (GKP qubit on silicon nitride) |
| Nov 2025 | DARPA Quantum Benchmarking Initiative Stage B ($15M funding) |

The 2022 Borealis result was significant — it demonstrated quantum advantage (sampling from a probability distribution faster than classical supercomputers) but in a narrow, non-commercial task. The 2025 Aurora and GKP qubit milestones are the steps toward fault-tolerant, general-purpose quantum computing.

---

## Leadership

| Name | Role | Background |
|------|------|------------|
| Christian Weedbrook | CEO & Founder | PhD Physics (Queensland), postdoc U of T, Canada's Quantum Advisory Council |
| Nathan Killoran | CTO Software | PhD U of Waterloo, quantum ML |
| Zachary Vernon | CTO Hardware | PhD Physics (Maryland), quantum photonics |
| Rafal Janik | COO | Former [[Shopify]] |
| Marian Lim | VP Finance | Former [[Wattpad]]/[[WEBTOON]] |

---

## Competitive landscape

| Company | Approach | Qubits | Status | Key difference |
|---------|----------|--------|--------|----------------|
| **Xanadu** | Photonic (squeezed light) | 12 (Aurora) | Public (XNDU) | Room temp, fiber-networkable |
| [[PsiQuantum]] | Photonic (single photon) | Pre-prototype | Private ($750M raised) | Partnered with [[GlobalFoundries]] for fab |
| [[Google]] | Superconducting | 105 (Willow) | Division of Alphabet | Quantum error correction demo 2024 |
| [[IBM]] | Superconducting | 1,121 (Condor) | Division of IBM | Largest qubit count, Qiskit ecosystem |
| [[IonQ]] | Trapped ion | 36 (Forte) | Public (IONQ) | Higher gate fidelity, slower |
| [[Rigetti]] | Superconducting | 84 (Ankaa-3) | Public (RGTI) | Fabless + foundry model |
| [[Quantinuum]] | Trapped ion | 56 (H2) | Private ([[Honeywell]] + Cambridge) | Highest quantum volume claims |

The photonic vs superconducting debate is the central technology risk. Superconducting approaches have more qubits and larger ecosystems but face fundamental scaling challenges (cooling, error rates, interconnects). Photonic approaches are earlier but potentially more scalable if error correction works. [[PsiQuantum]] is the closest pure-play photonic competitor but uses a different photonic architecture (single photon vs Xanadu's squeezed light) and remains private.

---

## Partnerships

- [[Volkswagen]] — quantum ML for logistics (2020), battery materials simulation (2022)
- [[University of Toronto]] — founding research relationship, talent pipeline
- [[University of Maryland]] — research and education collaboration (Mar 2025)
- [[DARPA]] — Quantum Benchmarking Initiative Stage B (Nov 2025, $15M)
- Government of [[Canada]] / Government of [[Ontario]] — Project OPTIMISM (up to CAD$390M, pending)

---

## Evolution

2016: Christian Weedbrook founded Xanadu out of his postdoctoral research at the University of Toronto, betting on continuous-variable photonic quantum computing when the field was dominated by superconducting approaches. The thesis: photons don't need cooling, can travel through fiber optics, and can be manufactured on standard silicon chips. At the time, no one had built a working photonic quantum computer.

2018-2019: Seed (CAD$9M) and Series A (CAD$32M) funded the transition from lab to company. Team grew from a handful of physicists to 100+ employees. Xanadu released Strawberry Fields (2018) and PennyLane (2019) as open-source quantum software libraries — an ecosystem play modeled on how [[Google]] built TensorFlow to create a developer community before hardware was ready.

2020-2021: The X8 processor went live on cloud, giving anyone internet access to a photonic quantum computer for the first time. Series B ($100M, led by [[Bessemer Venture Partners]] with [[In-Q-Tel]] and [[Goldman Sachs]]) was the credentialing round — In-Q-Tel's participation meant the CIA's tech arm saw potential in photonic QC for national security applications.

2022: Two pivotal moments. Borealis demonstrated quantum advantage in boson sampling — the first time a photonic system outperformed classical computation. And the Series C at $1B valuation made Xanadu a unicorn. The team was now 200+ people.

2023-2024: Quiet building period. Advanced packaging and photonic chip integration R&D. PennyLane gained traction as the leading quantum ML framework. No major commercial revenue — this is still an R&D company burning through venture capital.

2025: The Aurora prototype (12 universal photonic qubits) and the first on-chip GKP error-resistant qubit were the proof-of-concept milestones for fault-tolerant photonic quantum computing. DARPA's Stage B selection ($15M) validated the technical approach at the highest level of US defense research. The deSPAC with Crane Harbor was announced in November — Weedbrook chose the SPAC route over a traditional $200M funding round because "generating cash that way can take years and Xanadu is in a race."

2026: IPO closed March 27. Shares opened ~$14, closed $16.03. The $302M in proceeds (less than the targeted $500M due to SPAC redemptions) funds the next 2-3 years of R&D toward the stated goal: a large-scale quantum data center by 2029. The company has zero commercial revenue — the entire valuation is a bet on technical milestones.

---

## Related

- [[Quantum computing]] — sector concept
- [[PsiQuantum]] — photonic competitor
- [[Google]] — superconducting competitor (Willow)
- [[IBM]] — superconducting competitor (Condor/Heron)
- [[IonQ]] — trapped ion, public comp
- [[Goldman Sachs]] — Series B investor
- [[In-Q-Tel]] — Series B investor (CIA venture arm)
- [[Bessemer Venture Partners]] — lead investor across multiple rounds
- [[SpaceX IPO 2026]] — concurrent mega-IPO theme

---

*Sources: [BestStartup Canada](https://beststartup.ca/xanadu-quantum-technologies-makes-historic-tsx-and-nasdaq-debut-canadas-biggest-startup-news-this-week/), [Quantum Zeitgeist](https://quantumzeitgeist.com/xanadu-quantum-computing-list-nasdaq/), [BNN Bloomberg](https://www.bnnbloomberg.ca/business/2026/03/27/quantum-computing-firm-xanadu-starts-trading-on-tsx/), [Grokipedia](https://grokipedia.com/page/Xanadu_Quantum_Technologies). Created 2026-03-29.*
