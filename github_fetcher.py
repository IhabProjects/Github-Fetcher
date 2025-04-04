#!/usr/bin/env python3

import sys
import json
from utils.apiHandler import GitHubAPI
from utils.eventFormatter import EventFormatter
from utils.oneLineArg import parse_args
from utils.cli_display import (
    print_banner, print_usage, print_error,
    print_success, print_info, print_warning
)
from utils.profile_display import display_user_profile
from colorama import Fore, Style

def print_events(events, detailed=False):
    """Print events with nice formatting"""
    if not events:
        print_warning("No events found")
        return

    # Print summary header
    print(f"\n{Fore.CYAN}Found {len(events)} events{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}{'─' * 80}{Style.RESET_ALL}\n")

    # Print each event
    for i, event in enumerate(events, 1):
        print(EventFormatter.format_event(event, detailed=detailed))

        # Add separator between events
        if i < len(events):
            if detailed:
                print(f"\n{Fore.YELLOW}{'─' * 80}{Style.RESET_ALL}\n")
            else:
                print()

    # Print footer
    print(f"\n{Fore.YELLOW}{'─' * 80}{Style.RESET_ALL}")

def main():
    """Main entry point for the GitHub activity fetcher"""
    args = parse_args()

    # If no arguments provided, show banner and usage
    if len(sys.argv) == 1:
        print_banner()
        print_usage()
        sys.exit(0)

    # Create API handler
    api = GitHubAPI(token=args.token)

    # Fetch events based on provided arguments
    events = []

    try:
        if args.user:
            print_info(f"Fetching profile for user: {args.user}")

            # Fetch and display user profile
            user_data = api.get_user_profile(args.user)
            if user_data:
                display_user_profile(user_data)

            print_info(f"Fetching events for user: {args.user}")
            events = api.get_user_events(username=args.user, page=args.page, per_page=args.count)
            print_success(f"Successfully fetched {len(events)} events")
        elif args.repo:
            try:
                # Correctly split the repository string
                parts = args.repo.split('/')
                if len(parts) != 2:
                    raise ValueError("Invalid repository format")

                owner, repo = parts
                print_info(f"Fetching events for repository: {args.repo}")
                events = api.get_repo_events(owner=owner, repo=repo, page=args.page, per_page=args.count)
                print_success(f"Successfully fetched {len(events)} events")

            except ValueError:
                print_error("Repository should be in format 'owner/repo'")
                sys.exit(1)
        else:
            print_error("Either --user or --repo must be specified")
            print_usage()
            sys.exit(1)

        # Output events in requested format
        if args.json:
            print(json.dumps(events, indent=2))
        else:
            print_events(events, detailed=args.detailed)

    except KeyboardInterrupt:
        print_warning("\nOperation cancelled by user")
        sys.exit(0)
    except Exception as e:
        print_error(f"An unexpected error occurred: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
