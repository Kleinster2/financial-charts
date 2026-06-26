---
aliases: [iShares Core Asset Allocation ETFs, iShares Core Allocation ETFs, AOA, AOR, AOM, AOK, S&P Target Risk ETFs, target risk ETFs]
tags: [concept, etf, asset-allocation, multi-asset, ishares]
---

# iShares Core Asset Allocation ETFs

The **iShares Core Asset Allocation ETFs** are a four-fund family from [[iShares]] ([[BlackRock]]) that package a globally diversified stock-and-bond portfolio into a single ticker, each fund holding a fixed target-risk mix. They track the S&P Target Risk index series and sit on one axis — the equity/bond split — from AOK's conservative 30/70 to AOA's aggressive 80/20. All four launched November 2008, charge 0.15% net, and are funds-of-funds built from iShares Core building blocks. Combined assets are ~$9.3B (Jun 2026). Because the only variable across the four is equity weight, they form a clean risk ladder — a ready-made control group for any factor or [[Risk Parity|risk parity]] comparison.

---

## The ladder

![[ishares-allocation-ladder-performance.png]]
*Normalized total return since Jan 2009 (log scale). The four funds fan out monotonically by equity weight: AOA (80/20) +481%, AOR (60/40) +311%, AOM (40/60) +190%, AOK (30/70) +142%. The gradient holds in both directions — more equity means more return and deeper drawdowns. The 2020 COVID V and the 2022 selloff show the same ordering in reverse: AOA fell furthest, AOK least. Equity beta alone explains the spread; nothing crosses.*

---

## The four funds

| Ticker | Sleeve | Target eq/bond | AUM (Jun 2026) | Net ER | Total return since Jan 2009 | CAGR | Latest |
|--------|--------|----------------|----------------|--------|------------------------------|------|--------|
| AOK | Conservative | 30/70 | $786M | 0.15% | +142.1% | 5.2% | $41.36 |
| AOM | Moderate | 40/60 | $1.75B | 0.15% | +190.4% | 6.3% | $49.69 |
| AOR | Balanced | 60/40 | $3.63B | 0.15% | +310.5% | 8.4% | $69.02 |
| AOA | Aggressive | 80/20 | $3.16B | 0.15% | +481.0% | 10.6% | $96.88 |

Each step up the equity ladder added roughly 1.8pp/yr of CAGR over the 17.5-year window — 5.4pp total from AOK to AOA — at the cost of proportionally larger drawdowns. AUM does not follow the risk gradient: the 60/40 AOR ($3.63B) and 80/20 AOA ($3.16B) hold the bulk of assets, while the conservative AOK ($786M) is a quarter of AOR's size. Demand clusters at balanced-to-aggressive, not at capital preservation.

*Prices as of the 2026-06-25 close (4 PM ET); AUM and expense ratios from iShares / stockanalysis.com. Returns use adjusted close (dividends reinvested), measured from the first 2009 session.*

---

## Underlying building blocks

These are funds-of-funds: each holds 9–11 underlying iShares Core ETFs rather than individual securities. The equity sleeve spans US and international, the bond sleeve US and ex-US aggregate:

| Sleeve | Building block | Exposure |
|--------|----------------|----------|
| US large cap | IVV | [[S&P 500]] core |
| Intl developed | IDEV | ex-US developed |
| [[Emerging markets]] | IEMG | EM equity |
| US mid / small | IJH / IJR | size completion |
| US bonds | IUSB | total USD bond market |
| Intl bonds | IAGG | ex-US aggregate, USD-hedged |

In AOA (80/20), IVV alone is ~45% and IDEV ~22%, with bonds (IUSB + IAGG) only ~19%. In AOK (30/70) the weights invert: IUSB ~58%, IAGG ~10%, IVV ~17%. Same seven building blocks, dialed to a different risk point — which is why the four trade as one mechanical family, not four independent bets. The equity sleeve is genuinely global (US + developed + EM + size factors), so these are not the textbook "S&P 500 + AGG" 60/40, but a broader market-cap-weighted world portfolio.

---

## Synthesis

The suite is the investable form of the strategic [[Asset allocation]] decision — the static, set-and-forget counterpart to the tactical firm positioning that note tracks. The fixed stock/bond ratio is also exactly what the [[Stock-Bond Correlation Regime]] governs: when stock-bond correlation is negative, the bond sleeve cushions equity drawdowns (the 60/40 logic); when it flips positive — as in the 2022 inflation shock and the March 2026 stagflation scare — both sleeves fall together and the ladder compresses without re-ordering. A static-allocation fund cannot adapt to that regime change; it is a bet that the long-run diversification holds.

Contrast with [[Risk Parity]]: these funds weight by capital (dollars in stocks vs bonds), so equity risk dominates the portfolio even in the conservative AOK — a 30/70 capital split is still ~80% equity *risk*. Risk parity instead weights by risk contribution and levers bonds up to balance the two. The Core Allocation ladder is the unlevered, capital-weighted baseline against which risk parity's risk-weighted, levered claim is measured.

Because the only axis of variation is equity weight, the four are an ideal monotonic control group for the vault's cluster and correlation work: PC1 should resolve to near-pure equity beta and explain almost all cross-sectional variance, with join distances ordered exactly by the allocation gap. They benchmark the [[SPY]]/[[Treasuries]] two-asset frontier as packaged products.

---

## Related

- [[Asset allocation]] — the strategic/tactical positioning decision these funds package passively
- [[Stock-Bond Correlation Regime]] — governs whether the bond sleeve hedges or compounds equity moves
- [[Risk Parity]] — the risk-weighted, levered alternative to capital-weighted allocation
- [[iShares]] — issuer; [[BlackRock]] — parent
- [[SPY]] — the US large-cap core (IVV) inside the equity sleeve
- [[Treasuries]] — the rate exposure inside the bond sleeve; [[TLT]] is the long-duration extreme

---

## Log

| Date | Entry | Source |
|------|-------|--------|
| 2026-06-26 | Created. Backfilled AOA + AOK price history (completing the four-fund ladder; AOM/AOR re-pulled to fill 729-row gaps each and align to an adjusted-close basis — all four now 4,395 rows in the 2009-01-01→2026-06-24 window). Documented suite structure, AUM ($9.3B combined), 0.15% net ER, underlying iShares Core building blocks, and the 2009–2026 total-return ladder (AOA +481% / AOK +142%). Generated and embedded the ladder chart. | iShares, stockanalysis.com, market_data.db |
