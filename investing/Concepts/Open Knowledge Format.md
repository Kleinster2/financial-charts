---
aliases: [OKF, Google Open Knowledge Format]
tags: [concept, ai, data-infrastructure, standard]
---

# Open Knowledge Format

Open, vendor-neutral specification published by [[Google]] Cloud on June 12, 2026 for describing organizational knowledge to [[AI agents]] as a directory of Markdown files with YAML frontmatter — one file per concept (table, metric, playbook), only `type` required. This is the market-side node; the full technical specification lives in the technologies vault (cross-link below).

Market relevance: OKF turns the proprietary contents of a data catalog into a portable, free interchange format, which is why it is the catalyst for the [[Data catalog disruption]] thesis. Authored by Google engineers Sam McVeety and Amir Hormati; ships with a BigQuery producer, a static-HTML consumer, and an updated Knowledge Catalog that serves OKF to agents — a classic commoditize-the-complement move that makes the format free while monetizing the serving layer.

---

## Quick stats

| Metric | Value |
|--------|-------|
| Publisher | [[Google]] Cloud |
| Released | June 12, 2026 (v0.1) |
| Format | Markdown + YAML frontmatter, one `.md` per concept |
| Repo | GoogleCloudPlatform/knowledge-catalog |
| First source | BigQuery |

OKF is a specification, not a tradeable entity; market exposure is expressed through [[Data catalog disruption]]. No public price series to chart. (Market data not applicable.)

---

## Related

- [[Data catalog disruption]] — the market thesis OKF catalyzes
- [[Modern data stack]] — where the catalog layer sits
- [[AI agents]] — the consumer OKF is written for
- [[MCP]] — analogous open standard (tools, not knowledge)

### Cross-vault
- [Technologies: Open Knowledge Format](obsidian://open?vault=technologies&file=Open%20Knowledge%20Format) — full technical spec: bundle structure, frontmatter fields, link semantics, design principles, reference implementations

*Created 2026-06-13*
