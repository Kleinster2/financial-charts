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

### Charts

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
- [ ] **Named financing participants are swept explicitly** — when a source names strategic investors, founders, board members, or operator-investors in a round, check each one for an existing note instead of stopping at the lead firms
- [ ] **Interpretive people get notes in the same pass** — if a named investor changes how the financing should be read (for example founder-operator capital vs generic VC capital), create at least a stub/actor note during the same ingestion pass

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
