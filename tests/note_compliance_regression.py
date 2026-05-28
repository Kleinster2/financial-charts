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


if __name__ == "__main__":
    unittest.main()
