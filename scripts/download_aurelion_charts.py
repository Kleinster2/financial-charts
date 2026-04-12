"""Download Aurelion Research fertilizer primer charts from Substack to investing/attachments/."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.download_utils import run_batch

SUBSTACK_BASE = "https://substack-post-media.s3.amazonaws.com/public/images/{hash}_{dims}.png"

# (hash, dims, descriptive_filename) — Substack-specific tuple form
CHARTS = [
    ("6a0aefcf-e03b-475c-be69-102481fdbbd1", "3378x2322", "hormuz-urea-corridor-aurelion-mar2026.png"),
    ("4a4fbc1a-6458-47f9-ab7c-9d40a4f96f4c", "3795x2029", "urea-ammonia-price-spike-aurelion-mar2026.png"),
    ("ae294674-eabb-4bb2-a49c-9726c27468bd", "3417x1615", "urea-corn-futures-correlation-aurelion-mar2026.png"),
    ("ba676101-7711-48b8-a740-874df41e3597", "2722x894", "fertilizer-nutrients-k-n-p-aurelion.png"),
    ("766821ac-f3c0-4249-8153-21ebfb280ab4", "3608x1434", "global-fertilizer-market-by-product-aurelion.png"),
    ("8bf6db2e-a014-4534-af18-d6a164896b36", "3162x1617", "fertilizer-demand-caloric-intake-aurelion.png"),
    ("308265d6-da41-44e8-8c96-28c3350951fa", "2558x1512", "fertilizer-industrial-nox-demand-aurelion.png"),
    ("0a8dbadd-643d-4fe1-b98b-8e59ff7ed9b2", "3956x2065", "fertilizer-tier1-producer-concentration-aurelion.png"),
    ("8dc03402-04fd-4ca5-bd90-63c0982ba0e6", "3366x1615", "potash-price-history-2019-2026-aurelion.png"),
    ("de7d60d0-1657-4e58-aff1-2b8f5a877b8b", "3330x1615", "potash-capacity-utilization-aurelion.png"),
    ("6a90ddea-1f60-4e5d-9a90-3ae1badda6f3", "3095x1615", "potash-demand-by-region-aurelion.png"),
    ("88e98b92-a4c8-4068-b937-aa8fd309d7b3", "3838x1615", "india-potash-imports-aurelion.png"),
    ("2fe11e11-9c51-4f8f-91fc-f995f779c876", "3142x1615", "brazil-potash-cost-curve-aurelion.png"),
    ("798218e7-4bea-4002-9484-d8bc4cf49a86", "2720x1058", "nitrogen-share-of-nutrients-aurelion.png"),
    ("b2f0e737-206f-4147-ab8d-390ff00380a4", "3366x1615", "urea-benchmark-prices-egypt-china-brazil-aurelion.png"),
    ("e171fa3d-244f-4609-a2a5-297b92399c75", "3450x950", "nitrogen-value-chain-aurelion.png"),
    ("a2534eac-1ba2-448d-b08c-0ffecd901e7d", "3810x1792", "nitrogen-value-chain-detail-aurelion.png"),
    ("0acd326a-3f5a-475e-872c-3a188b8086c3", "3140x1615", "asia-nitrogen-consumption-aurelion.png"),
    ("8a160bfa-b9a1-4fa2-ab0c-53ef48a03960", "3833x1615", "urea-imports-india-brazil-china-aurelion.png"),
    ("d8dc27a9-d2d1-41d1-96b6-ca11989d3922", "3071x1615", "urea-capacity-additions-vs-demand-aurelion.png"),
    ("97024a46-39ba-4a35-99bc-ed731ed21bb7", "3161x1617", "dap-exporter-concentration-aurelion.png"),
    ("26b2ad2f-75f4-4b0d-a35e-f0c430be0104", "3224x1626", "dap-price-history-aurelion.png"),
    ("6a1795cf-4ea2-4b4d-b3cc-01b4d84b7f9e", "3140x1626", "us-phosphate-imports-decline-aurelion.png"),
    ("e9ac1618-4ae2-492b-9038-6057398ee160", "3013x1625", "global-phosphate-consumption-aurelion.png"),
]

OUT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "investing", "attachments")

jobs = [(SUBSTACK_BASE.format(hash=h, dims=d), name) for h, d, name in CHARTS]
run_batch(jobs, out_dir=OUT_DIR)
