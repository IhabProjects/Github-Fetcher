

import sys
from utils.apiHandler import GitHubApi
from utils.eventFormatter import EventFormatter
from utils.oneLineArg import parse_args

def main():
    """Main entry point for the script."""
    args = parse_args()

    # Create API Handler
    api = GitHubApi()

    # Fetch events based on passed arguments

    if args.user:
        events = api.get_user_events(username = args.user)
        for event in events:
            print(EventFormatter.format_event(event))
    else:
        print("Error: --user is required.")
        sys.exit(1)

if __name__ == "__main__":
    main()
