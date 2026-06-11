"""Render a report markdown file to styled HTML/PDF and optionally print it.

Usage:
    python scripts/print_report.py 2026-04-24-story-report --print
    python scripts/print_report.py investing/Reports/2026-04-24-story-report.md --print
    python scripts/print_report.py 2026-04-24-story-report --columns 2 --print

Story reports default to two-column layout (matches the newsletter print style);
other reports default to single-column. Override with --columns 1 or --columns 2.
"""

from __future__ import annotations

import argparse
import html
import re
import subprocess
import sys
import time
from pathlib import Path

import markdown


REPO = Path(__file__).resolve().parent.parent
REPORTS_DIR = REPO / "investing" / "Reports"
ATTACHMENTS_DIR = REPO / "investing" / "attachments"
CHROME = Path(r"C:/Program Files/Google/Chrome/Application/chrome.exe")
EDGE = Path(r"C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe")
DEFAULT_PRINTER = "HPFA4FA6 (HP DeskJet 2700 series)"

CSS = """
@page { size: Letter; margin: 0.55in 0.55in 0.7in 0.55in; }
html, body { margin: 0; padding: 0; }
body {
  font-family: Georgia, 'Times New Roman', serif;
  font-size: 9pt;
  line-height: 1.34;
  color: #111;
}
h1 {
  font-size: 15pt;
  margin: 0 0 0.14in 0;
  padding-bottom: 0.04in;
  border-bottom: 1.5pt solid #111;
}
h2 {
  font-size: 10.5pt;
  font-weight: 700;
  margin: 0.16in 0 0.05in 0;
  break-after: avoid;
  page-break-after: avoid;
}
h3 { font-size: 9.5pt; margin: 0.11in 0 0.04in 0; font-weight: 700; }
p  { margin: 0 0 0.075in 0; orphans: 2; widows: 2; }
table { width: 100%; border-collapse: collapse; margin: 0.06in 0 0.1in 0; }
th, td { border-bottom: 0.4pt solid #bbb; padding: 0.025in 0.035in; text-align: left; vertical-align: top; }
th { font-weight: 700; border-bottom: 0.7pt solid #666; }
ul { margin: 0.03in 0 0.08in 0.18in; padding: 0; }
li { margin: 0 0 0.03in 0; }
a  { color: #111; text-decoration: none; }
code { font-family: Consolas, monospace; font-size: 8pt; }
em { font-style: italic; }
strong { font-weight: 600; }
hr { border: none; border-top: 0.5pt solid #aaa; margin: 0.1in 0; }
.wl { color: #666; font-size: 0.92em; }
figure.chart {
  margin: 0.12in 0;
  break-inside: avoid;
  text-align: center;
}
figure.chart img { max-width: 100%; max-height: 4.8in; height: auto; }
figure.chart figcaption {
  font-size: 8pt;
  color: #555;
  margin-top: 0.04in;
  font-style: italic;
}
"""

CSS_TWO_COLUMN = """
@page { size: Letter; margin: 0.5in 0.5in 0.7in 0.5in; }
html, body { margin: 0; padding: 0; }
body {
  font-family: Georgia, 'Times New Roman', serif;
  font-size: 8.75pt;
  line-height: 1.32;
  color: #111;
  column-count: 2;
  column-gap: 0.28in;
  column-rule: 0.5pt solid #bbb;
  text-align: justify;
  hyphens: auto;
}
h1 {
  font-size: 15pt;
  margin: 0 0 0.14in 0;
  padding-bottom: 0.04in;
  border-bottom: 1.5pt solid #111;
  column-span: all;
  -webkit-column-span: all;
  text-align: left;
}
h2 {
  font-size: 9.8pt;
  font-weight: 700;
  margin: 0.12in 0 0.04in 0;
  color: #111;
  break-after: avoid;
  page-break-after: avoid;
  text-align: left;
}
h2:has(+ table) {
  column-span: all;
  -webkit-column-span: all;
}
h3 { font-size: 9pt; margin: 0.09in 0 0.03in 0; font-weight: 700; }
p  { margin: 0 0 0.07in 0; orphans: 2; widows: 2; }
table {
  width: 100%;
  border-collapse: collapse;
  margin: 0.06in 0 0.12in 0;
  column-span: all;
  -webkit-column-span: all;
  break-inside: avoid;
  text-align: left;
}
th, td { border-bottom: 0.4pt solid #bbb; padding: 0.025in 0.035in; text-align: left; vertical-align: top; }
th { font-weight: 700; border-bottom: 0.7pt solid #666; }
ul { margin: 0.03in 0 0.08in 0.18in; padding: 0; }
li { margin: 0 0 0.03in 0; }
a  { color: #111; text-decoration: none; }
code { font-family: Consolas, monospace; font-size: 8pt; }
em { font-style: italic; }
strong { font-weight: 600; }
hr { border: none; border-top: 0.5pt solid #aaa; margin: 0.1in 0; }
.wl { color: #666; font-size: 0.92em; }
figure.chart {
  margin: 0.12in 0;
  column-span: all;
  -webkit-column-span: all;
  break-inside: avoid;
  text-align: center;
}
figure.chart img { max-width: 100%; max-height: 4.8in; height: auto; }
figure.chart figcaption {
  font-size: 8pt;
  color: #555;
  margin-top: 0.04in;
  font-style: italic;
}
"""

WIKILINK = re.compile(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]")
IMAGE_EMBED = re.compile(
    r"!\[\[([^\]|]+?\.(?:png|jpg|jpeg|gif|svg|webp))(?:\|([^\]]+))?\]\]",
    re.IGNORECASE,
)


def style_wikilinks(text: str) -> str:
    """Render wikilinks as visible brackets with subtle print styling."""

    def repl(match: re.Match[str]) -> str:
        return f'<span class="wl">{match.group(0)}</span>'

    return WIKILINK.sub(repl, text)


def resolve_image_embeds(text: str) -> str:
    """Convert Obsidian image embeds (`![[chart.png]]` / `![[chart.png|caption]]`)
    into <figure>+<img> blocks pointing at investing/attachments. Embeds whose
    target file is not found are left unchanged so the broken reference is
    visible rather than silently dropped.
    """

    def repl(match: re.Match[str]) -> str:
        name = match.group(1).strip()
        caption = (match.group(2) or "").strip()
        path = ATTACHMENTS_DIR / name
        if not path.exists():
            hits = list(ATTACHMENTS_DIR.rglob(name))
            if hits:
                path = hits[0]
            else:
                return match.group(0)
        url = "file:///" + str(path).replace("\\", "/")
        alt = html.escape(caption or path.stem)
        figcap = (
            f"<figcaption>{html.escape(caption)}</figcaption>" if caption else ""
        )
        return f'<figure class="chart"><img src="{url}" alt="{alt}"/>{figcap}</figure>'

    return IMAGE_EMBED.sub(repl, text)


def resolve_report(value: str) -> Path:
    path = Path(value)
    if path.suffix.lower() != ".md":
        path = path.with_suffix(".md")
    if not path.is_absolute():
        if len(path.parts) == 1:
            path = REPORTS_DIR / path
        else:
            path = REPO / path
    return path


def render_html(md_path: Path, columns: int = 1) -> str:
    raw = md_path.read_text(encoding="utf-8")
    body_md = re.sub(r"^---\n.*?\n---\n", "", raw, count=1, flags=re.DOTALL)
    body_md = resolve_image_embeds(body_md)
    body_md = style_wikilinks(body_md)
    body_html = markdown.markdown(body_md, extensions=["extra", "sane_lists"])
    title = html.escape(md_path.stem)
    css = CSS_TWO_COLUMN if columns == 2 else CSS
    return f"""<!doctype html>
<html><head><meta charset=\"utf-8\"><title>{title}</title>
<style>{css}</style>
</head><body>
{body_html}
<script>window.addEventListener('load', function () {{ setTimeout(function () {{ window.print(); }}, 500); }});</script>
</body></html>"""


def resolve_columns(value: str, md_path: Path) -> int:
    """auto -> 2 for *-story-report*.md filenames, 1 otherwise. Explicit 1/2 wins."""
    if value == "auto":
        return 2 if "story-report" in md_path.stem else 1
    return int(value)


def html_to_pdf(html_path: Path, pdf_path: Path) -> None:
    if not CHROME.exists():
        sys.exit(f"Chrome not found at {CHROME}")
    url = "file:///" + str(html_path).replace("\\", "/")
    cmd = [
        str(CHROME),
        "--headless",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={pdf_path}",
        url,
    ]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def stamp_page_numbers(pdf_path: Path) -> None:
    """Stamp 'n / N' folios onto an existing PDF, bottom-center.

    Chromium ignores @page margin-box content and Paged.js breaks the
    two-column layout, so numbering is done post-render: a numbers-only
    overlay PDF is generated with Chrome and merged page-by-page via pypdf.
    """
    from pypdf import PdfReader, PdfWriter

    reader = PdfReader(str(pdf_path))
    total = len(reader.pages)
    pages_html = "".join(
        f'<div class="pg"><span class="num">{i} / {total}</span></div>'
        for i in range(1, total + 1)
    )
    overlay_html = f"""<!doctype html><html><head><meta charset="utf-8"><style>
@page {{ size: Letter; margin: 0; }}
html, body {{ margin: 0; padding: 0; }}
.pg {{ position: relative; width: 8.5in; height: 10.98in; page-break-after: always; }}
.num {{ position: absolute; bottom: 0.3in; left: 0; right: 0; text-align: center;
       font-family: Georgia, 'Times New Roman', serif; font-size: 7.5pt; color: #666; }}
</style></head><body>{pages_html}</body></html>"""

    tmp_html = pdf_path.with_suffix(".folio.html")
    tmp_pdf = pdf_path.with_suffix(".folio.pdf")
    tmp_html.write_text(overlay_html, encoding="utf-8")
    try:
        html_to_pdf(tmp_html, tmp_pdf)
        overlay = PdfReader(str(tmp_pdf))
        writer = PdfWriter()
        for page, folio in zip(reader.pages, overlay.pages):
            page.merge_page(folio)
            writer.add_page(page)
        with open(pdf_path, "wb") as fh:
            writer.write(fh)
    finally:
        tmp_html.unlink(missing_ok=True)
        tmp_pdf.unlink(missing_ok=True)


def print_via_edge(html_path: Path, printer: str) -> None:
    subprocess.run(
        [
            "powershell.exe",
            "-NoProfile",
            "-Command",
            f"(New-Object -ComObject WScript.Network).SetDefaultPrinter('{printer}')",
        ],
        check=True,
    )

    if not EDGE.exists():
        sys.exit(f"Edge not found at {EDGE}")

    url = "file:///" + str(html_path).replace("\\", "/")
    user_data = REPO / ".edge-print-profile"
    user_data.mkdir(exist_ok=True)

    _proc = subprocess.Popen(
        [
            str(EDGE),
            "--kiosk-printing",
            "--no-first-run",
            "--no-default-browser-check",
            f"--user-data-dir={user_data}",
            "--new-window",
            url,
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )

    print("waiting for print spooler to receive and render the job...")
    deadline = time.time() + 45
    saw_job = False
    printed = False
    while time.time() < deadline:
        time.sleep(2)
        check = subprocess.run(
            [
                "powershell.exe",
                "-NoProfile",
                "-Command",
                f"Get-PrintJob -PrinterName '{printer}' 2>$null | Measure-Object | Select-Object -ExpandProperty Count",
            ],
            capture_output=True,
            text=True,
        )
        count = (check.stdout or "0").strip()
        if count.isdigit() and int(count) > 0:
            saw_job = True
        elif saw_job:
            printed = True
            break

    subprocess.run(
        [
            "powershell.exe",
            "-NoProfile",
            "-Command",
            "Stop-Process -Name msedge -Force -ErrorAction SilentlyContinue",
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )

    if not saw_job:
        sys.exit("ERROR: no print job ever reached the spooler - Edge did not submit")
    if not printed:
        print("WARN: job still pending at timeout; check printer queue")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("report", help="Report stem, relative path, or absolute .md path")
    parser.add_argument("--printer", default=DEFAULT_PRINTER)
    parser.add_argument("--print", action="store_true", help="Also send to printer")
    parser.add_argument(
        "--columns",
        default="auto",
        choices=["auto", "1", "2"],
        help="Layout: 1 (single-column), 2 (two-column like newsletter), or auto (story-report → 2, else 1)",
    )
    args = parser.parse_args()

    md_path = resolve_report(args.report)
    if not md_path.exists():
        sys.exit(f"not found: {md_path}")

    columns = resolve_columns(args.columns, md_path)

    html_path = md_path.with_name(f".{md_path.stem}.html")
    pdf_path = md_path.with_suffix(".pdf")

    html_path.write_text(render_html(md_path, columns=columns), encoding="utf-8")
    html_to_pdf(html_path, pdf_path)
    stamp_page_numbers(pdf_path)
    print(f"PDF: {pdf_path} ({columns}-column, page numbers stamped)")

    if args.print:
        print_via_edge(html_path, args.printer)
        print(f"sent to printer: {args.printer}")


if __name__ == "__main__":
    main()
