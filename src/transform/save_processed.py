from pathlib import Path
import pandas as pd


def save_processed(df):

    processed_dir = Path("data/processed")

    processed_dir.mkdir(
        parents=True,
        exist_ok=True,
    )

    latest_file = (
        processed_dir /
        "latest_jobs.csv"
    )

    if latest_file.exists():

        existing = pd.read_csv(
            latest_file
        )

        df = pd.concat(
            [existing, df],
            ignore_index=True,
        )

        df.drop_duplicates(
            subset="source_job_id",
            inplace=True,
        )

    df.to_csv(
        latest_file,
        index=False,
    )

    return latest_file