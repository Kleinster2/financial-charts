#!/usr/bin/env python3
"""
Note compliance checker for the investing vault.

Checks actor notes against the standards defined in:
- investing/Meta/Note structures.md
- investing/Meta/Financials templates.md
- CLAUDE.md

Usage:
    python scripts/check_note_compliance.py investing/Actors/Snap.md
    python scripts/check_note_compliance.py investing/Actors/*.md  # Check all
    python scripts/check_note_compliance.py --changed  # Check git-changed files
    python scripts/check_note_compliance.py --orphans  # Find frequently mentioned terms without notes
"""

import argparse
from collections import Counter
from datetime import date
import re
import signal
import subprocess
import sys
from pathlib import Path
from typing import NamedTuple


class Issue(NamedTuple):
    severity: str  # "error" or "warning"
    rule: str
    message: str


class NoteChecker:
    def __init__(self, vault_root: Path, suggest_links: bool = False):
        self.vault_root = vault_root
        self.suggest_links = suggest_links
        self.existing_notes = self._index_existing_notes()

    def _index_existing_notes(self) -> set[str]:
        """Index all existing note names (without .md extension)."""
        notes = set()
        for md_file in self.vault_root.rglob("*.md"):
            # Skip Daily notes and Meta folder
            if "/Daily/" in str(md_file) or "\\Daily\\" in str(md_file):
                continue
            if "/Meta/" in str(md_file) or "\\Meta\\" in str(md_file):
                continue
            notes.add(md_file.stem)
        return notes

    def check_note(self, filepath: Path) -> list[Issue]:
        """Check a single note for compliance issues."""
        issues = []

        content = filepath.read_text(encoding="utf-8")
        lines = content.split("\n")

        # Determine note type from hashtags
        note_type = self._get_note_type(content)

        # Missing links check applies to all note types
        if self.suggest_links and note_type in ("actor", "etf", "benchmark", "concept", "event", "thesis"):
            issues.extend(self._check_missing_links(content, filepath))

        # Remaining checks are actor-specific
        if note_type not in ("actor", "etf", "benchmark"):
            return issues

        is_public = self._is_public_company(content)
        is_etf = note_type in ("etf", "benchmark") or "#etf" in content or "#benchmark" in content
        is_private = "#private" in content
        is_person = "#person" in content
        is_geography = "#geography" in content or any(tag in content for tag in ["#country", "#region", "#city"])
        is_vc = "#vc" in content
        is_product = "#product" in content  # Products belong to parent companies

        # Structure checks
        issues.extend(self._check_frontmatter(content, filepath))
        issues.extend(self._check_related_section(content, filepath))
        issues.extend(self._check_quick_stats(content, filepath))
        issues.extend(self._check_table_formatting(content, filepath))

        # Link checks
        issues.extend(self._check_dead_links(content, filepath))

        # Chart checks (public companies and ETFs, not products)
        if (is_public or is_etf) and not is_product:
            issues.extend(self._check_price_chart(content, filepath, is_etf))
            issues.extend(self._check_chart_captions(content, filepath))

        # Product chart checks (usage metrics like MAU, DAU, GMV)
        if is_product:
            issues.extend(self._check_product_chart(content, filepath))
            issues.extend(self._check_chart_captions(content, filepath))

        # Fundamentals chart (public companies only, not ETFs/products)
        if is_public and not is_etf and not is_person and not is_geography and not is_vc and not is_product:
            issues.extend(self._check_fundamentals_chart(content, filepath))

        # Financials checks (not products - those go on parent company)
        if is_public and not is_etf and not is_person and not is_geography and not is_vc and not is_product:
            issues.extend(self._check_historical_financials(content, filepath))

        # Cap table checks (private companies, not products)
        if is_private and not is_person and not is_geography and not is_vc and not is_product:
            issues.extend(self._check_cap_table(content, filepath))
            issues.extend(self._check_private_financials(content, filepath))

        # Leadership check (companies, not ETFs/people/geographies/products)
        if (is_public or is_private) and not is_etf and not is_person and not is_geography and not is_product:
            issues.extend(self._check_leadership(content, filepath))

        return issues

    def _get_note_type(self, content: str) -> str:
        """Determine note type from hashtags."""
        if "#actor" in content:
            if "#etf" in content or "#benchmark" in content:
                return "etf"
            return "actor"
        if "#concept" in content:
            return "concept"
        if "#event" in content:
            return "event"
        if "#thesis" in content:
            return "thesis"
        return "unknown"

    def _is_public_company(self, content: str) -> bool:
        """Check if note is for a public company."""
        # Has ticker in quick stats
        if re.search(r"Ticker\s*\|\s*[A-Z]{1,5}\s*\(", content):
            return True
        # Has #private tag = not public
        if "#private" in content:
            return False
        # Has #brand tag = subsidiary/brand, not standalone public
        if "#brand" in content:
            return False
        # Is an actor without #private = assume public
        if "#actor" in content and "#person" not in content:
            return True
        return False

    def _check_frontmatter(self, content: str, filepath: Path) -> list[Issue]:
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
            issues.append(Issue("warning", "frontmatter", "Missing aliases in frontmatter"))

        return issues

    def _check_related_section(self, content: str, filepath: Path) -> list[Issue]:
        """Check for Related section."""
        issues = []

        if "## Related" not in content:
            issues.append(Issue("error", "structure", "Missing '## Related' section"))

        return issues

    def _check_quick_stats(self, content: str, filepath: Path) -> list[Issue]:
        """Check for Quick stats section."""
        issues = []

        if "## Quick stats" not in content:
            issues.append(Issue("warning", "structure", "Missing '## Quick stats' section"))

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

            # Skip already seen
            if link in seen:
                continue
            seen.add(link)

            # Check if note exists
            if link not in self.existing_notes:
                issues.append(Issue("warning", "dead-link", f"Dead link: [[{link}]]"))

        return issues

    def _check_missing_links(self, content: str, filepath: Path) -> list[Issue]:
        """Suggest wikilinks for mentioned notes that aren't linked."""
        issues = []

        # Get already-linked notes
        linked = set(re.findall(r'\[\[([^\]|\\]+)(?:\\?\|[^\]]+)?\]\]', content))

        # Remove wikilinks from content so we don't match terms inside them
        content_without_links = re.sub(r'\[\[[^\]]+\]\]', '', content)

        # Sort by length descending so "AMD Ventures" matches before "AMD"
        for note_name in sorted(self.existing_notes, key=len, reverse=True):
            if note_name == filepath.stem:  # Skip self
                continue
            if note_name in linked:  # Already linked
                continue

            # Case-sensitive whole-word match in content without links
            if re.search(rf'\b{re.escape(note_name)}\b', content_without_links):
                issues.append(Issue("suggestion", "missing-link",
                    f"Mentions '{note_name}' — consider [[{note_name}]]"))

        return issues

    def fix_missing_links(self, filepath: Path) -> list[str]:
        """Auto-fix missing wikilinks in a note. Returns list of fixed names."""
        content = filepath.read_text(encoding="utf-8")
        fixed = []

        # Get already-linked notes
        linked = set(re.findall(r'\[\[([^\]|\\]+)(?:\\?\|[^\]]+)?\]\]', content))

        # Check against content without links to avoid false positives
        content_without_links = re.sub(r'\[\[[^\]]+\]\]', '', content)

        # Sort by length descending so "AMD Ventures" matches before "AMD"
        for note_name in sorted(self.existing_notes, key=len, reverse=True):
            if note_name == filepath.stem:  # Skip self
                continue
            if note_name in linked:  # Already linked
                continue

            # Only proceed if term exists outside of wikilinks
            if not re.search(rf'\b{re.escape(note_name)}\b', content_without_links):
                continue

            # Replace only occurrences NOT inside wikilinks
            # Use a function to check each match
            def replace_if_not_in_link(match):
                start = match.start()
                # Check if this position is inside a wikilink
                before = content[:start]
                open_brackets = before.count('[[') - before.count(']]')
                if open_brackets > 0:
                    return match.group(0)  # Inside a link, don't replace
                return f'[[{note_name}]]'

            pattern = rf'\b{re.escape(note_name)}\b'
            new_content = re.sub(pattern, replace_if_not_in_link, content)
            if new_content != content:
                content = new_content
                fixed.append(note_name)

        if fixed:
            filepath.write_text(content, encoding="utf-8")

        return fixed

    def _check_price_chart(self, content: str, filepath: Path, is_etf: bool) -> list[Issue]:
        """Check for price chart embed."""
        issues = []

        # Look for price chart patterns
        has_price_chart = bool(re.search(r'!\[\[.*(-price|-vs-|price-chart).*\.png\]\]', content, re.IGNORECASE))

        # Allow for data quality / unavailable notes (recent IPOs, etc.)
        has_chart_exemption = bool(re.search(
            r'(chart(ing)?|price)\s*(data\s*)?(unavailable|quality|issues?|corrupt|manual\s*tracking)',
            content, re.IGNORECASE
        ))

        if not has_price_chart and not has_chart_exemption:
            chart_type = "ETF" if is_etf else "Public company"
            issues.append(Issue("error", "chart", f"{chart_type} missing price chart"))

        return issues

    def _check_fundamentals_chart(self, content: str, filepath: Path) -> list[Issue]:
        """Check for fundamentals chart embed."""
        issues = []

        # Accept both "fundamentals" and "financials" in filename
        has_fundamentals = bool(re.search(r'!\[\[.*(fundamentals|financials).*\.png\]\]', content, re.IGNORECASE))

        # Allow for pre-profit startups / recent IPOs with limited disclosure
        has_exemption = bool(re.search(
            r'(pre-profit|limited\s*(financial\s*)?disclosure|not\s*(yet\s*)?public|recently\s*ipo)',
            content, re.IGNORECASE
        ))

        if not has_fundamentals and not has_exemption:
            issues.append(Issue("error", "chart", "Company missing fundamentals chart"))

        return issues

    def _check_product_chart(self, content: str, filepath: Path) -> list[Issue]:
        """Check for usage metrics chart in product notes (MAU, DAU, GMV, etc.)."""
        issues = []

        # Look for any chart embed - products have varied metrics
        has_chart = bool(re.search(r'!\[\[.*\.png\]\]', content))

        if not has_chart:
            issues.append(Issue("error", "chart", "Product missing usage chart (MAU, DAU, GMV, etc.)"))

        return issues

    def _check_chart_captions(self, content: str, filepath: Path) -> list[Issue]:
        """Check that chart embeds have caption lines below them."""
        issues = []

        lines = content.split("\n")
        for i, line in enumerate(lines):
            # Check if this is an image embed
            if re.match(r'!\[\[.*\.png\]\]', line):
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
            "### Funding history",
            "### Valuation history",
        ]

        has_cap_table = any(pattern in content for pattern in cap_table_patterns)

        if not has_cap_table:
            issues.append(Issue("error", "cap-table", "Private company missing cap table / funding history"))

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

    def find_orphan_terms(self, min_mentions: int = 5) -> list[tuple[str, int, list[str]]]:
        """Find terms mentioned frequently but without corresponding notes.

        Returns list of (term, count, sample_files) tuples, sorted by count descending.
        """
        # Common words to exclude (not potential note names)
        stopwords = {
            # Articles, prepositions, conjunctions
            'The', 'This', 'That', 'These', 'Those', 'With', 'From', 'Into', 'About',
            'After', 'Before', 'During', 'Through', 'Between', 'Under', 'Over',
            'Against', 'Within', 'Without', 'Around', 'Among', 'Beyond',
            # Common verbs/words
            'Also', 'Just', 'Only', 'Even', 'Still', 'Already', 'Always', 'Never',
            'Often', 'Usually', 'Sometimes', 'Perhaps', 'Maybe', 'However', 'Therefore',
            'Because', 'Although', 'While', 'Since', 'Until', 'Unless', 'Whether',
            'Both', 'Either', 'Neither', 'Each', 'Every', 'Some', 'Many', 'Most',
            'Other', 'Another', 'Such', 'What', 'Which', 'Where', 'When', 'Why', 'How',
            'Could', 'Would', 'Should', 'Must', 'Might', 'Will', 'Can', 'May',
            'Does', 'Did', 'Has', 'Had', 'Have', 'Was', 'Were', 'Been', 'Being',
            'Are', 'But', 'For', 'Not', 'You', 'All', 'Can', 'Her', 'His', 'Its',
            'New', 'Now', 'Old', 'See', 'Way', 'Who', 'Boy', 'Did', 'Get', 'Has',
            'Him', 'Let', 'Put', 'Say', 'She', 'Too', 'Use', 'Day', 'Got', 'Here',
            'Made', 'Make', 'More', 'Much', 'Need', 'Next', 'Part', 'Take', 'Than',
            'Them', 'Then', 'Very', 'Want', 'Well', 'Went', 'Year', 'Your', 'Know',
            'Like', 'Time', 'Good', 'Look', 'People', 'Think', 'First', 'Last',
            'Long', 'Great', 'Little', 'Own', 'Same', 'Right', 'Big', 'High', 'Small',
            # Financial/investment terms too generic
            'Stock', 'Stocks', 'Market', 'Markets', 'Price', 'Prices', 'Value', 'Trade',
            'Trading', 'Investment', 'Investing', 'Investor', 'Investors', 'Company',
            'Companies', 'Business', 'Revenue', 'Profit', 'Growth', 'Risk', 'Return',
            'Asset', 'Assets', 'Fund', 'Funds', 'Share', 'Shares', 'Equity', 'Debt',
            'Capital', 'Cash', 'Income', 'Earnings', 'Quarter', 'Annual', 'Fiscal',
            'Financial', 'Economic', 'Economy', 'Sector', 'Industry', 'Data', 'Chart',
            # Time/date words
            'January', 'February', 'March', 'April', 'June', 'July', 'August',
            'September', 'October', 'November', 'December', 'Monday', 'Tuesday',
            'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'Today',
            'Yesterday', 'Tomorrow', 'Week', 'Month', 'Year', 'Daily', 'Weekly',
            # Meta/format words
            'Note', 'Notes', 'Section', 'Table', 'List', 'Link', 'Links', 'Related',
            'Source', 'Sources', 'Example', 'Examples', 'Status', 'Update', 'Updated',
            'Created', 'See', 'Below', 'Above', 'Following', 'Previous',
            # Vault structure words
            'Metric', 'Metrics', 'Ticker', 'Focus', 'Founded', 'Quick', 'Detail',
            'Bull', 'Bear', 'Series', 'Case', 'Thesis', 'Parent', 'Sister', 'Actor',
            'Actors', 'Concept', 'Concepts', 'Event', 'Events', 'Sector', 'Sectors',
            'Description', 'Role', 'Type', 'Category', 'Name', 'Title', 'Summary',
            'Overview', 'Background', 'History', 'Strategy', 'Model', 'Approach',
            'Structure', 'Format', 'Template', 'Pattern', 'Annotation', 'Context',
            'Takeaway', 'Takeaways', 'Implications', 'Impact', 'Outlook', 'Valuation',
            'Correlation', 'Benchmark', 'Peer', 'Peers', 'Comparison', 'Analysis',
            'Leadership', 'Management', 'Board', 'Executive', 'Executives', 'Team',
            'Headquarters', 'Location', 'Region', 'Country', 'State', 'City',
            'Ownership', 'Stake', 'Position', 'Holdings', 'Portfolio', 'Allocation',
            # More common words
            'Product', 'Products', 'Service', 'Services', 'Customer', 'Customers',
            'Client', 'Clients', 'User', 'Users', 'Employee', 'Employees', 'Staff',
            'Partner', 'Partners', 'Partnership', 'Partnerships', 'Deal', 'Deals',
            'Transaction', 'Transactions', 'Acquisition', 'Acquisitions', 'Merger',
            'Launch', 'Launched', 'Release', 'Released', 'Announced', 'Announcement',
            'Report', 'Reports', 'Reported', 'Reporting', 'Filing', 'Filings',
            'Target', 'Targets', 'Goal', 'Goals', 'Plan', 'Plans', 'Planned',
            'Project', 'Projects', 'Initiative', 'Initiatives', 'Program', 'Programs',
            'Technology', 'Technologies', 'Platform', 'Platforms', 'System', 'Systems',
            'Solution', 'Solutions', 'Software', 'Hardware', 'Infrastructure',
            'Network', 'Networks', 'Server', 'Servers', 'Cloud', 'Center', 'Centers',
            'Power', 'Energy', 'Capacity', 'Supply', 'Demand', 'Production', 'Output',
            'Cost', 'Costs', 'Margin', 'Margins', 'Rate', 'Rates', 'Ratio', 'Ratios',
            'Performance', 'Results', 'Outcome', 'Outcomes', 'Success', 'Failure',
            'Change', 'Changes', 'Shift', 'Shifts', 'Trend', 'Trends', 'Movement',
            'Level', 'Levels', 'Stage', 'Stages', 'Phase', 'Phases', 'Step', 'Steps',
            'Issue', 'Issues', 'Problem', 'Problems', 'Challenge', 'Challenges',
            'Opportunity', 'Opportunities', 'Advantage', 'Advantages', 'Benefit',
            'Feature', 'Features', 'Function', 'Functions', 'Capability', 'Capabilities',
            'Access', 'Control', 'Support', 'Development', 'Research', 'Innovation',
            'Design', 'Build', 'Create', 'Develop', 'Expand', 'Grow', 'Scale',
            'Reduce', 'Increase', 'Improve', 'Enhance', 'Optimize', 'Transform',
            'Lead', 'Leader', 'Leaders', 'Leading', 'Head', 'Chief', 'Senior',
            'Director', 'Directors', 'Manager', 'Managers', 'Officer', 'Officers',
            'President', 'Vice', 'Chairman', 'Chair', 'Member', 'Members',
            'Founder', 'Founders', 'Owner', 'Owners', 'Shareholder', 'Shareholders',
            'Agreement', 'Agreements', 'Contract', 'Contracts', 'Terms', 'Conditions',
            'Policy', 'Policies', 'Rule', 'Rules', 'Regulation', 'Regulations',
            'Law', 'Laws', 'Legal', 'Compliance', 'Requirement', 'Requirements',
            'Standard', 'Standards', 'Quality', 'Safety', 'Security', 'Protection',
            'Process', 'Processes', 'Operation', 'Operations', 'Activity', 'Activities',
            'Action', 'Actions', 'Decision', 'Decisions', 'Choice', 'Choices',
            'Option', 'Options', 'Alternative', 'Alternatives', 'Possibility',
            'Reason', 'Reasons', 'Cause', 'Causes', 'Effect', 'Effects', 'Result',
            'Factor', 'Factors', 'Element', 'Elements', 'Component', 'Components',
            'Aspect', 'Aspects', 'Point', 'Points', 'Area', 'Areas', 'Field', 'Fields',
            'View', 'Views', 'Perspective', 'Perspectives', 'Opinion', 'Opinions',
            'Idea', 'Ideas', 'Thought', 'Thoughts', 'Belief', 'Beliefs', 'Assumption',
            'Claim', 'Claims', 'Statement', 'Statements', 'Comment', 'Comments',
            'Question', 'Questions', 'Answer', 'Answers', 'Response', 'Responses',
            'Form', 'Forms', 'Kind', 'Kinds', 'Sort', 'Sorts', 'Variety', 'Range',
            'Group', 'Groups', 'Class', 'Classes', 'Division', 'Divisions', 'Unit',
            'Line', 'Lines', 'Item', 'Items', 'Piece', 'Pieces', 'Part', 'Parts',
            'Whole', 'Entire', 'Complete', 'Full', 'Partial', 'Half', 'Quarter',
            'Beginning', 'End', 'Start', 'Finish', 'Middle', 'Center', 'Edge',
            'Side', 'Sides', 'Top', 'Bottom', 'Front', 'Back', 'Left', 'Right',
            'Order', 'Orders', 'Sequence', 'Priority', 'Priorities', 'Preference',
            'Way', 'Ways', 'Method', 'Methods', 'Means', 'Manner', 'Style', 'Mode',
            'Base', 'Basis', 'Foundation', 'Ground', 'Root', 'Core', 'Heart',
            'True', 'False', 'Real', 'Actual', 'Potential', 'Possible', 'Likely',
            'Certain', 'Sure', 'Clear', 'Obvious', 'Evident', 'Apparent', 'Visible',
            'Simple', 'Complex', 'Easy', 'Difficult', 'Hard', 'Soft', 'Strong', 'Weak',
            'Fast', 'Slow', 'Quick', 'Rapid', 'Steady', 'Stable', 'Volatile',
            'Open', 'Closed', 'Free', 'Restricted', 'Limited', 'Unlimited', 'Broad',
            'Wide', 'Narrow', 'Deep', 'Shallow', 'Thick', 'Thin', 'Heavy', 'Light',
            'Positive', 'Negative', 'Neutral', 'Mixed', 'Balanced', 'Biased',
            'Direct', 'Indirect', 'Internal', 'External', 'Domestic', 'Foreign',
            'General', 'Specific', 'Particular', 'Special', 'Unique', 'Common',
            'Normal', 'Typical', 'Usual', 'Regular', 'Standard', 'Custom', 'Original',
            'Initial', 'Final', 'Interim', 'Preliminary', 'Definitive', 'Official',
            # More specific stopwords from testing
            'Date', 'Trump', 'Bank', 'Credit', 'World', 'Texas', 'Pure', 'Post',
            'Amount', 'Less', 'Details', 'Period', 'Multiple', 'Various', 'Premium',
            'Multi', 'Dividend', 'Added', 'Lower', 'Higher', 'Largest', 'Segment',
            'Bloomberg', 'Notable', 'Timeline', 'Acquired', 'Tech', 'Korea', 'Singapore',
            'Person', 'Versus', 'Billion', 'Million', 'Trillion', 'Percent', 'Basis',
            'Index', 'Average', 'Median', 'Peak', 'Trough', 'Rally', 'Selloff', 'Crash',
            'Boom', 'Bust', 'Cycle', 'Wave', 'Bubble', 'Correction', 'Recovery',
            'Entry', 'Exit', 'Long', 'Short', 'Bullish', 'Bearish', 'Neutral',
            'Overweight', 'Underweight', 'Hold', 'Sell', 'Upgrade', 'Downgrade',
            'Wire', 'News', 'Press', 'Media', 'Article', 'Interview', 'Call',
            'Prior', 'Forward', 'Backward', 'Upward', 'Downward', 'Inward', 'Outward',
            'Annual', 'Quarterly', 'Monthly', 'Weekly', 'Daily', 'Yearly', 'Biannual',
            # Common descriptors that aren't proper nouns
            'Strategic', 'Enterprise', 'Digital', 'Regional', 'Retail', 'Diversified',
            'Corporate', 'Traditional', 'Legacy', 'Mobile', 'Commercial', 'Gross', 'Net',
            'Competitor', 'Competitors', 'Best', 'Risks', 'Theme', 'Round', 'Entity',
            'Former', 'Smaller', 'Larger', 'Medium', 'Small', 'Moderate', 'Extreme',
            'Built', 'Central', 'Hyperscaler', 'Geographic', 'Wikipedia', 'University',
            'Street', 'Grid', 'Watch', 'Ventures', 'North', 'South', 'East', 'West',
            'Pacific', 'Atlantic', 'America', 'Americas', 'York', 'Dhabi', 'David',
            'Financials', 'Brand', 'Export', 'Large', 'Exchange', 'Seed', 'Labs',
            'Vision', 'Driver', 'Near', 'Smart', 'Firm', 'Rare', 'Talent', 'Career',
            'Size', 'John', 'Property', 'None', 'Auto', 'Known', 'Combined', 'Chip',
            'Sold', 'Finance', 'Structural', 'Battery', 'Solar', 'Inference', 'Foundry',
            # Common adjectives
            'Major', 'Minor', 'Key', 'Main', 'Primary', 'Secondary', 'Top', 'Bottom',
            'Early', 'Late', 'Recent', 'Current', 'Future', 'Past', 'Present',
            'Global', 'Local', 'National', 'International', 'Public', 'Private',
            'Total', 'Average', 'Expected', 'Estimated', 'Reported', 'Announced',
        }

        # Collect all capitalized terms across vault
        term_counts: Counter[str] = Counter()
        term_files: dict[str, list[str]] = {}

        for md_file in self.vault_root.rglob("*.md"):
            # Skip Meta folder
            if "/Meta/" in str(md_file) or "\\Meta\\" in str(md_file):
                continue

            try:
                content = md_file.read_text(encoding="utf-8")
            except Exception:
                continue

            # Remove wikilinks so we don't count already-linked terms
            content_no_links = re.sub(r'\[\[[^\]]+\]\]', '', content)

            # Remove code blocks
            content_no_code = re.sub(r'```.*?```', '', content_no_links, flags=re.DOTALL)
            content_no_code = re.sub(r'`[^`]+`', '', content_no_code)

            # Find capitalized words (potential proper nouns)
            # Match single capitalized words
            single_matches = re.findall(r'\b([A-Z][a-z]+)\b', content_no_code)
            # Match multi-word proper nouns (2-3 consecutive capitalized words)
            multi_matches = re.findall(r'\b([A-Z][a-z]+(?:\s+[A-Z][a-z]+){1,2})\b', content_no_code)

            # Filter multi-word matches: all words must not be stopwords
            filtered_multi = []
            for phrase in multi_matches:
                words = phrase.split()
                if all(w not in stopwords for w in words):
                    filtered_multi.append(phrase)

            matches = single_matches + filtered_multi

            for term in matches:
                if term in stopwords:
                    continue
                # Skip single short words
                if len(term) < 4 and ' ' not in term:
                    continue
                # Skip common adjective/adverb patterns (likely not proper nouns)
                if re.match(r'.*(ive|ial|ical|ous|ary|ory|ern|ing|tion|ment|ness|able|ible|less|ful|ward|wise|like|ized|ising|ating|eted|ited|uted|sted|nced|rged|lled|pped|tted|dded|gged|mmed|nned|rred)$', term, re.IGNORECASE):
                    continue
                # Skip common nationality/regional adjectives
                if re.match(r'.*(ese|ish|ian|ean|can|ish)$', term, re.IGNORECASE) and len(term) < 12:
                    continue

                term_counts[term] += 1
                if term not in term_files:
                    term_files[term] = []
                if md_file.stem not in term_files[term]:
                    term_files[term].append(md_file.stem)

        # Filter to terms without notes, above threshold
        orphans = []
        for term, count in term_counts.most_common():
            if count < min_mentions:
                break
            if term not in self.existing_notes:
                # Get sample files (up to 3)
                samples = term_files.get(term, [])[:3]
                orphans.append((term, count, samples))

        return orphans


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

        # Filter to .md files in investing/Actors
        md_files = []
        for f in files:
            if f and f.endswith(".md") and "investing/Actors" in f:
                full_path = vault_root.parent / f
                if full_path.exists():
                    md_files.append(full_path)

        return md_files
    except Exception as e:
        print(f"Error getting changed files: {e}", file=sys.stderr)
        return []


def main():
    parser = argparse.ArgumentParser(description="Check vault notes for compliance")
    parser.add_argument("files", nargs="*", help="Files to check")
    parser.add_argument("--changed", action="store_true", help="Check git-changed files only")
    parser.add_argument("--orphans", action="store_true", help="Find frequently mentioned terms without notes")
    parser.add_argument("--min-mentions", type=int, default=5, help="Minimum mentions for orphan detection (default: 5)")
    parser.add_argument("--suggest-links", action="store_true", help="Suggest missing wikilinks")
    parser.add_argument("--fix", action="store_true", help="Auto-fix missing wikilinks (requires --suggest-links)")
    parser.add_argument("--all", action="store_true", help="Check all notes (Actors, Concepts, Events, Theses)")
    parser.add_argument("--log", action="store_true", help="Log fixes to today's daily note")
    parser.add_argument("--limit", "-n", type=int, help="Stop after N files")
    parser.add_argument("--offset", type=int, default=0, help="Skip first N files")
    parser.add_argument("--verbose", "-v", action="store_true", help="Show passing checks too")
    args = parser.parse_args()

    # Find vault root
    script_dir = Path(__file__).parent
    vault_root = script_dir.parent / "investing"

    if not vault_root.exists():
        print(f"Error: Vault not found at {vault_root}", file=sys.stderr)
        sys.exit(1)

    # --fix requires --suggest-links
    if args.fix and not args.suggest_links:
        print("Error: --fix requires --suggest-links", file=sys.stderr)
        sys.exit(1)

    checker = NoteChecker(vault_root, suggest_links=args.suggest_links)

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
            print("No changed .md files in investing/Actors")
            sys.exit(0)
    elif args.files:
        files = [Path(f) for f in args.files]
    elif args.all:
        # Check all note types
        files = []
        for folder in ["Actors", "Concepts", "Events", "Theses"]:
            folder_path = vault_root / folder
            if folder_path.exists():
                files.extend(folder_path.glob("*.md"))
    else:
        # Default: check all Actors
        files = list((vault_root / "Actors").glob("*.md"))

    # Check each file
    total_errors = 0
    total_warnings = 0
    total_fixed = 0
    files_checked = 0
    total_files = len(files)
    fixes_by_file = {}  # Track for logging
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

        # Auto-fix missing links if requested
        fixed = []
        if args.fix and suggestions:
            fixed = checker.fix_missing_links(filepath)
            total_fixed += len(fixed)
            if fixed:
                fixes_by_file[filepath.name] = fixed

        # Always show file name when fixing
        if args.fix:
            if fixed:
                print(f"\n{filepath.name}: fixed {len(fixed)} links")
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
