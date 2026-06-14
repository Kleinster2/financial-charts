#!/usr/bin/env python3
"""
Note compliance checker for the investing vault.

Checks actor and analyst/source-person notes against the standards defined in:
- investing/Meta/Note structures.md
- investing/Meta/Financials templates.md
- CLAUDE.md

Usage:
    python scripts/check_note_compliance.py investing/Actors/Snap.md
    python scripts/check_note_compliance.py investing/Actors/*.md  # Check all
    python scripts/check_note_compliance.py investing/Analysts/*.md
    python scripts/check_note_compliance.py --changed  # Check git-changed files
    python scripts/check_note_compliance.py --orphans  # Find frequently mentioned terms without notes
"""

import argparse
import json
from collections import Counter
from datetime import date
import re
import signal
import subprocess
import sys
from pathlib import Path
from typing import NamedTuple

# Make the note_checker/ package importable whether this file is run as a script
# (scripts/ on sys.path) or imported as scripts.check_note_compliance (repo root
# on sys.path). The split-out mixins live in scripts/note_checker/.
sys.path.insert(0, str(Path(__file__).resolve().parent))
from note_checker.indexing import IndexMixin
from note_checker.fixes import FixMixin
from note_checker.analytics import AnalyticsMixin


class Issue(NamedTuple):
    severity: str  # "error" or "warning"
    rule: str
    message: str


# Single-word note names that collide with common English words. The
# missing-link / table-cell checks would otherwise flag every prose use of
# "gold standard", "linear axis", "cash flow", "promise to deliver", etc. as a
# missing wikilink to the same-named note. Whole-word, case-sensitive matches
# against these note names are suppressed. Extend as new collisions surface.
COMMON_WORD_NOTE_NAMES = frozenset({
    "Gold", "Flow", "Linear", "Promise", "Texas", "Acquired", "Pure", "Post",
    "Open", "Closed", "Premium", "Target", "Index", "Average", "Watch", "Grid",
    "Street", "Vision", "Driver", "Brand", "Career", "Talent", "Labs", "Battery",
    "Solar", "Chip", "Finance", "Property", "Auto", "Seed", "Round", "Theme",
    "Entity", "Medium", "Wire", "Reflexivity", "Action", "Move", "Event",
    "Memory", "Infrastructure", "Specialized", "Storage", "Paradox",
})

# Concept names that are inherently plural-only (mass nouns) — the singular form
# is wrong or means something different ("owner earning" is not a thing). The
# singular-name check skips these instead of suggesting a nonsensical rename.
INHERENTLY_PLURAL_CONCEPTS = frozenset({
    "Owner earnings", "Earnings", "Retained earnings", "Proceeds", "Savings",
    "Winnings", "Earnings", "Owner's earnings",
})


class NoteChecker(IndexMixin, FixMixin, AnalyticsMixin):

    def __init__(self, vault_root: Path, suggest_links: bool = False, use_index_cache: bool = True):
        self.vault_root = vault_root
        self.suggest_links = suggest_links
        self._use_index_cache = use_index_cache
        self._new_index_cache: dict = {}
        self.existing_notes = self._index_existing_notes()
        cache = self._load_index_cache()
        self.known_aliases = self._index_aliases(cache)
        self.cross_vault_index = self._index_cross_vaults(cache)
        self._save_index_cache(self._new_index_cache)

    @staticmethod
    def _has_tag(content: str, tag: str) -> bool:
        """Check if content contains a tag as a hashtag token or in YAML frontmatter.

        Checks two places:
        1. Body hashtags: #tag as whole token (not substring)
        2. YAML frontmatter tags: both inline [a, b, c] and block (- item) formats

        The tag parameter includes the # prefix (e.g. "#etf"), which is stripped
        for frontmatter matching.
        """
        # Strip # prefix for frontmatter matching
        bare = tag.lstrip("#")

        # Check body hashtags
        if re.search(rf'(?<!\w){re.escape(tag)}(?=\s|$)', content, re.MULTILINE):
            return True

        # Check YAML frontmatter
        if content.startswith("---"):
            end = content.find("---", 3)
            if end != -1:
                fm = content[3:end]
                # Inline: tags: [actor, etf, risk-parity]
                inline = re.search(r'^tags:\s*\[([^\]]*)\]', fm, re.MULTILINE)
                if inline:
                    items = [t.strip().strip('"').strip("'") for t in inline.group(1).split(",")]
                    if bare in items:
                        return True
                # Block: tags:\n  - actor\n  - etf
                block = re.search(r'^tags:\s*\n((?:\s+-\s+.+\n?)+)', fm, re.MULTILINE)
                if block:
                    items = re.findall(r'^\s+-\s+(.+?)$', block.group(1), re.MULTILINE)
                    items = [t.strip().strip('"').strip("'") for t in items]
                    if bare in items:
                        return True

        return False

    # Cross-vault files to ignore (config files, not real counterparts)
    CROSS_VAULT_IGNORE = {"claude", "home", "edit-log", "vault-architecture", "changelog"}

    def _check_cross_vault_links(self, content: str, filepath: Path) -> list[Issue]:
        """Check if this note has a counterpart in another vault without a cross-vault link.

        Filtering rules to avoid false positives:
        - Config files (CLAUDE.md etc.) are skipped via CROSS_VAULT_IGNORE.
        - Alias-only matches (where the investing note's stem didn't match the
          cross-vault key) require that the investing note stem matches the
          cross-vault note stem. This prevents alias collisions like
          StoneCo→"Stone" matching technologies/Stone (raw material), or
          Gap→"GPS" matching technologies/GPS.
        """
        issues = []
        note_name = filepath.stem.lower()

        # Also check aliases of this note
        aliases = set()
        if content.startswith("---"):
            end = content.find("---", 3)
            if end != -1:
                fm = content[3:end]
                inline = re.search(r'^aliases:\s*\[([^\]]*)\]', fm, re.MULTILINE)
                if inline:
                    for alias in inline.group(1).split(","):
                        alias = alias.strip().strip('"').strip("'")
                        if alias:
                            aliases.add(alias.lower())
                block = re.search(r'^aliases:\s*\n((?:\s+-\s+.+\n?)+)', fm, re.MULTILINE)
                if block:
                    for alias in re.findall(r'^\s+-\s+(.+?)$', block.group(1), re.MULTILINE):
                        alias = alias.strip().strip('"').strip("'")
                        if alias:
                            aliases.add(alias.lower())

        names_to_check = {note_name} | aliases

        # Find matches in cross-vaults, tracking whether match was via stem
        matches = {}  # vault_name -> (note_stem, rel_path, matched_via_stem)
        for name in names_to_check:
            if name in self.CROSS_VAULT_IGNORE:
                continue
            if name in self.cross_vault_index:
                for vault_name, stem, rel_path in self.cross_vault_index[name]:
                    if stem.lower() in self.CROSS_VAULT_IGNORE:
                        continue
                    is_stem_match = (name == note_name)
                    if vault_name not in matches:
                        matches[vault_name] = (stem, rel_path, is_stem_match)
                    elif is_stem_match and not matches[vault_name][2]:
                        # Upgrade alias match to stem match
                        matches[vault_name] = (stem, rel_path, True)

        if not matches:
            return issues

        # Check if content already has cross-vault links for each matched vault
        for vault_name, (stem, rel_path, via_stem) in matches.items():
            # For alias-only matches, require stems to refer to the same entity
            if not via_stem and note_name != stem.lower():
                continue

            uri_pattern = f"obsidian://open?vault={re.escape(vault_name)}"
            if uri_pattern not in content:
                encoded_path = rel_path.replace(" ", "%20").replace("/", "%2F")
                uri = f"obsidian://open?vault={vault_name}&file={encoded_path}"
                issues.append(Issue(
                    "warning", "cross-vault",
                    f"Counterpart exists in {vault_name} vault: \"{stem}\" — "
                    f"consider adding: [{vault_name.title()}: {stem}]({uri})"
                ))

        return issues

    def check_note(self, filepath: Path) -> list[Issue]:
        """Check a single note for compliance issues."""
        issues = []

        content = filepath.read_text(encoding="utf-8")
        lines = content.split("\n")

        # Determine note type from folder and hashtags
        note_type = "analyst" if self._is_under_folder(filepath, "Analysts") else self._get_note_type(content)

        # Universal checks (all note types)
        issues.extend(self._check_bold_formatting(content, filepath))
        issues.extend(self._check_dead_links(content, filepath))
        issues.extend(self._check_cross_vault_links(content, filepath))
        issues.extend(self._check_cluster_validation_diagnostics(content, filepath))
        if note_type in ("actor", "analyst", "etf", "benchmark", "concept", "event", "thesis"):
            issues.extend(self._check_missing_links(content, filepath))

        # Concept-specific checks
        if note_type == "concept":
            issues.extend(self._check_singular_name(content, filepath))

        # Sector and index checks
        if note_type in ("sector", "index"):
            issues.extend(self._check_correlation_structure(content, filepath))

        # Synthesis check (concept and event notes, not stubs)
        if note_type in ("concept", "event"):
            issues.extend(self._check_synthesis(content, filepath))

        # Public-company M&A event notes must capture the tape, not only the strategy.
        if note_type == "event":
            issues.extend(self._check_ma_market_reaction(content, filepath))
            issues.extend(self._check_market_reaction_placeholders(content, filepath))
            issues.extend(self._check_market_reaction_peer_coverage(content, filepath))

        # Hub checks (concept and sector notes)
        if note_type in ("concept", "sector"):
            issues.extend(self._check_hub_chart(content, filepath, note_type))
            issues.extend(self._check_chart_captions(content, filepath))
            issues.extend(self._check_oneliner_links(content, filepath))
            issues.extend(self._check_table_cell_links(content, filepath))
            issues.extend(self._check_bidirectional_related(content, filepath))

        if note_type == "analyst":
            issues.extend(self._check_frontmatter(content, filepath, missing_alias_severity="error"))
            issues.extend(self._check_analyst_structure(content, filepath))
            issues.extend(self._check_related_section(content, filepath))
            issues.extend(self._check_quick_stats(content, filepath, missing_severity="error"))
            issues.extend(self._check_table_formatting(content, filepath))
            issues.extend(self._check_unsourced_work_claim(content, filepath))
            return issues

        # Remaining checks are actor-specific
        if note_type not in ("actor", "etf", "benchmark"):
            return issues

        is_public = self._is_public_company(content)
        is_etf = note_type in ("etf", "benchmark") or self._has_tag(content, "#etf") or self._has_tag(content, "#benchmark")
        is_private = self._has_tag(content, "#private")
        is_person = self._has_tag(content, "#person")
        is_geography = self._has_tag(content, "#geography") or any(self._has_tag(content, tag) for tag in ["#country", "#region", "#city"])
        is_vc = self._has_tag(content, "#vc")
        is_investor = self._has_tag(content, "#investor") or self._has_tag(content, "#hedgefund") or self._has_tag(content, "#pe")
        is_public_exempt = self._is_public_company_exempt(content)
        is_product = self._has_tag(content, "#product")  # Products belong to parent companies

        # Structure checks
        issues.extend(self._check_frontmatter(content, filepath))
        issues.extend(self._check_related_section(content, filepath))
        issues.extend(self._check_quick_stats(content, filepath))
        issues.extend(self._check_table_formatting(content, filepath))

        # Private-capital notes need the founder/principal story, not just names in Quick stats.
        if (is_vc or is_investor) and not is_person and not is_geography and not is_product:
            issues.extend(self._check_private_capital_founder_edge(content, filepath))

        # Chart checks (public companies and ETFs, not products)
        if ((is_public and not is_public_exempt) or is_etf) and not is_product:
            issues.extend(self._check_price_chart(content, filepath, is_etf))
            issues.extend(self._check_chart_captions(content, filepath))

        # Product chart checks (usage metrics like MAU, DAU, GMV)
        if is_product:
            issues.extend(self._check_product_chart(content, filepath))
            issues.extend(self._check_chart_captions(content, filepath))

        # Sector correlation (public companies and ETFs, not people/geographies/products)
        if ((is_public and not is_public_exempt) or is_etf) and not is_person and not is_geography and not is_product:
            issues.extend(self._check_sector_correlation(content, filepath))

        # Fundamentals chart (public companies only, not ETFs/products)
        if is_public and not is_public_exempt and not is_etf and not is_person and not is_geography and not is_vc and not is_product:
            issues.extend(self._check_fundamentals_chart(content, filepath))

        # Sankey chart (public companies only, not ETFs/products)
        if is_public and not is_public_exempt and not is_etf and not is_person and not is_geography and not is_vc and not is_product:
            issues.extend(self._check_sankey_chart(content, filepath))

        # Actor/Securities split (public companies in Actors/, not people/geographies/products)
        if is_public and not is_public_exempt and not is_etf and not is_person and not is_geography and not is_vc and not is_product:
            issues.extend(self._check_securities_split(content, filepath))

        # Financials checks (not products - those go on parent company)
        if is_public and not is_public_exempt and not is_etf and not is_person and not is_geography and not is_vc and not is_product:
            issues.extend(self._check_historical_financials(content, filepath))

        # Cap table checks (private companies, not investment firms or products)
        if is_private and not is_person and not is_geography and not is_vc and not is_investor and not is_product:
            issues.extend(self._check_cap_table(content, filepath))
            issues.extend(self._check_funding_rounds(content, filepath))
            issues.extend(self._check_ownership_table(content, filepath))
            issues.extend(self._check_private_financials(content, filepath))

        # Leadership check (companies, not ETFs/people/geographies/products)
        if (is_public or is_private) and not is_etf and not is_person and not is_geography and not is_product:
            issues.extend(self._check_leadership(content, filepath))

        # Evolution check (companies/countries/institutions, not people/products/ETFs, not stubs)
        if not is_etf and not is_person and not is_product:
            issues.extend(self._check_evolution(content, filepath))

        # Synopsis check (actor notes, not stubs)
        if note_type in ("actor", "etf", "benchmark"):
            issues.extend(self._check_synopsis(content, filepath))

        # Unsourced superlative work-claim check (people — catches vague/fabricated book claims)
        if is_person:
            issues.extend(self._check_unsourced_work_claim(content, filepath))

        # Analyst timeline check (public companies, not ETFs/people/geographies/products)
        if is_public and not is_public_exempt and not is_etf and not is_person and not is_geography and not is_product:
            issues.extend(self._check_analyst_timeline(content, filepath))

        # Credit rating check (public companies, not ETFs/people/geographies/products)
        if is_public and not is_public_exempt and not is_etf and not is_person and not is_geography and not is_product:
            issues.extend(self._check_credit_rating(content, filepath))

        return issues

    def _get_note_type(self, content: str) -> str:
        """Determine note type from hashtags."""
        if self._has_tag(content, "#actor"):
            if self._has_tag(content, "#etf") or self._has_tag(content, "#benchmark"):
                return "etf"
            return "actor"
        if self._has_tag(content, "#index"):
            return "index"
        if self._has_tag(content, "#sector"):
            return "sector"
        if self._has_tag(content, "#concept"):
            return "concept"
        if self._has_tag(content, "#event"):
            return "event"
        if self._has_tag(content, "#thesis"):
            return "thesis"
        return "unknown"

    @staticmethod
    def _is_under_folder(filepath: Path, folder_name: str) -> bool:
        """Return True when a note path is inside a vault folder."""
        return folder_name in filepath.parts

    @staticmethod
    def _extract_ticker(content: str) -> str | None:
        """Extract primary ticker symbol from frontmatter or a Quick stats table."""
        m = re.search(r"(?im)^ticker:\s*([A-Z0-9][A-Z0-9.\-]{0,12})", content)
        if m:
            return m.group(1)
        m = re.search(r"\|\s*Ticker(?:\s*\([^)]*\))?\s*\|\s*([A-Z0-9][A-Z0-9.\-]{0,12})", content)
        return m.group(1) if m else None

    @staticmethod
    def _extract_aliases(content: str) -> list[str]:
        """Extract aliases from YAML frontmatter without requiring PyYAML."""
        if not content.startswith("---"):
            return []

        second_dash = content.find("---", 3)
        if second_dash == -1:
            return []

        frontmatter = content[3:second_dash]
        aliases: list[str] = []

        inline = re.search(r'^aliases:\s*\[([^\]]*)\]', frontmatter, re.MULTILINE)
        if inline:
            aliases.extend(
                alias.strip().strip('"').strip("'")
                for alias in inline.group(1).split(",")
                if alias.strip()
            )

        block = re.search(r'^aliases:\s*\n((?:\s+-\s+.+\n?)+)', frontmatter, re.MULTILINE)
        if block:
            aliases.extend(
                alias.strip().strip('"').strip("'")
                for alias in re.findall(r'^\s+-\s+(.+?)$', block.group(1), re.MULTILINE)
                if alias.strip()
            )

        return aliases

    @classmethod
    def _extract_alias_ticker(cls, content: str) -> str | None:
        """Extract a ticker-like frontmatter alias when no explicit ticker exists."""
        for alias in cls._extract_aliases(content):
            if re.fullmatch(r"[A-Z][A-Z0-9]{1,5}(?:[.-][A-Z0-9]{1,4})?", alias):
                return alias
        return None

    def _extract_public_actor_ticker(self, content: str) -> str | None:
        """Return a ticker for public/listed actor notes, including alias-only stubs."""
        if self._is_public_company_exempt(content):
            return None

        ticker = self._extract_ticker(content)
        if ticker:
            return ticker

        alias_ticker = self._extract_alias_ticker(content)
        if not alias_ticker:
            return None

        if self._is_public_company(content):
            return alias_ticker

        public_listing_language = re.search(
            r'\b(NASDAQ|NYSE|listed|publicly traded|IPO)\b',
            content,
            re.IGNORECASE,
        )
        return alias_ticker if public_listing_language else None

    def _is_public_company_exempt(self, content: str) -> bool:
        """Check for actor tags that should never trigger public-company gates."""
        exempt_tags = [
            "#government", "#regulator", "#agency", "#ministry", "#law-firm",
            "#professional-services", "#private", "#private_company", "#brand",
            "#spac", "#de-spac", "#person", "#country", "#region", "#city",
            "#geography", "#vc", "#investor", "#hedgefund", "#pe", "#nonprofit",
            "#university", "#think-tank", "#academic", "#politician", "#macro",
            "#central-bank",
        ]
        return any(self._has_tag(content, tag) for tag in exempt_tags)

    def _is_public_company(self, content: str) -> bool:
        """Check if note is for a public company.

        Public-company compliance gates are expensive and should only fire for
        notes that explicitly identify a traded company/security. Do not infer
        public status from a bare ``#actor`` tag: government agencies, law firms,
        SPAC shells, and private companies are all actor notes too.
        """
        if self._is_public_company_exempt(content):
            return False
        if self._has_tag(content, "#public_company") or self._has_tag(content, "#public"):
            return True
        # Has ticker in quick stats / frontmatter. Require a real ticker-like
        # token, including foreign suffixes (e.g. 300274.SZ, ITM.L, NEL.OL).
        if self._extract_ticker(content):
            return True
        return False

    def _check_frontmatter(
        self,
        content: str,
        filepath: Path,
        missing_alias_severity: str = "warning",
    ) -> list[Issue]:
        """Check for proper frontmatter."""
        issues = []

        if not content.startswith("---"):
            issues.append(Issue("error", "frontmatter", "Missing frontmatter (should start with ---)"))
            return issues

        # Find end of frontmatter
        second_dash = content.find("---", 3)
        if second_dash == -1:
            issues.append(Issue("error", "frontmatter", "Malformed frontmatter (no closing ---)"))
            return issues

        frontmatter = content[3:second_dash]

        if "aliases:" not in frontmatter:
            issues.append(Issue(missing_alias_severity, "frontmatter", "Missing aliases in frontmatter"))
        elif "[[" in frontmatter:
            # Wikilinks in aliases cause Obsidian type mismatch errors
            issues.append(Issue("error", "frontmatter", "Aliases contain [[wikilinks]] — use plain text only"))

        return issues

    def _check_related_section(self, content: str, filepath: Path) -> list[Issue]:
        """Check for Related section."""
        issues = []

        if "## Related" not in content:
            issues.append(Issue("error", "structure", "Missing '## Related' section"))

        return issues

    def _check_singular_name(self, content: str, filepath: Path) -> list[Issue]:
        """Check that concept notes use singular names."""
        issues = []
        name = filepath.stem

        # Skip inherently-plural concept names (mass nouns with no sensible singular)
        if name in INHERENTLY_PLURAL_CONCEPTS:
            return issues

        # Skip if name doesn't end in 's' or ends in common non-plural suffixes
        non_plural_suffixes = ('ss', 'us', 'is', 'sis', 'ness', 'ics', 'ous')
        if not name.endswith('s') or name.lower().endswith(non_plural_suffixes):
            return issues

        # Check if singular form exists as alias
        singular = name[:-1]  # Remove trailing 's'

        # Parse frontmatter for aliases
        if content.startswith("---"):
            second_dash = content.find("---", 3)
            if second_dash != -1:
                frontmatter = content[3:second_dash]
                if f"aliases:" in frontmatter:
                    # Check if singular form is in aliases (case-insensitive)
                    aliases_match = re.search(r'aliases:\s*\[([^\]]+)\]', frontmatter)
                    if aliases_match:
                        aliases = [a.strip().strip('"\'') for a in aliases_match.group(1).split(',')]
                        if any(a.lower() == singular.lower() for a in aliases):
                            return issues  # Singular form exists as alias, OK

        issues.append(Issue(
            "warning",
            "naming",
            f"Concept note uses plural name '{name}'. Consider renaming to '{singular}' (singular)"
        ))
        return issues

    def _check_correlation_structure(self, content: str, filepath: Path) -> list[Issue]:
        """Check that sector and index notes have a correlation structure section."""
        issues = []

        if "## Correlation structure" not in content:
            issues.append(Issue(
                "warning",
                "structure",
                "Missing '## Correlation structure' section"
            ))
            return issues

        # Check for avg correlation value
        if not re.search(r'Avg correlation.*\d+\.\d+', content, re.IGNORECASE):
            issues.append(Issue(
                "warning",
                "structure",
                "Correlation structure missing average correlation value"
            ))

        return issues

    def _check_sector_correlation(self, content: str, filepath: Path) -> list[Issue]:
        """Check that public company actor notes have a sector correlation section.

        Fix: python scripts/add_sector_correlations.py --ticker TICKER
        """
        issues = []

        if "## Sector correlation" not in content and "## Volatility correlation" not in content:
            issues.append(Issue(
                "error",
                "sector-correlation",
                "Missing '## Sector correlation' section — run: "
                "python scripts/add_sector_correlations.py --ticker TICKER"
            ))

        return issues

    def _check_quick_stats(
        self,
        content: str,
        filepath: Path,
        missing_severity: str = "warning",
    ) -> list[Issue]:
        """Check for Quick stats section."""
        issues = []

        if "## Quick stats" not in content:
            issues.append(Issue(missing_severity, "structure", "Missing '## Quick stats' section"))

        return issues

    def _check_private_capital_founder_edge(self, content: str, filepath: Path) -> list[Issue]:
        """Warn when a mature fund note lacks a founder/principals narrative section."""
        issues = []

        body = content
        if content.startswith("---"):
            second_dash = content.find("---", 3)
            if second_dash != -1:
                body = content[second_dash + 3:]

        non_empty_lines = sum(1 for line in body.split("\n") if line.strip())
        if non_empty_lines < 40:
            return issues

        founder_sections = [
            "## Founder read",
            "## Founder edge",
            "## Principals",
            "## Partners",
            "## Notable partners",
        ]
        if any(section in content for section in founder_sections):
            return issues

        issues.append(Issue(
            "warning",
            "founder-edge",
            "Mature private-capital/fund note missing founder/principals narrative. "
            "Add ## Founder read or ## Principals explaining who the people are, "
            "their network/source-of-capital edge, and third-party origin context."
        ))

        return issues

    def _check_analyst_structure(self, content: str, filepath: Path) -> list[Issue]:
        """Check source-person notes in Analysts/ for the folder's minimum shape."""
        issues = []

        if not content.startswith("---"):
            return issues

        second_dash = content.find("---", 3)
        if second_dash == -1:
            return issues

        frontmatter = content[3:second_dash]
        body = content[second_dash + 3:]

        if "tags:" not in frontmatter:
            issues.append(Issue("error", "frontmatter", "Analyst notes require YAML tags in frontmatter"))

        if re.search(r"(?m)^type:\s*actor\s*$", frontmatter):
            issues.append(Issue("error", "taxonomy", "Analyst note frontmatter should not use type: actor"))

        if self._has_tag(content, "#actor"):
            issues.append(Issue("error", "taxonomy", "Analyst notes should not carry the actor tag"))

        body_tag_lines = re.findall(r"(?m)^#[A-Za-z0-9_-][^\n]*", body)
        if body_tag_lines:
            examples = ", ".join(line.strip() for line in body_tag_lines[:3])
            remaining = len(body_tag_lines) - min(len(body_tag_lines), 3)
            message = f"Analyst tags belong in YAML frontmatter, not body hashtag lines: {examples}"
            if remaining:
                message += f" (+{remaining} more)"
            issues.append(Issue("error", "taxonomy", message))

        return issues

    def _check_bold_formatting(self, content: str, filepath: Path) -> list[Issue]:
        """Flag bold formatting (**text**) in the note, exempting the opening definition line."""
        issues = []

        # Skip frontmatter
        body = content
        if content.startswith("---"):
            second_dash = content.find("---", 3)
            if second_dash != -1:
                body = content[second_dash + 3:]

        # Find bold patterns: **text** (but not inside code blocks)
        # Remove code blocks first
        body_no_code = re.sub(r'```.*?```', '', body, flags=re.DOTALL)
        body_no_code = re.sub(r'`[^`]+`', '', body_no_code)

        bold_matches = re.findall(r'\*\*(.+?)\*\*', body_no_code)

        # Exempt the first bold instance (opening definition line convention)
        extra_matches = bold_matches[1:]

        if extra_matches:
            examples = extra_matches[:3]
            preview = ", ".join(f'**{b}**' for b in examples)
            remaining = len(extra_matches) - len(examples)
            msg = f"Contains {len(extra_matches)} bold instances (excluding definition line): {preview}"
            if remaining > 0:
                msg += f" (+{remaining} more)"
            issues.append(Issue("error", "bold", msg))

        return issues

    def _check_dead_links(self, content: str, filepath: Path) -> list[Issue]:
        """Check for wikilinks that don't resolve to existing notes."""
        issues = []

        # Find all wikilinks: [[Note]] or [[Note|Display]] or [[Note\|Display]] (escaped in tables)
        # The pattern handles both escaped and unescaped pipes
        wikilinks = re.findall(r'\[\[([^\]|\\]+)(?:\\?\|[^\]]+)?\]\]', content)

        seen = set()  # Deduplicate
        for link in wikilinks:
            # Skip image embeds
            if link.endswith(('.png', '.jpg', '.jpeg', '.gif', '.svg')):
                continue

            # Obsidian links may include anchors or folder-qualified paths.
            # Resolve those against the note name before treating them as dead.
            note_name = link.split("#", 1)[0]
            if not note_name:
                continue
            note_name = note_name.replace("\\", "/").split("/")[-1]

            # Skip already seen
            if note_name in seen:
                continue
            seen.add(note_name)

            # Check if note exists (by filename or frontmatter alias)
            if note_name not in self.existing_notes and note_name not in self.known_aliases:
                issues.append(Issue("warning", "dead-link", f"Dead link: [[{link}]]"))

        return issues


    def _check_missing_links(self, content: str, filepath: Path) -> list[Issue]:
        """Check for existing vault entities mentioned without wikilinks.

        Runs by default as a warning-level check. With --suggest-links,
        uses "suggestion" severity to enable --fix auto-linking.
        """
        issues = []
        # "suggestion" when --suggest-links (enables --fix); "warning" by default
        severity = "suggestion" if self.suggest_links else "warning"

        # Get already-linked notes
        linked = set(re.findall(r'\[\[([^\]|\\]+)(?:\\?\|[^\]]+)?\]\]', content))

        # Remove wikilinks from content so we don't match terms inside them
        content_without_links = re.sub(r'\[\[[^\]]+\]\]', '', content)

        # Sort by length descending so "AMD Ventures" matches before "AMD"
        for note_name in sorted(self.existing_notes, key=lambda n: (-len(n), n)):
            if note_name == filepath.stem:  # Skip self
                continue
            if note_name in linked:  # Already linked
                continue
            if note_name in COMMON_WORD_NOTE_NAMES:  # Common-word collision (e.g. "Gold", "Flow")
                continue
            if note_name.isdigit():  # Pure numbers (e.g. "99") are never entity references
                continue
            if re.match(r"^\d{4}-\d{2}-\d{2}$", note_name):  # Daily-note dates (e.g. "2026-04-12")
                continue

            # Case-sensitive whole-word match in content without links
            if re.search(rf'\b{re.escape(note_name)}\b', content_without_links):
                issues.append(Issue(severity, "missing-link",
                    f"Mentions '{note_name}' — consider [[{note_name}]]"))

        return issues


    def _check_price_chart(self, content: str, filepath: Path, is_etf: bool) -> list[Issue]:
        """Check for price chart embed.

        Actor notes: fundamentals chart (which includes price overlay) satisfies this check.
        Securities/ETF notes: still require a standalone price chart.
        """
        issues = []

        # Look for price chart patterns
        has_price_chart = bool(re.search(r'!\[\[.*(-price|-vs-|price-chart).*\.png\]\]', content, re.IGNORECASE))

        # Fundamentals chart includes price overlay — counts as price chart for actor notes
        has_fundamentals = bool(re.search(r'!\[\[.*(fundamentals|financials).*\.png\]\]', content, re.IGNORECASE))
        is_securities = 'securities' in filepath.stem.lower()

        # Allow for data quality / unavailable notes (recent IPOs, etc.)
        has_chart_exemption = bool(re.search(
            r'(chart(ing)?|price)\s*(data\s*)?(unavailable|quality|issues?|corrupt|manual\s*tracking)',
            content, re.IGNORECASE
        ))

        # Actor notes with a fundamentals chart don't need a separate price chart
        if has_fundamentals and not is_etf and not is_securities:
            return issues

        if not has_price_chart and not has_chart_exemption:
            chart_type = "ETF" if is_etf else "Public company"
            ticker = self._extract_ticker(content)
            slug = filepath.stem.lower().replace(" ", "-")
            fix_hint = ""
            if ticker:
                fix_hint = (
                    f". Fix: generate via /api/chart/image?ticker={ticker}&primary={ticker}"
                    f" -> save as investing/attachments/{slug}-price-chart.png"
                    f" and embed with ![[{slug}-price-chart.png]]"
                )
            issues.append(Issue("error", "chart", f"{chart_type} missing price chart{fix_hint}"))

        return issues

    def _check_fundamentals_chart(self, content: str, filepath: Path) -> list[Issue]:
        """Check for fundamentals chart embed."""
        issues = []

        # Accept both "fundamentals" and "financials" in filename
        has_fundamentals = bool(re.search(r'!\[\[.*(fundamentals|financials).*\.png\]\]', content, re.IGNORECASE))

        # Allow for pre-profit startups / recent IPOs with limited disclosure,
        # and for cases where quarterly fundamentals data is unavailable even
        # though annual financials are present (common for foreign listings).
        has_exemption = bool(re.search(
            r'(pre-profit|limited\s*(financial\s*)?disclosure|not\s*(yet\s*)?public|recently\s*ipo|fundamentals\s*(chart\s*)?(data\s*)?unavailable|quarterly\s*fundamentals\s*(data\s*)?unavailable|annual-only\s*financial)',
            content, re.IGNORECASE
        ))

        if not has_fundamentals and not has_exemption:
            ticker = self._extract_ticker(content)
            slug = filepath.stem.lower().replace(" ", "-")
            fix_hint = ""
            if ticker:
                fix_hint = (
                    f". Fix: ensure fundamentals exist (fetch_fundamentals.py {ticker}),"
                    f" then generate via /api/chart/lw?tickers={ticker}&metrics=revenue,netincome"
                    f" -> save as investing/attachments/{slug}-fundamentals-chart.png"
                    f" and embed with ![[{slug}-fundamentals-chart.png]]"
                )
            issues.append(Issue("error", "chart", f"Company missing fundamentals chart{fix_hint}"))

        return issues

    def _check_sankey_chart(self, content: str, filepath: Path) -> list[Issue]:
        """Check for income statement Sankey chart embed."""
        issues = []

        has_sankey = bool(re.search(r'!\[\[.*sankey.*\.png\]\]', content, re.IGNORECASE))

        # Allow same exemptions as fundamentals (pre-profit, limited disclosure, etc.)
        has_exemption = bool(re.search(
            r'(pre-profit|limited\s*(financial\s*)?disclosure|not\s*(yet\s*)?public|recently\s*ipo|income\s*statement\s*(data\s*)?unavailable|annual-only\s*financial)',
            content, re.IGNORECASE
        ))

        if not has_sankey and not has_exemption:
            ticker = self._extract_ticker(content)
            slug = filepath.stem.lower().replace(" ", "-")
            fix_hint = ""
            if ticker:
                fix_hint = (
                    f". Fix: generate via /api/chart/sankey?ticker={ticker}"
                    f" -> save as investing/attachments/{slug}-sankey.png"
                    f" and embed with ![[{slug}-sankey.png]]"
                )
            issues.append(Issue("error", "chart", f"Company missing income statement Sankey chart{fix_hint}"))

        return issues

    def _check_securities_split(self, content: str, filepath: Path) -> list[Issue]:
        """Check that public company actor notes link to a securities note."""
        issues = []

        # Only applies to actor notes in Actors/ folder
        if 'Actors' not in str(filepath):
            return issues

        # Skip stubs (< 15 non-empty lines in body)
        body = content.split('---', 2)[-1] if content.count('---') >= 2 else content
        non_empty = sum(1 for line in body.split("\n") if line.strip())
        if non_empty < 15:
            return issues

        # Check for [[X securities note]] link (with legacy [[X securities]] still accepted)
        name = filepath.stem
        has_securities_link = bool(re.search(
            r'\[\[' + re.escape(name) + r'\s+securities(\s+note)?\]\]', content, re.IGNORECASE
        ))

        if not has_securities_link:
            issues.append(Issue(
                "error", "securities-split",
                f"Public company missing [[{name} securities note]] link in Related."
                f" Create investing/Assets/{name} securities note.md and link from Related > ### Securities"
            ))

        return issues

    def _check_product_chart(self, content: str, filepath: Path) -> list[Issue]:
        """Check for usage metrics chart in product notes (MAU, DAU, GMV, etc.)."""
        issues = []

        # Look for any chart embed - products have varied metrics
        has_chart = bool(re.search(r'!\[\[.*\.png\]\]', content))

        if not has_chart:
            slug = filepath.stem.lower().replace(" ", "-")
            fix_hint = (
                f". Fix: generate via /api/chart/lw?product={filepath.stem}&product_metrics=global_mau,revenue"
                f" -> save as investing/attachments/{slug}-usage-chart.png"
                f" and embed with ![[{slug}-usage-chart.png]]"
            )
            issues.append(Issue("error", "chart", f"Product missing usage chart (MAU, DAU, GMV, etc.){fix_hint}"))

        return issues

    def _check_hub_chart(self, content: str, filepath: Path, note_type: str) -> list[Issue]:
        """Check that sector/concept hub notes embed a current visual artifact."""
        issues = []

        has_chart = bool(re.search(r'!\[\[.*\.(png|jpe?g|gif|svg)\]\]', content, re.IGNORECASE))
        has_exemption = bool(re.search(
            r'('
            r'chart(ing)?|price|market|correlation|cluster|usage|fundamentals'
            r')\s*(data\s*)?(unavailable|not\s+available|not\s+applicable|n/a|quality|issues?|corrupt|manual\s*tracking)'
            r'|no\s+(chart|market|price|correlation)\s+(data\s+)?(available|applicable)',
            content,
            re.IGNORECASE,
        ))

        if not has_chart and not has_exemption:
            label = "Sector" if note_type == "sector" else "Concept"
            slug = filepath.stem.lower().replace(" ", "-")
            issues.append(Issue(
                "error",
                "chart",
                f"{label} note missing embedded chart. Fix: generate a latest-data chart via /api/chart/lw"
                f" -> save as investing/attachments/{slug}-chart.png"
                f" and embed with ![[{slug}-chart.png]], or state why chart data is unavailable."
            ))

        return issues

    def _check_cluster_validation_diagnostics(self, content: str, filepath: Path) -> list[Issue]:
        """Check cluster-owner notes for the standard validation diagnostics."""
        issues = []

        is_cluster_owner_path = (
            self._is_under_folder(filepath, "Concepts")
            or self._is_under_folder(filepath, "Sectors")
        )
        if not is_cluster_owner_path:
            return issues

        is_cluster_note = (
            bool(re.search(r'(?im)^>\s*\[![^\]]+\]\s*Cluster status:', content))
            or bool(re.search(r'(?im)^##\s+Cluster validation\b(?!\s+status\b)', content))
        )
        if not is_cluster_note:
            return issues

        def has(pattern: str) -> bool:
            return bool(re.search(pattern, content, re.IGNORECASE | re.MULTILINE))

        embed = r'!\[\[[^\]]*{stem}[^\]]*\.png(?:\|[^\]]*)?\]\]'

        if not has(r'^>\s*\[![^\]]+\]\s*Cluster status:'):
            issues.append(Issue(
                "error",
                "cluster-validation",
                "Cluster note missing status callout. Fix: add "
                "`> [!success|warning|failure] Cluster status: ...` below the H1."
            ))

        if not has(r'^##\s+Cluster validation\b'):
            issues.append(Issue(
                "error",
                "cluster-validation",
                "Cluster note missing `## Cluster validation` section."
            ))

        required_embeds = [
            ("correlation heatmap", "correlation"),
            ("dendrogram", "dendrogram"),
            ("PCA diagnostic", "pca"),
            ("90-day rolling tightness chart", "rolling-tightness-90d"),
        ]
        for label, stem in required_embeds:
            if not has(embed.format(stem=re.escape(stem))):
                issues.append(Issue(
                    "error",
                    "cluster-validation",
                    f"Cluster validation missing {label} embed."
                ))

        if not has(r'^#{2,4}\s+PC1 index weights\b'):
            issues.append(Issue(
                "error",
                "cluster-validation",
                "Cluster validation missing `PC1 index weights` section."
            ))

        if not has(r'\bRaw PC1-mimic weight\b'):
            issues.append(Issue(
                "error",
                "cluster-validation",
                "Cluster validation missing raw PC1-mimic weight table/column."
            ))

        has_join_distance_table = (
            has(r'\bjoin distance\b')
            and has(r'Distance\s*\(1-\\?\|corr\\?\|\)')
        )
        if not has_join_distance_table:
            issues.append(Issue(
                "error",
                "cluster-validation",
                "Cluster validation missing candidate join-distance topology table "
                "with `Distance (1-|corr|)`."
            ))

        if not has(r'^#{2,4}\s+Historical tightness evolution\b'):
            issues.append(Issue(
                "error",
                "cluster-validation",
                "Cluster validation missing `Historical tightness evolution` section."
            ))

        has_topology_vs_mimic = has(r'\bPC1-mimic\b') and has(
            r'\b(topology|dendrogram|join[- ]distance|core|satellite|later-joining)\b'
        )
        if not has_topology_vs_mimic:
            issues.append(Issue(
                "warning",
                "cluster-validation",
                "Cluster validation should distinguish topology from the raw-return PC1-mimic basket."
            ))

        has_history_verdict = has(
            r'\b(structurally durable|structurally tight|durable|newly formed|fragmenting|regime-dependent)\b'
        )
        if not has_history_verdict:
            issues.append(Issue(
                "warning",
                "cluster-validation",
                "Historical tightness section should say whether the cluster is durable, newly formed, "
                "fragmenting, or regime-dependent."
            ))

        return issues

    def _check_chart_captions(self, content: str, filepath: Path) -> list[Issue]:
        """Check that chart embeds have caption lines below them."""
        issues = []

        lines = content.split("\n")
        for i, line in enumerate(lines):
            # Check if this is an image embed
            if re.match(r'!\[\[.*\.(png|jpe?g|gif|svg)\]\]', line, re.IGNORECASE):
                # Next line should be italic caption or blank then italic
                next_idx = i + 1
                if next_idx < len(lines):
                    next_line = lines[next_idx].strip()
                    # Skip blank lines
                    while next_idx < len(lines) and not next_line:
                        next_idx += 1
                        if next_idx < len(lines):
                            next_line = lines[next_idx].strip()

                    # Check if it's an italic caption
                    if next_line and not next_line.startswith("*"):
                        issues.append(Issue("warning", "chart-caption", f"Chart missing caption: {line}"))

        return issues

    def _check_historical_financials(self, content: str, filepath: Path) -> list[Issue]:
        """Check for historical financials (10-year requirement for public companies)."""
        issues = []

        has_exemption = bool(re.search(
            r'(pre-profit|limited\s*(financial\s*)?disclosure|not\s*(yet\s*)?public|recently\s*ipo|annual-only\s*financial|historical\s*financials\s*(data\s*)?unavailable)',
            content, re.IGNORECASE
        ))
        if has_exemption:
            return issues

        # Look for Financials section
        if "## Financials" not in content and "### Annual" not in content:
            issues.append(Issue("error", "financials", "Missing Financials section with historical data"))
            return issues

        # Check for 10-year table pattern
        # Should have years like 2016, 2017... or FY columns
        year_pattern = r'\|\s*20[12]\d\s*\|'
        year_matches = re.findall(year_pattern, content)

        if len(set(year_matches)) < 5:
            issues.append(Issue("warning", "financials", "Financials table may not have 10 years of history"))

        # Check for required columns (case-insensitive, flexible matching)
        # Note: EPS is optional for loss-making companies, Stock Price shown in charts
        required_cols = {
            "Revenue": ["revenue", "total revenue", "net revenue"],
            "Net Income": ["net income", "net profit", "earnings"],
        }

        financials_section = content[content.find("## Financials"):] if "## Financials" in content else content
        financials_lower = financials_section.lower()

        for col_name, patterns in required_cols.items():
            if not any(p in financials_lower for p in patterns):
                issues.append(Issue("warning", "financials", f"Financials may be missing: {col_name}"))

        return issues

    def _check_cap_table(self, content: str, filepath: Path) -> list[Issue]:
        """Check for cap table in private company notes."""
        issues = []

        cap_table_patterns = [
            "## Cap table",
            "### Cap table",
            "## Ownership",
            "## Financing",
            "## Funding history",
            "### Funding history",
            "### Valuation history",
        ]

        has_cap_table = any(pattern in content for pattern in cap_table_patterns)

        if not has_cap_table:
            issues.append(Issue("error", "cap-table", "Private company missing cap table / funding history"))

        return issues

    def _check_funding_rounds(self, content: str, filepath: Path) -> list[Issue]:
        """Check for funding rounds table in private company notes."""
        issues = []

        funding_patterns = [
            "## Funding rounds",
            "### Funding rounds",
            "## Funding history",
            "### Funding history",
            "## Investment rounds",
            "### Investment rounds",
        ]

        has_funding_rounds = any(pattern in content for pattern in funding_patterns)

        # Also check for a table with Series/Round info
        if not has_funding_rounds:
            has_funding_rounds = bool(re.search(r'\|\s*(Series\s*[A-Z]|Seed|Round)\s*\|', content, re.IGNORECASE))

        if not has_funding_rounds:
            issues.append(Issue("error", "funding-rounds", "Private company missing funding rounds table"))
            return issues

        # Check for lazy catch-all rows like "Earlier" or "Various"
        lazy_patterns = [
            r'\|\s*Earlier\s*\|',
            r'\|\s*Various\s*\|',
            r'\|\s*Prior\s*(rounds?)?\s*\|',
            r'\|\s*Other\s*\|',
            r'\|\s*Previous\s*\|',
        ]
        for pattern in lazy_patterns:
            if re.search(pattern, content, re.IGNORECASE):
                issues.append(Issue("warning", "funding-rounds",
                    "Funding table has catch-all row (Earlier/Various) — expand to individual rounds"))
                break

        # Check for gaps in series letters
        # Only look within funding/cap table sections to avoid false positives
        # from portfolio company mentions
        funding_section = ""
        for section_header in ["## Funding", "### Funding", "## Cap table", "### Cap table"]:
            if section_header in content:
                start = content.find(section_header)
                # Find next ## section or end of file
                next_section = content.find("\n## ", start + 1)
                if next_section == -1:
                    funding_section = content[start:]
                else:
                    funding_section = content[start:next_section]
                break

        if funding_section:
            series_matches = re.findall(r'\|\s*Series\s*([A-Z])\b', funding_section, re.IGNORECASE)
            if series_matches:
                series_letters = sorted(set(s.upper() for s in series_matches))
                if series_letters:
                    # Check for gaps: if we have Series D, we should have A, B, C
                    highest = series_letters[-1]
                    expected = [chr(i) for i in range(ord('A'), ord(highest) + 1)]
                    missing = [s for s in expected if s not in series_letters]
                    if missing:
                        missing_str = ", ".join(f"Series {s}" for s in missing)
                        issues.append(Issue("warning", "funding-rounds",
                            f"Funding table missing rounds: {missing_str}"))

        return issues

    def _check_ownership_table(self, content: str, filepath: Path) -> list[Issue]:
        """Check for ownership/cap table with % estimates in private company notes."""
        issues = []

        ownership_patterns = [
            "### Ownership",
            "## Ownership",
            "### Ownership estimates",
            "## Ownership estimates",
            "### Cap table",  # With ownership % column
        ]

        has_ownership_section = any(pattern in content for pattern in ownership_patterns)

        # Also check for a table with ownership % column
        has_ownership_column = bool(re.search(r'\|\s*(Est\.?\s*)?Ownership\s*\|', content, re.IGNORECASE))
        has_pct_column = bool(re.search(r'\|\s*%\s*\||\|\s*Stake\s*\|', content, re.IGNORECASE))

        if not has_ownership_section and not has_ownership_column and not has_pct_column:
            issues.append(Issue("warning", "ownership-table", "Private company missing ownership % estimates table"))

        return issues

    def _check_private_financials(self, content: str, filepath: Path) -> list[Issue]:
        """Check for historical financials in private company notes."""
        issues = []

        # Look for any financials table (Revenue, EBITDA, Net income, etc.)
        has_financials = bool(re.search(r'\|\s*(Revenue|EBITDA|Net income|Net debt)\s*\|', content, re.IGNORECASE))

        if not has_financials:
            issues.append(Issue("warning", "financials", "Private company missing historical financials"))

        return issues

    def _check_table_formatting(self, content: str, filepath: Path) -> list[Issue]:
        """Check that tables have blank lines before them (required for Obsidian rendering)."""
        issues = []
        lines = content.split("\n")

        for i, line in enumerate(lines):
            # Check if this line starts a table (starts with |)
            if line.strip().startswith("|") and i > 0:
                # Look at previous non-empty line
                prev_idx = i - 1
                while prev_idx >= 0 and not lines[prev_idx].strip():
                    prev_idx -= 1

                if prev_idx >= 0:
                    prev_line = lines[prev_idx].strip()
                    # If previous line is content (not blank, not another table row, not a heading)
                    # and immediately precedes the table, it needs a blank line
                    if (prev_line and
                        not prev_line.startswith("|") and
                        not prev_line.startswith("#") and
                        i - 1 == prev_idx):  # No blank line between
                        # Extract context for error message
                        context = prev_line[:40] + "..." if len(prev_line) > 40 else prev_line
                        issues.append(Issue("warning", "table-format",
                            f"Table needs blank line after: {context}"))

        return issues

    def _check_leadership(self, content: str, filepath: Path) -> list[Issue]:
        """Check for Leadership section in company notes."""
        issues = []

        leadership_patterns = [
            "## Leadership",
            "### Leadership",
            "## Management",
            "### Management",
            "## Executive team",
            "### Executive team",
        ]

        has_leadership = any(pattern in content for pattern in leadership_patterns)

        if not has_leadership:
            issues.append(Issue("warning", "leadership", "Company missing Leadership section"))
            return issues

        # Check for CEO/CFO in leadership table
        content_lower = content.lower()
        has_ceo = bool(re.search(r'\|\s*ceo\b', content_lower))
        has_cfp = bool(re.search(r'\|\s*cf[op]\b', content_lower))  # CFO or CFP

        if not has_ceo:
            issues.append(Issue("warning", "leadership", "Leadership section may be missing CEO"))

        return issues

    def _check_evolution(self, content: str, filepath: Path) -> list[Issue]:
        """Check for Evolution section in actor notes (companies, countries, institutions).

        Stubs are exempt — Evolution is added when a note matures beyond stub level.
        A note is considered a stub if it has fewer than 40 non-empty lines of body content.
        """
        issues = []

        # Skip stubs: count non-empty lines after frontmatter
        body = content
        if content.startswith("---"):
            second_dash = content.find("---", 3)
            if second_dash != -1:
                body = content[second_dash + 3:]

        non_empty_lines = sum(1 for line in body.split("\n") if line.strip())
        if non_empty_lines < 40:
            return issues  # Stub — exempt

        evolution_patterns = [
            "## Evolution",
            "### Evolution",
        ]

        has_evolution = any(pattern in content for pattern in evolution_patterns)

        if not has_evolution:
            issues.append(Issue("warning", "evolution", "Mature actor note missing Evolution section"))

        return issues

    def _check_synopsis(self, content: str, filepath: Path) -> list[Issue]:
        """Check that actor notes have a synopsis paragraph after the one-liner.

        The synopsis is the dense lede paragraph immediately after the opening
        **Name** — definition line. It should be at least 100 characters to
        qualify as a real synopsis (not just a stub sentence).

        Stubs (< 40 non-empty body lines) are exempt.
        """
        issues = []

        # Skip stubs
        body = content
        if content.startswith("---"):
            second_dash = content.find("---", 3)
            if second_dash != -1:
                body = content[second_dash + 3:]

        non_empty_lines = sum(1 for line in body.split("\n") if line.strip())
        if non_empty_lines < 40:
            return issues

        # Find the opening definition line (starts with **)
        body_lines = body.strip().split("\n")

        # Skip tag lines (e.g., #actor #public) to find the definition line
        def_line_idx = None
        for i, line in enumerate(body_lines):
            stripped = line.strip()
            if not stripped:
                continue
            if stripped.startswith("#") and not stripped.startswith("##"):
                continue  # tag line
            if stripped.startswith("**") or " — " in stripped or " — " in stripped:
                def_line_idx = i
                break
            break  # something else came first

        if def_line_idx is None:
            return issues

        # Look for a substantial paragraph after the definition line
        # (before the first ## heading or ---)
        synopsis_text = []
        for i in range(def_line_idx + 1, len(body_lines)):
            stripped = body_lines[i].strip()
            if stripped.startswith("##") or stripped == "---":
                break
            if stripped:
                synopsis_text.append(stripped)

        total_len = sum(len(s) for s in synopsis_text)

        if total_len < 100:
            issues.append(Issue("warning", "synopsis",
                "Actor note missing synopsis paragraph after definition line"))

        return issues

    def _check_unsourced_work_claim(self, content: str, filepath: Path) -> list[Issue]:
        """Flag a superlative book/work claim that names no concrete titled work.

        The vault convention is to cite specific works ("Author of *Title* (Year)").
        A sentence that asserts a definitive / seminal / canonical / authoritative
        book or text WITHOUT an italicized title, a quoted title, or a source URL
        matches the fabrication shape that produced the invented "definitive book
        on RLHF" rather than a real citation. Warning-level — it nudges "name the
        work or cite it"; it never blocks an edit. A bare [[wikilink]] does not
        count as a title (it is usually a concept link), and "forthcoming" works
        (no title yet) and titled claims are exempt.
        """
        issues = []

        body = content
        if content.startswith("---"):
            second_dash = content.find("---", 3)
            if second_dash != -1:
                body = content[second_dash + 3:]

        body = re.sub(r"```.*?```", "", body, flags=re.DOTALL)  # drop fenced code

        qualifier = r"(?:definitive|seminal|canonical|authoritative|landmark|foundational|go-to)"
        work_noun = r"(?:books?|textbooks?|guides?|treatises?|monographs?|accounts?)"
        trigger = re.compile(
            rf"\b{qualifier}\b[\w\s,'’-]{{0,24}}?\b{work_noun}\b", re.IGNORECASE
        )
        # Concrete reference in the same sentence: italic *title*, "quoted title"
        # (straight or curly), or a source URL.
        concrete = re.compile(
            r"(?<!\*)\*(?!\*)[^*\n]{2,}\*(?!\*)"
            r"|[\"“][^\"”\n]{2,}[\"”]"
            r"|https?://"
        )

        for line in body.split("\n"):
            stripped = line.strip()
            if not stripped or stripped[0] in "|>#!":
                continue
            for sent in re.split(r"(?<=[.!?])\s+", stripped):
                if not trigger.search(sent):
                    continue
                if re.search(r"forthcoming", sent, re.IGNORECASE):
                    continue
                if concrete.search(sent):
                    continue
                claim = re.sub(r"\s+", " ", sent).strip()
                if len(claim) > 110:
                    claim = claim[:110] + "…"
                issues.append(Issue(
                    "warning", "unsourced-work-claim",
                    f"Superlative work claim with no concrete title or source: "
                    f"\"{claim}\". Name the specific work (*Title* (Year)) or cite it."
                ))

        return issues

    def _check_analyst_timeline(self, content: str, filepath: Path) -> list[Issue]:
        """Check for Analyst timeline section in public company notes.

        Stubs (< 40 non-empty body lines) are exempt.
        """
        issues = []

        # Skip stubs
        body = content
        if content.startswith("---"):
            second_dash = content.find("---", 3)
            if second_dash != -1:
                body = content[second_dash + 3:]

        non_empty_lines = sum(1 for line in body.split("\n") if line.strip())
        if non_empty_lines < 40:
            return issues

        if "## Analyst timeline" not in content:
            issues.append(Issue("warning", "analyst-timeline",
                "Public company missing '## Analyst timeline' section"))

        return issues

    def _check_credit_rating(self, content: str, filepath: Path) -> list[Issue]:
        """Check for ratings history section in public company notes.

        Looks for a dedicated ratings history section or table with S&P /
        Moody's / Fitch ratings and dates.  Stubs (< 40 non-empty body
        lines) are exempt.
        """
        issues = []

        # Skip stubs
        body = content
        if content.startswith("---"):
            second_dash = content.find("---", 3)
            if second_dash != -1:
                body = content[second_dash + 3:]

        non_empty_lines = sum(1 for line in body.split("\n") if line.strip())
        if non_empty_lines < 40:
            return issues

        # Check for ratings history section header or ratings history table
        has_ratings_section = bool(re.search(
            r'##\s*(?:Ratings?\s+history|Credit\s+ratings?\s+history|Ratings?)',
            content, re.IGNORECASE
        ))

        # Also accept a table with multiple rating entries (agency + date pattern)
        has_ratings_table = bool(re.search(
            r'\|[^|]*(?:S&P|Moody|Fitch)[^|]*\|[^|]*\d{4}[^|]*\|',
            content
        ))

        # Single rating mention in Quick stats still counts
        has_rating_row = bool(re.search(
            r'\|[^|]*(?:S&P\s+rating|Moody|Fitch|[Cc]redit\s+rating)[^|]*\|',
            content
        ))

        if not has_ratings_section and not has_ratings_table and not has_rating_row:
            issues.append(Issue("warning", "credit-rating",
                "Public company missing ratings history section."
                " Add ## Ratings history with S&P/Moody's/Fitch ratings and dates"))

        # Check placement: Ratings history should come after Financials and before Related
        if has_ratings_section:
            headers = [(m.start(), m.group()) for m in
                       re.finditer(r'^##\s+.+', content, re.MULTILINE)]
            header_names = [h[1] for h in headers]

            ratings_idx = next((i for i, h in enumerate(header_names)
                                if re.search(r'##\s*Ratings?\s+history', h, re.IGNORECASE)), None)
            financials_idx = next((i for i, h in enumerate(header_names)
                                   if re.search(r'##\s*Financials', h, re.IGNORECASE)), None)
            related_idx = next((i for i, h in enumerate(header_names)
                                if re.search(r'##\s*Related', h, re.IGNORECASE)), None)

            if ratings_idx is not None:
                if financials_idx is not None and ratings_idx < financials_idx:
                    issues.append(Issue("warning", "credit-rating-placement",
                        "## Ratings history should come after ## Financials, not before"))
                if related_idx is not None and ratings_idx > related_idx:
                    issues.append(Issue("warning", "credit-rating-placement",
                        "## Ratings history should come before ## Related"))

        return issues

    def _check_synthesis(self, content: str, filepath: Path) -> list[Issue]:
        """Check that concept and event notes have a ## Synthesis section.

        Stubs (< 40 non-empty body lines) are exempt.
        """
        issues = []

        # Skip stubs
        body = content
        if content.startswith("---"):
            second_dash = content.find("---", 3)
            if second_dash != -1:
                body = content[second_dash + 3:]

        non_empty_lines = sum(1 for line in body.split("\n") if line.strip())
        if non_empty_lines < 40:
            return issues

        if "## Synthesis" not in content:
            issues.append(Issue("warning", "synthesis",
                "Concept/event note missing '## Synthesis' section"))

        return issues

    def _check_ma_market_reaction(self, content: str, filepath: Path) -> list[Issue]:
        """Check that public-company M&A event notes capture market reaction.

        Strategic rationale and the market's first judgment are separate facts.
        If at least one linked actor is public, require a dedicated section for
        acquirer/target price moves, premium or exchange-ratio implications,
        implied consideration/spread math, and closing-risk read.
        """
        issues = []

        if not self._is_ma_event(content, filepath):
            return issues

        if not self._ma_event_involves_public_company(content):
            return issues

        has_market_reaction = bool(re.search(
            r'^##\s+Market\s+Reaction\b',
            content,
            re.IGNORECASE | re.MULTILINE
        ))

        if not has_market_reaction:
            issues.append(Issue(
                "warning",
                "market-reaction",
                "Public-company M&A event missing ## Market Reaction section "
                "with acquirer/target stock moves, premium or exchange-ratio "
                "implication, implied consideration/spread math, close/fail odds "
                "when defensible, external proxies, and tape verdict."
            ))

        return issues

    def _check_market_reaction_placeholders(self, content: str, filepath: Path) -> list[Issue]:
        """Warn when a Market Reaction section still has unresolved placeholders."""
        issues = []

        match = re.search(
            r'^##\s+Market\s+Reaction\b(?P<body>.*?)(?=^##\s+|\Z)',
            content,
            re.IGNORECASE | re.MULTILINE | re.DOTALL
        )
        if not match:
            return issues

        body = match.group("body")
        if re.search(r'\b(TODO|TBD|verify later|TODO verify)\b', body, re.IGNORECASE):
            issues.append(Issue(
                "warning",
                "market-reaction-placeholder",
                "Market Reaction section contains unresolved TODO/TBD/verify placeholder; "
                "verify primary and peer tape or state explicitly why closes are not yet available."
            ))

        return issues

    @staticmethod
    def _extract_wikilink_targets(content: str) -> set[str]:
        """Extract Obsidian wikilink targets as note names without headings/aliases."""
        targets: set[str] = set()
        for match in re.finditer(r'\[\[([^\]]+)\]\]', content):
            target = match.group(1).split("|", 1)[0].split("#", 1)[0].strip()
            if target:
                targets.add(target)
        return targets

    @staticmethod
    def _extract_market_reaction_body(content: str) -> str | None:
        match = re.search(
            r'^##\s+Market\s+Reaction\b(?P<body>.*?)(?=^##\s+|\Z)',
            content,
            re.IGNORECASE | re.MULTILINE | re.DOTALL
        )
        return match.group("body") if match else None

    def _event_related_or_readthrough_targets(self, content: str) -> set[str]:
        """Return entity-list/read-through links that should be market-reaction candidates."""
        targets: set[str] = set()

        related = re.search(
            r'^##\s+Related\b(?P<body>.*?)(?=^##\s+|\Z)',
            content,
            re.IGNORECASE | re.MULTILINE | re.DOTALL
        )
        if related:
            targets.update(self._extract_wikilink_targets(related.group("body")))

        for heading in re.finditer(
            r'^#{2,4}\s+(?:For\s+)?(?P<body>.*\[\[[^\]]+\]\].*)$',
            content,
            re.IGNORECASE | re.MULTILINE
        ):
            targets.update(self._extract_wikilink_targets(heading.group("body")))

        return targets

    def _check_market_reaction_peer_coverage(self, content: str, filepath: Path) -> list[Issue]:
        """Warn when listed actors in entity/read-through links are absent from Market Reaction."""
        issues = []
        market_body = self._extract_market_reaction_body(content)
        if market_body is None:
            return issues

        missing: list[str] = []
        for name in sorted(self._event_related_or_readthrough_targets(content)):
            actor_path = self.vault_root / "Actors" / f"{name}.md"
            if not actor_path.exists():
                continue

            try:
                actor_content = actor_path.read_text(encoding="utf-8")
            except (OSError, UnicodeDecodeError):
                continue

            ticker = self._extract_public_actor_ticker(actor_content)
            if not ticker:
                continue

            link_pattern = rf'\[\[{re.escape(name)}(?:[#|][^\]]*)?\]\]'
            ticker_pattern = rf'(?<![A-Z0-9.\-]){re.escape(ticker)}(?![A-Z0-9.\-])'
            if re.search(link_pattern, market_body) or re.search(ticker_pattern, market_body):
                continue

            missing.append(f"[[{name}]] ({ticker})")

        if missing:
            issues.append(Issue(
                "warning",
                "market-reaction-peer-coverage",
                "Market Reaction may be missing listed related/read-through actors: "
                + ", ".join(missing)
                + ". Add same-day/next-day tape or explicitly state why excluded."
            ))

        return issues

    def _is_ma_event(self, content: str, filepath: Path) -> bool:
        """Detect M&A event notes from tags, filename, or deal language."""
        if self._has_tag(content, "#ma"):
            return True

        text = f"{filepath.stem}\n{content}"
        return bool(re.search(
            r'\b(M&A|merger|acquisition|takeover|buyout|spin-merger|'
            r'all-stock|cash-and-stock|stock-and-cash|exchange\s+ratio|'
            r'definitive\s+(agreement|transaction)|acquir(?:e|es|ed|ing))\b',
            text,
            re.IGNORECASE
        ))

    def _ma_event_involves_public_company(self, content: str) -> bool:
        """Return True when an M&A event links to at least one public actor."""
        linked_names = set(re.findall(r'\[\[([^\]|\\]+)(?:\\?\|[^\]]+)?\]\]', content))

        for name in linked_names:
            actor_path = self.vault_root / "Actors" / f"{name}.md"
            if not actor_path.exists():
                continue
            try:
                actor_content = actor_path.read_text(encoding="utf-8")
            except (OSError, UnicodeDecodeError):
                continue
            if self._is_public_company(actor_content):
                return True

        return False

    def _check_oneliner_links(self, content: str, filepath: Path) -> list[Issue]:
        """Check that hub one-liners link to the entities they enumerate.

        Hub notes (concepts, sectors) often enumerate sub-entities in their
        opening one-liner. Any note name mentioned there should be wikilinked.
        """
        issues = []

        # Extract the one-liner: first non-empty, non-frontmatter, non-tag line
        body = content
        if content.startswith("---"):
            end = content.find("---", 3)
            if end != -1:
                body = content[end + 3:]

        oneliner = ""
        for line in body.split("\n"):
            stripped = line.strip()
            if not stripped:
                continue
            if stripped.startswith("#") and not stripped.startswith("##"):
                continue  # skip tag lines like #concept #sector
            oneliner = stripped
            break

        if not oneliner:
            return issues

        # Remove existing wikilinks from the one-liner for checking
        oneliner_plain = re.sub(r'\[\[[^\]]+\]\]', '', oneliner)

        # Check if any existing note names appear unlinked in the one-liner
        for note_name in sorted(self.existing_notes, key=lambda n: (-len(n), n)):
            if note_name == filepath.stem:
                continue
            if len(note_name) < 4:  # Skip very short names
                continue
            if note_name in COMMON_WORD_NOTE_NAMES:  # Common-word collision
                continue
            if note_name.isdigit() or re.match(r"^\d{4}-\d{2}-\d{2}$", note_name):
                continue
            if re.search(rf'\b{re.escape(note_name)}\b', oneliner_plain):
                issues.append(Issue("warning", "oneliner-link",
                    f"One-liner mentions '{note_name}' without wikilink"))

        return issues

    def _check_table_cell_links(self, content: str, filepath: Path) -> list[Issue]:
        """Check that table cells matching existing note names are wikilinked.

        Scans markdown tables for cell values that exactly match (case-sensitive)
        an existing vault note name but aren't wikilinked.
        """
        issues = []
        seen = set()

        for line in content.split("\n"):
            # Only process table rows
            if not line.strip().startswith("|"):
                continue
            # Skip separator rows
            if re.match(r'^\s*\|[\s\-:|]+\|', line):
                continue

            # Split into cells
            cells = [c.strip() for c in line.split("|")]
            for cell in cells:
                if not cell:
                    continue
                # Skip cells that already contain wikilinks
                if "[[" in cell:
                    continue
                # Strip markdown formatting for matching
                clean = re.sub(r'\*+', '', cell).strip()
                if not clean or len(clean) < 3:
                    continue
                # Check if the cell text exactly matches a note name
                if (clean in self.existing_notes and clean != filepath.stem
                        and clean not in seen
                        and clean not in COMMON_WORD_NOTE_NAMES
                        and not clean.isdigit()):
                    seen.add(clean)
                    issues.append(Issue("warning", "table-cell-link",
                        f"Table cell '{clean}' matches existing note — use [[{clean}]]"))

        return issues

    def _check_bidirectional_related(self, content: str, filepath: Path) -> list[Issue]:
        """Check that Related section links are bidirectional.

        If this note links to another concept/sector note in its Related section,
        that target should link back. Only checks notes that exist and are
        concept or sector type.
        """
        issues = []

        # Extract Related section
        related_match = re.search(r'^## Related\b.*?\n(.*?)(?=\n## |\Z)', content,
                                  re.MULTILINE | re.DOTALL)
        if not related_match:
            return issues

        related_text = related_match.group(1)

        # Extract all wikilinks from the Related section
        linked_names = set(re.findall(r'\[\[([^\]|]+?)(?:\|[^\]]+)?\]\]', related_text))

        this_name = filepath.stem

        for target_name in linked_names:
            # Find the target file
            target_path = None
            for md_file in self.vault_root.rglob(f"{target_name}.md"):
                target_path = md_file
                break

            if target_path is None or not target_path.exists():
                continue

            target_content = target_path.read_text(encoding="utf-8")
            target_type = self._get_note_type(target_content)

            # Only check concept and sector notes
            if target_type not in ("concept", "sector"):
                continue

            # Check if target's Related section links back to this note
            target_related = re.search(r'^## Related\b.*?\n(.*?)(?=\n## |\Z)',
                                       target_content, re.MULTILINE | re.DOTALL)
            if not target_related:
                issues.append(Issue("suggestion", "bidirectional-related",
                    f"[[{target_name}]] (Related) has no Related section linking back to [[{this_name}]]"))
                continue

            target_linked = set(re.findall(r'\[\[([^\]|]+?)(?:\|[^\]]+)?\]\]',
                                           target_related.group(1)))
            if this_name not in target_linked:
                issues.append(Issue("suggestion", "bidirectional-related",
                    f"[[{target_name}]] (Related) does not link back to [[{this_name}]]"))

        return issues


def log_to_daily_note(vault_root: Path, fixes_by_file: dict[str, list[str]]):
    """Append fix report to today's daily note."""
    if not fixes_by_file:
        return

    today = date.today().strftime("%Y-%m-%d")
    daily_note = vault_root / "Daily" / f"{today}.md"

    # Build report
    total = sum(len(fixes) for fixes in fixes_by_file.values())
    lines = [f"\n### Link fixes ({total} total)\n"]
    for filename, fixed_names in fixes_by_file.items():
        links = ", ".join(f"[[{name}]]" for name in fixed_names)
        lines.append(f"- **{filename}**: {links}")
    lines.append("")

    report = "\n".join(lines)

    if daily_note.exists():
        content = daily_note.read_text(encoding="utf-8")
        # Append before ## Related if it exists, otherwise at end
        if "## Related" in content:
            content = content.replace("## Related", f"{report}\n## Related")
        else:
            content = content.rstrip() + "\n" + report
        daily_note.write_text(content, encoding="utf-8")
    else:
        # Create minimal daily note
        daily_note.write_text(f"# {today}\n{report}", encoding="utf-8")

    print(f"Logged to {daily_note.name}")


def get_changed_files(vault_root: Path) -> list[Path]:
    """Get list of .md files changed in git (staged or unstaged)."""
    try:
        # Get both staged and unstaged changes
        result = subprocess.run(
            ["git", "diff", "--name-only", "HEAD"],
            capture_output=True,
            text=True,
            cwd=vault_root.parent,  # Run from repo root
        )
        files = result.stdout.strip().split("\n")

        # Also get untracked files
        result2 = subprocess.run(
            ["git", "ls-files", "--others", "--exclude-standard"],
            capture_output=True,
            text=True,
            cwd=vault_root.parent,
        )
        files.extend(result2.stdout.strip().split("\n"))

        # Filter to note classes with structural compliance checks.
        md_files = []
        for f in files:
            if (
                f
                and f.endswith(".md")
                and any(f"investing/{folder}" in f for folder in ("Actors", "Analysts"))
            ):
                full_path = vault_root.parent / f
                if full_path.exists():
                    md_files.append(full_path)

        return md_files
    except Exception as e:
        print(f"Error getting changed files: {e}", file=sys.stderr)
        return []


def main():
    # Windows defaults stdout/stderr to cp1252; printing a non-ASCII note name
    # (e.g. "Adam Glapiński") under output redirection raises UnicodeEncodeError
    # and aborts a full --all sweep partway. Force UTF-8 so reports never crash
    # on accented/CJK note names (matches the PostToolUse hook's handling).
    for _stream in (sys.stdout, sys.stderr):
        try:
            _stream.reconfigure(encoding="utf-8")
        except Exception:
            pass

    parser = argparse.ArgumentParser(description="Check vault notes for compliance")
    parser.add_argument("files", nargs="*", help="Files to check")
    parser.add_argument("--changed", action="store_true", help="Check git-changed files only")
    parser.add_argument("--orphans", action="store_true", help="Find frequently mentioned terms without notes")
    parser.add_argument("--min-mentions", type=int, default=5, help="Minimum mentions for orphan detection (default: 5)")
    parser.add_argument("--suggest-links", action="store_true", help="Suggest missing wikilinks")
    parser.add_argument("--fix", action="store_true", help="Auto-fix missing wikilinks (requires --suggest-links)")
    parser.add_argument("--create-stubs", action="store_true", help="Create stub notes for dead links")
    parser.add_argument("--all", action="store_true", help="Check all notes (Actors, Concepts, Events, Theses)")
    parser.add_argument("--market-reaction-peer-sweep", action="store_true",
                        help="Check all event notes for listed related/read-through actors missing from ## Market Reaction")
    parser.add_argument("--log", action="store_true", help="Log fixes to today's daily note")
    parser.add_argument("--limit", "-n", type=int, help="Stop after N files")
    parser.add_argument("--offset", type=int, default=0, help="Skip first N files")
    parser.add_argument("--verbose", "-v", action="store_true", help="Show passing checks too")
    parser.add_argument("--no-index-cache", action="store_true",
                        help="Disable the per-file vault index cache (rebuild from disk every run)")
    args = parser.parse_args()

    # Find vault root
    script_dir = Path(__file__).parent
    vault_root = script_dir.parent / "investing"

    if not vault_root.exists():
        print(f"Error: Vault not found at {vault_root}", file=sys.stderr)
        sys.exit(1)

    # --fix for link suggestions requires --suggest-links
    # (bold fix always works with --fix)

    checker = NoteChecker(vault_root, suggest_links=args.suggest_links, use_index_cache=not args.no_index_cache)

    # Handle focused market-reaction peer coverage sweep.
    if args.market_reaction_peer_sweep:
        events_dir = vault_root / "Events"
        results: list[tuple[str, Issue]] = []

        for filepath in sorted(events_dir.glob("*.md")):
            try:
                content = filepath.read_text(encoding="utf-8", errors="ignore")
            except (OSError, UnicodeDecodeError) as exc:
                results.append((filepath.name, Issue(
                    "warning",
                    "read-error",
                    f"Could not read event note: {exc}"
                )))
                continue

            for issue in checker._check_market_reaction_peer_coverage(content, filepath):
                results.append((filepath.name, issue))

        for filename, issue in results:
            print(f"{filename}: {issue.message}")
        print(f"TOTAL={len(results)}")
        sys.exit(1 if results else 0)

    # Handle --orphans mode
    if args.orphans:
        print(f"Scanning vault for orphan terms (min {args.min_mentions} mentions)...\n")
        orphans = checker.find_orphan_terms(min_mentions=args.min_mentions)

        if not orphans:
            print("No orphan terms found.")
            sys.exit(0)

        print(f"Found {len(orphans)} terms mentioned frequently but without notes:\n")
        print(f"{'Term':<30} {'Count':>6}  Sample files")
        print("-" * 70)

        for term, count, samples in orphans[:50]:  # Show top 50
            sample_str = ", ".join(samples[:3])
            if len(samples) > 3:
                sample_str += f" (+{len(samples)-3} more)"
            # Handle unicode safely for Windows console
            try:
                print(f"{term:<30} {count:>6}  {sample_str}")
            except UnicodeEncodeError:
                print(f"{term:<30} {count:>6}  (files with special chars)")

        if len(orphans) > 50:
            print(f"\n... and {len(orphans) - 50} more terms")

        print(f"\nTop candidates for new notes:")
        for term, count, samples in orphans[:10]:
            print(f"  - [[{term}]] ({count} mentions)")

        sys.exit(0)

    # Determine files to check
    if args.changed:
        files = get_changed_files(vault_root)
        if not files:
            print("No changed .md files in investing/Actors or investing/Analysts")
            sys.exit(0)
    elif args.files:
        files = [Path(f) for f in args.files]
    elif args.all:
        # Check all note types
        files = []
        for folder in ["Actors", "Analysts", "Concepts", "Events", "Theses"]:
            folder_path = vault_root / folder
            if folder_path.exists():
                files.extend(folder_path.glob("*.md"))
    else:
        # Default: check all primary source/entity notes.
        files = []
        for folder in ["Actors", "Analysts"]:
            folder_path = vault_root / folder
            if folder_path.exists():
                files.extend(folder_path.glob("*.md"))

    # Check each file
    total_errors = 0
    total_warnings = 0
    total_fixed = 0
    total_stubs = 0
    files_checked = 0
    total_files = len(files)
    fixes_by_file = {}  # Track for logging
    stubs_created = []  # Track created stubs
    files_processed = []  # Track which files were checked

    def print_summary(interrupted=False):
        status = "INTERRUPTED" if interrupted else "COMPLETE"
        print(f"\n{'='*50}")
        print(f"{status}: Checked {files_checked}/{total_files} files")
        print(f"Errors: {total_errors}")
        print(f"Warnings: {total_warnings}")
        if args.fix:
            print(f"Fixed: {total_fixed}")
            print(f"\nNotes visited:")
            for name in files_processed:
                filename = f"{name}.md"
                if filename in fixes_by_file:
                    links = ', '.join(f"[[{l}]]" for l in fixes_by_file[filename])
                    print(f"  {name}: {links}")
                else:
                    print(f"  {name}: (no fixes)")
        if args.create_stubs and stubs_created:
            print(f"Stubs created: {total_stubs}")
            for stub_name, source in stubs_created:
                print(f"  + {stub_name} (from {source})")
        if args.log and fixes_by_file:
            log_to_daily_note(vault_root, fixes_by_file)

    def handle_interrupt(signum, frame):
        print_summary(interrupted=True)
        sys.exit(130)

    signal.signal(signal.SIGINT, handle_interrupt)

    for i, filepath in enumerate(sorted(files)):
        if i < args.offset:
            continue

        if not filepath.exists():
            print(f"File not found: {filepath}", file=sys.stderr)
            continue

        issues = checker.check_note(filepath)
        files_processed.append(filepath.stem)

        errors = [i for i in issues if i.severity == "error"]
        warnings = [i for i in issues if i.severity == "warning"]
        suggestions = [i for i in issues if i.severity == "suggestion"]

        total_errors += len(errors)
        total_warnings += len(warnings)

        # Auto-fix bold if requested
        bold_fixed = 0
        if args.fix:
            bold_issues = [i for i in issues if i.rule == "bold"]
            if bold_issues:
                bold_fixed = checker.fix_bold(filepath)
                total_fixed += bold_fixed

        # Auto-fix missing links if requested
        fixed = []
        if args.fix and suggestions:
            fixed = checker.fix_missing_links(filepath)
            total_fixed += len(fixed)
            if fixed:
                fixes_by_file[filepath.name] = fixed

        # Create stub notes for dead links if requested
        if args.create_stubs:
            content = filepath.read_text(encoding="utf-8")
            dead_links = checker.get_dead_links(content)
            for link_name in dead_links:
                stub_path = checker.create_stub_note(link_name, filepath)
                if stub_path.name not in [s[0] for s in stubs_created]:
                    stubs_created.append((stub_path.name, filepath.stem))
                    total_stubs += 1

        # Always show file name when fixing
        if args.fix:
            if bold_fixed or fixed:
                parts = []
                if bold_fixed:
                    parts.append(f"{bold_fixed} bold")
                if fixed:
                    parts.append(f"{len(fixed)} links")
                print(f"\n{filepath.name}: fixed {', '.join(parts)}")
                for name in fixed:
                    print(f"  + [[{name}]]")
            else:
                print(f"\n{filepath.name}: no fixes needed")
        elif issues or args.verbose:
            status = "FAIL" if errors else ("WARN" if warnings else "PASS")
            print(f"\n{status}: {filepath.name}")

            for issue in issues:
                if issue.severity == "error":
                    prefix = "  ERROR"
                elif issue.severity == "warning":
                    prefix = "  WARN "
                else:
                    prefix = "  HINT "
                print(f"{prefix} [{issue.rule}] {issue.message}")

        files_checked += 1

        if args.limit and files_checked >= args.limit:
            break

    print_summary()
    sys.exit(1 if total_errors > 0 else 0)


if __name__ == "__main__":
    main()
