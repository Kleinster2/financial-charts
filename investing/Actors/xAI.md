---
aliases: [Grok, Macrohard]
---
#actor #ai #hyperscaler #private

**xAI** — Elon Musk's AI company (Grok). Now a SpaceX subsidiary after Feb 2026 acquisition. Building massive GPU clusters. Macrohard project to simulate Microsoft with AI.

---

## Origin story

Musk's return to AI (mid-2023):

| Event | Date | Notes |
|-------|------|-------|
| Co-founded [[OpenAI]] | 2015 | Early backer and board member |
| Left OpenAI | 2018 | Clashed with leadership over direction |
| ChatGPT viral success | Nov 2022 | Musk watched from sidelines |
| Founded xAI | Mid-2023 | Nearly a year after ChatGPT |

Recruiting: Lured AI researchers from [[Google]], [[Microsoft]], and [[Tesla]] to compete with Sam Altman's OpenAI.

---

## Relevance to semis

xAI is emerging as a major AI infrastructure builder. Colossus cluster and expansion plans make them a significant chip buyer.

---

## Macrohard ("Human Emulators")

"Purely AI software company" (Aug 2025):

Musk's vision: simulate a Microsoft-scale software business entirely with [[AI agents]].

| Aspect | Details |
|--------|---------|
| Trademark | Filed Aug 1, 2025 |
| Name | Tongue-in-cheek Microsoft jab |
| Concept | [[AI agents]] running entire software company |
| Products | Human emulators — digital Optimus for knowledge work |
| Revenue target | $10-100B (working backwards from this target) |

Musk quote: "In principle, given that software companies like Microsoft do not themselves manufacture any physical hardware, it should be possible to simulate them entirely with AI."

### Human emulator architecture

The core concept: Emulate anything a human does digitally — keyboard/mouse inputs + screen viewing + decision-making. No software adoption required. Can deploy anywhere a human currently works.

Opposite approach from other labs:
| Other labs | xAI (Macrohard) |
|------------|-----------------|
| Bigger models | Smaller models |
| More reasoning | More speed |
| 10+ minute responses OK | Must be 1.5x-8x faster than human |
| Users wait for AI | AI waits for users |

*"No one's going to wait around 10 minutes for the computer to do something I could have done in 5, but if it can be done in 10 seconds, I'd pay whatever amount of money for that."*

The small-model decision enables faster iteration: model updates that would take 4 weeks now take 1 week. Multiple experiments run in parallel.

### Tesla car computer deployment

The capital efficiency insight: Tesla cars have compute that's idle 70-80% of the time.

| Factor | Details |
|--------|---------|
| Tesla fleet | 4M+ in North America |
| HW4 penetration | ~50-70% |
| Idle time | 70-80% (charging, parked) |
| Built-in | Power, cooling, networking |
| Model | Lease time from owners, pay their car lease |

Implication: Deploy 1M+ human emulators with purely software implementation — no data center buildout required. Tesla computer is more capital-efficient than AWS/Oracle VMs or buying NVIDIA hardware directly.

### Internal deployment

Virtual employees being tested internally:
- Appear in org chart
- Can be asked for help like real employees
- When someone says "come to my desk" → no one there
- Engineers initially didn't know they were interacting with AI

Generalization better than expected: Tasks not in training data performed flawlessly.

### Macrohard leadership churn (Feb-Mar 2026)

Macrohard has burned through two leaders in under a month. [[Toby Pohlen]] (ex-[[DeepMind]]) was appointed to run the project, left 16 days later. Musk then redeployed [[Ashok Elluswamy]], head of AI software at [[Tesla]], to reboot the effort and audit previous work.

### "Digital Optimus" announcement (March 11, 2026)

Musk publicly announced the joint [[Tesla]]-xAI project, branding it "Digital Optimus." Architecture: Grok serves as "master conductor/navigator" (Kahneman System 2) while Tesla-built AI handles real-time screen/input processing from the past 5 seconds (System 1). Runs on Tesla AI4 chip ($650) + xAI's Nvidia-based cloud. Musk: "the only real-time smart AI system" — claims it could "emulate the function of entire companies."

Contradicts Musk's Sep 2024 statement that Tesla had "no need to license anything from xAI" — relevant to ongoing shareholder litigation. The $2B Tesla investment in xAI is now producing a joint product.

*Sources: CNBC, Electrek (Mar 11, 2026)*

### War room status

Macrohard team operating in war room mode for 4+ months (as of Jan 2026). Originally in dedicated war room, now in converted gym space. Continuous push.

Value per commit: $2.5M estimated (tied to revenue targets and timeline). Team doing 5+ commits/day.

Business model:
- Licensable AI frameworks
- Like Microsoft Windows licensing
- Competing with Azure, AWS, GCP
- Lower barrier for AI-driven companies

---

## Culture & Operations

Three layers of management:
1. ICs (individual contributors)
2. Co-founders / managers
3. [[Elon Musk]]

That's it. No middle management. Everyone an engineer — including sales team.

Engineer-first culture:
- ~100 engineers when Grok 3 shipped
- iOS team: 3 people (for millions of users)
- Fuzzy team boundaries — anyone can fix anything, show to owner, get merged immediately
- If you need something fixed in VM infrastructure, you fix it yourself and show the owner
- No formal team assignments — HR software often wrong about who's on what team

Decision-making:
- No one says no to good ideas
- Response to proposals: either "no that's dumb" or "why isn't it done already?"
- Implement same day, show results, get answer that day
- No deliberation, no bureaucracy

Speed culture:
- "No due dates. It's always yesterday."
- Requirements challenged constantly — find the physical/fundamental limit, not artificial blockers
- Delete something, add back if needed — frequently happens same day
- Estimated timelines always wrong — look at assumptions, knock them out, get 2x improvement

Elon meetings:
- Feedback at very high level (product direction) OR very low level (compute efficiency, latency)
- Never middle
- "How can I help? How can I make this faster?"
- Makes phone call → software patch next day from vendors

AI agents for internal work:
- Core production APIs being rebuilt by one person + 20 agents
- (Context: [[Anthropic]] cut xAI's access to Claude models Jan 2026)

---

## Infrastructure

### Colossus (Memphis)
- Current: 100k H100s
- Branded as "Macrohard" on roof
- One of highest single-site AI compute capacities in US
- Build time: 122 days (0 → 100K GPUs)

Speed secrets:
- Land lease structured as "temporary" to fast-track permitting (similar to carnival/event permits)
- Same-day training runs on new GPU racks (vs weeks at other companies)
- 80+ mobile generators for power balancing
- Battery packs for load switching (generators too slow to react to millisecond GPU demands)
- When municipal load high → seamless switch to generators without interrupting training

The Cybertruck bet: Tyler (engineer) bet Elon he could get a training run on new GPUs in 24 hours. He did. He got the Cybertruck.

Regulatory controversy (2024-2026):
- 35 gas turbines installed without permits (classified as "non-road engines")
- NAACP + environmental groups appealed
- EPA closed the "non-road engine" loophole (Jan 2026)
- New data centers can't replicate this approach
- Daily fines up to $10K per violation under new permit

### Colossus 2 / MACROHARDRR (Tennessee)
- Third building purchased
- Named "MACROHARDRR"
- 2GW total capacity target
- Location chosen for TVA power access ([[BYOP]] strategy)
- See [[Power constraints]]

### Mississippi expansion
- Third building across state line from Memphis
- Investment: $20B+ per Gov. Tate Reeves
- Brings total capacity to ~2GW

Musk claim: "More AI compute than everyone else combined within five years"

---

## Pentagon drone swarm contest (Feb 16, 2026)

xAI and parent [[SpaceX]] competing together in a $100M Pentagon prize challenge to produce voice-controlled, autonomous drone swarming technology. 6-month contest organized by Defense Innovation Unit and Defense Autonomous Warfare Group (DAWG). xAI hiring engineers with active security clearances; already has $200M Pentagon contract for [[Grok]] integration into military systems. Marks a new frontier — combining xAI's generative AI with offensive weapons development.

See [[SpaceX]] for full details.

---

## Financials (2025)

Bloomberg reported (Jan 2026):

| Quarter | Revenue | Gross Profit | EBITDA | Net Loss |
|---------|---------|--------------|--------|----------|
| Q1 | $43M | $14M | -$612M | ~$1.0B |
| Q2 | $59M | $14M | -$861M | — |
| Q3 | $107M | $63M | -$922M | $1.46B |
| Jan-Sep | $208M | $90M | -$2.4B | — |

- Monthly burn rate: ~$1B/month
- Cash burn: $7.8B in first 9 months of 2025
- Full-year burn estimate: ~$11B (per Bloomberg Intelligence)
- Stock-based comp: ~$160M through September
- Revenue target: $500M for 2025 → tracking ~$280M annualized (will miss)
- EBITDA projection: -$2.2B for full year → already -$2.4B through Sep (exceeded losses)
- Revenue nearly doubled Q2→Q3; gross margin improving

DC buildout needs: Told investors at least $18B required — now outdated estimate

---

## X (Twitter) debt burden

xAI merged with X in 2025 — inheriting significant debt:

| Metric | Value | Notes |
|--------|-------|-------|
| Total debt | ~$13B | From Musk's 2022 acquisition |
| Interest expense (9M 2025) | ~$1B | Almost half of X revenue |
| 9M 2025 revenue | ~$2B | Interest = 50% of revenue |

Regulatory issues: Grok chatbot "repeatedly used to digitally undress people online and post the images to X" — under intense scrutiny from regulators

---

## $20B off-balance-sheet SPV (Oct 2025)

Structure: xAI financing Nvidia GPUs through an SPV — debt stays off xAI's balance sheet.

| Component | Party | Role |
|-----------|-------|------|
| Lead equity | [[Valor Equity Partners]] (Antonio Gracias) | SPV sponsor |
| Debt | [[Apollo]] | Investment-grade lender |
| Chips | [[NVIDIA]] | Equity investor + chip supplier |
| Lessee | xAI | 5-year lease commitment only |

How it works:
1. SPV is a legal entity separate from xAI
2. SPV buys Nvidia chips with Apollo debt + Valor/Nvidia equity
3. SPV rents chips exclusively to xAI
4. xAI's only commitment: 5-year lease — nothing else on balance sheet

Why this matters:
- xAI has limits on how much secured debt it can borrow
- SPV structure allows billions in GPU financing without balance sheet impact
- Model being copied by other AI companies

See [[AI infrastructure financing]].

---

## Funding history

| Round | Date | Amount | Valuation | Notes |
|-------|------|--------|-----------|-------|
| Series A | Dec 2023 | $135M | — | SEC filing, part of $1B target |
| Series B | May 2024 | $6B | $24B | Valor, Sequoia, [[a16z]] led |
| Series C | Dec 2024 | $6B | $50B | [[Fidelity]], [[BlackRock]], Sequoia |
| Series D | Sep 2025 | $10B | $200B | — |
| Debt | Oct 2025 | $12.5B | — | [[Morgan Stanley]] arranged |
| Series E | Jan 2026 | $20B | $230B | Exceeded $15B target. Includes $3B from [[HUMAIN]] (Saudi [[PIF]]) |

Total raised: ~$42B+ equity + debt

Valuation trajectory: $24B → $50B → $200B → $230B → ~$250B (SpaceX merger implied)

Note: X Corp investors received 25% of xAI (announced Nov 2023).

---

## Key investors

| Investor | Type | Rounds |
|----------|------|--------|
| Elon Musk | Founder | All |
| [[Valor Equity Partners]] | Lead | Series B, E |
| [[Sequoia Capital]] | VC | Series B, C |
| [[a16z]] | VC | Series B |
| [[Fidelity]] | Asset manager | Series C, E |
| [[NVIDIA]] | Strategic | Series C, E |
| [[Cisco]] | Strategic | Series E |
| [[BlackRock]] | Asset manager | Series C |
| Qatar Investment Authority | Sovereign | Series E |
| [[MGX]] (Abu Dhabi) | Sovereign | Series C, E |
| [[Kingdom Holding]] | Saudi (Prince Alwaleed) | Series B, C |
| [[HUMAIN]] | Saudi ([[PIF]]) | Series E ($3B) — shares converted to SpaceX |
| [[Baron Capital]] | Asset manager | Series E |
| [[StepStone Group]] | PE | Series E |
| [[AMD]] | Strategic | Series C |

35 total investors. Heavy sovereign wealth (Qatar, UAE, Saudi) + strategic chip suppliers (NVIDIA, [[AMD]], [[Cisco]]).

---

## Leadership

| Role | Name | Background |
|------|------|------------|
| CEO/Founder | [[Elon Musk]] | — |
| CFO | Anthony Armstrong | Ex-[[Morgan Stanley]] (joined Fall 2025) |
| CRO | Jon Shulkin | [[Valor Equity Partners]] |
| Co-founder | Greg Yang | Departed Jan 2026 (Lyme disease) — recruiting lead, reached out to hires personally |
| Co-founder | Igor Babuschkin | Ex-[[DeepMind]], Starcraft AI (AlphaStar) |

*Prior CFO Mike Liberatore resigned Oct 2025 after 3 months.*

### Co-founder attrition (2025-2026)

Of 11 original co-founders (Mar 2023), only [[Manuel Kroiss]] ("Makro") and [[Ross Nordeen]] remain as of Mar 2026.

| Co-founder | Departed | Context |
|-----------|----------|---------|
| [[Igor Babuschkin]] | Aug 2025 | Built Colossus, led Grok dev |
| [[Greg Yang]] | Jan 21, 2026 | Cited Lyme disease. Key recruiting force |
| [[Tony Wu]] | ~Feb 2026 | Removed in Musk's leadership overhaul |
| [[Jimmy Ba]] | ~Feb 2026 | Removed in Musk's leadership overhaul |
| [[Zihang Dai]] | ~Mar 12, 2026 | Most senior technical staff. Had publicly acknowledged xAI was behind on coding |
| [[Guodong Zhang]] | Mar 13, 2026 | Ran Grok pre-training. Blamed for coding product issues, relieved of primary duties by Musk |

Other departures:

Sulaiman Ghori — Macrohard engineer (Mar 2025 - Jan 2026). Left Jan 20, 2026 — days after appearing on *Relentless* podcast where he described xAI culture, Macrohard project, and regulatory shortcuts. Neither xAI nor Ghori commented on circumstances.

[[Toby Pohlen]] — Former [[DeepMind]] researcher. Put in charge of Macrohard project by Musk (~late Feb 2026). Left 16 days later.

---

## SpaceX acquisition (Feb 2, 2026)

xAI is now a SpaceX subsidiary:

| Metric | Value |
|--------|-------|
| Combined valuation | $1.25T |
| xAI implied value | ~$250B (up from $230B) |
| Share price | $526.59/share |
| IPO timing | Mid-2026 |

Why merger happened:
- xAI burning ~$1B/month with minimal revenue
- $230B valuation = premium to [[Anthropic]] despite lower revenue
- Difficult to raise more independently
- SpaceX's ~$8B 2025 profit can fund AI infrastructure buildout

Tesla excluded: Tesla's $2B xAI investment converted to SpaceX subsidiary position — raising fiduciary concerns.

Strategic vision: Orbital data centers. SpaceX filed for 1 million satellite authorization (Jan 30, 2026). xAI = anchor customer for space-based AI compute.

Musk quote: "Within 2 to 3 years, the lowest cost to generate AI compute will be in space."

### Lunar factory & MassDriver (Feb 10, 2026)

At an xAI all-hands meeting, Musk told employees the company should build a factory on the Moon to manufacture AI satellites, and use a massive electromagnetic catapult (mass driver) dubbed "MassDriver" to launch them into orbit.

| Element | Detail |
|---------|--------|
| Concept | Lunar factory producing AI satellites |
| Launch system | Electromagnetic mass driver (space catapult) |
| Rationale | "You have to go to the Moon" — scaling AI compute beyond Earth's constraints |
| Moon city | Self-sustaining city on Moon in <10 years |
| Mars | Pushed to 20+ years (was previously 5-7 year timeline) |

Context: This represents Musk's Mars-to-Moon pivot. He spent years denigrating lunar missions as a "distraction" from Mars — now the Moon is "faster" for securing civilization. SpaceX filed for 1M satellite authorization (Jan 30, 2026). The "sentient sun" concept = vast constellation of AI satellites forming an orbital intelligence network.

See [[Lunar Mass Driver]] for full concept analysis. See [[SpaceX xAI merger]] for merger details.

*Source: NYT, Feb 10 2026*

---

## Coding product ("Grok Code Fast")

xAI's coding product has failed to gain traction against [[Anthropic]]'s [[Claude Code]] and [[OpenAI]]'s Codex. Musk identified training data quality as the key issue (FT, Mar 14 2026). [[Zihang Dai]], the most senior technical staff member, had publicly acknowledged xAI was behind on coding before departing. [[Guodong Zhang]], who ran Grok pre-training, was blamed for the data quality problems and relieved of duties.

Cursor poach (Mar 2026): xAI hired [[Andrew Milich]] and [[Jason Ginsberg]] from [[Cursor]] to improve Grok Code Fast. Musk welcomed them on X, adding: "Orbital space centres and mass drivers on the Moon will be incredible."

### SpaceX-Cursor option (Apr 21, 2026)

The reported [[SpaceX]]-[[Cursor]] agreement is effectively a second answer to xAI's coding weakness. If Grok Code Fast cannot win developers organically fast enough, SpaceX can pair Cursor's existing distribution with [[Colossus]] compute and potentially buy the whole surface later in 2026 for $60B. The alternative payment, $10B for the joint work, is large enough that this reads less like ordinary vendor spend and more like a staged acquisition structure.

For xAI, the strategic point is obvious: own the interface where expert developers already spend time, reduce long-term dependence on model access from [[Anthropic]] and [[OpenAI]], and present public investors with a fuller vertical stack ahead of [[SpaceX IPO 2026]].

See [[SpaceX Cursor partnership and acquisition option April 2026]].

---

## SpaceX/Tesla audit (Mar 2026)

After the [[SpaceX xAI merger|SpaceX merger]], Musk parachuted managers from [[SpaceX]] and [[Tesla]] into xAI to audit employees. The "fixers" reviewed work output and fired staff deemed inadequate (FT, Mar 14 2026).

Employees were sent a memo (Mar 12) denying mass layoffs. However, researchers continued quitting — burnout from "extremely hardcore" work demands and better offers from rivals. Recruiters began contacting previously rejected candidates to fill gaps, often on better financial terms.

Musk (Mar 14): "Many talented people over the past few years were declined an offer or even an interview at xAI. My apologies." Said he would go through company interview history and re-contact promising candidates.

Musk (Mar 13 on X): "xAI was not built right first time around, so is being rebuilt from the foundations up. Same thing happened with Tesla."

*Source: FT, Mar 14, 2026*

---

## Samsung connection

Musk controls both [[Tesla]] and xAI. Combined, they could be a major anchor customer for [[Samsung]] Taylor fab.

This is one of the "customer win" scenarios that validates the Korea thesis.

---

## Sovereign AI stack framing (Apr 9, 2026)

[[Deepwater Asset Management]] ([[Gene Munster]] + [[Doug Clinton]]) named xAI as the model and data layer of SpaceX's broader sovereign AI stack — the corporate-level framework where a single company owns energy, chips, models, data, distribution, and physical AI without renting any layer from a third party. In Deepwater's read, xAI is the piece that turned SpaceX from a launch-plus-satellite business into a full-stack AI company the moment the February 2026 acquisition closed. [[Grok]] becomes the model, [[X]] becomes the real-time data layer (with an increasing amount of scientific content flowing through it), and [[Colossus]] plus future orbital compute becomes the execution venue.

Deepwater specifically contrasted xAI's chip dependency with the rest of the stack — xAI today is heavily reliant on [[Nvidia]] just like everyone else, which is the hole that [[TERAFAB]] is meant to close. Until Terafab produces, xAI sits on the same [[TSMC]]-via-Nvidia supply chain as [[OpenAI]], [[Meta]], [[Anthropic]], and the rest of the tier-one model labs. The sovereignty claim is forward-looking — valid only after Terafab starts fabbing — but the fact that the capability is being built internally is what distinguishes the sovereign AI thesis from a standard hyperscaler bull case.

On Grok's positioning, Clinton's "truth-seeking model" framing is worth writing down directly because it is an explicit product strategy rather than a retrofit: *all AI models at some level will be injected with some of the biases of the creator. The question is whether Grok will have the least bias of all the models, and whether the least-biased model is more valuable — and the logical answer is yes when you're getting into certain things that might touch on science, physics, math, where social constructs are irrelevant in the context of nature.* The bet is that Grok is positioned as the scientific / physics / math truth-seeking model specifically because human social and political biases do not govern those domains. See [[Grok]] for the full product-level framing.

See [[Sovereign AI stack]] for the corporate framework and [[SpaceX IPO 2026]] for the valuation-layer implication.

---

## Terafab foundry resolution (Apr 7, 2026)

[[Intel]] joined [[TERAFAB]] as foundry partner (18A node), resolving the open question of who fabricates the D3 orbital and datacenter chips. Intel's packaging ([[EMIB]], [[Foveros]]) also addresses the advanced packaging bottleneck. The Samsung anchor customer scenario (where Musk's combined demand backstops the Taylor fab) may still play out for memory or secondary nodes, but the leading-edge logic path now runs through Intel.

---

## Quick stats

| Metric | Value |
|--------|-------|
| Status | SpaceX subsidiary (acquired Feb 2026) |
| Founder | Elon Musk |
| Product | Grok (LLM), Macrohard |
| Implied valuation | ~$250B (in SpaceX merger) |
| Total raised | ~$40B (equity + debt) |
| 2025 revenue (Jan-Sep) | $208M |
| 2025 EBITDA (Jan-Sep) | -$2.4B |
| Monthly burn | ~$1B |
| Current GPUs | [[NVIDIA]] H100/Blackwell |
| [[Target]] capacity | 2GW + orbital |
| X debt load | ~$12B (inherited from X acquisition) |
| xAI new debt | ~$5B (Morgan Stanley, incl. $3B HY bonds at 12.5%) |
| Combined debt | $17.5B |

*Updated 2026-03-14*

---

## $17.5B debt repayment plan (Mar 2, 2026)

Bloomberg (via Morgan Stanley notifications to lenders): X and xAI plan to repay $17.5B in debt in full.

| Component | Amount | Detail |
|-----------|--------|--------|
| Legacy X debt | ~$12B | Inherited when xAI acquired X (early 2025) |
| xAI new debt | ~$5B | Morgan Stanley-led package |
| — of which HY bonds | $3B | 12.5% coupon, sold at par, now trading at ~$1.17/dollar |

How: Source "yet to be determined" but xAI raised $20B Series E (Jan 2026), providing ample liquidity. HY bonds will be redeemed early at ~17 cent premium.

Why now: Pre-IPO balance sheet cleanup. [[SpaceX]] IPO targeting mid-2026 — clean debt profile improves the $1.75T valuation narrative.

Revenue sources (consolidated xAI + X):

| Stream | Scale |
|--------|-------|
| X advertising + premium | >$3.3B ARR (end-2025) |
| X Premium alone | $1B ARR (Feb 2026) |
| [[Grok]] subscriptions | ~$300M FY2025 (SuperGrok ~$30/mo, Heavy ~$300/mo) |
| xAI standalone (ex-X ads) | ~$500M ARR exiting 2025, guided $2B+ in 2026 |
| Government contracts | $300M DoD contracts + GSA ($0.42/user for 18 months) |

---

## Ratepayer Protection Pledge (Mar 4, 2026)

[[Gwynne Shotwell]] represented xAI at the White House [[Ratepayer Protection Pledge]] signing. Key commitments:

| Commitment | Detail |
|-----------|--------|
| Power per DC | 1.2 GW as primary power source — same commitment for every additional data center |
| Megapack expansion | Expanding what is already the largest global megapack installation |
| Grid backup | Sufficient backup power for the city of Memphis + town of South Haven, MS |
| Grid infrastructure | Building new substations and electrical infrastructure |
| Water recycling | ~4.7 billion gallons/year protected in Memphis aquifer |
| Employment | Thousands of workers from Memphis area (TN + MS) |
| Orbital data centers | Designing space-based DCs powered by solar — would free terrestrial plants for community use |

Shotwell: "I've been in the space industry for nearly 40 years... I have never seen things move more quickly than under your administration."

---

## Colorado AI Act lawsuit (Apr 2026)

In April 2026, xAI sued the state of [[Colorado]] over the [[Colorado AI Act]] (effective Jun 30 2026) — a state law targeting algorithmic discrimination in AI systems used to allocate education, housing, healthcare, credit, and employment, plus certain government services.

xAI's legal arguments, per the complaint:

- **First Amendment / forced speech:** xAI claims the law infringes the company's free-speech rights because it would force Grok to incorporate "the controversial viewpoints of legislators."
- **Operational impact:** xAI argues the law would force it to change Grok's behavior to comply, in particular around how the model handles allocation decisions in the listed sectors.

The complaint is also notably focused on the law's carve-out — Colorado's definition of "algorithmic discrimination" excludes biases designed to "increase diversity or redress historical discrimination." xAI's brief treats this exclusion as evidence that the statute is not viewpoint-neutral and is instead embedding a particular set of values into permitted AI behavior.

Politically the suit puts xAI alongside the Trump administration's federal-preemption push (see [[AI regulation]]) — which favors a single national framework over the patchwork of state AI laws now in flight. Colorado has so far defied that push.

[[FT]] columnist Martin Sandbu (Apr 26 2026) read the suit as a stress test of whether AI-driven decisions in regulated sectors must satisfy the standard public-justification requirement that applies to all other allocation decisions, and whether [[LLMs]] like [[Grok]] can themselves provide reasons sufficient to clear that bar. Sandbu's framing: "my AI said so" has so far not been treated as sufficient justification under the rule of law, even when allocations are made by automated systems.

For the regulatory landscape and the Colorado statute itself see [[AI regulation]]. For Grok product behavior see [[Grok]].

*Source: FT, Apr 26 2026.*

---

## For theses

[[AI capex arms race]]: Poster child of brutal AI economics (~$1B/mo burn)
[[Short Tesla]]: xAI capital drain on Tesla cash
[[Short TSMC long Korea]]: Musk as Samsung anchor = bullish Korea
[[AI hyperscalers]]: Emerging tier 2 hyperscaler
[[Long TSMC]]: Current GPUs = TSMC (via NVIDIA)

---

## Related

### Events
- [[SpaceX xAI merger]] — Feb 2026 acquisition, now SpaceX subsidiary

### Products
- [[Grok]] — AI model (Colossus 200K GPUs)

### People/Partners
- [[Elon Musk]] — founder and controller
- [[SpaceX]] — parent company (acquired xAI Feb 2026)
- [[Greg Yang]] — co-founder (departed Jan 2026), Tensor Programs, recruiting
- [[Igor Babuschkin]] — co-founder (departed Aug 2025), built Colossus, led Grok dev
- [[Tesla]] — Musk connection (Samsung anchor potential), car computer deployment
- [[Tesla Optimus]] — xAI to power humanoid robots (Macrohard = digital Optimus)
- [[Computer use]] — paradigm (Macrohard = speed-first computer use)
- [[Edge inference]] — deployment strategy (Tesla fleet compute)
- [[Samsung]] — potential foundry (Korea thesis)
- [[NVIDIA]] — supplier + investor (H100/Blackwell GPUs)
- [[TSMC]] — upstream (via NVIDIA)
- [[Apollo]] — SPV partner for chip purchases
- [[Valor Equity Partners]] — lead investor, CRO origin, SPV partner
- [[AI hyperscalers]] — category (tier 2)
- [[Ashok Elluswamy]] — Tesla AI software head, redeployed to reboot Macrohard (Mar 2026)
- [[Zihang Dai]] — co-founder, departed Mar 2026 (senior technical staff)
- [[Guodong Zhang]] — co-founder, departed Mar 2026 (Grok pre-training lead)
- [[Toby Pohlen]] — ex-DeepMind, ran Macrohard briefly (~16 days)
- [[Manuel Kroiss]] — co-founder, one of two remaining (as of Mar 2026)
- [[Ross Nordeen]] — co-founder, one of two remaining (as of Mar 2026)
- [[Cursor]] — AI coding competitor (xAI poached Andrew Milich, Jason Ginsberg)
- [[Microsoft]] — competitor (Macrohard jab)
- [[TVA]] — power source (Colossus location)
- [[Power constraints]] — context (2GW target)
- [[AI infrastructure financing]] — $20B SPV structure
- [[Sovereign AI stack]] — Deepwater framework: xAI is the model/data layer of SpaceX's full stack
- [[Deepwater Asset Management]] — source of the sovereign AI framing (Gene Munster + Doug Clinton, Apr 9, 2026)

---

## Sources

- [xAI Series E announcement](https://x.ai/news/series-e)
- [CNBC on $20B raise](https://www.cnbc.com/2026/01/06/elon-musk-xai-raises-20-billion-from-nvidia-cisco-investors.html)
- [TechFundingNews on $230B valuation](https://techfundingnews.com/xai-nears-a-230b-valuation-with-20b-funding-from-nvidia-and-others-to-challenge-openai-and-anthropic/)
- [Bloomberg on xAI financials](https://www.bloomberg.com/news/articles/2026-01-11/musk-s-xai-burned-through-cash-with-1-5-billion-quarterly-loss) (Jan 2026)
- [Bloomberg - Off-Balance-Sheet AI Debt](https://www.bloomberg.com/news/articles/2025-10-31/meta-xai-starting-trend-for-billions-in-off-balance-sheet-debt) (Oct 2025)
- [Relentless podcast: Sulaiman Ghori interview](https://open.spotify.com/episode/7em5vO1grAq1FXz9029Fvr) (Jan 15, 2026) — culture, Macrohard, infrastructure
- [CNBC - xAI turbine permit controversy](https://www.cnbc.com/2025/07/16/musks-xai-permits-challenged-by-naacp-environmental-groups-memphis.html) (Jul 2025)
- [CNBC - EPA closes turbine loophole](https://www.cnbc.com/2026/01/16/musks-xai-faces-tougher-road-expanding-memphis-area-after-epa-update.html) (Jan 2026)
- [Bloomberg - Musk's Relentless AI Pursuit](https://www.bloomberg.com/news/articles/2026-01-30/musk-s-ai-pursuit-has-him-on-the-hunt-for-capital) (Jan 30, 2026) — merger speculation, xAI burn rates, Tesla FCF forecast
- [FT - Musk orders new round of xAI job cuts](https://www.ft.com/content/e5fbc6c2-d5a6-4b97-a105-6a96ea849de5) (Mar 14, 2026) — coding product failure, SpaceX/Tesla auditors, co-founder exodus (9 of 11 departed)
