import requests


class AppLibrary:
    def __init__(self):
        self._base_url = "http://localhost:5001"

    def reset_application(self):
        response = requests.get(f"{self._base_url}/reset_db")
        response.raise_for_status()

    def create_reference(self, title, author, year):
        data = {
            "title": title,
            "author": author,
            "year": year,
        }

        response = requests.post(f"{self._base_url}/create_reference", data=data)
        response.raise_for_status()
