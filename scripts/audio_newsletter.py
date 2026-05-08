"""Generate an audio version of a daily newsletter via TTS.

Reads `investing/Newsletter/YYYY-MM-DD.md`, adapts the markdown for spoken
delivery (strips wikilink brackets, expands abbreviations and figures into
natural English), then renders to `investing/Newsletter/YYYY-MM-DD.mp3`.

Default mode is auto-fallback: ElevenLabs primary (voice `sarah`) → OpenAI
secondary (voice `nova`) if ElevenLabs fails (auth/quota/network/server).
Pin to one provider with `--provider {elevenlabs,openai}` to disable fallback.

Usage:
    python scripts/audio_newsletter.py 2026-05-07
    python scripts/audio_newsletter.py 2026-05-07 --voice adam
    python scripts/audio_newsletter.py 2026-05-07 --preview     # first chunk only
    python scripts/audio_newsletter.py 2026-05-07 --dry-run     # show adapted text, no API call
    python scripts/audio_newsletter.py 2026-05-07 --provider openai --voice onyx

API keys are read from environment or from `.env` at the repo root.
"""
from __future__ import annotations

import argparse
import io
import os
import re
import sys
from pathlib import Path

# Force UTF-8 stdout/stderr on Windows so the dry-run print doesn't choke on
# em dashes and arrows.
if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

REPO_ROOT = Path(__file__).resolve().parent.parent
NEWSLETTER_DIR = REPO_ROOT / "investing" / "Newsletter"

# OpenAI TTS voices — all work well for English narration. Default = nova
# (clear, warm female, good prosody for analytical content).
OPENAI_VOICES = {
    "alloy", "echo", "fable", "onyx", "nova", "shimmer", "ash", "sage", "coral",
}

# ElevenLabs preset voices (fallback provider).
ELEVENLABS_VOICES = {
    "sarah": "EXAVITQu4vr4xnSDxMaL",     # warm, clear, female
    "adam":  "pNInz6obpgDQGcFmaJgB",     # deep, measured, male
    "rachel": "21m00Tcm4TlvDq8ikWAM",    # neutral, professional, female
    "charlotte": "XB0fDUnXU5powFXDhCwa", # soft, articulate, female
    "george": "JBFqnCBsd6RMkjVDRZzb",    # mature, authoritative, male
    "brian":  "nPczCjzI2devNBz1zQrb",    # warm, conversational, male
}

DEFAULT_OPENAI_VOICE = "nova"
DEFAULT_OPENAI_MODEL = "gpt-4o-mini-tts"
DEFAULT_ELEVENLABS_VOICE = "sarah"
DEFAULT_ELEVENLABS_MODEL = "eleven_multilingual_v2"

# Style instruction for gpt-4o-mini-tts (it accepts free-form direction).
NEWSLETTER_STYLE_INSTRUCTION = (
    "Read in the voice of a financial-newsroom analyst: clear, measured, "
    "analytical. Slightly slower than conversational pace. Pause naturally "
    "at section breaks. Treat tickers (e.g., ZTS, WHR, BKSY) as letter-by-"
    "letter callouts. Numbers should be spoken naturally."
)


def load_env_key(name: str) -> str | None:
    """Read API key from env or repo .env file."""
    key = os.environ.get(name)
    if key:
        return key
    env_path = REPO_ROOT / ".env"
    if env_path.exists():
        for line in env_path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line.startswith(f"{name}="):
                return line.split("=", 1)[1].strip().strip('"').strip("'")
    return None


def strip_frontmatter(text: str) -> str:
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end != -1:
            return text[end + 5:].lstrip()
    return text


def adapt_for_speech(md: str) -> str:
    """Convert markdown to a spoken-friendly plain-text rendering."""
    text = strip_frontmatter(md)

    # Wikilinks: [[Display|Target]] -> Display, [[Entity]] -> Entity
    text = re.sub(r"\[\[([^\]|]+)\|([^\]]+)\]\]", r"\2", text)
    text = re.sub(r"\[\[([^\]]+)\]\]", r"\1", text)

    # Markdown links [text](url) -> text
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)

    # Code spans, bold, italic markers
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)
    text = re.sub(r"(?<!\*)\*([^*\n]+)\*(?!\*)", r"\1", text)

    # Headers: drop the # marks but keep the text on its own line so the TTS
    # treats it as a sentence. The blank lines around it create natural pauses.
    def header_repl(match: re.Match) -> str:
        title = match.group(2).rstrip(".").strip()
        if not title.endswith((".", "!", "?", ":")):
            title += "."
        return title

    text = re.sub(r"^(#{1,6})\s+(.+)$", header_repl, text, flags=re.MULTILINE)

    # Bullets: "- foo" -> "foo" (TTS narrates as a list naturally)
    text = re.sub(r"^\s*[-*]\s+", "", text, flags=re.MULTILINE)

    # Numeric / abbreviation expansions for cleaner speech.
    # Order matters - apply more-specific patterns first.
    expansions = [
        # --- RANGES (must come before single-value patterns) ---
        # Signed percent ranges: -7-9% -> "down 7 to 9 percent"
        (r"\+(\d+(?:\.\d+)?)\s*-\s*(\d+(?:\.\d+)?)\s*%", r"up \1 to \2 percent"),
        (r"-(\d+(?:\.\d+)?)\s*-\s*(\d+(?:\.\d+)?)\s*%", r"down \1 to \2 percent"),
        (r"(\d+(?:\.\d+)?)\s*-\s*(\d+(?:\.\d+)?)\s*%", r"\1 to \2 percent"),
        # Dollar ranges with magnitude: $2.45-2.95B, $775-800M, $7.71-7.87B
        (r"~?\$(\d+(?:\.\d+)?)\s*-\s*(\d+(?:\.\d+)?)\s*[Tt](?=\b|\s|$)", r"\1 to \2 trillion dollars"),
        (r"~?\$(\d+(?:\.\d+)?)\s*-\s*(\d+(?:\.\d+)?)\s*[Bb](?=\b|\s|$)", r"\1 to \2 billion dollars"),
        (r"~?\$(\d+(?:\.\d+)?)\s*-\s*(\d+(?:\.\d+)?)\s*[Mm](?=\b|\s|$)", r"\1 to \2 million dollars"),
        # Dollar range with no magnitude: $6.85-7.00 -> "6.85 to 7.00 dollars"
        (r"~?\$(\d+(?:\.\d+)?)\s*-\s*(\d+(?:\.\d+)?)", r"\1 to \2 dollars"),

        # --- SINGLE PERCENTS ---
        # Trailing-plus form: 90%+ -> "more than 90 percent"
        (r"(\d+(?:\.\d+)?)\s*%\s*\+", r"more than \1 percent"),
        # Signed percent moves
        (r"\+(\d+(?:\.\d+)?)\s*%", r"up \1 percent"),
        (r"-(\d+(?:\.\d+)?)\s*%", r"down \1 percent"),
        (r"(\d+(?:\.\d+)?)\s*%", r"\1 percent"),

        # --- SINGLE DOLLARS ---
        # Magnitude suffixes: $22B, $117.7M, $416M, $1.5T, $5K
        (r"~?\$(\d+(?:\.\d+)?)\s*[Tt](?=\b|\s|$)", r"\1 trillion dollars"),
        (r"~?\$(\d+(?:\.\d+)?)\s*[Bb](?=\b|\s|$)", r"\1 billion dollars"),
        (r"~?\$(\d+(?:\.\d+)?)\s*[Mm](?=\b|\s|$)", r"\1 million dollars"),
        (r"~?\$(\d+(?:\.\d+)?)\s*[Kk](?=\b|\s|$)", r"\1 thousand dollars"),
        # Plain dollar figures: $26 -> "26 dollars", $1,200 -> "1,200 dollars"
        (r"~?\$(\d+(?:,\d{3})*(?:\.\d+)?)", r"\1 dollars"),

        # --- TIME / CALENDAR ABBREVIATIONS ---
        (r"\bQ1\b", "first quarter"),
        (r"\bQ2\b", "second quarter"),
        (r"\bQ3\b", "third quarter"),
        (r"\bQ4\b", "fourth quarter"),
        (r"\bFY\s?(\d{2})\b", lambda m: f"fiscal year 20{m.group(1)}"),
        (r"\bFY\s?(\d{4})\b", r"fiscal year \1"),
        (r"\bH1\b", "first half"),
        (r"\bH2\b", "second half"),

        # --- COMMON FINANCIAL ABBREVIATIONS ---
        (r"\bYoY\b", "year over year"),
        # bps lacks a leading word boundary when stuck to a digit (180bps);
        # match optional digits attached and reinsert.
        (r"(\d)\s*bps\b", r"\1 basis points"),
        (r"\bbps\b", "basis points"),
        (r"\bMoU\b", "memorandum of understanding"),

        # --- MULTIPLIERS / GREEK ---
        (r"(\d+(?:\.\d+)?)\s*x\b", r"\1 times"),
        (r"(\d+(?:\.\d+)?)×", r"\1 times"),
        (r"σ", " sigma"),
        # Cleanup: " - sigma" or "-sigma" -> " sigma"
        (r"-\s+sigma", " sigma"),

        # --- TYPOGRAPHIC CLEANUP ---
        (r"\s+—\s+", ", "),
        (r"—", ", "),
        (r"\s*→\s*", " to "),
        (r"\s*->\s*", " to "),
        (r"…", "..."),
        (r"[“”]", '"'),
        (r"[‘’]", "'"),
        (r"~", "approximately "),

        # --- DEFENSIVE NUMERIC CLEANUPS ---
        # Trailing .00 is awkward to hear: "34.00 dollars" -> "34 dollars"
        (r"(\d+)\.00(\s+(?:dollars|trillion|billion|million|thousand|percent))", r"\1\2"),
        # Underscores in identifiers (script names) -> spaces so they read naturally
        (r"_", " "),
        # Collapse double "percent" if a stray pattern produced one
        (r"\bpercent\s+percent\b", "percent"),
    ]
    for pattern, repl in expansions:
        text = re.sub(pattern, repl, text)

    # Collapse runs of blank lines and trailing whitespace
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = "\n".join(line.rstrip() for line in text.splitlines()).strip()
    return text


def chunk_for_tts(text: str, max_chars: int = 3500) -> list[str]:
    """Split adapted text into chunks under the TTS request limit.

    Splits on paragraph boundaries. Preserves natural section breaks. Keeps
    each chunk under max_chars to stay well within the 5000-char free-tier
    limit and the 10000-char paid limit.
    """
    paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]
    chunks: list[str] = []
    current = ""
    for para in paragraphs:
        candidate = (current + "\n\n" + para) if current else para
        if len(candidate) > max_chars and current:
            chunks.append(current)
            current = para
        else:
            current = candidate
    if current:
        chunks.append(current)
    return chunks


def synthesize_openai(chunks: list[str], voice: str, model: str, api_key: str) -> bytes:
    """Generate MP3 via OpenAI Audio API. Returns concatenated bytes."""
    from openai import OpenAI

    client = OpenAI(api_key=api_key)
    audio_buffer = bytearray()
    kwargs_extra = {}
    if model == "gpt-4o-mini-tts":
        kwargs_extra["instructions"] = NEWSLETTER_STYLE_INSTRUCTION
    for i, chunk in enumerate(chunks, 1):
        sys.stderr.write(f"  [{i}/{len(chunks)}] {len(chunk):>5} chars... ")
        sys.stderr.flush()
        response = client.audio.speech.create(
            model=model,
            voice=voice,
            input=chunk,
            response_format="mp3",
            **kwargs_extra,
        )
        chunk_bytes = response.content
        audio_buffer.extend(chunk_bytes)
        sys.stderr.write(f"{len(chunk_bytes):>7} bytes\n")
    return bytes(audio_buffer)


def synthesize_elevenlabs(chunks: list[str], voice: str, model: str, api_key: str) -> bytes:
    """Generate MP3 via ElevenLabs. Returns concatenated bytes."""
    from elevenlabs.client import ElevenLabs

    voice_id = ELEVENLABS_VOICES.get(voice, voice)
    if voice not in ELEVENLABS_VOICES and not re.fullmatch(r"[A-Za-z0-9]{20}", voice):
        raise ValueError(
            f"Unknown ElevenLabs voice '{voice}'. "
            f"Presets: {', '.join(ELEVENLABS_VOICES)}. Or pass a 20-char voice ID."
        )

    client = ElevenLabs(api_key=api_key)
    audio_buffer = bytearray()
    for i, chunk in enumerate(chunks, 1):
        sys.stderr.write(f"  [{i}/{len(chunks)}] {len(chunk):>5} chars... ")
        sys.stderr.flush()
        stream = client.generate(
            text=chunk,
            voice=voice_id,
            model=model,
            output_format="mp3_44100_128",
        )
        chunk_bytes = b"".join(stream)
        audio_buffer.extend(chunk_bytes)
        sys.stderr.write(f"{len(chunk_bytes):>7} bytes\n")
    return bytes(audio_buffer)


PROVIDERS = {
    "elevenlabs": {
        "key_env": "ELEVENLABS_API_KEY",
        "default_voice": DEFAULT_ELEVENLABS_VOICE,
        "default_model": DEFAULT_ELEVENLABS_MODEL,
        "valid_voice": lambda v: v in ELEVENLABS_VOICES or bool(re.fullmatch(r"[A-Za-z0-9]{20}", v)),
        "synthesize": synthesize_elevenlabs,
        "key_url": "https://elevenlabs.io/app/developers/api-keys",
    },
    "openai": {
        "key_env": "OPENAI_API_KEY",
        "default_voice": DEFAULT_OPENAI_VOICE,
        "default_model": DEFAULT_OPENAI_MODEL,
        "valid_voice": lambda v: v in OPENAI_VOICES,
        "synthesize": synthesize_openai,
        "key_url": "https://platform.openai.com/api-keys",
    },
}


def attempt_provider(provider: str, chunks: list[str], voice_override: str | None,
                     model_override: str | None) -> bytes:
    """Run TTS via one provider. Raises on any failure."""
    cfg = PROVIDERS[provider]

    api_key = load_env_key(cfg["key_env"])
    if not api_key:
        raise RuntimeError(
            f"{cfg['key_env']} not set in .env or environment "
            f"(get a key at {cfg['key_url']})"
        )

    voice = voice_override or cfg["default_voice"]
    if not cfg["valid_voice"](voice):
        if voice_override:
            sys.stderr.write(
                f"  voice '{voice_override}' not valid for {provider}, "
                f"using default '{cfg['default_voice']}'\n"
            )
        voice = cfg["default_voice"]

    model = model_override or cfg["default_model"]
    print(f"Provider: {provider}")
    print(f"Voice:    {voice}")
    print(f"Model:    {model}")
    print("Synthesizing...")
    return cfg["synthesize"](chunks, voice, model, api_key)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("date", help="Newsletter date (YYYY-MM-DD)")
    parser.add_argument(
        "--provider",
        default="auto",
        choices=["auto", "elevenlabs", "openai"],
        help=(
            "TTS provider. 'auto' (default) tries ElevenLabs then OpenAI on failure. "
            "Pin to one to disable fallback."
        ),
    )
    parser.add_argument(
        "--voice",
        default=None,
        help=(
            "Voice. ElevenLabs: sarah (default), adam, rachel, charlotte, george, brian, or raw ID. "
            "OpenAI: alloy, echo, fable, onyx, nova (default), shimmer, ash, sage, coral. "
            "Invalid voices fall back to the provider's default."
        ),
    )
    parser.add_argument(
        "--model",
        default=None,
        help="Model override. Default depends on provider.",
    )
    parser.add_argument(
        "--preview",
        action="store_true",
        help="Render only the first chunk (cheap voice/style test).",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print adapted text and chunk plan; no API call.",
    )
    parser.add_argument(
        "--out",
        type=Path,
        help="Override output path. Default: investing/Newsletter/<date>.mp3",
    )
    args = parser.parse_args()

    md_path = NEWSLETTER_DIR / f"{args.date}.md"
    if not md_path.exists():
        print(f"error: newsletter not found at {md_path}", file=sys.stderr)
        return 1

    md = md_path.read_text(encoding="utf-8")
    spoken = adapt_for_speech(md)
    chunks = chunk_for_tts(spoken, max_chars=3500)

    if args.preview:
        chunks = chunks[:1]

    print(f"Source:   {md_path}")
    print(f"Adapted:  {len(spoken):,} chars in {len(chunks)} chunk(s)")
    if args.dry_run:
        print("\n--- ADAPTED TEXT ---\n")
        print(spoken)
        print("\n--- CHUNK BOUNDARIES ---")
        for i, c in enumerate(chunks, 1):
            head = c[:80].replace("\n", " ")
            print(f"  [{i}] {len(c):>5} chars | {head}...")
        return 0

    # Build provider chain
    if args.provider == "auto":
        chain = ["elevenlabs", "openai"]
    else:
        chain = [args.provider]

    audio_bytes = None
    last_err: Exception | None = None
    for i, prov in enumerate(chain):
        try:
            audio_bytes = attempt_provider(prov, chunks, args.voice, args.model)
            if i > 0:
                print(f"  (used fallback provider: {prov})")
            break
        except Exception as e:
            last_err = e
            is_last = i == len(chain) - 1
            label = type(e).__name__
            detail = str(e)[:300]
            if is_last:
                print(f"\nerror: {prov} failed ({label}): {detail}", file=sys.stderr)
                if len(chain) > 1:
                    print("       all providers in fallback chain exhausted.", file=sys.stderr)
                return 3
            # Try next in chain
            sys.stderr.write(f"\n  ! {prov} failed ({label}): {detail}\n")
            sys.stderr.write(f"  -> falling back to {chain[i + 1]}...\n\n")

    if audio_bytes is None:
        return 3

    out_path = args.out or NEWSLETTER_DIR / f"{args.date}.mp3"
    if args.preview:
        out_path = out_path.with_name(out_path.stem + "-preview" + out_path.suffix)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_bytes(audio_bytes)
    size_kb = len(audio_bytes) / 1024
    print(f"\nWrote: {out_path}  ({size_kb:.1f} KB)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
