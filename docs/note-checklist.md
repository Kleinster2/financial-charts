# Note Completion Checklist

Run before marking any vault note "done" (actors, concepts, events, theses, sectors).

## 1. Run automated check FIRST

```bash
python scripts/check_note_compliance.py investing/Actors/NewNote.md
```

Fix all errors before proceeding to manual checks.

**Automated checks:**
- Frontmatter (exists, has aliases)
- Dead links (wikilinks to non-existent notes)
- Missing price/fundamentals/Sankey charts
- Missing chart captions
- Missing Related section
- Missing Quick stats section
- Missing Leadership section with CEO
- Missing historical financials (10-year for public)
- Missing cap table (private)
- Funding rounds table — exists, complete (no gaps/catch-all rows), individual rounds listed
- Missing ownership % estimates table (private)
- Missing credit rating in Financial position or Quick stats table (public companies)
- Missing `## Market Reaction` on public-company M&A event notes
- Table formatting (blank lines before tables)

**Exit codes:** 0 = pass, 1 = errors

---

## 2. Manual checks

These cannot be automated. Review each one.

### Currency

- [ ] **Web search for recent news** — verify note reflects current reality
- [ ] Key facts are current (not stale by weeks/months)
- [ ] Numbers are latest available (MAU, revenue, valuations, ownership stakes)

### Completeness

- [ ] **No info left outside note** — all research findings go in the note, not just conversation
- [ ] Board table exists (companies) — Chair, independent vs insider, notable affiliations
- [ ] Principals table exists (funds) — PE/VC: founding partners; sovereign funds: CEO, CIO; hedge funds: founder, PM

### Specificity

- [ ] **No lazy shorthand** — "American-owned" needs: who owns what %, board composition, economic rights vs equity
- [ ] Ownership changes include: exact stakes, governance, economic rights, compliance concerns
- [ ] Revenue/valuation claims have exact figures, not "significant" or "major"
- [ ] Partnerships/deals specify: terms, duration, exclusivity, economics

### Analysis

- [ ] **Mature notes have an Analysis section** — interpretation derived strictly from facts already in the note
- [ ] Analysis does not import framing from sources — every claim traces to a fact in the note
- [ ] Stubs and thin notes skip this (not enough surface area to interpret)
- [ ] Tensions, contradictions, and structural patterns in the facts are surfaced
- [ ] Open questions are explicit, not papered over with a tidy narrative

### Public-company M&A market reaction

For any merger, acquisition, take-private, spin-merger, or strategic combination involving a listed company, the event note is incomplete until it separates strategic logic from market verdict. Add a `## Market Reaction` section even when the deal rationale already feels obvious.

- [ ] Acquirer stock reaction is captured (same-day and next-day when available)
- [ ] Target stock reaction is captured
- [ ] Deal premium, exchange-ratio value, or cash/stock mix implication is stated
- [ ] Current implied consideration is calculated from live deal terms (cash, stock ratio, collars, contingent payments)
- [ ] Gross spread and annualized spread are calculated when the target still trades
- [ ] Break value / standalone downside assumption is stated when defensible
- [ ] Crude implied close/fail odds are calculated for merger-arb setups where a break value can be estimated; if not defensible, say why
- [ ] External estimates or proxies are checked (analyst targets, arb-spread commentary, options/prediction-market odds); if none exist, state that the probability is internal math
- [ ] One sentence answers: "what did the tape believe?"
- [ ] Source is cited and price moves are verified against local closes when writing precise price-performance claims
- [ ] Securities notes for the public acquirer/target have short `## Market reaction` mirrors that link back to the event note

Failure mode this prevents: the note captures the strategic thesis ("why the deal matters") but misses the market's first judgment ("who got paid, who got discounted, and what risk the tape is pricing"). This happened in the first-pass [[NextEra-Dominion merger 2026]] note on May 19, 2026: the event note had the AI-power consolidation thesis, but not Dominion's target-premium rally versus NextEra's acquirer selloff, and the first market-reaction fix still missed the standard merger-arb implied-odds calculation.

### Listed-company event / peer reaction

For any non-M&A event involving listed companies or listed peer sets — joint venture, strategic partnership, product launch, financing, customer win/loss, regulatory decision, or competitive announcement — the event note is incomplete until it distinguishes broad tape from event-specific read-through.

- [ ] Primary listed actors' same-day stock reactions are captured
- [ ] Next-day reactions are captured when available
- [ ] Obvious second-order peers / competitors are checked, including listed peers already named elsewhere in the note/entity list/read-through, not just named companies in the headline
- [ ] Relevant benchmark or sector ETF moves are included (`[[SPY]]`, `[[QQQ]]`, sector ETF, peer basket)
- [ ] One sentence separates broad-market/sector tape from the event-specific read-through
- [ ] If local data is stale or missing, use an external historical-price source rather than leaving a placeholder
- [ ] `## Market Reaction` contains no unresolved `TODO`, `TBD`, or "verify later" text
- [ ] If same-day close is not yet available, state the status explicitly and log a daily-note follow-up to fill it after the close

Failure mode this prevents: the first-pass [[Google-Blackstone TPU cloud venture 2026]] note correctly identified [[CoreWeave]] as the exposed peer but left `CRWV | TODO verify`; the first repair then chased CRWV without systematically checking other listed peers already named in the note, especially [[Nebius]] / NBIS. The fix was to check CRWV, NBIS, and the broader AI-capacity basket against [[SPY]], [[QQQ]], and [[SMH]], showing the JV did not broadly reprice AI infrastructure but did hit listed neocloud peers.

### Charts

- [ ] **All provided/source charts ingested** — every user-provided chart, screenshot, table-like graphic, or article visualization has a durable note artifact
- [ ] Rights path chosen — image saved/embedded with attribution when allowed; otherwise chart axes/series/dates/values/takeaway extracted into note text or tables with source attribution
- [ ] Daily note records chart disposition (`saved/embedded`, `extracted/not copied`, or follow-up reason)
- [ ] Price chart has actor + peers/benchmark (not just actor alone)
- [ ] Fundamentals chart exists (public companies)
- [ ] Income statement Sankey exists (public companies with income data in DB)
- [ ] **Open and verify chart images** — confirm legend matches caption
- [ ] **No chart titles** — legend suffices
- [ ] **Research major moves** — don't fabricate explanations; web search actual causes
- [ ] Link captions to vault notes

### Links

- [ ] Every entity in tables is `[[wikilinked]]`
- [ ] Every entity in body text is `[[wikilinked]]`
- [ ] Related section includes all linked entities

### Hub linking (reverse direction)

After creating or editing any note, check whether parent/hub notes need a backlink or update. This applies to all vault work — not just new notes. Adding a section to an existing actor note can introduce relationships that a sector or concept hub should reflect.

- [ ] **Identify hub notes** — scan the note's Related section for broad parent notes (sector notes like [[Shipping]], concept hubs like [[Oil]]/[[LNG]], parent actors, event hubs)
- [ ] **Read each hub's Related section** — if the note isn't listed (or a new relationship isn't reflected), add it with a one-line description
- [ ] **Check for bare-text mentions** — grep the hub for unlinked mentions of entities introduced by the edit and wikilink them

Examples:
- New concept note → sector note, parent concept hub
- New section in an actor note → sector note if it introduces a new sector relationship
- New event note → actor notes for all involved parties, concept hubs for affected domains
- Expanded Related in any note → check that the reverse link exists in the target

Quick hub audit:
```bash
# Find notes that mention the new entity but don't wikilink it
grep -rl "VLCC" investing/ | grep -v "VLCC.md"
```

---

### Scope expansion / framework-cluster sweep

Reverse-link checks catch missing backlinks, but they do not catch the deeper failure mode where a fact changes a framework and only the direct entity notes get updated. Run this sweep whenever an edit changes a taxonomy, capital stack, risk map, peer set, market structure, or named playbook.

- [ ] **Classify the update** — is this only an entity fact, or does it change a broader framework? Phrases like "structural twin," "new category," "capital-stack split," "risk taxonomy," "playbook," "distribution model," or "peer set" trigger the sweep.
- [ ] **Search sibling framework notes** — grep the important entities plus the mechanism, not just the event name. Search `Concepts/`, `Theses/`, and `Sectors/` before stopping at actor/event notes.
- [ ] **Read the likely hubs before finalizing** — at minimum: direct note, parent concept hub, risk/financing/deals ledger if one exists, and any active thesis note that depends on the framework.
- [ ] **Update or explicitly defer** — either patch stale hub notes, add cross-links to the canonical note, or write a one-line daily-note explanation for why no hub update was needed.

### Physical-bottleneck / constraint-cluster sweep

For infrastructure, energy, logistics, data-center, mining, semiconductor, or utility-linked updates, the framework sweep must ask: *what physical bottleneck does this capital or contract solve?* Do this before finalizing any note that mentions MW/GW, data-center capacity, power, grid, interconnection, [[Power purchase agreement|PPA]], site selection, land, permits, construction, transformers, cooling, "energy and digital infrastructure," "long-term capacity," or "supply assurance."

- [ ] **Separate money from deliverability** — state who provides equity/debt, who provides technology/offtake, and who converts the money into physical capacity.
- [ ] **Check already identifiable constraint clusters** — power availability, grid/interconnection, site control, permitting, equipment lead times, cooling, and data-center operator platforms. Use existing hubs such as [[Power constraints]], [[Power purchase agreement]], [[Power grid primer]], [[Power-constrained geography]], [[AI infrastructure financing]], [[AI infrastructure deals]], and [[AI infrastructure financing risk]] where relevant.
- [ ] **Avoid overclaiming assets** — distinguish "brings powered-capacity delivery capability" from "brings a named power plant/PPA/interconnection/site." If the source does not disclose a power asset, grid region, interconnection, PPA, or site, say so explicitly.
- [ ] **Update the constraint home** — if the event materially changes a power/site/interconnection/cooling/transformer frame, update or link the canonical constraint note, not just the deal or actor note.

Failure mode this prevents: the first Google-Blackstone TPU JV pass captured [[Blackstone]]'s $5B equity and the 500 MW target, but treated the deal mostly as a capital-provider map. The missing synthesis was that Blackstone's edge is powered-capacity delivery — site, grid/interconnection, construction, operations, and energy procurement — while no specific power plant, [[Power purchase agreement|PPA]], utility interconnection, grid region, or facility site had been disclosed.

### Correlation-cluster scoping

If the framework sweep involves public tickers, scope the edit against already identifiable market-behavior clusters. Do not use a fresh event to speculate that a new durable cluster exists; re-clustering is confirmed ex post after enough return history. The near-term job is to check whether existing cluster notes, sector-correlation sections, or cluster configs already cover the relevant names.

- [ ] **List the affected public tickers** — primary names, obvious listed peers already named in the note, adjacent-sector controls, and broad ETFs.
- [ ] **Search existing cluster evidence** — check `scripts/cluster_configs/`, cluster concept notes, actor `## Sector correlation` sections, and `docs/cluster-validation.md` examples. Prefer existing validated/falsified clusters over proposing a new cohort.
- [ ] **Map to existing clusters, or mark "no established cluster"** — if the affected names already belong to an identifiable cluster, update/link that canonical cluster note. If they do not, do not invent a cluster; note that the event is only a candidate future re-clustering signal.
- [ ] **Run validation only when there is enough history** — run `python scripts/cluster_analysis.py --primary TICKER` or config-based validation when an existing cluster needs refresh or a proposed cohort has enough ex-post return data. For event-level changes, explicitly log why validation is deferred.
- [ ] **Keep the canonical home clean** — event notes can cite the one-day tape, but the durable correlation diagnostic belongs in the actor note's `## Cluster validation` section or the cohort concept note, not duplicated across every event note.
- [ ] **Separate tape from cluster** — same-day peer reaction is evidence of event sensitivity, not proof of a durable correlation cluster. Durable cluster claims require windowed return correlations, dendrogram boundary, and PC1 diagnostics over a relevant history window.

Quick framework audit:

```bash
rg -n "(ENTITY_A|ENTITY_B|mechanism phrase|capital stack|risk taxonomy)" investing/Concepts investing/Theses investing/Sectors
```

Quick cluster audit:

```bash
rg -n "(TICKER_A|TICKER_B|existing cluster name|cluster validation|Sector correlation)" scripts/cluster_configs investing/Actors investing/Concepts investing/Sectors
```

Failure mode this prevents: the first-pass [[Google-Blackstone TPU cloud venture 2026]] / CRWV / NBIS capital-provider update correctly touched the event note, [[CoreWeave]], and [[Neocloud financing]], but initially missed broader framework notes like [[AI infrastructure financing]], [[AI infrastructure deals]], and [[AI infrastructure financing risk]]. The fix was not more entity search; it was recognizing that "who provides the capital" changed the AI-infrastructure financing framework.

---

Quick link audit:
```bash
grep -oE '\b[A-Z][a-z]+\b' note.md | sort -u
```
Compare against wikilinks. If proper noun appears without `[[brackets]]`, fix it.

---

## Vault-wide Orphan Detection

Find terms mentioned frequently without notes:

```bash
python scripts/check_note_compliance.py --orphans --min-mentions 50
```

Scans vault for capitalized terms appearing 50+ times without corresponding notes. Run periodically.

---

## Domain Completeness Check

**Don't just search what exists — ask what MUST exist.**

For any domain query, enumerate canonical entities:

| Domain | Must-have notes |
|--------|-----------------|
| Crypto | Bitcoin, Ethereum, token economics, unlock schedules |
| Semiconductors | Foundry, fabless, memory, logic |
| AI infrastructure | Training, inference, GPUs |
| Banking | Deposits, lending, capital ratios |

**When exploring a domain:**
1. Search what exists
2. Enumerate what must exist
3. Check the gap
4. Flag missing

Don't confuse infrastructure with foundations. Coinbase is crypto infrastructure; Bitcoin is a crypto foundation.

## Individual creator completeness (journalists, analysts, researchers, podcasters)

**Use an enumerative search query, not a confirmatory one.**

Failure mode this prevents: question-shaped searches return question-shaped answers. If you query `"<name>" <publication>` to confirm an affiliation, the search delivers that affiliation and stops — you miss everything else. The first-pass Michael Weiss note (May 19, 2026) shipped without his Substack, podcast, Free Russia Foundation affiliation, or forthcoming book because the search was built to confirm the Insider connection, not to enumerate his platforms.

When creating an actor stub for an individual content producer, run an explicit enumerative pass before considering the note complete:

| Platform | What to search |
|----------|----------------|
| Newsletter / Substack | `"<name>" substack` — many journalists run a personal Substack distinct from their employer outlets |
| Podcast | `"<name>" podcast site:apple.com/podcasts OR site:open.spotify.com` |
| Books | `"<name>" books` — published + forthcoming; pulls bibliography pages from Wikipedia / personal site |
| Personal site | `"<name>" "personal website" OR "<firstname><lastname>.com"` — often the most complete affiliations list |
| Wikipedia | `"<name> (journalist)" OR "<name> (analyst)" wikipedia` — the page usually enumerates outlets cleanly |
| Adjacent affiliations | `"<name>" "senior fellow" OR "visiting scholar" OR "contributing editor"` — surfaces second-tier positions the main biography skips |

**Stopping condition:** the note is complete when you can answer all five questions:
1. Where does this person publish their own work? (newsletter / Substack / personal blog)
2. Where do they appear as a host or recurring voice? (podcast, video series)
3. What books have they written or contributed to? (published + forthcoming) — **highest-priority gap category** (see #Refinements from retroactive audit below)
4. What institutional affiliations do they hold? (employer + think-tank + foundation + visiting positions)
5. What is the primary collaboration network? (co-authors, co-hosts, regular outlets)

**Stopping condition is NOT "question I was just asked is answered."** That's the failure mode. Confirmation searches end when the immediate question is satisfied; completeness passes end when the five questions all have answers (or explicit "no evidence found").

### Refinements from retroactive audit (May 19, 2026)

A 13-note retroactive audit of existing journalist/analyst notes (~77% gap-hit-rate; 10 corrected, 2 already exemplary, 1 already complete) surfaced three refinements to the rule:

1. **Negative answers count as completeness data.** "She doesn't have a Substack" or "He doesn't host his own podcast" is a useful finding *when stated explicitly* — it prevents future re-audits from re-asking the same question. The stopping condition is "all five questions answered (or explicitly 'no evidence found')" — a negative answer counts as an answer, but only if the note explicitly states the absence. A silent gap is not a negative answer; it's an unanswered question.

2. **Books are the highest-priority gap category.** Across the 13-note audit, missing books were the most-common and most-impactful gap (Chris Miller had 3 missing prior books; Foroohar's *Homecoming* was missing; Eric Jang's *AI Is Good for You* was missing; Nathan Lambert had an *unverified* book claim that needed removal). Books carry the actor note's authority — missing them is more damaging than missing podcasts or newsletters. Two implications: (a) elevate the books question in the enumerative-search order (don't leave it for last); (b) when a book is claimed in a stub, verify the title against a search result before shipping — the "definitive book on RLHF" pattern (claimed → unverified → caught retroactively) is the same fabrication mode as the *Menace of Unreality* misattribution and the Yaoji Holdings → Alibaba Health correction.

3. **Non-obvious biographical dimensions matter.** Some actors have unusual non-economic dimensions that materially change how readers interpret them: Michael Pettis's Beijing indie-music-scene founder role (D-22 rock club + [[Maybe Mars]] record label) doesn't fit cleanly into any of the five questions, but it defines who he is in a way that the academic-economist framing alone misses. Rule: if a biography has an unusual non-economic dimension that defines the actor, capture it explicitly in the synopsis or quick-stats — don't leave it implicit. The five-question template covers professional outputs; this is the affiliation-outside-the-affiliation that gives the note its texture.

### When this applies

This applies to the `/deepdive` skill when the entity is an individual content producer rather than a company — see `.claude/skills/deepdive/SKILL.md` Phase 2.

The same five-question + three-refinement pattern works retroactively as an audit tool: read existing notes, identify gaps via the 5-question template, run enumerative searches for the gaps in parallel, edit in parallel, log the audit. Demonstrated on 13 notes May 18-19, 2026 with ~77% gap-hit-rate.

## 7. Claims grounding

After distributing facts from a source, check that every claim is supported by a concept note or current entity note.

### Technical terms as claims

If you write a technical term as a claim in 2+ notes (e.g., "yields rising on term premium, not inflation expectations"), verify:

- [ ] **Concept note exists** — the term has a `[[wikilinked]]` concept note explaining the mechanism
- [ ] **Mechanics are in the note** — not just a mention, but enough for a reader to understand *how you know* the claim is true

If the concept note doesn't exist, create it in the same pass. Don't leave orphaned claims across multiple notes.

### State assertions

If you assert the state of a vault entity ("inflation expectations remain stable," "labor market weakening"), verify:

- [ ] **Entity note is current** — open the note, check the last update date
- [ ] **Data supports the claim** — the note has specific data (not just old data) backing the assertion
- [ ] **Update if stale** — if the note is weeks/months behind, add the current data before or during the same pass

Failure mode: asserting "X is stable" while the X note has Jan 2026 data and you're working in April. The claim may be true, but the vault can't prove it.

---

## 8. Concept extraction

After creating or editing a note, scan for terms that deserve their own concept note. This requires domain judgment — pattern-matching can't catch it.

Ask: "Are there specific named frameworks, classifications, or mechanisms mentioned here that apply across multiple actors or theses?"

**Create a concept note:**
- "Regional Transmission Organization" — regulatory classification linking PJM, MISO, ISO-NE
- "Rule 22e-4" — SEC liquidity rule affecting fund structure decisions

**Don't create a concept note:**
- "wholesale electricity market" — too generic
- "independent federal agency" — description, not a concept

If yes, create the concept note and wikilink it in the same editing pass — don't leave it for later cleanup.

**Rule of thumb:** If the same term appears in 3+ notes as a claim (not just a mention), it almost certainly needs its own concept note. The repetition is the signal.

---

## 9. Reviewing agent-written output

When a sub-agent (research agent, deepdive sub-task, Explore agent) writes or matures a note, treat the output as a draft. Run a full compliance pass against all active vault rules — not just the automated `check_note_compliance.py` script. The script catches structural issues; it does NOT catch editorial rules like country linking, bold violations, plain-language glossing, or honest piped links.

After any agent writes a note:

- Audit for: geographic country links that should be aspect-specific, bare country hubs, bold violations, unexplained jargon, deceptive piped links
- Don't rely solely on the compliance script
- Fix all violations before telling the user the note is done
- This applies even when the agent already updated the daily note — the note itself still needs review

### Agent stub format

Sub-agents creating stub notes systematically place inline tags (`#actor #person` etc.) at the end of the one-liner paragraph instead of on their own line above it. They also add an unnecessary `# H1` header before the one-liner. The vault convention is: frontmatter → inline tags on own line → one-liner (no H1).

After any agent creates stub notes, check the first 8 lines of each file. Fix tag placement and remove H1 headers before declaring done.
