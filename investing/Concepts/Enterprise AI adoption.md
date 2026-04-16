#concept #ai #enterprise #skeptical

# Enterprise AI adoption

The gap between AI hype and enterprise reality.

---

## The headline numbers (2025)

- **$37B** enterprise AI spending (up from $1.7B in 2023)
- **88%** of organizations using AI in at least one function
- **6%** of global [[SaaS]] market

Sounds bullish. But...

---

## The reality check

- **95% of AI pilots delivered no measurable P&L impact** (MIT "GenAI Divide" study, Aug 2025)
- **31%** of use cases reached full production (double from 2024, but still low)
- VCs predicted 2025 would be "the year" — now saying 2026

**Important caveat**: The 95% failure rate applies to broad enterprise pilots. Two clear exceptions:
1. **Coding tools** — 55% of departmental spend, clear ROI
2. **Agents** — 35% adoption, 66% seeing measurable value (see [[Agentic AI]])

**Pattern**: AI works where output is measurable and tasks are defined. Struggles where ROI is fuzzy (generic "transformation").

---

## Where the money actually goes

| Category | Share of departmental AI spend | ROI evidence |
|----------|-------------------------------|--------------|
| **Coding** | 55% ($4B) | **Strong** — GitHub Copilot, [[Claude]] Code, [[Cursor]] |
| IT | 10% | Moderate |
| Marketing | 9% | Weak |
| Customer success | 9% | Mixed |
| Design | 7% | Moderate |
| HR | 5% | Weak |

**Coding is the killer app** — measurable output, clear productivity gains. Tools like [[Claude]] Code, GitHub Copilot, [[Cursor]] have proven ROI. Everything else is more experimental.

**Why coding works:**
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

1. **Integration complexity** — AI doesn't plug into existing workflows
2. **Data readiness** — Enterprises don't have clean, accessible data
3. **ROI measurement** — Hard to quantify "productivity gains"
4. **Security/compliance** — Regulated industries move slow
5. **Vendor sprawl** — Too many tools, no clear winner

---

## [[Trade]] implications

**Be skeptical of:**
- "AI revenue growth" without margin disclosure
- Enterprise AI startups outside coding (long sales cycles, high churn)
- "AI transformation" narratives from legacy vendors
- Vertical AI solutions (customer service bots, sales AI)

**Bullish:**
- **Coding tools** — GitHub Copilot, [[Claude]] Code, [[Cursor]] — proven ROI, clear winner
- Infrastructure (compute, not applications)
- Horizontal platforms with coding use cases

**The coding exception matters:**
- 55% of spend, clear ROI = this segment is real
- Companies enabling developer productivity are investable
- Don't conflate "enterprise AI failing" with "all AI failing"

---

## The 2026 prediction

VCs say 2026 is "the year" enterprises see real value.

They said the same about 2025. And 2024.

**What to watch:**
- CIO surveys on AI budget growth vs cuts
- Enterprise contract renewals (churn data)
- Actual productivity metrics (not surveys)

---

## Related

- [[Agentic AI]] — exception (35% adoption, 66% seeing value)
- [[Model lab economics]] — context (infrastructure vs application spend)
- [[AI hyperscalers]] — infrastructure (compute, not applications)
- [[Anysphere]] — beneficiary ([[Cursor]], coding tools)
- [[Anthropic]] — beneficiary ([[Claude]] Code, coding tools)
