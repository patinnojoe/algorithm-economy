from collectors.trending import get_trending_videos
from collectors.recent import get_recent_videos
from collectors.search import get_search_videos
from collectors.channels import get_channel_videos

from src.utils.youtube_parser import parse_video
from src.utils.io import save_raw

from src.config import (
    TRENDING_LIMIT,
    RECENT_LIMIT,
    SEARCH_LIMIT,
    CHANNEL_LIMIT
)

import pandas as pd


def build_dataset():
    dataset = []

    print("Fetching trending videos...")
    trending = get_trending_videos(TRENDING_LIMIT)
    dataset += [parse_video(v, "trending") for v in trending]

    print("Fetching recent videos...")
    recent = get_recent_videos(RECENT_LIMIT)
    dataset += [parse_video(v, "recent") for v in recent]

    print("Fetching search videos...")
    search = get_search_videos(SEARCH_LIMIT)
    dataset += [parse_video(v, "search") for v in search]

    print("Fetching channel videos...")
    channel_ids = [
        "UCX6OQ3DkcsbYNE6H8uQQuVA"  # replace later
    ]

    for ch in channel_ids:
        channel_videos = get_channel_videos(ch, CHANNEL_LIMIT)
        dataset += [parse_video(v, "channel") for v in channel_videos]

    df = pd.DataFrame(dataset)

    save_raw(df)

    print(f"Dataset built: {len(df)} videos")

    return df


if __name__ == "__main__":
    build_dataset()