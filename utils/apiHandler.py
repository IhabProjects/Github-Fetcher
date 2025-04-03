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
    def get_user_events(self, username, page=1):
        """Fetch events for a specific user."""

        endpoint = f"{self.BASE_URL}/users/{username}/events"
        params = {"page": page}

        response = requests.get(endpoint, headers=self.headers, params=params)
        response.raise_for_status()
        return response.json()
    def get_repo_events(self, repo, page=1):
        """Fetch events for a specific repository."""

        endpoint = f"{self.BASE_URL}/repos/{repo}/events"
        params = {"page": page}

        response = requests.get(endpoint, headers=self.headers, params=params)
        response.raise_for_status()
        return response.json()
