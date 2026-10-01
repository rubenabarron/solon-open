"""Tests for the mechanical gate. Run from the repository root:

    python -m unittest discover -s scripts -p "test_*.py"
"""

from __future__ import annotations

import pathlib
import sys
import tempfile
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import gate  # noqa: E402


class GateTests(unittest.TestCase):
    def _check(self, text: str) -> list[str]:
        with tempfile.TemporaryDirectory() as tmp:
            path = pathlib.Path(tmp) / "sample.md"
            path.write_text(text, encoding="utf-8")
            return gate.check_file(path)

    def test_clean_text_passes(self) -> None:
        self.assertEqual(self._check("Solon turns overrides into policy.\n"), [])

    def test_em_dash_fails(self) -> None:
        problems = self._check("a \u2014 b\n")
        self.assertTrue(any("em dash" in p for p in problems))

    def test_double_hyphen_punctuation_fails(self) -> None:
        problems = self._check("a -- b\n")
        self.assertTrue(any("double-hyphen" in p for p in problems))

    def test_cli_flags_and_table_separators_pass(self) -> None:
        self.assertEqual(self._check("gh repo create x --public\n"), [])
        self.assertEqual(self._check("|---|---|\n"), [])

    def test_banned_strings_fail(self) -> None:
        company_style = "Solon" + "AI" + " Corp\n"
        bare_phrase = "we are Solon " + "AI\n"
        self.assertTrue(any("banned string" in p for p in self._check(company_style)))
        self.assertTrue(any("banned string" in p for p in self._check(bare_phrase)))

    def test_secret_patterns_fail(self) -> None:
        token = "ghp_" + "a" * 24 + "\n"
        self.assertTrue(any("secret-like" in p for p in self._check(token)))


if __name__ == "__main__":
    unittest.main()
