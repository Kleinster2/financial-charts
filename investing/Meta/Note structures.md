# Note Structures

Templates and required content for different note types.

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

## Linking practices

### Core principle: If it's mentioned, it's linked

**Every actor, company, person, or concept mentioned in a note should be a wikilink.** No exceptions. This applies to:

- Intros and summaries
- Tables (investors, customers, competitors, partners)
- Body text mentions
- Related sections

**Why this matters:**
- Broken links show what notes need to be created
- Links get resolved automatically when notes are created
- The graph reveals connections across the vault
- Readers can navigate to learn more

### Specific rules

**Link in intros.** If a note mentions multiple entities (e.g., "OTB owns Diesel, Margiela, Marni, Jil Sander"), link them all — not just ones with existing notes.

**Link in tables.** Investor tables, customer lists, competitor comparisons — every named entity should be linked:

```markdown
| Investor | Role |
|----------|------|
| [[Tiger Global]] | Series D lead |      ✓ Correct
| Greenoaks | Series B lead |              ✗ Wrong — should be [[Greenoaks]]
```

**Link in body text.** Don't leave company names, people, or concepts as plain text:

```markdown
✗ Wrong: "Acquired by Capital One for $5.15B"
✓ Right: "Acquired by [[Capital One]] for $5.15B"
```

**After creating notes, revisit links.** When you create related notes, go back and ensure all cross-references are properly linked.

**Update linked notes.** When you create a new note, add it to the Related sections of notes that reference it.

---

## Actor note requirements

| Actor type | Required content |
|------------|------------------|
| **Public companies** | Extensive historical financials (see [[Financials templates]]) |
| **Private companies** | Full cap table, historical financials, derivative arrangements (see below) |
| **Research shops / funds** | Key analysts, AUM, notable positions, recent calls |
| **Individuals** | Role, affiliations, key decisions, track record |
| **Geographies** | Economic data, key sectors, policy environment |

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

## Charts for public companies

Two standard charts for public company actor notes:

1. **Price vs benchmark** — stock performance vs relevant index (e.g., AAPL vs QQQ)
2. **Fundamentals** — revenue, net income, and free cash flow (absolute values)

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
| Banks | XLF (financials) or KBE (banks) |
| Semiconductors | SMH or SOX |
| Fintech | ARKF or IPAY |
| China tech | KWEB |
| Retail | XRT |
| Energy | XLE |

The benchmark shows sector context; the peers show relative positioning within it.

```bash
# Price comparison (normalized)
curl "http://localhost:5000/api/chart/lw?tickers=AAPL,QQQ&start=2020-01-01&normalize=true" \
  -o investing/attachments/aapl-price-chart.png

# Fundamentals (absolute values)
curl "http://localhost:5000/api/chart/lw?tickers=AAPL&metrics=revenue,netincome,fcf&start=2006-04-01" \
  -o investing/attachments/aapl-fundamentals.png
```

**Start date:** Pick a date that shows the relevant story — after major dips, IPO, or pivots.

---

## Event note structure

```markdown
#event #[category] #[year]

# Event Name

Brief summary of what happened and why it matters.

---

## What happened

Timeline, key facts, numbers.

---

## Why it matters

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
