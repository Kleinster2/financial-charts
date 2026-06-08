---
aliases: [Repo smoke map 2026-06-08]
tags: [report, vault-hygiene]
---

# Repo smoke map 2026-06-08

This is a bounded smoke map, not a claim that the whole repository is compliance-clean. The full `scripts/check_note_compliance.py --all` pass exceeded the normal runtime window, and a quiet full-check importer also exceeded five minutes. The usable result from this pass is a fast structural classification plus a small hard-error cleanup.

## Scope

| Folder | Notes |
|--------|------:|
| Actors | 4,867 |
| Analysts | 123 |
| Concepts | 1,024 |
| Events | 214 |
| Theses | 32 |
| Total | 6,260 |

## Hard-error map

| Bucket | Count | Interpretation |
|--------|------:|----------------|
| Public notes missing price-chart marker | 1,173 | Old actor-template debt; requires chart/data work by cohort |
| Public notes missing fundamentals/financial marker | 893 | Old actor-template debt; likely mixes true missing data and exemption-language gaps |
| Public notes missing Sankey marker | 1,242 | Old actor-template debt; should be fixed with fundamentals/chart cohort passes |
| Public notes missing securities-note marker | 1,224 | Actor/securities split backlog |
| Public notes missing sector-correlation marker | 829 | Cluster/correlation backlog |
| Private notes missing cap-table marker | 878 | Private-company depth backlog |
| Private notes missing funding-rounds marker | 995 | Private-company funding-table backlog |
| Missing frontmatter | 777 | Universal structural backlog |
| Extra bold formatting | 2,246 files / 30,726 instances | Mechanical formatting backlog, too broad for a single safe commit |
| Missing `## Related` | 4 | Universal structural gap; fixed in this pass |
| Actor/analyst notes missing Quick stats | 742 | Actor/analyst shape backlog |
| Frontmatter wikilinks | 1 | Universal frontmatter gap; fixed in this pass |
| Analyst body hashtag lines | 4 | Analyst-note shape backlog |

## Fixed in this pass

- [[Agriculture]] - removed the `[[DBA]]` wikilink from YAML aliases while preserving DBA as a plain alias.
- [[AI Race]] - added frontmatter, added `## Related`, and stripped 21 extra bold spans.
- [[Foundry Wars]] - added frontmatter and `## Related`.
- [[Glassworm botnet takedown May 2026]] - added `## Related`.
- [[Netflix-WB Senate Antitrust Hearing 2026-02-03]] - added frontmatter, converted the inline related line into `## Related`, normalized dead links to existing notes, and stripped 21 extra bold spans.

Targeted validation after edits:

| Check | Result |
|-------|--------|
| Five-note target set | 0 errors / 24 warnings |
| Built-in bold fixer | 42 extra bold spans removed |

The 24 remaining warnings are backlog by design: correlation-structure warnings on old index notes, missing/dead-link hints, and one market-reaction warning on the Netflix-WB event.

## Backlog order

1. Public actor template debt by cohort: securities-note links, price/fundamentals/Sankey charts, financials, and sector correlation.
2. Private actor depth debt: cap table and funding-round table passes by private-capital cluster.
3. Universal structure: missing frontmatter and missing Quick stats.
4. Mechanical formatting: extra bold spans, only in scoped batches so the daily-note inventory stays readable.
