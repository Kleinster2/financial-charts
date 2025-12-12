"""
HTTP utilities with retry/backoff and optional disk caching.

Usage:
    from http_utils import fetch_with_retry, FetchError

    text = fetch_with_retry(
        "https://api.example.com/data",
        params={"id": "foo"},
        retries=3,
        backoff=2,
        timeout=30,
        cache_dir=".http_cache",
        cache_ttl_s=3600,
    )
"""
from __future__ import annotations

import hashlib
import json
import logging
import time
from pathlib import Path
from typing import Any, Mapping, Optional, Union

import requests

logger = logging.getLogger(__name__)


class FetchError(RuntimeError):
    """Exception raised when fetch fails after all retries."""

    def __init__(
        self,
        url: str,
        params: Optional[Mapping[str, Any]] = None,
        kind: str = "unknown",
        status_code: Optional[int] = None,
        last_exc: Optional[Exception] = None,
    ):
        msg = f"{kind} error fetching {url}"
        if status_code is not None:
            msg += f" (HTTP {status_code})"
        if params:
            msg += f" params={dict(params)}"
        if last_exc:
            msg += f": {last_exc}"
        super().__init__(msg)
        self.url = url
        self.params = params
        self.kind = kind
        self.status_code = status_code
        self.last_exc = last_exc


def _cache_key(url: str, params: Optional[Mapping[str, Any]]) -> str:
    """Generate cache key from URL and params."""
    base = url
    if params:
        items = "&".join(f"{k}={params[k]}" for k in sorted(params))
        base = f"{url}?{items}"
    return hashlib.sha256(base.encode("utf-8")).hexdigest()


def _load_cache(cache_dir: Path, key: str, ttl_s: Optional[float]) -> Optional[str]:
    """Load cached response if valid."""
    path = cache_dir / f"{key}.json"
    if not path.exists():
        return None
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
        if ttl_s is not None:
            saved_at = payload.get("saved_at", 0)
            if (time.time() - saved_at) > ttl_s:
                return None
        return payload.get("text")
    except Exception:
        return None


def _save_cache(
    cache_dir: Path,
    key: str,
    url: str,
    params: Optional[Mapping[str, Any]],
    text: str,
):
    """Save response to cache."""
    cache_dir.mkdir(parents=True, exist_ok=True)
    payload = {
        "url": url,
        "params": dict(params) if params else None,
        "saved_at": time.time(),
        "text": text,
    }
    (cache_dir / f"{key}.json").write_text(json.dumps(payload), encoding="utf-8")


def fetch_with_retry(
    url: str,
    params: Optional[Mapping[str, Any]] = None,
    retries: int = 3,
    backoff: float = 2.0,
    timeout: float = 30.0,
    headers: Optional[Mapping[str, str]] = None,
    cache_dir: Optional[Union[str, Path]] = None,
    cache_ttl_s: Optional[float] = None,
) -> str:
    """
    Fetch URL with retry/backoff and optional caching.

    Args:
        url: URL to fetch
        params: Query parameters
        retries: Number of retry attempts (default: 3)
        backoff: Exponential backoff base (default: 2.0, gives 1s, 2s, 4s delays)
        timeout: Request timeout in seconds (default: 30)
        headers: Optional HTTP headers
        cache_dir: Directory for disk cache (None to disable)
        cache_ttl_s: Cache TTL in seconds (None for infinite)

    Returns:
        Response text

    Raises:
        FetchError: On failure after all retries
    """
    cache_path = Path(cache_dir) if cache_dir else None
    key = _cache_key(url, params)

    # Check cache first
    if cache_path:
        cached = _load_cache(cache_path, key, cache_ttl_s)
        if cached is not None:
            logger.debug(f"Cache hit for {url}")
            return cached

    last_exc: Optional[Exception] = None
    last_status: Optional[int] = None
    last_kind = "unknown"

    for attempt in range(retries + 1):
        try:
            resp = requests.get(url, params=params, headers=headers, timeout=timeout)
            last_status = resp.status_code

            if 200 <= resp.status_code < 300:
                text = resp.text
                if cache_path:
                    _save_cache(cache_path, key, url, params, text)
                return text

            # 429 or 5xx -> retry
            if resp.status_code == 429 or resp.status_code >= 500:
                last_kind = "server"
                raise requests.HTTPError(f"HTTP {resp.status_code}", response=resp)

            # Other 4xx -> no retry (client error)
            last_kind = "client"
            resp.raise_for_status()

        except requests.Timeout as e:
            last_kind, last_exc = "timeout", e
        except requests.HTTPError as e:
            last_exc = e
        except requests.RequestException as e:
            last_kind, last_exc = "network", e

        if attempt < retries:
            sleep_s = backoff**attempt  # 1, 2, 4, ... when backoff=2
            logger.warning(
                f"Retry {attempt + 1}/{retries} for {url} ({last_kind}); sleeping {sleep_s:.1f}s"
            )
            time.sleep(sleep_s)

    raise FetchError(
        url, params=params, kind=last_kind, status_code=last_status, last_exc=last_exc
    )
