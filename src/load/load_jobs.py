import pandas as pd

from src.load.db import get_engine


def load_jobs(df):

    engine = get_engine()

    existing_ids = pd.read_sql(
        "SELECT source_job_id FROM jobs",
        engine,
    )

    existing_ids = set(
        existing_ids["source_job_id"]
        .astype(str)
        .tolist()
    )

    new_df = df[
        ~df["source_job_id"]
        .astype(str)
        .isin(existing_ids)
    ]

    if new_df.empty:
        print(
            "No new records found. "
            "Skipping load."
        )
        return

    new_df.to_sql(
        name="jobs",
        con=engine,
        if_exists="append",
        index=False,
    )

    print(
        f"Loaded {len(new_df)} new rows."
    )