---
aliases:
  - Google Blackstone TPU cloud
  - Blackstone Google TPU joint venture
  - TPU compute-as-a-service venture
  - Google Blackstone AI cloud
tags:
  - event
  - ai
  - infrastructure
  - tpu
  - financing
---
#event #ai #infrastructure #tpu #financing

# Google-Blackstone TPU cloud venture 2026

On May 18, 2026, [[Alphabet|Google]] and [[Blackstone]] announced a new U.S.-based joint venture that will sell data centre capacity, networking, and access to [[Google Cloud]]'s [[TPU]] as a compute-as-a-service offering. [[Blackstone]] commits $5B in initial equity, with the first 500 MW of capacity targeted to come online in 2027 and scale further over time. [[Benjamin Treynor Sloss]] — the Google veteran who founded the Site Reliability Engineering practice in 2003 and was promoted in 2025 to chief programs officer leading data-centre efficiency, AI diffusion, and "infrastructure capital structures and long-term capacity and supply assurance" — was named CEO of the new company. The event matters because it externalises Google's TPU-distribution function into a Blackstone-controlled vehicle and mirrors, on the TPU side, the [[Neocloud financing|chip-maker-backed neo-cloud playbook]] that [[NVIDIA]] established with [[CoreWeave]], [[Nebius]], and [[Nscale]].

---

## Synthesis

The deal is most cleanly read as the supply-side response to the [[Anthropic hyperscaler financing surge April 2026|April 2026 Anthropic financing surge]] and the [[Google TPU Competitive Position|TPU customer roster]] [[Thomas Kurian]] unveiled at Cloud Next 2026 — Google has more demand for external TPU capacity than its own first-party fleet can comfortably serve while also running [[Gemini]] and consumer Google. Routing the third-party tranche through a separately-capitalised Blackstone vehicle solves three problems at once: it raises off-balance-sheet capital for the buildout (up to ~$25B all-in including leverage per [[Financial Times|FT]]'s anonymous source), it reduces the political friction inside Google between [[Google Cloud]] and [[Google DeepMind]] over scarce TPU capacity, and it gives external customers a non-Google brand to sign with even though the silicon and software stack are Google's.

The cleanest competitive read is that Google has decided to compete with [[NVIDIA]] not just on chips but on the *capital structure* around chips. [[NVIDIA]]'s neo-cloud playbook — equity in [[CoreWeave]], [[Nebius]], [[Nscale]], plus financing via [[Blackstone]] itself — converts GPU sales into a customer-financed flywheel. The Google-Blackstone JV is the structural twin: it converts TPU capacity into a [[Blackstone]]-financed flywheel that doesn't rely on [[Google Cloud]]'s balance sheet for the build. The chip race is now also a financing race; [[CoreWeave]] for the first time has a credibly-backed TPU-cloud peer.

The single-source caveat: the *majority-ownership* claim and the $25B leverage figure come only from [[Financial Times|FT]]'s anonymous "people familiar"; Blackstone's official release confirms only the $5B equity and the 500 MW / 2027 target, leaving the ownership split formally undisclosed.

---

## Deal terms

| Detail | Value | Source |
|---|---|---|
| Initial equity from [[Blackstone]] | $5B from funds managed by Blackstone | Blackstone official release, FT |
| Total potential investment with leverage | Up to ~$25B | FT, single anonymous source — not in Blackstone PR |
| First capacity online | 500 MW in 2027 (article said "next year" — formal PR confirms 2027) | Blackstone PR |
| Ownership split | [[Blackstone]] majority — per FT only; Blackstone PR does not specify | FT |
| Customer go-to-market | "Another option to access cloud TPUs in addition to using them through [[Google Cloud]]" | Blackstone PR |
| Hardware/software | Google supplies [[TPU]], software, and services | Blackstone PR + FT |
| Status of facilities | Some data-centre facilities already under construction | FT |
| Geographic footprint | U.S.-based new company; specific sites not disclosed | Blackstone PR |

---

## Capital-provider comparison vs CRWV / NBIS

The JV sits beside [[CoreWeave]] / CRWV and [[Nebius]] / NBIS in the accelerated-cloud category, but the capital provider is not the same. The Google-Blackstone structure is private-capital equity for a TPU operating company; the listed GPU clouds depend more on Nvidia support, customer contracts, public equity, private credit, and convertible debt.

| Vehicle | Capital providers | Customer/offtake support | Read-through |
|---|---|---|---|
| Google-Blackstone TPU JV | [[Blackstone]] funds provide $5B initial equity; [[Alphabet|Google]] contributes TPU hardware, software, and services. FT's up-to-$25B leverage figure remains FT-only. | No named anchor customer yet; [[Anthropic]] is the obvious demand candidate from the April 2026 TPU-capacity context. | TPU-side CoreWeave analogue, but capitalized as a Blackstone-backed private operating company. |
| [[CoreWeave]] / CRWV | [[NVIDIA]] equity plus public equity and private-credit facilities. The March 2026 $8.5B delayed-draw term loan was anchored by [[Blackstone]] Credit & Insurance, with [[Morgan Stanley]] / [[MUFG]] structuring and [[Goldman Sachs]] / [[JPMorgan Chase]] as lead arrangers. | [[Microsoft]] revenue concentration/backlog, plus [[Meta]] / [[Perplexity]] diversification. | GPU neocloud funded through Nvidia support, customer-backed debt, and private credit. |
| [[Nebius]] / NBIS | $700M strategic equity from investors including [[Accel]], [[NVIDIA]], and [[Orbis Investments]]-managed accounts; about $4.3375B convertible notes sold privately to qualified institutional buyers. | [[Microsoft]] up to $19.4B and roughly $3B [[Meta]] contract as demand anchors, not sponsor capital. | Listed GPU-cloud buildout funded through strategic equity and capital markets rather than a Blackstone-style infra JV. |

Sources: Blackstone release (May 18 2026), Reuters / StreetInsider on CoreWeave's $8.5B loan, CoreWeave Q1 2026 release, Nebius Dec 2024 strategic-equity release, Nebius Mar 2026 convertible-notes release.

---

## Leadership

| Role | Person | Background |
|---|---|---|
| CEO, new JV | [[Benjamin Treynor Sloss]] | 20+ years at Google. Founded [[Site Reliability Engineering]] in 2003, coined the SRE term, grew the practice to ~4,000 engineers. VP 24/7 overseeing networking, data centres, and SRE for all of Google. Promoted in 2025 to "chief programs officer" leading data-centre efficiency, AI diffusion, infrastructure capital structures, and long-term capacity and supply assurance — the function this JV externalises. |
| [[Blackstone]] sponsor | [[Jon Gray]] | President and COO, [[Blackstone]]. Architect of Blackstone's real-estate and digital-infrastructure expansion, including the 2021 [[QTS]] acquisition. |
| [[Google Cloud]] sponsor | [[Thomas Kurian]] | CEO, [[Google Cloud]] since Nov 2018. Strategic driver of TPU monetization through external anchor customers. |

The Sloss appointment is the structural signal. His prior remit — data-centre efficiency, AI diffusion, *infrastructure capital structures, long-term capacity and supply assurance* — is precisely the set of functions being moved outside Google's balance sheet into a Blackstone vehicle. The hire is functional continuity, not a side bet.

---

## Quoted material

[[Jon Gray]] (FT, Blackstone press release): "We see a generational opportunity to invest capital at scale building AI infrastructure… This new company has enormous potential as it helps to meet the unprecedented demand for compute." (Blackstone PR carries a third sentence: "we are incredibly proud to partner with Google.")

[[Thomas Kurian]] (Blackstone press release / FT): the venture "helps meet growing demand for TPUs, which are optimized specifically for efficiency"; gives organisations "more options for organisations to access accelerated compute capability."

FT framing: "the most aggressive move yet by the world's third-largest cloud provider to expand the reach of its self-developed AI chips and compete directly with leading chipmaker Nvidia."

---

## Market Reaction

| Ticker | May 18 close / move | May 19 close / move | Read |
|---|---:|---:|---|
| GOOGL | $396.94 / +0.04% | $387.66 / -2.34% | No clean positive repricing for [[Alphabet]]. Announcement-day price action was essentially flat and the next session was dominated by broader Google I/O / AI-duration tape. |
| NVDA | $222.32 / -1.33% | $220.61 / -0.77% | No immediate TPU-threat repricing in [[NVIDIA]]. NVDA outperformed [[SMH]] on May 18 (-1.33% vs -1.83%), with earnings later in the week still the dominant near-term catalyst. |
| BX | $117.04 / -0.72% | $114.26 / -2.38% | Mild negative read for [[Blackstone]]: investors treated the deal as capital-intensive and long dated rather than immediately accretive. |
| CRWV | $103.77 / -3.29% | $99.81 / -3.82% | The clearest affected equity. [[CoreWeave]] underperformed [[QQQ]] by about 286 bps and [[SPY]] by about 322 bps on May 18 as investors priced a TPU-backed neocloud peer into the competitive set. |
| NBIS | $199.86 / -9.13% | $197.73 / -1.07% | [[Nebius]] was hit even harder on May 18. Attribution is slightly messier because NBIS had run sharply into the event and analyst-rating noise followed, but multiple market write-ups grouped Nebius with CoreWeave as the AI-cloud names pressured by the Google-Blackstone TPU push. |

The single-day tape did not reprice the AI complex broadly. [[SPY]] fell 0.07%, [[QQQ]] fell 0.43%, and [[SMH]] fell 1.83% on May 18; against that backdrop, GOOGL was flat, NVDA traded with semiconductors rather than as a singled-out loser, and BX's decline was modest. The market impact showed up most clearly in the listed neoclouds: CRWV because the Google-Blackstone JV directly narrows the non-hyperscaler accelerated-cloud category that [[CoreWeave]] helped define, and NBIS because [[Nebius]] is the closest public GPU-cloud comparable. A broader crypto-to-AI capacity basket was also red on May 18 — [[Applied Digital]] -8.04%, [[Hut 8]] -6.12%, [[Cipher Mining]] -5.95%, [[TeraWulf]] -5.29%, [[IREN]] -4.68%, [[Core Scientific]] -2.64% — but attribution is weaker there because that cohort had already been selling off on May 15 and several names had separate financing, acquisition, or Bitcoin/AI-capacity catalysts. Two broader reads are consistent with that: (1) the deal is incremental for [[Alphabet|Google]] and [[NVIDIA|Nvidia]] because the [[Google TPU Competitive Position|TPU shift]] was already visible after the [[Anthropic hyperscaler financing surge April 2026|April 2026 Anthropic deal]] and Cloud Next 2026 customer roster; (2) the Blackstone PR did not confirm the most striking FT details (Blackstone majority, $25B all-in), so the broader market may be waiting for governance and capacity-disclosure clarity.

[[Google Cloud]] has no standalone listed equity, so the GCP read-through is captured through [[Alphabet]] / GOOGL rather than a separate same-day or next-day tape line.

Correlation-cluster scoping: this is event tape, not fresh cluster validation. The already identifiable clusters to check are [[AI Compute]] and [[Crypto-to-AI]]. AI Compute remains a chip/foundry/customer triangle centered on [[TSMC|TSM]], [[NVIDIA|NVDA]], and [[AMD]], with [[Alphabet|GOOGL]] as a hyperscaler buyer/control; the Google-Blackstone JV is a TPU-vs-GPU competitive signal, not evidence that CRWV or NBIS belong in that cluster. Crypto-to-AI already captures miner-to-AI capacity names such as CORZ, HUT, IREN, WULF, MARA, RIOT, and CLSK; [[CoreWeave]] is an AI-infra control/adjacent factor in that framework, while [[Nebius]] has no established cluster validation in the vault. Treat the CRWV/NBIS move and capacity-basket weakness as market-reaction evidence and future-watch signal, not proof of a durable listed-neocloud return-correlation cluster.

Price source: StockAnalysis historical tables for GOOGL, NVDA, BX, CRWV, NBIS, APLD, HUT, CIFR, WULF, IREN, CORZ, SPY, QQQ, and SMH, accessed May 19, 2026. Invezz separately tied CRWV's May 19 premarket weakness to the Google-Blackstone deal and quoted [[Bernstein]]'s Madison Rezaei saying the 500 MW plan is "not immediately problematic" but marks "the beginning of a more earnest hyperscale attack" on the market. BanklessTimes and Investing.com market write-ups also grouped Nebius with CoreWeave as pressured AI-cloud names.

---

## Structural read-through

### For [[Alphabet]] / [[Google Cloud]]

Google externalises the supply-side risk on the buildout while preserving full ownership of the silicon, software, and chip roadmap. The third-party demand that exceeded [[Google Cloud]]'s comfortable allocation now has a non-Google contracting venue, which reduces the [[Gemini]] / DeepMind political friction over TPU capacity that [[Thomas Kurian]]'s expanded allocation authority created. The JV is also a near-term financing optimization: rather than absorbing 500 MW of buildout into the $180-190B FY26 [[Hyperscaler capex|capex guide]], the equity goes onto Blackstone's books.

The longer-term competitive optionality is the more interesting prize. Embedding TPUs inside a Blackstone-controlled retail-facing cloud weakens [[NVIDIA]]'s ecosystem moat by making TPU access feel less like a [[Google Cloud]] lock-in. That's the same logic [[NVIDIA]] used when it backed [[CoreWeave]] and [[Nebius]] — make the chips available outside the dominant cloud incumbent to broaden the addressable market.

### For [[Blackstone]]

The JV is the largest AI-infrastructure deal Blackstone has anchored on its own — bigger than the $10B [[QTS]] take-private (2021), bigger than its portion of the $7.5B [[CoreWeave]] debt facility (2024). It positions Blackstone as the dominant private-capital intermediary for AI infrastructure across both chip families: equity in [[Anthropic]] and [[OpenAI]] on the model side, [[QTS]] data centres on the colocation side, [[CoreWeave]] financing on the GPU-cloud side, and now equity in the largest TPU-cloud venture. The cleanest comparison is to [[Blue Owl]]'s $60B [[Meta]] Hyperion JV — but Blackstone's structure is a *durable operating company*, not a project SPV, which carries different risk and return characteristics.

The 2021 [[Blackstone]] AI thesis — built around [[QTS]] colocation for hyperscalers — is now layered with a captive TPU-cloud operating business. Blackstone's AI infrastructure exposure stack is now arguably broader than any other private-capital sponsor.

The "power" contribution is best read as powered-capacity delivery capability, not a disclosed power asset. [[Blackstone]] is not just writing a cheque; it is underwriting the site selection, utility/interconnection, construction, operations, and energy-procurement problem that turns [[Alphabet|Google]]'s TPUs into billable 500 MW data-centre capacity. That matches Jon Gray's official framing of Blackstone's "energy and digital infrastructure" strength and its existing digital-infra base in [[QTS]] and [[AirTrunk]]. The caveat is important: no specific power plant, [[Power purchase agreement|PPA]], utility interconnection, grid region, or site has been disclosed, so the note should not treat Blackstone as bringing named electricity supply yet.

### For [[NVIDIA]]

The JV is the clearest sign yet that the competitive frame around TPU has shifted from "Google internal tool" to "TPU as competitive AI silicon distributed through every business model Nvidia uses." Nvidia's neo-cloud financing playbook ([[CoreWeave]], [[Nebius]], [[Nscale]]) was a structural advantage; it now has a credibly-backed mirror image. The narrower point — TPU has not been submitted to MLPerf — survives, but the customer-share and capital-structure disputes are both weakening.

The frenemy framing matters here. [[Financial Times|FT]] explicitly notes that [[Alphabet|Google]] "is also one of the largest buyers of Nvidia's graphics processing unit chips" — the same company building this TPU-cloud to challenge Nvidia is one of Nvidia's biggest GPU customers. That dual posture is the structural ceiling on how aggressively Google can position the JV against Nvidia in the near term: the TPU-cloud sells the alternative while [[Google Cloud]] continues to buy and operate large Nvidia fleets for the workloads TPU doesn't yet serve (consumer cloud, third-party GPU-preference customers, fine-tuning workloads tied to the Nvidia ecosystem). The deeper read is that Google's chip strategy is a *substitution at the margin* rather than a clean break — the JV expands the TPU addressable market without forcing customers to choose.

The market's muted reaction reflects the timing: [[NVIDIA]] earnings due later in the week dominate the near-term tape, and the absolute capacity in this JV (500 MW in 2027) is small relative to Nvidia's quarterly run-rate.

### For [[CoreWeave]]

CoreWeave is the structural loser at the margin. Its core thesis — fast GPU access outside hyperscaler quotas, backed by Nvidia capital — now has a TPU twin backed by [[Blackstone]] (also one of CoreWeave's own debt providers). The competitive landscape narrows: a customer that wanted TPU exposure previously had to go through [[Google Cloud]] or [[FluidStack]]; that customer now has an option that looks more like CoreWeave but with TPU silicon. CoreWeave's 65% [[Microsoft]] revenue concentration is somewhat insulating in the near term, but the long-term TAM for non-hyperscaler accelerated cloud is now contested across chip families.

### For [[FluidStack]]

FluidStack was the first Google-backed TPU neo-cloud play (the Feb 2026 $100M Google investment plus the [[Anthropic]] / [[Hut 8]] / [[TeraWulf]] deployments). The Blackstone JV is the much-larger second step — same strategic logic, more capital, more public-market visibility. The two are complementary on capacity but the new JV will likely take the larger marquee customers.

### For [[Neocloud financing]]

The taxonomy expands. The concept note's existing table covers Nvidia-financed GPU neo-clouds ([[CoreWeave]], [[Lambda Labs]], [[IREN]], [[Nebius]], [[Nscale]], [[Crusoe Energy]]); the Google-Blackstone JV opens a new category — chip-maker-backed TPU neo-clouds — that mirrors the Nvidia playbook but with different silicon. See [[Neocloud financing]] for the expanded structure.

---

## Why the FT/Blackstone source disagreement matters

Two figures are FT-only and absent from the official Blackstone release:

1. *Total leverage up to $25B*: FT cites "one of the people [familiar]" only. Blackstone PR confirms the $5B equity but not the leverage cap. The $25B figure is plausible — 5x equity-to-total is standard for infrastructure project finance — but should be treated as an FT-sourced estimate, not a confirmed term.
2. *Blackstone majority ownership*: FT states it as fact; Blackstone PR is silent. This is unusual — JV ownership splits are normally disclosed in the announcement. The silence suggests the structure may still be in flux or governance details are being held for regulatory/competitive reasons.

Vault treatment: record both as FT-attributed claims with the gap to the official PR called out explicitly. Update if Blackstone or Google file securities-disclosure language that pins the figures.

---

## Watch for

The JV is a structural shift, not a one-off deal. The following downstream items are not yet resolved and would each be a natural follow-up ingestion when they surface.

| Watch item | What would trigger an update | Why it matters |
|---|---|---|
| Formal ownership-split disclosure | SEC / regulatory filing or company-release clarification | Resolves the FT-vs-PR sourcing gap on the *Blackstone majority* claim. Determines whether the venture consolidates onto Blackstone's books or sits as joint-venture equity-method. |
| $25B leverage stack formalisation | Bank-led debt facility, project-finance issuance, or 10-Q disclosure | The 5x equity-to-total ratio implied by FT's anonymous source is plausible but unconfirmed. The lender syndicate identity will matter — same Blackstone-financed banks as [[CoreWeave]]? New entrants? |
| Anchor-customer announcement(s) | Press release / earnings commentary by [[Anthropic]], [[OpenAI]], [[Cohere]], [[Mistral]], [[Thinking Machines Lab]], or others | The JV's economics depend on customer lock-in. Anthropic is the most-likely anchor given the [[Anthropic hyperscaler financing surge April 2026|$200B / 5 GW deal]] context, but a non-Anthropic customer would expand the TPU TAM more meaningfully. |
| [[NVIDIA]] earnings commentary (this week) | [[Jensen Huang]] / [[Colette Kress]] remarks on the JV during the post-close call | The first explicit Nvidia framing of the JV. Watch whether Nvidia escalates to a competitive counter-investment or stays in measured-confidence mode. |
| Asia-Pacific equivalent of the JV | Google partnering with [[GIC]], [[Temasek]], [[Mubadala]], or a Japanese mega-bank for an APAC TPU-cloud | Would convert the US-only JV into a globally-distributed TPU-cloud utility. Mirrors the [[Citi-HPS direct lending EMEA partnership May 2026|Citi-HPS EMEA partnership]] pattern of regional bank-private-credit JVs. |
| Hyperscaler peer responses | [[AWS]] / [[Microsoft]] equivalent ([[Trainium]]-cloud with [[Apollo]] / [[KKR]] / [[Brookfield]]?) | The Google-Blackstone JV is a financing blueprint, not just a one-off. If [[AWS]] or [[Microsoft|Azure]] copies the structure for their own custom silicon, the entire AI-infra capital stack becomes private-credit-led. |
| Facility geographic disclosure | Site naming for the 500 MW under-construction capacity | Determines power-grid exposure ([[PJM]] vs [[ERCOT]] vs Western Interconnection), tax-incentive geography, and proximity to [[QTS]]'s existing footprint. |
| [[CoreWeave]] competitive response | Earnings commentary on TPU peer + customer concentration risk | CoreWeave is the structural loser at the margin. The next earnings call will be the first public read on whether the JV is affecting their pipeline. |
| Regulatory / antitrust scrutiny | DOJ / FTC / EU Commission comments on Google-Blackstone concentration in AI-infra | The JV touches both AI-compute distribution (Google dominance concern) and AI-infrastructure-financing concentration (Blackstone across QTS + CoreWeave + JV). Either regulator could raise concerns. |
| [[FluidStack]] role rebalance | Quiet wind-down or repositioning as secondary TPU outlet | FluidStack was Google's first TPU-neo-cloud bet (Feb 2026 $100M). The JV likely takes the larger marquee customers; whether FluidStack remains a parallel channel or gets folded in is structurally informative. |

---

## Related

- [[Alphabet]] / [[Google Cloud]] — venture partner, hardware supplier
- [[Blackstone]] — anchor sponsor, majority owner (per FT)
- [[Benjamin Treynor Sloss]] — JV CEO, SRE founder
- [[Jon Gray]] — Blackstone president/COO; quoted
- [[Thomas Kurian]] — Google Cloud CEO; quoted
- [[TPU]] — silicon at the centre of the JV
- [[NVIDIA]] — competitive frame
- [[CoreWeave]] — structural peer competitor (GPU-cloud counterpart)
- [[Nebius]] — Nvidia-backed neo-cloud comparable
- [[FluidStack]] — earlier, smaller Google-backed TPU deployment play
- [[QTS]] — Blackstone's prior anchor AI-infra asset
- [[Anthropic]] — TPU anchor customer driving the demand thesis
- [[Anthropic hyperscaler financing surge April 2026]] — upstream demand event
- [[Google TPU Competitive Position]] — strategic context
- [[Neocloud financing]] — taxonomy expansion (chip-backed TPU clouds)
- [[AI infrastructure deals]] — capital-stack ledger
- [[Hyperscaler capex]] — off-balance-sheet financing logic
- [[AI infrastructure financing risk]] — circular-financing frame
- [[Site Reliability Engineering]] — Sloss-founded discipline

---

## Sources

- [Blackstone — Joint Venture with Google to Create New TPU Cloud (press release)](https://www.blackstone.com/news/press/blackstone-announces-joint-venture-with-google-to-create-new-tpu-cloud/) — May 18 2026
- [Financial Times — Google makes chip push with Blackstone-backed AI cloud group](https://www.ft.com/content/5730b605-8fb2-4973-a188-b4a587ce3580) — Rafe Rosner-Uddin and Ryan McMorrow, May 18 2026
- [Reuters via Investing.com — Google, Blackstone to launch AI cloud venture](https://www.investing.com/news/stock-market-news/google-blackstone-to-create-new-ai-cloud-company-wsj-reports-4697320)
- [Cryptopolitan — Google and Blackstone form AI cloud venture to challenge CoreWeave](https://www.cryptopolitan.com/google-and-blackstone-form-ai-cloud-venture/)
- [Benzinga — Google-Blackstone AI Venture Targets Exploding Demand For Compute Power With $5 Billion Initial](https://www.benzinga.com/markets/tech/26/05/52653665/google-blackstone-ai-cloud-business-data-centers-chips)
- [Invezz — CoreWeave stock falls 4%: why Google Blackstone deal is bad for the stock?](https://invezz.com/news/2026/05/19/coreweave-stock-falls-4-why-google-blackstone-deal-is-bad-for-the-stock/) — May 19 2026
- [BanklessTimes — CoreWeave Stock Drops on Google-Blackstone Deal: Is the Dip Justified?](https://www.banklesstimes.com/articles/2026/05/19/coreweave-stock-drops-on-google-blackstone-deal-is-the-dip-justified/) — May 19 2026
- Sloss SRE/role background: [Google SRE — Ben Treynor Sloss on SRE](https://sre.google/in-conversation/), [DevOps Institute — Origins of SRE](https://www.devopsinstitute.com/blog-the-origins-of-sre-from-the-director-of-sre-education-at-google/)
