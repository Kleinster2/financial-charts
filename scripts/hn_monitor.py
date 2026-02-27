#!/usr/bin/env python3
"""
Monitor Hacker News for stories mentioning vault actors.

Usage:
    python scripts/hn_monitor.py              # Check top 60 stories
    python scripts/hn_monitor.py --best       # Check "best" stories
    python scripts/hn_monitor.py --top 100    # Check top 100 stories
    python scripts/hn_monitor.py --new        # Check newest stories
"""

import argparse
import json
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from urllib.request import urlopen, Request
from urllib.error import URLError

HN_API = "https://hacker-news.firebaseio.com/v0"
VAULT_ROOT = Path(__file__).parent.parent / "investing"


def fetch_json(url: str, retries: int = 2) -> dict | list | None:
    """Fetch JSON from URL with retries."""
    for attempt in range(retries + 1):
        try:
            req = Request(url, headers={"User-Agent": "hn-monitor/1.0"})
            with urlopen(req, timeout=10) as resp:
                return json.loads(resp.read())
        except (URLError, TimeoutError) as e:
            if attempt < retries:
                time.sleep(1)
            else:
                print(f"  Failed to fetch {url}: {e}", file=sys.stderr)
                return None


# Names that match too broadly in HN titles (common English words, tech terms)
BLOCKLIST = {
    "index ventures", "index", "frame", "block", "command", "storage",
    "progressive", "opendoor", "hive digital", "jump trading",
    "california", "stanford", "postgres", "stepstone group",
    "ba&sh", "bash", "hugo boss", "maker", "makerdao",
    "anywhere real estate", "sprint",
}


def load_vault_entities() -> dict[str, str]:
    """Load vault actor/concept names and aliases for matching.
    
    Returns dict of lowercase_name -> original_name.
    """
    entities = {}
    
    for folder in ["Actors", "Concepts", "Events", "Products"]:
        folder_path = VAULT_ROOT / folder
        if not folder_path.exists():
            continue
        
        for md_file in folder_path.glob("*.md"):
            name = md_file.stem
            # Skip very short names (too many false positives)
            if len(name) < 5:
                continue
            if name.lower() not in BLOCKLIST:
                entities[name.lower()] = name
            
            # Parse aliases from frontmatter
            try:
                content = md_file.read_text(encoding="utf-8")
                if content.startswith("---"):
                    end = content.find("---", 3)
                    if end != -1:
                        frontmatter = content[3:end]
                        alias_match = re.search(r'aliases:\s*\[([^\]]*)\]', frontmatter)
                        if alias_match:
                            aliases = [a.strip().strip('"\'') for a in alias_match.group(1).split(',')]
                            for alias in aliases:
                                alias = alias.strip()
                                if len(alias) >= 5 and alias.lower() not in BLOCKLIST:
                                    entities[alias.lower()] = name
            except Exception:
                pass
    
    return entities


def match_entities(text: str, entities: dict[str, str]) -> list[str]:
    """Find vault entities mentioned in text. Returns list of original names."""
    if not text:
        return []
    
    text_lower = text.lower()
    matched = set()
    
    # Sort by length descending to match longer names first
    for key, name in sorted(entities.items(), key=lambda x: len(x[0]), reverse=True):
        if name in matched:
            continue
        # Word boundary match
        if re.search(rf'\b{re.escape(key)}\b', text_lower):
            matched.add(name)
    
    return sorted(matched)


def get_story_ids(mode: str) -> list[int]:
    """Get story IDs from HN API."""
    endpoint = {
        "top": "topstories",
        "best": "beststories",
        "new": "newstories",
    }.get(mode, "topstories")
    
    data = fetch_json(f"{HN_API}/{endpoint}.json")
    return data if data else []


def get_item(item_id: int) -> dict | None:
    """Get a single HN item."""
    return fetch_json(f"{HN_API}/item/{item_id}.json")


def main():
    parser = argparse.ArgumentParser(description="Monitor HN for vault-relevant stories")
    parser.add_argument("--top", type=int, default=60, help="Number of stories to check (default: 60)")
    parser.add_argument("--best", action="store_true", help="Use 'best' stories instead of 'top'")
    parser.add_argument("--new", action="store_true", help="Use 'new' stories instead of 'top'")
    parser.add_argument("--all", action="store_true", help="Show all stories, not just matches")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    args = parser.parse_args()
    
    mode = "best" if args.best else ("new" if args.new else "top")
    
    print(f"Loading vault entities...", file=sys.stderr)
    entities = load_vault_entities()
    print(f"  {len(entities)} searchable terms from vault", file=sys.stderr)
    
    print(f"Fetching HN {mode} stories...", file=sys.stderr)
    story_ids = get_story_ids(mode)[:args.top]
    print(f"  Checking {len(story_ids)} stories...", file=sys.stderr)
    
    # Fetch all items in parallel (HN API is Firebase, handles concurrency fine)
    items_by_id = {}
    with ThreadPoolExecutor(max_workers=10) as pool:
        futures = {pool.submit(get_item, sid): sid for sid in story_ids}
        for future in as_completed(futures):
            sid = futures[future]
            try:
                items_by_id[sid] = future.result()
            except Exception:
                pass
    
    results = []
    for i, sid in enumerate(story_ids):
        item = items_by_id.get(sid)
        if not item or item.get("type") != "story":
            continue
        
        title = item.get("title", "")
        url = item.get("url", "")
        text = item.get("text", "")
        score = item.get("score", 0)
        comments = item.get("descendants", 0)
        hn_url = f"https://news.ycombinator.com/item?id={sid}"
        
        search_text = f"{title} {url} {text}"
        matches = match_entities(search_text, entities)
        
        if matches or args.all:
            result = {
                "rank": i + 1,
                "title": title,
                "url": url,
                "hn_url": hn_url,
                "score": score,
                "comments": comments,
                "matches": matches,
            }
            results.append(result)
    
    # Output
    matched_results = [r for r in results if r["matches"]]
    
    if args.json:
        print(json.dumps(results, indent=2))
    else:
        if matched_results:
            print(f"\n{'='*70}")
            print(f"VAULT MATCHES ({len(matched_results)} stories)")
            print(f"{'='*70}\n")
            
            for r in matched_results:
                actors = ", ".join(f"[[{m}]]" for m in r["matches"])
                print(f"#{r['rank']:>2} | {r['score']:>4}pts | {r['comments']:>3}c | {r['title']}")
                print(f"     {r['url'] or '(text post)'}")
                print(f"     HN: {r['hn_url']}")
                print(f"     Actors: {actors}")
                print()
        else:
            print("\nNo vault-relevant stories found in current HN front page.")
        
        if args.all:
            unmatched = [r for r in results if not r["matches"]]
            if unmatched:
                print(f"\n{'='*70}")
                print(f"OTHER STORIES ({len(unmatched)})")
                print(f"{'='*70}\n")
                for r in unmatched:
                    print(f"#{r['rank']:>2} | {r['score']:>4}pts | {r['comments']:>3}c | {r['title']}")


if __name__ == "__main__":
    main()
