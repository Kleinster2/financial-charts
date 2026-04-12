"""Shared download utilities for per-service chart/image ingestion scripts.

Usage pattern:
    from scripts.lib.download_utils import download_validated, run_batch

    JOBS = [(url, "file-name.png"), ...]
    run_batch(JOBS, out_dir="investing/attachments", headers={...})

Safety guarantees:
    - Validates Content-Type header against expected MIME type
    - Validates file-format magic bytes before write (catches HTML error pages
      served with a misleading content-type)
    - Atomic write via .part temp file + os.replace
    - Returns non-zero exit code from run_batch if any download failed
"""
import os
import sys
import urllib.request

DEFAULT_UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"
)

MAGIC_BYTES = {
    "image/png": b"\x89PNG\r\n\x1a\n",
    "image/jpeg": b"\xff\xd8\xff",
    "image/gif": b"GIF8",
    "image/webp": b"RIFF",
    "application/pdf": b"%PDF-",
}

MIME_FROM_EXT = {
    ".png": "image/png",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".gif": "image/gif",
    ".webp": "image/webp",
    ".pdf": "application/pdf",
}


def infer_mime(path):
    """Guess MIME from file extension; return None if unknown."""
    _, ext = os.path.splitext(path.lower())
    return MIME_FROM_EXT.get(ext)


def download_validated(url, out_path, headers=None, expect_mime=None, timeout=30, min_bytes=0):
    """Download url to out_path atomically, validating content type and magic bytes.

    Args:
        url: source URL
        out_path: final destination path
        headers: optional dict of request headers (default: User-Agent only)
        expect_mime: MIME type to enforce (default: inferred from out_path extension)
        timeout: socket timeout seconds
        min_bytes: minimum response size to accept (default 0 — any size)

    Returns:
        number of bytes written

    Raises:
        ValueError: content-type mismatch, magic-byte mismatch, or too small
        urllib.error.URLError: network failure
    """
    if expect_mime is None:
        expect_mime = infer_mime(out_path)
    req_headers = {"User-Agent": DEFAULT_UA}
    if headers:
        req_headers.update(headers)

    req = urllib.request.Request(url, headers=req_headers)
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        if expect_mime:
            ctype = resp.headers.get("Content-Type", "").lower()
            if expect_mime not in ctype:
                raise ValueError(f"expected Content-Type {expect_mime}, got {ctype!r}")
        data = resp.read()

    if len(data) < min_bytes:
        raise ValueError(f"response too small: {len(data)} bytes < min {min_bytes}")

    if expect_mime in MAGIC_BYTES:
        magic = MAGIC_BYTES[expect_mime]
        if not data.startswith(magic):
            raise ValueError(f"magic-byte mismatch for {expect_mime} (got {data[:8]!r})")

    tmp = out_path + ".part"
    try:
        with open(tmp, "wb") as f:
            f.write(data)
        os.replace(tmp, out_path)
    except Exception:
        if os.path.exists(tmp):
            try:
                os.remove(tmp)
            except OSError:
                pass
        raise

    return len(data)


def run_batch(jobs, out_dir, headers=None, skip_if_larger_than=10000, expect_mime=None):
    """Run a batch of (url, filename) downloads. Skip existing files above threshold.

    Args:
        jobs: iterable of (url, filename) pairs
        out_dir: directory to write into (created if missing)
        headers: optional request headers shared across all downloads
        skip_if_larger_than: skip if destination exists and is larger than N bytes
        expect_mime: MIME enforced for all jobs; None means infer per-file from extension

    Exits 0 on all-success, 1 on any failure (with failed filenames printed).
    """
    os.makedirs(out_dir, exist_ok=True)
    ok, fail, failures = 0, 0, []

    for url, name in jobs:
        out_path = os.path.join(out_dir, name)
        if os.path.exists(out_path) and os.path.getsize(out_path) > skip_if_larger_than:
            print(f"SKIP (exists): {name}")
            ok += 1
            continue
        try:
            size = download_validated(url, out_path, headers=headers, expect_mime=expect_mime)
            print(f"OK {size/1024:.0f}KB: {name}")
            ok += 1
        except Exception as e:
            print(f"FAIL: {name} — {e}")
            fail += 1
            failures.append(name)

    total = ok + fail
    print(f"\n{ok} ok / {fail} fail / {total} total")
    if failures:
        print("Failed:", ", ".join(failures))
        sys.exit(1)
