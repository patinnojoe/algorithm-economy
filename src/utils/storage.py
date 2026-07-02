from src.config import RAW_DATA_DIR, PROCESSED_DATA_DIR


def save_raw(df, filename="youtube_raw.csv"):

    RAW_DATA_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    path = RAW_DATA_DIR / filename

    df.to_csv(path, index=False)

    print(f"Saved: {path}")


def save_processed(
    df,
    filename="youtube_clean.csv"
):

    PROCESSED_DATA_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    path = PROCESSED_DATA_DIR / filename

    df.to_csv(path, index=False)

    print(f"Saved: {path}")