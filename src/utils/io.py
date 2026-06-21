import pandas as pd
from src.config import RAW_DATA_DIR, PROCESSED_DATA_DIR
from pathlib import Path
import datetime


def _timestamp():
    return datetime.datetime.now().strftime("%Y%m%d_%H%M%S")


# def save_raw(df: pd.DataFrame, name="youtube_raw"):
#     RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)

#     path = RAW_DATA_DIR / f"{name}_{_timestamp()}.csv"
#     df.to_csv(path, index=False)

#     print(f"[RAW SAVED] {path}")


# def save_processed(df: pd.DataFrame, name="youtube_processed"):
#     PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)

#     path = PROCESSED_DATA_DIR / f"{name}_{_timestamp()}.csv"
#     df.to_csv(path, index=False)

#     print(f"[PROCESSED SAVED] {path}")


# def load_data(path):
#     return pd.read_csv(path)


def append_raw(df, name="youtube_raw"):
    path = RAW_DATA_DIR / f"{name}.csv"

    if path.exists():
        old = pd.read_csv(path)
        before = len(old)

        combined = pd.concat([old, df], ignore_index=True)
        combined = combined.drop_duplicates(subset=["video_id"])

        after = len(combined)

        combined.to_csv(path, index=False)

        print(f"[APPENDED] +{after - before} new unique rows | Total: {after}")

    else:
        df = df.drop_duplicates(subset=["video_id"])
        df.to_csv(path, index=False)
        print(f"[CREATED] {len(df)} rows")