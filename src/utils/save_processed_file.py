from src.config import PROCESSED_DATA_DIR

def save_processed(df, name="youtube_clean.csv"):
    df.to_csv(PROCESSED_DATA_DIR / name, index=False)
    return print(f"file saved to {PROCESSED_DATA_DIR/name}")