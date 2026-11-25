"""Robot Framework helper library for reference application setup."""

# Robot Framework imports this library by its established filename.
# pylint: disable=invalid-name

import requests


class AppLibrary:
    """Provide HTTP helpers used by the Robot Framework suites."""

    def __init__(self):
        """Initialize the application base URL."""
        self._base_url = "http://localhost:5001"

    def reset_application(self):
        """Reset the test database."""
        response = requests.get(  # pylint: disable=missing-timeout
            f"{self._base_url}/reset_db"
        )
        response.raise_for_status()

    def create_reference(self, title, author, year):
        """Create a reference through the application's form endpoint."""
        data = {
            "title": title,
            "author": author,
            "year": year,
        }

        response = requests.post(  # pylint: disable=missing-timeout
            f"{self._base_url}/create_reference", data=data
        )
        response.raise_for_status()
