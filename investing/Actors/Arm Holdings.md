---
aliases: [ARM, Arm]
tags:
  - actor
  - ip
  - uk
  - semiconductor
  - ai-infrastructure
---

Arm Holdings is the invisible substrate of modern computing — the instruction set architecture inside every smartphone, most cloud CPUs, and an accelerating share of data centers, automotive systems, and robots. For 35 years it operated as a pure IP licensor, collecting royalties on 280B+ chips shipped without ever making one itself. On March 24, 2026, that changed: Arm announced the AGI CPU, its first in-house production silicon, targeting agentic AI data center workloads, with [[Meta]] as lead partner and [[TSMC]] fabricating on 3nm. The stock jumped 16% the next day.

---

## Synopsis

The questions that determine Arm's economic value are no longer about whether the architecture will win — it already did. The real questions are:

1. Can the AGI CPU deliver on a $15B revenue target by 2031 — nearly 4x the company's entire current revenue — without destroying the licensing relationships that underpin the existing business? Arm is now simultaneously supplier and competitor to [[Amazon]], [[Google]], [[Microsoft]], [[NVIDIA]], and [[Qualcomm]], all of whom design custom Arm-based server chips. The customer list for AGI CPU (Meta, [[OpenAI]], [[Cerebras]], [[Cloudflare]]) skews toward companies that lack in-house silicon teams, which is the intended wedge — but the tension is structural and permanent.

2. Does the shift from IP licensing to silicon sales change the margin structure in ways that hurt or help? The IP business runs at ~95% gross margins; Arm's CFO guided AGI CPU at ~50% gross margin. If management's $15B silicon revenue / $25B total revenue / $9 EPS by 2031 targets hold, the incremental $7.5B gross profit and $5B operating profit dwarf the margin compression concern. But execution risk is real — Arm has never manufactured, managed supply chains, or run OEM relationships at scale.

3. How durable is the architecture monopoly as [[RISC-V]] matures and [[China]] accelerates adoption of open-source alternatives? China is Arm's second-largest market (~19% of revenue) and the most motivated to de-risk from Arm dependency. Export control tightening and the messy Arm China JV history add geopolitical risk. RISC-V isn't a near-term threat in high-performance server silicon, but in IoT, embedded, and eventually edge inference, the erosion is real.

4. What is [[SoftBank]]'s endgame? [[Masayoshi Son]] owns 87% and chairs the board. SoftBank just acquired [[Ampere Computing]] for $6.5B (March 2025), creating a parallel Arm-based server chip asset. The combined portfolio — Arm IP + Arm AGI CPU silicon + Ampere server CPUs + Graphcore AI accelerators — positions SoftBank to control multiple layers of the AI compute stack. But SoftBank's history of overpaying and mismanaging portfolio synergies (WeWork, Sprint, Vision Fund I) makes execution the open question.

---

## Quick stats

| Metric | Value |
|--------|-------|
| Ticker | ARM (NASDAQ) |
| Market cap | ~$153B (pre-AGI CPU announcement, Mar 24) |
| Revenue (FY2025, ended Mar 31) | $4.01B |
| Revenue (TTM, Dec 2025) | ~$4.67B |
| Net income (FY2025) | $792M |
| Non-GAAP EPS (Q3 FY2026) | $0.43 |
| Employees | 8,330 |
| HQ | Cambridge, England, [[UK]] |
| CEO | Rene Haas (since Feb 2022) |
| Chairman | [[Masayoshi Son]] |
| Owner | [[SoftBank]] (~87%) |
| IPO | September 14, 2023 (NASDAQ, $54.5B valuation) |
| Cumulative chips shipped | 280B+ |

---

## Sector correlation

| Sector | ETF | Correlation |
|--------|-----|-------------|
| Technology | XLK | 0.81 |
| [[Semiconductors]] | SMH | 0.80 |
| Industrials | XLI | 0.72 |
| *S&P 500* | *SPY* | *0.78* |

ARM trades as a core Technology name (XLK r = 0.81).

---

## Charts

![[arm-90d.png]]

![[arm-vs-smh.png]]
*[[Semiconductors|SMH]]*

![[arm-fundamentals.png]]

---

## Revenue breakdown

Arm has two revenue streams, both derived from the same IP:

| Segment | Q3 FY2026 (Dec 2025) | YoY growth |
|---------|---------------------|------------|
| Royalty revenue | $737M | +27% |
| License & other revenue | $505M | +25% |
| Total | $1.24B | +26% |

| Fiscal year | Total revenue | Licensing | Royalty |
|-------------|--------------|-----------|--------|
| FY2023 (Mar 2023) | $2.68B | — | — |
| FY2024 (Mar 2024) | $3.23B | ~$1.68B | ~$1.55B |
| FY2025 (Mar 2025) | $4.01B | ~$1.72B | ~$2.29B |

Licensing revenue: one-time upfront payments when customers take an architecture license or CSS (Compute Subsystem) license. Lumpy, depends on deal timing.

Royalty revenue: per-chip payments on every processor shipped using Arm designs. Recurring, tied to end-market volumes. Growing faster as Armv9 and CSS adoption raises the per-chip royalty rate.

Annualized contract value (ACV) grew 28% YoY in Q3 FY2026, reflecting licensing momentum. Data center royalties grew triple digits YoY — the fastest-growing segment, driven by hyperscaler custom CPU ramps.

---

## The AGI CPU: strategic pivot to silicon (March 2026)

On March 24, 2026, Arm announced the AGI CPU at an event in San Francisco — the first production silicon in the company's 35-year history. This is the most significant strategic shift since SoftBank's acquisition.

The [[Arm AGI CPU]] is a 136-core Neoverse V3 data center CPU on [[TSMC]] 3nm, targeting [[Agentic AI]] inference. Co-developed with [[Meta]] as lead partner. 300W TDP, 2x performance per rack versus x86, 50% gross margin. Volume production H2 2026. Revenue target: $15B/yr by 2031 — nearly 4x Arm's entire current revenue. Customers include [[OpenAI]], [[Cerebras]], [[Cloudflare]], SAP, SK Telecom. 50+ ecosystem supporters. Citi called it the "most significant shift in the company's history."

See [[Arm AGI CPU]] for full specifications, competitive comparison, market discovery timeline, customer details, and the agentic AI thesis.

---

## Business model: the three layers

Post-AGI CPU, Arm operates at three distinct levels of the value chain:

### 1. IP licensing (original model)
Arm designs CPU architectures and licenses them as intellectual property. Customers take an architecture license (design their own cores) or a technology license (use Arm's pre-designed cores like Cortex or Neoverse). Upfront license fee + per-chip royalty. Asset-light, ~95% gross margins. This is how 280B+ chips got shipped.

### 2. Compute Subsystems (CSS)
Introduced more recently, CSS are pre-integrated, pre-verified subsystems that go beyond individual cores — they include interconnects, memory controllers, and system IP, reducing customer design time from years to months. CSS raises the per-chip royalty rate significantly versus bare IP licenses. 21 CSS licenses across 12 companies as of Q3 FY2026; five customers already shipping CSS-based chips. The top four Android OEMs ship CSS-powered devices. CSS is the structural royalty accelerator.

### 3. Production silicon (AGI CPU — new)
Arm now designs and sells complete chips, manufactured by [[TSMC]]. The customer buys a finished product, not IP. ~50% gross margins, but massive revenue potential. This competes directly with [[Intel]] (Xeon), [[AMD]] (EPYC), and indirectly with hyperscaler custom chips (Graviton, Axion, Cobalt, Grace).

---

## Evolution

The story of Arm is the story of a Cambridge research project that became the invisible monopoly of modern computing — and is now gambling that monopoly on becoming a chipmaker.

1990: Founded as Advanced RISC Machines Ltd, a joint venture between [[Apple]] ($3M investment), Acorn Computers, and VLSI Technology. Twelve engineers from Acorn. The original ARM processor had been designed for the Acorn Archimedes desktop computer, and [[Apple]] selected it for the Newton PDA. Robin Saxby recruited as first CEO. The name change from "Acorn RISC Machine" to "Advanced RISC Machines" happened at Apple's insistence — they didn't want a competitor's name in the JV.

1993–1998: First profitable year in 1993. The genius move was the licensing model: rather than competing with Intel on manufacturing, Arm licensed its designs and let others build. Silicon Valley office opened 1994. By 1998, renamed ARM Holdings and listed on both the London Stock Exchange and NASDAQ. Apple's stake had diluted to ~15% by early 1999.

1998–2007: The mobile explosion. ARM architecture became the default for mobile processors because of one characteristic: power efficiency. When Nokia, then Apple (iPhone, 2007), and the entire smartphone industry needed processors that wouldn't drain batteries, Arm was the only game. The per-chip royalties were small — fractions of a dollar — but the volume was enormous. By the late 2000s, ARM was in virtually every mobile phone on Earth.

2010–2016: Peak IP model. ARM expanded into automotive, IoT, and embedded while competitors tried and failed to break the mobile monopoly. Intel's Atom mobile push was a costly failure. The company generated steady, growing revenue with minimal capex — a pure IP business at scale. In July 2016, [[SoftBank]]'s [[Masayoshi Son]] offered £24.3B ($32B) to take the company private, a 43% premium. The deal closed September 2016. Son's thesis: ARM would be the brain of the IoT revolution, with a trillion connected devices.

2016–2020: The SoftBank era. Son installed new management with a mandate to grow headcount and capabilities aggressively, prioritizing expansion over profitability. In 2017, SoftBank transferred a 25% stake to the Vision Fund (investors included Saudi PIF). Arm China was partly sold to a Chinese consortium including state-linked investors — a decision that would later become a governance nightmare. Revenue grew modestly while headcount ballooned. The IoT vision underdelivered.

2020–2022: [[NVIDIA]] attempted acquisition. In September 2020, NVIDIA announced a $40B deal to buy Arm from [[SoftBank]]. It would have been the largest semiconductor acquisition ever. But the deal united an unlikely coalition of opponents: [[Google]], [[Microsoft]], [[Qualcomm]], and other Arm customers feared an NVIDIA-owned Arm would disadvantage them; the UK government raised national security concerns; the EU, UK CMA, and US FTC all launched competition investigations. The deal collapsed in February 2022. Meanwhile, the Arm China JV descended into chaos: CEO Allen Wu refused to leave after being fired, publicly declared the subsidiary's "independence," and the dispute dragged through Chinese courts for over two years before resolution in April 2022.

2022–2023: Post-NVIDIA reset. Rene Haas — a former NVIDIA exec who'd joined Arm in 2013 and risen to lead the IP Products Group — replaced Simon Segars as CEO on the same day the NVIDIA deal was officially called off (February 8, 2022). Haas pivoted strategy toward higher-value designs: Armv9 architecture with richer royalty structures, Neoverse for data centers, and Compute Subsystems (CSS) that bundle more value per chip. SoftBank bought back the 25% Vision Fund stake for ~$16B (valuing Arm at $64B), then IPO'd on September 14, 2023: $4.87B raised at a $54.5B valuation. SoftBank retained ~90% ownership.

2023–2025: The AI tailwind and the Neoverse bet. Arm's data center story accelerated dramatically. [[Amazon]]'s Graviton processors (Arm-based) proved that Arm could compete with x86 in the cloud — AWS reported the majority of new compute capacity added in 2025 was Graviton-powered. [[Google]] built Axion on Arm, [[Microsoft]] launched Cobalt, [[NVIDIA]] designed Grace and then Vera (88 cores). Neoverse deployments exceeded 1 billion cores. Arm targeted 50% data center CPU share among top hyperscalers. Armv9 and CSS raised royalty rates per chip, and data center royalties grew triple digits YoY. Revenue crossed $1B per quarter for the first time.

2025–2026: The silicon pivot. Behind the scenes, Arm had been developing its own chip since 2023. In July 2025, Arm signaled to investors it was investing in manufacturing, and hired key executives (including from [[Amazon]]'s AI team). On March 20, 2025, [[SoftBank]] announced the acquisition of [[Ampere Computing]] for $6.5B — adding another Arm-based server chip company (Oracle, Google, Microsoft, and others were Ampere customers). Then on March 24, 2026: the AGI CPU launch. First production silicon in 35 years. [[Meta]] as co-developer and lead customer. $15B revenue target. A $1 trillion addressable market claim. The stock jumped 16%.

---

## Competitive landscape

### Data center CPUs: the main battleground

| Player | Chip | Architecture | Status |
|--------|------|-------------|--------|
| [[Intel]] | Xeon (Sapphire Rapids, Emerald Rapids, Granite Rapids) | x86 | Incumbent, losing share but still dominant |
| [[AMD]] | EPYC (Genoa, Bergamo, Turin) | x86 | Taking share from Intel aggressively |
| [[Amazon]] | Graviton (v1–v4) | Arm (custom) | Dominant in AWS, majority of new capacity |
| [[Google]] | Axion | Arm (custom, Neoverse-based) | 30,000+ apps migrated to Arm |
| [[Microsoft]] | Cobalt 100/200 | Arm (Neoverse CSS-based) | Azure fleet deployment |
| [[NVIDIA]] | Grace / Vera CPU | Arm (custom) | Paired with GPUs in AI servers |
| [[Qualcomm]] | Orion (rumored server) | Arm (custom, Nuvia-derived) | Won Arm licensing lawsuit (Sept 2025) |
| [[Ampere Computing]] | AmpereOne / Aurora (512 cores) | Arm (Neoverse-based) | Acquired by [[SoftBank]] for $6.5B |
| Arm | AGI CPU | Arm (Neoverse V3) | First-party silicon, H2 2026 production |

The coopetition dynamic is the core tension. Every hyperscaler with a custom Arm chip program is technically a competitor to the AGI CPU — but also a customer of Arm's IP. AWS's James Hamilton endorsed the AGI CPU launch enthusiastically (celebrating the partnership), but AWS will keep building Graviton. The AGI CPU isn't aimed at AWS — it's aimed at everyone who isn't AWS.

### The coopetition problem

For 35 years, Arm's business model was beautifully conflict-free: design the architecture, license it to everyone, collect royalties, compete with nobody. The AGI CPU breaks that.

[[Amazon]], [[Google]], [[Microsoft]], and [[NVIDIA]] each spent hundreds of millions designing custom Arm-based server CPUs (Graviton, Axion, Cobalt, Grace/Vera). They did this partly because Arm didn't sell chips — Arm was the neutral Switzerland of computing. Now Arm is selling a finished chip that competes with those custom designs in the same data center racks.

The intended wedge is a different customer segment: companies that can't afford custom silicon. [[Meta]] doesn't have a CPU team. [[OpenAI]] doesn't. [[Cloudflare]] doesn't. SAP doesn't. These companies currently buy [[Intel]] Xeon or [[AMD]] EPYC. The AGI CPU gives them an Arm option without spending $500M+ and 3-4 years on custom design. Mohamed Awad: "It expands our market to include customers that were not interested in an IP model."

The tension is structural regardless of intent:

- [[Qualcomm]] already sued over licensing control — and won (Sept 2025). Arm's ability to enforce IP terms on custom designs is weakened. If Arm can't prevent Qualcomm from using Nuvia-derived cores, the architecture license gives less leverage than the market assumed.
- If the AGI CPU is genuinely 2x per rack versus x86, some hyperscalers will question why they're spending billions on custom designs when they could buy Arm's chip. The AGI CPU isn't aimed at AWS today — but competitive gravity pulls.
- Conversely, if hyperscalers feel threatened by a supplier competing downstream, they could accelerate [[RISC-V]] adoption to reduce Arm dependency. The licensing business depends on trust that Arm won't use customer roadmap visibility (gained through IP licensing) to compete in silicon — an information asymmetry that makes partners uncomfortable.
- AWS's James Hamilton publicly celebrated the AGI CPU launch. That's either genuine comfort that Graviton's lead is unassailable, or diplomatic positioning while AWS quietly evaluates alternatives. Either way, the relationship dynamics have permanently changed.

The $15B AGI CPU revenue target by 2031 essentially requires Arm to capture a massive share of the "everyone who isn't a hyperscaler" market — enterprises, mid-tier cloud providers, AI startups, telcos. If they stay in that lane, the licensing business is safe. If the AGI CPU starts winning deals that would have gone to Graviton or Axion, coopetition becomes actual competition — and the 280B+ chip royalty machine is at risk.

### Mobile: still the cash cow

Arm has a near-monopoly in mobile CPU IP. Every iPhone, every Android phone uses Arm architecture. The migration from Armv8 to Armv9 (and from bare IP to CSS) is raising royalty rates per chip, offsetting flat-to-declining unit volumes. The top four Android OEMs ship CSS-powered devices. This business generates the base revenue that funds everything else.

### Threats

[[RISC-V]]: Open-source ISA that eliminates royalties. [[China]] is the strongest adopter, motivated by geopolitical risk. RISC-V has gained traction in IoT, microcontrollers, and some embedded applications. Not yet competitive in high-performance server or mobile, where Arm's software ecosystem (billions of apps, developer tools, OS support) creates massive switching costs. But the long-term trajectory is erosion at the low end.

[[Intel]]/[[AMD]] x86: Still ~85% of data center CPUs. x86 has decades of enterprise software compatibility. But the performance-per-watt gap is structural — Arm claims 2x per rack versus x86. The agentic AI thesis (always-on inference, power-constrained) plays directly to Arm's efficiency advantage. Intel is simultaneously dealing with foundry losses and manufacturing challenges. AMD has been more competitive on performance but lacks Arm's efficiency story.

---

## The Qualcomm litigation

Arm sued [[Qualcomm]] in 2022 over Qualcomm's acquisition of Nuvia (a startup founded by former Apple chip architects). Arm claimed Qualcomm was using Nuvia's Arm architecture license without authorization after the acquisition. The dispute went to trial in December 2024: the jury found Qualcomm did not breach its Architecture License Agreement or Technology License Agreement, but deadlocked on whether Nuvia violated its original licenses. In September 2025, the court entered final judgment in Qualcomm's favor, dismissing all remaining claims. Qualcomm declared "complete victory." The loss underscored the limits of Arm's ability to control what licensees do with custom core designs — a vulnerability as more companies build custom Arm-based silicon.

---

## SoftBank relationship

[[SoftBank]] owns approximately 87% of Arm, making it the crown jewel of [[Masayoshi Son]]'s portfolio — 54.6% of SoftBank's NAV at one point. The small free float (~13%) contributes to ARM's extreme valuation multiples.

[[Masayoshi Son]] chairs Arm's board. The relationship is both an asset (deep pockets, strategic patience, willingness to fund the silicon pivot) and a risk (Son's track record includes massive value destruction at WeWork and Vision Fund I, and his willingness to use Arm shares as collateral for margin loans). A 40% decline in ARM stock would reportedly trigger margin call risk for SoftBank.

SoftBank-related technology licensing and design services contributed approximately $200M in Q3 FY2026 revenue — a material related-party revenue stream tied to Son's broader AI infrastructure ambitions (Stargate project, Ampere acquisition, Graphcore).

---

## Arm China

Arm China (安谋科技) is a semi-independent entity that licenses Arm's IP to Chinese customers. In 2018, [[SoftBank]] sold a majority stake to a Chinese consortium including China Investment Corp and Silk Road Fund. From 2020 to 2022, a governance crisis erupted when CEO Allen Wu refused to be dismissed, publicly declared independence, and the dispute dragged through Chinese courts. Wu was finally replaced in April 2022. Former key staff left to found Borui Jingxin, a competing chip design startup.

China accounts for approximately 19% of Arm's total revenue — the second-largest geographic market after the US. Export control escalation could disrupt this revenue stream, and China's aggressive [[RISC-V]] investment is partly motivated by reducing dependence on Arm.

---

## Geopolitics and export controls

Arm is UK-based (Cambridge) but US-influenced through its NASDAQ listing, American customer base, and [[SoftBank]] (Japan) ownership. This creates a complex jurisdictional position:

- US [[export controls]] could restrict Arm IP sales to Chinese entities, as they have for [[NVIDIA]] GPUs and advanced semiconductor equipment
- The Arm China JV adds a layer of complexity — it operates semi-independently and serves the Chinese market through its own structure
- UK government demonstrated willingness to intervene on national security grounds during the NVIDIA acquisition attempt
- Chinese companies are the most motivated RISC-V adopters precisely because of Arm dependency risk

---

## Valuation

| Metric | Value |
|--------|-------|
| Market cap (pre-AGI CPU, Mar 24) | ~$153B |
| Forward P/E (FY2026E) | ~66x |
| Forward P/E (FY2027E) | ~50x |
| Revenue (FY2025) | $4.01B |
| P/S (FY2025) | ~38x |
| Management 2031 targets | $25B revenue, $9 EPS |
| Implied 2031 P/E at current mcap | ~17x (on $9 EPS) |

The stock is priced for aggressive execution on the silicon strategy. At current prices, the market is implying significant confidence in the $25B / $9 EPS target. The 87% SoftBank ownership creates a thin float that amplifies moves in both directions.

---

## Financials

| Metric | FY2023 | FY2024 | FY2025 | TTM (Dec 2025) |
|--------|--------|--------|--------|----------------|
| Revenue | $2.68B | $3.23B | $4.01B | ~$4.67B |
| Operating income | — | — | $831M | — |
| Net income | — | — | $792M | — |
| Non-GAAP diluted EPS | — | — | — | ~$1.75 (street est.) |
| Total assets | — | — | $8.93B | — |
| Total equity | — | — | $6.84B | — |
| Employees | — | — | 8,330 | — |

*FY ends March 31. Revenue growth: +21% (FY2024), +24% (FY2025). Q3 FY2026 revenue $1.24B (+26% YoY), Q4 FY2026 guidance $1.47B (+/- $50M).*

Management 5-year targets (by ~2031): $25B revenue, $9 EPS — implying the IP business doubles and the AGI CPU silicon business adds ~$15B.

---

## Investment case

### Bull
- Near-monopoly in mobile CPU IP, expanding to servers/AI/automotive/robotics
- AGI CPU opens a $1T addressable market with committed customers (Meta, OpenAI)
- Agentic AI structurally favors CPUs over GPUs for inference orchestration
- CSS raising royalty rates per chip across all end markets
- Triple-digit data center royalty growth
- Every major AI trend — hyperscaler custom silicon, edge inference, robotics — runs on Arm
- [[SoftBank]] provides strategic capital for multi-generation silicon roadmap
- Software ecosystem moat (billions of apps, decades of developer tooling) is nearly impossible to replicate

### Bear
- Valuation extreme (~66x forward P/E, ~38x revenue)
- First-time silicon maker with zero manufacturing/supply chain experience
- Competing with own customers creates structural tension
- [[RISC-V]] long-term erosion in IoT, embedded, potentially edge
- China revenue (~19%) at geopolitical risk from export controls and RISC-V adoption
- [[SoftBank]] overhang: thin float, margin call risk, related-party revenue questions
- Qualcomm litigation loss shows limited ability to enforce IP control on custom designs
- $15B silicon revenue target by 2031 requires massive execution with no historical precedent

---

## Related

- [[SoftBank]] — parent company (~87%), [[Masayoshi Son]] chairs board
- [[Masayoshi Son]] — chairman, controls strategic direction
- [[Meta]] — AGI CPU lead partner and co-developer
- [[TSMC]] — fabricates AGI CPU on 3nm N3P
- [[Apple]] — co-founder (1990 JV), largest mobile customer (A-series, M-series)
- [[Qualcomm]] — customer (Snapdragon), won architecture license lawsuit (2025)
- [[NVIDIA]] — customer (Grace/Vera CPU), tried to acquire (2020, blocked)
- [[Amazon]] — customer (Graviton, majority of new AWS capacity)
- [[Google]] — customer (Axion, 30,000+ apps migrated)
- [[Microsoft]] — customer (Cobalt 100/200)
- [[AMD]] — x86 competitor (EPYC)
- [[Intel]] — x86 competitor (Xeon), foundry services ecosystem supporter
- [[OpenAI]] — AGI CPU customer
- [[Cerebras]] — AGI CPU customer
- [[Cloudflare]] — AGI CPU customer
- [[Ampere Computing]] — SoftBank-owned Arm server chip company ($6.5B acquisition)
- [[RISC-V]] — open-source ISA, long-term competitive threat
- [[Arm AGI CPU]] — first in-house production silicon (Product note)
- [[Agentic AI]] — key demand driver for AGI CPU
- [[Semiconductors]] — sector
- [[Export controls]] — [[China]] licensing risk
