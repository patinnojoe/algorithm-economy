def extract_video_ids(items):
    """
    Extract video IDs from Search API results.
    """

    ids = []

    for item in items:

        try:
            ids.append(item["id"]["videoId"])

        except KeyError:
            continue

    return ids