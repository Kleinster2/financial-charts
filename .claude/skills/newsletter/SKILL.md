---
name: newsletter
description: "Generate a personal daily market newsletter after the close. Reads today's daily note and all notes created/expanded during the session, then writes a narrative brief in clean markdown. The voice is analytical and structural — identifies tensions, connects threads, surfaces what the market is pricing vs what the data says. Not a recap. Use when the user says /newsletter, 'write the newsletter', 'daily brief', or 'wrap up the day'."
---

# Daily Newsletter

Personal end-of-day market brief. The newsletter is a **saved vault artifact** at `investing/Newsletter/YYYY-MM-DD.md`, not just chat output. It's also displayed in chat for review, automatically rendered to MP3 via ElevenLabs TTS, and can be printed to paper via the dedicated two-column script. Treat it as a vault operation — check existing infrastructure in `scripts/` before reaching for generic tooling.

## Workflow

### Step 1: Final ingestion (if needed)

If the user hasn't run `/news` recently or asks for a final sweep:
1. Run `python scripts/quick_movers.py` to check for late-day sigma movers
2. If significant movers have no vault coverage, flag them — but don't run a full `/news` cycle unless asked

### Step 2: Gather the day's work

1. Read today's daily note (`investing/Daily/YYYY-MM-DD.md`) — run `date` to confirm date
2. If `investing/Reports/YYYY-MM-DD-story-report.md` exists, read it first. Treat it as the exhaustive story map for the day.
3. Extract every note listed under "Notes created/expanded"
4. Read each referenced note to understand the substance (not just the log entry)
5. Read the daily note's Synthesis section if one exists

### Step 3: Identify the stories

Group the day's work into 2-5 stories. A "story" is not a note — it's a narrative thread that may span multiple notes. If the daily story report exists, select the most important threads from it rather than repeating every card. Examples:
- Intel-Apollo Fab 34 buyback (touches Intel, Apollo, Athene, Intel bonds)
- Iran oil timeline escalation (touches oil price timeline, analyst notes, sector notes)
- Semiconductor earnings season (touches multiple actor notes)

For each story, identify:
- What happened (facts, figures, dates)
- Why it matters (structural, not just price action)
- The tension or open question (what's unresolved, what the market may be mispricing)
- Connections to other vault themes

**Newsletter sections weave in pre-existing vault context — not just today's edits.** Read the touched note(s) in full before writing the section, not only the new content. The "what happened" line is today-specific; the "why it matters" and "the tension" lines should reflect the whole arc the note documents, including earlier events, prior framings, and structural context that anchor today's developments. A section that only narrates the day's additions misses the threads the vault has already built up.

### Step 4: Write the newsletter

**Format:**

```
# [Date] — [One-line theme for the day]

## [Story 1 headline — active voice, names the tension]

[2-4 paragraphs. Lead with the news, move to the structural read, end with the open question. Exact figures. Named sources. Wikilinks to vault entities.]

## [Story 2 headline]

[Same structure]

...

## Threads to watch

[3-5 bullet points of unresolved questions or developing situations from today's work that deserve follow-up. These are forward-looking — what to check tomorrow.]
```

### Voice rules

- **Analytical, not editorial.** Present dynamics, not bull/bear calls. "The bet is X — if Y doesn't materialize, they just levered up" is good. "This is bullish" is not.
- **Tensions, not market reads.** When two facts in a story pull in opposite directions, present both and name the tension. Never claim to know what "the market is missing" or "isn't pricing" — that requires positioning data, credit spreads, flow, and options markets we don't have. The newsletter surfaces contradictions; the reader decides whether they're priced.
- **Structural, not reactive.** Connect today's news to the vault's accumulated knowledge. The newsletter's value is context the reader already has from the vault — surface it.
- **Exact figures.** Dollar amounts, percentages, dates, named analysts with firms. No "significant" or "substantial."
- **Sharp, not sterile.** Personal research voice — the reader is a macro-focused investor who already knows the basics. Don't explain what Apollo does. Do explain why their return on Fab 34 matters for how we think about Intel's cost of capital.
- **No bold in body text.** Headers only.
- **No emojis.**

### Charts (optional)

The print pipeline resolves Obsidian image embeds (`![[chart.png]]` / `![[chart.png|caption]]`) to figures that span both columns. Use them sparingly:

- **At most 1-2 charts per newsletter, total.** Pick the single chart that anchors the day's most important story. A 400-800 word brief turns into a chart catalog if every story gets a chart.
- **Only embed charts that already live in a touched note.** Do not generate a fresh chart for the newsletter — the chart must be one you saw while reading the day's notes. This keeps charts anchored to vault state and avoids duplicate plumbing.
- **Place the embed inside the relevant story section** (after the lead paragraph, before the structural read), not in a trailing "Charts" appendix.
- **The optional caption** (after the `|`) renders as italic figcaption under the image. Use it to name the chart's point in one clause, not to repeat the surrounding paragraph.

### What NOT to include

- Routine stub creation (unless the stub itself is interesting — e.g., a new actor entering the vault)
- Compliance fixes, formatting changes, editorial cleanup
- Notes that were only lightly touched (typo fix, added one link)
- Repetition of the daily note's edit log — the newsletter replaces it, not duplicates it

### Length

Target 400-800 words total. Shorter is better if the day was quiet. Longer is fine if multiple major stories landed. Never pad.

### Step 5: Save, render audio, and print

1. **Save to vault.** Write the newsletter markdown to `investing/Newsletter/YYYY-MM-DD.md` with frontmatter:

   ```
   ---
   date: YYYY-MM-DD
   type: newsletter
   tags: [newsletter]
   ---
   ```

2. **Display in chat** for review — same content as the saved file.

3. **Render to audio (default).** After saving, automatically generate the MP3 audio version:

   ```
   python scripts/audio_render.py YYYY-MM-DD
   ```

   What it does: reads the saved markdown, adapts it for spoken delivery (strips wikilink brackets; expands percent ranges, dollar magnitudes, quarter and fiscal-year abbreviations, bps, MoU, σ; smooths em-dashes into comma-pauses), then renders to `investing/Newsletter/YYYY-MM-DD.mp3` via the auto-fallback chain: **ElevenLabs primary** (voice `sarah`, model `eleven_multilingual_v2`) → **OpenAI fallback** (voice `nova`, model `gpt-4o-mini-tts`) on any provider failure (auth, quota, network, server). Both keys live in `.env`. Newsletter is ~5-7 min listen at 8K chars / 3 chunks.

   Open the MP3 in the user's default player after generation:

   ```
   start "" "investing/Newsletter/YYYY-MM-DD.mp3"
   ```

   **Quota note:** ElevenLabs free tier is 10K chars/month — one full newsletter consumes the monthly budget, after which the chain auto-falls-through to OpenAI without intervention. OpenAI TTS is ~$0.10/newsletter on `gpt-4o-mini-tts`, billed against the existing API account. Use `--preview` to render only the first chunk (sample test). Use `--dry-run` to inspect the adapted text without an API call. Pin to one provider with `--provider {elevenlabs,openai}` to disable fallback. Override voice with `--voice` (ElevenLabs: sarah, adam, rachel, charlotte, george, brian; OpenAI: alloy, echo, fable, onyx, nova, shimmer, ash, sage, coral).

   If both providers fail, don't block the workflow — note the failure in chat and continue with print/save.

4. **Print to paper** when the user says "print", "send to print", "print it", etc. Use the dedicated script, never raw `Out-Printer` or `notepad /p`:

   ```
   python scripts/print_newsletter.py YYYY-MM-DD --print
   ```

   What it does: renders the markdown to HTML with `column-count: 2` CSS (Georgia serif, 8.75pt, justified, column rule), generates `investing/Newsletter/YYYY-MM-DD.pdf` via Chrome headless, then prints via Edge kiosk-printing to the default printer (`HPFA4FA6 (HP DeskJet 2700 series)`). Override the printer with `--printer NAME`. Frontmatter is stripped; **wikilinks are preserved and rendered in a subtle gray** so the reader can see what's linked on paper.

   **Do not** improvise with `Out-Printer`, `notepad /p`, or a hand-rolled HTML. The two-column layout and visible wikilinks are the point.

   Note: the edit-logger will record the Newsletter file as `[[YYYY-MM-DD]] (Newsletter)`, which collides with the daily note's own name and can trip the daily-summary hook. Add a one-line summary block to the daily note under `## Notes created/expanded` (e.g., `### Newsletter — EOD brief`) mentioning `[[YYYY-MM-DD]]` before ending the session.
