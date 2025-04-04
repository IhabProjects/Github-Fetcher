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
    def get_user_profile(self, username):
        """Fetch user profile information"""
        try:
            #Fetch User Basic info:
            user_endpoint = f"{self.BASE_URL}/users/{username}"
            user_response = requests.get(user_endpoint, headers=self.headers)
            user_response.raise_for_status()
            user_data = user_response.json()

            #Fetch User Repositories:
            repos_endpoint = f"{self.BASE_URL}/users/{username}/repos"
            repos_response = requests.get(repos_endpoint, headers=self.headers)
            repos_response.raise_for_status()
            repos_data = repos_response.json()

            #Calculate additional statistics:
            languages = {}
            total_stars = 0
            total_forks = 0

            for repo in repos_data:
                total_stars += repo.get("stargazers_count", 0)
                total_forks += repo.get("forks_count", 0)
                if repo['language'] and not repo['fork']:
                    languages[repo['language']] = languages.get(repo['language'], 0) + 1

            #Sort languages by count:
            top_languages = sorted(languages.items(), key=lambda x: x[1], reverse=True)[:5]
            return {
                'profile': user_data,
                'stats': {
                    'public_repos': user_data['public_repos'],
                    'followers': user_data['followers'],
                    'following': user_data['following'],
                    'total_stars': total_stars,
                    'total_forks': total_forks,
                    'top_languages': top_languages
                }
            }
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 404:
                print(f"Error: User '{username}' not found")
            elif e.response.status_code == 403:
                print("Error: API rate limit exceeded. Try using a token.")
            else:
                print(f"HTTP Error: {e}")
            return None
        except requests.exceptions.RequestException as e:
            print(f"Request Error: {e}")
            return None
