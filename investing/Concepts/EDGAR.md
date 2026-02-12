---
aliases: [SEC EDGAR, EDGAR database]
---
#concept #regulation #infrastructure

EDGAR (Electronic Data Gathering, Analysis, and Retrieval) — the [[SEC]]'s online filing system for corporate disclosures. All public company filings — [[13F]]s, 10-Ks, 10-Qs, 8-Ks, proxy statements, insider transactions — are submitted and publicly accessible through EDGAR. Launched 1996. Free to access.

---

## Key filing types available

| Form | Purpose | Frequency |
|------|---------|-----------|
| 10-K | Annual report | Annual |
| 10-Q | Quarterly report | Quarterly |
| 8-K | Material events | As needed |
| [[13F]] | Institutional holdings | Quarterly |
| DEF 14A | Proxy statement | Annual |
| Form 4 | Insider trades | Within 2 business days |
| S-1 | IPO registration | One-time |
| SC 13D/G | Beneficial ownership >5% | As needed |

---

## Access

| Method | URL / tool |
|--------|-----------|
| Full-text search | efts.sec.gov/LATEST/search-index |
| Company filings | sec.gov/cgi-bin/browse-edgar |
| XBRL data | sec.gov/dera/data |
| API | efts.sec.gov (rate-limited; requires User-Agent header) |

SEC blocks most automated scrapers without a proper User-Agent header. This vault uses `scripts/parse_sec_filing.py` to fetch and parse filings with the required header.

---

## Quick stats

| Metric | Value |
|--------|-------|
| Launched | 1996 |
| Operator | [[SEC]] |
| Cost | Free |
| Filings | All SEC-regulated disclosures |

---

## Related

- [[13F]] — institutional holdings filing submitted via EDGAR
- [[SEC]] — regulator that operates EDGAR

---

*Created 2026-02-11*
