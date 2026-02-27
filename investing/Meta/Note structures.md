# Note Structures

Templates and required content for different note types.

**Enforcement:** `scripts/check_note_compliance.py` enforces rules marked with ✓. Unmarked rules are guidance only.

| Enforced | Rule |
|----------|------|
| ✓ | Related section exists |
| ✓ | Quick stats exists |
| ✓ | Price chart (public companies) |
| ✓ | Fundamentals chart (public companies) |
| ✓ | Chart captions (italicized) |
| ✓ | Historical financials table |
| ✓ | Cap table (private companies) |
| ✓ | Ownership table (private) |
| ✓ | Leadership section |
| ✓ | Table formatting (blank line before) |
| ✓ | Frontmatter |
| ✓ | Correlation structure (sector and index notes) |
| | Currency/specificity (subjective) |
| | Sector correlation section (actor notes) |
| | Journal sections |
| | Event note structure |
| ✓ | Synopsis (actor notes) |
| ✓ | Synthesis (concept/event notes) |

---

## Synopsis (actor notes)

**Every actor note should open with a synopsis paragraph** immediately after the frontmatter one-liner. This is the lede — a reader should get the full picture from this paragraph alone.

**What to include:**
- What the company does (one clause)
- Key current metrics (revenue, valuation, circulation — whatever matters most)
- Recent catalyst or inflection point
- Bull and bear case in brief
- Forward-looking signal (what to watch next)

**Example (Circle):**
> Issuer of USDC, the #2 stablecoin ($75B in circulation). IPO'd June 2025 at $31, now trading ~$83 after a blowout first earnings report (Q4 revenue $770M, +77% YoY; FY $2.7B, +64%). The bull case: USDC is becoming the regulated stablecoin rail — Visa settlement, OCC charter, 55 financial institutions on Circle Payments Network, and Meta testing USDC payments for 3.5B users. The bear case: still GAAP-negative, rate cuts would compress reserve income, and Tether holds 60%+ market share.

**Keep it to one paragraph.** Dense, specific, no filler. If you can't summarize the thesis in one paragraph, you don't understand it well enough.

---

## Synthesis (concept and event notes)

**Concept and event notes should include a `## Synthesis` section** that connects all the threads and states what it means for positioning.

This is NOT a summary — it's the analytical layer that emerges from reading all the evidence in the note. It should answer: What's the non-obvious conclusion? How do the pieces fit together? What's the investable takeaway?

**What to include:**
- The core dynamic and whether it's accelerating or decelerating
- How recent evidence confirms or challenges the thesis
- Who benefits and who gets hurt (specific names)
- Position/conviction statement

**Placement:** After the introductory section, before detailed evidence sections. Reader gets the conclusion first, then can drill into supporting data.

**When to update:** Every time significant new evidence is added to the note, revisit the synthesis. A stale synthesis is worse than none.

---

## Currency and specificity

**Every note check must verify the note reflects current reality.**

### Currency requirements

Before marking any note "complete," web search to verify:
- Key facts are current (not stale by weeks/months)
- Major developments since last update are captured
- Numbers reflect latest available data (MAU, revenue, valuations, ownership)

**Stale notes are wrong notes.** A note saying "facing US ban" when the ban resolved is misinformation.

### Specificity requirements

**No lazy shorthand.** Vague summaries hide the actual story. Drill every claim:

| Lazy | Required |
|------|----------|
| "American-owned" | Who owns what %? Who sits on board? Who controls what? |
| "backed by major investors" | Name them. Stakes. Board seats. |
| "significant revenue" | Exact figure. Growth rate. Breakdown by segment. |
| "recently acquired" | Date. Price. Terms. Buyer. Financing structure. |
| "partnership with" | What kind? Revenue share? Exclusivity? Duration? |

**The test:** Could someone reconstruct the actual situation from your note? If not, add detail.

### Ownership and control

For any ownership change, acquisition, or restructuring, always capture:

1. **Equity stakes** — exact percentages for all material holders
2. **Governance** — board composition, who represents whom
3. **Economic rights** — licensing fees, profit shares, royalties (may differ from equity)
4. **Operational control** — who runs what functions day-to-day
5. **Retained rights** — what the seller/minority keeps (IP, brands, territories)
6. **Compliance/legal** — any concerns about whether structure satisfies requirements

**Example:** TikTok US deal — "American investors hold 80% equity" is incomplete without noting ByteDance retains algorithm IP and ~50% of profits via licensing.

### Preserving timelines

When facts evolve over time, preserve the progression rather than overwriting:

| Wrong | Right |
|-------|-------|
| Overwrite "$100B valuation" → "$110B valuation" | "Initially reported at ~$100B (Dec 2025); closed at $110B (Jan 2026)" |
| Replace "Series D pending" → "Series D closed" | Show both the initial reporting and final close |

Financial data has a lifecycle: initial reports → negotiations → final close. Each stage is information.

**When to preserve vs. replace:**

| Data type | Preserve history? |
|-----------|-------------------|
| Funding rounds (amount, valuation) | Yes — show initial reports and final terms |
| Deal negotiations | Yes — terms often change |
| Earnings/revenue | No — just update to latest |
| Headcount, MAU, fleet size | No — just update to latest |
| Ownership stakes | Yes if contested; no if routine |

**The test:** Would knowing the previous value provide insight? If a valuation jumped 10% during negotiations, that's signal. If revenue grew 5% quarter-over-quarter, that's just normal updating.

---

## Markdown formatting

**Tables need a blank line before them** — otherwise they render as unstructured text:

```markdown
# Wrong
**Current ownership:**
| Header | Header |

# Right
**Current ownership:**

| Header | Header |
```

---

## Actor note requirements

| Actor type | Required content |
|------------|------------------|
| **Public companies** | Leadership, historical financials, sector correlation (see below) |
| **Private companies** | Leadership, full cap table, historical financials, derivative arrangements (see below) |
| **Research shops / funds** | Key analysts, AUM, notable positions, recent calls |
| **Individuals** | Role, affiliations, key decisions, track record |
| **Geographies** | Economic data, key sectors, policy environment |

### Sector correlation (public companies)

Public company notes should include a **Sector correlation** section showing how the stock trades relative to validated sectors.

```markdown
## Sector correlation

| Sector | Correlation | Fit |
|--------|-------------|-----|
| [[Defense IT Services]] | **0.65** | Primary |
| [[Defense Primes]] | 0.42 | Secondary |
| [[Cybersecurity]] | 0.35 | Weak |
```

**Fit categories:**
- **Primary** — ≥0.55, stock belongs in this sector
- **Secondary** — 0.40-0.54, meaningful but weaker exposure
- **Weak** — <0.40, not a sector play

**Orphan stocks** don't fit any sector (all correlations <0.50). Mark with callout:

```markdown
> [!warning] Sector Orphan
> BA does not trade with any validated sector. Idiosyncratic story.
```

**Examples of orphans:** BA (commercial aerospace), INTC (turnaround), NU (LatAm), PYPL (loosely attached to payments)

**When to include:** Required for stocks that are outliers, borderline, or have multi-sector exposure. Optional for stocks clearly in one sector.

### Leadership section

All company notes (public and private) require a **Leadership** section:

```markdown
## Leadership

| Role | Name | Background |
|------|------|------------|
| CEO | [[Name]] | Brief background |
| CFO | Name | Brief background |
| Board Chair | Name | Affiliation |
```

**Required roles:**
- CEO / President
- CFO (if public or PE-backed)
- Key founders (if still involved)
- Board members with notable affiliations (PE sponsors, major investors)

**Wikilink executives when:**
- They have their own note (major figures)
- They're affiliated with other vault actors (e.g., DigitalBridge advisor)
- They sit on multiple boards in the vault

**Background format:** Keep brief — years experience, notable prior roles, education if relevant. Example: "20+ yrs tech/infra; ex-IBM VP LatAm, UOL Diveo COO"

### Private company depth standard

Private company notes require the same rigor as public companies. The [[Valentino]] note is the template.

**1. Full historical cap table**

Every ownership change from founding to present:

| Date | Event | Buyer | Seller | Amount | Implied EV |
|------|-------|-------|--------|--------|------------|
| 1960 | Founded | Founder | — | Seed capital | — |
| 1998 | Sale to PE | PE Fund | Founder | $XXM | $XXM |
| 2012 | Secondary | New Owner | PE Fund | $XXXM | $XXXM |

Include: founding, every sale, every funding round, every secondary, every capital injection. Note implied enterprise value at each transaction.

**The cap table replaces "Funding rounds" and "Key investors" sections.** Don't duplicate — the cap table contains all funding information plus investor details. For VC-backed startups, use columns: Date, Event, Investors, Amount, Valuation. The Related section can list key investors with annotations. See [[Brex]] for the template.

**2. Historical financials (10+ years where available)**

| Year | Revenue | Growth | EBITDA | EBITDA % | Notes |
|------|---------|--------|--------|----------|-------|
| 2015 | $XXM | — | $XXM | XX% | Context |
| ... | ... | ... | ... | ... | ... |

Show the full cycle: growth, peak, decline. Include forward estimates with "E" suffix.

**3. Derivative arrangements**

Any puts, calls, earnouts, convertibles, or warrants get a dedicated section:

| Term | Original | Current |
|------|----------|---------|
| Put option | Exercisable 2026-2027 | Postponed to 2028-2029 |
| Call option | Exercisable 2028 | Postponed to 2029 |
| Pricing basis | EBITDA multiple | Unchanged |
| Estimated price | ~$XB | "Substantially below" |

Include: exact terms, pricing formulas, exercise windows, amendments, and **strategic implications for each party** (why they'd exercise or not).

---

## Industry vs Sector notes

**Two distinct note types based on correlation:**

| Type | Correlation | Purpose | Tradeable? |
|------|-------------|---------|------------|
| **Industry** | <0.50 or umbrella | Overview, themes, market structure | No |
| **Sector** | ≥0.50 | Validated trading cluster | Yes, as basket |

### Industry notes

Industry notes provide context but are NOT tradeable baskets. Mark with callout:

```markdown
> [!info] Industry Overview
> This is an industry overview, not a tradeable sector. See related sectors below for validated trading clusters.
```

**Examples:** Data Centers, Defense, Fintech, Semiconductors, Memory

**Required content:** Market size, themes, value chain, key players, related sectors

### Sector notes

Sector notes are validated trading clusters (correlation ≥0.50). These CAN be traded as baskets.

**Examples:** DC REITs (0.69), Defense IT Services (0.61), Payments Networks (0.86), WFE (0.70)

**Required content:** Correlation structure, sector chart, key actors

Sector notes should include a **Correlation structure** section to validate the grouping.

### Correlation structure template

```markdown
## Correlation structure

| Metric | Value | Interpretation |
|--------|-------|----------------|
| **Avg correlation** | **0.XX** | Strong/Moderate/Weak |
| Range | 0.XX - 0.XX | Loosest to tightest pair |
| vs [other sector] | 0.XX | Cross-sector comparison |
| Period | 2024-01 to present | 1-2 year lookback |
```

### Interpretation scale

| Correlation | Label | Meaning |
|-------------|-------|---------|
| ≥0.60 | **Strong** | Tight sector, moves as unit |
| 0.40-0.59 | **Moderate** | Valid sector grouping |
| 0.25-0.39 | **Weak** | Loose grouping, consider splitting |
| <0.25 | **Very weak** | Not a meaningful sector |

### Benchmarks (2024-01 to 2026-01)

| Sector | Correlation | Assessment |
|--------|-------------|------------|
| GS-MS (Investment Banks) | 0.87 | Very strong (near-identical) |
| V-MA (Payments Networks) | 0.86 | Very strong (duopoly) |
| Regional Banks | 0.85 | Strong |
| US Banks (all) | 0.77 | Strong |
| EDA | 0.75 | Strong |
| WFE | 0.70 | Strong |
| DC REITs | 0.69 | Strong |
| Defense IT Services | 0.61 | Strong |
| AI Compute | 0.61 | Strong |
| Crypto-to-AI | 0.61 | Strong |
| Connectivity | 0.58 | Moderate |
| Korea Memory | 0.53 | Moderate |
| Hyperscalers | 0.52 | Moderate |
| Digital Fintechs | 0.51 | Moderate |
| US Memory | 0.50 | Moderate |
| Defense Primes (ex-BA) | 0.49 | Moderate |
| Defense (all incl BA) | 0.40 | Weak — BA is outlier |
| Data Centers (all) | 0.39 | Weak — splits into REITs vs Crypto |
| Foundry (TSM+INTC) | 0.28 | Weak — INTC is turnaround story |

**Notes on weak sectors:**
- **Foundry** doesn't exist as tradeable sector — TSMC trades with customers (NVDA 0.69, AMD 0.56) not "peers"
- **INTC** is uncorrelated with everything (0.28-0.34) — IDM turnaround/restructuring play
- **Boeing** is uncorrelated with defense primes (0.12-0.33) — commercial aerospace story
- **Data Centers** splits into DC REITs (0.69) and Crypto-to-AI (0.61) with only 0.08-0.20 cross-correlation

**When to split a sector:** If cross-correlation is <0.30 within a sector, create sub-sectors (e.g., Data Centers → DC REITs + Crypto-to-AI).

### ETF benchmarks by sector

Some sectors have ETFs that track well; others are market-uncorrelated with no good benchmark.

| Sector | Best Benchmark | Correlation | Notes |
|--------|----------------|-------------|-------|
| AI Compute | SMH | 0.71-0.84 | Semis ETF covers NVDA, AMD, TSM |
| WFE | SMH | 0.54-0.86 | Equipment makers in semis ETF |
| Connectivity | SOXX | 0.75-0.80 | Networking chips |
| Banks | KBE | 0.68-0.76 | Regional bank ETF; XLF too diluted |
| Payments Networks | SPY | 0.39-0.40 | Weak fit; V-MA are unique duopoly |
| US Retail Trading | ARKF | 0.74-0.80 | Fintech ETF covers HOOD, COIN |
| DC REITs | VNQ | 0.57-0.64 | Real estate ETF; partial fit |
| Crypto-to-AI | BITO | 0.41-0.58 | Bitcoin futures; loose fit |
| Defense Primes | — | 0.11-0.34 vs SPY | **Market-uncorrelated** |
| Defense IT Services | — | ~0.30 vs SPY | **Market-uncorrelated** |
| Life Insurance | — | 0.27-0.45 vs SPY | **Market-uncorrelated** |
| P&C Insurance | — | 0.18-0.28 vs SPY | **Most market-uncorrelated** |
| Alt Managers | — | 0.47-0.51 vs SPY | **Weak market correlation** |

**Market-uncorrelated sectors** (Defense, Insurance, Alt Managers) trade on industry-specific drivers (defense budgets, underwriting cycles, AUM/deal flow) rather than GDP or tech earnings. These function as natural hedges against growth/tech exposure.

### Sector charts

**Every sector note requires a comparison chart** showing normalized performance of all key actors.

```bash
# Sector chart (all actors, normalized, no title since legend shows tickers)
curl "http://localhost:5000/api/chart/lw?tickers=ASML,AMAT,LRCX,KLAC&start=2024-01-01&normalize=true" \
  -o investing/attachments/wfe-sector-chart.png
```

**Chart placement:** Immediately after the intro paragraph, before Key actors table.

**Chart caption:** Italicized line below explaining what the chart shows — which names outperforming, correlation visible in movement, any divergences worth noting.

```markdown
![[wfe-sector-chart.png]]
*LRCX outperforming, but all four move together. AMAT-LRCX especially tight (0.90 correlation).*
```

**Naming convention:** `{sector-name}-sector-chart.png` (lowercase, hyphenated).

### Journal section

**Concept and sector notes should include a Journal section** for logging significant market-moving events. This gives structural notes a timestamped record of catalysts without mixing them into reference content.

```markdown
## Journal

| Date | Event | Impact |
|------|-------|--------|
| 2026-01-30 | [[Kevin Warsh]] nominated Fed Chair | Curve steepened, deregulation expectations |
| 2026-01-28 | FOMC holds rates | First pause since July |
```

**When to add entries:**
- Policy changes affecting the sector/concept
- Major earnings that move the group
- Regulatory actions
- Leadership changes at key institutions
- Significant price moves with clear catalysts

**Placement:** After the main structural content, before Related section.

**Link to daily notes:** Journal entries should also appear in the corresponding daily note's Markets section with full detail. The journal is a quick-reference log; the daily has the full narrative.

---

## Charts for public companies

Two standard charts for public company actor notes:

1. **Price vs benchmark** — stock performance vs relevant index (e.g., AAPL vs QQQ)
2. **Fundamentals** — revenue and net income in separate panes (automatic when both metrics requested)

**Every actor gets their own chart.** Never reuse another actor's chart — even if the tickers overlap. Each actor needs peers relevant to *them*:

| Actor | Good peers | Bad peers |
|-------|------------|-----------|
| Barclays | UK banks (HSBC, Lloyds) | European banks (DB, UBS) |
| TSMC | Foundry peers (Samsung, Intel Foundry) | Generic "semis" |
| Nubank | LatAm fintechs (StoneCo, Inter) | US neobanks |

The peer set tells a story. Wrong peers = wrong story.

**Chart composition: actor + peers + sector benchmark.** Every comparison chart includes three elements:

1. **The actor** — the subject of the note
2. **2-3 relevant peers** — direct competitors or comparable companies
3. **Sector benchmark** — ETF/index for the peer group

Example for Barclays: `BCS, HSBC, LYG, NWG, XLF`

| Actor type | Sector benchmark |
|------------|------------------|
| US banks | KBE (banks) or XLF (financials) |
| European banks | EUFN (Europe financials) |
| US semiconductors | SMH or SOX |
| European semiconductors | Add SMH to database |
| US fintech | ARKF or IPAY |
| China tech | KWEB |
| US retail | XRT |
| US energy | XLE |
| LatAm | Find regional ETF or use US sector peer |

The benchmark shows sector context; the peers show relative positioning within it.

```bash
# Price comparison (normalized) — primary= ensures actor gets consistent blue color
curl "http://localhost:5000/api/chart/lw?tickers=AAPL,QQQ&start=2020-01-01&normalize=true&primary=AAPL" \
  -o investing/attachments/aapl-price-chart.png

# Fundamentals (separate panes for revenue and net income)
curl "http://localhost:5000/api/chart/lw?tickers=AAPL&metrics=revenue,netincome&start=2015-01-01" \
  -o investing/attachments/aapl-fundamentals.png
```

**Primary parameter:** Use `primary=TICKER` to ensure the actor always gets the first color (blue #2962FF). This provides visual consistency — the actor is always blue in its own note.

**Start date:** Pick a date that shows the relevant story — after major dips, IPO, or pivots.

---

## Standard section: Insights

**Use `## Insights` instead of "Why X matters"** for the key takeaways section in all note types.

This section answers: What's the non-obvious takeaway? What pattern does this reveal? Why should an investor care?

```markdown
## Insights

- Independent title insurers doubled share (15% → 27%) by not competing with their own agents
- Agent-only model eliminates channel conflict that plagues Big Four
```

**Keep it tight:** 2-4 bullets. Each insight should be specific and backed by data in the note.

---

## Event note structure

```markdown
#event #[category] #[year]

# Event Name

Brief summary of what happened and why it matters.

---

## Deal terms (for M&A/funding)

| Metric | Value |
|--------|-------|
| Combined valuation | $X |
| Exchange ratio | X:1 |
| Cash option | $X/share |

---

## What happened

Timeline, key facts, numbers.

---

## The real story (for major events)

Historical arc showing motivations — trace back years if needed.

---

## Insights

Impact, implications, what changed.

---

## Actors involved

| Actor | Role |
|-------|------|
| [[Company A]] | Acquirer |
| [[Company B]] | Target |
| [[Person X]] | Decision-maker |

---

## Related

- [[Actor 1]] — role in event
- [[Concept]] — dynamic this illustrates
- [[Other Event]] — connected event
```

### Deal terms checklist (M&A events)

For mergers, acquisitions, and major funding rounds, capture transaction mechanics:

| Required | Field |
|----------|-------|
| ✓ | Valuation (pre/post, implied multiples) |
| ✓ | Consideration (cash/stock mix, exchange ratio) |
| ✓ | Premium to prior round/trading price |
| ○ | Cash option (if any) |
| ○ | Legal counsel (both sides) |
| ○ | Conditions/regulatory approvals needed |
| ○ | Timeline (signing → expected close) |
| ○ | Break fees |

**Example (SpaceX-xAI):**
```markdown
| Metric | Value |
|--------|-------|
| Combined valuation | **$1.25 trillion** |
| SpaceX valuation | $1 trillion |
| xAI valuation | $250 billion |
| Exchange ratio | 0.1433 xAI → 1 SpaceX |
| Cash option | $75.46/share (for xAI execs) |
| Legal counsel | Sullivan & Cromwell (SpaceX), Gibson Dunn (xAI) |
```

### Historical arc section ("The real story")

**For strategic events, trace the story back years.** Surface-level deal announcements miss the "why now" — the motivations, failed attempts, and relationships that led here.

**When to include:**
- M&A between companies with prior relationship
- Strategic pivots reversing earlier decisions
- Deals involving serial acquirers or repeat players
- Events with regulatory/political backstory

**Format:** Timeline table showing key moments, then narrative connecting them.

```markdown
## The real story: The 12-year arc

| Year | Event |
|------|-------|
| 2012 | Hassabis warns Musk: AI could follow humans to Mars |
| 2014 | Google acquires DeepMind; Musk tried to block |
| 2015 | Musk + Altman found OpenAI as counterweight |
| 2018 | Musk leaves OpenAI board after equity dispute |
| 2023 | Launches xAI (4 months after signing AI moratorium) |
| **2026** | **SpaceX acquires xAI** |

**Court documents** (Musk v. OpenAI, trial Apr 2026):
- Musk wanted $80B foundation with his children controlling AGI
- Called Hassabis capable of creating "AGI dictatorship"
```

**Source types for historical arc:**
- Court filings and depositions
- SEC filings (proxy fights, 13D/G, S-1 risk factors)
- Prior interview quotes with dates
- Regulatory submissions
- Contemporary news reports (not retrospective summaries)

### Comparative financial tables

**When covering a struggling or controversial company, show metrics against a healthier peer.** Raw numbers lack context; ratios reveal the real story.

```markdown
## xAI's burn problem

| Metric | xAI | OpenAI |
|--------|-----|--------|
| Monthly burn | ~$1B | ~$750M |
| 2025 revenue | ~$500M | ~$12-13B |
| Burn-to-revenue | **26:1** | 0.7:1 |
| MAU | 64M | 800-900M WAU |

**Translation:** xAI's valuation only makes sense with exit strategy.
```

**When to use:**
- Company burning cash faster than peers
- Valuation premium without revenue support
- Strategic rationale depends on comparison (acquirer vs target)

**Key ratios:**
- Burn-to-revenue (monthly burn ÷ monthly revenue)
- Valuation-to-revenue (market cap or valuation ÷ ARR)
- Relative growth rates
- Unit economics comparison

### Key quotes section

**For events with notable public statements, collect quotes with attribution and date.**

```markdown
## Key quotes

**Musk on merger (Feb 2026):**
> "This marks not just the next chapter, but the next book..."

**Musk on existential stakes (Dec 2025):**
> "We might have AI smarter than any human by the end of this year..."
```

**When to include:**
- CEO/founder statements explaining strategic rationale
- Quotes that contradict prior positions
- Statements with legal/regulatory implications
- Predictions with specific timelines (track later)

### Regulatory exposure section

**For events involving regulated industries or antitrust risk, create a systematic matrix.**

```markdown
## Regulatory exposure

| Agency | Concern |
|--------|---------|
| **CFIUS** | National security — defense contracts + foreign investors |
| **FTC/DOJ** | $1.25T consolidation across multiple sectors |
| **SEC** | Self-dealing between controller's entities |
| **FCC** | 1 million satellite authorization pending |
```

**When to include:**
- Cross-border M&A (CFIUS)
- Large horizontal mergers (FTC/DOJ)
- Deals involving government contractors
- Related-party transactions (SEC)
- Sector-specific regulators (FCC, FDA, FERC, etc.)

### Corporate structure diagrams

**For complex ownership or consolidation events, use ASCII diagrams to show relationships.**

```markdown
## "Muskonomy" consolidation

```
Tesla ($2B invested in xAI → now SpaceX subsidiary)
    ↓
xAI (Grok + X platform)
    ↓
SpaceX (rockets, Starlink, Starshield, space DCs)
```
```

**When to use:**
- Holding company structures
- Related-party transactions (who owns what % of whom)
- Vertical integration chains
- Before/after ownership comparisons

**Keep it simple:** ASCII diagrams should clarify, not complicate. If the structure needs more than 10 lines, consider a table instead.

### When to create an Event note

| Event type | Create Event note? |
|------------|-------------------|
| M&A (mergers, acquisitions, divestitures) | Yes |
| Bankruptcies, restructurings | Yes |
| IPOs, spinoffs, delistings | Yes |
| Major funding rounds ($100M+) | Yes |
| Major product launches | Yes |
| Strategic pivots, major partnerships | Yes |
| Major legal/regulatory actions | Yes |
| Quarterly earnings | No (stays in actor) |
| Minor executive changes | No (stays in actor) |
| Small funding rounds | No (stays in actor/daily) |
| Routine product updates | No (stays in actor) |

### Concept note maintenance

**When an event validates, changes, or advances a concept, update the concept note with a dated section linking back.**

The concept note should remain a structural reference — don't bloat it with event details. Instead, add a brief dated section at the end that:
1. States what changed
2. Links to the event note for full analysis
3. Updates any estimates/timelines

**Example (Space data centers → SpaceX-xAI merger):**

```markdown
## SpaceX-xAI merger (Feb 2, 2026)

**Merger rationale explicitly cites space DCs:**

> "Global electricity demand for AI simply cannot be met with terrestrial solutions..."

**Musk's updated timeline:**
- "Within 2-3 years, lowest cost to generate AI compute will be in space"
- 100 GW/year of solar-powered AI satellites within decade

See [[SpaceX xAI merger]] for full analysis.

*Updated 2026-02-03*
```

**When to update concept notes:**
- Major company commits to the concept (validates thesis)
- Timeline estimates change materially
- New technical approach announced
- Regulatory environment shifts
- Concept moves from speculative → concrete (or vice versa)

**What NOT to do:**
- Don't duplicate event details in concept note
- Don't remove structural content to make room
- Don't update for minor news that doesn't change the concept

### Actor notes reference events

Actor notes should have a "Key events" section:

```markdown
## Key events

- [[Saks-Neiman merger]] — 2024, $2.7B acquisition
- [[Saks bankruptcy]] — Jan 2026, Chapter 11
```

---

## Daily note structure

1. **Vault activity** (at top): Track notes created/modified
   - Created: table with Note, Type, Topic
   - Modified: table with Note, Changes
2. **Market data**: Levels, moves, key stats
3. **Topic sections**: News by category (varies by day)
4. **Thesis implications table**: Columns: Thesis, New evidence, Direction
5. **Open threads**: Checklist of things to track/follow up
6. **Sources**: Articles referenced

---

## Related section format

Notes should end with an annotated `## Related` section:

```markdown
## Related

- [[NVIDIA]] — primary customer, GPU ecosystem
- [[Broadcom]] — competitor in PCIe switches
- [[AI hyperscalers]] — end customers driving demand
```

**Relationship types to annotate:**
- Customer / supplier
- Competitor / peer
- Investor / investee
- Partner
- Adjacent player (same ecosystem, different layer)
- Industry context (concept notes)

### Actor Related section with sub-sector

When an actor belongs to a sub-sector with a sister concept:

```markdown
### Sectors
- [[AI Storage]] — sub-sector (→ [[AI storage bottleneck]])
- [[AI Infrastructure]] — parent sector
```

The `(→ [[concept]])` notation hints that the concept exists without creating a redundant direct link.

---

## Lessons sections

Some notes — particularly concepts and events — yield genuine investment lessons. When they do, capture them explicitly.

### When to include a Lessons section

| Criterion | Explanation |
|-----------|-------------|
| **Completed cycle** | A boom-bust, failure, or strategic arc has played out with known outcomes |
| **Measurable results** | Capital was deployed and returns (or losses) can be quantified |
| **Structural takeaways** | The failure/success modes are repeatable patterns, not one-off situations |
| **Non-obvious** | The lessons aren't just "don't lose money" or the bull/bear case restated |

### When NOT to include a Lessons section

| Criterion | Explanation |
|-----------|-------------|
| **Story still developing** | No lessons from an ongoing situation — you're guessing, not concluding |
| **Sector overview or actor profile** | These describe the present, not a completed narrative |
| **Restating bull/bear** | If the "lessons" are just the investment case reframed, skip it |
| **No hard data** | Pattern-matching without measurable outcomes is speculation |

### Format

```markdown
### Lessons

1. **Short thesis.** Supporting evidence with numbers
2. **Short thesis.** Supporting evidence with numbers
```

Keep to 3-5 lessons maximum. Each must be backed by specific data from the note.
