"""
base.py

Shared utilities for interacting with the YouTube Data API v3.

Responsibilities
----------------
- Create authenticated YouTube client
- Safe API requests with retries
- Automatic pagination
- Batch retrieval of full video metadata

Author:
Innocent Josiah Patrick
"""

import os
import time
import logging
from dotenv import load_dotenv
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


# --------------------------------------------------
# Environment
# --------------------------------------------------

load_dotenv()

API_KEY = os.getenv("YOUTUBE_API_KEY")

if API_KEY is None:
    raise ValueError(
        "YOUTUBE_API_KEY not found in environment variables."
    )


# --------------------------------------------------
# Logging
# --------------------------------------------------

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)


# --------------------------------------------------
# Build client
# --------------------------------------------------

youtube = build(
    serviceName="youtube",
    version="v3",
    developerKey=API_KEY,
    cache_discovery=False
)


# --------------------------------------------------
# Safe Request
# --------------------------------------------------

def safe_request(
    request,
    retries=5,
    backoff=2
):
    """
    Execute an API request with exponential backoff.

    Parameters
    ----------
    request
        Google API request object

    retries : int

    backoff : int

    Returns
    -------
    dict | None
    """

    for attempt in range(retries):

        try:
            return request.execute()

        except HttpError as e:

            logger.warning(
                f"HTTP Error (Attempt {attempt+1}/{retries}) "
                f"{e.resp.status}"
            )

        except Exception as e:

            logger.warning(
                f"Request Failed (Attempt {attempt+1}/{retries}) "
                f"{e}"
            )

        sleep_time = backoff ** attempt
        time.sleep(sleep_time)

    logger.error("Maximum retries exceeded.")

    return None


# --------------------------------------------------
# Pagination
# --------------------------------------------------

def paginate(
    request,
    limit=None
):
    """
    Iterate through every page returned by
    a YouTube API request.

    Parameters
    ----------
    request

    limit : int | None

    Yields
    ------
    list
        items from each page
    """

    total = 0

    while request:

        response = safe_request(request)

        if response is None:
            break

        items = response.get("items", [])

        yield items

        total += len(items)

        logger.info(f"Collected {total:,} records")

        if limit is not None and total >= limit:
            break

        request = youtube.search().list_next(
            request,
            response
        )


# --------------------------------------------------
# Fetch full video metadata
# --------------------------------------------------

def fetch_video_details(
    video_ids,
    batch_size=50
):
    """
    Fetch complete metadata for a list of videos.

    Parameters
    ----------
    video_ids : list[str]

    batch_size : int

    Returns
    -------
    list
    """

    videos = []

    for i in range(
        0,
        len(video_ids),
        batch_size
    ):

        batch = video_ids[i:i + batch_size]

        request = youtube.videos().list(
            part="snippet,statistics,contentDetails",
            id=",".join(batch)
        )

        response = safe_request(request)

        if response:

            videos.extend(
                response.get("items", [])
            )

    logger.info(
        f"Retrieved metadata for {len(videos):,} videos."
    )

    return videos


# --------------------------------------------------
# Helper
# --------------------------------------------------

def extract_video_ids(items):
    """
    Extract video ids from search results.

    Parameters
    ----------
    items : list

    Returns
    -------
    list[str]
    """

    ids = []

    for item in items:

        video = item.get("id")

        if isinstance(video, dict):

            video_id = video.get("videoId")

            if video_id:
                ids.append(video_id)

    return ids