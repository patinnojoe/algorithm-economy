"""
parser.py

Utilities for converting raw YouTube API responses
into a standardized dataset.

Author:
Innocent Josiah Patrick
"""

from datetime import datetime


# --------------------------------------------------
# Helpers
# --------------------------------------------------

def safe_int(value):
    """Safely convert values to integers."""
    try:
        return int(value)
    except (TypeError, ValueError):
        return 0


# --------------------------------------------------
# Video Parser
# --------------------------------------------------

def parse_video(item, discovery_source):
    """
    Convert a raw YouTube API response into a
    standardized discovery record.
    """

    snippet = item.get("snippet", {})
    stats = item.get("statistics", {})
    content = item.get("contentDetails", {})

    views = safe_int(stats.get("viewCount"))
    likes = safe_int(stats.get("likeCount"))
    comments = safe_int(stats.get("commentCount"))

    engagement_rate = (
        (likes + comments) / views
        if views > 0
        else 0
    )

    return {

        # --------------------------------------------------
        # Video Identity
        # --------------------------------------------------

        "video_id": item.get("id"),

        # --------------------------------------------------
        # Video Metadata
        # --------------------------------------------------

        "title": snippet.get("title"),

        "description": snippet.get("description"),

        "published_at": snippet.get("publishedAt"),

        "category_id": snippet.get("categoryId"),

        "tags": snippet.get("tags", []),

        "duration": content.get("duration"),

        # --------------------------------------------------
        # Channel Metadata
        # --------------------------------------------------

        "channel_id": snippet.get("channelId"),

        "channel_title": snippet.get("channelTitle"),

        # --------------------------------------------------
        # Video Statistics
        # --------------------------------------------------

        "views": views,

        "likes": likes,

        "comments": comments,

        "engagement_rate": engagement_rate,

        # --------------------------------------------------
        # Discovery Metadata
        # --------------------------------------------------

        "discovery_source": discovery_source,

        "collection_method": item.get("collection_method"),

        "collection_query": item.get("collection_query"),

        "collection_region": item.get("collection_region"),

        "collection_timestamp": item.get("collection_timestamp"),

        # --------------------------------------------------
        # Processing Metadata
        # --------------------------------------------------

        "collected_at": datetime.utcnow().isoformat()

    }