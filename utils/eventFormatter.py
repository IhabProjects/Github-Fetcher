from datetime import datetime

class EventFormatter:
    """Formats event data for display."""

    EVENTS_TYPES = {
        "PushEvent": "pushed to",
        "IssuesEvent": "modified issue in",
        "PullRequestEvent": "opened a pull request in",
        "IssueCommentEvent": "commented on an issue in",
        "WatchEvent": "starred",
        "ForkEvent": "forked",
    }



    @staticmethod
    def format_time(time_str):
        """Formats the current time."""
        dt = datetime.strptime(time_str, "%Y-%m-%dT%H:%M:%SZ")
        return dt.strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def format_event(event):
        """Formats a single event."""
        event_type = event["type"]
        actor = event["actor"]["login"]
        repo = event["repo"]["name"]
        created_at = EventFormatter.format_time(event["created_at"])

        action = EventFormatter.EVENTS_TYPES.get(event_type, "Interacted with")
        if event_type == "PushEvent":
            action = f"{action} {event['payload']['size']} commits"
        elif event_type == "IssuesEvent":
            action = f"{action} issue #{event['payload']['issue']['number']}"
        elif event_type == "PullRequestEvent":
            action = f"{action} pull request #{event['payload']['pull_request']['number']}"
        elif event_type == "IssueCommentEvent":
            action = f"{action} issue #{event['payload']['issue']['number']}"
        elif event_type == "WatchEvent":
            action = f"{action} {repo}"

        return f"{created_at} - {actor} performed {event_type} on {repo}"
