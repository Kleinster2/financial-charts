#!/usr/bin/env python3
"""
Batch refresh all price charts in the vault.

Scans all .md files for chart embeds, parses filenames, and regenerates
each chart from the API. Supports parallel execution for speed.

Usage:
    python scripts/refresh_all_charts.py [--dry-run] [--workers N] [--verbose]
"""

import argparse
import re
import os
import sys
from pathlib import Path
from datetime import datetime, timedelta
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import urlencode
import requests

# Configuration
VAULT_ROOT = Path(__file__).parent.parent / "investing"
ATTACHMENTS_DIR = VAULT_ROOT / "attachments"
API_BASE = "http://localhost:5000/api/chart/lw"
DEFAULT_WORKERS = 2
DEFAULT_TIMEOUT = 60

# Regex to find chart embeds in markdown
EMBED_PATTERN = re.compile(r'!\[\[([^\]]+\.png)\]\]')


def parse_duration(duration_str):
    """Parse duration like '90d', '1y' into a start date string."""
    match = re.match(r'^(\d+)(d|y)$', duration_str, re.IGNORECASE)
    if not match:
        return None

    num = int(match.group(1))
    unit = match.group(2).lower()

    if unit == 'y':
        days = num * 365
    else:
        days = num

    start = datetime.now() - timedelta(days=days)
    return start.strftime('%Y-%m-%d')


def parse_chart_filename(filename):
    """
    Parse a chart filename to extract API parameters.

    Returns dict with keys: tickers, normalize, start, sort_by_last
    Or None if pattern not recognized.
    """
    name = filename.replace('.png', '')

    # Skip fundamentals charts
    if 'fundamentals' in name.lower():
        return None

    # Skip non-price charts (custom names that don't match patterns)
    # Pattern 1: comparison charts (ticker-vs-ticker[-year].png)
    if '-vs-' in name:
        # Extract year suffix if present
        year_match = re.search(r'-(\d{4})$', name)
        start_year = year_match.group(1) if year_match else None
        name_without_year = re.sub(r'-\d{4}$', '', name) if start_year else name

        # Check for -fx suffix
        is_forex = name_without_year.endswith('-fx')
        if is_forex:
            name_without_year = name_without_year[:-3]

        # Split on -vs-
        segments = name_without_year.split('-vs-')
        tickers = []
        for seg in segments:
            ticker = seg.replace('-price-chart', '').replace('_', '.').upper()
            if is_forex:
                ticker += '=X'
            tickers.append(ticker)

        if len(tickers) < 2:
            return None

        # Validate tickers
        for t in tickers:
            if not re.match(r'^[A-Z0-9.]{1,15}(=X)?$', t):
                return None

        params = {
            'tickers': tickers,
            'normalize': True,
            'sort_by_last': True,
        }
        if start_year:
            params['start'] = f'{start_year}-01-01'

        return params

    # Pattern 2: single ticker price chart (ticker-price-chart[-year].png)
    if '-price-chart' in name:
        year_match = re.search(r'-(\d{4})$', name)
        start_year = year_match.group(1) if year_match else None

        ticker = name
        if start_year:
            ticker = re.sub(r'-\d{4}$', '', ticker)
        ticker = ticker.replace('-price-chart', '').replace('_', '.').upper()

        if not re.match(r'^[A-Z0-9.]{1,15}$', ticker):
            return None

        params = {
            'tickers': [ticker],
            'normalize': False,
        }
        if start_year:
            params['start'] = f'{start_year}-01-01'

        return params

    # Pattern 3: duration chart (ticker-90d.png, ticker-1y.png)
    duration_match = re.match(r'^(.+)-(\d+[dy])$', name, re.IGNORECASE)
    if duration_match:
        ticker = duration_match.group(1).replace('_', '.').upper()
        duration = duration_match.group(2)

        if not re.match(r'^[A-Z0-9.]{1,15}$', ticker):
            return None

        start = parse_duration(duration)
        if not start:
            return None

        return {
            'tickers': [ticker],
            'normalize': False,
            'start': start,
        }

    # Unknown pattern
    return None


def build_api_url(params):
    """Build API URL from parsed parameters."""
    query = {
        'tickers': ','.join(params['tickers']),
    }
    if params.get('normalize'):
        query['normalize'] = 'true'
    if params.get('start'):
        query['start'] = params['start']
    if params.get('sort_by_last'):
        query['sort_by_last'] = 'true'

    return f"{API_BASE}?{urlencode(query)}"


def find_all_chart_embeds():
    """Scan all markdown files and find chart embeds."""
    charts = {}  # filename -> set of source notes

    for md_file in VAULT_ROOT.rglob('*.md'):
        try:
            content = md_file.read_text(encoding='utf-8')
            for match in EMBED_PATTERN.finditer(content):
                filename = match.group(1)
                if filename not in charts:
                    charts[filename] = set()
                charts[filename].add(str(md_file.relative_to(VAULT_ROOT)))
        except Exception as e:
            print(f"Warning: Could not read {md_file}: {e}", file=sys.stderr)

    return charts


def refresh_chart(filename, params, dry_run=False, verbose=False):
    """Fetch chart from API and save to attachments folder."""
    url = build_api_url(params)
    output_path = ATTACHMENTS_DIR / filename

    if dry_run:
        return True, f"Would fetch: {url}"

    try:
        response = requests.get(url, timeout=DEFAULT_TIMEOUT)
        if response.status_code != 200:
            return False, f"API error {response.status_code}"

        output_path.write_bytes(response.content)
        return True, f"OK ({len(response.content)} bytes)"
    except Exception as e:
        return False, str(e)


def main():
    parser = argparse.ArgumentParser(description='Batch refresh all price charts')
    parser.add_argument('--dry-run', action='store_true', help='Show what would be done without doing it')
    parser.add_argument('--workers', type=int, default=DEFAULT_WORKERS, help=f'Number of parallel workers (default: {DEFAULT_WORKERS})')
    parser.add_argument('--verbose', '-v', action='store_true', help='Show detailed output')
    args = parser.parse_args()

    # Check API is running
    if not args.dry_run:
        try:
            response = requests.get(API_BASE.replace('/api/chart/lw', '/'), timeout=5)
            if response.status_code >= 400:
                print("Error: Flask app not responding. Start it with: python charting_app/app.py", file=sys.stderr)
                sys.exit(1)
        except requests.exceptions.ConnectionError:
            print("Error: Cannot connect to Flask app. Start it with: python charting_app/app.py", file=sys.stderr)
            sys.exit(1)

    # Find all chart embeds
    print("Scanning vault for chart embeds...")
    all_charts = find_all_chart_embeds()
    print(f"Found {len(all_charts)} unique chart files referenced in notes")

    # Parse and filter to recognized patterns
    to_refresh = []
    skipped = []

    for filename, sources in all_charts.items():
        params = parse_chart_filename(filename)
        if params:
            to_refresh.append((filename, params, sources))
        else:
            skipped.append((filename, sources))

    print(f"  Recognized patterns: {len(to_refresh)}")
    print(f"  Skipped (unknown/fundamentals): {len(skipped)}")

    if args.verbose and skipped:
        print("\nSkipped files:")
        for filename, sources in skipped[:10]:
            print(f"  {filename}")
        if len(skipped) > 10:
            print(f"  ... and {len(skipped) - 10} more")

    if not to_refresh:
        print("Nothing to refresh.")
        return

    # Refresh charts in parallel
    print(f"\nRefreshing {len(to_refresh)} charts with {args.workers} workers...")

    success = 0
    failed = 0

    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = {
            executor.submit(refresh_chart, filename, params, args.dry_run, args.verbose): filename
            for filename, params, sources in to_refresh
        }

        for future in as_completed(futures):
            filename = futures[future]
            ok, msg = future.result()
            if ok:
                success += 1
                if args.verbose or args.dry_run:
                    print(f"  [OK] {filename}: {msg}")
            else:
                failed += 1
                print(f"  [FAIL] {filename}: {msg}", file=sys.stderr)

    # Summary
    print(f"\nDone: {success} refreshed, {failed} failed")

    if failed > 0:
        sys.exit(1)


if __name__ == '__main__':
    main()
