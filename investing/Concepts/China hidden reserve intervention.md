---
aliases:
  - China hidden FX intervention
  - China backdoor intervention
  - China shadow reserves
  - Chinese hidden reserves
tags: [concept, macro, china, fx, reserves, capital-flows]
---

# China hidden reserve intervention

China hidden reserve intervention is the problem of measuring [[China]]'s foreign-exchange management when dollar buying no longer shows up cleanly as [[PBOC]] official reserve accumulation. The operative claim is not that one official series proves intervention; it is that [[State Administration of Foreign Exchange]] (SAFE) settlement data, state-bank foreign assets, domestic FX deposits, and the PBOC balance sheet have to be read together.

---

## Synthesis

[[Brad Setser]]'s June 2026 update turns the China reserve question from a simple "why are official reserves flat?" puzzle into a state-financial-system accounting problem. If exporters and domestic firms keep foreign currency as deposits, those dollars can become funding for state banks' external assets without ever becoming reported PBOC reserves. If firms actually sell dollars for renminbi, but the PBOC balance sheet does not expand, the corresponding foreign asset may still sit elsewhere in the banking system. Either way, the official reserve line understates the currency-management footprint (per Setser).

The important market point is measurement, not motive. China's visible [[Treasuries]] holdings have fallen and official reserves have looked stable, but Setser's combined proxy says state institutions may still be absorbing very large foreign-currency flows. That makes "[[De-dollarization]]" too blunt a label: the portfolio may be moving away from clean PBOC-reported Treasury reserves while still preserving a large dollar-asset stock through state banks, deposits, and settlement gaps (inference).

Chart data note: the charts below are source-preserved CFR charts, not local market-data charts. The underlying SAFE/PBOC banking series are not yet in `market_data.db`, so local chart data is unavailable until those official series are ingested.

---

## Mechanics

| Channel | What it measures | Why it matters |
|---|---|---|
| PBOC official reserves | Visible central-bank FX stock | Cleanest official series, but it can miss assets held outside the central-bank balance sheet |
| SAFE settlement | Banks' FX purchases and sales against renminbi | Captures conversion flows, but not simple retention of foreign currency as deposits |
| Domestic FX deposits | Dollars and other FX held by firms, households, and financial institutions in China's banking system | Can fund state-bank foreign assets without first becoming reported PBOC reserves |
| State commercial banks' net foreign assets | External assets and liabilities on state-bank balance sheets | Possible warehouse for intervention-like accumulation outside official reserves |
| Treasury TIC data | Public U.S. data on foreign holdings of U.S. securities | Useful for visible holder/custodian trends, but incomplete if China shifts through banks, custodians, or non-Treasury assets |

---

## Setser's June 2026 Update

Setser's June 4 2026 CFR post, "Scaling China's Hidden Intervention In the Foreign Exchange Market," pushes against the narrow reading that the rise in state-bank foreign assets is fully explained by domestic FX deposits. The PBOC's defense, as Setser describes it, is that state banks are simply matching domestic foreign-currency deposits with foreign assets. Setser's counter is that this does not eliminate the intervention question; it moves the accounting problem. If domestic deposits explain the state-bank asset rise, the unexplained SAFE settlement flows still need another balance-sheet home.

His broader proxy combines official reserves, the settlement gap, domestic FX deposits, and state-bank net foreign assets. The resulting upper-bound frame suggests Chinese state institutions may have added roughly $700B of foreign assets over the prior 12 months. Treat that number as a public-data reconstruction, not an official disclosure. The durable value is the framework: the currency-management footprint is larger than the reported PBOC reserve line.

---

## Source Chart Packet

![[china-hidden-reserve-intervention-onshore-fx-deposits-by-sector.png]]
*Onshore FX deposits by sector; Setser/CFR, Jun. 4 2026. Preserved as source chart.*

![[china-hidden-reserve-intervention-chart-2.png]]
*Domestic FX deposits stock; Setser/CFR, Jun. 4 2026. Preserved as source chart.*

![[china-hidden-reserve-intervention-domestic-fx-deposits-vs-loans.png]]
*Domestic FX deposits versus loans; Setser/CFR, Jun. 4 2026. Preserved as source chart.*

![[china-hidden-reserve-intervention-usd-cny-rate-differentials.png]]
*USD/CNY rate differentials and deposit behavior; Setser/CFR, Jun. 4 2026. Preserved as source chart.*

![[china-hidden-reserve-intervention-settlement-proxy-vs-yuan.png]]
*Settlement proxy versus yuan pressure; Setser/CFR, Jun. 4 2026. Preserved as source chart.*

![[china-hidden-reserve-intervention-pboc-settlement-deposits-sum-chart-10.png]]
*PBOC reserve and settlement/deposit sum, first variant; Setser/CFR, Jun. 4 2026. Preserved as source chart.*

![[china-hidden-reserve-intervention-pboc-settlement-deposits-sum-chart-11.png]]
*PBOC reserve and settlement/deposit sum, second variant; Setser/CFR, Jun. 4 2026. Preserved as source chart.*

![[china-hidden-reserve-intervention-fx-flows-including-deposits.png]]
*FX flows including deposits; Setser/CFR, Jun. 4 2026. Preserved as source chart.*

![[china-hidden-reserve-intervention-reserves-gap-deposits-stock.png]]
*Reserve gap and deposit stock; Setser/CFR, Jun. 4 2026. Preserved as source chart.*

![[china-hidden-reserve-intervention-pboc-vs-safe-settlement-cumulative.png]]
*PBOC versus SAFE settlement, cumulative view; Setser/CFR, Jun. 4 2026. Preserved as source chart.*

![[china-hidden-reserve-intervention-pboc-vs-safe-settlement-2000-2010.png]]
*PBOC versus SAFE settlement, 2000-2010 benchmark; Setser/CFR, Jun. 4 2026. Preserved as source chart.*

![[china-hidden-reserve-intervention-settlement-plus-state-bank-nfa.png]]
*Settlement plus state-bank net foreign assets; Setser/CFR, Jun. 4 2026. Preserved as source chart.*

![[china-hidden-reserve-intervention-chart-18.png]]
*Upper-bound hidden-intervention stock using state-bank net foreign assets and cumulative settlement; Setser/CFR, Jun. 4 2026. Preserved as source chart.*

---

## Why It Matters

- China's current-account and trade-surplus accounting can understate the amount of surplus dollar absorption happening inside the state financial system.
- RMB pressure is better read through a basket of settlement, deposit, state-bank, and reserve series than through the PBOC official reserve line alone.
- TIC-visible Treasury selling does not by itself prove China is abandoning dollars; assets may shift through custodians, state banks, or non-Treasury dollar instruments.
- U.S. currency-manipulation surveillance becomes a transparency problem: the key question is where surplus dollars are parked, not only whether PBOC reported reserve accumulation.
- The note separates [[Dollar reserve status erosion]] from reserve opacity. A less visible dollar stock is not the same thing as a smaller dollar stock.

---

## Related

- [[Brad Setser]]
- [[PBOC]]
- [[State Administration of Foreign Exchange]]
- [[China]]
- [[US-China finance]]
- [[China trade]]
- [[De-dollarization]]
- [[Dollar reserve status erosion]]
- [[Treasury International Capital]]
- [[Treasuries]]
- [[Global imbalances]]
- [[Chinese yuan]]

---

## Sources

- Brad Setser, CFR, "Scaling China's Hidden Intervention In the Foreign Exchange Market," Jun. 4 2026: https://www.cfr.org/articles/scaling-chinas-hidden-intervention-in-the-foreign-exchange-market
- U.S. Treasury, January 2026 FX report press release: https://home.treasury.gov/news/press-releases/sb0373
- SAFE official website: https://www.safe.gov.cn/en/
