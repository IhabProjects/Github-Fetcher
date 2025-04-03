

import sys
from utils.apiHandler import GitHubAPI
from utils.eventFormatter import EventFormatter
from utils.oneLineArg import parse_args

def main():
    """Main entry point for the script."""
    args = parse_args()

    # Create API Handler
    api = GitHubAPI()

    # Fetch events based on passed arguments

    if args.user:
        events = api.get_user_events(username = args.user)
        for event in events:
            print(EventFormatter.format_event(event))
    elif args.repo:
        try:
            owner, repo = args.repo.split("/")
            events = api.get_repo_events(owner, repo)
            for event in events:
                print(EventFormatter.format_event(event))
        except ValueError:
            print("Error: Invalid repository format. Use 'owner/repo'.")
            sys.exit(1)
    else:
        print("Error: --user is required.")
        sys.exit(1)

if __name__ == "__main__":
    main()
