---
aliases:
  - sentiment indicators
  - fear and greed
  - Fear and Greed Index
  - CNN Fear and Greed
  - investor sentiment
  - market sentiment
tags:
  - concept
  - macro
  - indicator
  - contrarian
---

# Market Sentiment Indicators

The collective toolkit for measuring what investors feel, as opposed to what they own or what the fundamentals say. The core premise, validated by six decades of data: extreme sentiment readings are contrarian signals — peak fear precedes rallies, peak greed precedes selloffs. The challenge is that sentiment can stay extreme longer than portfolios can stay solvent, and no single indicator captures the full picture.

---

## Synthesis

The sentiment indicator universe divides into three fundamentally different data sources: what people say (surveys), what the market prices (volatility and options), and what money actually does (flows and positioning). Each has blind spots the others fill. Survey-based measures like [[AAII]] and [[Investors Intelligence]] capture retail and advisor psychology but update weekly and sample narrow populations. Market-derived measures like [[VIX]] and put/call ratios react in real time but can't distinguish rational hedging from panic. Positioning data like [[CFTC]] Commitment of Traders and [[NAAIM]] show actual money movement but lag by days. The academic consensus since Baker & Wurgler (2006) is that sentiment has its strongest predictive power on hard-to-value, hard-to-arbitrage securities — small caps, unprofitable companies, extreme-growth stocks — precisely where the gap between price and fundamental value is widest.

The practical question is convergence: when multiple independent indicators from different data sources simultaneously flash extreme readings, the signal strengthens. March 2020 is the cleanest modern example — [[CNN]] Fear & Greed hit 2 (near-zero), AAII bearish hit record territory, VIX closed at an all-time high of 82.69, and the CBOE equity put/call ratio spiked to 1.28, all within the same week. The [[S&P 500]] bottomed on March 23, 2020 and doubled within 18 months. But convergence also appeared in October 2008, and buying that signal meant enduring another five months of drawdown before the March 2009 bottom. Sentiment tells you *where* you are in the cycle. It does not tell you *when* the turn comes.

---

The story of market sentiment measurement is the story of a slow, grudging acceptance that crowds are informative — just not in the way they think.

The oldest continuous dataset is [[Investors Intelligence]], launched in 1963 by Abe Cohen of Chartcraft. Cohen started surveying independent newsletter writers thinking their consensus would confirm trend direction — if most advisors were bullish, the market was probably going up. The opposite turned out to be true. Advisors were "almost always wrong at major market turning points," and the survey became the first widely used contrarian indicator. Only four editors have classified the newsletters in 63 years, and just two since 1982, giving the data unusual consistency. The key thresholds crystallized over decades: bullish readings above 55% signal excessive optimism, bearish readings above 55% mark capitulation zones. In 1990, seven consecutive readings above 55% bearish coincided with the recession bottom — the [[S&P 500]] rallied 25.6% over the following year.

The [[AAII]] Sentiment Survey arrived in 1987, extending sentiment measurement to individual investors. The methodology is straightforward: AAII members vote weekly on whether they're bullish, bearish, or neutral on stocks over the next six months. The sample skews affluent (over half hold portfolios above $500,000), male, and educated — this is the upper echelon of hands-on retail, not the general public. Historical averages run 38% bullish, 31.5% neutral, 30.5% bearish. The extremes are where the signal lives. On March 5, 2009 — days before the generational bottom — bearish sentiment hit 70.3%, the all-time record. AAII's own analysis of such extremes: when bearish readings exceed three standard deviations above average, the average six-month S&P 500 return is +25.8%, and the average twelve-month return is +35.0%. The survey also caught the other side: on August 21, 1987, bearish sentiment fell to 6.0% (record low pessimism), and the October 1987 crash arrived less than two months later.

Volatility-derived sentiment measurement began with the [[VIX]], announced by the [[CBOE]] on January 19, 1993. Robert Whaley of Duke developed the original formula using [[S&P 100]] at-the-money options; a 2003 overhaul by CBOE and [[Goldman Sachs]] switched to [[S&P 500]] options across a wide strike range, measuring expected 30-day volatility. The VIX doesn't ask what anyone thinks — it reads what they're paying for protection. The all-time closing high of 82.69 on March 16, 2020 and the intraday peak of 89.53 on October 24, 2008 mark the two moments of maximum market terror in the index's history. Forward return data after extreme spikes is striking: when VIX closes above ~47, the 360-day S&P 500 return has been positive 100% of the time since 1990, averaging +35.3%. The bond market's equivalent, the [[MOVE Index]], was created by Harley Bassman at [[Merrill Lynch]] in 1994 and now lives at [[ICE]]. It measures implied volatility from Treasury options at four maturities (2Y, 5Y, 10Y at double weight, 30Y). MOVE often spikes before VIX — the bond market sends earlier warnings. Its all-time peak of 264.6 on October 10, 2008 preceded VIX's peak by two weeks.

Options flow adds a separate dimension. The [[CBOE]] publishes three daily put/call ratios: equity-only (the purest retail sentiment read), index-only (structurally biased by institutional hedging), and total. The equity ratio's average since 2007 is ~0.94. Readings above 1.0 mean put volume exceeds call volume — bearish sentiment that contrarian logic reads as bullish. Readings below 0.72 mark excessive call buying — greed territory. In March 2020, the equity put/call ratio spiked to 1.28, confirming what VIX and the surveys were showing. The structural caveat: zero-commission trading and the explosion of 0DTE options since 2020 have altered the signal's baseline. Historical thresholds may need recalibration.

Positioning data reveals what money is doing rather than what mouths are saying. The [[CFTC]] Commitment of Traders report traces back to 1924 (when the USDA published early versions) and has been weekly since the 1960s. Tuesday positions, released Friday at 3:30 PM ET. The disaggregated format (since 2009) separates producers, swap dealers, managed money, and other reportables — the managed money category is the speculative positioning read. Extreme net long or short positions in managed money historically precede reversals. The [[NAAIM]] Exposure Index (since 2006) takes a different cut: actual equity exposure reported by active investment managers every Wednesday, scaled from -200% (leveraged short) to +200% (leveraged long). Unlike surveys, this reflects real allocations, not opinions.

Composites attempt to synthesize multiple signals into single readings. [[CNN]]'s Fear & Greed Index, launched in spring 2012, equally weights seven components: S&P 500 momentum vs its 125-day moving average, NYSE 52-week highs vs lows, McClellan Volume Summation (advancing vs declining volume), put/call ratio, VIX, stock vs Treasury return spread, and junk bond yield spread. Scale: 0 (extreme fear) to 100 (extreme greed). Despite being a media product, its track record at extremes is notable — it hit 2 on both March 12 and March 23, 2020, the latter being the exact S&P 500 bottom. The [[Bank of America]] Bull & Bear Indicator combines hedge fund positioning, credit technicals, equity breadth, equity and bond flows, and leveraged positioning into a 0-10 scale. Readings above 8 trigger sell signals, below 2 trigger buys. Since 2002, 16 sell signals have been triggered with an accuracy rate of ~63%. In January 2026, it hit 9.4-9.6 — the highest in 20+ years — alongside record-low cash levels (3.2%) and record equity overweights among fund managers.

The academic grounding came in 2006 with Baker and Wurgler's landmark "Investor Sentiment and the Cross-Section of Stock Returns" in the Journal of Finance. They constructed a composite from six proxies: closed-end fund discount, share turnover, IPO count, first-day IPO returns, dividend premium, and equity share of new issues. The key finding reshaped how institutions think about sentiment: its predictive power is strongest on hard-to-value and hard-to-arbitrage stocks. When beginning-of-period sentiment is high, subsequent returns on speculative stocks (small, young, high-volatility, unprofitable, non-dividend-paying) are relatively low. When sentiment is low, those same stocks earn relatively high subsequent returns. The effect is weaker on large, profitable, dividend-paying companies — precisely because they're easier to value and arbitrage. De Long, Shleifer, Summers, and Waldmann (1990) had provided the theoretical framework: irrational noise traders create real pricing risk that rational arbitrageurs cannot fully eliminate. Tetlock (2007) extended the empirical work to media, finding that high pessimism in the Wall Street Journal's daily market column predicted downward price pressure followed by reversion to fundamentals.

The crypto market developed its own sentiment infrastructure. The Crypto Fear & Greed Index (Alternative.me, since February 2018) measures [[Bitcoin]] and broader crypto sentiment through six weighted components: BTC volatility (25%), market momentum and volume (25%), social media engagement (15%), polling surveys (15%), Bitcoin dominance (10%), and Google Trends (10%). The Bitcoin dominance component captures a crypto-specific dynamic: rising BTC dominance means money fleeing speculative altcoins into the relative safety of Bitcoin — a fear signal. Falling dominance means risk appetite pushing into smaller tokens — greed.

The limitations are real and recurring. Timing is the central problem — extreme sentiment identifies zones of opportunity or danger but not the exact reversal point. The noise trader risk framework (De Long et al.) explains why: irrational sentiment can push prices far from fundamentals before mean-reverting, and betting against the crowd prematurely is how many contrarians go broke. Survey frequency constrains responsiveness — AAII updates weekly, BofA monthly, while markets move by the minute. Sample bias is endemic: AAII polls affluent members, Investors Intelligence polls newsletter writers, NAAIM polls active managers. None captures the full investor population. And structural market changes — passive indexing flows, algorithmic trading, the zero-commission 0DTE options explosion — continuously alter signal baselines. The most reliable approach, confirmed by both academic research and practitioner experience, is multi-indicator convergence: when surveys, volatility, options flow, and positioning simultaneously flash extreme readings from independent data sources, the signal's reliability increases substantially. Single-indicator extremes are noise. Convergence across categories is signal.

---

## Reference

### Indicator taxonomy

| Category | Indicator | Publisher | Frequency | History |
|----------|-----------|-----------|-----------|---------|
| Survey | [[AAII]] Sentiment Survey | AAII | Weekly (Thu) | 1987 |
| Survey | [[Investors Intelligence]] Advisors Sentiment | Chartcraft | Weekly | 1963 |
| Survey | [[Consumer sentiment\|UMich Consumer Sentiment]] | Univ. of Michigan | Monthly | 1952 |
| Survey | Conference Board Consumer Confidence | [[Conference Board]] | Monthly | 1967 |
| Volatility | [[VIX]] | [[CBOE]] | Real-time | 1993 (calc back to 1986) |
| Volatility | [[MOVE Index]] | [[ICE]]/BofA | Daily | 1988 |
| Options | CBOE Equity Put/Call Ratio | [[CBOE]] | Daily | ~2006 |
| Positioning | CFTC Commitment of Traders | [[CFTC]] | Weekly (Fri) | 1962 (weekly) |
| Positioning | [[NAAIM]] Exposure Index | NAAIM | Weekly (Wed) | 2006 |
| Composite | CNN Fear & Greed Index | [[CNN]] | Daily | 2012 |
| Composite | Bull & Bear Indicator | [[Bank of America]] | Monthly | 2002 |
| Crypto | Crypto Fear & Greed Index | Alternative.me | Daily | 2018 |

### CNN Fear & Greed components

| # | Component | What it measures | Contrarian logic |
|---|-----------|-----------------|-----------------|
| 1 | Market Momentum | S&P 500 vs 125-day MA | Below MA = fear |
| 2 | Stock Price Strength | NYSE 52-wk highs vs lows | Net new lows = fear |
| 3 | Stock Price Breadth | McClellan Volume Summation | Declining volume dominance = fear |
| 4 | Put/Call Options | Put vs call volume | High put/call = fear |
| 5 | Market Volatility | VIX vs 50-day MA | Elevated VIX = fear |
| 6 | Safe Haven Demand | Treasury vs stock returns (20 days) | Treasuries outperforming = fear |
| 7 | Junk Bond Demand | Junk vs investment-grade spread | Widening spread = fear |

### Contrarian signal track record

| Date | Indicator(s) | Reading | S&P 500 outcome |
|------|-------------|---------|----------------|
| Aug 1987 | AAII bearish | 6.0% (record low bearish) | Oct 1987 crash within 2 months |
| Oct 1990 | AAII bearish | 67% | +25.6% over 12 months |
| 1999 | Investors Intelligence bulls | >60% | Dot-com crash 2000-2002 |
| Mar 5, 2009 | AAII bearish | 70.3% (all-time record) | +39.5% (6mo), +56.9% (12mo) |
| Mar 16, 2020 | VIX | 82.69 (all-time close) | Bottom 5 trading days later |
| Mar 23, 2020 | CNN F&G | 2 (near-zero) | Exact S&P 500 bottom. +100% in 18mo |
| Mar 2020 | CBOE equity P/C | 1.28 | Coincided with bottom |
| Feb 2018 | BofA Bull & Bear | 9.4 | -10-12% in 9 days (Volmageddon) |
| Feb 2020 | BofA Bull & Bear | >8 (sell) | -30%+ within weeks (COVID) |
| Jan 2026 | BofA Bull & Bear | 9.4-9.6 (20-yr high) | Record-low cash (3.2%), record equity overweight |

### Academic foundations

| Paper | Finding |
|-------|---------|
| De Long, Shleifer, Summers & Waldmann (1990), JPE | Noise traders affect prices and earn excess returns; rational arbitrage cannot fully eliminate sentiment-driven mispricings |
| Baker & Wurgler (2006), JF | Sentiment predicts cross-sectional returns — strongest on small, young, volatile, unprofitable stocks. High sentiment → low subsequent returns on speculative stocks |
| Baker & Wurgler (2007), JEP | Sentiment is measurable and has "clearly discernible, important, and regular effects" on firms and markets |
| Tetlock (2007), JF | Media pessimism predicts downward price pressure followed by fundamental reversion; extreme pessimism predicts high volume |
| Ben-Rephael, Kandel & Wohl (2012), JFE | Mutual fund flow sentiment relates to ~1.95% of market excess return; 85% reverses within 4 months |

### Key limitations

| Limitation | Detail |
|-----------|--------|
| Timing gap | Identifies zones, not turns. Extreme sentiment can persist for months before reversal. |
| Rational vs irrational | Cannot distinguish panic from legitimate fundamental reassessment. |
| Survey frequency | Weekly (AAII) or monthly (BofA) — markets move faster. |
| Sample bias | AAII: affluent members. II: newsletter writers. NAAIM: active managers. None captures full investor population. |
| Structural shifts | 0DTE options, passive flows, algorithmic trading alter historical baselines. |
| Single-indicator noise | Any one indicator at extremes has limited reliability. Multi-indicator convergence is required. |
| Accuracy | BofA Bull & Bear sell signals: ~63% accuracy. Far from infallible. |

---

## Related

- [[VIX]] — the core volatility-derived fear gauge, one component of CNN Fear & Greed
- [[VIX ETPs]] — tradeable VIX products and their structural decay
- [[Market internals framework]] — orthogonal indicator framework (breadth, concentration, fear, credit)
- [[Consumer sentiment]] — UMich and Conference Board household surveys (macro, not market-specific)
- [[S&P 500]] — the index most sentiment indicators reference
- [[CBOE]] — publisher of VIX, put/call ratios, SKEW
