"""Robot Framework helper library for reference application setup."""

# Robot Framework imports this library by its established filename.

import requests


class AppLibrary:
    """Provide HTTP helpers used by the Robot Framework suites."""

    def __init__(self):
        """Initialize the application base URL."""
        self._base_url = "http://localhost:5001"

    def reset_application(self):
        """Reset the test database."""
        response = requests.get(
            f"{self._base_url}/reset_db",
            timeout=10,
        )
        response.raise_for_status()

    def create_reference(self, title, author, year):
        """Create a reference through the application's form endpoint."""
        data = {
            "title": title,
            "author": author,
            "year": year,
        }

        response = requests.post(
            f"{self._base_url}/create_reference",
            data=data,
            timeout=10,
        )
        response.raise_for_status()
