# Note Structures

Templates and required content for different note types.

---

## Actor note requirements

| Actor type | Required content |
|------------|------------------|
| **Public companies** | Extensive historical financials (see [[Financials templates]]) |
| **Private companies** | Cap table (investors, rounds, valuations, total raised) |
| **Research shops / funds** | Key analysts, AUM, notable positions, recent calls |
| **Individuals** | Role, affiliations, key decisions, track record |
| **Geographies** | Economic data, key sectors, policy environment |

---

## Charts for public companies

Two standard charts for public company actor notes:

1. **Price vs benchmark** — stock performance vs relevant index (e.g., AAPL vs QQQ)
2. **Fundamentals** — revenue, net income, and free cash flow (absolute values)

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
