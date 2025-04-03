#!/usr/bin/env python3

import sys
import json
from utils.apiHandler import GitHubAPI
from utils.eventFormatter import EventFormatter
from utils.oneLineArg import parse_args

def main():
    """Main entry point for the GitHub activity fetcher"""
    args = parse_args()

    # Create API handler
    api = GitHubAPI(token=args.token)

    # Fetch events based on provided arguments
    events = []

    if args.user:
        events = api.get_user_events(username=args.user, page=args.page, per_page=args.count)
    elif args.repo:
        try:
            # Correctly split the repository string
            parts = args.repo.split('/')
            if len(parts) != 2:
                raise ValueError("Invalid repository format")

            owner, repo = parts
            events = api.get_repo_events(owner=owner, repo=repo, page=args.page, per_page=args.count)
        except ValueError:
            print("Error: Repository should be in format 'owner/repo'")
            sys.exit(1)
    else:
        print("Error: Either --user or --repo must be specified")
        sys.exit(1)

    # Output events in requested format
    if args.json:
        print(json.dumps(events, indent=2))
    else:
        for event in events:
            print(EventFormatter.format_event(event, detailed=args.detailed))
            # Add a separator between detailed events for better readability
            if args.detailed:
                print("-" * 40)

if __name__ == "__main__":
    main()
