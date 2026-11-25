"""Validation helpers for reference form input."""

import re


class UserInputError(Exception):
    """Raised when user-provided reference data is invalid."""


def validate_text_entries(entries: list):
    """Validate that text fields are non-empty and no longer than 50 characters."""
    # entries is a list of tuples where each tuple is (variable_name, variable_value)
    for entry_name, entry_value in entries:
        if not entry_value:
            raise UserInputError(f"{entry_name} must be at least 1 letter")
        if len(entry_value) > 50:
            raise UserInputError(f"{entry_name} must be under 50 characters long")


def validate_year_entry(year):
    """Validate that a year is a four-digit value between 1000 and 2999."""
    if not re.search("^[1-2][0-9]{3}$", year):
        raise UserInputError("Year must be an integer between 1000 and 2999")
