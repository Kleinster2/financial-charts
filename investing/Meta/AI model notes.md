# AI Model Notes

Design discussion: where should individual AI models (ChatGPT, Claude, Gemini) live in the vault?

**Status:** Resolved — Products/ folder created

---

## Current state

Individual models exist as Actors:
- `ChatGPT.md`, `Claude.md`, `Gemini.md`, `DeepSeek.md`, `Doubao.md`, `Ernie.md`, `GLM.md`

Model category concepts exist:
- `Chinese open models.md`, `Text diffusion models.md`

Missing category concepts:
- `Frontier models`, `Reasoning models`, `Multimodal models`, `Open-weight models`

---

## The problem

Models don't fit cleanly in any folder:

| Folder | Fit | Tension |
|--------|-----|---------|
| Actors | Entities you track | No agency — labs make decisions, not products |
| Concepts | Ideas, phenomena | ChatGPT is an instance, not a category |
| Events | Moments in time | Launch is an event, but product persists |
| Products/ (new) | Clean semantics | Adds hierarchy; only AI models need it |

---

## Options evaluated

### 1. Keep as Actors (current)

Accept that "Actor" means "named entity" not "agent." Products are the exception.

| Pro | Con |
|-----|-----|
| Already built this way | Only products lack agency |
| Matches how market talks | Blurs Actor definition |
| No migration needed | Mental asterisk required |

### 2. Fold into parent labs

Merge ChatGPT → OpenAI, Claude → Anthropic. Keep only category concepts.

| Pro | Con |
|-----|-----|
| One source of truth | Violates atomic (OpenAI ≠ ChatGPT) |
| Matches how you'd invest | Loses product-level granularity |
| Less maintenance | ChatGPT has cultural weight beyond OpenAI |

### 3. Split: Events + parent sections

Launch moments in Events/, ongoing product specs as sections in parent Actor.

| Pro | Con |
|-----|-----|
| Events = moments (correct) | Fragments one thing into two places |
| Actors = agents (correct) | No single home for "ChatGPT" |
| Clean definitions | More complex to navigate |

### 4. Create Products/ folder

New folder for things made and sold by Actors.

| Pro | Con |
|-----|-----|
| Semantic clarity | Violates "links over folders" |
| Solves agency problem | Only ~7 notes need this |
| Natural home for products | Slippery slope (Services? Features?) |
| | Boundary problems (is H100 a product?) |

### 5. Move to Concepts

Treat ChatGPT as "the ChatGPT phenomenon."

| Pro | Con |
|-----|-----|
| Concepts don't need agency | Instance vs category confusion |
| Matches some existing notes | ChatGPT has concrete attributes (pricing, users) |
| | "Frontier models" is concept; ChatGPT is instance |
| | Wrong level of abstraction |

---

## Why AI models got reified

Other products don't have notes (no iPhone.md, Azure.md, S3.md). Only AI models did.

Hypothesis: AI models *feel* agentive because they talk back. They respond, refuse, reason. This creates a perception of agency even though decisions (pricing, features, access) are made by the parent lab.

This is a perception quirk, not a structural reality. The vault structure shouldn't be driven by it.

---

## Resolution

**New folder: Products/**

Products are things made by Actors that lack agency but warrant detailed tracking.

### Definition

A note belongs in Products/ if:

1. It's a product/artifact, not an entity with agency
2. It has a clear parent Actor who makes decisions about it
3. It's an instance of a Concept category
4. It's significant enough to need its own detailed note

### What belongs in Products/

| Category | Examples |
|----------|----------|
| AI models | ChatGPT, Claude, Gemini, DeepSeek |
| AI chips | H100, B200, A100, MI300X |
| Pharmaceuticals | Ozempic, Wegovy, Mounjaro |
| Vehicles | Model 3, Cybertruck, F-150 Lightning |
| Rockets | Falcon 9, Starship, New Glenn |

### Structure

Each product note links to:
- **Parent Actor** — who makes decisions about it (NVIDIA, OpenAI, Novo Nordisk)
- **Parent Concept** — what category it belongs to (AI accelerators, Frontier models, GLP-1 drugs)

### Why not other folders?

| Folder | Why not |
|--------|---------|
| Actors | Products lack agency — the parent Actor decides |
| Concepts | Products are instances, not categories |
| Events | Product launch is an event, but the product persists |

### Migration

Move from Actors/ to Products/:
- `ChatGPT.md`, `Claude.md`, `Gemini.md`, `DeepSeek.md`, `Doubao.md`, `Ernie.md`, `GLM.md`

Create new:
- `H100.md`, `B200.md`, etc. as needed

---

## Related

- [[Linking and hierarchy]]
- [[Note structures]]
