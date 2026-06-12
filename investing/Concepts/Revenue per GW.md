---
aliases: [Revenue/GW, ARR per GW, Rev per GW, Monetization per GW, Revenue per gigawatt]
tags: [concept, ai, economics, datacenter, capex, unit-economics]
---

#concept #ai #economics #datacenter #capex

Revenue per GW — annualized revenue divided by gigawatts of critical IT capacity consumed. The cross-stack comparator for the AI capex financability debate: how much monetization each layer of the compute economy extracts from a gigawatt, and at what margin. Framework articulated by [[Clark Tang]] ([[Altimeter Capital]], Mar 1 2026) on X; the cost side comes from [[Epoch AI]], [[Bernstein]], and [[NVIDIA]] per-GW build estimates.

---

## Synthesis

The metric exists because the financability question — [[Hyperscaler capex]] guides at $700-725B for 2026, ~20 GW of incremental IT capacity per [[AI compute demand curve]] — cannot be answered from the spending side alone. A gigawatt costs roughly $35-60B to build ([[Epoch AI]]: ~$38B upfront TCO, annualizing to ~$8.5B/yr over asset lives; [[Bernstein]] ~$35B; NVIDIA's own $50-60B framing) and rents at roughly $10-13B/yr ([[Dylan Patel]]). The question is which layers monetize a GW well above that hurdle.

The ladder, per Tang's run-rate estimates (CY2025 basis): raw infrastructure monetizes at $8-12B/GW with core hardware-rental operating margins of 10-20%; model providers monetize inference-allocated capacity at $22-31B/GW with estimated gross margins of 50-70%; hyperscale internet apps ([[Google]], [[Meta]]) monetize at $41-57B/GW with 32-41% operating margins — the most profitable per-GW businesses in existence, and before the 2022 datacenter cycle their revenue per GW was significantly higher. Software ([[Snowflake]], [[Salesforce]]) shows $31-34B/GW, but there the number is an output, not an input — software sells value, not repackaged power, and cannot grow by adding gigawatts.

Three structural reads follow. First, the margin escalator: [[AWS]] disclosed a 17% operating margin in its first segment report (Q1 2015) and built toward ~40% over a decade by attaching software to rented hardware — the playbook [[CoreWeave]], [[Oracle]] [[OCI]], and the neoclouds are betting on repeating. Second, the layers are complements: every dollar of internet-app and model-provider monetization validates the thin-margin rental economics beneath it. Third, the financability conclusion is slope-dependent: at [[OpenAI]]'s disclosed $20B exit ARR on a 1.9 GW footprint ($10.5B ARR/GW blended), the system clears its hurdle only if inference revenue keeps compounding while training remains tolerable overhead — which is why [[Jensen Huang]]'s Q4 FY26 claim that "we're generating profitable tokens" is the load-bearing assertion of the whole buildout (see [[Jensen 1000x compute thesis]]).

What would falsify the optimistic read: inference ARR slope flattening while GW additions continue (denominator grows, numerator doesn't), training share of footprints staying high instead of declining, depreciation schedules proving shorter than rental-margin assumptions embed, or the ~3-5%/yr gross-margin gains Tang expects providers to keep being competed away to users instead (see [[Inference economics]] for the token-level version of that fight).

---

## The framework chart

![[revenue-per-gw-framework-altimeter-mar2026.png]]
*Revenue/GW vs operating profit/GW across the compute stack — [[Clark Tang]] ([[Altimeter Capital]]), X post, Mar 1 2026 (97.4K views). Run-rate basis, CY2025 public data plus stated adjustments. For model providers the x-axis uses estimated gross margin, not operating margin.*

---

## The numbers

| Layer | Name | Revenue/GW | Op income/GW | Margin |
|---|---|---|---|---|
| Hyperscale internet apps | [[Google]] | $57B | $18B | 32% OM |
| Hyperscale internet apps | [[Meta]] | $41B | $17B | 41% OM |
| Cloud | [[AWS]] | $10B | $4B | 35% OM |
| Cloud | Azure ([[Microsoft]]) | $9B | $4B | 40% OM |
| Neocloud | [[CoreWeave]] | $10B | $2B | 15% OM (Tang adjustment) |
| Model provider | [[OpenAI]] | $22B | $12B | 55% est. GM |
| Model provider | [[Anthropic]] | $31B | $20B | 65% est. GM |
| Software (context) | [[Snowflake]] | $34B | $3B | (35%) [[GAAP]] shown; OI uses CY25 non-GAAP |
| Software (context) | [[Salesforce]] | $31B | $6B | 20% OM |

All figures are Tang's run-rate estimates from public CY2025 data; the cells flagged red in the original chart (CoreWeave, OpenAI, Anthropic, Snowflake) are adjusted or estimated rather than reported.

---

## Methodology and adjustments (Tang's stated assumptions)

- [[CoreWeave]] at 15% OM is a deliberate discount to its publicly discussed 20-30% long-term margins and [[Oracle]]'s GPU-cloud margin targets — assuming a shorter depreciation cycle than the companies assume and zero incremental software margin. Cross-check: Oracle's reported AI-infrastructure gross margin was 32% (above 30% guidance) at its FY26 Q3 print, and The Information reported GPU-rental gross margins in the teens during 2025 — the wide range reflects basis differences (gross vs operating, blended vs marginal) as much as disagreement.
- [[OpenAI]]: $20B exit ARR at end-2025 on a 1.9 GW footprint — both company-disclosed in the Jan 2026 "A business that scales with the value of intelligence" post, CFO [[Sarah Friar]]'s revenue-tracks-compute-1:1 argument (compute grew 0.2 GW 2023 → 0.6 GW 2024 → ~1.9 GW 2025) — gives $10.5B ARR/GW blended; the same ratio [[Brad Gerstner]] quotes as the "Sarah Friar number" in his 5-6-year payback formula. Tang allocates the footprint ~60/40 inference/training, putting inference-allocated monetization at ~$22B/GW. Training capacity generates no revenue directly; whether that is overhead or the product depends on the slope of inference growth.
- [[Anthropic]]: assumed more training-weighted than OpenAI. Tang's outside-in read: "remarkably amazing utilization of their limited resources" and strong contribution margins. The 65% figure is an estimated gross margin, deliberately an upper bound.
- Model providers use estimated GM instead of OM "to leave an upper bound on the profitability of these businesses which are fundamentally different software businesses than past ones."
- [[Snowflake]] / [[Salesforce]] revenue/GW is derived (AWS revenue/GW divided by product gross margins) — an inference about how much compute their revenue rides on, not a disclosure. Snowflake's operating income uses CY25 non-GAAP OP% because GAAP is negative.

---

## The cost side (the hurdle a GW must clear)

| Estimate | Per-GW figure | Source |
|---|---|---|
| Upfront TCO, 1 GW AI datacenter | ~$38B capex + ~$0.9B/yr opex | [[Epoch AI]] |
| Annualized cost over asset lives | ~$8.5B/yr | [[Epoch AI]] |
| Build cost, low estimate | ~$35B | [[Bernstein]] |
| Build cost, NVIDIA's framing | $50-60B | [[NVIDIA]] |
| Vault rule of thumb | ~$50B (~$35B chips) | [[AI compute demand curve]] |
| Rental cost | ~$10-13B/GW/yr | [[Dylan Patel]] ([[SemiAnalysis]]) |
| Revenue density, AI vs traditional DC | ~$12.50/W/yr vs ~$4.20/W/yr | Lean Research |

The arithmetic that matters: infrastructure-layer monetization ($8-12B ARR/GW) sits barely above the annualized cost (~$8.5B/yr) — which is exactly why core rental operating margins start at 10-20% and why that layer's economics hinge on software attach, financing terms, and depreciation assumptions. The layers above (models at $22-31B/GW, apps at $41-57B/GW) are what make the system-level [[ROIC]] positive, if the demand is real.

Inside [[Altimeter Capital]] itself the same arithmetic circulates as [[Brad Gerstner]]'s rule of thumb (Mar 2026, vault-recorded before this framework was ingested): 1 GW ≈ $50B to build, ~$10B/yr of revenue, a 5-6 year payback — the firm-level payback complement to Tang's layer-by-layer view.

---

## Layer observations (Tang)

1. Software: revenue/GW is an output, not an input. [[Snowflake]] runs a feature-rich scaled cloud data warehouse built over a decade of R&D; it cannot grow by adding power. Low raw COGS means most of gross margin is reinvested in S&M to sell large, long-duration contracts. See [[Software AI bifurcation]].
2. [[Google]] and [[Meta]] are the most profitable businesses per GW; retrieval-era ads were "the most profitable businesses known to mankind" — ~90% contribution margin, minimal S&M, a baked-in 20%+/yr growth algorithm from improving ad efficacy. But the algorithm slows with scale; they could not grow by adding power either. AI gives those profit pools an investment target again.
3. Infrastructure monetizes at ~$8-12B/GW, closest to the hardware. Core cloud ARR/GW is ~$12B (derivable from AWS power disclosures); new accelerated-compute infrastructure runs ~$10B ARR/GW consistently across [[Oracle]] [[OCI]], [[CoreWeave]], and [[NVIDIA]] figures. Hardware rental alone starts at 10-20% OM; the path to 40% is software attach at higher blended gross margins — the 2010s hyperscaler playbook.
4. Model providers are the mid-2010s [[Uber]]/[[Airbnb]]/[[Netflix]] profitability debate replayed: it's all about unit economics. At 50-70% gross margins, GM dollars can be allocated with significant operating leverage at scale. The research-compute budget is the structural outlier vs past company generations — Tang expects it to fall as a share of budgets, with inference-optimization benefits mostly passed to consumers while providers keep ~3-5%/yr of GM gains.

---

## The inflection claim

Tang dates the "switch flip" to mid-2025, taking off late 2025: [[Claude Opus|Opus 4.5]] and [[GPT-5]] crossed the usefulness threshold from chatbots and research tools to autonomous, agentic work (citing [[Andrej Karpathy]]'s testimony among others), shifting the game to inference throughput and latency. On the S-curve, more compute = more revenues = more operating leverage for model providers. [[Jensen Huang]], Q4 FY26 earnings call (Feb 25, 2026), asked how the hyperscalers will pay for their investments: "I am confident in their cash flow growing... in this new world of AI, compute is revenues... we've reached the inflection point and we're generating profitable tokens that are productive for customers and profitable for the cloud service providers."

The counterweights already in the vault: enterprise token rationing ([[Inference economics]], May 2026), the [[GPU deployment bottleneck]] (shipped ≠ deployed), [[AI infrastructure financing risk]] (circular capital), and the [[Hyperscaler capex]] free-cash-flow trough with equity raises now in the stack. The framework argues the destination economics work; it does not say the financing path is smooth.

Cluster-validation disposition: no tradeable peer cohort is claimed here — the framework deliberately spans four business layers, two private companies, and two segments (AWS, Azure) that are not separately listed. The public hyperscaler subset is already covered by the existing hyperscalers cluster artifacts (see [[Mag 7 cluster]], [[AI hyperscalers]]).

---

## Related

- [[Clark Tang]] — framework author
- [[Altimeter Capital]] — his firm
- [[Hyperscaler capex]] — the spending side this framework pressure-tests
- [[AI compute demand curve]] — the GW-capacity side (~20 GW incremental 2026)
- [[Inference economics]] — token-level margins underneath the per-GW view
- [[AI infrastructure financing]] — the funding stack
- [[AI infrastructure financing risk]] — the bear case
- [[Jensen 1000x compute thesis]] — profitable-tokens claim, Q4 FY26 call
- [[Software AI bifurcation]] — the software layer's per-GW position
- [[GPU-as-a-Service]] — neocloud rental economics
- [[GPU rental price index]] — market pricing of the rental layer
- [[Data center physical layer]] — what a GW physically is
- [[OpenAI]], [[Anthropic]], [[CoreWeave]], [[Oracle]], [[Google]], [[Meta]], [[Amazon]], [[Microsoft]], [[Snowflake]], [[Salesforce]] — plotted names

*Sources: [Clark Tang on X, Mar 1 2026](https://x.com/_clarktang) (97.4K views); [OpenAI, "A business that scales with the value of intelligence"](https://openai.com/index/a-business-that-scales-with-the-value-of-intelligence/) ($20B run-rate + 0.2/0.6/1.9 GW footprint); [Epoch AI, 1-GW datacenter TCO](https://epoch.ai/data-insights/ai-datacenter-cost-breakdown); [Amazon Q1 2015 10-Q](https://www.sec.gov/Archives/edgar/data/1018724/000101872415000038/amzn-20150331x10q.htm) (first AWS segment disclosure, 17% OM); [NVIDIA Q4 FY26 press release](https://www.sec.gov/Archives/edgar/data/0001045810/000104581026000019/q4fy26pr.htm); [Investing.com on per-GW build cost](https://www.investing.com/news/stock-market-news/how-much-does-a-gw-of-data-center-capacity-actually-cost-4314046).*

*Created 2026-06-12*
