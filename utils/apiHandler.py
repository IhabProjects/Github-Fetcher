import requests
import sys

class GitHubAPI:
    """Handles API requests to GitHub"""

    BASE_URL = "https://api.github.com"

    def __init__(self, token=None):
        """Initialize the API handler with optional authentication token"""
        self.headers = {
            "Accept": "application/vnd.github.v3+json"
        }
        if token:
            self.headers["Authorization"] = f"token {token}"

    def get_user_events(self, username, page=1, per_page=30):
        """Fetch events for a specific user"""
        endpoint = f"{self.BASE_URL}/users/{username}/events"
        params = {"page": page, "per_page": per_page}

        try:
            response = requests.get(endpoint, headers=self.headers, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 404:
                print(f"Error: User '{username}' not found")
            elif e.response.status_code == 403:
                print("Error: API rate limit exceeded. Try using a token.")
            else:
                print(f"HTTP Error: {e}")
            sys.exit(1)
            
        except requests.exceptions.RequestException as e:
            print(f"Request Error: {e}")
            sys.exit(1)

    def get_repo_events(self, owner, repo, page=1, per_page=30):
        """Fetch events for a specific repository"""
        # Fix: Correctly format the endpoint URL
        endpoint = f"{self.BASE_URL}/repos/{owner}/{repo}/events"
        params = {"page": page, "per_page": per_page}

        try:
            response = requests.get(endpoint, headers=self.headers, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 404:
                print(f"Error: Repository '{owner}/{repo}' not found")
            elif e.response.status_code == 403:
                print("Error: API rate limit exceeded. Try using a token.")
            else:
                print(f"HTTP Error: {e}")
            sys.exit(1)
        except requests.exceptions.RequestException as e:
            print(f"Request Error: {e}")
            sys.exit(1)
