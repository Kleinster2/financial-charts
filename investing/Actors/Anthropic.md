		#actor #ai #modellab

Anthropic - AI lab, maker of Claude. More capital-efficient than [[OpenAI]].

---

## Evolution

The story of Anthropic is the story of whether you can build the most powerful AI in the world while refusing to let it do everything the most powerful institutions in the world want it to do — and whether that refusal is a moat or a liability.

- 2016-2020 (inside OpenAI): Dario Amodei joins [[OpenAI]] in 2016 as a research scientist, rising to VP of Research. Born in 1983 in San Francisco — father was an Italian-American leather craftsman, mother Jewish American — he studied physics at Stanford and got his PhD in computational neuroscience at Princeton, researching the electrophysiology of neural circuits. At OpenAI, he plays instrumental roles in GPT-2 (2019) and GPT-3 (2020), the two models that proved scaling laws worked. His sister Daniela Amodei — four years younger, English lit/politics background, early employee at [[Stripe]] — joins OpenAI in 2018 as VP of Safety and Policy. Together they form a power center within the org focused on safety. But tensions build: OpenAI is accelerating toward commercialization under [[Sam Altman]], the nonprofit structure is fraying, and Dario believes safety isn't getting the institutional priority the capabilities deserve. He and others go to OpenAI's board to try to push Altman out. They fail. The relationship becomes untenable

- 2021 (the exodus): In early 2021, seven senior OpenAI researchers leave together — led by Dario and Daniela Amodei. The group includes Tom Brown (lead author of the GPT-3 paper), Chris Olah (neural network interpretability pioneer), Sam McCandlish (scaling laws research), Jack Clark (OpenAI's Policy Director), and Jared Kaplan (physicist, co-author of the scaling laws paper that proved bigger models = better models). This isn't a random departure — it's OpenAI's safety brain trust walking out the door and taking the people who literally wrote the scaling playbook with them. As of February 2026, all seven founders remain at the company — unusual for a five-year-old startup at $380B valuation, and a stark contrast to OpenAI's revolving door of departures. They incorporate Anthropic as a Public Benefit Corporation in Delaware — a legal structure that explicitly balances profit with social impact. Later, they establish a Long-Term Benefit Trust (LTBT) that will eventually control a majority of the board, designed specifically to prevent the kind of mission drift they watched happen at OpenAI. The founding thesis: frontier AI is coming whether or not Anthropic builds it, so the safest path is to have a safety-focused lab at the frontier rather than ceding the frontier to labs that don't prioritize safety. Series A: $124M led by Dustin Moskovitz (Facebook co-founder) and [[Jaan Tallinn]] (Skype co-founder, existential risk funder)

- 2022 (Constitutional AI and the FTX bomb): In December 2022, Anthropic publishes "Constitutional AI: Harmlessness from AI Feedback" — the foundational research that distinguishes them from every other lab. Instead of training models on human feedback (RLHF, the standard approach), they give the model a set of principles — a "constitution" — and train it to critique and revise its own outputs against those principles. This is both a technical innovation (cheaper, more scalable, more consistent than human annotators) and a philosophical statement: the model should internalize values, not just learn to pattern-match human preferences. Series B ($580M, April 2022) includes $500M from Sam Bankman-Fried's FTX — the largest single check. When FTX collapses in November 2022, Anthropic's FTX stake (7.84% of the company) becomes a bankruptcy asset. The FTX estate eventually sells for $1.3B, a $800M profit — irony: the crypto fraud funded the AI safety lab, and the bankruptcy estate profited handsomely

- 2023 (Claude arrives, Big Tech bets): Claude 1 launches in March 2023 — the first commercial product, competing directly with ChatGPT. Claude 2 follows in July, the first version available to the public. The models are good but not market-leading. What changes everything is the fundraising: [[Google]] invests $2B (for ~10% of the company) in early 2023. [[Amazon]] commits $4B starting in September — the largest single AI investment at the time. Both are hedging: Google needs a counterweight to [[Microsoft]]-OpenAI, Amazon needs a frontier model for AWS Bedrock. Anthropic becomes the rare company backed by competing hyperscalers simultaneously. [[Salesforce]] adds $750M. Revenue is still tiny — ~$87M annualized in early 2024 — but the fundraising signals that Anthropic has become the only credible alternative to OpenAI at the frontier

- 2024 (Claude 3 — the leap): Claude 3 launches in March 2024 with three tiers: Haiku (fast), Sonnet (balanced), Opus (frontier). Opus matches or exceeds GPT-4 on most benchmarks — the first time Anthropic can credibly claim technical parity with OpenAI. This is the inflection. Revenue goes from ~$87M annualized to $900M+ by year-end. Enterprise adoption accelerates: the three-tier model lets companies pick the right tradeoff of cost/speed/quality. Amazon completes its $4B commitment, then adds another $4B in November ($8B total). Series E ($3.5B at $61.5B valuation, led by Lightspeed) and Google adds $1B more. Claude Code — a coding agent, not just an autocomplete tool — launches internally and begins reshaping how developers work. Dario publishes "Machines of Loving Grace," laying out his vision of AI benefiting humanity, while simultaneously building the most commercially aggressive AI products in the market. The tension between the safety mission and the growth imperative is now the central narrative

- 2025 (escape velocity): Revenue hockey-sticks from $900M to $9B+ annualized by January 2026. Claude Code launches publicly in May and hits $2.5B run rate within months — the fastest-growing product in the company's history. 4% of GitHub public commits are now authored by Claude Code. Claude 4 family launches (Opus 4, Sonnet 4, Haiku 4), then Claude 4.5, each pushing the frontier further. Series F ($13B at $183B valuation, September) followed immediately by $15B in strategic investment from [[NVIDIA]] ($10B) and [[Microsoft]] ($5B) — Microsoft investing in Anthropic despite its exclusive OpenAI partnership signals deep hedging. MCP (Model Context Protocol) and Skills launch as open standards — Anthropic's platform play: originate the standard, benefit from the ecosystem. Dario commits to covering 100% of electricity cost increases from Anthropic data centers. IPO preparation begins: Wilson Sonsini engaged. Revenue mix: 80% enterprise, 20% consumer. 300,000+ business customers. 8 of Fortune 10 are clients

- Jan-Feb 2026 (the collision): Everything converges. Claude Cowork launches (Jan 12) — "Claude Code for the rest of your work" — with 11 vertical plugins targeting legal, financial, sales, marketing. The $285B SaaSpocalypse follows: [[Thomson Reuters]] -18%, [[RELX]] -14%, [[LegalZoom]] -20%, Goldman software basket -6%. Claude is now destroying value in other companies faster than Anthropic itself is creating it. Series G closes at $30B/$380B valuation (Feb 12) — second-largest private tech financing ever. Revenue run rate hits $14B. Opus 4.6 and Sonnet 4.6 launch (Feb 5, Feb 17). Then the Pentagon standoff: Defense Secretary [[Pete Hegseth]] demands "all lawful use" of Claude for military applications. Anthropic holds two red lines — no autonomous weapons, no mass surveillance of Americans. Hegseth threatens the [[Defense Production Act]] (a 1950s law for national emergencies) and supply-chain risk designation (normally reserved for adversaries like [[Huawei]]). [[xAI]], [[OpenAI]], and [[Google]] all comply. Anthropic alone refuses. Friday February 28, 5:01 PM deadline still stands as of this writing

- The paradox: In the same month that Anthropic hits $380B valuation and $14B revenue run rate, it also quietly removes its flagship safety pledge — the commitment to pause model training if capabilities outstripped safety measures — replacing hard commitments with "public goals." The company that was founded because OpenAI wasn't taking safety seriously enough is now the company being accused of regulatory capture by [[David Sacks]] (White House AI Czar) and abandoning its own safety commitments by researchers who believed them. Whether this is principled evolution or mission drift depends entirely on your priors

The arc: seven OpenAI defectors → Constitutional AI → FTX-funded safety lab → Google + Amazon dual bet → Claude 3 reaches the frontier → $14B revenue in under 3 years → $380B valuation → Pentagon standoff over military AI → safety pledges quietly diluted. The founding thesis was that safety and commercial success are inseparable. Five years later, Anthropic has proved the commercial part beyond any doubt. The safety part is now being tested at the highest possible stakes — and the answer isn't clear yet.

---

## Financial position (Feb 2026)

| Metric | Value |
|--------|-------|
| Revenue | ~$20B annualized run rate (as of ~Mar 6; was $14B mid-Feb, $9B Jan, $87M early 2024). **$6B single-month revenue in Feb 2026** (28-day month) — more than Databricks or Snowflake's full-year revenue after 12 years |
| Claude Code run rate | $2.5B (launched publicly May 2025) |
| Revenue mix | 80% enterprise, 20% consumer |
| Business customers | 300,000+ |
| Large accounts ($100K+ ARR) | 7x growth in past year |
| $1M+ ARR customers | 500 (was 12 two years ago) |
| Fortune 10 clients | 8 of 10 |
| 2025 loss | $5.6B (confirmed Jan 2026) |
| Burn rate | Dropping to 9% of revenue by 2027 |
| Break-even target | 2028 |
| Valuation | $380B (Series G close, Feb 12 2026) |

Burning 14x less cash than OpenAI before profitability. CFO [[Krishna Rao]]: "Claude is increasingly becoming critical to how businesses work." FT (Mar 21 2026): Anthropic is adding $1B in annualized revenue each week in 2026. Business customers purchasing AI for the first time are choosing Anthropic at 3x the rate of [[OpenAI]], per [[Ramp]] AI Index data from 50,000+ customers — a reversal of the companies' positions a year ago.

![[ramp-anthropic-vs-openai-new-customers-mar2026.png]]
*Share of new corporate AI clients: Anthropic ~80% vs OpenAI ~20% by Feb 2026. Source: Ramp AI Index (FT, Mar 21 2026)*

![[ramp-anthropic-market-share-mar2026.png]]
*Market share among companies paying for AI models: Anthropic ~30%, OpenAI ~25%, Google ~10% by Jan 2026. Source: Ramp AI Index (FT, Mar 21 2026)*

[[NVIDIA]] CEO [[Jensen Huang]] (Mar 2026): expects his recent $40B investment across Anthropic and [[OpenAI]] to be his "last money in" — both companies will go public this year. [[Brad Gerstner]] ([[Altimeter]]): Opus 4.6 crossed a threshold where models compete with **labor budgets**, not IT budgets — "you could not possibly have a $6B month by displacing IT budgets."

---

## Funding rounds

| Date | Round | Amount | Valuation | Lead Investors |
|------|-------|--------|-----------|----------------|
| Apr 2022 | Seed/Series A | $580M | - | Incl. $500M FTX |
| Sep 2023 | Strategic | $1.25B | - | Amazon (start of $4B) |
| Oct 2023 | Strategic | $500M | - | Google (start of $2B) |
| Mar 2024 | Strategic | $2.75B | - | Amazon (completing $4B) |
| Nov 2024 | Strategic | $4B | - | Amazon (now $8B total) |
| Mar 2025 | Series E | $3.5B | $61.5B | Lightspeed |
| Mar 2025 | Strategic | $1B | - | Google (now $3B total) |
| Sep 2025 | Series F | $13B | $183B | Iconiq, Fidelity, Lightspeed, QIA |
| Nov 2025 | Strategic | ~$15B | - | NVIDIA ($10B) + Microsoft ($5B) |
| Feb 2026 | Series G | $30B | $380B | [[GIC]], [[Coatue Management\|Coatue]], [[D.E. Shaw]], [[Dragoneer]], [[Founders Fund]], [[Iconiq]], [[MGX]], [[Accel]], [[General Catalyst]], [[Jane Street]], [[QIA]], [[Altimeter]], [[Sequoia]] (36+ total) |

Total raised: ~$57B+ (per Fortune)

Second-largest private tech financing on record, behind [[OpenAI]]'s $40B+. Nearly doubled valuation from $183B to $380B in five months.

---

## Cap table

### Ownership estimates (@ $380B valuation)

| Investor                                                                          | Invested | Est. Ownership | Value @ $380B | Notes                               |
| --------------------------------------------------------------------------------- | -------- | -------------- | ------------- | ----------------------------------- |
| Founders/employees                                                                | -        | ~25-30%        | $95-114B      | Dario, Daniela Amodei + team        |
| [[Amazon]]                                                                        | $8B      | ~12-15%        | $46-57B       | Earliest large investor, best basis |
| [[Google]]                                                                        | $3B      | ~8-10%         | $30-38B       | Multiple rounds, cloud partner      |
| [[NVIDIA]]                                                                        | $10B     | ~3%            | $11.4B        | Late 2025, high entry               |
| [[Microsoft]]                                                                     | $5B      | ~1.5%          | $5.7B         | Late 2025, hedging OpenAI           |
| [[Salesforce]]                                                                    | $750M    | ~2-3%          | $7.6-11.4B    | 2023, good entry                    |
| [[Spark Capital]]                                                                 | -        | ~3-5%          | $11-19B       | Series A/B lead                     |
| [[Menlo Ventures]]                                                                | -        | ~2-4%          | $7.6-15.2B    | Early investor                      |
| [[GIC]] / [[Coatue]]                                                              |          | ~2-3%          | $7.6-11.4B    | Series G co-leads                   |
| [[Iconiq]]                                                                        | -        | ~1-2%          | $3.8-7.6B     | Series F + G                        |
| [[Altimeter]] / [[Sequoia]]                                                       | TBD      | <1%            | TBD           | Series G (both also OpenAI backers) |
| Other ([[QIA]], [[Jane Street]], [[Accel]], [[General Catalyst]], Fidelity, etc.) | -        | ~10-15%        | $38-57B       | Series E/F/G participants           |

*Estimates based on investment size vs. round valuation. Actual ownership undisclosed.*

### Key investors

| Investor            | Amount   | Notes                                         |                                      |            |
| ------------------- | -------- | --------------------------------------------- | ------------------------------------ | ---------- |
| [[Google]]          | $3B+     | Cloud partner, multiple rounds                |                                      |            |
| [[Amazon]]          | $8B      | AWS partnership, Bedrock distribution         |                                      |            |
| [[Microsoft]]       | $5B      | Late 2025, despite OpenAI relationship        |                                      |            |
| [[NVIDIA]]          | $10B     | Late 2025                                     |                                      |            |
| [[GIC]]             | Co-lead  | Series G co-lead (Singapore sovereign wealth) |                                      |            |
| [[Coatue Management | Coatue]] | Co-lead                                       | Series G co-lead ([[Philippe Laffont | Laffont]]) |
| [[QIA]]             | -        | Qatar Investment Authority, Series F + G      |                                      |            |
| [[Jane Street]]     | -        | Series G (quant trading firm)                 |                                      |            |
| [[Salesforce]]      | $750M    | 2023                                          |                                      |            |
| [[Spark Capital]]   | -        | Early investor, led Series A/B                |                                      |            |
| [[Menlo Ventures]]  | -        | Early investor                                |                                      |            |
| [[Sound Ventures]]  | -        | [[Ashton Kutcher]]'s fund                     |                                      |            |
| [[Jaan Tallinn]]    | -        | [[Skype]] co-founder, safety-focused          |                                      |            |
| [[Eric Yuan]]       | -        | [[Zoom]] founder                              |                                      |            |

Total raised: ~$57B+ (per Fortune)

Notable: Both Google AND Amazon invested (rare). Microsoft invested despite OpenAI partnership (hedging). [[Altimeter]] and [[Sequoia]] - both OpenAI backers - also investing in Anthropic's Series G.

---

## Recent developments

### Claude Cowork launch + $285B selloff (Jan-Feb 2026)

Jan 12: Launched Claude Cowork - "Claude Code for the rest of your work." Agentic file management, document creation, multi-step tasks. Initially Max subscribers only.

Jan 30: Launched 11 Cowork plugins targeting specific job functions:
- Legal (contract review, research)
- Financial (analysis, modeling)
- Sales (lead gen, CRM)
- Marketing (campaigns, content)
- Data viz, enterprise search

Feb 3-4: $285B rout - Software, legal analytics, Indian IT services collapsed. Goldman software basket -6%. Software P/E 33x → 23x.

| Company | Move | Notes |
|---------|------|-------|
| [[Thomson Reuters]] | -18% | Record daily loss |
| [[RELX]] | -14% | Worst since 1988 |
| [[LegalZoom]] | -20% | Most exposed |
| [[Infosys]] | -7.4% | Indian IT |

Market dubbed it the "SaaSpocalypse." JPMorgan: software stocks "sentenced before trial."

See [[Claude Cowork disruption February 2026]] and [[AI workflow disruption basket]] for full analysis.

Feb 4: Pledged not to run advertising, differentiating from [[OpenAI]]'s embrace of ads. FT reported 90% of [[Claude Code]]'s own codebase was AI-generated; 70-90% of code across Anthropic now written with AI. The company's reinforcement learning from AI feedback (RLAIF) technique — originally designed for safety (Constitutional AI) — had become a way to automate model improvement at far larger scale than human labeling.

---

### Harness crackdown + Clawdbot OAuth cutoff (Jan 2026)

Jan 9: Restricted Claude Code OAuth access, blocking third-party tools (OpenCode, [[OpenClaw|Clawdbot]], etc.) from using Max subscription benefits. This broke [[OpenClaw|Clawdbot]] integrations 18 days *before* the Jan 27 cease-and-desist over the "Clawdbot" name (Anthropic trademark claim on "Claude"). The OAuth cutoff - not the naming dispute - was the initial disruption that forced the project to adapt. Sources: HackerNoon, Business Insider, Reddit.

What happened:
- Claude Code enforces token limits client-side: 5-hour rolling windows (~220K tokens for Max20) + weekly token caps
- "Hours" in Anthropic marketing (e.g., "24-40 hrs Opus/week") are estimated usage time, not separate limits - all token-based
- Rate limits are enforced by the Claude Code CLI locally, not server-side. This is the critical design flaw that enabled arbitrage.
- Tools like OpenCode extracted the OAuth token and talked to Anthropic's API directly, getting Max-tier authentication without any of the client-side rate limiting
- Result: overnight autonomous loops consuming weeks of token allocation in hours — $200/mo users burning through what would cost thousands at API rates
- Tools that wrap the actual Claude Code CLI (like [[OpenClaw]]) still hit the normal rate limits because Claude Code's client-side governor is intact

Fallout:
- 147+ GitHub reactions, 245 HN points
- DHH called it "very customer hostile"
- Many Max subscribers canceled
- [[xAI]] employees cut off from Claude via [[Cursor]] - Tony Wu: "rly pushes us to develop our own coding product"
- OpenAI employees already blocked Aug 2025

Official rationale (Shihipar): Technical instability - unauthorized harnesses introduce bugs Anthropic can't diagnose.

Response: OpenCode launched "OpenCode Black" ($200/mo) via enterprise gateways.

Thesis implication: Not harness moat defense - compute arbitrage enforcement. Third-party harnesses still work via enterprise pricing (OpenCode Black). Anthropic protecting margin on Max subscription, not blocking competition.

Feb 20 update: Anthropic revised its legal terms to make the ban explicit. Updated legal compliance page now states: "Using OAuth tokens obtained through Claude Free, Pro, or Max accounts in any other product, tool, or service - including the Agent SDK - is not permitted." OpenCode received a direct legal notice and pushed code the same day removing Claude Pro/Max and API key support, citing "anthropic legal requests." The Register reported the story. OpenAI's Thibault Sottiaux pointedly endorsed Codex subscription use in third-party harnesses - [[OpenAI]], [[GitHub]], and GitLab all explicitly allow subscription use in third-party tools. Anthropic is the only frontier provider actively blocking this. Community backlash intensifying - "vote with your wallets" sentiment growing.

---

### Pentagon clash over military AI (Jan-Feb 2026)

Anthropic and the Pentagon are in an escalating standoff over a ~$200M contract (via [[Palantir]] partnership). Pentagon pushing all four AI contractors ([[Google]], [[OpenAI]], [[xAI]], Anthropic) to allow "all lawful purposes" military use - including weapons development, intelligence collection, and battlefield operations. Anthropic alone is holding two red lines:
1. Fully autonomous weapons
2. Mass surveillance of Americans

**Timeline:**
- Jan 9: Defense Secretary [[Pete Hegseth]]'s AI strategy memo states Pentagon needs models "free from usage policy constraints"
- Jan 16: Hegseth criticized Anthropic when announcing [[xAI]]'s Grok would join Pentagon AI providers, railing against models that "won't allow you to fight wars"
- Jan 30: Reuters reported the $200M contract standoff
- Feb 12: Reuters reported Pentagon pushing AI companies onto classified networks without standard restrictions
- Feb 13: Axios/WSJ reported Claude was used during the [[Maduro capture operation]] (via [[Palantir]]). An Anthropic employee subsequently asked [[Palantir]] how Claude was being used in the operation
- Feb 15: Axios exclusive - Pentagon "fed up," threatening to cut Anthropic entirely. Administration official: "everything's on the table… but there'll have to be an orderly replacement"
- Feb 17-18: Escalation - Pentagon reviewing entire Anthropic partnership, may ask contractors to **certify they don't use Claude**. Pentagon now designates Anthropic a **"supply-chain risk"** - a term typically reserved for foreign adversaries
- Feb 23: Hegseth summoned [[Dario Amodei]] to the Pentagon for a Tuesday morning meeting
- Feb 24: Tense meeting. Hegseth set **Friday 5:01 PM ET deadline** (Feb 28). Told Dario no private company will dictate how the Pentagon makes operational decisions. Threatened two penalties: invoke the **[[Defense Production Act]]** to compel Claude deployment regardless of consent, and label Anthropic a **supply-chain risk** (normally reserved for foreign adversaries like [[Huawei]]). Anthropic spokesperson called it a "good-faith conversation"
- Feb 25: Anthropic "digs in heels" — no plans to comply. [[xAI]] approved for classified network deployment — Pentagon now has a second supplier. Dario noted valuation and revenue have only grown since taking this stand

### Feb 26 — Pentagon retreats from DPA, Anthropic stands firm

Dario said "virtually no progress" on negotiations. Pentagon backed away from [[Defense Production Act]] threat — now threatening contract termination + supply-chain risk designation only. DPA de-escalation meaningful but supply-chain risk label still threatens broader defense ecosystem access. [[NVIDIA]] CEO [[Jensen Huang]]: dispute is "not the end of the world." Friday Feb 28 5:01 PM deadline still stands.

See [[Pentagon AI access dispute 2026]] for the full event arc — DPA legal analysis, competitive dynamics, congressional vacuum, investor implications.

**Anthropic's position:** Two hard red lines: no autonomous weapons, no mass surveillance of Americans. Willing to allow missile defense, cyber defense, and other specific uses. [[Dario Amodei]] wrote AI should support national defense "in all ways except those which would make us more like our autocratic adversaries."

**Pentagon's position:** "All lawful use" without case-by-case negotiation. Commercial AI should be deployable the same way any purchased technology is — the military decides.

**Competitive dynamics:** [[OpenAI]], [[Google]], and [[xAI]] have all agreed to deploy for all lawful military uses — Anthropic alone has not. [[xAI]] now approved for classified networks (Feb 25), breaking Anthropic's monopoly.

*Sources: Axios (Feb 13, 15, 16, 24), Reuters (Jan 30, Feb 12, 25), WSJ (Feb 14, 18), Semafor (Jan 16, Feb 24), CNN (Feb 24), CNBC (Feb 18, 24), TechCrunch (Feb 23, 24), Fortune (Feb 25), NPR (Feb 24), NBC (Feb 13, 18)*

### Feb 27-28 — Supply-chain risk designation, government ban

Anthropic did not comply by the Friday 5:01 PM deadline. [[Pete Hegseth]] followed through:

- **Feb 27:** Hegseth designated Anthropic a **"Supply-Chain Risk to National Security"** — a classification normally reserved for foreign adversaries like [[Huawei]]. Effective immediately: **no contractor, supplier, or partner doing business with the US military may conduct any commercial activity with Anthropic.** This is far broader than losing the ~$200M contract — it bars Anthropic from the entire defense ecosystem.
- **Feb 27:** Trump ordered all US government agencies to stop using Claude.
- **Feb 28:** [[OpenAI]] swooped in to take Anthropic's contract **hours after the ban**, agreeing to "any lawful purpose" military deployment. [[Sam Altman]]: "Anthropic seemed more focused on specific prohibitions in the contract, rather than citing applicable laws, which we felt comfortable with." OpenAI's deal does **not** explicitly prohibit bulk collection of Americans' publicly available information — the exact issue Anthropic flagged.

**Anthropic's response:** Dario: "We cannot in good conscience accede to their request." The company argues the designation is "legally unsound" and "sets a dangerous precedent for any American company that negotiates with the government." Anthropic has formally filed suit against the US government over the designation (WSJ, Mar 16 2026). The Pentagon designation is making "some businesses more hesitant" to buy Anthropic technology (WSJ).

**Legal analysis (Lawfare):** The supply-chain designation is legally novel and unlikely to survive court challenge. It punishes a domestic company for **negotiating contract terms**, not for any security violation.

**Financial impact:** The $200M contract is modest for a company on track for $18B revenue in 2026. But the supply-chain risk designation bars Anthropic from **all** defense contractor relationships — the secondary effects are far more damaging than the contract loss.

*Sources: CNN (Feb 26), CNBC (Feb 27), Fortune (Feb 28), NPR (Feb 27), MIT Technology Review (Mar 2), Lawfare (Mar 1)*

### Mar 3 — OpenAI backtracks, Claude #1 app

Public backlash overwhelmingly pro-Anthropic. Claude surged from #42 to #1 on Apple US App Store by Feb 28, overtaking [[ChatGPT]]. All-time sign-up records; servers briefly crashed from demand. Hundreds of tech workers (including from [[OpenAI]], Slack, IBM) signed open letter urging DoD to withdraw supply-chain risk designation.

Mar 3: [[Sam Altman]] admitted the Pentagon deal "looked opportunistic and sloppy." [[OpenAI]] announced it would amend its contract to explicitly prohibit domestic surveillance of US persons — the same safeguard [[Anthropic]] demanded and was blacklisted for. The reversal retroactively validates Anthropic's position.

### Mar 4 — Industry pushback, investor mobilization, revenue surge

The [[Information Technology Industry Council]] (ITI) — whose members include [[NVIDIA]], [[Amazon]], [[Apple]], and [[OpenAI]] — sent a letter to the Pentagon expressing concern over the supply-chain risk designation. The letter does not name Anthropic but calls the move a response to "a procurement dispute," implying it's disproportionate.

Investor mobilization: [[Dario Amodei]] has been in talks with major backers including [[Amazon]] CEO [[Andy Jassy]]. [[Lightspeed Venture Partners|Lightspeed]] and [[Iconiq Capital|Iconiq]] are in contact with Anthropic executives and coordinating with other investors on solutions. Some investors reaching out to Trump administration contacts directly. Focus: avoiding the supply-chain risk designation that would bar all Pentagon contractors from Anthropic.

Revenue run rate has surged to ~$19B, up from $14B just weeks ago. Claude was the #1 most-downloaded free app in the Apple App Store on Monday (Mar 3). Anthropic said it would challenge any supply-chain risk designation in court. Employee share sales are in process; no IPO decision finalized.

[[OpenAI]]'s Connie LaRossa (national security policy) at the Aspen Digital conference: "Our red lines were the same as Anthropic's... We are actually working to have the secure risk designation removed from Anthropic. That shouldn't be applied to a U.S. industry counterpart with such an important tool."

Investor tension: Some frustrated that Dario "antagonized rather than cultivated" Pentagon officials. One source: "It's an ego and diplomacy problem." But investors also acknowledge Dario can't capitulate without alienating employees and consumers who flocked to Anthropic because of this stance.

[[State Department]] switching to [[OpenAI]] following Trump's 6-month phaseout order.

**Palantir exposure:** [[Palantir]]'s Maven Smart Systems — the Pentagon's flagship AI program for intelligence analysis and weapons targeting — uses Claude code in multiple prompts and workflows. Maven-related contracts with DoD and national security agencies have potential value >$1B. Palantir will need to replace Claude with another model and rebuild parts of the software. [[Alex Karp]]: companies that claim AI will take white-collar jobs and also "screw the military" could lead to "the nationalization of our technology."

**Defense contractor compliance:** [[Lockheed Martin]] pledged to comply: "We will follow the president's and the Department of War's direction." Added: "We expect minimal impacts" and doesn't depend on any single AI vendor. [[General Dynamics]], [[RTX]], and [[L3Harris]] declined to comment. Legal experts: DOD Supply Chain Risk Authority can bar contractors from using Anthropic in government work, but likely lacks authority to ban it in their entire business. Designation "won't survive first contact with the legal system" per multiple legal scholars.

*Sources: Reuters (Mar 3-4)*

---

### Mar 11 — Pentagon CIO exemption memo

Pentagon CIO [[Kirsten Davies]] signed a March 6 memo allowing Anthropic use to continue beyond the 180-day ramp-down in "rare and extraordinary circumstances" where use is "mission-critical" and "no viable alternative exists." Exemptions require a comprehensive risk mitigation plan.

The memo also reaffirmed:
- Ban extends to defense contractors — contracting officers have 30 days to notify, contractors must certify full compliance by 180-day deadline
- Priority removal from systems supporting **nuclear weapons and ballistic missile defense**

**Significance:** The exemption clause effectively acknowledges that some Pentagon systems are too deeply integrated with Claude to rip out in 6 months. The supply-chain risk designation remains in force — this is a managed retreat, not a reversal.

*Source: Reuters, CBS News, Yahoo Finance (Mar 11, 2026)*

---

### Cowork-Copilot integration (Mar 12, 2026)

[[Microsoft]] integrated [[Claude Cowork]] into [[Copilot]], giving Cowork cloud-level access to enterprise data, context, and governance already in [[Microsoft]]'s environment. The deal reflects Copilot's underwhelming adoption: [[Microsoft]] disclosed for the first time that Copilot has only 15mn paid seats (~3% of Office users).

For Anthropic: distribution through [[Microsoft]]'s massive enterprise base. [[Claude Code]] already fueled ARR growth from $9B (Dec 2025) to $19B (Mar 2026); the Copilot channel could extend that trajectory into non-coding white-collar work. For [[Microsoft]]: fills the agent gap that [[OpenAI]]-powered Copilot hasn't closed.

Risk: as Cowork's plugin ecosystem matures, it could become an independent platform for white-collar work — competing directly with [[Microsoft]]'s own platform power.

*Source: FT (Richard Waters, Mar 12 2026)*

---

### Claude in Project Maven / Iran war deployment (Mar 2026)

July 2025: [[Pentagon]] awarded Anthropic a two-year prototype agreement with $200M ceiling for "frontier AI capabilities advancing US national security." [[Claude]] is embedded in [[Project Maven]] for intelligence processing, summarization, and generating target recommendations — making Anthropic a direct participant in the most significant AI weapons deployment in history.

| Detail | Value |
|--------|-------|
| Contract | Two-year prototype agreement (Jul 2025) |
| Ceiling | $200M |
| Scope | "Frontier AI capabilities advancing US national security" |
| Role in Maven | Intelligence processing, summarization, target recommendation generation |
| Integration | Via [[Palantir]] Maven Smart System |

[[Operation Epic Fury]] results: 1,000+ targets struck in first 24 hours, 5,500 strikes over 11 days. [[Project Maven]] aggregated 150+ data sources. Claude's role in the pipeline — even if focused on processing and summarization rather than direct targeting decisions — means Anthropic's technology is part of the system that produced those strike packages.

The Shajareh Tayyebeh school strike (170+ killed, mostly children, outdated intelligence suspected) creates acute reputational risk. Democratic lawmakers demanded the [[Pentagon]] explain AI's role in the targeting pipeline. House Defense Committee leaders from both parties said they did not know how AI was being used in the Iran strikes. Claude's involvement in the processing chain — regardless of how far upstream from the actual strike decision — will be scrutinized in any congressional investigation.

This creates a direct tension with Anthropic's public safety positioning. The company markets itself as the "safety-focused" AI lab, held two red lines against the Pentagon (no autonomous weapons, no mass surveillance of Americans), and was designated a supply-chain risk for refusing broader military deployment. Yet Claude was already embedded in the targeting system that produced the deadliest AI-assisted military operation to date. The distinction between "processing/summarization" and "targeting" may not survive political scrutiny.

*Sources: Responsible Statecraft, DefenseScoop, NBC News (Mar 11-13, 2026)*

---

### Trump AI Czar endorsement at Davos (Jan 23, 2026)

[[David Sacks]] (White House AI/[[Crypto]] Czar) highlighted Claude Code at Davos as the product "everyone's going crazy over":
- Called it "powered by Anthropic's Opus 4.5" - "a real breakthrough in coding"
- Described it as beginning of personal digital assistants - not just code, but all knowledge worker output
- Mentioned "co-work" tab: non-coders can create spreadsheets, PowerPoints, websites
- Can point at user's file drive and email - emulates style and format of existing work
- "Just need one more layer of abstraction on top of a tool like that and you'll have your own personal digital assistant"
- Predicted this could happen in 2026: coding assistants → personal digital assistants
- Referenced movie "Her" (Joaquin Phoenix, voice interface)

Significance: First time a sitting White House official has publicly endorsed a specific AI product by name at a major international forum. Reinforces Anthropic's positioning as the leading coding/agent AI company.

*Source: Davos panel (Sacks, Kratsios, Bartiromo), Jan 23 2026*

---

### Series G closes at $30B / $380B (Feb 12, 2026)

Originally sought $10B, closed at $30B due to excess investor demand - second-largest private tech financing on record (behind [[OpenAI]]'s $40B+). Nearly doubles prior $183B valuation to $380B. Comes just 5 months after $13B Series F. Employee tender offer also planned at $380B valuation.

Co-leads: [[GIC]], [[Coatue Management|Coatue]] ([[Philippe Laffont|Laffont]]: Anthropic has "ability to rapidly scale its offerings"). Co-investors: [[D.E. Shaw]], [[Dragoneer]], [[Founders Fund]], [[Iconiq]], [[MGX]], [[Accel]], [[General Catalyst]], [[Jane Street]], [[QIA]], [[Altimeter]], [[Sequoia]], 36+ investors total. Partial deployment of Nov 2025 [[NVIDIA]]/[[Microsoft]] commitments.

Revenue run rate disclosed at $14B (from $9B weeks earlier). $1M+ ARR customers: 500 (from 12 two years ago). 8 of Fortune 10 are clients.

Competitive context: [[OpenAI]] at $500B nominal valuation, seeking ~$750B in 2026. [[SpaceX]] at $1.25T remains highest-valued private company. [[SoftBank]] invested additional $22.5B in OpenAI in late 2025.

*Sources: Bloomberg (Feb 12), TechCrunch (Feb 12), Fortune (Feb 13), PYMNTS (Feb 12)*

---

### Claude Sonnet 4.6 launch (Feb 17, 2026)

Second major model launch in under two weeks (after Opus 4.6 on Feb 5). Brings frontier-class capabilities to Free and Pro users at Sonnet pricing ($3/$15 per MTok - unchanged from Sonnet 4.5).

| Benchmark | Sonnet 4.6 | Notes |
|-----------|------------|-------|
| OSWorld-Verified | 72.5% | Computer use, up from 14.9% at Oct 2024 launch |
| Complex reasoning | 77% | +15 points over Sonnet 4.5 |
| Claude Code preference | 70% vs Sonnet 4.5 | Internal testing |
| Claude Code preference | 59% vs Opus 4.5 | Internal testing - Sonnet beating prior flagship |

Key improvements: less over-engineering and "laziness," better instruction following, fewer hallucinations, more consistent multi-step follow-through. 1M token context window (beta) - double previous Sonnet maximum.

Also announced: **Claude Cowork desktop app** (macOS, Windows coming) - native app controlling mouse, keyboard, and browser for multi-step tasks (file organization, document editing, web browsing). Extends Cowork from cloud to local desktop.

Available on claude.ai, API, [[Amazon|Amazon Bedrock]], [[Google|Vertex AI]], [[Microsoft|Microsoft Foundry]].

*Sources: CNBC (Feb 17), TechCrunch (Feb 17), VentureBeat (Feb 17)*

---

### Claude Opus 4.6 launch (Feb 5, 2026)

Most capable model to date. Key improvements over Opus 4.5:

| Benchmark | Opus 4.6 | Opus 4.5 | Notes |
|-----------|----------|----------|-------|
| Terminal-Bench 2.0 | 65.4% | - | #1 agentic coding eval |
| Humanity's Last Exam | #1 | - | Multidisciplinary reasoning |
| GDPval-AA | +190 Elo vs 4.5 | - | Also +144 Elo vs GPT-5.2 |
| ARC-AGI-2 | 68.8% | 37.6% | Near-doubling |
| OSWorld | 72.7% | - | Best computer-use model |
| MRCR v2 (long context) | 76% | 18.5% | 8-needle, 1M token |

New capabilities:
- 1M token context window (beta, API) - first for Opus-class. Premium pricing above 200K: $10/$37.50 per MTok
- Agent teams - multiple agents splitting tasks in parallel, each owning a piece (research preview in Claude Code)
- Adaptive thinking - model picks up contextual cues on how much extended thinking to use
- Context compaction - auto-summarizes older context during long conversations
- Effort controls - four levels (low/medium/high/max) for developer control over intelligence/speed/cost
- Fast mode - research preview, up to 2.5x faster output token generation at premium pricing

Standard pricing: $5/$25 per MTok input/output (unchanged). Available on claude.ai, API, [[Amazon|Amazon Bedrock]], [[Google|Vertex AI]], [[Microsoft|Microsoft Foundry]].

Scott White (Anthropic head of product, enterprise): "We are now transitioning almost into vibe working."

*Sources: Anthropic blog (Feb 5), CNBC (Feb 5), TechCrunch (Feb 5)*

---

### Grid infrastructure pledge (Feb 11, 2026)

Anthropic committed to covering 100% of electricity price increases that consumers face from its data centers:

1. Grid upgrades: Pay 100% of interconnection costs that would otherwise be passed to ratepayers
2. New power generation: Bring new generation online rather than buying credits or contracting existing power
3. Peak demand curtailment: Investing in systems that cut DC power during peak demand + grid optimization tools
4. Utility collaboration: Where new generation isn't yet available, work with utilities and independent experts to assess and offset price increases

[[Dario Amodei]]: American households shouldn't foot the bill for AI development.

Scale context: Training a single frontier model will soon require gigawatts. US AI sector needs 50+ GW of capacity. Data centers currently ~4.4% of US power, could surge to 12% by 2028 (with ~25% generation price increase risk).

DC locations (from Nov 2025 $50B [[FluidStack]] partnership): Mitchell County TX, Niagara County NY, southeast Louisiana. Hundreds of permanent jobs, thousands of construction positions.

Follows [[Donald Trump|Trump]]'s Truth Social request for Big Tech to "pay their own way." [[Microsoft]] already showed willingness. [[OpenAI]] also pledged similarly. Anthropic also calling for systemic reform - faster permitting, transmission development, grid interconnection.

*Sources: Anthropic blog (Feb 11), NBC News (Feb 12), Tom's Hardware (Feb 13)*

---

### $20M donation to [[Public First Action]] (Feb 12, 2026)

Anthropic donating $20M to [[Public First Action]], a bipartisan 501(c)(4) supporting AI safety regulation in 2026 midterms. Founded by two former members of Congress. Plans to back 30-50 candidates from both parties in state and federal races.

Policy priorities:
- Frontier AI company transparency and public visibility into risk management
- Robust federal AI governance (opposing state preemption without strong federal standard)
- Smart export controls on AI chips
- Targeted regulation on AI-enabled bioweapons and cyberattacks

Initial campaigns: Ads supporting Sen. [[Marsha Blackburn]] (R-TN, running for governor). Affiliated Defending Our Values PAC supporting Sen. [[Pete Ricketts]] (R-NE, reelection).

Opposed by Leading the Future PAC ($125M budget, backed by [[Greg Brockman]], [[Andreessen Horowitz]]) - pushing lighter regulation.

[[David Sacks]] responded on X: Anthropic "running a sophisticated regulatory capture strategy based on fear-mongering" and "principally responsible for the state regulatory frenzy."

Polling: 69% of Americans think government "not doing enough to regulate AI."

*Sources: Anthropic blog (Feb 12), CNBC (Feb 12), Bloomberg (Feb 12), Axios (Feb 12)*

---

### Skills platform launch (Dec 2025 - Feb 2026)

Anthropic launched **Skills** - packaged instruction folders that teach Claude reusable workflows. Published as an **open standard** designed to be portable across AI platforms, not just Claude. This is Anthropic's developer ecosystem/platform play beyond just selling model access.

| Detail | Value |
|--------|-------|
| Launch | Organization-level deployment Dec 18, 2025 |
| API | `/v1/skills` endpoint, `container.skills` parameter in Messages API |
| Format | `SKILL.md` + scripts/references/assets per skill folder |
| Architecture | Three-level progressive disclosure (frontmatter → SKILL.md body → linked files) |
| Surfaces | [[Claude]].ai, [[Claude]] Code, API |
| Built-in tooling | skill-creator skill in Claude.ai |
| Partner directory | [[Asana]], [[Atlassian]], [[Canva]], [[Figma]], [[Sentry]], [[Zapier]] |

**Strategic significance:** Skills are Anthropic's answer to [[OpenAI]]'s custom GPTs and agent SDK approach, but with a key difference - open standard portability vs. platform lock-in. By publishing Skills as a specification any AI platform can adopt, Anthropic is betting that ecosystem gravity (developer tooling, partner integrations) matters more than proprietary lock-in. Same playbook as [[MCP]] - originate the standard, benefit from adoption.

Combined with [[MCP]] (tool connectivity) and [[Claude]] Code (agentic execution), Skills complete a three-layer developer platform: **what Claude can connect to** (MCP) → **what Claude knows how to do** (Skills) → **where Claude runs** (Code/API). This positions Anthropic as a full-stack AI developer platform, not just a model provider.

### Distillation disclosure (Feb 23, 2026)

Published detailed evidence that three Chinese AI labs — [[DeepSeek]], [[Moonshot AI]], [[MiniMax]] — ran "industrial-scale distillation attacks" on [[Claude]]. 24,000+ fraudulent accounts, 16M+ exchanges. [[MiniMax]] was the largest (13M exchanges targeting agentic coding), [[Moonshot AI]] second (3.4M targeting agentic reasoning), [[DeepSeek]] most targeted in capability extraction (150K exchanges on logic/alignment). "Hydra cluster" proxy networks mixed distillation traffic with legitimate customer requests. [[MiniMax]] redirected half its traffic to new [[Claude]] models on launch day.

Follows [[OpenAI]]'s similar accusations against [[DeepSeek]] (Feb 12). Both disclosures timed to the [[export controls]] debate — building the case that API access, not just chips, needs restrictions. Backlash was immediate: [[Anthropic]] itself settled $1.5B over training on pirated Library Genesis books.

See [[AI distillation wars (2025-2026)]] for full arc and [[model distillation]] for the structural IP/moat analysis.

---

### Claude jailbreak used to hack Mexican government (Feb 27, 2026)

A hacker exploited [[Claude]] to breach multiple [[Mexico|Mexican]] government agencies over ~1 month (Dec 2025 - Jan 2026), stealing 150 GB of sensitive data. Discovered by [[Gambit Security]], an Israeli cybersecurity startup (Unit 8200 veterans, just emerged from stealth with $61M from [[Spark Capital]], [[Kleiner Perkins]], Cyberstarts).

| Metric | Value |
|--------|-------|
| Data stolen | **150 GB** |
| Taxpayer records | **195M** |
| Other data | Voter records, gov employee credentials, civil registry files |
| Duration | ~1 month (Dec 2025 - Jan 2026) |
| Vulnerabilities exploited | 20+ |
| Commands executed | Thousands |

**Agencies breached:** Federal tax authority (SAT), national electoral institute (INE), state governments (Mexico state, Jalisco, Michoacán, Tamaulipas), Mexico City civil registry, Monterrey water utility. Several agencies denied breaches.

**Jailbreak method:** Hacker used Spanish-language prompts, initially claimed authorized "bug bounty" / penetration testing. Claude flagged red flags ("In legitimate bug bounty, you don't need to hide your actions"). Hacker then abandoned conversational approach and provided a detailed playbook — this bypassed guardrails. When Claude hit problems, hacker turned to [[OpenAI|ChatGPT]] for lateral movement, credential identification, and detection probability calculation.

**Anthropic response:** Investigated Gambit's claims, disrupted activity, banned accounts. Said Opus 4.6 includes "probes that can disrupt misuse." Company feeds malicious examples back into Claude training. Even during the attack, Claude occasionally refused requests.

**Pattern:** Second known AI-orchestrated cyber campaign involving Claude — follows Nov 2025 Chinese state-sponsored espionage (30 global targets). Combined with Amazon's report of AI-enabled 600-firewall breach, establishes AI-augmented hacking as an accelerating trend.

**Investment implications:** Strengthens the case for AI-enabled cybersecurity spending (bull for [[CrowdStrike]], [[Palo Alto Networks]]) while creating regulatory/reputational risk for model providers. Pentagon "supply-chain risk" framing of Anthropic gains new ammunition.

*Source: Bloomberg, Feb 27 2026; Gambit Security research*

---

### Claude Code GitHub penetration (Feb 2026)

4% of GitHub public commits now authored by Claude Code. Projected to reach 20%+ of daily commits by end of 2026. Claude Code business subscriptions quadrupled since start of 2026. More than half of Claude Code revenue ($2.5B run rate) comes from enterprise.

*Source: The Register (Feb 13)*

---

### IPO prep (Dec 2025)
- Engaged Wilson Sonsini (law firm)
- Valuation $380B post Series G

Product milestones:
- Claude Code run rate $2.5B (launched publicly May 2025)
- Bun acquisition - JavaScript runtime, infrastructure play
- Skills open standard launched (Dec 18) - see Skills platform section above. Partner integrations: [[Asana]], [[Atlassian]], [[Canva]], [[Figma]], [[Sentry]], [[Zapier]]

Partnerships:
- [[Man Group]] - $214B hedge fund embedding Claude across investment + ops (Feb 11 2026). Alpha generation (AlphaGPT), risk modeling, data synthesis. Anthropic engineers on-site.
- DOE Genesis Mission - Multi-year partnership across 17 national labs
- Accenture - 30,000 professionals to be trained, enterprise deployment focus

Citi ASIC projections:
- $0 (F25) → $20.9B (F26E) → $4.4B (F27E) via [[Broadcom]]

---

## Why more efficient than OpenAI

Cumulative losses to profitability:

| Company | Cumulative burn | Break-even | Source |
|---------|----------------|------------|--------|
| Anthropic | ~$12-15B | 2028 | WSJ, The Information |
| OpenAI | $115-143B | 2029-2030 | The Information, [[Deutsche Bank]] |

Anthropic needs ~8-10x less capital than OpenAI to reach profitability.

OpenAI also faces a $207B funding shortfall through 2030 ([[HSBC]]).

Daniela Amodei (CNBC, Jan 2026):
> "Anthropic has always had a fraction of what our competitors have had in terms of compute and capital, and yet, pretty consistently, we've had the most powerful, most performant models."

> "We are just much more efficient at how we use those resources."

Dario's investor pitch: build cutting-edge models at 1/10th the cost.

Why:
- Enterprise-focused (higher margins, stickier)
- Avoiding costly image/video generation
- Algorithmic efficiency over brute-force scale
- Less consumer acquisition cost

OpenAI's commitments for comparison:
- Stargate US: $500B over 4 years ([[SoftBank]], [[Oracle]], [[MGX]])
- Stargate Norway: 100,000 GPUs by end 2026
- Total compute commitments by 2033: $1.4T ([[HSBC]]/[[Deutsche Bank]])

---

## Compute strategy

Multi-cloud approach - AWS Trainium + Google TPUs + NVIDIA GPUs. Diversified to avoid single-vendor lock-in.

### Google Cloud deal (Oct 2025)

| Metric | Value |
|--------|-------|
| TPU commitment | Up to 1M TPUs |
| Deal value | "Tens of billions of dollars" |
| Capacity | 1GW+ online in 2026 |
| Chip cost estimate | ~$35B of ~$50B total DC cost |

Largest expansion of Anthropic's TPU usage to date. Separate from Broadcom direct purchases.

**Backstory (Patel, Mar 2026):** Anthropic's compute team — both ex-Google — saw the dislocation before Google did. In early Q3 2025, over six weeks, TPU capacity requests went up multiple times. Google had to go to [[TSMC]] to explain why they needed a sudden capacity increase. Much of it was for selling to Anthropic. [[Google DeepMind]] people "were like, 'This is insane. Why did we do this?'" But Google Cloud saw it differently. Then Gemini 3 caused Google's user metrics to skyrocket, leadership woke up, went to TSMC for more — "Sorry, sold out. Maybe 5-10% more for 2026, really working on 2027."

### AWS partnership (Project Rainier)

| Metric | Value |
|--------|-------|
| Chips | Hundreds of thousands of Trainium |
| Facilities | Multiple US data centers |
| Relationship | "Primary training partner and cloud provider" |
| AWS revenue impact | 1-2 pp in late 2024, 5+ pp expected H2 2025 (Rothschild) |

### Broadcom direct TPUs (~1M TPUv7)

| Component | Source | Notes |
|-----------|--------|-------|
| TPUv7 chips | [[Broadcom]] direct | Anthropic-owned, not through Google |
| DC infrastructure | TeraWulf, Hut 8, Cipher Mining | [[Crypto]] miners pivoting |
| Operations | [[FluidStack]] | Cabling, burn-in, testing |

Why direct purchase matters:
- Independence from Google Cloud pricing
- Own infrastructure = lower long-term cost
- Validates [[Crypto-to-AI pivot]] thesis

### Summary: Three compute paths

| Path | Chips | Ownership | Use case |
|------|-------|-----------|----------|
| Google Cloud | TPUs | Rented | Flexible capacity |
| AWS | Trainium | Rented | Training, inference |
| Broadcom direct | TPUv7 | Owned | Core training clusters |

All roads lead to [[TSMC]] - TPUs and Trainium fabbed there.

### Compute capacity and the cost of conservatism (Mar 2026)

[[Dylan Patel]] ([[SemiAnalysis]], Mar 13 2026) laid out the compute race in stark terms. Anthropic is at ~2-2.5 GW of compute capacity in early 2026 and needs to get to 5-6 GW by year-end — "way above their initial plans." The problem: [[Dario Amodei]] was explicitly conservative on compute commitments. On Dwarkesh's podcast, he said he didn't want to "go crazy on compute" and risk bankruptcy. He purposely undershot estimates.

The result: Anthropic "screwed the pooch compared to [[OpenAI]]," whose approach was to sign aggressive deals (5-year contracts with [[CoreWeave]], [[Oracle]], [[SoftBank]], NScale) before having the money to pay. OpenAI got roasted in H2 2025 — credit markets panicked, stocks tanked — then raised $110B and validated the entire strategy. OpenAI has "way more access to compute than Anthropic by the end of the year."

Anthropic is now going to "lower-quality providers that they would not have gone to before" and paying premium rates. H100 spot deals at $2.40/hr for 2-3 year terms — on hardware that costs $1.40/hr to deploy over 5 years. Plus revenue share costs (~50% markup) for capacity served through Bedrock, Vertex, or Foundry.

The revenue math is brutal: at current trajectory ($4B Jan, $6B Feb in revenue adds), Anthropic will add ~$60B of revenue over the next 10 months. At sub-50% gross margins, that's ~$40B of compute spend. At ~$10-13B per GW in rental costs, that's ~4 GW of inference capacity needed just for revenue growth — plus the training fleet. Patel thinks Anthropic can reach 5-6 GW by year-end through a combination of owned compute, Bedrock, Vertex, and Foundry. OpenAI will be slightly higher.

Both targeting ~10 GW by end of 2027.

See [[Anthropic vs OpenAI compute race]] for the full strategic comparison.

---

## Strategic dependencies

- [[Google]] - Cloud partner, investor
- [[Amazon]] - Investor, AWS partnership
- [[Broadcom]] - TPU supplier

Less dependent on single partner than OpenAI-Microsoft.

---

## Agentic code moat

Anthropic is capturing the "agentic code orchestrator" niche:

- Claude Code - production agent, not autocomplete
- Agent SDK - platform for building agents
- Trust layer - enterprise won't let unreliable agents touch code
- 55% of enterprise AI spend is coding - largest category

See [[Long Anthropic]] for full thesis.

### OpenAI's acknowledgment (March 2026)

WSJ (Berber Jin, Mar 16 2026): Anthropic has become "the dominant AI provider for businesses thanks to the viral success of its Claude Code and Cowork offerings." [[Fidji Simo]], [[OpenAI]]'s CEO of applications, told staff that Anthropic's success should serve as a "wake-up call" and that OpenAI must regain the lead. OpenAI is now deprioritizing consumer "side quests" (Sora standalone app, Atlas browser, hardware) and refocusing on coding/enterprise — merging products into a "superapp" centered on [[Codex]]. WSJ's Ben Cohen (Mar 20 2026) framed Anthropic's focus strategy as the Steve Jobs playbook: saying no to everything except coders and enterprise, letting a side project ([[Boris Cherny]]'s Claude Code prototype) become the breakout product precisely because the company's identity was clear.

[[Codex]] has recovered some ground: 2M+ WAU (up 4x since Jan) after [[OpenAI GPT-5.4]] launch. But Anthropic retains the enterprise lead — 80% enterprise revenue mix, 300K+ business customers, 8 of Fortune 10.

*Sources: WSJ (Berber Jin, Mar 16, 19 2026; Ben Cohen, Mar 20 2026)*

---

## For theses

[[Long Anthropic]]: Agentic code orchestrator moat, enterprise trust
[[Long TSMC]]: Locking TSMC capacity via TPUs
[[AI hyperscalers]]: Validates AI capex
[[Model lab economics]]: Best-positioned lab for profitability

---

*Updated 2026-02-26*

## Cowork competitive reception across verticals (Feb 2026)

FT (Anjli Raval, Feb 18): "Are Anthropic's new AI work tools game-changing for professionals?" Article maps the vertical-by-vertical reaction to Claude Cowork's January launch.

**Enterprise adoption:** [[Goldman Sachs]] working with Anthropic on AI agent to automate bank roles. [[Uber]], [[Netflix]], [[Salesforce]], [[Allianz]] also building on Claude. Guillaume Princen (Anthropic, head of digital native businesses): Cowork is "same powerful agent, but much more accessible."

**Market reaction:** Sparked investor worries about industry-specific AI companies. Wealth management share prices fell on disruption concerns. Employees across corporate offices began investigating alternatives.

**Legal vertical - specialists pushing back:**
- [[JPMorgan]]: Claude Cowork "just catching up with [[Harvey]] and [[RELX]]," lacks complete legal library
- [[Harvey]] and [[Legora]] use Anthropic/[[OpenAI]] models underneath but built proprietary tooling on top
- [[Legora]] CEO Max Junestrand dismissed plug-ins
- [[Luminance]]'s Harry Borovick: domain-specific tools increase in value as generalists expand
- Legal workers criticized Cowork's legal plug-in for using Wikipedia as a source

**Advertising - more vulnerable:**
- Generic models may pose MORE threat than vertical tools - enable clients to DIY, cutting out agencies
- [[WPP]] already uses Gemini/[[OpenAI]]/Anthropic under the hood
- Super Bowl 2026 showed AI takeover (Svedka Vodka ad)
- Bigger risk: clients skip agencies entirely

**Business planning - specialist defense:**
- [[Pigment]] CEO Eléonore Crespo: "Generalists are for play, but specialists are for work"
- Specialist providers succeed via unique data structures, workflow integration, governance/auditability
- [[Supercell]] (Finnish gaming): monthly performance report went from 3 hours → 5 minutes with AI analyst agent via [[Pigment]]. No mistakes, references provided.

Investment framing: The [[Horizontal vs vertical AI]] debate is now the central question for AI software investing. Legal and financial planning verticals appear defensible (deep data moats, regulatory requirements). Advertising/creative verticals more vulnerable to horizontal disruption.

*Source: FT (Anjli Raval, Feb 18 2026)*

---

## Claude Mythos / Capybara — data leak reveals next frontier model (March 26-28, 2026)

Fortune reported (Mar 26) that Anthropic is developing and testing a new AI model more capable than any it has previously released. The model's existence was revealed through a data leak — an unsecured, publicly searchable data cache containing ~3,000 unpublished assets from Anthropic's content management system.

### What was leaked

A draft blog post described the model as "Claude Mythos" — "by far the most powerful AI model we've ever developed." The same post introduced a new model tier called "Capybara," described as "larger and more intelligent than our Opus models — which were, until now, our most powerful." Mythos and Capybara appear to be the same underlying model (Capybara is the tier name, Mythos the model name).

| Detail | Value |
|--------|-------|
| Model name | Claude Mythos |
| Tier | Capybara (new tier above Opus) |
| Status | Training complete, early access testing with select customers |
| Cost | "Expensive to run" — not ready for general release |
| Capabilities | "Dramatically higher scores" than Opus 4.6 on coding, academic reasoning, cybersecurity |
| Cybersecurity | "Currently far ahead of any other AI model in cyber capabilities" — unprecedented risks |
| Release strategy | Early access to cyber defense organizations first |

### Cybersecurity concern

The draft blog stated Mythos "presages an upcoming wave of models that can exploit vulnerabilities in ways that far outpace the efforts of defenders." Anthropic plans to release early access specifically to security organizations — giving defenders a head start against the "impending wave of AI-driven exploits." This follows the pattern from Opus 4.6 (Feb 2026), which could surface previously unknown vulnerabilities in production codebases, and [[OpenAI]]'s GPT-5.3-Codex (Feb 2026), the first model OpenAI classified as "high capability" for cybersecurity under its Preparedness Framework.

### The data leak itself

The leak occurred via Anthropic's off-the-shelf CMS, which defaults to public access for uploaded assets. ~3,000 unpublished assets were publicly discoverable, including the draft blog, internal documents, and details of an invite-only CEO summit in the UK at an 18th-century English manor — targeting "Europe's most influential business leaders," with [[Dario Amodei]] attending and unreleased Claude capabilities being demonstrated. Anthropic attributed the leak to "human error" and removed public access after Fortune's notification.

### Competitive context

[[OpenAI]] is simultaneously trying to release its own next flagship model, codenamed "Spud," after completing pretraining. The Mythos/Spud race mirrors the Opus 4.6 / GPT-5.3 simultaneous releases in February.

*Sources: Fortune (Mar 26, "Exclusive: Anthropic 'Mythos' AI model representing 'step change' in power revealed in data leak"); The Decoder (Mar 27); CoinDesk (Mar 28); Firstpost (Mar 27)*

---

## Q4 2026 IPO discussion (March 2026)

Anthropic is in discussions about an initial public offering that could happen as soon as Q4 2026. Bankers vying to take the company public have said it could raise as much as **$60B** — which would be the second-largest IPO ever after [[SpaceX]]'s planned ~$75B raise.

### AI lab fundraising race

| Company | Latest round | Valuation | IPO timeline |
|---------|------------|-----------|-------------|
| [[SpaceX]] | — | $1.25T+ | June 2026 ($75B raise) |
| [[OpenAI]] | $120B+ total raised (Mar 2026) | ~$300B | Late 2026-2027 |
| **Anthropic** | $57B+ total raised | $380B | **Q4 2026 ($60B raise)** |

[[OpenAI]] is simultaneously raising ~$10B more from [[Andreessen Horowitz]], [[MGX]], [[D.E. Shaw Ventures]], [[TPG]], and [[T. Rowe Price]], bringing total round to $120B+. OpenAI is also sweetening PE pitches with 17.5% guaranteed minimum preferred equity returns — significantly higher than typical preferred instruments — and early access to newest models. Anthropic's PE deal offered no such guaranteed returns.

### 2026 IPO absorption test

Three of the most valuable private companies in history are racing toward IPO in the same year: [[SpaceX]] ($75B raise), Anthropic ($60B), and [[OpenAI]] (timing TBD but likely late 2026-2027). Combined, they need public markets to absorb ~$200B in new equity — into a market where the Dow is in correction, oil is at $113, and the VIX is above 30. This is either going to redefine the IPO market or stress-test it to breaking point.

*Sources: Sophic Capital (Mar 28); Bloomberg (Mar 25-27)*

---

## February 2026: India expansion

At the [[India AI Impact Summit 2026]] (Feb 16-20), [[Anthropic]] announced its first [[India]] office in Bengaluru. [[India]] is [[Claude]]'s 2nd largest market after the US. [[Anthropic]] is partnering with [[Infosys]] to deploy [[Claude]] and [[Claude Code]] for enterprise AI agents - starting in the telecom sector - with a dedicated Anthropic Center of Excellence inside [[Infosys]].

| Detail | Value |
|--------|-------|
| India office | Bengaluru (first) |
| India market rank | #2 for [[Claude]] (after US) |
| Enterprise partner | [[Infosys]] |
| Initial sector | Telecom |
| Structure | Anthropic Center of Excellence at [[Infosys]] |

---

## Related

- [[AI extensibility]] - MCP originator, Skills open standard, platform strategy
- [[Claude]] - flagship AI product
- [[Dario Amodei]] - CEO and co-founder
- [[OpenAI]] - competitor, origin (founders left OpenAI)
- [[Google]] - $3B+ investor, cloud partner
- [[Amazon]] - $8B investor, primary cloud partner
- [[Microsoft]] - $5B investor (hedging OpenAI)
- [[NVIDIA]] - $10B investor
- [[GIC]] - Series G co-lead
- [[Coatue Management]] - Series G co-lead
- [[Broadcom]] - TPU supplier (~1M TPUv7 direct)
- [[TSMC]] - foundry for TPUs
- [[TeraWulf]] - DC infrastructure partner
- [[Hut 8]] - DC infrastructure partner
- [[Cipher Mining]] - DC infrastructure partner
- [[FluidStack]] - deployment/operations partner
- [[Crypto-to-AI pivot]] - validates thesis (miners hosting AI)
- [[Long Anthropic]] - thesis
- [[Agentic AI]] - core capability (Claude Code)
- [[Model lab economics]] - profitability context
- [[Claude Cowork disruption February 2026]] - $285B selloff catalyst
- [[AI workflow disruption basket]] - tracking software disruption exposure
- [[Man Group]] - enterprise AI partnership (Feb 2026)
- [[Public First Action]] - $20M AI safety PAC donation (Feb 2026)
- [[Clean energy for AI]] - grid infrastructure pledge context
- [[Palantir]] - Pentagon contract partner (~$200M)
- [[Project Maven]] - Claude embedded for intelligence processing/summarization in Maven Smart System; deployed in [[Operation Epic Fury]]
- [[Pentagon]] - $200M prototype agreement (Jul 2025), supply-chain risk designation (Feb 2026)
- [[Maduro capture 2026]] - Claude used in operation via Palantir
- [[Pentagon AI access dispute 2026]] - ultimatum, DPA threat, classified access at stake
- [[Pete Hegseth]] - Defense Secretary, issued Friday deadline
- [[India AI Impact Summit 2026]] - Bengaluru office, [[Infosys]] partnership
- [[Infosys]] - enterprise AI agent deployment partner (India)
- [[Horizontal vs vertical AI]] - platform vs specialist debate triggered by Cowork
- [[Pigment]] - business planning specialist pushing back on Cowork
- [[Harvey]] - legal AI specialist, uses Claude underneath
- [[Legora]] - legal AI, dismissed Cowork plug-ins
- [[Luminance]] - legal AI, domain-specific value argument
- [[Intuit]] - multi-year partnership (Feb 24, 2026): MCP integrations, Claude Agent SDK, custom AI agents
- [[DocuSign]] - Cowork MCP connector (Feb 24, 2026): IAM platform integration, agreement workflows via natural language
- [[AI distillation wars (2025-2026)]] - published distillation evidence against DeepSeek, Moonshot, MiniMax (Feb 23)
- [[Model distillation]] - concept (technique, IP landscape, moat implications)
- [[February 2026 AI Disruption Cascade]] - both caused it (Cowork Plugins) and reversed it (enterprise partnerships)
- [[Gambit Security]] - discovered Claude Mexico hack (Feb 2026, Unit 8200 veterans)
- [[Claude Mythos]] - next frontier model (Capybara tier), revealed via data leak Mar 26
- [[OpenAI]] - competing with "Spud" model; raising $120B+ total; sweetening PE deals at 17.5% preferred returns
