
import numpy as np
import pandas as pd
import ast
from src.config import CATEGORY_MAP
import re



# convert duration into actual hr, mins and seconds values
def parse_duration(duration):
    hours = minutes = seconds = 0

    match = re.match(r"PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?", duration)

    if match:
        hours = int(match.group(1)) if match.group(1) else 0
        minutes = int(match.group(2)) if match.group(2) else 0
        seconds = int(match.group(3)) if match.group(3) else 0

    return hours * 3600 + minutes * 60 + seconds







# covert []  to standard python list
def process_tags(df):
    df = df.copy()

    df["tags"] = df["tags"].apply(lambda x: ast.literal_eval(x) if isinstance(x, str) else [])
    df["tag_count"] = df["tags"].apply(len)
    df["has_tags"] = df["tag_count"] > 0

    return df


#  map category id with category name
def process_category(df):
    df = df.copy()
    df["category_name"] = df["category_id"].map(CATEGORY_MAP)
    return df




# build features
def build_features(df):
    df = df.copy()

    # logs
    df["log_views"] = np.log1p(df["views"])
    df["log_likes"] = np.log1p(df["likes"])
    df["log_comments"] = np.log1p(df["comments"])

    # rates (safe)
    df["like_rate"] = np.where(df["views"] > 0, df["likes"] / df["views"], 0)
    df["comment_rate"] = np.where(df["views"] > 0, df["comments"] / df["views"], 0)

    df["engagement_total"] = df["likes"] + df["comments"]
    df["log_engagement_total"] = np.log1p(df["engagement_total"])

    # time
    df["published_at"] = pd.to_datetime(df["published_at"])
    df["hour"] = df["published_at"].dt.hour
    df["day_of_week"] = df["published_at"].dt.dayofweek

    # duration (IMPORTANT ADDITION)
    df["duration_seconds"] = df["duration"].apply(parse_duration)
    df["duration_minutes"] = df["duration_seconds"] / 60
    df["is_short"] = (df["duration_seconds"] <= 60).astype(int)

    # virality
    threshold = df["views"].quantile(0.9)
    df["is_viral"] = (df["views"] >= threshold).astype(int)

    return df





