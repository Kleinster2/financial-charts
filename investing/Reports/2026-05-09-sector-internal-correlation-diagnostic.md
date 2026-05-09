---
aliases: [sector correlation report May 2026, sector taxonomy diagnostic 2026-05-09]
tags: [report, diagnostic, vault-structure, sectors, correlation]
created: 2026-05-09
updated: 2026-05-09
window: 252 trading days through 2026-05-03
script: scripts/sector_correlation_diagnostic.py
---

#report #diagnostic #sectors

# Sector internal correlation diagnostic — 2026-05-09

A whole-vault check on whether `Sectors/` hubs have meaningful internal correlation, i.e. whether members share a common price driver or are merely filed together.

This is the second pass of the diagnostic, run after commit `f658ff5` implemented three of the four follow-ups from the first pass — capital-allocator retag, parent-hub indexes, and hub-link gap fills. The DB window is unchanged, so deltas here come purely from membership and tagging changes in the vault, not from market regime shifts.

---

## Method

For each `Sectors/*.md` note, extract `[[Actor]]` wikilinks, map them to tickers via `Actors/*.md` frontmatter aliases (with `ticker_metadata.name` as a fallback), pull daily closes from `stock_prices_daily` over the trailing 252 trading days through 2026-05-03, compute pairwise Pearson correlation on simple daily returns, and report mean and median across the pair set.

101 sector hubs total. 7 are now tagged `#capital-allocator` and skipped at the script level — they aggregate firms by what they do (allocate capital), not by what they sell, so internal price-driver correlation is correctly absent. 73 of the remaining 94 hubs had at least three actors mappable to DB tickers and produced a correlation reading. 21 had insufficient mapped tickers (private-only sectors, missing actor lists, or unfilled aliases).

Caveats. Raw correlation is biased upward by market beta — a sector at 0.27 is less coherent than the number suggests once SPY is netted out. The 252-day window can mask regime shifts. Results are a relative ranking, not an absolute coherence score.

---

## Changes since prior run

Three structural changes in the vault between runs, all driven by the prior diagnostic:

- Seven hubs retagged from `#sector` to `#capital-allocator` and now skipped: [[Activist Investors]], [[Sovereign Wealth Funds]], [[Corporate Venture Capital]], [[Family Offices]], [[Hedge Funds]], [[Individual Investors]], [[Market Makers]]. They no longer pollute the low-signal band.
- Six parent hubs converted to index-with-callout pages, naming the tighter children below them: [[Semiconductors]], [[AI Infrastructure]], [[Defense]], [[Healthcare]], [[Media]], [[Insurance]]. Their correlation readings here are the index correlation, not a thematic-sector reading — low coherence is now the expected behaviour, not a flaw.
- Three of four hub-link gaps closed. [[AI Storage]] went from 1 mapped ticker to 4 (NetApp wikilinked, [[Pure Storage]] confirmed, [[Dell]] and [[HPE]] picked up after alias fixes). [[Korea AI chips]] and [[Korea Memory]] both unblocked once `005930.KS` was added as a [[Samsung]] alias. [[Edge cloud]] is still capped at 2 mapped because [[Fastly]] (FSLY) is not present in `stock_prices_daily`.

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

Unchanged from the prior run — none of these hubs were touched by the restructure. They continue to do real analytical work: when WFE rallies, [[Applied Materials]], [[Lam Research]], [[KLA]] and [[ASML]] move together; when Private Real Estate sells off, [[Blackstone]], [[Brookfield]] and friends sell off together.

---

## Mid-band (0.30–0.50) — pulling some weight, partly diluted

| Sector | Mapped | Avg corr | Note |
|--------|-------:|---------:|------|
| [[Semiconductor Test]] | 5 | 0.46 | |
| [[Private Equity]] | 5 | 0.46 | |
| [[Private Credit]] | 16 | 0.45 | |
| [[Real estate]] | 4 | 0.44 | |
| [[AI Storage]] | 4 | 0.41 | new entry — gap closed (was 1 mapped) |
| [[Life Insurance]] | 3 | 0.41 | |
| [[Telecom]] | 4 | 0.41 | |
| [[DC REITs]] | 5 | 0.40 | |
| [[Payments Networks]] | 5 | 0.39 | |
| [[Space]] | 11 | 0.38 | |
| [[Consumer Staples]] | 3 | 0.37 | |
| [[Aerospace]] | 6 | 0.37 | |
| [[Memory]] | 6 | 0.36 | |
| [[Cybersecurity]] | 14 | 0.35 | |
| [[Fintech]] | 13 | 0.35 | |
| [[Korea Memory]] | 3 | 0.35 | new entry — gap closed (was 2 mapped) |
| [[Connectivity]] | 3 | 0.34 | |
| [[Biopharma]] | 12 | 0.34 | |
| [[Munitions]] | 3 | 0.34 | |
| [[Database companies]] | 3 | 0.34 | |
| [[Luxury]] | 7 | 0.33 | |
| [[Housing]] | 12 | 0.32 | |
| [[REITs]] | 3 | 0.31 | |
| [[Defense IT Services]] | 4 | 0.31 | |

[[AI Storage]] at 0.41 is a clean win — the hub now reads as a coherent sub-sector of [[AI Infrastructure]] rather than a one-actor stub. [[Korea Memory]] at 0.35 lands where one would expect a 3-actor Korea-listed memory cluster: directionally coherent but pulled down by KRW dynamics and trading-hour gaps. Cybersecurity at 0.35 across 14 actors remains a healthy reading — that is a coherent signal across a large set, not the same animal as a 3-actor 0.35 cluster.

---

## Low signal (< 0.30) — broad sectors with diluted drivers

| Sector | Mapped | Avg corr | Status |
|--------|-------:|---------:|--------|
| [[Korea AI chips]] | 3 | 0.30 | new entry — gap closed (was 2 mapped) |
| [[Semiconductors]] | 24 | 0.29 | converted to index in f658ff5 |
| [[Commercial real estate]] | 3 | 0.28 | |
| [[Energy and Utilities]] | 14 | 0.27 | |
| [[Drones]] | 4 | 0.27 | |
| [[Specialty Coffee]] | 3 | 0.27 | |
| [[Defense Primes]] | 10 | 0.26 | |
| [[Restaurants]] | 4 | 0.26 | |
| [[Data Centers]] | 26 | 0.26 | |
| [[Gaming Hardware]] | 4 | 0.26 | |
| [[Fashion]] | 12 | 0.26 | |
| [[Insurance]] | 19 | 0.26 | converted to index in f658ff5 |
| [[Robotics]] | 10 | 0.25 | |
| [[Infrastructure]] | 12 | 0.25 | |
| [[AI Infrastructure]] | 23 | 0.25 | converted to index in f658ff5 |
| [[Automotive]] | 9 | 0.24 | |
| [[Beauty]] | 6 | 0.23 | |
| [[Consumer Internet]] | 18 | 0.23 | |
| [[Drug Distribution]] | 7 | 0.22 | |
| [[Gaming]] | 15 | 0.22 | |
| [[AI VFX Tools]] | 5 | 0.21 | |
| [[Travel]] | 6 | 0.20 | |
| [[Consumer]] | 6 | 0.20 | |
| [[Life Sciences]] | 5 | 0.19 | |
| [[AI Video Generation]] | 8 | 0.18 | |
| [[AI-Native Studios]] | 6 | 0.18 | |
| [[Healthcare]] | 25 | 0.17 | converted to index in f658ff5 |
| [[Defense]] | 10 | 0.15 | converted to index in f658ff5 |
| [[Media]] | 17 | 0.14 | converted to index in f658ff5 |
| [[Transport]] | 5 | 0.12 | |

Three reads here.

The first is the parent-hub-as-index group. [[Semiconductors]], [[AI Infrastructure]], [[Defense]], [[Healthcare]], [[Media]] and [[Insurance]] still report low coherence — and that is now the intended behaviour. They were converted to indexes in `f658ff5` because their sub-sectors carry the analytical work; the parent reading is the residual, which is supposed to look diluted.

The second is genuinely diluted thematic sectors that have not yet been split — [[Consumer Internet]] (0.23 across 18), [[Gaming]] (0.22 across 15), [[Energy and Utilities]] (0.27 across 14), [[Fashion]] (0.26 across 12). These are the next candidates for parent-to-index conversion.

The third is sub-sector hubs that are *meant* to be tight but came in at low-signal — [[Robotics]] at 0.25, [[Drones]] at 0.27, [[AI VFX Tools]] at 0.21, [[AI-Native Studios]] at 0.18, [[AI Video Generation]] at 0.18. These are the hubs to watch: if Robotics is meant to be a coherent thematic cluster, a 0.25 reading suggests either heterogeneous membership or that no shared price driver has emerged yet (i.e. the market is not yet trading robotics as one thing).

---

## Coverage gaps — 21 sectors with insufficient mapped tickers

Down from 28 in the prior run. The capital-allocator retag and the AI Storage / Korea hub fixes account for the reduction.

Still genuinely private-only or near-private: [[Hedge Funds]], [[Family Offices]], [[Senior Living]], [[Cement]], [[Title Insurance]], [[Title Agencies]], [[Iranian banking]], [[China defense]], [[Venture Capital]], [[Growth Equity]], [[Mortgage REITs]], [[Mortgage]], [[Commercial Mortgage]], [[Asset Managers]], [[Aluminum Mining]], [[Sextech]], [[AI Avatars]], [[DTC Telehealth]].

Still gapped despite at least one public member:

- [[Edge cloud]] — 2 mapped. [[Fastly]] (FSLY) is public but missing from `stock_prices_daily`. Action: ingest FSLY into the price DB. Then [[Akamai]], [[Cloudflare]], [[Fastly]] gives a 3-actor reading.
- [[Software-defined Defense]] — 2 mapped. [[Palantir]] is in; the rest of the natural cohort ([[Anduril]], [[Rebellion Defense]], [[Shield AI]]) is private. This is structurally a private-actor problem and may stay capped until one of them lists.
- [[Fertilizer]] — 2 mapped. Several public fertilizer names exist (CF, MOS, NTR) but are not yet wikilinked from the hub. Fixable in the hub itself.
- [[Shipping]] — 1 mapped. Multiple public shippers exist; this is a hub-link audit problem.

---

## Implications

The restructure landed cleanly. The coherent set is unchanged because the hubs in it weren't touched, the gap fills produced in-band readings (AI Storage 0.41, Korea Memory 0.35), and the parent-to-index conversions show up as expected — low coherence, but with their correlation reading now contextualised as an index residual rather than a thematic verdict.

The next pass of structural work has two natural targets. The first is the second wave of parent-to-index conversions for [[Consumer Internet]], [[Gaming]], [[Energy and Utilities]], [[Fashion]] and possibly [[Cybersecurity]] — all carry enough breadth that the hub reading is a directory readout, not a sector readout. The second is the watchlist of sub-sector hubs that came in soft despite being designed as tight clusters: [[Robotics]], [[AI Video Generation]], [[AI-Native Studios]], [[AI VFX Tools]]. For each of these the diagnostic question is whether the membership is heterogeneous or whether the market is simply not yet trading the theme as one thing. That distinction matters for portfolio construction — heterogeneous hubs need splitting, latent-theme hubs need waiting on.

The skip of capital-allocator hubs also opens a separate diagnostic question for that set: a coherent capital-allocator hub is one where members have correlated *fund flows* or *AUM dynamics*, not correlated stock prices. That is a different measurement and a different next report.

### Suggested follow-ups

1. Extend the parent-to-index pattern to [[Consumer Internet]], [[Gaming]], [[Energy and Utilities]], [[Fashion]], and reassess [[Cybersecurity]]. The bar: if at least two children read tighter than the parent, convert the parent.
2. Investigate the soft-reading thematic hubs ([[Robotics]], [[AI Video Generation]], [[AI-Native Studios]], [[AI VFX Tools]]) — split if heterogeneous, leave and revisit if the theme is latent.
3. Ingest [[Fastly]] (FSLY) into `stock_prices_daily` so [[Edge cloud]] gives a real reading next pass.
4. Audit hub-link coverage for [[Fertilizer]] and [[Shipping]] — both should clear the threshold once public members are wikilinked in.
5. Design a separate flow-based diagnostic for `#capital-allocator` hubs (correlated AUM growth, fund-flow betas) rather than reusing the price-correlation pipeline.
6. Re-run this diagnostic quarterly via `scripts/sector_correlation_diagnostic.py` to track whether splits actually raised coherence.

---

## Reproducing this report

`python scripts/sector_correlation_diagnostic.py` from the repo root regenerates the full table. Use `--window N` to change the trailing window (default 252) and `--min-actors N` to change the threshold for inclusion (default 3).

The script depends on `Actors/*.md` frontmatter aliases for the actor-to-ticker map and on `Sectors/*.md` frontmatter tags to skip `#capital-allocator` hubs. Improving alias coverage and tagging coverage directly improves the next run.

---

## Related

- [[Sectors and clusters do different work]] — taxonomic hubs vs narrative groupings (Telegram thread 2026-05-09)
- [[Vault structure]] — vault folder taxonomy
- [[quick_movers]] — daily mover detection that benefits from coherent sector hubs
