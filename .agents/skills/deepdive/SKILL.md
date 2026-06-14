---
name: deepdive
description: "Deep-dive entity research and note creation pipeline. Use for any entity the user wants a comprehensive vault note on — companies, people, concepts, countries, products. Triggers on /deepdive ENTITY or when the user names an entity and wants thorough research + vault note creation/expansion. The skill adds SEC filing protocols, full chart sets, stale-reference scanning, and entity-type branching that CLAUDE.md's general vault instructions don't sequence."
---

# Deep-Dive Entity Research

Create or expand a comprehensive vault note. Usage: `/deepdive ENTITY NAME`

CLAUDE.md already defines note structure (Synopsis, Evolution, Core thesis, etc.), formatting rules, and vault conventions. This skill does NOT repeat those — it adds the research protocols, data integration steps, and quality gates that CLAUDE.md doesn't sequence.

## Phase 1: Vault Reconnaissance

Most entities already have some vault presence. The default path is expansion, not creation.

1. **Hard gate** — check for existing notes and aliases:
   ```bash
   python scripts/check_before_create.py "ENTITY NAME"
   ```

2. **Vault search** — find all mentions across the investing vault:
   ```bash
   bash scripts/vault_search.sh investing "ENTITY NAME"
   ```
   Also search by ticker, product names, key people — anything that might surface references the entity name misses.

3. **Geopolitics vault search** — if the entity touches defense, trade, sanctions, diplomacy, energy security, or industrial policy:
   ```bash
   bash scripts/vault_search.sh geopolitics "ENTITY NAME"
   ```
   Note specific counterpart notes for cross-vault linking later.

4. **Branch on what you find:**
   - **Full note exists** → read it, assess gaps against the gold standard (see `investing/Actors/Block.md` for actor notes), then expand. Tell the user what's there and what's missing.
   - **Stub exists** → read it, proceed to Phase 2 to expand.
   - **Nothing exists** → proceed to Phase 2 to create from scratch.

## Phase 2: Research (entity-type-aware)

### All entity types:
- Multiple web searches to triangulate: identity, recent developments, hard numbers
- Search the vault for related concepts, sectors, and themes — not just the entity itself but adjacent ideas
- Gather and attribute hard numbers. No "significant" or "substantial."
- For infrastructure, energy, data-center, utility, logistics, mining, semiconductor, or capital-stack entities, run the physical-bottleneck sweep from `docs/note-checklist.md`: if MW/GW, power, sites, interconnections, PPAs, permits, construction, transformers, cooling, "energy and digital infrastructure," "long-term capacity," or "supply assurance" appear, identify what constraint the entity solves. Separate capital from deliverability, link the relevant constraint hubs, and state explicitly when no power plant/PPA/interconnection/grid region/site has been disclosed.

### Public companies — additional steps:
- **SEC filings** — always pull the latest 10-K and most recent 10-Q:
  ```bash
  python scripts/parse_sec_filing.py TICKER --type 10-K --save /tmp/TICKER-10k.txt
  python scripts/parse_sec_filing.py TICKER --type 10-Q --save /tmp/TICKER-10q.txt
  ```
  These are primary sources. Extract revenue segments, risk factors, insider transactions, guidance language.

- **Database setup** — check if ticker exists, add if missing, ensure fundamentals are loaded:
  ```bash
  python scripts/add_ticker.py TICKER
  python fetch_fundamentals.py TICKER
  ```

- **Price freshness** — update before generating charts:
  ```bash
  python update_market_data.py --lookback 10 --assets all
  ```

- **Price verification** — before writing any stock price into the note, verify against actual DB closing prices. Never trust secondary sources for price data.

### Private companies — additional steps:
- Search for funding rounds, valuations, investor names
- No SEC filings, no ticker to add, no price chart
- The funding rounds table and cap table estimates replace financial data sections

### Individual content producers (journalists, analysts, researchers, podcasters) — additional steps:
- **Enumerate platforms, don't confirm a single role.** Run an explicit enumerative pass: newsletter/Substack + podcast + books (published + forthcoming) + personal site + Wikipedia + adjacent affiliations (think tank + foundation + visiting positions). See `docs/note-checklist.md` "Individual creator completeness" section for the full search-query template + the three retroactive-audit refinements
- Stopping condition: five questions answered (where they publish, where they host, what they've written, institutional affiliations, collaboration network) — *not* "the immediate question is answered." Confirmatory searches return confirmatory answers; the completeness pass needs an enumerative shape
- **Books are the highest-priority gap category** — elevate the books question in the enumerative-search order; verify any claimed book title against a search result before shipping (the "definitive book on RLHF" pattern caught in the May 19 audit was a fabrication that the verification step prevents)
- **Negative answers count as completeness data** when stated explicitly. "She doesn't have a Substack" or "He doesn't host his own podcast" is a finding, not a gap — but only if the note states the absence. A silent gap is an unanswered question
- **Capture non-obvious biographical dimensions** in the synopsis when they define the actor. Michael Pettis's Maybe Mars / D-22 / Beijing indie-music-scene founder role is the canonical case — doesn't fit the five-question template cleanly but changes how readers interpret him
- Failure patterns this prevents:
  - May 19 2026 Michael Weiss note — first pass missed his Foreign Office Substack, weekly podcast, Free Russia Foundation affiliation, and forthcoming GRU history book; surfaced only on a second search after the user pointed it out
  - May 18 2026 Nathan Lambert stub — claimed an unverified "definitive book on RLHF" that the May 19 retroactive audit corrected. Same fabrication pattern as the *Menace of Unreality* misattribution and Yaoji Holdings → Alibaba Health correction

### Concepts — structural differences:
- Route to `investing/Concepts/`, not `Actors/`
- Use Synthesis (not Synopsis) — interpretive framing of where the concept stands now
- No Evolution section — organize by analytical dimension (pathways, economics, regulatory, demand)
- No ticker, no Quick stats with financial metrics — use concept-relevant metrics (production volumes, cost curves, mandate timelines)
- The note's value is connecting actors to a theme — wikilink every relevant company, regulator, and policy

### Parallel research fan-out (hard or multi-dimension entities)

For any entity that needs coverage across several independent dimensions — private companies, individual content producers, or any subject where one sequential thread risks answering the immediate question and stopping — fan the research out across concurrent sub-agents (the Agent tool) rather than running a single thread. This is width over depth: many retrieval paths at once, the local equivalent of issuing many search/fetch calls in one step. It raises coverage and cuts wall-clock, and it structurally prevents the single-thread completeness misses documented above (the missed-platforms and fabricated-book failures in Individual content producers). Reserve it for hard or multi-dimension entities — a thin stub-to-stub expansion does not need a fan-out.

- **Dispatch one sub-agent per dimension.** Give each: the entity, what the vault note already contains, its single assigned dimension, the primary/target sources to prefer, and an output contract — return findings as `claim — value — source URL`, plus an explicit `NOT FOUND` for anything in its dimension it could not confirm. Use `Explore` for search-heavy dimensions, `general-purpose` for multi-step ones.
- **Dimensions are entity-type-specific** (reuse the dimension sets from the entity-type steps above):
  - Public company: recent developments/catalysts; competitive set + market share; analyst coverage + price targets; regulatory/legal exposure. SEC segments and DB prices stay on the main thread — they are scripted, not searched.
  - Private company: funding history (rounds, dates, amounts, valuations, leads); investor roster + board; named customers/partnerships; product/tech + competitive set.
  - Individual creator: newsletter/Substack; podcast(s); books (published + forthcoming); personal site + Wikipedia/Wikidata; institutional affiliations; collaboration network — one dimension per agent.
- **Consolidate** every return into the completeness ledger below, keeping the source URL attached to each fact and reconciling conflicts across agents. Sub-agent output is raw input, not final copy — apply every vault rule (wikilinks, no bold in note bodies, sourcing) before it enters the note.
- **Caveat:** sub-agents start cold and hit the same fetch/403 wall — give each enough context to work, and on a 403 they fall back to Chrome per CLAUDE.md. Fan-out buys coverage and speed, not a 403 bypass.

### Completeness ledger (research done-criterion)

Before leaving Phase 2, emit a completeness ledger — a table with one row per required dimension for the entity type and three columns: Dimension | Status (`answered` / `not found (stated)` / `n/a`) | Source. Research is not done until the ledger is filled.

- **No row may be blank.** `not found (stated)` is a valid, required status — a silent gap is an unanswered question; a stated absence ("no self-hosted podcast") is a finding the note records. This is the operational form of "negative answers count as completeness data."
- **Every world-fact claim headed for the Synopsis/Synthesis carries a source.** Book titles, awards, funding figures, role and affiliation claims each need a source URL in the ledger. A claim with no source does not enter the note. This is the anti-fabrication gate — exactly the check that catches an invented book title (the "definitive book on RLHF" pattern) before it ships.
- **Dimension rows mirror the fan-out dimensions** for the entity type above. A `NOT FOUND` returned by a sub-agent becomes `not found (stated)`, and the note states the absence.
- The ledger is a pre-write checkpoint, not a permanent note section. Log "completeness ledger filled" in the daily-note edit log.

## Phase 3: Write the Note

CLAUDE.md defines note structure, formatting, and quality standards in detail. Follow those. Key reminders the skill adds:

- **If expanding an existing note**: use Edit operations to add/update sections. Preserve all existing content. Never overwrite — augment.
- **If the note is mature enough** (3+ substantive sections, 100+ lines): add an Analysis section. This is interpretation derived strictly from facts in the note — structural tensions, open questions, what the data reveals that isn't obvious. See CLAUDE.md's vault philosophy: "The vault earns its value by being more thorough than what's freely available."
- **Actor notes (required structural slots) — see `docs/vault-note-guide.md` → "One-line read + What to watch":**
  - **One-line read** — single sentence at the top capturing the active position. Form: `[Actor] is [structural position] because [primary driver], with the bet being [trade/outcome being tracked].`
  - **What to watch** — labeled dial-set, 3–6 signals, each `**Signal name** — what it is, what reading changes the position (which way).`
  - Both slots are required for actors. They are structural slots, not bull/bear scaffolding — the rest of the note still presents dynamics, not binary editorial frames (`vault-note-guide.md` → "Vault is factual/conceptual, not thesis/trade"). For concept and event notes that anchor an active investment case, include a watch-list; the one-line read is actor-specific.
- **Quotes**: extract and date every relevant quote from sources. Format: `[[Firm]] analyst Name (Feb 13): *"quote text"*`
- **Narrative-read-back gate (done criterion for actor notes):** before declaring the deepdive done, write the one-paragraph narrative read of the entity *using only the note*. If anything in that narrative is sharper in chat than in the file, the file is the bug — port it back. Self-check; do not wait to be asked "is all that in the notes?" Synthesis emerging in conversation that could have been lifted from the note = the note is missing a slot.
- **Completeness-ledger gate (research done-criterion):** the Phase 2 completeness ledger (see Phase 2 → **Completeness ledger**) must be filled before writing — every required dimension marked `answered` / `not found (stated)` / `n/a`, and every world-fact claim (book titles, awards, funding figures, affiliations) carrying a source. A claim with no source does not enter the note.

## Phase 4: Charts (public companies only)

Generate the full chart set — not just a price chart. Each chart reveals something different.

1. **Peer comparison price chart** (required) — always compare to 2-3 peers, never solo:
   ```
   /api/chart/lw?tickers=TICKER,PEER1,PEER2&start=...&normalize=true&primary=TICKER
   ```
   Save as `ticker-vs-peer1-price-chart.png`. Choose peers that illuminate the investment question.

2. **Fundamentals chart** (required if fundamentals are in DB):
   ```
   /api/chart/lw?tickers=TICKER&metrics=revenue,netincome&start=...
   ```

3. **Sankey diagram** (required if income statement data exists in DB):
   ```
   /api/chart/sankey?ticker=TICKER
   ```
   Save as `ticker-sankey.png`. Caption format: fiscal year, revenue → net income, net margin, major cost buckets as % of revenue.

4. **Waterfall chart** (if income statement data exists):
   ```
   /api/chart/waterfall?ticker=TICKER
   ```
   Save as `ticker-waterfall.png`

Verify every chart with `wc -c` — files under 1KB are errors, not PNGs. Embed each in the note with an italic interpretation caption and a corresponding data table.

Skip charts entirely for private companies and concepts. For concepts, harvest source charts (IEA forecasts, industry reports) if found during research.

## Phase 5: Stubs and Vault Maintenance

1. **Compliance check**:
   ```bash
   python scripts/check_note_compliance.py investing/TYPE/ENTITY.md
   ```

2. **Create stubs** for every dead-linked entity. Run `check_before_create.py` for each before creating — don't create stubs for entities that already have notes. Parallelize with sub-agents.

3. **Stale reference scan** — search the vault for other notes that mention this entity:
   ```bash
   bash scripts/vault_search.sh investing "ENTITY NAME"
   ```
   Check if any of those notes contain stale data (old valuations, outdated revenue figures, wrong status). If you find stale references, update them. This is vault maintenance — data consistency across the entire vault matters.

## Phase 6: Daily Note

1. Confirm today's date: `date +%Y-%m-%d`
2. Update today's daily note (`investing/Daily/YYYY-MM-DD.md`):
   - `## Notes created/expanded`: every note created or expanded, with brief description
   - `## Edit log`: every file touched
3. Create the daily note with `#daily` tag if it doesn't exist

## Phase 7: Final Compliance and Cross-Vault

1. Re-run compliance on the main note. Fix any remaining errors.
2. **Cross-vault gate**: Does this entity warrant a geopolitics vault counterpart? Defense, sanctions, trade policy, diplomatic precedent, infrastructure competition → flag to user. Don't skip silently.
3. **Concept extraction**: Scan for terms that deserve their own concept note. If a reader would benefit from a dedicated note on a term used in this note, create and wikilink it.
