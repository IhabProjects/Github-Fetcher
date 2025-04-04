from datetime import datetime
from colorama import Fore, Style

class EventFormatter:
    """Formats GitHub events for display"""

    EVENT_TYPES = {
        "PushEvent": {
            "icon": "🔨",
            "color": Fore.GREEN,
            "action": "pushed to"
        },
        "IssuesEvent": {
            "icon": "⚡",
            "color": Fore.MAGENTA,
            "action": "modified issue in"
        },
        "IssueCommentEvent": {
            "icon": "💭",
            "color": Fore.BLUE,
            "action": "commented on issue in"
        },
        "PullRequestEvent": {
            "icon": "🔀",
            "color": Fore.CYAN,
            "action": "created PR in"
        },
        "PullRequestReviewEvent": {
            "icon": "👀",
            "color": Fore.YELLOW,
            "action": "reviewed PR in"
        },
        "PullRequestReviewCommentEvent": {
            "icon": "💬",
            "color": Fore.BLUE,
            "action": "commented on PR in"
        },
        "CreateEvent": {
            "icon": "✨",
            "color": Fore.GREEN,
            "action": "created"
        },
        "DeleteEvent": {
            "icon": "🗑️",
            "color": Fore.RED,
            "action": "deleted"
        },
        "WatchEvent": {
            "icon": "⭐",
            "color": Fore.YELLOW,
            "action": "starred"
        },
        "ForkEvent": {
            "icon": "🍴",
            "color": Fore.CYAN,
            "action": "forked"
        },
        "ReleaseEvent": {
            "icon": "📦",
            "color": Fore.GREEN,
            "action": "released in"
        },
        "CommitCommentEvent": {
            "icon": "💡",
            "color": Fore.BLUE,
            "action": "commented on commit in"
        },
        "PublicEvent": {
            "icon": "🌍",
            "color": Fore.GREEN,
            "action": "made public"
        },
        "MemberEvent": {
            "icon": "👥",
            "color": Fore.MAGENTA,
            "action": "updated member in"
        }
    }

    @staticmethod
    def format_time(time_str):
        """Format the GitHub time string to human-readable format"""
        dt = datetime.strptime(time_str, "%Y-%m-%dT%H:%M:%SZ")
        return dt.strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def format_event(event, detailed=False):
        """Format a single GitHub event as a string"""
        event_type = event["type"]
        actor = event["actor"]["login"]
        repo = event["repo"]["name"]
        created_at = EventFormatter.format_time(event["created_at"])

        # Get event type info with defaults
        event_info = EventFormatter.EVENT_TYPES.get(event_type, {
            "icon": "❔",
            "color": Fore.WHITE,
            "action": "interacted with"
        })

        # Format the basic event line
        basic_info = (
            f"{Fore.WHITE}[{created_at}] "
            f"{event_info['icon']} "
            f"{event_info['color']}{actor}{Fore.WHITE} "
            f"{event_info['action']} "
            f"{Fore.YELLOW}{repo}{Style.RESET_ALL}"
        )

        if not detailed:
            return basic_info

        # Add detailed information based on event type
        details = []

        if event_type == "PushEvent" and "payload" in event:
            payload = event["payload"]
            if "commits" in payload:
                details.append(f"\n  {Fore.CYAN}Commits: {len(payload['commits'])}{Style.RESET_ALL}")
                for commit in payload["commits"]:
                    if "message" in commit:
                        # Get first line of commit message
                        message = commit["message"].split("\n")[0]
                        details.append(
                            f"  {Fore.GREEN}➜{Style.RESET_ALL} {message[:60]}"
                            f"{'...' if len(message) > 60 else ''}"
                        )

        elif event_type == "IssuesEvent" and "payload" in event:
            payload = event["payload"]
            if "issue" in payload and "title" in payload["issue"]:
                action = payload.get("action", "unknown")
                title = payload["issue"]["title"]
                number = payload["issue"]["number"]
                details.append(
                    f"\n  {Fore.MAGENTA}#{number}{Style.RESET_ALL} "
                    f"{action.capitalize()}: {title}"
                )

        elif event_type == "PullRequestEvent" and "payload" in event:
            payload = event["payload"]
            if "pull_request" in payload and "title" in payload["pull_request"]:
                action = payload.get("action", "unknown")
                title = payload["pull_request"]["title"]
                number = payload["pull_request"]["number"]
                details.append(
                    f"\n  {Fore.CYAN}PR #{number}{Style.RESET_ALL} "
                    f"{action.capitalize()}: {title}"
                )

                # Add PR statistics if available
                pr = payload["pull_request"]
                stats = (
                    f"\n  {Fore.GREEN}+{pr.get('additions', 0)}{Style.RESET_ALL} "
                    f"{Fore.RED}-{pr.get('deletions', 0)}{Style.RESET_ALL} "
                    f"({pr.get('changed_files', 0)} files)"
                )
                details.append(stats)

        if details:
            return basic_info + "\n" + "\n".join(details)
        return basic_info
