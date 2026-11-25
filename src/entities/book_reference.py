"""Domain entity representing a book reference."""


class Reference:
    """Store the fields belonging to a book reference."""

    # Preserve the existing constructor parameter name for compatibility.
    # pylint: disable=too-few-public-methods
    def __init__(self, id, title, author, year):
        """Initialize a reference with its database fields."""
        # pylint: disable=redefined-builtin
        self.id = id
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        """Return a readable representation of the reference."""
        return f"{self.title} ({self.year}) by {self.author}"
