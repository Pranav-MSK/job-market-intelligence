from pathlib import Path


def save_processed(df):
    Path("data/processed").mkdir(
        parents=True,
        exist_ok=True,
    )

    filename = "data/processed/jobs_clean.csv"

    df.to_csv(
        filename,
        index=False,
    )

    return filename