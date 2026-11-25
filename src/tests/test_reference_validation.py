"""Unit tests for reference form validation."""

import unittest

from utils import UserInputError, validate_text_entries, validate_year_entry


class TestReferenceValidation(unittest.TestCase):
    """Verify valid and invalid reference field values."""

    def test_rejects_empty_author_when_title_is_valid(self):
        """Reject an empty author even when the title is valid."""
        with self.assertRaises(UserInputError):
            validate_text_entries([("title", "The Hobbit"), ("author", "")])

    def test_rejects_years_outside_allowed_range(self):
        """Reject years outside the accepted range."""
        for year in ("999", "3000"):
            with self.subTest(year=year):
                with self.assertRaises(UserInputError):
                    validate_year_entry(year)

    def test_accepts_boundary_years(self):
        """Accept both boundary years."""
        for year in ("1000", "2999"):
            with self.subTest(year=year):
                validate_year_entry(year)
