#!/usr/bin/env python3
"""
Extract transcripts from YouTube videos.

Default behavior: pull YouTube subtitles (auto-generated or manual) via yt-dlp.
Falls back to local Whisper transcription only if no subs are available.
Whisper fallback requires: pip install openai-whisper

Usage:
    # Default: grab subtitles, fall back to Whisper if none
    python scripts/transcribe_youtube.py "https://www.youtube.com/watch?v=VIDEO_ID"

    # Save to file
    python scripts/transcribe_youtube.py "URL" --save transcript.txt

    # Portuguese content
    python scripts/transcribe_youtube.py "URL" --language pt

    # Only subtitles, never Whisper (fast, no heavy deps)
    python scripts/transcribe_youtube.py "URL" --subs-only

    # Force Whisper even if subs exist
    python scripts/transcribe_youtube.py "URL" --whisper

    # Whisper with specific model
    python scripts/transcribe_youtube.py "URL" --whisper --model small
"""

import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path


def check_yt_dlp():
    """Verify yt-dlp is available."""
    try:
        subprocess.run(["yt-dlp", "--version"], capture_output=True, check=True)
    except FileNotFoundError:
        print("Error: yt-dlp not found. Install with: pip install yt-dlp", file=sys.stderr)
        sys.exit(1)


def get_video_metadata(url: str) -> dict:
    """Extract video metadata without downloading."""
    result = subprocess.run(
        ["yt-dlp", "--dump-json", "--no-download", url],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        print(f"Error fetching metadata: {result.stderr.strip()}", file=sys.stderr)
        sys.exit(1)
    data = json.loads(result.stdout)
    upload_date = data.get("upload_date", "")
    if upload_date and len(upload_date) == 8:
        upload_date = f"{upload_date[:4]}-{upload_date[4:6]}-{upload_date[6:]}"
    return {
        "title": data.get("title", "Unknown"),
        "channel": data.get("channel", data.get("uploader", "Unknown")),
        "date": upload_date,
        "duration": data.get("duration"),
        "subtitles": data.get("subtitles", {}),
        "automatic_captions": data.get("automatic_captions", {}),
    }


def download_subtitles(url: str, language: str | None, tmpdir: str) -> str | None:
    """Try to download existing YouTube subtitles. Returns transcript text or None."""
    out_template = os.path.join(tmpdir, "subs")
    cmd = [
        "yt-dlp",
        "--skip-download",
        "--write-sub",
        "--write-auto-sub",
        "--sub-format", "vtt",
        "--output", out_template,
        url,
    ]
    if language:
        cmd.extend(["--sub-lang", language])
    else:
        cmd.extend(["--sub-lang", "en"])

    result = subprocess.run(cmd, capture_output=True, text=True)
    # Find any .vtt file in tmpdir
    for f in Path(tmpdir).glob("*.vtt"):
        return parse_vtt(f.read_text(encoding="utf-8", errors="replace"))
    return None


def parse_vtt(vtt_text: str) -> str:
    """Convert VTT subtitle text to plain transcript."""
    lines = []
    seen = set()
    for line in vtt_text.splitlines():
        # Skip headers, timestamps, empty lines
        if not line.strip():
            continue
        if line.startswith("WEBVTT") or line.startswith("Kind:") or line.startswith("Language:"):
            continue
        if re.match(r'^\d{2}:\d{2}', line):
            continue
        if line.startswith("NOTE"):
            continue
        # Strip VTT tags
        clean = re.sub(r'<[^>]+>', '', line).strip()
        if not clean:
            continue
        # Deduplicate repeated lines (common in auto-subs)
        if clean not in seen:
            seen.add(clean)
            lines.append(clean)
    return " ".join(lines)


def download_audio(url: str, tmpdir: str) -> str:
    """Download audio from YouTube video, return path to audio file."""
    out_template = os.path.join(tmpdir, "audio.%(ext)s")
    cmd = [
        "yt-dlp",
        "--extract-audio",
        "--audio-format", "mp3",
        "--audio-quality", "5",  # moderate quality, smaller file
        "--output", out_template,
        url,
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error downloading audio: {result.stderr.strip()}", file=sys.stderr)
        sys.exit(1)
    # Find the output file
    for f in Path(tmpdir).glob("audio.*"):
        return str(f)
    print("Error: audio file not found after download", file=sys.stderr)
    sys.exit(1)


def transcribe_audio(audio_path: str, model_name: str, language: str | None) -> str:
    """Transcribe audio file using Whisper."""
    try:
        import whisper
    except ImportError:
        print(
            "Error: openai-whisper not installed (needed as fallback).\n"
            "Install with: pip install openai-whisper\n"
            "Or use --subs-only to only use YouTube subtitles.",
            file=sys.stderr,
        )
        sys.exit(1)

    print(f"Loading Whisper model '{model_name}'...", file=sys.stderr)
    model = whisper.load_model(model_name)

    print("Transcribing...", file=sys.stderr)
    options = {}
    if language:
        options["language"] = language
    result = model.transcribe(audio_path, **options)
    return result["text"]


def format_output(metadata: dict, transcript: str, method: str, url: str) -> str:
    """Format transcript with metadata header."""
    lines = [
        "# Transcript",
        f"- **Title:** {metadata['title']}",
        f"- **Channel:** {metadata['channel']}",
        f"- **Date:** {metadata['date']}",
        f"- **URL:** {url}",
        f"- **Method:** {method}",
        "---",
        "",
        transcript,
    ]
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Transcribe YouTube videos using yt-dlp + Whisper"
    )
    parser.add_argument("url", help="YouTube video URL")
    parser.add_argument(
        "--model", default="base",
        choices=["tiny", "base", "small", "medium", "large"],
        help="Whisper model size (default: base)"
    )
    parser.add_argument(
        "--language",
        help="Language hint for Whisper (e.g., 'pt' for Portuguese, 'en' for English)"
    )
    parser.add_argument(
        "--save",
        help="Save output to file instead of stdout"
    )
    parser.add_argument(
        "--subs-only", action="store_true",
        help="Only try YouTube subtitles, never fall back to Whisper"
    )
    parser.add_argument(
        "--whisper", action="store_true",
        help="Force Whisper transcription, skip subtitle check"
    )

    args = parser.parse_args()

    if args.subs_only and args.whisper:
        print("Error: --subs-only and --whisper are mutually exclusive", file=sys.stderr)
        sys.exit(1)

    check_yt_dlp()

    # Fetch metadata
    print("Fetching video metadata...", file=sys.stderr)
    metadata = get_video_metadata(args.url)
    duration = metadata.get("duration")
    if duration:
        mins = duration // 60
        print(f"Video: {metadata['title']} ({mins}m{duration % 60}s)", file=sys.stderr)
    else:
        print(f"Video: {metadata['title']}", file=sys.stderr)

    transcript = None
    method = None

    with tempfile.TemporaryDirectory() as tmpdir:
        # Default: try subtitles first (unless --whisper forces Whisper)
        if not args.whisper:
            print("Trying YouTube subtitles...", file=sys.stderr)
            transcript = download_subtitles(args.url, args.language, tmpdir)
            if transcript:
                method = "youtube-subs"
                print("Got YouTube subtitles.", file=sys.stderr)
            elif args.subs_only:
                print("Error: no subtitles found and --subs-only specified.", file=sys.stderr)
                sys.exit(1)
            else:
                print("No subtitles found, falling back to Whisper...", file=sys.stderr)

        # Whisper fallback (or forced with --whisper)
        if transcript is None:
            audio_path = download_audio(args.url, tmpdir)
            transcript = transcribe_audio(audio_path, args.model, args.language)
            method = f"whisper-{args.model}"

    output = format_output(metadata, transcript, method, args.url)

    if args.save:
        save_path = Path(args.save)
        save_path.parent.mkdir(parents=True, exist_ok=True)
        save_path.write_text(output, encoding="utf-8")
        print(f"Saved to {args.save}", file=sys.stderr)
    else:
        print(output)


if __name__ == "__main__":
    main()
