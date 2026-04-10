#concept #ai #infrastructure

**OpenAI Infrastructure Spend** — tracking [[OpenAI]]'s compute investment plans, infrastructure deals, and the gap between announced commitments and actual spend targets.

---

## Compute spend reset (Feb 20, 2026)

OpenAI told investors it's now targeting **~$600B in total compute spend by 2030**, down from the **$1.4T infrastructure commitment** touted by [[Sam Altman]] in late 2025.

| Metric | Previous | Revised |
|--------|----------|---------|
| Infrastructure target | $1.4T ("commitments") | **~$600B** (compute spend) |
| Timeline | Vague ("coming years") | **By 2030** |
| 2030 revenue forecast | Not disclosed | **$280B** |

**Key nuance:** The $1.4T included partner commitments ([[SoftBank]], [[Oracle]] for [[Stargate]]); the $600B is OpenAI's own compute spend (training + inference). Still a massive number but more grounded and directly tied to revenue projections.

The spending plan is meant to more directly tie to expected revenue growth — with $280B projected for 2030, split roughly equally between consumer ([[ChatGPT]]) and enterprise businesses. The implied compute-to-revenue ratio: ~2:1.

**CFO argument (Jan 2026):** Sarah Frier published blog claiming revenue tracks compute 1:1 — 10x revenue growth (2023–2025) alongside 9.5x compute growth. Implies more capital = more revenue. The $600B/$280B ratio suggests this relationship may not hold at scale.

*Source: CNBC, Feb 20, 2026.*

---

## Own data center plans abandoned (Mar 2026)

OpenAI scrapped plans to build and own data centers, pivoting to renting server capacity from [[Microsoft]] Azure, [[Amazon]] AWS, and [[Google]] Cloud. Per The Information, OpenAI had aimed to directly lease or own some data center campuses and develop large portions of [[Project Stargate]] itself. Two things killed the plan:

1. Financing: lenders would not back a company with $13.1B revenue, $13.5B H1 2025 net loss, and $1.4T in stated commitments. No specific banks named in reporting — sourcing is "struggled to secure backing from lenders" (CNBC, Mar 22) and "lenders refused to underwrite" (The Deep Dive, Mar 17).

2. Construction reality: [[Sam Altman]] at [[BlackRock]]'s US Infrastructure Summit (Mar 11): "Anything at this scale, it's just like so much stuff goes wrong." Cited severe weather at the Abilene campus that temporarily "brought things down," plus supply chain challenges and tight deadlines. Virginia Tech engineering professor Walid Saad noted 1 GW DCs take 3-10 years start to finish — permitting, power access, site selection, hardware delivery all introduce delays OpenAI cannot control.

IPO pressure compounded both: Daniel Newman (Futurum Group CEO) to CNBC: "The market wants to see OpenAI's revenues rolling at a pace in which the spending can be justified." The pivot is about Wall Street optics as much as financing — public market investors won't buy a company burning cash on physical infrastructure it has no track record building. [[Gartner]] analyst Arun Chandrasekaran: "They're starting to say, 'You know what, let's try to secure the capacity that we can from the providers that are willing to give us that capacity now.'"

OpenAI does not currently own any data centers and may not for the foreseeable future (CNBC, citing unnamed sources).

| Metric | Old plan | New reality |
|--------|----------|-------------|
| Approach | Build and own DCs | Rent from hyperscalers + JV partners |
| Achieved capacity (2025) | 1.9 GW | Available via JV partners |
| Financing | Self-funded + JV | Lenders refused; pivoting to opex |
| IPO readiness | Capital-intensive builder | Asset-light consumer of compute |

The pivot triggered a leadership overhaul. Sachin Katti (ex-[[Intel]] CTO/AI Officer, joined Nov 2025) now heads all infrastructure, reorganized into three groups: technical design, commercial partnerships, and facility operations. Keith Heyde (Director of Physical Infrastructure, the main advocate for in-house ownership) departed ahead of the restructuring. Three more infrastructure leaders — Peter Hoeschele, Shamez Hemani, Anuj Saharan — left together for the same unnamed startup (Apr 10, 2026). See [[OpenAI talent exodus]].

This is distinct from the [[Project Stargate]] JV, which continues: the Abilene 1.2 GW campus, the 4.5 GW Oracle contract ($300B lifetime), and the Wisconsin site are all proceeding under partner ownership. What was abandoned is OpenAI building and owning facilities as principal — a separate initiative from the JV. The net effect: OpenAI's $600B compute-spend target now flows entirely through Stargate JV partner-built facilities ([[Oracle]], [[Crusoe Energy]]), hyperscaler rental agreements (Azure, AWS, GCP), and dedicated inference deals ([[Cerebras]]). This reduces capital intensity but increases dependency on partners whose incentives may not always align.

---

## Stargate infrastructure

### UAE Stargate (per SemiAnalysis, Jan 2026)

| Metric | Value |
|--------|-------|
| Location | UAE |
| Power source | 4x [[Ansaldo Energia]] AE94.3 gas turbines |
| Gross capacity | 1.3GW |
| Derated capacity | **1GW** (desert heat penalty −23%) |
| Phase 1 | 200MW by YE2026 |
| Status | "Going well" |

**Key insight:** On-site gas turbines = [[BYOP]] (Bring Your Own Power). Desert heat derates capacity by 23%.

**Texas Abilene (contrast):** "GPUs not going BRRR" — UAE progressing faster than domestic site.

**Turbine supplier:** [[Ansaldo Energia]] (Italian)

---

## Cerebras compute deal (Jan 14, 2026)

| Metric | Value |
|--------|-------|
| Deal value | **$10B+** |
| Compute | 750 MW |
| Duration | 2026–2028 |
| Use case | Inference (especially coding) |

**Why [[Cerebras]]:**
- 15x faster responses than GPU-based systems
- [[Sam Altman]] was early Cerebras investor
- Diversifies away from [[NVIDIA]]/[[Microsoft]] dependency

**Cerebras CEO:** "Largest high-speed AI inference deployment in the world."

---

## Nvidia inference concerns (Feb 2026)

**[[Reuters]] exclusive (Feb 2):** OpenAI dissatisfied with some [[NVIDIA]] chips, actively seeking alternatives.

| Issue | Detail |
|-------|--------|
| Problem | Inference speed for specific workloads |
| Affected products | [[Codex]] (coding), agent-to-agent comms |
| Need | Faster "time to first token" |
| Target | ~10% of inference compute from alternatives |

**Chip requirements:**
- SRAM-heavy architecture (memory embedded on silicon)
- Traditional GPUs rely on external memory → slower fetch times
- Inference needs more memory bandwidth than training

**Alternatives explored:**

| Company | Status |
|---------|--------|
| [[AMD]] | GPUs purchased |
| [[Cerebras]] | Commercial deal signed (Jan 2026) |
| [[Groq]] | Talks shut down after [[NVIDIA]] acquisition |

**NVIDIA $100B deal — dead (Mar 2026):**
The original Sep 2025 deal — $100B investment tied to deployment of 10 GW of NVIDIA systems — collapsed in stages:
- Nov 2025: NVIDIA quarterly filing disclosed the deal "may not come to fruition"
- Jan 2026: WSJ reported deal was "on ice"
- Feb 2026: NVIDIA filing said "no assurance" on investment and partnership agreement
- Mar 2026: [[Jensen Huang]] at conference said the $100B opportunity is "probably not in the cards"

What replaced it: NVIDIA invested $30B as part of the Feb 2026 mega-round — a standalone investment with no deployment milestones attached, distinct from the original deal structure. Huang called it "might be the last time" NVIDIA invests before OpenAI's IPO. OpenAI agreed to use 3 GW of dedicated inference capacity and 2 GW of training capacity on NVIDIA's forthcoming [[Rubin|Vera Rubin]] systems as part of the arrangement.

The earlier timeline for context:
- [[Jensen Huang]]: Investment "was never a commitment" (Bloomberg, Feb 2026)
- Huang: "There's no drama involved" (CNBC Feb 3)

**[[Sam Altman]] response (Feb 2):** Nvidia makes "the best AI chips in the world." OpenAI hopes to remain "gigantic customer for a very long time."

**[[NVIDIA]] defensive moves:**
- Acquired [[Groq]] IP for $20B (Dec 2025)
- Hired away Groq chip designers
- Non-exclusive licensing deal — Groq pivoting to cloud software

*Updated 2026-04-10*

---

## $100B+ mega-round (Feb 2026)

Largest private funding round in history. ~90% from strategic investors. First tranche closing by end of February.

| Investor | Amount | Status |
|----------|--------|--------|
| [[Amazon]] | Up to **$50B** | In talks |
| [[SoftBank]] | ~**$30B** | In talks (on top of prior $41B) |
| [[NVIDIA]] | Up to **$30B** | In talks |
| [[Microsoft]] | TBD | Expected |
| VCs + SWFs | TBD | Later tranche |

*Source: Bloomberg/CNBC, Feb 2026.*

$850B+ post-money ($730B pre-money). [[Amazon]] potentially contributing half the round — would make them a major OpenAI stakeholder alongside [[Microsoft]] and [[SoftBank]]. [[NVIDIA]] increasing from $250M (Oct 2024) to up to $30B signals deepening strategic ties despite inference chip tensions.

### Prior $50B Middle East round (Jan 2026)

| Detail | Value |
|--------|-------|
| Raise | $50B+ |
| Valuation | $750–830B |
| Key investors | [[MGX]] (Abu Dhabi), other Gulf SWFs |
| Status | Superseded by $100B+ mega-round (Feb 2026) |

---

## Related

- [[OpenAI]] — parent actor
- [[Stargate]] — joint venture with [[SoftBank]]
- [[AI infrastructure financing]] — GW economics (1 GW = $10B funding)
- [[Cerebras]] — $10B+ inference compute deal
- [[NVIDIA]] — primary GPU supplier, inference tensions
- [[Ansaldo Energia]] — turbine supplier (UAE Stargate)
- [[BYOP]] — on-site power generation pattern
- [[Power constraints]] — grid gap context
- [[UAE Tech]] — Stargate UAE site (1GW)
- [[AI Infrastructure]] — sector hub
- [[Model lab economics]] — profitability analysis
