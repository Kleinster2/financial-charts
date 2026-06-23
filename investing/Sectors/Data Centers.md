---
aliases:
  - Datacenters
  - Data centre
  - Colocation
  - Data center infrastructure
  - data centers
  - data center
---
#sector #datacenter #reit #infrastructure #ai

# Data Centers

> [!info] Industry Overview
> This is an industry overview, not a tradeable sector. The validated trading clusters are [[DC REITs]] (0.69) and [[Crypto-to-AI]] (0.61).

Physical infrastructure for cloud computing and AI — colocation, hyperscale, GPU clouds, power/cooling.

---

## Sector performance

![[data-centers-performance.png]]
*Normalized total return since Jan 2024 (log scale). The two data-center REITs [[Equinix|EQIX]]/[[Digital Realty|DLR]] hug [[SPY]] near the bottom (modest, rate-sensitive returns) while the crypto-to-AI names [[Core Scientific|CORZ]]/[[IREN]]/[[TeraWulf|WULF]] run +600–1900%. The "data center" label does not trade as one factor: the 0.39 sector-wide correlation splits into [[DC REITs]] (0.69) and [[Crypto-to-AI]] (0.61), which barely correlate with each other (0.08–0.20). That split is why this is an industry overview, not a tradeable sector — the factor lives in the sub-cohorts.*

---

## Market overview

| Segment | 2025 market | Growth | Key players |
|---------|-------------|--------|-------------|
| Colocation/wholesale | ~$60B | 15%+ CAGR | [[Equinix]], [[Digital Realty]] |
| Hyperscale (owned) | ~$200B capex | 30%+ CAGR | AWS, Azure, GCP |
| GPU cloud (neocloud) | ~$10B | 50%+ CAGR | [[CoreWeave]], [[Lambda Labs]] |
| Cooling/power | ~$15B | 20%+ CAGR | [[Vertiv]], [[Schneider Electric]] |

Total addressable market: $500B+ by 2030 (AI-driven)

---

## Market segments

### Colocation REITs

| Company | Market cap | Focus | AI relevance |
|---------|------------|-------|--------------|
| [[Equinix]] | ~$105B | Interconnection | Moderate (enterprise) |
| [[Digital Realty]] | ~$66B | Wholesale hyperscale | High (AI workloads) |
| CoreSite | (Owned by [[American Tower]]) | US interconnection | Moderate |
| [[CyrusOne]] | (Owned by [[KKR]]) | Enterprise | Moderate |
| [[QTS Data Centers]] | (Owned by [[Blackstone]]) | Hyperscale | Dominant |

Business model: Long-term leases, inflation escalators, 60-70% gross margins.

### Private capital ownership

Major platforms now owned by private capital. See [[Private Real Estate]] for investment detail.

| Platform | Owner | Notes |
|----------|-------|-------|
| [[QTS Data Centers]] | [[Blackstone]] | 70+ facilities, 2+ GW, $25B+ pipeline |
| [[CyrusOne]] | [[KKR]] | 50+ facilities |
| Related Digital | [[Related Companies]] | New platform (2025) |

### GPU clouds (Neoclouds)

| Company | Status | Customers | Risk |
|---------|--------|-----------|------|
| [[CoreWeave]] | Public (CRWV) | Microsoft (65%) | High concentration |
| [[Nebius]] | Public (NBIS) | Microsoft, Meta | Strategic-equity funded |
| [[Lambda Labs]] | Private | AI startups | Smaller scale |
| [[Crusoe Energy]] | Private | Stranded gas model | Unusual cost structure |
| [[Voltage Park]] | Private | [[Foundation Capital]] | Emerging |

The thesis is simple — fill the GPU demand hyperscalers cannot meet — but the financing structure is where the risk lives, and it is the most-debated fragility in the AI-infrastructure complex. Neoclouds are funded by a stack of [[NVIDIA]] strategic equity, customer-contract backlog, and private credit collateralized by the GPUs themselves ([[CoreWeave]]'s March 2026 $8.5B term loan was anchored by [[Blackstone]] credit). That carries two tail risks the colocation REITs do not. First, concentration: CoreWeave draws ~65% of revenue from [[Microsoft]], so the equity is effectively a single-customer credit (its CDS has traded near 773 bps, ~42% implied default). Second, the circularity that [[Neocloud financing]] turns on — NVIDIA both supplies and finances the buyers that help it hit quarterly numbers, so neocloud bookings are a weaker demand signal than they look ("real demand or orchestrated demand"). GPU depreciation compounds both: the collateral is a fast-aging asset. Bull case, the hyperscaler shortfall is durable; bear case, one customer loss or one Nvidia-allocation shift cracks a highly-levered, single-asset balance sheet. See [[Neocloud financing]].

### Crypto-to-AI pivots

| Company | Ticker | Pivot status |
|---------|--------|--------------|
| [[Core Scientific]] | CORZ | 12-yr CoreWeave hosting deal; $9B CoreWeave buyout rejected by holders (Oct 2025) |
| [[Hut 8]] | HUT | AI + BTC hybrid |
| [[IREN]] | IREN | Expanding AI |
| [[Bitdeer]] | BTDR | NVIDIA deal |
| [[TeraWulf]] | WULF | AI hosting |
| [[Cipher Mining]] | CIFR | AI expansion |

[[Core Scientific]] is the cautionary tale: [[CoreWeave]] agreed in July 2025 to acquire it in an all-stock deal (~$9B), but Core Scientific shareholders rejected the merger (20.8M for vs 203.5M against) and it was terminated October 30, 2025 — holders judged the all-stock terms undervalued the standalone AI-hosting buildout. The underlying 12-year, ~$3.5B [[CoreWeave]] hosting contract remains.

See [[Crypto-to-AI pivot]] for full analysis.

### Hyperscaler-owned

| Hyperscaler | 2026 capex (guidance) | 2025 capex | Focus |
|-------------|------------------------|------------|-------|
| [[Amazon]] AWS | ~$200B | ~$125B | AI/cloud |
| [[Google]] GCP | ~$175–185B | ~$91B | AI/cloud |
| [[Meta]] | ~$115–135B | ~$72B | AI training |
| [[Microsoft]] Azure | ~$110–120B | ~$90B | AI/cloud |
| [[Oracle]] | ~$50B (FY26) | ~$21B (FY25) | Catching up fast (OCI) |

Big-four combined 2026 capex guidance is ~$725B, up 77% from ~$410B in 2025, with roughly 75% of it (~$450B) AI-specific — GPUs, data centers, and power. Hyperscalers building own vs leasing. See [[AI hyperscalers]].

---

## The capex / insourcing loop

The ~$725B of 2026 hyperscaler capex is the single number that prices most of this sector — but it cuts in opposite directions depending on where in the stack you sit, and the tables above hold both halves without connecting them:

- Mixed for the wholesale REITs. Every dollar a hyperscaler spends building its own capacity is a lease it does not sign. [[Digital Realty]] (wholesale/hyperscale) is the most exposed — its customers are the same hyperscalers now guiding to $100B+ each. [[Equinix]] is more insulated: its moat is interconnection and an enterprise base that hyperscalers do not replicate when they self-build. That difference is why the two carry different AI-relevance reads (DLR high, EQIX moderate) yet cohere only at 0.69 rather than tighter.
- The insourcing risk is capped by a power ceiling. Self-building is not clean substitution: the binding constraint is deliverable power, not capital (see [[Power constraints]] and the [[India]] read below). Hyperscalers build and lease at the same time because they cannot energize sites fast enough — so the REIT bear case is real but bounded by the same bottleneck that creates the boom.
- Unambiguously bullish for picks-and-shovels. [[Vertiv]], [[Schneider Electric]], and the power names ([[GE Vernova]], [[Constellation Energy]], [[Vistra]]) sell into the capex no matter who wins build-vs-lease — hyperscaler-owned, REIT, and neocloud capacity all need the same UPS, liquid cooling, switchgear, and electrons. That agnosticism makes the cooling/power cohort the cleanest expression of the capex number itself.
- Binary for the neoclouds. [[CoreWeave]] and the GPU clouds are both customers of this capex and competitors for it — a levered bet that the hyperscaler shortfall persists long enough to service GPU-collateralized debt. See [[Neocloud financing]].

The through-line the catalog otherwise misses: the capex number is bullish for power and cooling, mixed for the REITs (insourcing risk against a power ceiling that forces leasing anyway), and binary for the neoclouds. "Long data centers" has to say which.

---

## Geographic hubs

| Hub | Significance |
|-----|--------------|
| [[Ashburn]] (Virginia) | 70% of US internet traffic |
| [[Dallas Data Hub]] | Low power costs, growing |
| [[Phoenix Data Hub]] | Land, power availability |
| [[Columbus Ohio]] | Midwest hub, Intel investment |
| [[São Paulo Data Hub]] | LatAm leader |
| [[Rio de Janeiro Data Hub]] | Rio AI City (3.2GW) |
| [[Querétaro]] (Mexico) | ~65% of Mexican capacity; nearshoring, water-stressed |
| [[Singapore Tech]] | Asia-Pacific hub |
| [[Malaysia]] (Johor) | Singapore overspill; top-3 APAC, ~2 GW by end-2026 |
| [[Japan]] (Tokyo / Osaka) | Top-3 APAC; hyperscaler-led, power/seismic-constrained |
| [[China]] (Beijing + western hubs) | [[East Data West Compute]]; chip-constrained, domestic accelerators |
| [[UAE]] (Abu Dhabi / Dubai) | Global #1–2 emerging DC markets; Stargate UAE (5 GW, $30B+) |
| [[Saudi Arabia]] | HUMAIN/DataVolt 6.4 GW pipeline; NEOM Oxagon (1.5 GW) |
| [[India]] | Fast-growing AI/data-center market where grid delivery and microgrids are the bottleneck |
| [[France]] | Nuclear-heavy grid and SoftBank/SB Energy 5 GW AI data-center plan (May 2026) |
| London | European financial hub |
| Frankfurt | European cloud hub |
| [[Ireland]] (Dublin) | ~22% of national power; 2021 grid moratorium, eased Dec 2025 |

---

## United States: the Stargate cluster

The US is the world's #1 market (the Northern Virginia hub around [[Ashburn]] runs ~20 GW), and its frontier is the [[Project Stargate]] build — though Stargate has become a brand more than a structure. The flagship is the 1.2 GW Abilene, Texas campus (450,000+ [[NVIDIA]] GB200s under a 15-year [[Oracle]] lease, [[Crusoe Energy]] developer); the planned expansion to 2 GW collapsed in March 2026 over OpenAI–Oracle demand-forecast disputes, and [[Microsoft]] leased the ~700 MW expansion site instead. By April 2026 the FT reported the $500B JV "effectively abandoned" in favor of bilateral OpenAI deals — yet the numbers underneath grew (>8 GW secured, $600B+ projected by 2030), with sites across Texas, Ohio, New Mexico, Wisconsin, and a 1 GW Michigan campus. It is the capex/insourcing loop in one program: the JV was a financing innovation that became unnecessary once capital markets normalized around AI infrastructure, leaving the build to [[Oracle]], hyperscaler rentals, and the picks-and-shovels suppliers.

---

## India

[[Asia Tech Lens]]' May 2026 India grid-risk piece makes the sector point cleanly: data-center demand can grow faster than usable, site-level power. The country has strong hyperscaler demand, Google Vizag, Microsoft Hyderabad, Amazon investment plans, AdaniConneX, Nxtra, and Yotta, but the bottleneck is deliverable 24/7 power rather than abstract national capacity.

The sector read is positive for operators and suppliers that can solve the bundle: grid interconnection, renewable PPAs, batteries, substations, backup generation, cooling, fiber, and local permitting. See [[India AI]], [[Power constraints]], and [[BYOP]].

---

## France

[[SoftBank]]'s May 2026 plan for 5 GW of French AI data centers turns France into the main European sovereign-AI power host to watch. It is a power-first siting thesis: nuclear baseload, grid access, [[Schneider Electric]]/[[EDF]] industrial partners, and state support are the asset.

---

## Gulf / Middle East

The Gulf is the geography this note most understates. By Cushman & Wakefield's 2025 ranking, Abu Dhabi and Dubai are the world's first- and second-fastest-growing data-center markets — ahead of every US and European hub — on a deliberate convergence of subsidized power, solar, sovereign capital, and a data-sovereignty pitch as the neutral host between the US and China. It is the global version of the sovereign-AI power thesis the France section only gestures at.

UAE — the sovereign-AI flagship. Stargate UAE (the Abu Dhabi node of [[Project Stargate]]) is a 5 GW, $30B+ campus with a 1 GW first compute cluster, built by [[Khazna Data Centers]] and run by [[OpenAI]] and [[Oracle]] on [[NVIDIA]] GB300, with [[SoftBank]] and [[Cisco]] — the largest AI build outside the US, first 200 MW targeting 2026. [[G42]] holds 60%, the structural signature of the model: sovereign infrastructure under national control. Separately, [[Microsoft]] and [[G42]] are adding another 200 MW through Khazna by end-2026 — Microsoft's 2024 $1.5B investment in [[G42]] is the chip-access enabler, the deal that moved G42 off Chinese vendors to qualify for US accelerators. [[Khazna Data Centers]] (a [[G42]] company; [[MGX]] and [[Silver Lake]] invested as e& exited) holds 70%+ of UAE/Middle East colocation. And [[MGX]] — the [[Mubadala]]/[[G42]] sovereign-AI vehicle — is the same buyer in the [[Aligned Data Centers]] $40B deal above and a member of the AI Infrastructure Partnership, so Abu Dhabi capital sits on both sides of the global build.

Saudi Arabia — the fast follower. [[HUMAIN]], [[Saudi PIF]]'s ~$23B AI company (launched May 2025), is coordinating a 6.4 GW data-center pipeline with [[DataVolt]] on [[NVIDIA]]/[[AMD]] GPUs, first facilities targeting Q2 2026, with a stated aim of ~6% of global AI workload. [[NEOM]]'s Oxagon adds a $5B, 1.5 GW renewable AI campus (Red Sea seawater cooling, net-zero; phase-one 300 MW by 2028). HUMAIN raised up to $1.2B to fund the expansion.

The hinge is export control. The entire Gulf build runs on US accelerators, so it is contingent on the chip-access framework — the 2025 US–Gulf AI agreements and [[G42]]'s divestment from Chinese tech. Tighter controls compress it; the current opening is what unlocked Stargate UAE. See [[Project Stargate]] and [[US-China decoupling]]; for the chip-diplomacy framing, the geopolitics vault's [American AI Export Program](obsidian://open?vault=geopolitics&file=Concepts%2FAmerican%20AI%20Export%20Program).

---

## Singapore & Johor

[[Singapore Tech|Singapore]] is the mature Asia-Pacific hub that throttled itself: a 2019–2022 moratorium on new data centers (land, power, and water limits) capped the city-state and pushed demand across the strait to [[Malaysia]]'s Johor, now one of the top-three APAC markets alongside Tokyo and Beijing. Malaysia's capacity is set to more than double to ~2,055 MW by end-2026 (JLL). [[AirTrunk]] alone is building toward 700+ MW of IT load across four Malaysian campuses (~$6.8B committed); [[Equinix]], [[Vantage Data Centers]], Princeton Digital, Keppel, and Bridge are also in Johor. Singapore has since cracked the door — a December 2025 allocation call (DC-CFA2) for at least 200 MW, gated on 50%+ green power. The Johor overspill is the cleanest case of the note's power-and-land bottleneck routing capital to the next jurisdiction over.

---

## Ireland (Dublin)

Dublin is the cautionary European hub — where the note's power-constraint thesis already broke the market. Data centers reached ~22% of [[Ireland]]'s electricity in 2024 (the grid operator EirGrid forecasts 31% by 2034), and a 2021 grid-connection moratorium effectively froze new Dublin builds, with no new connections signaled possibly until 2028. A December 2025 regulator (CRU) decision reopened the door but on demanding terms for large (>10 MVA) loads: on-site generation sized to 100% of the connection, siting only in unconstrained locations, and 80% of annual demand matched by renewable investment in Ireland. It is the live preview of what other grids are approaching (see [[Power constraints]]), and a direct input to Europe's AI-sovereignty problem, since [[Ireland]] hosts much of the continent's hyperscale capacity.

---

## Japan

[[Japan]] is one of APAC's top-three data-center markets (with Johor and Beijing), anchored on Greater Tokyo (the Inzai corridor) and a secondary Osaka hub. Demand is hyperscaler-led — [[Google]], [[Microsoft]], [[Amazon]], and [[Oracle]] have all committed multi-billion-dollar Japan buildouts — while domestic players (NTT, KDDI/Telehouse) and [[AirTrunk]] supply capacity. The constraints are Japan-specific: a power system still rebalancing after the post-Fukushima nuclear pullback, high land costs, and seismic siting. The marquee move is [[SoftBank]]'s conversion of a former Sharp LCD plant at Sakai into an AI data center — old industrial sites with existing grid connections becoming the scarce asset, the same pattern as the US rust-belt builds.

---

## China

[[China]] builds on a different model: state-directed siting under [[East Data West Compute]] (东数西算), the 2022 plan that routes eastern data demand to compute hubs in the energy-rich west (Inner Mongolia, Gansu, Ningxia, Guizhou). The builders are the state telecoms — [[China Mobile]], [[China Telecom]], and [[China Unicom]] (which reported 45 EFLOPS in 2025) — alongside the cloud majors (Alibaba, Tencent). The binding constraint is silicon, not power or capital: US [[Export controls]] cap access to [[NVIDIA]]'s top parts, pushing the build onto domestic accelerators (Huawei Ascend) and making compute efficiency, not just capacity, the national priority. It is the one major DC geography largely walled off from the US-stack thesis running through the rest of this note.

---

## Brazil / Latin America

LatAm's largest DC market — two GW-scale "AI City" projects under development, all private. Beyond Brazil, [[Querétaro]] is [[Mexico]]'s hub (~65% of national capacity, $10B+ committed — AWS, [[Microsoft]], [[CloudHQ]]), the nearshoring-driven #2 LatAm market, constrained by water stress.

| Operator | Owner | Key Project | Potential |
|----------|-------|-------------|-----------|
| [[Scala Data Centers]] | [[DigitalBridge]] | Scala AI City (RS) | 4.75GW |
| [[Elea Data Centers]] | [[Goldman Sachs]]/[[Piemonte Holding]] | Rio AI City | 3.2GW |
| [[Ascenty]] | [[Digital Realty]]/[[Brookfield]] | 38 facilities | 4,000+ km fiber |
| [[ODATA]] | [[Aligned Data Centers]] (Macquarie → BlackRock/GIP, pending) | 23 facilities | ~2GW buildout |
| [[V.tal]] (Tecto) | [[BTG Pactual]]/GIC/CPP | Fiber + DC | $1B investment |

Why Brazil for AI:
- 80%+ renewable grid (hydro) — sustainability credentials
- Sub-80ms latency to US via [[Malbec Cable]]
- Lower power costs than US/Europe
- Growing domestic demand (fintech, enterprise)

REDATA incentives (originally MP 1,318/2025): tax suspensions (PIS/Cofins, IPI, import duties) for DCs meeting 100% renewable supply + strict water efficiency (≤0.05 L/kWh). R$5.2B budget, R$2T investment potential over 10 years; import/IPI suspensions effective Jan 1, 2026. Legislative status (June 2026): the government withdrew the provisional measure in early February 2026 before its Feb 25 expiry and refiled identical content as a bill (projeto de lei); the Chamber of Deputies approved REDATA on Feb 25, 2026, and it now awaits Federal Senate action. See [[Brazil AI]] for details.

Financing: Brazilian domestic [[Green bonds]] dominant. [[Bradesco BBI]] leads, with [[UBS BB]], [[Itaú BBA]], [[Santander Brasil]]. Scala issued BRL 5.32B total — record for Brazil DC sector.

No public exposure: All major Brazil DC operators are private. Indirect plays: [[DigitalBridge]] (DBRG) owns Scala, [[Digital Realty]] (DLR) owns 51% of Ascenty.

---

## Power constraints

Critical bottleneck: AI data centers need 10-50x power density of traditional.

| Challenge | Impact |
|-----------|--------|
| Grid capacity | Multi-year wait for connections |
| Utility buildout | Can't keep pace with demand |
| Renewable targets | Conflicts with 24/7 needs |
| Nuclear option | [[Nuclear power for AI]] gaining traction |

See [[Power constraints]] and [[Clean energy for AI]].

---

## Cooling technology

| Technology | Status | Players |
|------------|--------|---------|
| Air cooling | Legacy | Traditional DCs |
| Liquid cooling | Scaling | [[Vertiv]], [[Schneider Electric]] |
| Immersion cooling | Emerging | GRC, Submer |
| Rear-door heat exchangers | Growing | [[Modine Manufacturing]] |

AI GPUs require liquid cooling: Air can't handle 700W+ chips.

---

## Power infrastructure

| Component | Key players |
|-----------|-------------|
| UPS systems | [[Vertiv]], [[Schneider Electric]], Eaton |
| Generators | Caterpillar, Cummins |
| Transformers | [[GE Vernova]], [[Siemens Energy]] |
| Switchgear | [[Schneider Electric]], ABB |

---

## Investment themes

| Theme | Expression |
|-------|------------|
| REIT yield + growth | [[Equinix]], [[Digital Realty]] |
| AI infrastructure | [[CoreWeave]], [[IREN]], [[Core Scientific]] |
| Picks & shovels | [[Vertiv]], [[Schneider Electric]] |
| Crypto-AI arbitrage | [[Hut 8]], [[TeraWulf]] |
| Power plays | [[Constellation Energy]], [[Vistra]] |

---

## Key metrics

| Metric | What it measures |
|--------|------------------|
| MW deployed | Power capacity |
| [[PUE]] | Power Usage Effectiveness (efficiency) |
| Utilization | % of capacity leased |
| Interconnections | Network value (Equinix) |
| Contract duration | Revenue visibility |
| $/kW | Construction cost efficiency |

---

## Risks

| Risk | Impact |
|------|--------|
| [[Power constraints]] | Limits new capacity |
| Hyperscaler insourcing | REITs lose share |
| Interest rates | REIT valuations sensitive |
| GPU depreciation | Neocloud asset risk |
| Customer concentration | CoreWeave/IREN risk |
| Overbuilding | Utilization pressure |

---

## Public data center exposure

| Company | Ticker | Focus |
|---------|--------|-------|
| [[Equinix]] | EQIX | Colocation REIT |
| [[Digital Realty]] | DLR | Wholesale REIT |
| [[CoreWeave]] | CRWV | GPU cloud |
| [[Core Scientific]] | CORZ | [[Crypto-to-AI]] |
| [[IREN]] | IREN | [[Crypto-to-AI]] |
| [[Hut 8]] | HUT | [[Crypto-to-AI]] |
| [[TeraWulf]] | WULF | [[Crypto-to-AI]] |
| [[Vertiv]] | VRT | Cooling/power |
| [[Modine Manufacturing]] | MOD | Thermal management |

---

## Correlation structure

*Avg correlation, Data Centers as a whole: 0.39 — too weak. Splits into distinct sub-sectors.*

| Sub-sector | Intra-corr | Key players | Sister concept |
|------------|-----------|-------------|----------------|
| [[DC REITs]] | 0.69 | [[Equinix]], [[Digital Realty]] | — |
| [[Crypto-to-AI]] | 0.61 | [[Core Scientific]], [[Hut 8]], [[IREN]], [[TeraWulf]] | [[Crypto-to-AI pivot]] |
| GPU clouds (neoclouds) | — | [[CoreWeave]], [[Lambda Labs]], [[Nebius]] | [[Neocloud financing]] |
| Cooling/power equipment | — | [[Vertiv]], [[Schneider Electric]], [[Modine Manufacturing]] | [[Water constraints]] |
| Cross-sector | 0.08–0.20 | REITs vs Crypto barely correlated | — |

REITs and Crypto-to-AI are fundamentally different businesses despite both owning data centers — the cross-sector correlation (0.08–0.20) sits below either cohort's internal cohesion. Only [[DC REITs]] and [[Crypto-to-AI]] clear the validation threshold; the GPU-cloud and cooling/power groupings are listed as economic sub-sectors, not yet correlation-validated cohorts.

---

## Related

### Actors
- [[QTS Data Centers]] — largest private platform (Blackstone)
- [[CyrusOne]] — \#2 private platform (KKR)
- [[Equinix]] — largest DC REIT
- [[Digital Realty]] — hyperscale REIT
- [[CoreWeave]] — GPU cloud leader
- [[Vertiv]] — cooling/power infrastructure
- [[Khazna Data Centers]] — dominant UAE / Middle East operator (G42)

### Adjacent sectors
- [[AI Infrastructure]] — broader AI infra thesis
- [[AI Storage]] — storage layer sub-sector
- [[Private Real Estate]] — Blackstone/QTS, KKR/CyrusOne buildout

### Concepts
- [[Power constraints]] — key bottleneck
- [[Clean energy for AI]] — sustainability angle
- [[Nuclear power for AI]] — power solution
- [[Neocloud financing]] — financing patterns (→ GPU clouds sub-sector)
- [[Crypto-to-AI pivot]] — sector trend (→ crypto pivots sub-sector)
- [[Latin America AI competitiveness]] — Brazil DC thesis

### Geographies
- [[Ashburn]] — major hub
- [[São Paulo Data Hub]] — LatAm leader
- [[Rio de Janeiro Data Hub]] — Rio AI City
- [[UAE]] — global #1–2 emerging markets (Stargate UAE)
- [[Saudi Arabia]] — HUMAIN/DataVolt 6.4 GW pipeline
- [[Malaysia]] — Johor, the Singapore-overspill market
- [[Ireland]] — Dublin, the grid-constraint case

### Brazil / LatAm operators
- [[Scala Data Centers]] — largest LatAm hyperscale (DigitalBridge)
- [[Elea Data Centers]] — Rio AI City (Goldman Sachs)
- [[Ascenty]] — Digital Realty/Brookfield JV
- [[ODATA]] — Aligned/Macquarie
- [[V.tal]] — fiber + Tecto DCs (BTG Pactual)

---

## Sources

- Synergy Research Group
- Company filings

*Created 2026-01-09, updated 2026-06-22*
