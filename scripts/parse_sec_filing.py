#!/usr/bin/env python3
"""
Parse SEC EDGAR filings.

Downloads 10-K/10-Q filings and extracts information based on custom search terms.
No hardcoded assumptions — pass the terms relevant to your analysis.

Usage:
    # Download and search for specific terms
    python scripts/parse_sec_filing.py AAPL --terms "revenue,growth,margin"

    # Distressed company analysis
    python scripts/parse_sec_filing.py SOND --terms "going concern,material weakness,default"

    # Growth company analysis
    python scripts/parse_sec_filing.py NVDA --terms "revenue,market share,data center,AI"

    # Just download the filing (no term search)
    python scripts/parse_sec_filing.py AAPL --save filing.html

    # By CIK or direct URL
    python scripts/parse_sec_filing.py --cik 1819395 --terms "litigation"
    python scripts/parse_sec_filing.py --url <edgar_url> --terms "dividend,buyback"

    # 10-Q instead of 10-K
    python scripts/parse_sec_filing.py AAPL --type 10-Q --terms "guidance,outlook"
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

# Pattern for extracting dollar amounts
DOLLAR_PATTERN = re.compile(r'\$\s*\d+(?:\.\d+)?\s*(?:million|billion)', re.IGNORECASE)


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
            print(f"ERROR: SEC blocked request. Update USER_AGENT in script.")
            sys.exit(1)
        raise


def get_cik_from_ticker(ticker: str) -> str:
    """Look up CIK from ticker symbol."""
    url = "https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&company=&CIK={}&type=10-K&dateb=&owner=include&count=1&output=atom".format(ticker)
    data = fetch_url(url).decode('utf-8')
    # Extract CIK from response
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


def get_latest_filing_url(cik: str, filing_type: str = "10-K", include_amendments: bool = False) -> tuple[str, str]:
    """Get URL of latest filing of given type."""
    cik_padded = cik.zfill(10)
    url = f"https://data.sec.gov/submissions/CIK{cik_padded}.json"
    data = fetch_url(url).decode('utf-8')
    submissions = json.loads(data)

    filings = submissions.get('filings', {}).get('recent', {})
    forms = filings.get('form', [])
    accessions = filings.get('accessionNumber', [])
    primary_docs = filings.get('primaryDocument', [])

    # First pass: look for exact match (non-amendment)
    for i, form in enumerate(forms):
        if form == filing_type:
            accession = accessions[i].replace('-', '')
            doc = primary_docs[i]
            filing_url = f"https://www.sec.gov/Archives/edgar/data/{cik}/{accession}/{doc}"
            return filing_url, form

    # Second pass: include amendments if allowed or no exact match
    if include_amendments:
        for i, form in enumerate(forms):
            if form == f"{filing_type}/A":
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
    # Normalize whitespace
    html = re.sub(r'\s+', ' ', html)
    return html


def count_terms(text: str, terms: list[str]) -> dict[str, int]:
    """Count occurrences of each term."""
    text_lower = text.lower()
    return {term: len(re.findall(re.escape(term), text_lower)) for term in terms}


def extract_context(text: str, term: str, chars: int = 150, max_results: int = 3) -> list[str]:
    """Extract text surrounding each occurrence of term."""
    pattern = re.compile(f'.{{0,{chars}}}{re.escape(term)}.{{0,{chars}}}', re.IGNORECASE)
    matches = pattern.findall(text)
    return [m.strip() for m in matches[:max_results]]


def extract_dollar_amounts(text: str) -> dict[str, int]:
    """Extract and count dollar amounts mentioned."""
    amounts = DOLLAR_PATTERN.findall(text)
    counts = {}
    for amt in amounts:
        amt_clean = amt.strip()
        counts[amt_clean] = counts.get(amt_clean, 0) + 1
    # Sort by count
    return dict(sorted(counts.items(), key=lambda x: -x[1])[:20])


def analyze_filing(html_content: bytes, terms: list[str]) -> dict:
    """Analyze a filing and extract information for given terms."""
    html = html_content.decode('utf-8', errors='replace')
    text = strip_html(html)

    results = {
        "term_counts": count_terms(text, terms) if terms else {},
        "dollar_amounts": extract_dollar_amounts(text),
        "excerpts": {},
    }

    # Extract context for terms with matches
    for term in terms:
        if results["term_counts"].get(term, 0) > 0:
            results["excerpts"][term] = extract_context(text, term)

    return results


def print_report(results: dict, filing_url: str, filing_type: str, terms: list[str]):
    """Print analysis report."""
    print("=" * 60)
    print(f"SEC FILING ANALYSIS: {filing_type}")
    print(f"URL: {filing_url}")
    print("=" * 60)

    # Term counts
    if results["term_counts"]:
        print("\nTERM COUNTS:")
        for term, count in sorted(results["term_counts"].items(), key=lambda x: -x[1]):
            bar = "#" * min(count, 30)
            print(f"   {term:25} {count:4}  {bar}")
    else:
        print("\nNo search terms specified. Use --terms to search for specific terms.")

    # Dollar amounts
    if results["dollar_amounts"]:
        print("\nTOP DOLLAR AMOUNTS MENTIONED:")
        for amt, count in list(results["dollar_amounts"].items())[:10]:
            print(f"   {amt:25} ({count}x)")

    # Excerpts
    if results["excerpts"]:
        print("\nEXCERPTS:")
        for term, excerpts in results["excerpts"].items():
            print(f"\n   [{term.upper()}]")
            for i, exc in enumerate(excerpts, 1):
                # Truncate long excerpts
                if len(exc) > 200:
                    exc = exc[:200] + "..."
                print(f"   {i}. ...{exc}...")

    print("\n" + "=" * 60)


def main():
    parser = argparse.ArgumentParser(
        description="Parse SEC EDGAR filings with custom search terms",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s AAPL --terms "revenue,growth,margin"
  %(prog)s SOND --terms "going concern,material weakness"
  %(prog)s NVDA --type 10-Q --terms "data center,AI"
  %(prog)s AAPL --save apple-10k.html
        """
    )
    parser.add_argument("ticker", nargs="?", help="Stock ticker symbol")
    parser.add_argument("--cik", help="CIK number")
    parser.add_argument("--url", help="Direct filing URL")
    parser.add_argument("--type", default="10-K", help="Filing type (default: 10-K)")
    parser.add_argument("--terms", help="Comma-separated terms to search for")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    parser.add_argument("--save", help="Save HTML to file")

    args = parser.parse_args()

    if not any([args.ticker, args.cik, args.url]):
        parser.print_help()
        sys.exit(1)

    # Parse terms
    terms = []
    if args.terms:
        terms = [t.strip().lower() for t in args.terms.split(",")]

    # Get filing URL
    if args.url:
        filing_url = args.url
        filing_type = args.type
    else:
        cik = args.cik or get_cik_from_ticker(args.ticker)
        print(f"CIK: {cik}")
        filing_url, filing_type = get_latest_filing_url(cik, args.type)

    print(f"Fetching: {filing_url}")

    # Download filing
    html_content = fetch_url(filing_url)
    print(f"Downloaded: {len(html_content):,} bytes")

    # Optionally save
    if args.save:
        Path(args.save).write_bytes(html_content)
        print(f"Saved to: {args.save}")

    # Analyze
    results = analyze_filing(html_content, terms)

    # Output
    if args.json:
        print(json.dumps(results, indent=2))
    else:
        print_report(results, filing_url, filing_type, terms)


if __name__ == "__main__":
    main()
