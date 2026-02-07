#!/usr/bin/env python3
"""
Download SEC EDGAR filings and output clean text.

Downloads 10-K/10-Q filings, strips HTML, outputs text for context ingestion.
Analysis is done by the LLM, not by keyword matching.

Usage:
    # Download latest 10-K as clean text
    python scripts/parse_sec_filing.py AAPL

    # Save to file for subagent ingestion
    python scripts/parse_sec_filing.py AAPL --save aapl-10k.txt

    # 10-Q instead of 10-K
    python scripts/parse_sec_filing.py AAPL --type 10-Q

    # By CIK or direct URL
    python scripts/parse_sec_filing.py --cik 1819395
    python scripts/parse_sec_filing.py --url <edgar_url>

    # Keep raw HTML instead of stripping
    python scripts/parse_sec_filing.py AAPL --raw --save aapl-10k.html
"""

import argparse
import gzip
import json
import re
import sys
from html import unescape
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import HTTPError

# SEC requires declared user agent
USER_AGENT = "klein-financial-charts research@example.com"


def fetch_url(url: str) -> bytes:
    """Fetch URL with proper SEC headers."""
    req = Request(url, headers={
        "User-Agent": USER_AGENT,
        "Accept-Encoding": "gzip, deflate",
    })
    try:
        with urlopen(req, timeout=30) as resp:
            data = resp.read()
            # Check if gzipped
            if data[:2] == b'\x1f\x8b':
                data = gzip.decompress(data)
            return data
    except HTTPError as e:
        if e.code == 403:
            print(f"ERROR: SEC blocked request. Update USER_AGENT in script.", file=sys.stderr)
            sys.exit(1)
        raise


def get_cik_from_ticker(ticker: str) -> str:
    """Look up CIK from ticker symbol."""
    url = "https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&company=&CIK={}&type=10-K&dateb=&owner=include&count=1&output=atom".format(ticker)
    data = fetch_url(url).decode('utf-8')
    match = re.search(r'CIK=(\d+)', data)
    if match:
        return match.group(1)
    # Try company tickers JSON
    url = "https://www.sec.gov/files/company_tickers.json"
    data = fetch_url(url).decode('utf-8')
    tickers = json.loads(data)
    for entry in tickers.values():
        if entry.get('ticker', '').upper() == ticker.upper():
            return str(entry['cik_str']).zfill(10)
    raise ValueError(f"Could not find CIK for ticker: {ticker}")


def get_latest_filing_url(cik: str, filing_type: str = "10-K") -> tuple[str, str]:
    """Get URL of latest filing of given type."""
    cik_padded = cik.zfill(10)
    url = f"https://data.sec.gov/submissions/CIK{cik_padded}.json"
    data = fetch_url(url).decode('utf-8')
    submissions = json.loads(data)

    filings = submissions.get('filings', {}).get('recent', {})
    forms = filings.get('form', [])
    accessions = filings.get('accessionNumber', [])
    primary_docs = filings.get('primaryDocument', [])

    for i, form in enumerate(forms):
        if form == filing_type:
            accession = accessions[i].replace('-', '')
            doc = primary_docs[i]
            filing_url = f"https://www.sec.gov/Archives/edgar/data/{cik}/{accession}/{doc}"
            return filing_url, form

    raise ValueError(f"No {filing_type} found for CIK {cik}")


def strip_html(html: str) -> str:
    """Remove HTML tags and decode entities."""
    # Remove script/style
    html = re.sub(r'<script[^>]*>.*?</script>', ' ', html, flags=re.DOTALL | re.IGNORECASE)
    html = re.sub(r'<style[^>]*>.*?</style>', ' ', html, flags=re.DOTALL | re.IGNORECASE)
    # Remove tags
    html = re.sub(r'<[^>]+>', ' ', html)
    # Decode entities
    html = unescape(html)
    # Normalize whitespace but preserve some structure
    html = re.sub(r'[ \t]+', ' ', html)
    html = re.sub(r'\n\s*\n', '\n\n', html)
    return html.strip()


def main():
    parser = argparse.ArgumentParser(
        description="Download SEC EDGAR filings as clean text for LLM analysis",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("ticker", nargs="?", help="Stock ticker symbol")
    parser.add_argument("--cik", help="CIK number")
    parser.add_argument("--url", help="Direct filing URL")
    parser.add_argument("--type", default="10-K", help="Filing type (default: 10-K)")
    parser.add_argument("--save", help="Save output to file")
    parser.add_argument("--raw", action="store_true", help="Keep raw HTML instead of stripping")
    parser.add_argument("--quiet", action="store_true", help="Suppress status messages")

    args = parser.parse_args()

    if not any([args.ticker, args.cik, args.url]):
        parser.print_help()
        sys.exit(1)

    def log(msg):
        if not args.quiet:
            print(msg, file=sys.stderr)

    # Get filing URL
    if args.url:
        filing_url = args.url
        filing_type = args.type
    else:
        cik = args.cik or get_cik_from_ticker(args.ticker)
        log(f"CIK: {cik}")
        filing_url, filing_type = get_latest_filing_url(cik, args.type)

    log(f"Fetching: {filing_url}")

    # Download filing
    html_content = fetch_url(filing_url)
    log(f"Downloaded: {len(html_content):,} bytes")

    # Process
    if args.raw:
        output = html_content.decode('utf-8', errors='replace')
    else:
        html = html_content.decode('utf-8', errors='replace')
        output = strip_html(html)
        log(f"Text length: {len(output):,} chars")

    # Output
    if args.save:
        Path(args.save).write_text(output, encoding='utf-8')
        log(f"Saved to: {args.save}")
    else:
        print(output)


if __name__ == "__main__":
    main()
