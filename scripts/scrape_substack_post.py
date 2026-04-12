"""Scrape a Substack post URL to metadata + markdown body + image download jobs.

Usage:
    python scripts/scrape_substack_post.py URL
    python scripts/scrape_substack_post.py URL --download DIR
    python scripts/scrape_substack_post.py URL --body-out body.md
    python scripts/scrape_substack_post.py - < post.html        # paywalled fallback: paste HTML

Output (stdout):
    - Metadata header (title, author, publication, date, URL, image count)
    - JOBS list: [(s3_url, suggested_filename), ...] ready to paste into a per-publication script
      or to feed directly to lib/download_utils.run_batch()
    - Body as markdown (pipe to a file with --body-out, or > somewhere)
"""
import argparse
import json
import os
import re
import sys
import urllib.parse

import requests
from bs4 import BeautifulSoup, NavigableString, Tag

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.download_utils import DEFAULT_UA, run_batch

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

S3_IMAGE_RE = re.compile(
    r'substack-post-media\.s3\.amazonaws\.com/public/images/([^_/]+)_(\d+x\d+)\.([a-zA-Z]+)'
)


def extract_s3_image(src):
    """Return (hash, dims, ext, s3_url) from an img src, or None."""
    if not src:
        return None
    decoded = urllib.parse.unquote(src)
    m = S3_IMAGE_RE.search(decoded)
    if not m:
        return None
    h, dims, ext = m.group(1), m.group(2), m.group(3).lower()
    s3_url = f'https://substack-post-media.s3.amazonaws.com/public/images/{h}_{dims}.{ext}'
    return h, dims, ext, s3_url


def slugify(text, max_len=50):
    if not text:
        return ''
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_-]+', '-', text)
    return text[:max_len].strip('-')


def fetch_html(url):
    resp = requests.get(url, headers={'User-Agent': DEFAULT_UA}, timeout=30)
    resp.raise_for_status()
    return resp.text


def _inline(node):
    """Convert inline content (text + simple tags) to markdown string."""
    out = []
    for child in node.children:
        if isinstance(child, NavigableString):
            out.append(str(child))
        elif isinstance(child, Tag):
            name = child.name
            if name in ('strong', 'b'):
                out.append('**' + _inline(child).strip() + '**')
            elif name in ('em', 'i'):
                out.append('*' + _inline(child).strip() + '*')
            elif name == 'a':
                href = child.get('href', '')
                txt = _inline(child).strip()
                out.append(f'[{txt}]({href})' if href else txt)
            elif name == 'code':
                out.append('`' + child.get_text() + '`')
            elif name == 'br':
                out.append('  \n')
            else:
                out.append(_inline(child))
    return ''.join(out)


def _block(tag):
    """Convert a block-level tag to markdown (returns '' for tags that should be dropped)."""
    name = tag.name
    if name in ('h1', 'h2', 'h3', 'h4', 'h5', 'h6'):
        level = int(name[1])
        return '\n' + '#' * level + ' ' + _inline(tag).strip() + '\n\n'
    if name == 'p':
        txt = _inline(tag).strip()
        return txt + '\n\n' if txt else ''
    if name == 'blockquote':
        inner = _inline(tag).strip()
        return '\n> ' + inner.replace('\n', '\n> ') + '\n\n' if inner else ''
    if name == 'ul':
        items = []
        for li in tag.find_all('li', recursive=False):
            items.append('- ' + _inline(li).strip())
        return '\n' + '\n'.join(items) + '\n\n' if items else ''
    if name == 'ol':
        items = []
        for i, li in enumerate(tag.find_all('li', recursive=False), 1):
            items.append(f'{i}. ' + _inline(li).strip())
        return '\n' + '\n'.join(items) + '\n\n' if items else ''
    if name == 'figure':
        img = tag.find('img')
        cap = tag.find('figcaption')
        caption_text = ''
        if cap:
            caption_text = _inline(cap).strip()
        elif img:
            caption_text = img.get('alt', '') or ''
        return f'\n![{caption_text}](figure)\n\n'
    if name == 'hr':
        return '\n---\n\n'
    if name == 'pre':
        return '\n```\n' + tag.get_text() + '\n```\n\n'
    if name in ('div', 'section', 'article'):
        return ''.join(_block(c) if isinstance(c, Tag) else str(c)
                       for c in tag.children)
    return ''


def html_to_markdown(root):
    return ''.join(
        _block(c) if isinstance(c, Tag) else str(c)
        for c in root.children
    ).strip() + '\n'


def find_body(soup):
    for sel in ('.available-content', '.body.markup', 'div.body', 'article'):
        node = soup.select_one(sel)
        if node:
            return node
    return None


def extract_images(body_node, publication_slug):
    """Walk figures + bare imgs; return list of {hash, dims, ext, s3_url, caption, filename}."""
    images = []
    seen = set()
    if not body_node:
        return images

    def add(h, dims, ext, s3_url, caption, index_hint):
        if h in seen:
            return
        seen.add(h)
        cap_slug = slugify(caption)
        if cap_slug:
            filename = f'{cap_slug}-{publication_slug}.{ext}'
        else:
            filename = f'{publication_slug}-fig{index_hint:02d}.{ext}'
        images.append({
            'hash': h, 'dims': dims, 'ext': ext, 's3_url': s3_url,
            'caption': caption, 'filename': filename,
        })

    idx = 0
    for fig in body_node.find_all('figure'):
        img = fig.find('img')
        if not img:
            continue
        src = img.get('src') or img.get('data-src') or ''
        parsed = extract_s3_image(src)
        if not parsed:
            srcset = img.get('srcset', '')
            if srcset:
                first = srcset.split(',')[0].strip().split(' ')[0]
                parsed = extract_s3_image(first)
        if not parsed:
            continue
        h, dims, ext, s3_url = parsed
        cap = fig.find('figcaption')
        caption = _inline(cap).strip() if cap else (img.get('alt', '') or '')
        idx += 1
        add(h, dims, ext, s3_url, caption, idx)

    for img in body_node.find_all('img'):
        if img.find_parent('figure'):
            continue
        src = img.get('src') or img.get('data-src') or ''
        parsed = extract_s3_image(src)
        if not parsed:
            continue
        h, dims, ext, s3_url = parsed
        caption = img.get('alt', '') or ''
        idx += 1
        add(h, dims, ext, s3_url, caption, idx)

    return images


def _parse_json_ld(soup):
    """Return the first Article-type JSON-LD blob as a dict, or {}."""
    for script in soup.find_all('script', type='application/ld+json'):
        raw = script.string or script.get_text() or ''
        try:
            data = json.loads(raw)
        except (ValueError, TypeError):
            continue
        if isinstance(data, list):
            data = next((d for d in data if isinstance(d, dict)), {})
        if isinstance(data, dict) and data.get('@type') in (
            'NewsArticle', 'Article', 'BlogPosting'
        ):
            return data
    return {}


def parse_post(html, url):
    soup = BeautifulSoup(html, 'html.parser')

    ld = _parse_json_ld(soup)

    title = ld.get('headline') or ''
    if not title:
        h1 = soup.select_one('h1.post-title') or soup.find('h1')
        title = h1.get_text(strip=True) if h1 else ''

    pub_date = ld.get('datePublished') or ''
    if not pub_date:
        time_tag = soup.find('time')
        if time_tag:
            pub_date = time_tag.get('datetime', '') or time_tag.get_text(strip=True)
    if not pub_date:
        meta_pub = soup.find('meta', attrs={'property': 'article:published_time'})
        if meta_pub:
            pub_date = meta_pub.get('content', '')

    author = ''
    ld_author = ld.get('author')
    if isinstance(ld_author, list) and ld_author:
        author = (ld_author[0] or {}).get('name', '')
    elif isinstance(ld_author, dict):
        author = ld_author.get('name', '')
    if not author:
        for sel in (('meta', {'name': 'author'}),
                    ('meta', {'property': 'article:author'})):
            tag = soup.find(*sel)
            if tag and tag.get('content'):
                author = tag.get('content')
                break

    if url and url != '<stdin>':
        parsed = urllib.parse.urlparse(url)
        publication = parsed.netloc.replace('.substack.com', '').split('.')[0]
    else:
        site = soup.find('meta', attrs={'property': 'og:site_name'})
        publication = slugify(site.get('content', '')) if site else 'substack'

    body_node = find_body(soup)
    body_md = html_to_markdown(body_node) if body_node else ''

    paywalled = bool(
        soup.select_one('.paywall-content, .subscription-widget-wrap .subscribe-container')
        and len(body_md) < 500
    )

    images = extract_images(body_node, publication)

    return {
        'url': url, 'title': title, 'author': author, 'date': pub_date,
        'publication': publication, 'body_markdown': body_md,
        'images': images, 'paywalled': paywalled,
    }


def format_jobs(images):
    if not images:
        return 'JOBS = []  # no images found'
    lines = ['JOBS = [']
    for im in images:
        cap = f'  # {im["caption"]}' if im['caption'] else ''
        lines.append(f'    ("{im["s3_url"]}", "{im["filename"]}"),{cap}')
    lines.append(']')
    return '\n'.join(lines)


def main():
    ap = argparse.ArgumentParser(description='Scrape a Substack post URL to metadata + body + image jobs.')
    ap.add_argument('url', help='Substack post URL, or "-" to read HTML from stdin')
    ap.add_argument('--download', metavar='DIR', help='Download images to DIR immediately')
    ap.add_argument('--body-out', metavar='FILE', help='Write body markdown to FILE (default: stdout)')
    ap.add_argument('--tuples-only', action='store_true', help='Skip body markdown in output')
    args = ap.parse_args()

    if args.url == '-':
        html = sys.stdin.read()
        url = '<stdin>'
    else:
        url = args.url
        html = fetch_html(url)

    post = parse_post(html, url)

    print(f'# Title: {post["title"]}')
    print(f'# URL: {post["url"]}')
    print(f'# Author: {post["author"]}')
    print(f'# Publication: {post["publication"]}')
    print(f'# Date: {post["date"]}')
    print(f'# Images: {len(post["images"])}')
    if post['paywalled']:
        print('# NOTE: paywall detected — body may be truncated; pipe HTML via stdin if needed')
    print()

    print(format_jobs(post['images']))
    print()

    if not args.tuples_only:
        if args.body_out:
            with open(args.body_out, 'w', encoding='utf-8') as f:
                f.write(post['body_markdown'])
            print(f'# Body markdown written to {args.body_out}')
        else:
            print('# --- BODY MARKDOWN ---')
            print(post['body_markdown'])

    if args.download:
        jobs = [(im['s3_url'], im['filename']) for im in post['images']]
        if not jobs:
            print('# --download requested but no images found')
            return
        run_batch(jobs, out_dir=args.download)


if __name__ == '__main__':
    main()
