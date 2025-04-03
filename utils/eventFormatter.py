from datetime import datetime

class EventFormatter:
    """Formats event data for display."""

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
        """Formats GitHub time string to human-readable format"""
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
        elif event_type == "ForkEvent":
            action = f"{action} {repo}"
        elif event_type == "ReleaseEvent":
            action = f"{action} {event['payload']['release']['tag_name']}"
        elif event_type == "CommitCommentEvent":
            action = f"{action} commit {event['payload']['comment']['commit_id']}"
        elif event_type == "PublicEvent":
            action = f"{action} {repo}"
        elif event_type == "MemberEvent":
            action = f"{action} {event['payload']['member']['login']}"
        elif event_type == "DeleteEvent":
            action = f"{action} {event['payload']['ref_type']} {event['payload']['ref']}"
        elif event_type == "CreateEvent":
            action = f"{action} {event['payload']['ref_type']} {event['payload']['ref']}"
        elif event_type == "PullRequestReviewEvent":
            action = f"{action} pull request #{event['payload']['pull_request']['number']}"
        elif event_type == "PullRequestReviewCommentEvent":
            action = f"{action} pull request #{event['payload']['pull_request']['number']}"
        return f"{created_at} - {actor} {action} {repo}"
