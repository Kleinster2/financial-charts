---
aliases: [sector correlation report May 2026, sector taxonomy diagnostic 2026-05-09]
tags: [report, diagnostic, vault-structure, sectors, correlation]
created: 2026-05-09
window: 252 trading days through 2026-05-03
script: scripts/sector_correlation_diagnostic.py
---

#report #diagnostic #sectors

# Sector internal correlation diagnostic — 2026-05-09

A whole-vault check on whether `Sectors/` hubs have meaningful internal correlation, i.e. whether members share a common price driver or are merely filed together.

---

## Method

For each `Sectors/*.md` note, extract `[[Actor]]` wikilinks, map them to tickers via `Actors/*.md` frontmatter aliases (with `ticker_metadata.name` as a fallback), pull daily closes from `stock_prices_daily` over the trailing 252 trading days through 2026-05-03, compute pairwise Pearson correlation on simple daily returns, and report mean and median across the pair set.

96 sector hubs total. 68 had at least three actors mappable to DB tickers and produced a correlation reading. 28 had insufficient mapped tickers (private-only sectors, missing actor lists, or unfilled aliases).

Caveats. Raw correlation is biased upward by market beta — a sector at 0.27 is less coherent than the number suggests once SPY is netted out. The 252-day window can mask regime shifts. Results are a relative ranking, not an absolute coherence score.

---

## Results — coherent thematic hubs (avg pairwise ≥ 0.50)

| Sector | Actors mapped | Avg corr | Median |
|--------|--------------:|---------:|-------:|
| [[WFE]] | 4 | 0.83 | 0.83 |
| [[Private Real Estate]] | 6 | 0.77 | 0.78 |
| [[Alternative Managers]] | 6 | 0.73 | 0.75 |
| [[US Retail Trading]] | 3 | 0.70 | 0.69 |
| [[US Memory]] | 3 | 0.70 | 0.69 |
| [[Residential Mortgage]] | 4 | 0.69 | 0.68 |
| [[Financial data industry]] | 5 | 0.68 | 0.68 |
| [[Crypto-to-AI]] | 6 | 0.68 | 0.68 |
| [[Copper Mining]] | 9 | 0.66 | 0.68 |
| [[Semiconductor Materials]] | 4 | 0.65 | 0.65 |
| [[P&C Insurance]] | 3 | 0.65 | 0.66 |
| [[AI Compute]] | 3 | 0.58 | 0.56 |
| [[Chinese Entertainment]] | 3 | 0.57 | 0.56 |
| [[Data Analytics Conglomerates]] | 7 | 0.56 | 0.55 |
| [[Hotel industry]] | 5 | 0.54 | 0.50 |
| [[Banks]] | 13 | 0.52 | 0.54 |
| [[Analysts and Strategists]] | 4 | 0.51 | 0.51 |
| [[ETF Issuers]] | 5 | 0.51 | 0.45 |
| [[Sensors]] | 4 | 0.50 | 0.50 |
| [[Sports betting]] | 5 | 0.50 | 0.46 |

These hubs are doing analytical work — when WFE rallies, [[Applied Materials]], [[Lam Research]], [[KLA]] and [[ASML]] tend to move together; when Private Real Estate sells off, [[Blackstone]], [[Brookfield]] and friends sell off together. The sector view is a real lens.

---

## Mid-band (0.30–0.50) — pulling some weight, partly diluted

| Sector | Mapped | Avg corr |
|--------|-------:|---------:|
| [[Semiconductor Test]] | 5 | 0.46 |
| [[Private Equity]] | 5 | 0.46 |
| [[Private Credit]] | 16 | 0.45 |
| [[Real estate]] | 4 | 0.44 |
| [[Life Insurance]] | 3 | 0.41 |
| [[Telecom]] | 4 | 0.41 |
| [[DC REITs]] | 5 | 0.40 |
| [[Payments Networks]] | 5 | 0.39 |
| [[Memory]] | 5 | 0.38 |
| [[Space]] | 11 | 0.38 |
| [[Consumer Staples]] | 3 | 0.37 |
| [[Aerospace]] | 6 | 0.37 |
| [[Cybersecurity]] | 14 | 0.35 |
| [[Fintech]] | 13 | 0.35 |
| [[Connectivity]] | 3 | 0.34 |
| [[Biopharma]] | 12 | 0.34 |
| [[Munitions]] | 3 | 0.34 |
| [[Database companies]] | 3 | 0.34 |
| [[Luxury]] | 7 | 0.33 |
| [[Housing]] | 12 | 0.32 |
| [[REITs]] | 3 | 0.31 |
| [[Semiconductors]] | 23 | 0.31 |
| [[Defense IT Services]] | 4 | 0.31 |

Most of these are still doing real work but have noticeable internal heterogeneity. Cybersecurity at 0.35 across 14 actors is healthier than it sounds — that's a coherent signal across a large set. Semiconductors at 0.31 across 23 actors is the opposite — a parent hub diluted by its own breadth.

---

## Low signal (< 0.30) — broad sectors with diluted drivers

| Sector | Mapped | Avg corr |
|--------|-------:|---------:|
| [[Commercial real estate]] | 3 | 0.28 |
| [[AI Infrastructure]] | 22 | 0.27 |
| [[Energy and Utilities]] | 14 | 0.27 |
| [[Drones]] | 4 | 0.27 |
| [[Specialty Coffee]] | 3 | 0.27 |
| [[Defense Primes]] | 10 | 0.26 |
| [[Restaurants]] | 4 | 0.26 |
| [[Data Centers]] | 26 | 0.26 |
| [[Gaming Hardware]] | 4 | 0.26 |
| [[Fashion]] | 12 | 0.26 |
| [[Insurance]] | 19 | 0.26 |
| [[Robotics]] | 10 | 0.25 |
| [[Infrastructure]] | 12 | 0.25 |
| [[Automotive]] | 9 | 0.24 |
| [[Beauty]] | 6 | 0.23 |
| [[Consumer Internet]] | 18 | 0.23 |
| [[Drug Distribution]] | 7 | 0.22 |
| [[Gaming]] | 15 | 0.22 |
| [[AI VFX Tools]] | 5 | 0.21 |
| [[Travel]] | 6 | 0.20 |
| [[Consumer]] | 6 | 0.20 |
| [[Life Sciences]] | 5 | 0.19 |
| [[AI Video Generation]] | 8 | 0.18 |
| [[AI-Native Studios]] | 6 | 0.18 |
| [[Healthcare]] | 25 | 0.17 |
| [[Media]] | 16 | 0.16 |
| [[Defense]] | 10 | 0.15 |
| [[Sovereign Wealth Funds]] | 3 | 0.14 |
| [[Activist Investors]] | 3 | 0.13 |
| [[Transport]] | 5 | 0.12 |
| [[Corporate Venture Capital]] | 5 | 0.10 |

Two distinct cases here.

The first is genuinely diluted thematic sectors — Healthcare, Defense, Insurance, Media, Consumer Internet — where the price driver is fragmented because the hub aggregates structurally different sub-industries. These are the candidates for splitting.

The second is organisationally defined hubs — Sovereign Wealth Funds, Activist Investors, Corporate Venture Capital — where the members are categorised by what they do rather than by what they sell, and so their share-price drivers are correctly unrelated. These hubs work as directories, not as sectors. They should be classified differently.

---

## Coverage gaps — 28 sectors with insufficient mapped tickers

Two-actor or single-actor mapped sets are too thin for a meaningful pairwise correlation. Some are private-only by nature — [[Hedge Funds]], [[Family Offices]], [[Iranian banking]], [[Cement]], [[Title Insurance]], [[Senior Living]]. Others should be fixable by expanding the actor list or fixing aliases.

Notable gaps to fix:

- [[AI Storage]] — only 1 actor mapped to a DB ticker. [[Pure Storage]] (PSTG) and [[NetApp]] (NTAP) are public and exist in the DB, so this is a missing-link problem in the sector hub.
- [[Edge cloud]] — only 2 mapped despite [[Akamai]], [[Cloudflare]], [[Fastly]] all being public.
- [[Korea AI chips]], [[Korea Memory]] — 2 each. [[Samsung]] and [[SK Hynix]] are in the DB; the issue is wikilink coverage in the hub.
- [[Software-defined Defense]] — 2 mapped. [[Palantir]], [[Anduril]] (private), [[Rebellion Defense]] (private), [[Shield AI]] (private) — partly a private-actor problem, partly a hub-link problem.

---

## Implications

The diagnostic backs the hypothesis that sectors should have meaningful internal correlation when they are doing analytical rather than purely directory work. The shape of the data also confirms that the right place for tight thematic clusters is *below* a parent sector hub — sub-sectors like AI Compute, US Memory, Semi Materials, Semi Test all show stronger coherence than their parent [[Semiconductors]] hub, which means the structural pattern is to demote some parents to indices and let the sub-sectors do the analytical work.

The split between thematic-but-too-broad sectors and organisationally defined hubs also suggests a tag-level distinction rather than a single `#sector` bucket. Capital allocators (SWFs, activists, CVC, family offices) should not be measured by the same correlation yardstick as industry hubs.

### Suggested follow-ups

1. Restructure parent hubs whose sub-sectors already show stronger coherence: [[Semiconductors]], [[AI Infrastructure]], [[Defense]], [[Healthcare]], [[Media]], [[Insurance]] become indexes that link to tighter sub-sector hubs.
2. Re-tag organisationally defined hubs ([[Activist Investors]], [[Sovereign Wealth Funds]], [[Corporate Venture Capital]], [[Family Offices]], [[Hedge Funds]], [[Individual Investors]], [[Market Makers]]) with a tag like `#capital-allocator` rather than `#sector`, so the diagnostic stops flagging them as broken.
3. Fill the hub-link gaps in [[AI Storage]], [[Edge cloud]], [[Korea AI chips]], [[Korea Memory]] so the next run gives a real reading.
4. Re-run the diagnostic quarterly via `scripts/sector_correlation_diagnostic.py` to track whether splits actually raised coherence.

---

## Reproducing this report

`python scripts/sector_correlation_diagnostic.py` from the repo root regenerates the full table. Use `--window N` to change the trailing window (default 252) and `--min-actors N` to change the threshold for inclusion (default 3).

The script depends on `Actors/*.md` frontmatter aliases for the actor-to-ticker map, so improving alias coverage directly improves the next run.

---

## Related

- [[Sectors and clusters do different work]] — taxonomic hubs vs narrative groupings (Telegram thread 2026-05-09)
- [[Vault structure]] — vault folder taxonomy
- [[quick_movers]] — daily mover detection that benefits from coherent sector hubs
