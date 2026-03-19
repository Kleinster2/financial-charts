---
aliases: [AI in economics, AI economics research, LLM economics]
tags: [concept, ai, research, productivity]
---

# AI in economic research

How AI tools are changing the production, scope, and quality control of economic research — and whether the profession's error-correction mechanisms survive the transition.

---

## Synthesis

The data through early 2026 tells a split story. AI has clearly expanded what economists can study — qualitative data that was prohibitively expensive to analyse is now tractable, and forecasting models are getting more flexible. But the profession's output hasn't visibly improved: no surge in top-journal submissions, no measurable readability gains in [[NBER]] abstracts, and submission quality flat per editors. The real tension is in quality control. [[Refine]] (Ben Golub) finds errors in 1/3+ of papers that already passed peer review at top journals — meaning the baseline was porous. If AI simultaneously makes it easier to generate volume *and* humans delegate more of the checking, the net effect on research quality is ambiguous. The economics profession is now a live experiment in whether AI-augmented error detection can outrun AI-augmented slop production.

---

## Adoption metrics

![[nber-ai-working-papers-ft.png]]
*Share of [[NBER]] working papers mentioning AI-related terms in title or abstract. Monthly share hit ~15% by early 2026, up from ~2% pre-ChatGPT. 12-month rolling average ~10%. Source: NBER / FT (Mar 19, 2026).*

- ~25% of [[American Economic Review]] submissions now disclose AI use, mostly for editing and programming help — per AER editor Erzo Luttmer
- Overall submission quality "hadn't obviously changed"

![[econ-journal-submissions-ft.png]]
*Monthly submissions to top economics journals. No obvious ChatGPT-driven inflection in volume. [[QJE]] trending ~200/month, [[American Economic Review|AER]] ~150, [[JPE]] ~100. All gradual uptrends predating Nov 2022. Source: journals / FT (Mar 19, 2026).*

---

## Three channels

### 1. Productivity

AI automates data cleaning, grant writing, table formatting, code generation. Adopters report transformative gains:

- Paul Novosad ([[Dartmouth College]]): "roughly quintupled the time he could spend actually thinking about research questions"
- Elliott Ash ([[ETH Zürich]]): productivity gains "so exciting, it made him want to work more"

But no visible impact on aggregate output quality or volume at top journals yet — consistent with the [[Productivity J-curve]] framework (investment precedes measurable harvest).

### 2. Scope expansion

AI unlocks qualitative data that was previously too expensive to collect or analyse systematically:

- Zoning regulation effects — text analysis at scale
- Impact of difficult job interviews — qualitative coding automated
- Corporate earnings calls trawled for tariff response signals
- Flexible "general-purpose" forecasting models: [[Bank for International Settlements]] unveiled one on Mar 16, 2026 — would have predicted the persistence of inflation in 2021-22

### 3. Error detection

The most consequential and most fragile channel.

- [[Refine]] (co-created by Ben Golub): AI-powered reviewing tool that scours economics papers for errors
- Already being tested by several of the top five economics journals
- Finding problems in at least 1/3 of papers that had already passed peer review at top journals
- Implication: peer review was already porous before AI — Refine is surfacing pre-existing failures

Risk: moral hazard. If human reviewers were already underinvesting in error-checking (low-reward task), AI availability may further reduce effort. Reports of "shamefully sloppy AI-generated referee reports" already circulating. The discipline's core question: *can AI get better at finding errors faster than humans stop looking for them?*

---

## AI-generated research quality

David Yanagizawa-Drott ([[University of Zürich]]): part of a project to generate 1,000 economic studies using AI. Output so far is "decent" but not Nobel Prize-winning. AI can't yet produce top-tier research autonomously — it's a productivity multiplier for human researchers, not a replacement.

Soumaya Keynes (FT) used an AI agent to investigate whether AI had improved [[NBER]] abstract readability. Result: no. Average sentence length fell post-ChatGPT, but in line with older trends. Word complexity actually *rose*. The AI-assisted research process itself illustrated the limitation — the agent produced code that "took ages to check."

---

## Implications

The AI-in-economics story maps to the broader [[Enterprise AI adoption]] pattern: clear productivity gains for defined tasks (data cleaning, code, formatting), scope expansion into previously intractable problems, but no aggregate quality breakthrough yet. The error-detection channel is unique to research — it's both the highest-value application and the most vulnerable to moral hazard.

For markets, the signal is indirect but real: if AI forecasting models (like the BIS general-purpose model) prove superior at predicting macro outcomes, the competitive advantage shifts from proprietary models to data access and compute. The [[Productivity J-curve]] predicts the visible harvest comes later — but the profession's ability to validate that harvest depends on quality control mechanisms that are themselves under strain.

---

## Source

Soumaya Keynes, "Economists have caught the AI bug," *Financial Times*, Mar 19, 2026.

---

## Related

- [[Enterprise AI adoption]] — 95% pilot failure rate in enterprise; academia shows a similar mixed signal
- [[AI adoption curve]] — where academic research sits in the global adoption distribution
- [[Productivity J-curve]] — framework for why productivity gains are delayed
- [[Productivity]] — macro productivity data and AI attribution
- [[AI labor displacement]] — peer review as potential displacement target
- [[Bank for International Settlements]] — unveiled AI forecasting model Mar 16
- [[Agentic AI]] — the agent exception to enterprise AI failure; Keynes used an agent for her own research
