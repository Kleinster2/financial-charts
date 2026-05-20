---
aliases: [SDH100RT, Silicon Data H100 index, GPU spot prices, H100 rental prices, GPU rental market]
---
#concept #ai #infrastructure #data

**GPU rental price index** — tracking the spot/on-demand rental price of AI GPUs (primarily [[NVIDIA]] H100s) as a real-time indicator of AI compute demand, supply constraints, and infrastructure economics.

---

## Why it matters

H100 rental prices are the oil price of AI — a single number that captures the balance between explosive demand and constrained supply. Falling prices signal oversupply or demand destruction. Rising prices signal capacity constraints and accelerating adoption.

Key signals:
- Inference economics — rental prices directly determine the cost of running AI models (see [[Inference economics]])
- Hyperscaler capex validation — if spot prices stay high, $300B+ annual capex is justified
- AMD/NVIDIA competition — AMD gaining share should push H100 prices down
- Custom silicon threat — [[Google]] TPUs, [[Amazon]] Trainium, [[Meta]] MTIA all compete to reduce GPU dependence

---

## SDH100RT — Silicon Data's index

The first formal GPU rental price index, launched June 2025 by Silicon Data.

| Detail | Value |
|--------|-------|
| Name | SDH100RT (Silicon Data H100 Real-Time) |
| Launch | June 27, 2025 |
| Distribution | Bloomberg terminals + paid API |
| Methodology | 3.5M data points daily from 30+ sources worldwide |
| Metric | Average spot rental price per H100-hour |
| Expansion | A100 index in testing (as of Sep 2025) |
| Cost | Enterprise pricing (not free) |

Silicon Data also offers SiliconMark — a benchmarking tool that validates compute quality alongside price, helping buyers assess cost *and* performance.

---

## DIY tracking (our approach)

Since SDH100RT requires Bloomberg/paid API, we built a scraper that collects daily H100 spot prices from public sources:

Script: `scripts/scrape_gpu_prices.py`
Storage: `gpu_rental_prices` table in `market_data.db`

### Sources

| Provider | Type | H100 Price Range | Notes |
|----------|------|-----------------|-------|
| Vast.ai | Marketplace (spot) | Varies — often sold out | Hundreds of GPU offers, but H100s frequently fully allocated |
| RunPod | Fixed (community/secure) | $1.99-$3.29/hr | Community cloud cheaper, secure cloud premium |
| Lambda Labs | Fixed (on-demand) | $3.29/hr | Enterprise-grade, consistent |
| SF Compute | Managed clusters | ~$1.50/hr avg | Bulk pricing, no lock-in |

*Prices as of Feb 25, 2026*

### Key finding: H100 scarcity on spot markets

As of Feb 2026, zero H100 offers on Vast.ai's on-demand marketplace — all datacenter GPUs are fully allocated. Only consumer/prosumer GPUs (RTX 3090, 4090, etc.) available on spot. This is itself a demand signal: H100 supply is tight enough that nothing sits idle.

### Running the scraper

```bash
python scripts/scrape_gpu_prices.py              # scrape today's prices
python scripts/scrape_gpu_prices.py --history     # show recent history
python scripts/scrape_gpu_prices.py --csv         # export all data
```

---

## Price history context

| Period | H100 $/hr (approx) | Driver |
|--------|-------------------|--------|
| Early 2024 | $3.50-$4.50 | Peak scarcity, Blackwell not yet shipping |
| Mid 2025 | $2.50-$3.50 | Blackwell arriving, H100 supply easing |
| Late 2025 | $2.00-$3.00 | More supply, but demand still strong |
| Feb 2026 | $1.50-$3.29 | Wide range; bulk/spot diverging from enterprise |

The decline from 2024 peaks reflects both supply additions (TSMC ramping) and generation shift (Blackwell displacing H100 for training). But prices haven't collapsed — inference demand is absorbing freed-up H100 capacity.

---

## Kalshi compute-rental pricing layer (May 20, 2026)

[[Kalshi]]'s GPU compute-price markets now provide a public prediction-market overlay on the same scarcity signal this note tracks. The contracts are not observed rental prices; they ask whether named GPU compute-per-hour prices will clear thresholds at weekly or monthly resolution. Treat them as market-implied color on supply/demand, not as a substitute for SDH100RT or direct provider scraping.

| Contract family | May 20 active-market read | Vault interpretation |
|---|---|---|
| [[H100]] SXM monthly price, May 31 (KXH100MON) | All 40 active strikes had some volume or open interest. The top strike, >$2.17/hr, was 86c / 96c bid-ask with 96c last; aggregate active volume was 2,278.03 and open interest was 1,625.77. | The market is pricing [[H100]] rental above $2/hr as the base case, consistent with scarcity easing from the 2024 peak but not collapsing. |
| [[H100]] weekly price-up check, May 22 (KXH100W) | Single active strike at $3.14 was 85c / 87c bid-ask with 63c last, but only 9.95 volume and 6.95 open interest. | Directionally bullish, but too thin to override the monthly ladder. |
| [[H200]] monthly price, May 31 (KXH200MON) | The top strike, >$2.74/hr, was 70c / 100c bid-ask with 70c last; active volume was 262 and open interest was 197. | [[H200]] scarcity is bid, but the wide quotes make the precise midpoint unreliable. |
| [[H200]] weekly price-up check, May 22 (KXH200W) | Single active strike at $4.96 was 12c / 27c bid-ask with 16c last, 199 volume, and 27.05 open interest. | The weekly momentum contract leans against a near-term jump even while the month-end ladder remains elevated. |
| [[RTX 5090]] monthly price, May 31 (KXRTX5090MON) | The high strike, >$0.67/hr, was 50c / 79c bid-ask with 53c last; the most active strikes were $0.52-$0.55 with 85c-99c asks. | Consumer/prosumer compute remains bid, with a rough market center above $0.60/hr. |
| [[RTX 5090]] weekly price-up check, May 22 (KXRTX5090W) | Single active strike at $0.59 was 88c / 99c bid-ask with 83c last, 150.19 volume, and 142.11 open interest. | The cleanest non-data-center signal in the pull; retail GPU compute is still tightening. |
| [[A100]] / [[B200]] / [[Nvidia RTX PRO 6000|RTX PRO 6000]] | [[A100]] and [[B200]] ladders existed but had little or no usable liquidity; [[Nvidia RTX PRO 6000|RTX PRO 6000]] returned no active API markets. | Skip for durable signal until open interest appears. [[B200]] spot economics still need direct provider data and hardware-channel checks. |

The useful synthesis is asymmetry: H100 and H200 prices remain high enough to support the AI-infrastructure scarcity thesis, while the B200 prediction-market layer is not liquid enough to say whether Blackwell supply is clearing cleanly. That matters because [[AI hyperscalers]] can keep bidding for older Hopper capacity even as [[Blackwell]] ramps, especially for inference and enterprise workloads that do not require the newest training clusters.

*Sources: [[Kalshi]] API series KXH100MON, KXH100W, KXH200MON, KXH200W, KXRTX5090MON, KXRTX5090W, KXA100MON, KXA100W, KXB200MON, KXB200W, KXRTXPRO6000MON, and KXRTXPRO6000W, read May 20, 2026.*

---

## Related

- [[Inference economics]] — how GPU rental costs determine AI model profitability
- [[NVIDIA]] — H100/H200/Blackwell GPU manufacturer
- [[AMD]] — competitor GPUs (MI300X, MI450), could pressure prices
- [[CUDA moat]] — software lock-in keeps users on NVIDIA despite price
- [[Tech equity-for-infrastructure deals]] — deals driven by compute scarcity
- [[Meta-AMD 6GW deal]] — demand signal for GPU infrastructure
- [[AI hyperscalers]] — primary demand drivers
