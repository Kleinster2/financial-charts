#concept #ai #infrastructure

OpenAI Infrastructure Spend — tracking [[OpenAI]]'s compute investment plans, infrastructure deals, and the gap between announced commitments and actual spend targets.

---

## Stargate quietly abandoned as joint venture (FT, Apr 29, 2026)

By the end of April, the original Stargate joint-venture framing had effectively dissolved. The FT (Hammond, Morris, Keohane, Bradshaw — Apr 29) reported that OpenAI has replaced the JV structure with a series of bilateral deals struck opportunistically with [[Oracle]], [[Microsoft]], [[NVIDIA]], [[AMD]], [[Broadcom]], [[CoreWeave]], and [[Cerebras]] — at one point totaling more than $1tn in commitments, some since scaled back. A person involved in the buildout from the outset: "I don't know what 'Stargate' means at this point. I think it is a completely antiquated line right now." A person familiar with [[SoftBank]] thinking: "basically any compute that involves Softbank or Oracle can be Stargate" — the umbrella name now means whatever its users want it to mean.

The numbers underneath have continued to grow even as the JV emptied out:

| Metric | Original (Jan 2025) | Status (Apr 2026) |
|---|---|---|
| Capacity target | 10 GW | **>8 GW already secured** |
| Spend target | $500B by 2029 | **$600B+ by end-2030** |
| Structure | JV (OpenAI + Oracle + MGX + SoftBank) | Bilateral deals + hyperscaler rentals |
| Lead financier | [[SoftBank]] $40B+ commitment | Capital markets normalized; JV financing no longer necessary |

The story per the FT internal source: "We created enough demand in the market, and others came along, so we sidelined first party data centers." Translation: the JV was a financing innovation that solved supply-chain complexity and lender wariness, both of which eased once AI capex became investable on its own. The original problems — no credit rating, no operating history at infrastructure scale — were solved by the [[NVIDIA]]/[[Oracle]]/[[Microsoft]] ecosystem absorbing the capex onto their own balance sheets.

The reshuffles by site:
- **Abilene, TX**: OpenAI declined the Crusoe expansion ("expansion was at an insane price"); [[Microsoft]] took the ~700MW lease (better creditworthiness, per Crusoe sources)
- **Narvik, Norway**: OpenAI declined to lease from [[Nscale]] directly; now accessing via Microsoft Azure
- **UK NE England**: Project halted (OpenAI blamed UK regulation and energy costs; UK AI minister Kanishka Narayan blamed "the financing environment for OpenAI")
- **Michigan**: New cheaper option OpenAI moved to instead of Abilene expansion
- **Ohio**: SoftBank building own DCs; capacity may go to OpenAI via tender

The pattern: OpenAI walks from anything not creditworthy or not at the right price, and Microsoft picks up the residual capacity. The Microsoft cleanup function is durable — wherever OpenAI exits, Microsoft has stepped in. A person familiar with Microsoft's thinking told FT this "helps out those who are feeling let down and misled by OpenAI on projects." This signals two things: Microsoft's compute appetite is large enough to absorb OpenAI's leavings, and OpenAI's reputational cost for partner whiplash is now non-trivial.

**Anthropic capitulation.** [[Anthropic]] chief executive [[Dario Amodei]] — who had spent 2025 criticizing rivals for "gung-ho" infrastructure plans — signed off "hundreds of billions of dollars of spending on long-term capacity" this month, with power constraints starting to weigh on Claude's ability to meet demand. The Amodei capitulation removes the only frontier-lab framing AI infrastructure spend as imprudent. See [[Anthropic vs OpenAI compute race]].

**Market read-through (Apr 28).** A report that OpenAI had missed internal revenue and user-growth targets sent SoftBank, Oracle, and [[CoreWeave]] shares down — the cleanest market evidence that the buildout's beneficiaries are now priced as OpenAI counterparties, not standalone businesses. OpenAI responded that its business is "firing on all cylinders." See [[AI infrastructure financing risk]].

Denise Dresser, OpenAI chief revenue officer, in an April note to sales staff: "We saw the exponential compute curve earlier, acted on it faster, and now have a real structural advantage." The framing inverts the partner-complaint narrative — what looks like unreliability to [[Nscale]] and [[Crusoe Energy]] looks like optionality from inside OpenAI. The question for the coming quarters is whether [[Amazon]], [[Google]], [[Microsoft]], and [[Meta]] — which generate tens of billions in annual profit and can self-fund infrastructure — can outspend OpenAI on assets they own outright, while OpenAI runs a leaner balance sheet via hyperscaler rentals.

*Source: FT (Hammond, Morris, Keohane, Bradshaw — Apr 29, 2026)*

---

## Sized against the hyperscalers (Apr 2026)

The $600B OpenAI compute target needs to be read against the hyperscalers it now rents from. The Big 4 (AMZN, MSFT, GOOGL, META) committed $710B in 2026 capex alone after the Apr 29 Q1 print night — more than OpenAI's entire 5-year cumulative target in a single year.

![[openai-vs-hyperscaler-capex-2026.png]]
*OpenAI $600B 2026-2030 cumulative vs Big 4 hyperscaler 2026 single-year capex (AMZN $200B, MSFT $190B, GOOGL $185B, META $135B). Capex/revenue ratio in each bar shows the structural distinction: OpenAI commits at 30x revenue, hyperscalers at 0.3-0.8x. Source: FT Apr 29 2026 (OpenAI $600B); company Q1 2026 capex guides per [[Hyperscaler capex]] note. Revenue uses TTM est.*

| | OpenAI | Big 4 hyperscaler avg | Ratio |
|---|---|---|---|
| 2026 capex commitment | ~$120B (linear) | ~$177B (avg of $135-$200B) | OpenAI 0.7x |
| 5-year cumulative target | $600B | $3.5T+ implied | OpenAI 0.17x |
| Revenue (2025 exit ARR) | $20B | $362B avg | OpenAI 0.06x |
| Capex/revenue ratio | ~6x | ~0.5x | OpenAI 12x |

The hyperscalers can self-fund the buildout from operating cash flow — Apple-style. OpenAI cannot. That is the financing-gap concept compressed into a single chart: every dollar of OpenAI capex beyond the $122B Feb 2026 mega-round depends on debt markets staying open and the IPO clearing. The hyperscalers' $710B 2026 spend is a vote of confidence in AI demand; OpenAI's $600B 2026-2030 spend is a hostage to its own revenue trajectory. The FT Apr 28 counterparty selloff (SBG/ORCL/CRWV down on the OpenAI miss-targets report) is the market beginning to price that distinction. See [[AI infrastructure financing risk]] and [[Hyperscaler capex]].

---

## Compute spend reset (Feb 20, 2026)

OpenAI told investors it's now targeting ~$600B in total compute spend by 2030, down from the $1.4T infrastructure commitment touted by [[Sam Altman]] in late 2025.

| Metric | Previous | Revised |
|--------|----------|---------|
| Infrastructure target | $1.4T ("commitments") | ~$600B (compute spend) |
| Timeline | Vague ("coming years") | By 2030 |
| 2030 revenue forecast | Not disclosed | $280B |

Key nuance: The $1.4T included partner commitments ([[SoftBank]], [[Oracle]] for [[Stargate]]); the $600B is OpenAI's own compute spend (training + inference). Still a massive number but more grounded and directly tied to revenue projections.

The spending plan is meant to more directly tie to expected revenue growth — with $280B projected for 2030, split roughly equally between consumer ([[ChatGPT]]) and enterprise businesses. The implied compute-to-revenue ratio: ~2:1.

CFO argument (Jan 2026): Sarah Frier published blog claiming revenue tracks compute 1:1 — 10x revenue growth (2023–2025) alongside 9.5x compute growth. Implies more capital = more revenue. The $600B/$280B ratio suggests this relationship may not hold at scale.

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
| Derated capacity | 1GW (desert heat penalty −23%) |
| Phase 1 | 200MW by YE2026 |
| Status | "Going well" |

Key insight: On-site gas turbines = [[BYOP]] (Bring Your Own Power). Desert heat derates capacity by 23%.

Texas Abilene (contrast): "GPUs not going BRRR" — UAE progressing faster than domestic site.

Turbine supplier: [[Ansaldo Energia]] (Italian)

---

## Cerebras compute deal (Jan 14, 2026)

| Metric | Value |
|--------|-------|
| Deal value | $10B+ |
| Compute | 750 MW |
| Duration | 2026–2028 |
| Use case | Inference (especially coding) |

Why [[Cerebras]]:
- 15x faster responses than GPU-based systems
- [[Sam Altman]] was early Cerebras investor
- Diversifies away from [[NVIDIA]]/[[Microsoft]] dependency

Cerebras CEO: "Largest high-speed AI inference deployment in the world."

Apr 17, 2026 update: What looked in January like a targeted diversification deal had become, by the time of Cerebras's renewed filing, a much larger forward-demand pillar. Reuters reported the commitment had expanded to more than $20B over three years, with potential total spend near $30B, while the filing also made clear that none of this relationship contributed recognized 2025 revenue yet. See [[Cerebras IPO revival April 2026]].

---

## Deployment Company (May 2026)

OpenAI's May 11 launch of The OpenAI Deployment Company is not a compute-spend item in the narrow sense, but it is the clearest answer so far to the compute-monetization question. The platform is meant to embed forward-deployed engineers into enterprises, redesign workflows around AI, and convert pilots into durable systems. [[Brookfield]] agreed to invest $500M; Axios reported a $14B post-money valuation frame.

Why it belongs here: OpenAI's infrastructure spend only works if the company can turn compute into revenue and customer productivity fast enough. The Deployment Company is a services-led bridge from model capacity to enterprise adoption. It also gives OpenAI and private-equity partners a channel to monetize AI transformation across portfolio companies rather than waiting for organic SaaS-style adoption.

See [[Brookfield OpenAI deployment platform May 2026]] for deal structure and investor read-through.

---

## Nvidia inference concerns (Feb 2026)

[[Reuters]] exclusive (Feb 2): OpenAI dissatisfied with some [[NVIDIA]] chips, actively seeking alternatives.

| Issue | Detail |
|-------|--------|
| Problem | Inference speed for specific workloads |
| Affected products | [[Codex]] (coding), agent-to-agent comms |
| Need | Faster "time to first token" |
| Target | ~10% of inference compute from alternatives |

Chip requirements:
- SRAM-heavy architecture (memory embedded on silicon)
- Traditional GPUs rely on external memory → slower fetch times
- Inference needs more memory bandwidth than training

Alternatives explored:

| Company | Status |
|---------|--------|
| [[AMD]] | GPUs purchased |
| [[Cerebras]] | Commercial deal signed (Jan 2026) |
| [[Groq]] | Talks shut down after [[NVIDIA]] acquisition |

NVIDIA $100B deal — dead (Mar 2026):
The original Sep 2025 deal — $100B investment tied to deployment of 10 GW of NVIDIA systems — collapsed in stages:
- Nov 2025: NVIDIA quarterly filing disclosed the deal "may not come to fruition"
- Jan 2026: WSJ reported deal was "on ice"
- Feb 2026: NVIDIA filing said "no assurance" on investment and partnership agreement
- Mar 2026: [[Jensen Huang]] at conference said the $100B opportunity is "probably not in the cards"

What replaced it: NVIDIA invested $30B as part of the Feb 2026 mega-round — a standalone investment with no deployment milestones attached, distinct from the original deal structure. Huang called it "might be the last time" NVIDIA invests before OpenAI's IPO. OpenAI agreed to use 3 GW of dedicated inference capacity and 2 GW of training capacity on NVIDIA's forthcoming [[Rubin|Vera Rubin]] systems as part of the arrangement.

The earlier timeline for context:
- [[Jensen Huang]]: Investment "was never a commitment" (Bloomberg, Feb 2026)
- Huang: "There's no drama involved" (CNBC Feb 3)

[[Sam Altman]] response (Feb 2): Nvidia makes "the best AI chips in the world." OpenAI hopes to remain "gigantic customer for a very long time."

[[NVIDIA]] defensive moves:
- Acquired [[Groq]] IP for $20B (Dec 2025)
- Hired away Groq chip designers
- Non-exclusive licensing deal — Groq pivoting to cloud software

*Updated 2026-05-12 with FT Apr 29 reframing and hyperscaler-capex sizing chart*

---

## $100B+ mega-round (Feb 2026)

Largest private funding round in history. ~90% from strategic investors. First tranche closing by end of February.

| Investor | Amount | Status |
|----------|--------|--------|
| [[Amazon]] | Up to $50B | In talks |
| [[SoftBank]] | ~$30B | In talks (on top of prior $41B) |
| [[NVIDIA]] | Up to $30B | In talks |
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
