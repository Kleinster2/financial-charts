# Research Workflow

## Sourcing Standards

**Prefer official sources for hard data:**

| Data type | Primary source | Fallback |
|-----------|----------------|----------|
| Revenue, Net Income, EPS | 10-K, 10-Q | Earnings releases |
| Employee headcount | 10-K (annual), proxy | News (flag as estimate) |
| Segment breakdown | 10-K, 10-Q | Investor presentations |
| Guidance | Earnings calls, 8-K | News coverage |
| Ownership/cap table | Proxy (DEF 14A), 13-F | News (flag as estimate) |
| Bond prices/yields | Bloomberg terminal | BondbloX (free yield/Z-spread/duration; news articles have actual prices) |

Non-filing sources: note it — "~210k employees (company website, Jan 2026)"

**SEC EDGAR shortcuts:**
- All filings: `https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=TICKER&type=10-K`
- Recent 10-K: search `"[company] 10-K 2024 filetype:pdf"`
- CLI: `python scripts/parse_sec_filing.py TICKER --save /tmp/filing.txt` (run `--help` for full usage)

**Quarterly data from SEC filings:**
- Q1, Q2, Q3 come from 10-Q filings
- Q4 must be **calculated**: 10-K annual total minus (Q1+Q2+Q3) — 10-Ks only report full-year figures
- Avoid 8-K for earnings — just a wrapper; numbers are in exhibits
- Always extract **granular segment data**, not just top-level revenue/margins (business segments, geographic breakdown, product line detail)

---

## Daily News Search

### Search API Tips

**Prefer freshness filters over exact date strings.** Exact dates like `"February 4 2026"` often return 0 results — articles don't always include the literal date string. Instead:

```
# Good — uses API freshness filter
web_search(query="stock market gainers losers", freshness="pd")  # past day
web_search(query="AMD earnings", freshness="pw")  # past week

# Often fails — exact date string
web_search(query="\"February 4 2026\" stock market")  # returns 0
```

**Rate limiting (Brave free tier):** 1 request/second. Run searches sequentially, not in parallel. Paid tier ($5/mo) allows 15 req/sec.

### Category Searches

| Category | Search terms |
|----------|--------------|
| **Market movers** | "biggest stock gainers losers [date]" |
| **Macro** | "markets treasury dollar Fed [date]" |
| **Semiconductors** | "semiconductor chip memory [date]" |
| **AI** | "AI artificial intelligence [date]" |
| **China** | "China economy tech [date]" |
| **Asia semis** | "Japan Korea semiconductor [date]" |
| **Trade/Policy** | "tariffs trade regulation policy [date]" |
| **Defense** | "Pentagon military defense tech [date]" |
| **Energy** | "energy power grid nuclear [date]" |
| **Europe** | "Europe economy tech [date]" (weekly) |
| **Earnings** | Check calendar |

**Market movers catch what categories miss.** Corning +17% on Meta deal wouldn't appear in "semiconductor" searches.

**Don't miss:** China domestic news (GDP, NDRC, stimulus) — often absent from US-focused searches.

---

## Source Separation: Facts vs. Framing

Every source — article, transcript, podcast, filing — contains two things: facts and framing. The vault imports facts. It never imports framing. We build our own.

**Facts** are verifiable: dates, figures, events, quotes, legal filings, corporate actions. They can be confirmed or contradicted by independent sources.

**Framing** is interpretation: narrative arcs ("rise and fall"), causal claims ("this triggered"), characterizations ("crown jewel," "aggressive," "hubris"), and editorial structure (villain/hero, genius/fraud). Every source has a story it's telling. That story is not our story.

**The rule:** Extract what happened. Do not import why the source thinks it happened, how they feel about it, or the narrative structure they built around it. The vault reader forms their own interpretation from the facts.

**Process the entire source.** Do not skim for key points or extract highlights. Go through every paragraph, every aside, every throwaway detail. The facts that matter most are often buried in parentheticals, background context, or passing mentions — not in the headline claims. A source that spends three paragraphs on a dramatic narrative arc may contain one sentence with a specific date, figure, or entity name that no other source has. That sentence is the value. Miss it by skimming and the ingestion was incomplete.

**What this means in practice:**
- "Acquired X for R$10M" → import
- "In a brilliant move, acquired X" → do not import "brilliant"
- "Stock fell 97%" → import
- "The company was essentially worthless" → do not import the characterization
- "Creditors executed collateral guarantees in Feb 2026" → import
- "The empire collapsed like dominoes" → do not import the metaphor
- "PF alleges hidden partnership" → import (attributed)
- "This was the greatest financial engineering scheme in Brazilian history" → do not import the superlative

**Narrative traps to watch for:**
- Rise-and-fall arcs (sources love these; reality is messier)
- Single-cause explanations ("X triggered everything" — usually multiple factors)
- Hindsight framing ("this would later prove fatal" — we don't know that at time of writing)
- Moral framing ("greed," "hubris," "reckless" — these are judgments, not facts)
- Compression of ambiguity into certainty (investigations become convictions, allegations become facts)

**When ambiguity exists, preserve it.** If something is alleged, say "alleged." If the outcome is contested, say "contested." If there are open questions, list them. The vault is not a courtroom and not a newspaper — it doesn't need to pick a side.

---

## Analysis Sections

The vault's purpose is not just to store facts — it's to interpret them. Mature notes should include an Analysis section that connects the facts already in the note into investment-relevant interpretation.

**The constraint:** Every claim in the editorial must trace back to a fact in the same note. If it requires outside knowledge, assumptions, or narrative imported from a source, it doesn't belong. The test: could someone read only the facts in the note and arrive at the same conclusions?

**What good analysis does:**
- Surface structural patterns (e.g., a portfolio table that shows no exits across nine holdings)
- Identify tensions between facts in the same note (e.g., a CVM fine for the same pattern alleged decades later)
- Describe mechanical relationships (e.g., how cross-collateral propagates a single default across unrelated holdings)
- Name what's unresolved honestly — open questions, not false certainty

**What analysis is not:**
- Imported narrative from a source dressed up in our voice
- Moral judgments ("reckless," "visionary," "fraudulent")
- Predictions about outcomes of ongoing investigations or deals
- Filler opinions on companies we don't have enough facts to interpret

**When to include one:**
- The note has enough factual surface area that patterns emerge from reading it
- Stubs and thin notes skip this — three facts don't need analysis
- When the facts are genuinely ambiguous or contradictory, the analysis is where that tension gets named

**Format:** Place after Status/Open questions, before Related.

---

## Fact-Checking Non-Filing Sources

Transcripts, podcasts, YouTube videos, and press interviews often contain inflated or imprecise figures. These sources are valuable for data points and claims — but numbers must be verified before entering the vault as fact.

**Process:**
1. Extract facts from the source (dates, figures, events, attributed claims)
2. Do not carry over the source's narrative structure, characterizations, or causal framing
3. Identify all quantitative claims and dateable assertions
4. Cross-reference each against filings, Bloomberg, or reputable financial press
5. Mark each claim in the notes:
   - Verified → state as fact with source
   - Contradicted → correct the figure, cite the better source
   - Unverifiable → keep the claim, mark as "argued" or "unverified"

**Never remove unverified claims.** The vault captures what was claimed. Use qualifiers:
- "argued" — source asserts this but filings/data don't confirm
- "unverified" — no independent source found to confirm or deny
- "[figure] per [source]; [different figure] per [better source]" — when sources conflict

**Common inflation patterns in oral sources:**
- Market cap and revenue rounded up or cited at all-time highs
- Margins quoted from best quarter, not trailing average
- Production/output figures lagging behind recent acquisitions or disposals
- Timelines compressed ("15 months later" when the full cycle was longer)
- Nationality, birthplace, and biographical details garbled

**Daily note documentation:** When ingesting a transcript or non-filing source, include a fact-check table in the daily note showing each claim, verdict, and any correction applied. This creates a permanent audit trail.

---

## Verify Before Reporting

**Summary articles recycle recent news as "context."** This pollutes results.

**For any major deal/announcement:**
1. Search `"[company] [deal] announcement date"` to verify timing
2. If older than 3 days, classify as "Recent" not "Today"

**Present news in two sections:**

| Section | Criteria |
|---------|----------|
| **Confirmed Today** | Verified same-day (earnings, FOMC, stock moves with %) |
| **Recent (Not Today)** | Announced earlier — include actual date |

**Red flags for recycled news:**
- Acquisitions/deals (often announced weeks ago)
- "Landmark" or "historic" framing
- Round-number valuations without transaction details

---

## Follow Up on Big Movers

**Any stock move >10% needs a "why" search.**

1. Search `"[ticker] stock why up/down [date]"`
2. Identify catalyst (earnings, deal, upgrade, macro)
3. Include in report with context

---

## Earnings Searches

**General searches miss forward guidance.** Run two searches:

1. General: `"[company] earnings [date]"` — headline results
2. Guidance: `"[company] Q1/FY guidance [date]"` — forward estimates

Forward guidance often moves stocks more than backward-looking beats.

### Earnings Calendar (CRITICAL)

**Always check earnings calendar when doing daily news.** Don't rely on category searches to surface earnings.

1. **Search:** `"earnings reports week [date]"` or `"earnings calendar [date]"`
2. **Check prior day's after-hours** — results release after market close
3. **Check today's pre-market** — some report before open

**Must-cover earnings (beyond focus areas):**

| Category | Tickers | Why |
|----------|---------|-----|
| Mag 7 | AAPL, MSFT, GOOGL, AMZN, META, NVDA, TSLA | Market leaders |
| Financials | JPM, GS, BAC | Credit/macro signal |
| Consumer | DIS, PYPL, NFLX, SBUX | Spending signal |
| Industrial | CAT, UPS, FDX | Economy signal |
| Semis | AMD, INTC, QCOM, MU, TXN | Cycle signal |

**For each earnings report:**
- Add section to actor note (EPS, revenue, guidance, stock reaction)
- Add to daily note
- Note CEO changes, guidance surprises, strategic shifts

---

## Processing New Information

**Every piece of news needs an atomic home — daily notes are never the only location.**

1. **Check existing notes first** — search vault before web
2. **Find the right home** — actors taking actions, not catch-all concepts
3. **Regional actors stay high-level** — specific news → specific actors
4. **Always update daily notes** — use event date, not article date
5. **Check for events** — M&A, bankruptcy, IPO → create Event note
6. **Recognize systemic events** — if same news hits 2+ actors, create Concept/Event note first
7. **Trace repercussions** — how did markets react?

### Tracing Market Repercussions

| Asset class | What to look for |
|-------------|------------------|
| Treasuries | Yield curve shifts (2Y, 10Y, 30Y) |
| Equities | Index moves, sector rotation |
| FX | Dollar, relevant currency pairs |
| Commodities | Gold, oil if macro-relevant |
| Sector ETFs | Rate-sensitive (XLF, XLU, XLRE) |

**Process:**
1. Update primary actor note(s)
2. Search for market reaction
3. Add to daily note Markets section
4. Add to Journal sections of affected concept/sector notes

### Systemic vs Company-specific

| Signal | Action |
|--------|--------|
| Same news hits 2+ companies | Create concept/event note first |
| Policy/regulatory change | Concept note for the policy |
| Sector-wide selloff | Concept note for the catalyst |
| Macro event | Concept note |

Actor notes answer "how does this affect THIS company specifically?" — don't re-explain sector-wide context.

### Actor Note Discipline (CRITICAL)

**Daily notes are never sufficient.** Every company mentioned in daily news must have its actor note updated or created.

**For existing notes:**
- Add dated section with the new development
- Include stock move with %
- Link to relevant Event/Concept notes

**For missing notes:**
- Create the actor note before finishing daily note
- Do brief web research to establish basics (what they do, market cap, key metrics)
- Follow actor note structure from [[Note structures]]

**Systemic events — order of operations:**
1. Create Event/Concept note for the catalyst FIRST
2. Update all affected actor notes (link back to event)
3. Update daily note (link to event and actors)

Example: Claude Cowork disruption (Feb 2026) hit 10+ companies → create `[[Claude Cowork disruption February 2026]]` event note first, then update Thomson Reuters, RELX, ServiceNow, etc. with links back to the event.
