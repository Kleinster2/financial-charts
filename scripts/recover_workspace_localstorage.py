#!/usr/bin/env python3
"""
Recover charting-sandbox workspace cards from browser localStorage.

The sandbox persists its chart cards under the localStorage key ``sandbox_cards``
(origin http://localhost:5000). Browsers store localStorage in a LevelDB at
``…/Local Storage/leveldb``, where values are UTF-16LE and the SSTable data
blocks are Snappy-compressed. This tool reads those stores directly (read-only,
no LevelDB lock) — handy when the backend ``workspace.json`` lost content that
git/backups never captured, but an older browser snapshot still holds it.

No third-party deps: a minimal pure-Python Snappy decompressor + SSTable block
reader are included, so it runs offline where ``plyvel`` / ``ccl_chromium_reader``
aren't installable.

Usage:
    python scripts/recover_workspace_localstorage.py                 # scan all browsers
    python scripts/recover_workspace_localstorage.py --browsers edge windsurf
    python scripts/recover_workspace_localstorage.py --out /tmp/recovery

Outputs to --out (default charting_app/recovered_snapshots/):
    all_snapshots.json      every distinct sandbox_cards array found, with metadata
    largest_snapshot.json   the snapshot with the most cards (best full-state copy)

Background: docs note [[project_workspace_recovery]] (2026-06-21 recovery).
"""
import argparse
import datetime
import glob
import hashlib
import json
import os
from collections import defaultdict

# Default Windows localStorage locations for browsers that have hosted the sandbox.
DEFAULT_DIRS = {
    'edge': r'C:\Users\{user}\AppData\Local\Microsoft\Edge\User Data\Default\Local Storage\leveldb',
    'chrome': r'C:\Users\{user}\AppData\Local\Google\Chrome\User Data\Default\Local Storage\leveldb',
    'windsurf': r'C:\Users\{user}\AppData\Roaming\Windsurf\Local Storage\leveldb',
}


# ---------------------------------------------------------------- snappy ----
def snappy_decompress(data):
    """Decompress a raw Snappy block (no framing). Pure Python."""
    pos = 0
    while data[pos] & 0x80:          # skip preamble varint (uncompressed length)
        pos += 1
    pos += 1
    out = bytearray()
    n = len(data)
    while pos < n:
        tag = data[pos]; pos += 1
        t = tag & 0x03
        if t == 0:                                    # literal
            lit = tag >> 2
            if lit < 60:
                lit += 1
            else:
                extra = lit - 59
                lit = int.from_bytes(data[pos:pos + extra], 'little') + 1
                pos += extra
            out += data[pos:pos + lit]; pos += lit
        else:                                         # copy
            if t == 1:
                length = ((tag >> 2) & 0x07) + 4
                off = ((tag >> 5) << 8) | data[pos]; pos += 1
            elif t == 2:
                length = (tag >> 2) + 1
                off = int.from_bytes(data[pos:pos + 2], 'little'); pos += 2
            else:
                length = (tag >> 2) + 1
                off = int.from_bytes(data[pos:pos + 4], 'little'); pos += 4
            start = len(out) - off
            if start < 0:
                raise ValueError('bad snappy copy offset')
            for k in range(length):
                out.append(out[start + k])
    return bytes(out)


# --------------------------------------------------------------- sstable ----
def _read_varint(data, pos):
    result = shift = 0
    while True:
        b = data[pos]; pos += 1
        result |= (b & 0x7f) << shift
        if not (b & 0x80):
            return result, pos
        shift += 7


def _read_block(data, offset, size):
    """Return the (decompressed) bytes of an SSTable block, or None if codec unknown."""
    raw = data[offset:offset + size]
    ctype = data[offset + size]      # 1 byte compression type after the block body
    if ctype == 0:
        return raw
    if ctype == 1:
        return snappy_decompress(raw)
    return None                      # zstd/other not supported


def _data_block_handles(data):
    """Parse the SSTable footer + index block -> list of (offset, size) for data blocks."""
    footer = data[-48:]
    pos = 0
    _, pos = _read_varint(footer, pos)   # metaindex handle (skip)
    _, pos = _read_varint(footer, pos)
    idx_off, pos = _read_varint(footer, pos)
    idx_size, pos = _read_varint(footer, pos)
    idx = _read_block(data, idx_off, idx_size)
    if idx is None:
        return []
    num_restarts = int.from_bytes(idx[-4:], 'little')
    entries_end = len(idx) - 4 - num_restarts * 4
    pos = 0
    last_key = b''
    handles = []
    while pos < entries_end:
        shared, pos = _read_varint(idx, pos)
        nonshared, pos = _read_varint(idx, pos)
        vlen, pos = _read_varint(idx, pos)
        last_key = last_key[:shared] + idx[pos:pos + nonshared]
        pos += nonshared
        val = idx[pos:pos + vlen]; pos += vlen
        vp = 0
        boff, vp = _read_varint(val, vp)
        bsize, vp = _read_varint(val, vp)
        handles.append((boff, bsize))
    return handles


# ------------------------------------------------------------ json scan ----
def _scan(data, s, step):
    """Bracket-balance scan from s. step=1 (latin1) or 2 (utf16le, low byte at j)."""
    n = len(data)
    depth = 0
    in_str = esc = False
    j = s
    while j < n:
        c = data[j]
        hi = data[j + 1] if step == 2 and j + 1 < n else 0
        if step == 1 or hi == 0:
            if in_str:
                if esc:
                    esc = False
                elif c == 0x5c:
                    esc = True
                elif c == 0x22:
                    in_str = False
            elif c == 0x22:
                in_str = True
            elif c == 0x5b:
                depth += 1
            elif c == 0x5d:
                depth -= 1
                if depth == 0:
                    return data[s:j + step]
        j += step
        if j - s > 12_000_000:       # safety cap
            return None
    return None


def _find_card_arrays(data):
    """Yield byte-slices of balanced JSON arrays that start like a cards array."""
    for needle, step in ((b'[{"', 1), (b'[\x00{\x00"\x00', 2)):
        i = 0
        while True:
            s = data.find(needle, i)
            if s == -1:
                break
            slc = _scan(data, s, step)
            if slc:
                yield slc
                i = s + len(slc)
            else:
                i = s + 1


def _parse_cards(slc):
    attempts = []
    if b'\x00' in slc[:8]:
        attempts.append(lambda b: json.loads(b.decode('utf-16-le')))
    attempts += [json.loads, lambda b: json.loads(b.decode('latin-1'))]
    for fn in attempts:
        try:
            v = fn(slc)
            if isinstance(v, list) and v and isinstance(v[0], dict) and 'page' in v[0]:
                return v
        except Exception:
            pass
    return None


# ----------------------------------------------------------------- main ----
def recover(dirs):
    """Return a list of distinct recovered snapshots, richest first."""
    seen = {}
    results = []
    for browser, d in dirs.items():
        if not os.path.isdir(d):
            print(f"  [skip] {browser}: no leveldb dir at {d}")
            continue
        files = sorted(glob.glob(os.path.join(d, '*.ldb')) + glob.glob(os.path.join(d, '*.log')))
        for path in files:
            data = open(path, 'rb').read()
            buffers = []
            if path.endswith('.ldb'):
                try:
                    for off, size in _data_block_handles(data):
                        blk = _read_block(data, off, size)
                        if blk:
                            buffers.append(blk)
                except Exception:
                    buffers.append(data)   # fall back to raw (uncompressed regions)
            else:
                buffers.append(data)
            for buf in buffers:
                for slc in _find_card_arrays(buf):
                    cards = _parse_cards(slc)
                    if not cards:
                        continue
                    key = repr([(str(c.get('page')), str(c.get('title', ''))[:60]) for c in cards])
                    h = hashlib.md5(key.encode()).hexdigest()
                    if h in seen:
                        continue
                    seen[h] = True
                    pc = defaultdict(int)
                    for c in cards:
                        try:
                            pg = int(c.get('page', 1))
                        except (TypeError, ValueError):
                            pg = -1
                        pc[pg] += 1
                    results.append({
                        'browser': browser,
                        'file': os.path.basename(path),
                        'mtime': datetime.datetime.fromtimestamp(os.path.getmtime(path)).isoformat(),
                        'total': len(cards),
                        'per_page': dict(sorted(pc.items())),
                        'cards': cards,
                    })
    results.sort(key=lambda r: r['total'], reverse=True)
    return results


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--browsers', nargs='+', default=list(DEFAULT_DIRS),
                    choices=list(DEFAULT_DIRS), help='browsers to scan (default: all)')
    ap.add_argument('--out', default='charting_app/recovered_snapshots',
                    help='output dir for recovered JSON (default: charting_app/recovered_snapshots)')
    ap.add_argument('--user', default=os.environ.get('USERNAME', 'klein'),
                    help='Windows username for default localStorage paths')
    args = ap.parse_args()

    dirs = {b: DEFAULT_DIRS[b].format(user=args.user) for b in args.browsers}
    results = recover(dirs)

    print(f"\nRecovered {len(results)} distinct sandbox_cards snapshots\n")
    print(f"{'browser':<8} {'file':<14} {'date':<11} {'cards':>5}  top pages (page:count)")
    print('-' * 90)
    for r in results:
        top = " ".join(f"{p}:{n}" for p, n in sorted(r['per_page'].items(), key=lambda x: -x[1])[:6])
        print(f"{r['browser']:<8} {r['file']:<14} {r['mtime'][:10]:<11} {r['total']:>5}  {top}")

    os.makedirs(args.out, exist_ok=True)
    json.dump(results, open(os.path.join(args.out, 'all_snapshots.json'), 'w', encoding='utf-8'), indent=1)
    if results:
        json.dump(results[0]['cards'],
                  open(os.path.join(args.out, 'largest_snapshot.json'), 'w', encoding='utf-8'), indent=1)
    print(f"\nSaved {len(results)} snapshots to {args.out}/")


if __name__ == '__main__':
    main()
