from datetime import datetime

class EventFormatter:
    """Formats GitHub events for display"""

    EVENT_TYPES = {
        "PushEvent": "pushed to",
        "IssuesEvent": "modified issue in",
        "IssueCommentEvent": "commented on issue in",
        "PullRequestEvent": "created PR in",
        "PullRequestReviewEvent": "reviewed PR in",
        "PullRequestReviewCommentEvent": "commented on PR in",
        "CreateEvent": "created",
        "DeleteEvent": "deleted",
        "WatchEvent": "starred",
        "ForkEvent": "forked",
        "ReleaseEvent": "released in",
        "CommitCommentEvent": "commented on commit in",
        "PublicEvent": "made public",
        "MemberEvent": "updated member in",
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

        action = EventFormatter.EVENT_TYPES.get(event_type, "interacted with")

        basic_info = f"{created_at} - {actor} {action} {repo}"

        if not detailed:
            return basic_info

        # Add detailed information based on event type
        details = []

        if event_type == "PushEvent" and "payload" in event:
            payload = event["payload"]
            if "commits" in payload:
                details.append(f"  Commits: {len(payload['commits'])}")
                for commit in payload["commits"]:
                    if "message" in commit:
                        # Get first line of commit message
                        message = commit["message"].split("\n")[0]
                        details.append(f"  - {message[:60]}{'...' if len(message) > 60 else ''}")

        elif event_type == "IssuesEvent" and "payload" in event:
            payload = event["payload"]
            if "issue" in payload and "title" in payload["issue"]:
                action = payload.get("action", "unknown")
                title = payload["issue"]["title"]
                number = payload["issue"]["number"]
                details.append(f"  {action.capitalize()} issue #{number}: {title}")

        elif event_type == "PullRequestEvent" and "payload" in event:
            payload = event["payload"]
            if "pull_request" in payload and "title" in payload["pull_request"]:
                action = payload.get("action", "unknown")
                title = payload["pull_request"]["title"]
                number = payload["pull_request"]["number"]
                details.append(f"  {action.capitalize()} PR #{number}: {title}")

        if details:
            return basic_info + "\n" + "\n".join(details)
        return basic_info
