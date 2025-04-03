import requests

class GithubApi:
    """Handles API requests to GitHub."""

    BASE_URL = "https://api.github.com"

    def __init__(self, token = None):
        """Initialise the GithubApi class with an optional token."""
        self.headers = {
            "Accept": "application/vnd.github.v3+json",
            "Authorization": f"Bearer {token}" if token else None,
        }
