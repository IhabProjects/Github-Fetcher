

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

    events = []


    if args.user:
        events = api.get_user_events(username = args.user, page = args.page, per_page = args.count)
        for event in events:
            print(EventFormatter.format_event(event))
    elif args.repo:
        try:
            # Correctly split the repository string
            parts = args.repo.split('/')
            if len(parts) != 2:
                raise ValueError("Invalid repository format")

            owner, repo = parts
            events = api.get_repo_events(owner=owner, repo=repo, page=args.page, per_page=args.count)
        except ValueError:
            print("Error: Invalid repository format. Use 'owner/repo'.")
            sys.exit(1)
    else:
        print("Error: Either --user or --repo must be specified")
        sys.exit(1)


    if args.json:
        # Print raw JSON output if --json flag is set
        print(json.dumps(events, indent=2))
    else:
        # Print formatted output if --json flag is not set
        for event in events:
            print(EventFormatter.format_event(event))

if __name__ == "__main__":
    main()
