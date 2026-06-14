"""Vault analytics for NoteChecker (mixin): orphan-term detection."""
import re
from collections import Counter
from pathlib import Path


class AnalyticsMixin:
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
