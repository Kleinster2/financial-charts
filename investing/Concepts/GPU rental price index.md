---
aliases: [SDH100RT, Silicon Data H100 index, GPU spot prices, H100 rental prices, GPU rental market]
---
#concept #ai #infrastructure #data

**GPU rental price index** — tracking the spot/on-demand rental price of AI GPUs (primarily [[NVIDIA]] H100s) as a real-time indicator of AI compute demand, supply constraints, and infrastructure economics.

---

## Why it matters

H100 rental prices are the **oil price of AI** — a single number that captures the balance between explosive demand and constrained supply. Falling prices signal oversupply or demand destruction. Rising prices signal capacity constraints and accelerating adoption.

Key signals:
- **Inference economics** — rental prices directly determine the cost of running AI models (see [[Inference economics]])
- **Hyperscaler capex validation** — if spot prices stay high, $300B+ annual capex is justified
- **AMD/NVIDIA competition** — AMD gaining share should push H100 prices down
- **Custom silicon threat** — [[Google]] TPUs, [[Amazon]] Trainium, [[Meta]] MTIA all compete to reduce GPU dependence

---

## SDH100RT — Silicon Data's index

The first formal GPU rental price index, launched June 2025 by **Silicon Data**.

| Detail | Value |
|--------|-------|
| Name | SDH100RT (Silicon Data H100 Real-Time) |
| Launch | June 27, 2025 |
| Distribution | Bloomberg terminals + paid API |
| Methodology | 3.5M data points daily from 30+ sources worldwide |
| Metric | Average spot rental price per H100-hour |
| Expansion | A100 index in testing (as of Sep 2025) |
| Cost | Enterprise pricing (not free) |

Silicon Data also offers **SiliconMark** — a benchmarking tool that validates compute quality alongside price, helping buyers assess cost *and* performance.

---

## DIY tracking (our approach)

Since SDH100RT requires Bloomberg/paid API, we built a scraper that collects daily H100 spot prices from public sources:

**Script:** `scripts/scrape_gpu_prices.py`
**Storage:** `gpu_rental_prices` table in `market_data.db`

### Sources

| Provider | Type | H100 Price Range | Notes |
|----------|------|-----------------|-------|
| **Vast.ai** | Marketplace (spot) | Varies — often sold out | Hundreds of GPU offers, but H100s frequently fully allocated |
| **RunPod** | Fixed (community/secure) | $1.99-$3.29/hr | Community cloud cheaper, secure cloud premium |
| **Lambda Labs** | Fixed (on-demand) | $3.29/hr | Enterprise-grade, consistent |
| **SF Compute** | Managed clusters | ~$1.50/hr avg | Bulk pricing, no lock-in |

*Prices as of Feb 25, 2026*

### Key finding: H100 scarcity on spot markets

As of Feb 2026, **zero H100 offers** on Vast.ai's on-demand marketplace — all datacenter GPUs are fully allocated. Only consumer/prosumer GPUs (RTX 3090, 4090, etc.) available on spot. This is itself a demand signal: H100 supply is tight enough that nothing sits idle.

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

The **decline from 2024 peaks** reflects both supply additions (TSMC ramping) and generation shift (Blackwell displacing H100 for training). But prices haven't collapsed — inference demand is absorbing freed-up H100 capacity.

---

## Related

- [[Inference economics]] — how GPU rental costs determine AI model profitability
- [[NVIDIA]] — H100/H200/Blackwell GPU manufacturer
- [[AMD]] — competitor GPUs (MI300X, MI450), could pressure prices
- [[CUDA moat]] — software lock-in keeps users on NVIDIA despite price
- [[Tech equity-for-infrastructure deals]] — deals driven by compute scarcity
- [[Meta-AMD 6GW deal]] — demand signal for GPU infrastructure
- [[AI hyperscalers]] — primary demand drivers
