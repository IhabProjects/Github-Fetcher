from datetime import datetime

class EventFormatter:
    """Formats event data for display."""

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

        return f"{created_at} - {actor} performed {event_type} on {repo}"
