---
name: Hawkish Warsh Fed / rates
type: report
topic: "[[Rate expectations]]"
lens: neutral
deepdive: false
generated: 2026-06-23 20:22
sources_read: 9
tags: [report]
---

# Hawkish Warsh Fed — the market hired a dove and got orthodoxy

The most consequential repricing of 2026 is not in any chip — it is in the identity of the Fed reaction function, and Jun 23 is the equity market paying the bill for getting it wrong. The vault's [[Kevin Warsh]] note still carries the January framing: "Goldilocks," "dovish views align with Trump's rate preferences," "aligning with Trump on rate cuts." The Warsh who actually arrived, per the [[Rate expectations]] note's own Jun 22 update and the analyst tape, dropped the Fed's easing bias at his first meeting. [[Ed Yardeni]] said he was "blown away," having expected a dove and instead hearing "a strict, orthodox message on inflation with a strong commitment to price stability." That gap — between the dove the market underwrote for months and the hawk it got — is the engine under the selloff. When the longest-duration, most rate-sensitive asset class falls 8% ([[SOXX]] −7.88%) while staples rise nearly 2% (XLP +1.87%) in the same session, the move is not a technology story. It is a discount-rate story wearing a technology costume.

The inflation floor underneath the hawkishness is real, not rhetorical, and that is the binding constraint. The [[Rate expectations]] note documents the May 12 CPI regime break — headline 3.8% year-on-year, the hottest since 2023, with energy driving more than 40% of the monthly rise through the [[2026 Strait of Hormuz crisis]]. The Jun 17 SEP then ratified it: the median 2026 funds-rate dot moved from 3.4% to 3.8%, the core-PCE dot from 2.7% to 3.3%, and nine of eighteen dots now pencil hikes by year-end. [[Ed Yardeni|Yardeni]]'s call is a July hike; the selloff coverage prices a second by December. This is the clean inversion of the entire 2024-25 setup — for two years the risk to the AI trade was that the Fed would not cut fast enough; now the risk is that it hikes. The note's own phrase for the regime is the sharpest one available: a "hike-bias hold" with "a chair actively validating it rather than just a hot CPI print forcing it."

The history vault carries the precedent this rhymes with. The [Central Banking](obsidian://open?vault=history&file=Central%20Banking) and [1973 Oil Crisis](obsidian://open?vault=history&file=1973%20Oil%20Crisis) notes describe an energy-shock inflation that forces a reluctant central bank into orthodoxy against political pressure for ease — the structural shape of the current setup. The disanalogy is the politics: Warsh is tightening into a [[Trump II|Trump]] administration that wants cuts before the midterms, which is why the [[Rate expectations]] note frames the live question not as "will he hike" but as whether a Warsh Fed can keep the long end contained while refusing to validate the administration's preference for cuts. The [[Greenspan put]] tension [[Martin Sandbu]] flagged in January — Warsh's "tough love" instinct against the market's expectation of a bailout — is now being tested in real time. Jun 23 is the first sizable drawdown of his chairmanship, and whether he blinks is the [[Fed independence]] question made tradeable.

The AI selloff is the invoice for a mispriced Fed chair: the market spent 2026 pricing the dove Warsh was supposed to be, and Jun 23 is the first installment of repricing the hawk he turned out to be.

## Other vault references

- [[Kevin Warsh]] — the chair; the note's "Policy views" framing predates the hawkish debut and is stale
- [[Federal Reserve]] / [[Fed independence]] — the institution and the political-pressure axis the regime turns on
- [[Nasdaq semiconductor selloff June 2026]] — the equity expression of the hike-bias regime
- [[Ed Yardeni]] — the July-hike call and the "blown away" reaction to Warsh's orthodoxy
- [[2026 Strait of Hormuz crisis]] — the energy shock feeding the headline CPI that floors the easing path
- [[Greenspan put]] — the bailout-expectation tension Warsh's instinct cuts against
- [Central Banking](obsidian://open?vault=history&file=Central%20Banking) / [1973 Oil Crisis](obsidian://open?vault=history&file=1973%20Oil%20Crisis) — the energy-shock-forces-orthodoxy precedent

## Gaps

- [[Kevin Warsh]] "Policy views" table is stale — it still reads dovish / aligned-with-Trump-on-cuts; the actual hawkish debut, the [[Ed Yardeni|Yardeni]] reaction, and the Jun 17 SEP dots need folding in via `/ingest` or `/deepdive`.
- [[Rate expectations]] last contract snapshot is May 13; the Jun 17 FOMC SEP is not yet a dated entry — a refresh via `fed_rate_expectations.py` plus the SEP dot table would update the implied path.
- [[Kevin Hassett]] — the road not taken ("cut early, cut often"); the counterfactual sharpens how large the Warsh surprise was.
