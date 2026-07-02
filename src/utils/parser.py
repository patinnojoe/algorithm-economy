"""
parser.py

Utilities for converting raw YouTube API responses
into a standardized dataset.
"""

from datetime import datetime


def safe_int(value):
    """Safely convert values to integers."""
    try:
        return int(value)
    except (TypeError, ValueError):
        return 0


def parse_video(item, source):
    """
    Parse a raw YouTube video object into
    a standardized dictionary.
    """

    snippet = item.get("snippet", {})
    stats = item.get("statistics", {})
    content = item.get("contentDetails", {})

    views = safe_int(stats.get("viewCount"))
    likes = safe_int(stats.get("likeCount"))
    comments = safe_int(stats.get("commentCount"))

    engagement_rate = (
        (likes + comments) / views
        if views > 0 else 0
    )

    return {

        "video_id": item.get("id"),

        "title": snippet.get("title"),
        "description": snippet.get("description"),

        "channel_id": snippet.get("channelId"),
        "channel_title": snippet.get("channelTitle"),

        "published_at": snippet.get("publishedAt"),

        "category_id": snippet.get("categoryId"),
        "tags": snippet.get("tags", []),

        "views": views,
        "likes": likes,
        "comments": comments,

        "engagement_rate": engagement_rate,

        "duration": content.get("duration"),

        "source": source,

        "collected_at": datetime.utcnow().isoformat()
    }