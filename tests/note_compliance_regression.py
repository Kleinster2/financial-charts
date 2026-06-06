import unittest
from pathlib import Path
import sys
import subprocess
from tempfile import TemporaryDirectory

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from scripts.check_note_compliance import NoteChecker


class MarketReactionPeerCoverageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.checker = NoteChecker(ROOT / "investing")

    def test_flags_related_public_actor_missing_from_market_reaction(self) -> None:
        content = """---
aliases: []
---
#event

## Market Reaction

| Ticker | Move |
|---|---:|
| CRWV | -3.0% |

## Related

- [[CoreWeave]]
- [[Nebius]]
"""

        issues = self.checker._check_market_reaction_peer_coverage(
            content, ROOT / "investing" / "Events" / "synthetic.md"
        )

        self.assertEqual(len(issues), 1)
        self.assertEqual(issues[0].rule, "market-reaction-peer-coverage")
        self.assertIn("[[Nebius]] (NBIS)", issues[0].message)
        self.assertNotIn("[[CoreWeave]]", issues[0].message)

    def test_accepts_related_public_actor_covered_by_ticker(self) -> None:
        content = """---
aliases: []
---
#event

## Market Reaction

NBIS fell 9.13% as the closest listed peer.

## Related

- [[Nebius]]
"""

        issues = self.checker._check_market_reaction_peer_coverage(
            content, ROOT / "investing" / "Events" / "synthetic.md"
        )

        self.assertEqual(issues, [])

    def test_macro_aliases_do_not_create_false_public_actor_warning(self) -> None:
        content = """---
aliases: []
---
#event

## Market Reaction

Rate-sensitive equities sold off.

## Related

- [[Federal Reserve]]
"""

        issues = self.checker._check_market_reaction_peer_coverage(
            content, ROOT / "investing" / "Events" / "synthetic.md"
        )

        self.assertEqual(issues, [])

    def test_market_reaction_peer_sweep_cli_is_clean(self) -> None:
        result = subprocess.run(
            [sys.executable, "scripts/check_note_compliance.py", "--market-reaction-peer-sweep"],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
        )

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("TOTAL=0", result.stdout)


class AnalystStructureTests(unittest.TestCase):
    def check_synthetic_analyst(self, content: str):
        with TemporaryDirectory(dir="C:/tmp") as tmpdir:
            vault = Path(tmpdir) / "investing"
            analysts = vault / "Analysts"
            analysts.mkdir(parents=True)
            note = analysts / "Synthetic Analyst.md"
            note.write_text(content, encoding="utf-8")

            original_cross_vaults = NoteChecker.CROSS_VAULTS
            NoteChecker.CROSS_VAULTS = {}
            try:
                checker = NoteChecker(vault)
                return checker.check_note(note)
            finally:
                NoteChecker.CROSS_VAULTS = original_cross_vaults

    def test_analyst_notes_require_aliases_tags_and_quick_stats(self) -> None:
        content = """---
---

Synthetic Analyst -- Test analyst.

## Related
"""

        issues = self.check_synthetic_analyst(content)
        errors = [issue.message for issue in issues if issue.severity == "error"]

        self.assertIn("Missing aliases in frontmatter", errors)
        self.assertIn("Analyst notes require YAML tags in frontmatter", errors)
        self.assertIn("Missing '## Quick stats' section", errors)

    def test_analyst_notes_reject_body_tags_and_actor_markers(self) -> None:
        content = """---
aliases: [Synthetic]
tags: [actor, analyst]
---
#person #analyst

Synthetic Analyst -- Test analyst.

## Quick stats

| Metric | Value |
|--------|-------|
| Role | Analyst |

## Related
"""

        issues = self.check_synthetic_analyst(content)
        errors = [issue.message for issue in issues if issue.severity == "error"]

        self.assertIn("Analyst notes should not carry the actor tag", errors)
        self.assertTrue(any("body hashtag lines" in message for message in errors))

    def test_valid_analyst_minimum_shape_is_clean(self) -> None:
        content = """---
aliases: [Synthetic]
tags: [analyst, macro]
---

Synthetic Analyst -- Test analyst.

## Quick stats

| Metric | Value |
|--------|-------|
| Role | Analyst |

## Related
"""

        issues = self.check_synthetic_analyst(content)
        errors = [issue for issue in issues if issue.severity == "error"]

        self.assertEqual(errors, [])


class SectorConceptChartTests(unittest.TestCase):
    def check_synthetic_note(self, folder: str, filename: str, content: str):
        with TemporaryDirectory(dir="C:/tmp") as tmpdir:
            vault = Path(tmpdir) / "investing"
            note_dir = vault / folder
            note_dir.mkdir(parents=True)
            note = note_dir / filename
            note.write_text(content, encoding="utf-8")

            original_cross_vaults = NoteChecker.CROSS_VAULTS
            NoteChecker.CROSS_VAULTS = {}
            try:
                checker = NoteChecker(vault)
                return checker.check_note(note)
            finally:
                NoteChecker.CROSS_VAULTS = original_cross_vaults

    def test_sector_notes_require_chart(self) -> None:
        content = """---
aliases: [Synthetic Sector]
---
#sector

# Synthetic Sector

This sector note discusses a market cohort.

## Correlation structure

Avg correlation: 0.67.

## Related
"""

        issues = self.check_synthetic_note("Sectors", "Synthetic Sector.md", content)
        errors = [issue for issue in issues if issue.severity == "error"]

        self.assertTrue(any(issue.rule == "chart" for issue in errors))

    def test_concept_notes_require_chart(self) -> None:
        content = """---
aliases: [Synthetic Concept]
---
#concept

# Synthetic Concept

This concept note discusses market structure.

## Synthesis

The causal read-through is testable.

## Related
"""

        issues = self.check_synthetic_note("Concepts", "Synthetic Concept.md", content)
        errors = [issue for issue in issues if issue.severity == "error"]

        self.assertTrue(any(issue.rule == "chart" for issue in errors))

    def test_sector_chart_satisfies_chart_gate(self) -> None:
        content = """---
aliases: [Synthetic Sector]
---
#sector

# Synthetic Sector

![[synthetic-sector-chart.png]]
*Synthetic chart caption.*

## Correlation structure

Avg correlation: 0.67.

## Related
"""

        issues = self.check_synthetic_note("Sectors", "Synthetic Sector.md", content)
        errors = [issue for issue in issues if issue.severity == "error"]

        self.assertFalse(any(issue.rule == "chart" for issue in errors))


class PrivateCapitalFounderEdgeTests(unittest.TestCase):
    def check_synthetic_actor(self, content: str):
        with TemporaryDirectory(dir="C:/tmp") as tmpdir:
            vault = Path(tmpdir) / "investing"
            actors = vault / "Actors"
            actors.mkdir(parents=True)
            note = actors / "Synthetic Capital.md"
            note.write_text(content, encoding="utf-8")

            original_cross_vaults = NoteChecker.CROSS_VAULTS
            NoteChecker.CROSS_VAULTS = {}
            try:
                checker = NoteChecker(vault)
                return checker.check_note(note)
            finally:
                NoteChecker.CROSS_VAULTS = original_cross_vaults

    def test_mature_vc_note_warns_without_founder_read(self) -> None:
        content = """---
aliases: [Synthetic]
tags: [actor, vc, private]
---

**Synthetic Capital** is a test venture firm with a global LP network.

This paragraph creates enough body material to move the note out of stub territory.
The firm uses strategic LPs, family capital, and customer introductions as its edge.

## Synopsis

The firm matters because the investor network is part of the product.

## Quick stats

| Metric | Value |
|--------|-------|
| Type | Venture capital |
| Founders | Alice Example, Bob Example |

## Strategy

Synthetic Capital invests across AI, software, and frontier technology.
The strategy section is intentionally verbose enough to satisfy the mature-note threshold.
It describes how sourcing, LP introductions, and follow-on capital become part of the product.
It adds more detail about the firm's platform, portfolio construction, and private-market access.
It adds more detail about the firm's platform, portfolio construction, and private-market access.
It adds more detail about the firm's platform, portfolio construction, and private-market access.
It adds more detail about the firm's platform, portfolio construction, and private-market access.
It adds more detail about the firm's platform, portfolio construction, and private-market access.
It adds more detail about the firm's platform, portfolio construction, and private-market access.
It adds more detail about the firm's platform, portfolio construction, and private-market access.
It adds more detail about the firm's platform, portfolio construction, and private-market access.
It adds more detail about the firm's platform, portfolio construction, and private-market access.
It adds more detail about the firm's platform, portfolio construction, and private-market access.
It adds more detail about the firm's platform, portfolio construction, and private-market access.
It adds more detail about the firm's platform, portfolio construction, and private-market access.
It adds more detail about the firm's platform, portfolio construction, and private-market access.
It adds more detail about the firm's platform, portfolio construction, and private-market access.
It adds more detail about the firm's platform, portfolio construction, and private-market access.
It adds more detail about the firm's platform, portfolio construction, and private-market access.
It adds more detail about the firm's platform, portfolio construction, and private-market access.
It adds more detail about the firm's platform, portfolio construction, and private-market access.
It adds more detail about the firm's platform, portfolio construction, and private-market access.
It adds more detail about the firm's platform, portfolio construction, and private-market access.
It adds more detail about the firm's platform, portfolio construction, and private-market access.
It adds more detail about the firm's platform, portfolio construction, and private-market access.
It adds more detail about the firm's platform, portfolio construction, and private-market access.
It adds more detail about the firm's platform, portfolio construction, and private-market access.
It adds more detail about the firm's platform, portfolio construction, and private-market access.
It adds more detail about the firm's platform, portfolio construction, and private-market access.
It adds more detail about the firm's platform, portfolio construction, and private-market access.
It adds more detail about the firm's platform, portfolio construction, and private-market access.
It adds more detail about the firm's platform, portfolio construction, and private-market access.

## Related
"""

        issues = self.check_synthetic_actor(content)

        self.assertTrue(any(issue.rule == "founder-edge" for issue in issues))

    def test_founder_read_satisfies_private_capital_gate(self) -> None:
        content = """---
aliases: [Synthetic]
tags: [actor, vc, private]
---

**Synthetic Capital** is a test venture firm with a global LP network.

This paragraph creates enough body material to move the note out of stub territory.
The firm uses strategic LPs, family capital, and customer introductions as its edge.

## Synopsis

The firm matters because the investor network is part of the product.

## Quick stats

| Metric | Value |
|--------|-------|
| Type | Venture capital |

## Founder read

Alice Example supplies the source-of-capital edge and Bob Example supplies sector access.
Third-party profile context explains why the founders had access before the firm scaled.

## Strategy

Synthetic Capital invests across AI, software, and frontier technology.
The strategy section is intentionally verbose enough to satisfy the mature-note threshold.
It describes how sourcing, LP introductions, and follow-on capital become part of the product.
It adds more detail about the firm's platform, portfolio construction, and private-market access.
It adds more detail about the firm's platform, portfolio construction, and private-market access.
It adds more detail about the firm's platform, portfolio construction, and private-market access.
It adds more detail about the firm's platform, portfolio construction, and private-market access.
It adds more detail about the firm's platform, portfolio construction, and private-market access.
It adds more detail about the firm's platform, portfolio construction, and private-market access.
It adds more detail about the firm's platform, portfolio construction, and private-market access.
It adds more detail about the firm's platform, portfolio construction, and private-market access.
It adds more detail about the firm's platform, portfolio construction, and private-market access.
It adds more detail about the firm's platform, portfolio construction, and private-market access.
It adds more detail about the firm's platform, portfolio construction, and private-market access.
It adds more detail about the firm's platform, portfolio construction, and private-market access.
It adds more detail about the firm's platform, portfolio construction, and private-market access.
It adds more detail about the firm's platform, portfolio construction, and private-market access.
It adds more detail about the firm's platform, portfolio construction, and private-market access.
It adds more detail about the firm's platform, portfolio construction, and private-market access.
It adds more detail about the firm's platform, portfolio construction, and private-market access.
It adds more detail about the firm's platform, portfolio construction, and private-market access.
It adds more detail about the firm's platform, portfolio construction, and private-market access.
It adds more detail about the firm's platform, portfolio construction, and private-market access.
It adds more detail about the firm's platform, portfolio construction, and private-market access.
It adds more detail about the firm's platform, portfolio construction, and private-market access.
It adds more detail about the firm's platform, portfolio construction, and private-market access.
It adds more detail about the firm's platform, portfolio construction, and private-market access.
It adds more detail about the firm's platform, portfolio construction, and private-market access.
It adds more detail about the firm's platform, portfolio construction, and private-market access.
It adds more detail about the firm's platform, portfolio construction, and private-market access.
It adds more detail about the firm's platform, portfolio construction, and private-market access.

## Related
"""

        issues = self.check_synthetic_actor(content)

        self.assertFalse(any(issue.rule == "founder-edge" for issue in issues))


if __name__ == "__main__":
    unittest.main()
