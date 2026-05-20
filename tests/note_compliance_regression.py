import unittest
from pathlib import Path
import sys
import subprocess

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


if __name__ == "__main__":
    unittest.main()
