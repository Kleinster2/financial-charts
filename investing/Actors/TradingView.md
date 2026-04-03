---
aliases: [TradingView, tradingview.com]
tags: [actor, fintech, platform, data, charting, private]
---

# TradingView

Financial charting and social trading platform. The most-visited investing website globally, with 100M+ registered users and 200M+ monthly visits.

---

## Quick stats

| Field | Value |
|-------|-------|
| Founded | 2011 |
| HQ | Westerville, Ohio (offices in NYC, London) |
| CEO | Denis Globa (co-founder) |
| Co-founders | Denis Globa, Stan Bokov (CSO), Constantin Ivanov (CTO), Andrew Kirillov (CFO) |
| Employees | ~2,583 (Feb 2026) |
| Users | 100M+ registered; 200M+ monthly visits |
| Revenue | $172.9M (2023) |
| Valuation | $3B (Oct 2021, Series C) |
| Total funding | $339M across 4 rounds |
| Status | Private, no IPO filed |

---

## Product

Web-based charting platform covering equities, FX, crypto, futures, bonds, and economic indicators. Free tier with ads; paid tiers (Pro, Pro+, Premium, Expert) unlock multi-chart layouts, alerts, and server-side alerts.

Pine Script — proprietary scripting language for custom indicators and strategies. v6 released Nov 2024, the largest update since v4 (enums, dynamic requests, runtime logging). Active open-source community with monthly platform updates.

Social layer: users publish chart ideas, follow analysts, comment on setups. The social dimension differentiates it from Bloomberg Terminal or [[Refinitiv]] — TradingView serves retail and semi-professional traders, not institutional desks.

Broker integrations: [[Interactive Brokers]], IG, Saxo, TradeStation, Alpaca, and others. Webhook-based alert system enables automated trading through third-party bridges (TradersPost, Pineify). No native order execution without broker integration.

News feed aggregates [[Reuters]], Benzinga, and other wire services directly into charts.

---

## Funding rounds

| Date | Round | Amount | Lead | Valuation |
|------|-------|--------|------|-----------|
| 2018 | Series A | — | — | — |
| 2019 | Series B | $37M | [[Insight Partners]] | — |
| 2020 | Series C | — | — | — |
| Oct 2021 | Series C extension | $298M | [[Tiger Global]] | $3B |

---

## Competitive landscape

| Platform | Segment | Differentiator |
|----------|---------|----------------|
| TradingView | Retail/semi-pro charting | Social layer, Pine Script, free tier |
| [[Bloomberg]] Terminal | Institutional | Data depth, fixed income, chat |
| [[Refinitiv]] Eikon | Institutional | Reuters data, FX |
| StockCharts | Retail technical analysis | Simpler, education-focused |
| Koyfin | Semi-pro/RIA | Fundamental screening, dashboards |

TradingView's moat is network effects: the social graph of chart ideas and Pine Script community creates switching costs that pure charting tools lack.

---

## Analysis

The $3B valuation dates to October 2021 — four years stale. Revenue was $172.9M in 2023, and the company hasn't raised since, which typically signals either self-funding (profitable or near-profitable on freemium/subscription) or timing a better window. [[Nasdaq]] Private Market has shares trading at ~$2,500/share (Mar 2026), implying a materially higher current valuation.

IPO candidate in the 2026 wave alongside [[SpaceX IPO 2026|SpaceX]], [[Anthropic]], and others — profile fits (high-traffic consumer fintech, recurring revenue, global user base), but no filing yet.

The structural position is aggregator economics. Broker integrations mean [[Interactive Brokers]], IG, Saxo, and others compete for distribution *on TradingView's platform*. The interface layer — visualization and community — is becoming the front door to trading for retail globally. That's the stickiest layer: TradingView doesn't do proprietary data (like [[Bloomberg]]/[[Refinitiv]]), doesn't do execution (like [[Robinhood]]), doesn't do research (like Koyfin). It does the layer where users spend their time, and brokers pay for access to that attention.

Pine Script compounds the lock-in. Users invest time building custom indicators and strategies in a proprietary language — switching costs rise with usage, and the published indicator library attracts new users who attract more broker integrations. Classic two-sided network effect.

Open question: whether the 2026 IPO window opens for them, and what the revenue trajectory looks like post-2023. No public data on profitability.

---

## Vault usage

Referenced across vault notes as a data source for real-time charting:
- [[Credit spreads]] — OAS chart source
- [[JGB]] — JP10Y real-time yield
- [[Market internals framework]] — breadth data ($SPXA200R)
- [[Samsara]], [[Mota-Engil]] — earnings/price source citations

---

## Related

- [[Bloomberg]] — institutional terminal competitor
- [[Refinitiv]] — Reuters-owned data platform
- [[Interactive Brokers]] — key broker integration partner
- [[CBOE]] — options/volatility data feeds
