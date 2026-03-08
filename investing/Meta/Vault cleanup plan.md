#meta #maintenance

# Vault cleanup plan

Saved March 8, 2026 from a review of the investing vault.

Current state at review:
- 4,214 notes
- 43,497 links
- 4 orphan notes
- Main risk: quality dispersion, especially across short `Actors/` notes

---

## Goal

Shift the vault from collection mode to signal-density mode.

The vault is already useful. The next step is to keep note quality, review cadence, and graph structure from falling behind note count.

---

## Anchor habit: weekly maintenance

This only works if it becomes a repeated habit rather than a one-time cleanup project.

Start the weekly checklist immediately and keep it lightweight enough to survive:

- review active theses
- close or advance research queue items
- prune or merge dead stubs
- refresh dashboard charts
- check chart freshness on embedded visuals that matter to active notes

---

## Week 1: Triage and simplification

### 1. Freeze low-value note creation

Stop creating new low-value `Actors/` notes unless they directly support a live thesis, event, or daily note.

### 2. Keep the note system binary

Do not overcomplicate note classes. In practice, most notes should be treated as one of two things:

- **Active**: doing real work for current research, synthesis, or decision-making
- **Stub**: placeholder notes waiting to be upgraded, merged, or retired

This is easier to enforce than a three-tier system with fuzzy middle categories.

### 3. Use minimal metadata only

Do not create metadata that will not be maintained.

Use only:

- `status`
- `last_reviewed`

Suggested `status` values:

- `stub`
- `active`
- `mature`

### 4. Triage the shortest notes first

Focus first on short `Actors/` notes.

Each short note should become one of three things:

- a true stub with explicit missing fields
- merged into a stronger parent note
- retired only after a backlink check confirms it can be removed safely

Deletion should be rare. If a note has inbound links, merge or redirect rather than delete.

---

## Week 2: Strengthen the graph around decisions

### 1. Upgrade the highest-value hubs

Pick 10-15 high-value notes and fully upgrade them.

Suggested starting set:

- [[Long datacenter infrastructure]]
- [[2026 Iran conflict market impact]]
- [[Google]]
- [[research-queue]]
- [[Dashboard]]
- [[OpenAI]]
- [[NVIDIA]]
- [[AI capex arms race]]
- [[Power constraints]]
- [[Private credit retail liquidity crisis 2026]]
- [[Long inference stack]]
- [[Long memory]]
- [[Semiconductors]]
- [[AI Infrastructure]]
- [[Oil]]

### 2. Standardize what a strong hub contains

Each important hub should have:

- a crisp thesis or takeaway
- key supporting links
- disconfirming evidence
- what would change the conclusion
- the next review trigger

### 3. Promote more from Daily to evergreen

The daily workflow is strong, but the vault compounds only when material from `Daily/` gets pushed into thesis, event, concept, and actor notes.

---

## Week 3: Automate maintenance

### 1. Extend vault health checks

Extend `vault_health.py` or add a second script to report:

- shortest notes
- notes missing `last_reviewed`
- notes with many inbound links but weak content
- stale active theses
- daily notes whose useful links were never promoted to evergreen notes
- stale charts attached to active notes or the dashboard

### 2. Keep the dashboard opinionated

[[Dashboard]] should stay focused on what matters now, not become a gallery of everything.

---

## One-rule version

If only one rule gets enforced, make stub handling ruthless.

The vault is already past the "collect more" stage and into the "raise signal density" stage.
