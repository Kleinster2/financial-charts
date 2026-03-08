---
aliases: [integrated device manufacturing, IDM, integrated device manufacturer]
---
#concept #semiconductor #structure

**IDM model** — Integrated device manufacturing: designing and fabricating chips under one roof. A business model under structural pressure as fab economics demand utilization levels that single-company product lines can't sustain.

---

## Synthesis

The IDM model worked when a company's product portfolio could fill its fabs to 80–95% utilization. But leading-edge fabs now cost $20B+ to build and require massive ongoing opex. If the products aren't winning market share, the fab becomes a highly capitalized albatross — burning cash whether it runs or not. This isn't an execution problem; it's a structural business model problem. [[AMD]] faced it 15 years ago and spun out [[GlobalFoundries]]. [[Intel]] faces it now with [[Intel Foundry Services]]. The only way to sustain IDM at leading edge is to attract external (fabless) customers — which requires competitive process technology, design toolchains, and PDKs. Without that, you're subsidizing a factory with your own products.

---

## The economics problem

| Assumption | Requirement |
|------------|-------------|
| Leading-edge fab capex | $20B+ |
| Target utilization | 80–95% |
| Sustaining opex | Billions annually |
| Product volume needed | Enough to fill the fab |

If your products don't command enough market demand to fill the fab, you're stuck paying for idle capacity. The math doesn't work.

---

## Historical precedent: AMD → GlobalFoundries

[[AMD]] went through this exact transition ~2009:
- Couldn't sustain fab economics alongside [[Intel]]'s desktop/server dominance
- Spun off manufacturing into [[GlobalFoundries]] (with Abu Dhabi's Mubadala as investor)
- GlobalFoundries eventually abandoned leading-edge process development (7nm and below)
- AMD became fabless, now uses [[TSMC]] — and has thrived as a result

The lesson: spinning off the fab isn't failure. It's recognizing that design and manufacturing have different capital structures and competitive dynamics.

---

## Intel's current dilemma

[[Intel]] is the last major IDM attempting leading-edge logic:

- [[Intel Foundry Services]] exists to attract external customers
- But fabless companies need competitive toolchains, PDKs, and design ecosystem support
- [[Lip-Bu Tan]] (Intel CEO, 2025–) understands this from his [[Cadence]] and [[Celesta Capital]] background
- [[Sriram Viswanathan]] (Celesta co-founder, ex-Intel Capital): "Unless and until Intel creates the tool chains and makes it easy for fabless companies to use the leading edge process that the Intel fab creates, they're going to have a real problem relying on their existing products to go through the fab"

The chicken-and-egg: you need external customers to justify fab investment, but you need a compelling fab to attract external customers.

---

## Who remains IDM?

| Company | Status | Notes |
|---------|--------|-------|
| [[Intel]] | IDM (attempting foundry) | Leading-edge but struggling for external customers |
| [[Samsung]] | IDM + foundry | ~7% foundry share; yield issues at 3nm |
| [[Texas Instruments]] | IDM | Mature nodes; different economics |
| [[Infineon]] | IDM | Specialty; no leading-edge pressure |

[[TSMC]] proved the pure-play foundry model works. The question is whether any IDM can compete at the leading edge without transitioning to a foundry model.

---

## Related

- [[Intel]] — last major IDM at leading edge
- [[Intel Foundry Services]] — Intel's attempt to become a foundry
- [[AMD]] — former IDM, spun out fabs successfully
- [[GlobalFoundries]] — AMD's foundry spinoff
- [[TSMC]] — pure-play foundry model that IDMs compete against
- [[Samsung]] — IDM + foundry hybrid
- [[Foundry Wars]] — competitive dynamics
- [[Foundry monopoly consolidation]] — structural advantages of the leader
- [[Lip-Bu Tan]] — Intel CEO navigating the IDM challenge
- [[Celesta Capital]] — VC perspective on IDM sustainability
