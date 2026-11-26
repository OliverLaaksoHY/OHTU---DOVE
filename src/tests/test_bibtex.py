"""Unit tests for BibTeX conversion."""

import unittest

from bibtex import citation_key, remove_bibtex, to_bibtex
from entities.book_reference import Reference


class TestBibtex(unittest.TestCase):
    """Test citation keys, escaping, and complete BibTeX entries."""

    def test_citation_key_uses_author_surname_and_year(self):
        """Build keys from regular and comma-separated author names."""
        self.assertEqual(citation_key(Reference(1, "The Hobbit", "J. R. R. Tolkien", 1937)),
                         "tolkien1937")
        self.assertEqual(citation_key(Reference(2, "Dune", "Herbert, Frank", 1965)),
                         "herbert1965")

    def test_special_characters_are_escaped(self):
        """Escape characters that have special meaning in BibTeX."""
        self.assertEqual(
            remove_bibtex(r"100% & Dune_#1"),
            r"100\% \& Dune\_\#1",
        )

    def test_formats_a_book_entry(self):
        """Format a reference as a complete BibTeX book entry."""
        reference = Reference(1, "The Hobbit", "J. R. R. Tolkien", 1937)
        expected = (
            "@book{tolkien1937,\n"
            "  title = {The Hobbit},\n"
            "  author = {J. R. R. Tolkien},\n"
            "  year = {1937}\n"
            "}\n"
        )

        self.assertEqual(to_bibtex(reference), expected)


if __name__ == "__main__":
    unittest.main()
