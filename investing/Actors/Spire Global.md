---
aliases: [SPIR, Spire, NanoSatisfi]
tags:
  - actor
  - satellite
  - defense
  - weather
  - usa
  - public
---

**Spire Global** — space-to-cloud data and analytics company operating the second-largest commercial satellite constellation (~110 LEMUR-2 CubeSats). Collects weather, RF, and aviation data via multi-sensor LEO satellites and sells it as recurring subscriptions to government agencies and commercial customers.

---

## Sector correlation

> [!warning] Sector Orphan
> SPIR does not trade tightly with any sector ETF (max r = 0.48 with KRE).

| Sector | ETF | Correlation |
|--------|-----|-------------|
| [[Banks\|Regional Banks]] | KRE | 0.48 |
| Technology | XLK | 0.45 |
| Software | IGV | 0.44 |
| *S&P 500* | *SPY* | *0.39* |

SPIR trades between Regional Banks and Technology without a tight sector fit.

---

## The story

Founded in 2012 as NanoSatisfi by three [[International Space University]] graduates — Peter Platzer (Austrian, ex-quant at [[Deutsche Bank]]/[[Rohatyn Group]]), Jeroen Cappaert, and Joel Spark — who saw that CubeSats could democratize Earth observation data. The bet: mass-produce cheap multi-sensor nanosats, collect proprietary atmospheric and RF data at global scale, and sell it as cloud-delivered subscriptions rather than one-off imagery contracts.

The company went public via SPAC merger with NavSight Holdings in August 2021 at a $1.6B valuation with a $245M PIPE. Post-SPAC reality was painful — shares fell from ~$10 to under $2 by 2024 as losses mounted and growth disappointed. The pivot came in 2025: Spire sold its maritime AIS business (originally [[exactEarth]], acquired 2021) to Kpler for ~$233.5M, wiped out all debt, and refocused on three verticals — weather, space services, and aviation.

By Q4 2025, ex-maritime revenue was growing 44% YoY, gross margins were expanding, and the company guided to EBITDA breakeven by Q4 2026 / Q1 2027. Three sensor breakthroughs in early 2026 — HyMS (hyperspectral microwave sounder) first light, single-satellite RF geolocation, and a diamond quantum magnetometer for the [[NGA]] — repositioned Spire as a multi-domain ISR platform, not just a weather data vendor. The $151B [[MDA]] SHIELD IDIQ (Dec 2025) and $237M [[Space Force]] STEP 2.0 IDIQ gave it contracting vehicles for [[Golden Dome]] and broader defense work. The stock recovered from $6.60 to $16 in six months.

---

## Why it matters

Spire sits at the intersection of three accelerating trends: proliferated LEO constellations, software-defined defense, and commercial weather data procurement. Its multi-sensor approach (GNSS-RO + AIS + ADS-B + RF geolocation + HyMS + magnetometer on the same buses) is unique among commercial operators — competitors specialize in one domain. The single-satellite RF geolocation capability demonstrated in March 2026 is a direct challenge to [[HawkEye 360]]'s multi-satellite approach. Government contract vehicles (SHIELD, STEP 2.0) position Spire as a sensor/data layer for missile defense and space domain awareness without the capital intensity of building interceptors.

---

## Key stats

| Metric | Value |
|--------|-------|
| Ticker | SPIR ([[NYSE]]) |
| Market cap | ~$556M (Apr 2026) |
| Shares outstanding | ~33.5M |
| Revenue (FY 2025) | $71.6M |
| Revenue growth (ex-maritime) | +44% YoY (Q4 2025) |
| GAAP gross margin | 41% (Q4), non-GAAP 43-44% |
| Net income (FY 2025) | $51.3M (includes maritime sale gain) |
| Adj. EBITDA (FY 2025) | $(39.7)M |
| Cash + marketable securities | $81.8M (Q4 2025) |
| Debt | $0 |
| Employees | ~505 (Feb 2026) |
| Constellation | ~110 LEMUR-2 CubeSats (LEO, sun-synchronous, 400-600 km) |
| 52-week range | $6.60 - $16.14 |
| Went public | Aug 2021 (SPAC, NavSight Holdings, $1.6B valuation) |
| CEO | Theresa Condor (Jan 2025; previously COO, founding team) |
| Executive Chairman | Peter Platzer (founder) |
| HQ | Vienna, Virginia |

---

## 2026 guidance

| Metric | Q1 2026 | FY 2026 |
|--------|---------|---------|
| Revenue | $14.5-15.5M | $75-85M |
| Adj. EBITDA | $(11.5)M to $(11.2)M | $(26)M to $(20.7)M |
| Revenue growth (ex-maritime) | — | ~50% YoY |
| EBITDA breakeven | — | Q4 2026 to Q1 2027 |
| Long-term gross margin (3-5yr) | — | 60-70% |

75% of 2026 low-end guidance covered by existing contracts. WildFireSat revenue excluded. Q1 includes $1.7M residual maritime revenue.

---

## Business segments

### Weather (GNSS radio occultation)

Collects atmospheric profiles (temperature, humidity, pressure) via GPS radio occultation using STRATOS sensors. Data feeds directly into numerical weather prediction models.

| Customer | Contract value | Period |
|----------|---------------|--------|
| [[NOAA]] | $11.2M | 2025 (1-year) |
| [[NOAA]] (ocean winds) | $2.5M | 2025 |
| [[EUMETSAT]] | EUR 3M | 2025 renewal |
| [[NASA]] (CSDAP) | Ongoing | — |

### Space services (satellite-as-a-service)

Hosts third-party payloads on Spire's buses. Customers get orbit access without building their own satellites.

| Contract | Agency | Value | Details |
|----------|--------|-------|---------|
| STEP 2.0 IDIQ | [[Space Force]] (Space Systems Command) | $237M shared ceiling (10-year) | One of 12 awardees. Experimental payload hosting. |
| WildFireSat | [[Canadian Space Agency]] | CAD $72M (~$50.4M) | 10-satellite wildfire constellation with [[OroraTech]]. Launch 2029. Currently paused. |

### Aviation (ADS-B)

Global aircraft tracking for aviation safety, search-and-rescue, and flight planning.

---

## Sensor breakthroughs (early 2026)

### HyMS first light (Mar 12, 2026)

Hyperspectral Microwave Sounder demonstrator returned first data. 1,000+ sensing channels across water vapor and temperature bands. Complements existing GNSS-RO to provide the most complete atmospheric profiling from a commercial constellation. First-of-kind compact form factor.

### Single-satellite RF geolocation (Mar 24, 2026)

Detected and geolocated S-band and X-band signals from a single satellite — traditionally requires multiple satellites in formation. Capabilities now span VHF through X-band. Co-funded by [[Luxembourg]]/[[ESA]]. Direct defense/GEOINT application. Management plans 15x RFGL capacity expansion over the next 12 months.

### NGA MagQuest magnetometer (Apr 1, 2026)

Diamond quantum magnetometer ([[SBQuantum]] partnership) deployed on [[SpaceX]] Transporter-16. High-precision geomagnetic mapping for [[NGA]]. GPS-resilient navigation alternative. Results expected late 2026; permanent acquisition capability targeted for 2030.

---

## Defense positioning

| Contract | Value | Relevance |
|----------|-------|-----------|
| [[MDA]] SHIELD IDIQ | $151B shared ceiling (10-year, Dec 2025) | [[Golden Dome]] contracting framework. Spire competes for task orders as sensor/data layer. |
| STEP 2.0 IDIQ | $237M ceiling (10-year, May 2025) | Experimental payload hosting for [[Space Force]]. |
| SHIELD significance | — | Among ~2,100 awardees. Positions Spire for missile defense data/tracking requirements. |

Spire's RF geolocation, weather, and multi-sensor capabilities are directly applicable to maritime domain awareness in the [[Persian Gulf]] context ([[2026 Strait of Hormuz crisis]]). The connection is structural (capability match + contract vehicle) rather than announced.

---

## Maritime divestiture

Sold maritime AIS business (originally [[exactEarth]], acquired 2021) to [[Kpler]] for ~$233.5M + $7.5M services agreement. Closed April 2025. [[CMA]] (UK) cleared July 2025. Proceeds eliminated all debt. Spire retains AIS data collection capability but Kpler handles maritime analytics.

---

## Satellite constellation

| Attribute | Value |
|-----------|-------|
| Fleet size | ~110 LEMUR-2 CubeSats |
| Orbit | Sun-synchronous LEO, 400-600 km |
| Sensors per bus | GNSS-RO (STRATOS), AIS (SENSE), ADS-B, RF geolocation, HyMS, magnetometer |
| Recent launch | 10 sats on [[SpaceX]] Transporter-16 (Mar 30, 2026) |
| Rank | Second-largest commercial constellation; largest by number of distinct sensor types |

Offices: Vienna VA, San Francisco, Boulder, Washington DC, Glasgow, Luxembourg, Munich, Singapore, Cambridge (Ontario). ~505 employees across 9 locations.

---

## Competition

| Company | Ticker | Focus | Differentiation vs. Spire |
|---------|--------|-------|---------------------------|
| [[Planet Labs]] | PL | Optical Earth imaging (3m daily global) | Imagery, not RF/weather. ~200+ sats. |
| [[Maxar]] | Private ([[Advent International]]) | High-res optical/radar | Higher resolution (30cm), fewer sats, defense-heavy. |
| [[BlackSky]] | BKSY | Real-time geospatial intelligence | Optical + AI analytics. Smaller constellation. |
| [[HawkEye 360]] | Private | RF signal detection/geolocation | Most direct RF competitor. Multi-satellite geolocation (Spire now doing single-sat). |
| [[Tomorrow.io]] | Private | Weather intelligence | Weather-focused. Own constellation + radar. |
| GeoOptics | Private | GNSS-RO weather data | Direct weather data competitor. Smaller scale. |

Spire's differentiation: multi-sensor on same buses, government contract vehicles (SHIELD, STEP 2.0), single-satellite RF geolocation, and HyMS — none replicated by competitors.

---

## Analyst coverage

| Analyst | Firm | Rating | Price target |
|---------|------|--------|-------------|
| Erik Rasmussen | [[Stifel]] | Buy | $16 |
| Scott Buck | [[HC Wainwright]] | Buy | $19 |
| Austin Moeller | [[Canaccord Genuity]] | Buy | $14 |
| Brian Kinstlinger | [[Alliance Global Partners]] | Hold | $9 |

Consensus: Buy (4 of 5 analysts). Average PT $14.20. Stock at ~$16 is above average PT but below HC Wainwright's $19 target.

---

## Related

- [[Golden Dome]] — SHIELD IDIQ is the primary contracting framework
- [[Space]] — sector hub
- [[Planet Labs]], [[BlackSky]], [[HawkEye 360]] — peers/competitors
- [[SpaceX]] — launch provider (Transporter missions)
- [[2026 Strait of Hormuz crisis]] — structural relevance (maritime domain awareness + RF)
- [[Kpler]] — acquired Spire's maritime business
- [[Long global rearmament]] — defense thesis alignment

### Securities

- [[Spire Global securities]] — SPIR price history, charts, technicals

### Charts

![[spir-price-chart.png]]

![[spir-sankey.png]]

![[spir-waterfall.png]]
