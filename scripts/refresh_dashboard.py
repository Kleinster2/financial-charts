"""Batch-refresh all Dashboard.md charts via Flask test client."""
import sys, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, "charting_app"))

from charting_app.app import app

ATTACHMENTS = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                           "investing", "attachments")

# Standard /api/chart/lw charts: (filename, query_params)
LW_CHARTS = [
    ("spy-vs-qqq-vs-iwm-vs-rsp-2025.png",
     "tickers=SPY,QQQ,IWM,RSP&start=2025-01-01&normalize=true"),
    ("vix-ytd.png",
     "tickers=^VIX&start=2025-01-01"),
    ("smh-vs-nvda-vs-amd-vs-tsm-vs-intc-vs-asml-vs-amat-vs-lrcx-2025.png",
     "tickers=SMH,NVDA,AMD,TSM,INTC,ASML,AMAT,LRCX&start=2025-01-01&normalize=true"),
    ("drgn-vs-kweb-vs-cqqq-price-chart.png",
     "tickers=DRGN,KWEB,CQQQ&normalize=true&start=2025-01-01"),
    ("bil-vs-shy-vs-iei-vs-ief-vs-tlt-2025.png",
     "tickers=BIL,SHY,IEI,IEF,TLT&start=2025-01-01&normalize=true"),
    ("tlt-vs-2510_t-vs-iglt_l-vs-ibgl_l-vs-xlb_to-vs-govt_ax-vs-cbon-2025.png",
     "tickers=TLT,2510.T,IGLT.L,IBGL.L,XLB.TO,GOVT.AX,CBON&start=2025-01-01&normalize=true"),
    ("usdjpy-vs-usdeur-vs-usdgbp-vs-usdchf-fx-2025.png",
     "tickers=USDJPY=X,USDEUR=X,USDGBP=X,USDCHF=X&start=2025-01-01&normalize=true"),
    ("usdcny-vs-usdbrl-vs-usdmxn-vs-usdzar-vs-usdinr-vs-usdils-fx-2025.png",
     "tickers=USDCNY=X,USDBRL=X,USDMXN=X,USDZAR=X,USDINR=X,USDILS=X&start=2025-01-01&normalize=true"),
    ("gld-vs-slv-vs-pplt-vs-pall-2025.png",
     "tickers=GLD,SLV,PPLT,PALL&start=2025-01-01&normalize=true"),
    ("uso-vs-ung-vs-uga-2025.png",
     "tickers=USO,UNG,UGA&start=2025-01-01&normalize=true"),
    ("cper-vs-dbb-2025.png",
     "tickers=CPER,DBB&start=2025-01-01&normalize=true"),
    ("dba-vs-corn-vs-weat-vs-soyb-2025.png",
     "tickers=DBA,CORN,WEAT,SOYB&start=2025-01-01&normalize=true"),
    ("dbc-vs-gsg-2025.png",
     "tickers=DBC,GSG&start=2025-01-01&normalize=true"),
    ("btc-usd-vs-eth-usd-vs-sol-usd-vs-xrp-usd-vs-bnb-usd-vs-mstr-2025.png",
     "tickers=BTC-USD,ETH-USD,SOL-USD,XRP-USD,BNB-USD,MSTR&start=2025-01-01&normalize=true"),
    ("hyg-vs-lqd-vs-emb-2025.png",
     "tickers=HYG,LQD,EMB&start=2025-01-01&normalize=true"),
    ("spy-vs-eem-vs-efa-2025.png",
     "tickers=SPY,EEM,EFA&start=2025-01-01&normalize=true"),
    ("ewj-vs-ewg-vs-ewu-vs-ewq-vs-ewl-vs-ewd-vs-ewa-vs-ewc-2025.png",
     "tickers=EWJ,EWG,EWU,EWQ,EWL,EWD,EWA,EWC&start=2025-01-01&normalize=true"),
    ("ewz-vs-inda-vs-ewt-vs-ewy-vs-eww-vs-ewh-vs-eido-vs-eza-vs-tur-vs-epol-vs-eis-2025.png",
     "tickers=EWZ,INDA,EWT,EWY,EWW,EWH,EIDO,EZA,TUR,EPOL,EIS&start=2025-01-01&normalize=true"),
    ("xlk-vs-xlf-vs-xle-vs-xlv-vs-xli-vs-xly-vs-xlp-vs-xlu-vs-xlre-vs-xlb-vs-xlc-2025.png",
     "tickers=XLK,XLF,XLE,XLV,XLI,XLY,XLP,XLU,XLRE,XLB,XLC&start=2025-01-01&normalize=true"),
    ("dprime-vs-ita-2025.png",
     "tickers=DPRIME,ITA&start=2025-01-01&normalize=true"),
    ("avav-vs-ktos-vs-dprime-vs-uso-vs-gld-vs-dal-2025.png",
     "tickers=AVAV,KTOS,DPRIME,USO,GLD,DAL&start=2025-01-01&normalize=true"),
    ("vgt-vs-xlk-price-chart.png",
     "tickers=VGT,XLK&start=2025-01-01&normalize=true"),
]

def main():
    client = app.test_client()

    ok, fail = 0, 0
    for filename, params in LW_CHARTS:
        out = os.path.join(ATTACHMENTS, filename)
        resp = client.get(f"/api/chart/lw?{params}")
        if resp.status_code == 200 and len(resp.data) > 1000:
            with open(out, "wb") as f:
                f.write(resp.data)
            print(f"  OK  {filename} ({len(resp.data):,} bytes)")
            ok += 1
        else:
            print(f"  FAIL {filename} (status={resp.status_code}, {len(resp.data)} bytes)")
            fail += 1

    print(f"\nDone: {ok} refreshed, {fail} failed")

if __name__ == "__main__":
    main()
