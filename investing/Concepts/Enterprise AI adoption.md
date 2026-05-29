#concept #ai #enterprise #skeptical

# Enterprise AI adoption

The gap between AI hype and enterprise reality.

---

## The headline numbers (2025)

- $37B enterprise AI spending (up from $1.7B in 2023)
- 88% of organizations using AI in at least one function
- 6% of global [[SaaS]] market

Sounds bullish. But...

---

## The reality check

- 95% of AI pilots delivered no measurable P&L impact (MIT "GenAI Divide" study, Aug 2025)
- 31% of use cases reached full production (double from 2024, but still low)
- VCs predicted 2025 would be "the year" — now saying 2026

Important caveat: The 95% failure rate applies to broad enterprise pilots. Two clear exceptions:
1. Coding tools — 55% of departmental spend, clear ROI
2. Agents — 35% adoption, 66% seeing measurable value (see [[Agentic AI]])

Pattern: AI works where output is measurable and tasks are defined. Struggles where ROI is fuzzy (generic "transformation").

---

## Where the money actually goes

| Category | Share of departmental AI spend | ROI evidence |
|----------|-------------------------------|--------------|
| Coding | 55% ($4B) | Strong — GitHub Copilot, [[Claude]] Code, [[Cursor]] |
| IT | 10% | Moderate |
| Marketing | 9% | Weak |
| Customer success | 9% | Mixed |
| Design | 7% | Moderate |
| HR | 5% | Weak |

Coding is the killer app — measurable output, clear productivity gains. Tools like [[Claude]] Code, GitHub Copilot, [[Cursor]] have proven ROI. Everything else is more experimental.

Why coding works:
- Output is measurable (lines of code, tasks completed)
- Feedback loop is immediate (does it compile/run?)
- Developers are early adopters
- Integrates into existing workflows (IDE plugins)

---

## Legacy-code modernization as durable TAM floor

AI-native coding (greenfield projects, modern stacks) is roughly 5% of the broader coding market. The remaining 95% is legacy code — accumulated over 50 years of enterprise IT — where frontier models are substantially less productive per token because the languages, conventions, and institutional knowledge fall outside the modern training distribution.

The canonical example is COBOL (an IBM business language from 1959 still running the backend of many banks, insurers, payment processors, and government systems). [[Chamath Palihapitiya]] cited on [[All-In Podcast]] (Apr 10 2026) a $100B-revenue enterprise customer that calls 60-year-old pensioners back in to read legacy COBOL because no younger engineers can. Similar patterns exist across RPG (IBM i / AS/400), MUMPS (healthcare, Epic), Fortran (scientific computing, actuarial), and PL/I (banking).

Two opposing reads on what this means for enterprise AI TAM:

| Read | Implication |
|------|-------------|
| Durable TAM floor | Legacy-code modernization is a multi-decade services business. Tools that can read, explain, and safely rewrite legacy codebases unlock trillions of dollars of productivity. Coding spend expands dramatically as tools cross the capability threshold. |
| Bounded ceiling | Frontier models underperform on legacy languages; specialized fine-tuned models underperform on the long tail. The work stays expensive and human-led because the risk of a subtle rewrite bug in a payment ledger or claim-adjudication system is catastrophic. Coding spend grows less than hype suggests. |

The binding question is whether any current tool (Claude Code, Cursor, GitHub Copilot, [[Cognition]] Devin, [[OpenClaw]], [[Ridges AI]]) will demonstrate safe production-quality legacy migration at scale. As of April 2026 the published benchmark surface is dominated by [[SWE-Bench]] (modern Python) and similar frontier-native benchmarks. Legacy-code benchmarks are thin; performance there is the main gap between the "coding is 5% penetrated" read and the "coding is already saturated" read.

This TAM framing is the analytical counter to "Anthropic is compute-constrained against near-infinite demand" framings (see [[Anthropic]]): compute is the binding constraint on the served segment, but penetration of the unserved segment is the binding constraint on total market. Both can be true.

---

## Why adoption lags

1. Integration complexity — AI doesn't plug into existing workflows
2. Data readiness — Enterprises don't have clean, accessible data
3. ROI measurement — Hard to quantify "productivity gains"
4. Security/compliance — Regulated industries move slow
5. Vendor sprawl — Too many tools, no clear winner

---

## May 2026: individual speed vs firm-level ROI

[[Exponential View]]'s May 27 2026 framework is useful because it separates AI tool adoption from operating-model redesign. The essay starts from the puzzle most visible in engineering orgs: individual developers using [[Claude Code]] can ship more code and more pull requests, yet the company does not automatically ship proportionally more useful product.

The historical analogy is factory electrification. Stage 1 is the lightbulb: safer, faster local work with the same operating logic. For AI, this is the individual productivity layer: email, research, coding assistance, presentations, and other single-worker tasks. Stage 2 is the group drive: a motor attached to the existing shafting. For AI, this is the agent attached to legacy workflow geometry -- support tickets, recruiting screens, marketing variants, sales proposals, internal analysis packets. It can cut cost and cycle time inside the workflow, but the firm is still governed by the old decision layers.

Stage 3 is the unit drive: redesign the flow around throughput rather than grafting the new power source onto the old layout. For AI, that means the system can observe a signal, orient against the roadmap / codebase / policy context, decide within governed bounds, build or route the work, and shorten the full decision loop. The bottleneck moves from "can one worker produce more output?" to "can the organization absorb, decide, ship, and learn faster?"

This is why [[Uber]]'s AI-token-spend concern matters. Uber is one of the most algorithmic companies in public markets, but COO Andrew Macdonald still questioned whether rising [[Claude Code]] / AI-token usage mapped cleanly to more useful consumer features. It is also why [[Klarna]]'s customer-service assistant is best read as Stage 2 rather than proof of enterprise-wide transformation: the bot absorbed tickets and reduced human load, but it stayed inside the support workflow.

The [[Oliver Wyman]] Forum survey provides the macro cross-check: only 27% of CEOs said AI ROI had met or exceeded expectations, while 53% said it was too early to assess ROI. That is not evidence that AI has no utility; it is evidence that installation has moved faster than organizational redesign.

*Sources: [Exponential View, "Why AI isn't showing up on your bottom line", May 27 2026](https://www.exponentialview.co/p/why-ai-isnt-showing-up-on-your-bottom-line); [Oliver Wyman Forum CEO Agenda 2026](https://www.oliverwymanforum.com/ceo-agenda/how-ceos-navigate-geopolitics-trade-technology-people.html); [Business Insider / Rapid Response via Exponential View](https://www.exponentialview.co/p/why-ai-isnt-showing-up-on-your-bottom-line); [Klarna press release via PRNewswire, Feb 27 2024](https://www.prnewswire.co.uk/news-releases/klarna-ai-assistant-handles-two-thirds-of-customer-service-chats-in-its-first-month-302072744.html).*

---

## May 2026: verification labor as adoption cost

[[Noah Smith]]'s May 27 2026 [[Noahpinion]] public preview adds a labor-market version of the same adoption bottleneck. If AI agents become powerful enough to do much of the technical work, firms still need humans to specify goals, verify output, and keep systems aligned with what the organization actually wants. Human work shifts from direct production toward supervision and correction.

That is not a bearish claim about AI capability. It is a constraint on realized enterprise ROI. The value of an agentic workflow depends on the verification ratio: how much human time is required per unit of model output before the work can be trusted. In software coding, the ratio can be favorable because tests, compilers, code review, and production telemetry create feedback loops. In legal, finance, medicine, regulated customer communication, and strategic analysis, the verification layer can remain expensive because the cost of a subtle error is high.

This slots between the Exponential View operating-model ladder and the Okta shadow-AI finding. Individual usage can explode, and agents can do real work, but firm-level adoption still requires a governance process that decides what work can be delegated, how outputs are checked, who owns liability, and when humans override the system.

*Source: [[Noah Smith]], [[Noahpinion]], [May 27 2026](https://www.noahpinion.blog/p/your-future-job-will-be-to-keep-ai). Public preview only; no paid-body claims inferred.*

---

## May 2026: shadow AI adoption outpaces governance

[[Okta]]'s May 2026 survey adds the security/governance version of the same adoption-vs-ROI gap. Workers are already using AI tools heavily, but a large share of that adoption sits outside formal enterprise control. Okta found that 52% of employees use unapproved AI tools, while 90% of executives say they are confident in visibility into AI tools and 95% believe employees use AI responsibly.

This is why high reported usage does not automatically equal mature enterprise adoption. [[Shadow AI]] can inflate the apparent penetration rate while leaving the organization without inventory, identity controls, data-loss policy, or measurement. The usage is real, but the operating model is immature. The same pattern appears in the Exponential View framework above: individual productivity can rise before the firm redesigns workflows, security, and decision throughput.

The investment read is that shadow AI creates budget for [[Okta]], [[Cybersecurity]], browser/DLP vendors, and services firms that can turn unmanaged usage into governed workflows. It also raises adoption friction: regulated enterprises cannot scale AI from personal accounts and policy exceptions into core workflows without solving identity, visibility, and auditability.

*Sources: Okta, ["AI Agents at Work 2026: Securing the agentic enterprise"](https://www.okta.com/newsroom/articles/ai-agents-at-work-2026-agentic-enterprise-security/), May 27 2026; The Register, ["Bosses blinded by confidence about shadow AI use by workers"](https://www.theregister.com/ai-ml/2026/05/27/bosses-blinded-by-confidence-about-shadow-ai-use-by-workers/), May 27 2026.*

---

## Peer-belief bottleneck

[[Joachim Klement]]'s May 28, 2026 read of Cullen, Faia, Guglielminetti, Perez-Truglia, and Rondinelli's [[Italy|Italian]] central-bank firm survey adds a social-learning channel to the adoption-lag problem. Managers of roughly 3,000 Italian firms were asked about their own AI/robotics adoption and their beliefs about peer adoption. Klement reports that 93% underestimated peer adoption by at least 2.5 percentage points, with the average manager underestimating adoption by roughly a quarter.

The crucial split is that correcting the belief gap did not move AI adoption plans in a statistically clear way, while it did move robotics. The NBER version of the paper estimates that a 1 percentage-point increase in expected competitor adoption raised intended future robotics adoption by 0.704 percentage points, with no comparable significant AI effect.

The read-through is not simply "peer pressure will accelerate AI." It is more precise: enterprise managers may be running on stale priors about how far peers have moved, but AI adoption still needs visible ROI and implementation confidence before peer information changes behavior. Robotics is more legible: a factory can see that competitors are automating a physical process, and the competitive-response channel is cleaner. For generic AI, the binding constraint still looks like workflow fit, data readiness, governance, and measurable value.

*Sources: [Joachim Klement, "If your peer does it, do you do it?", May 28 2026](https://klementoninvesting.substack.com/p/if-your-peer-does-it-do-you-do-it); [Cullen et al., "The Innovation Race", NBER WP 34532](https://www.nber.org/papers/w34532).*

---

## May 2026: the services-budget counter-signal

[[Capgemini]]'s May 27, 2026 Capital Markets Day is useful because it reframes enterprise AI adoption from "tool rollout" to operating-model redesign. The company told investors that clients are treating AI as a broader business transformation rather than a standard IT upgrade, which means budgets can come from business functions as well as the CIO. Reuters also reported management's claim that the AI-related opportunity pipeline already exceeded $12B.

This is not a contradiction of the adoption-lag problem above. It is the reason the lag exists. If AI value requires a full reset of data foundations, governance, workflows, security controls, human-agent supervision, and cloud architecture, then adoption is slow -- but the spend pool shifts toward [[IT services]] firms that can do the integration work.

The market's skepticism remains important. Capgemini shares fell 3.5% on May 27 even after the strategy update, which says investors want proof that agentic-AI consulting turns into revenue and margin rather than just pipeline language. The watch item is whether services firms begin reporting accelerating organic growth from AI transformation, or whether AI remains a pitch overlay on flat consulting demand.

*Sources: [Reuters via Investing.com, May 27 2026](https://www.investing.com/news/stock-market-news/capgemini-says-ai-widens-client-spending-pool-4712824); [Capgemini 2026 Capital Markets Day press release](https://investors.capgemini.com/en/publication/2026-capital-markets-day/); [Bourse Direct historical quote table, May 27 2026](https://www.boursedirect.fr/fr/marche/euronext-paris/capgemini-se-FR0000125338-CAP-EUR-XPAR/graphiques).*

---

## [[Trade]] implications

Be skeptical of:
- "AI revenue growth" without margin disclosure
- Enterprise AI startups outside coding (long sales cycles, high churn)
- "AI transformation" narratives from legacy vendors
- Vertical AI solutions (customer service bots, sales AI)

Bullish:
- Coding tools — GitHub Copilot, [[Claude]] Code, [[Cursor]] — proven ROI, clear winner
- Infrastructure (compute, not applications)
- Horizontal platforms with coding use cases

The coding exception matters:
- 55% of spend, clear ROI = this segment is real
- Companies enabling developer productivity are investable
- Don't conflate "enterprise AI failing" with "all AI failing"

---

## The 2026 prediction

VCs say 2026 is "the year" enterprises see real value.

They said the same about 2025. And 2024.

What to watch:
- CIO surveys on AI budget growth vs cuts
- Enterprise contract renewals (churn data)
- Actual productivity metrics (not surveys)

---

## Related

- [[Agentic AI]] — exception (35% adoption, 66% seeing value)
- [[AI adoption curve]] — diffusion curve and peer-belief channel
- [[Model lab economics]] — context (infrastructure vs application spend)
- [[AI hyperscalers]] — infrastructure (compute, not applications)
- [[IT services]] — services layer that benefits if AI adoption requires integration
- [[Capgemini]] — May 2026 example of the services-budget counter-signal
- [[Exponential View]] — May 2026 framework: lightbulb / group drive / unit drive
- [[Productivity J-curve]] — historical general-purpose-technology lag framework
- [[Shadow AI]] — unmanaged adoption as a governance/security version of the adoption gap
- [[Klarna]] — customer-service agent as Stage 2 workflow-cost example
- [[Uber]] — AI-token spend vs useful consumer-feature output example
- [[Robotics]] — peer-belief channel is cleaner for physical automation than for generic AI
- [[Anysphere]] — beneficiary ([[Cursor]], coding tools)
- [[Anthropic]] — beneficiary ([[Claude]] Code, coding tools)
- [[Noahpinion]] — verification-labor frame for the human role inside agentic adoption
