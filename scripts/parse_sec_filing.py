#!/usr/bin/env python3
"""
Download SEC EDGAR filings and output clean text.

Downloads most recent 10-K or 10-Q, strips HTML, outputs text for context ingestion.
Analysis is done by the LLM, not by keyword matching.

Usage:
    # Download most recent filing (10-K or 10-Q, whichever is latest)
    python scripts/parse_sec_filing.py AAPL

    # Save to file for subagent ingestion
    python scripts/parse_sec_filing.py AAPL --save aapl-filing.txt

    # Force specific type
    python scripts/parse_sec_filing.py AAPL --type 10-K
    python scripts/parse_sec_filing.py AAPL --type 10-Q

    # Download multiple filings for comparison
    python scripts/parse_sec_filing.py AAPL --type 10-Q --count 4 --save /tmp/aapl
    # Creates: /tmp/aapl-10-Q-2025-11-01.txt, /tmp/aapl-10-Q-2025-08-02.txt, ...

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

# Cache raw HTML to avoid re-downloading immutable filings
CACHE_DIR = Path(__file__).resolve().parent.parent / "data" / "edgar_cache"


def get_cache_path(filing_url: str) -> Path | None:
    """Derive cache path from an EDGAR filing URL."""
    match = re.search(r'/Archives/edgar/data/\d+/(\w+)/(.+)$', filing_url)
    if not match:
        return None
    accession, doc = match.groups()
    return CACHE_DIR / accession / doc


def update_cache_index(accession: str, ticker: str, filing_type: str, filing_date: str, size: int):
    """Record a cached filing in the index."""
    index_path = CACHE_DIR / "cache_index.json"
    index = {}
    if index_path.exists():
        index = json.loads(index_path.read_text(encoding='utf-8'))
    index[accession] = {
        "ticker": ticker.upper(),
        "type": filing_type,
        "date": filing_date,
        "size": size,
    }
    index_path.write_text(json.dumps(index, indent=2), encoding='utf-8')


def list_cache():
    """Print cached filings."""
    index_path = CACHE_DIR / "cache_index.json"
    if not index_path.exists():
        print("Cache is empty.")
        return
    index = json.loads(index_path.read_text(encoding='utf-8'))
    if not index:
        print("Cache is empty.")
        return
    # Sort by ticker then date
    entries = sorted(index.values(), key=lambda e: (e["ticker"], e["date"]))
    for e in entries:
        size_mb = e["size"] / (1024 * 1024)
        if size_mb >= 1:
            size_str = f"{size_mb:.1f}M"
        else:
            size_str = f"{e['size'] / 1024:.0f}K"
        print(f"{e['ticker']:<6} {e['type']:<6} {e['date']}  {size_str:>6}")


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


def get_filing_urls(cik: str, filing_type: str | None = None, count: int = 1) -> list[tuple[str, str, str]]:
    """Get URLs of filings. Returns list of (url, form_type, date) tuples."""
    cik_padded = cik.zfill(10)
    url = f"https://data.sec.gov/submissions/CIK{cik_padded}.json"
    data = fetch_url(url).decode('utf-8')
    submissions = json.loads(data)

    filings = submissions.get('filings', {}).get('recent', {})
    forms = filings.get('form', [])
    accessions = filings.get('accessionNumber', [])
    primary_docs = filings.get('primaryDocument', [])
    dates = filings.get('filingDate', [])

    # If no type specified, find most recent 10-K or 10-Q
    target_types = [filing_type] if filing_type else ["10-K", "10-Q"]

    results = []
    for i, form in enumerate(forms):
        if form in target_types:
            accession = accessions[i].replace('-', '')
            doc = primary_docs[i]
            filing_url = f"https://www.sec.gov/Archives/edgar/data/{cik}/{accession}/{doc}"
            filing_date = dates[i] if i < len(dates) else "unknown"
            results.append((filing_url, form, filing_date))
            if len(results) >= count:
                break

    if not results:
        raise ValueError(f"No {filing_type or '10-K/10-Q'} found for CIK {cik}")

    return results


def html_table_to_markdown(table_html: str) -> str:
    """Convert an HTML table to markdown format."""
    # Extract rows
    rows = re.findall(r'<tr[^>]*>(.*?)</tr>', table_html, re.DOTALL | re.IGNORECASE)
    if not rows:
        return ""

    md_rows = []
    for row in rows:
        # Extract cells (th or td)
        cells = re.findall(r'<t[hd][^>]*>(.*?)</t[hd]>', row, re.DOTALL | re.IGNORECASE)
        if not cells:
            continue
        # Clean cell content
        cleaned = []
        for cell in cells:
            # Strip tags, decode entities, normalize whitespace
            text = re.sub(r'<[^>]+>', ' ', cell)
            text = unescape(text)
            text = re.sub(r'\s+', ' ', text).strip()
            # Escape pipe characters
            text = text.replace('|', '\\|')
            cleaned.append(text)
        if any(cleaned):  # Skip empty rows
            md_rows.append('| ' + ' | '.join(cleaned) + ' |')

    if len(md_rows) < 1:
        return ""

    # Add header separator after first row
    num_cols = md_rows[0].count('|') - 1
    separator = '|' + '---|' * num_cols

    if len(md_rows) >= 1:
        result = md_rows[0] + '\n' + separator
        if len(md_rows) > 1:
            result += '\n' + '\n'.join(md_rows[1:])
        return result
    return ""


def strip_html(html: str) -> str:
    """Convert HTML to clean text, preserving tables as markdown."""
    # Remove script/style/xml tags
    html = re.sub(r'<script[^>]*>.*?</script>', ' ', html, flags=re.DOTALL | re.IGNORECASE)
    html = re.sub(r'<style[^>]*>.*?</style>', ' ', html, flags=re.DOTALL | re.IGNORECASE)
    html = re.sub(r'<xml[^>]*>.*?</xml>', ' ', html, flags=re.DOTALL | re.IGNORECASE)

    # Convert tables to markdown before stripping other tags
    def replace_table(match):
        md = html_table_to_markdown(match.group(0))
        return '\n\n' + md + '\n\n' if md else ' '

    html = re.sub(r'<table[^>]*>.*?</table>', replace_table, html, flags=re.DOTALL | re.IGNORECASE)

    # Strip remaining tags
    html = re.sub(r'<[^>]+>', ' ', html)

    # Decode entities
    html = unescape(html)

    # Normalize whitespace but preserve structure
    html = re.sub(r'[ \t]+', ' ', html)
    html = re.sub(r'\n[ \t]+', '\n', html)
    html = re.sub(r'\n{3,}', '\n\n', html)

    return html.strip()


def main():
    parser = argparse.ArgumentParser(
        description="Download SEC EDGAR filings as clean text for LLM analysis",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("ticker", nargs="?", help="Stock ticker symbol")
    parser.add_argument("--cik", help="CIK number")
    parser.add_argument("--url", help="Direct filing URL")
    parser.add_argument("--type", help="Filing type (default: most recent 10-K or 10-Q)")
    parser.add_argument("--count", type=int, default=1, help="Number of filings to download (default: 1)")
    parser.add_argument("--save", help="Save output to file (prefix for multiple filings)")
    parser.add_argument("--raw", action="store_true", help="Keep raw HTML instead of stripping")
    parser.add_argument("--no-cache", action="store_true", help="Skip cache, re-download from SEC")
    parser.add_argument("--list-cache", action="store_true", help="List cached filings and exit")
    parser.add_argument("--quiet", action="store_true", help="Suppress status messages")

    args = parser.parse_args()

    if args.list_cache:
        list_cache()
        return

    if not any([args.ticker, args.cik, args.url]):
        parser.print_help()
        sys.exit(1)

    def log(msg):
        if not args.quiet:
            print(msg, file=sys.stderr)

    # Get filing URL(s)
    if args.url:
        filings = [(args.url, args.type or "filing", "unknown")]
    else:
        cik = args.cik or get_cik_from_ticker(args.ticker)
        log(f"CIK: {cik}")
        filings = get_filing_urls(cik, args.type, args.count)

    # Process each filing
    for idx, (filing_url, filing_type, filing_date) in enumerate(filings):
        # Check cache first
        cache_path = get_cache_path(filing_url) if not args.no_cache else None
        if cache_path and cache_path.exists():
            html_content = cache_path.read_bytes()
            log(f"Cache hit: {cache_path} ({len(html_content):,} bytes)")
        else:
            log(f"Fetching: {filing_url}")
            html_content = fetch_url(filing_url)
            log(f"Downloaded: {len(html_content):,} bytes")
            # Cache raw HTML
            if cache_path:
                cache_path.parent.mkdir(parents=True, exist_ok=True)
                cache_path.write_bytes(html_content)
                accession = cache_path.parent.name
                update_cache_index(accession, args.ticker or args.cik or "unknown", filing_type, filing_date, len(html_content))
                log(f"Cached: {cache_path}")

        # Process
        if args.raw:
            output = html_content.decode('utf-8', errors='replace')
        else:
            html = html_content.decode('utf-8', errors='replace')
            output = strip_html(html)
            log(f"Text length: {len(output):,} chars")

        # Output
        if args.save:
            if args.count > 1:
                # Multiple filings: use prefix-type-date.txt format
                save_path = f"{args.save}-{filing_type}-{filing_date}.txt"
            else:
                save_path = args.save
            Path(save_path).write_text(output, encoding='utf-8')
            log(f"Saved to: {save_path}")
        else:
            if args.count > 1:
                print(f"\n{'='*60}\n{filing_type} - {filing_date}\n{'='*60}\n")
            print(output)


if __name__ == "__main__":
    main()
