---
aliases:
  - MiniMax securities
  - MiniMax stock
  - 0100.HK
  - HKEX 0100
tags:
  - asset
  - equities
  - hong-kong
  - china
---

# MiniMax securities note

MiniMax securities note tracks public-market exposure to [[MiniMax]] through its Hong Kong-listed shares and its proposed RMB-share / [[STAR Market]] route.

## Instruments

| Instrument | Venue | Status |
|------------|-------|--------|
| Class A ordinary shares | [[HKEX]] | Listed January 9, 2026; stock code 0100 |
| Proposed RMB shares | [[STAR Market]] | Preliminary proposal announced May 31, 2026; no assurance it will materialize |

## Capital-market timeline

| Date | Event | Signal |
|------|-------|--------|
| December 31, 2025 | HKEX listing application timetable published | Dealings expected to begin January 9, 2026; stock code 0100 |
| January 9, 2026 | Hong Kong trading commenced | MiniMax became a direct public-market proxy for China's model-lab tier |
| May 31, 2026 | Proposed RMB-share / STAR Market announcement | MiniMax began exploring mainland RMB-share access after its HK listing |
| June 1, 2026 | [[MiniMax M3]] release and post-announcement trading | Product catalyst and capital-market catalyst arrived together |

## STAR Market proposal

The May 31 announcement says MiniMax is assessing a possible issue of RMB-denominated shares and listing of those RMB shares on the [[STAR Market]]. The company had engaged professional advisers and entered a tutoring agreement, but concrete issue size, timing, board/shareholder approvals, and regulatory approvals were not settled.

This is not a completed fundraising event. The clean read-through is that MiniMax is trying to add a mainland funding and investor-access channel on top of its offshore Hong Kong listing.

## Price / data note

External quote pages showed a volatile June 1 tape after the STAR proposal and M3 release. StockAnalysis showed a June 1 open at HK$884, high HK$907.50, low HK$702, close HK$717, down 14.64%; Investing.com-style feeds showed HK$708, down 15.71%, likely reflecting last price / adjusted feed timing.

Local chart automation did not validate the ticker: `python scripts/add_ticker.py 0100.HK` failed to fetch a usable history from yfinance, so no local chart was generated. Treat this note as manually sourced until the vault price pipeline supports 0100.HK.

## Investing read-through

0100.HK is useful because it is one of the few listed ways to express the Chinese foundation-model lab story. The risk is that the equity can trade on three overlapping narratives that do not always confirm each other:

- product capability: [[MiniMax M3]], [[Hailuo]], token volume, benchmark claims
- capital access: HK listing, possible RMB shares, [[STAR Market]]
- China AI sentiment: [[China AI Tigers]], public-market validation premium, A-share/H-share momentum

## Sources

- MiniMax HKEX announcement, "Proposed Issue of RMB Shares and Listing of RMB Shares on the STAR Market," May 31, 2026.
- MiniMax HKEX listing timetable announcement, December 31, 2025.
- StockAnalysis 0100.HK historical data, accessed June 2, 2026.
- Investing.com 0100 quote/history snippets, accessed June 2, 2026.

## Related

- [[MiniMax]]
- [[MiniMax M3]]
- [[HKEX]]
- [[STAR Market]]
- [[China AI Tigers]]
