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

## Ratings History (Public Companies)

Public company actor notes (non-stubs) should include a `## Ratings history` section with a table of S&P, Moody's, and Fitch actions: Date, Agency, Action (upgrade/downgrade/affirm/outlook revision), Rating, Outlook. Place it immediately after `## Financials` — ratings are a financial attribute, not operational detail. If the note has no Financials section yet, place it before `## Related`.

Reference: See [[Micron]] for the template.

---

## Concept Note Structure: Story + Reference

Concept notes (non-stub) must follow a story + reference structure.

1. One-liner — frontmatter + single paragraph: what it is, why it matters, current state.
2. The story — full narrative arc as connected analytical prose. Trace the causal chain: physics/fundamentals → economics → ecosystem/players → implications. No headers within the story — continuous exposition. Hard numbers inline with sources. Self-contained.
3. Reference — tables, specs, quick stats, company lists, timeline data, key quotes.
4. Related — wikilinks to connected notes.

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
