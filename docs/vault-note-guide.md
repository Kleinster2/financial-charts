# Vault Note Guide

Reference for note structure, voice, and architecture. Read on demand when writing or reviewing notes.

---

## Actor Note Philosophy: Executive Brief + Comprehensive Primer

An actor note serves two functions simultaneously:

1. Frame the key economic value questions. The Synopsis distills the 3-5 durable questions that determine the entity's economic value — not "what's the stock doing" but "what determines whether this entity is worth more or less." These questions should still be relevant six months from now.

2. Provide everything the reader needs to answer those questions independently. The body is a comprehensive primer: ownership structures, financials, competitive dynamics, regulatory context, technology, history. A complete actor note is self-contained.

Stock price moves, analyst calls, and catalysts go in the securities note (`Assets/`), not the actor note. The actor note cites earnings numbers and business events; the securities note tracks how the market priced them.

Synopsis framing: key economic questions, not market recap. Center on the questions that matter: Is the core business durable? Is the valuation justified? What structural forces help or hurt? Catalysts are evidence supporting a question, not standalone listicle items.

Answer your own questions. The body must contain analytical sections that directly address the Synopsis questions — not just factual/historical sections. A note that frames three questions and then provides only chronological facts is half a note.

No bull/bear framing. Do not organize analysis into "bull case" / "bear case." Present dynamics, what's structurally different or historically consistent, and what's unresolved. Same applies to "risks vs. opportunities" and any other binary editorial frame.

Sum-of-parts in prose. When a SOTP structure exists, state it plainly with numbers inline.

### Voice and density: the Hyundai standard

Every actor note should read like a sharp analyst briefing someone smart over coffee — not a Wikipedia article, not a consulting deck. Lead with what matters most. Stack dynamics with specific numbers and chain logic. Use analyst quotes as named evidence, not anonymous authority. State SOTP math in plain English.

Gold standard example (Hyundai Motor synopsis):

> Hyundai traded sideways at 100K-300K KRW for a decade. After the Atlas humanoid debut at CES 2026 (Jan 5), it doubled to 674K KRW. Now pulled back to 492K KRW (~27% off peak). Forward PE ~9.6x.
>
> Three dynamics are driving the repricing:
>
> 1. Boston Dynamics IPO (potentially 2027 Nasdaq). Hyundai owns 88% (affiliates 68% + Chairman Chung Euisun personally 22.6%). Valuations range wildly: KB Securities 128T won, Hanwha 150T won, others 40-60T won. Chung paid ~$220M for his 20% stake — could be worth $13.6B+. SoftBank holds 9.5% with a put option exercisable by June 2026. CEO Robert Playter just left, replaced by CFO Amanda McMaster — commercial pivot signal. Atlas production target: 30,000 units by 2028 at $130-140K each.
> 2. Governance restructuring. BD IPO proceeds give Chung the war chest to unwind Hyundai's circular ownership (the only major Korean chaebol that still has it). Inheritance tax on his father's 7T+ won stake alone is ~4T won. This has been a decade-long investor complaint — resolution would trigger a Korea discount unwind.
> 3. Google DeepMind partnership for Atlas AI + Nvidia for autonomous driving. Previously the knock on Atlas was Tesla Optimus had the data advantage. DeepMind collaboration changes that equation. Samsung Securities analyst: "If robotics and solid-state battery tech are validated, Tesla — not Toyota — becomes the valuation comp."
>
> Open questions: Analysts cut 2026 earnings estimates 22% on tariffs at 25% on Korea (deal to reduce to 15% but Korean legislature hasn't ratified). Pulled IONIQ 6 from US market (tariff-exposed, made in Korea); IONIQ 5/9 safe (Georgia plant). Chinese EVs eating market share outside US/India. $20B US investment + $5.8B Louisiana steel plant is political insurance but capital-heavy. BNP Paribas calculates the core auto business trades at 10.3x PE after stripping out Hyundai Motor India + Boston Dynamics — the SOTP math hinges on what BD IPO actually prices at and whether the governance restructuring materializes.

---

## Synopsis (Actor Notes)

Every actor note (non-stub) must include a synopsis immediately after the frontmatter/one-liner intro and before Quick stats. No `## Synopsis` header — the position does the work. This is a 2-4 paragraph dense summary that frames the key economic dynamics: what the entity is, the dynamics driving it, and the open questions. Sharp prose with hard numbers — a self-contained briefing, not a teaser.

---

## Evolution Section (Actor Notes)

Company, country, and institution actor notes should include an Evolution section — narrative history with analytical teeth, not a bullet-point timeline. Each entry explains *why* that moment mattered and what it caused.

Style: Each bullet is a year or era, written as a dense paragraph. Open with a thesis sentence that frames the arc ("The story of X is the story of Y"). Each entry should:
- Start with the date/era
- State what happened
- Explain *why* it mattered — the strategic logic, the mistake, the consequence
- Connect to what came before and after (cause → effect chains)
- Include hard numbers (valuations, GPV, MAU, stock prices) to anchor the narrative

What to cover: Founding story, key pivots, acquisitions (with deal terms and whether they worked), leadership changes, crises, stock/valuation inflection points, competitive dynamics, and the current state. Don't skip the failures.

What NOT to do:
- Don't write a dry timeline ("2018: Acquired X for $Y")
- Don't skip years where nothing happened — the gap is the story
- Don't editorialize without evidence

Length: Scale to complexity. 3-4 bullets for a startup, 10-12 dense paragraphs for a complex company. Evolution can be the longest section.

Template opening: "The story of [Company] is the story of [core tension/arc]."

Reference: See [[Block]] for the gold standard.

Other rules:
- Wikilink to other vault entities mentioned in the evolution
- Cross-vault URI links when evolution connects to history vault themes
- Stubs don't need Evolution — add when the note matures

---

## Leadership Section (Actor Notes — Triggered)

An optional "Leadership (current)" table for actor notes where organizational structure is itself an investable signal. Not default — triggered by either condition:

1. **3+ senior leadership changes in 12 months** (C-suite, function heads, board-level)
2. **Org structure is the thesis** — a safety vacuum, strategic pivot readable through personnel, founder/key-man risk, or leadership churn that signals execution risk

**Placement:** Between Quick stats and Synopsis. Replaces any CEO/COO/CTO rows that were in Quick stats (avoid duplication).

**Format:**

```markdown
## Leadership (current, [month year])

| Function | Leader | Since | Prior | Notes |
|----------|--------|-------|-------|-------|
| CEO | [[Name]] | Date | Previous employer/role | — |
| [Function] | Vacant | Date | Last holder → where they went | Duration of vacancy |
| [Function] | Disbanded | Date | Last leader → reassigned role | Why it was eliminated |
```

**Rules:**
- Include vacancies and disbanded functions — absences are signals
- "Prior" column shows where the person came from (for new hires) or where they went (for vacancies)
- One interpretive paragraph below the table tying org structure to strategy
- Update the date in the header when the table changes
- If the company stabilizes (no changes for 12+ months), the section can stay but mark it "(stable)" in the header

**Examples of companies that qualify:** [[OpenAI]] (CTO vacant 19 months, safety team disbanded, infra leadership turnover, apps consolidation), [[Intel]] (CEO transition, foundry spinoff leadership), [[Oracle]] (co-CEO split, Ellison key-man risk at 80+).

**Companies that don't need it:** Stable leadership where the org chart isn't the story. Most actor notes.

---

## Synthesis Sections

Distinct from Synopsis (which frames the key economic questions for actors). Synthesis is the "so what" — interpretation of where a thesis or situation stands now, derived from the accumulated data in the note.

**Daily notes** open with `## Synthesis` — a narrative connecting all ingested stories, written after the session's work is done. What threads connect, what's accelerating, what the day means for positioning. Structure: `## Synthesis` → `---` → `## Notes created/expanded` → `## Edit log`.

**Mature concept and event notes** get `## Synthesis` right after the one-liner and `---`. Not a summary of the note but the current state of the argument: what's confirmed, what's contradicted, where the position is. Updated as new data comes in — this is a living section, not a one-time write.

**Actor notes** already have Synopsis serving this purpose. **Thesis notes** already lead with the thesis statement. Neither needs a separate Synthesis.

Structure for concept/event: one-liner → `---` → `## Synthesis` → `---` → data sections.

### Synthesis voice — narrative arc, not bullets

A Synthesis section (and the Synopsis in an actor note) reads as a story, not a list. The voice that works:

- **Open with the central insight** — name what the story actually IS in the first two sentences. Not "here are the facts" but "the binding constraint is X." The reader should know the thesis before they know the data.
- **Trace the constraint chain** — walk the causality from center outward. "Start at the center. Next is X. Then Y." Each paragraph reinforces the argument by adding a constrained link, not by switching topics.
- **Embed specific figures in flowing prose** — "Micron returned +441%" inside a sentence, not as a bullet. Numbers do the work; they should live inside the argument, not beside it.
- **End with a cautionary tale or counter-example** — the case that closes the loop by showing what happens when the thesis *doesn't* hold. (Example: Ajinomoto as the dilution counter-case to the packaging-scarcity thesis.) Symmetry is persuasive.
- **Finish with a one-line version** — a tight takeaway that compresses the whole argument into a single sentence. Bold allowed here since it's a heading-equivalent.

What to avoid: bullet lists for the analytical core (save bullets for reference tables and data), topic headers inside the Synthesis (it should flow as continuous prose), recapping what's already in the data sections below. Synthesis is argument, not summary.

The test: can the reader close the note after the Synthesis and still understand the position? If yes, the Synthesis is doing its job.

---

## Event Notes to Unburden Actors

When a single event touches 3+ actor notes, create a dedicated event note (in `Events/`) with the full detail. Actor notes carry short summaries + link to the event note. This prevents duplication and keeps actor notes focused on the entity, not on retelling shared events.

The event note is the canonical location for the timeline, the market reaction, and the cross-cutting analysis. Each actor note references it with a one-line summary and a wikilink. If you find yourself writing the same paragraph in three actor notes, you need an event note.

---

## Ratings History (Public Companies)

Public company actor notes (non-stubs) should include a `## Ratings history` section with a table of S&P, Moody's, and Fitch actions: Date, Agency, Action (upgrade/downgrade/affirm/outlook revision), Rating, Outlook. Place it immediately after `## Financials` — ratings are a financial attribute, not operational detail. If the note has no Financials section yet, place it before `## Related`.

Reference: See [[Micron]] for the template.

---

## Concept Note Structure: Story + Reference

Concept notes (non-stub) must follow a story + reference structure.

1. One-liner — frontmatter + single paragraph: what it is, why it matters, current state.
2. Plain-English preamble when needed — if the concept is taxonomy-heavy, abstract, or easy to misread, open with 1-3 spoken-English sentences that decode the note before the denser synthesis begins. Think: "what this means in normal language," not a second abstract summary.
3. The story — full narrative arc as connected analytical prose. Trace the causal chain: physics/fundamentals → economics → ecosystem/players → implications. No headers within the story — continuous exposition. Hard numbers inline with sources. Self-contained.
4. Reference — tables, specs, quick stats, company lists, timeline data, key quotes.
5. Related — wikilinks to connected notes.

Length: Scale to complexity. Narrow concept: 5-8 paragraphs. Broad technology transition: 15-20.

Reference: See [[Co-Packaged Optics]] for the template.

When to use: Any concept where the reader benefits from understanding the causal chain. Not every concept needs a long story — narrow technical definitions are fine as structured reference.

---

## Actor / Securities Split

Actors with tradeable instruments get a two-note structure.

The actor note covers the entity itself — Synopsis, Evolution, business economics, financials, competitive dynamics, capex, strategy, management. Everything about what the entity IS and DOES. Earnings numbers go here; stock reactions go in securities.

The securities note covers all tradeable instruments and their price dynamics:
1. Instruments — what exists (stock, bonds, ETFs, options, derivatives, cross-listings)
2. Price history — absolute price chain (chronological: event, price, effect)
3. Relative value — beta-adjusted ratios against sector/peers
4. Sector correlation — correlation table with relevant ETFs
5. Earnings reactions — stock moves on results
6. Analyst coverage — PTs, ratings, upgrades/downgrades
7. Market expectations — what's priced in, what isn't
8. Charts — all price/comparison charts

Boundary: "Is this about the entity or about the market's pricing of the entity?"

Naming: `[Actor name] securities` (lowercase). Examples: `Micron securities`, `Brazil securities`.

Folder: Securities notes live in `investing/Assets/`.

Linking: Actor links to securities in Related under `### Securities`. Securities links back to actor as first Related entry. Same event can appear in both.

Applies to: Any actor with tradeable instruments (companies, countries, institutions).

Does NOT apply to: Actors without tradeable instruments. Stubs don't need a securities note.

Reference: See [[Micron]] and [[Micron securities]] as template.

---

## People: investing-vault actor vs cross-vault link

Not every person mentioned gets an investing-vault Actors/ note. The test: **is this person's durable content a market-lever action**, or is it biographical/political/domain content that belongs in a sibling vault?

**Investing-vault Actors/ notes are for people whose market-lever actions ARE the content:**
- Central bank chairs and committee members (Powell, Galípolo, Lagarde)
- Treasury / Finance ministers with active policy on markets (Bessent, Haddad)
- Sitting heads of state with direct policy impact on tracked assets (Lula, Trump, Xi)
- CEOs of tracked companies (Huang, Zuckerberg, Musk)
- Fund managers and allocators whose calls are the record (Gerstner, Ackman, Dalio, Druckenmiller)
- Analysts whose published work is repeatedly cited (McNally at Rapidan, Toland at Citi)

**Cross-vault link — not an investing-vault actor:**
- Political figures without direct market-lever roles (opposition candidates, legislators, local officials)
- Historical figures whose content is biographical
- Domain specialists (scholars, journalists, technologists) whose expertise sits in a sibling vault
- Family members, donors, advisors named incidentally

For these, use a markdown cross-vault link in-body: `[Flávio Bolsonaro](obsidian://open?vault=Brazil%20News%20%26%20Analysis&file=People%2FFl%C3%A1vio%20Bolsonaro)`. Do not create an investing-vault stub that duplicates the sibling vault's biography.

**The failure mode this prevents:** a Brazilian presidential election produces five candidates. Each has a full political biography in the Brazil vault. Creating five investing-vault stubs for them is bloat: the stubs duplicate content, provide no investing-specific signal the event note doesn't already carry, and fragment the canonical biographical source across two vaults.

**Escape hatch:** if a specific investing-lens angle on a person outgrows its home in an event note (e.g., a candidate's announced privatization list becomes a running tracker with price exposures), create a focused investing note titled for the *angle*, not the person — e.g., `Flávio Bolsonaro privatization agenda` in Concepts/, not a full actor note.

**Retroactive rule:** if an existing investing-vault person note is 80%+ biography duplicating a sibling vault, delete it and rewire backlinks to cross-vault markdown links.

Example from 2026-04-16: the 2026 Brazil presidential election ingestion initially created five candidate stubs (Flávio/Jair Bolsonaro, Caiado, Zema, Renan Santos). All were deleted the same day — their content lived in the [[2026 Brazil presidential election]] event note, and their biographical content lived in the Brazil vault. [[Lula]] stayed because he is the sitting president = direct market-lever actor.

---

## Economics / Prices Split (Concepts Only)

For non-actor concepts with tradeable prices (commodities, rates, currencies) — things without an "actor."

The Economics note covers how the thing works — supply, demand, structure, players, mechanics. Story + reference structure.

The Prices note covers:
1. Absolute price — the number and what put it there (chronological chain)
2. Relative price — against correlated markets and peers, always risk/beta-adjusted

Relative prices must be risk-adjusted — outperforming a benchmark by 20% means nothing if beta is 2x.

Naming: `Uranium Economics` / `Uranium Prices`.

Folder: Both in `Concepts/`.

Does NOT apply to: Purely analytical concepts, structural concepts, or actors (use Actor/Securities split).

---

## Updating Existing Notes

The vault is not a collection of facts — it weaves facts into explanations and cross-references. When new data arrives, the goal is to make the existing note's argument stronger, not longer.

**Do not append dated fact blocks.** A section called "### Apr 2026 update" sitting below the existing analysis turns the note into a timeline. The reader now has to mentally merge two sections to understand the current state. Instead:

1. Update existing sections in place — revise numbers, strengthen or challenge the argument, add new evidence inline where it belongs thematically
2. Connect new facts to the note's existing analytical threads — if the note argues that compute is the binding constraint, new compute data goes into that argument, not into a separate chronological appendix
3. Cross-reference outward — what does this new data change in related notes? Update those too
4. If the new data changes the thesis or conclusion, update the synthesis/synopsis — don't leave the old interpretation standing next to contradicting facts

**When dated sections are appropriate:** Evolution sections are chronological by design. Event notes track timelines. Daily notes are dated. But analytical sections (Synopsis, Synthesis, competitive positioning, cost structure) should read as the current state of the argument, not as a log of when each fact was learned.

**The test:** A reader opening the note for the first time should get a coherent analytical picture without needing to mentally reconcile "what the note said in March" with "what was appended in April."

---

## Product Note Gate

When a major product launch catalyzes an actor update (new chip, platform, vehicle — anything with its own specs, customers, roadmap, competitive landscape), create the product note in the same pass. Don't wait to be asked.

- Actor note keeps strategic framing (Synopsis, business model, competitive analysis, Evolution)
- Product note carries hardware/spec detail (specifications, competitive comparison table, customer list with use cases, economics, roadmap, market discovery timeline)
- Actor links to product with a summary paragraph

See [[Arm AGI CPU]] as reference template.

### The story (required for non-stub product notes)

Every product note (non-stub) must include a narrative intro section (`## The story`) immediately after the one-liner and before Quick stats. This traces the arc: what problem exists → what the product does about it → the business logic → competitive/industry reaction → why it matters for the thesis. Connected analytical prose, not bullet points. Hard numbers inline. Self-contained — a reader who stops after this section still understands why the product matters.

The story section follows the same philosophy as concept note stories and actor synopses: lead with narrative, follow with structured reference. The rest of the note (Quick stats, specs, competitive tables, market discovery timeline) provides the detail that backs the story.

Reference: See [[EmDash]] for the template.

### Market discovery timeline (required for product notes)

Every product note must include a "Market discovery timeline" — a chronological table tracking how information became public and how the market priced each disclosure: rumors/leaks, announcements, spec reveals, customer confirmations, revenue/guidance, and stock price reactions. The analytical value is in the gaps: what the market knew vs. what surprised it.
