from pathlib import Path
import hashlib

import pandas as pd
from pandas.errors import EmptyDataError


def create_job_hash(df):
    """
    Create a stable fingerprint for every job.
    Adzuna frequently changes job IDs, so we don't rely on them.
    """

    cols = (
        df["title"].fillna("").str.lower().str.strip()
        + "|"
        + df["company"].fillna("").str.lower().str.strip()
        + "|"
        + df["city"].fillna("").str.lower().str.strip()
        + "|"
        + df["description"]
        .fillna("")
        .str[:500]                 # first 500 chars are enough
        .str.lower()
        .str.replace(r"\s+", " ", regex=True)
        .str.strip()
    )

    return cols.apply(
        lambda x: hashlib.md5(
            x.encode("utf-8")
        ).hexdigest()
    )


def save_processed(df):

    output_dir = Path("data/processed")
    output_dir.mkdir(
        parents=True,
        exist_ok=True,
    )

    csv_path = output_dir / "latest_jobs.csv"

    # ----------------------------------------
    # Create fingerprint for incoming jobs
    # ----------------------------------------
    df = df.copy()

    df["job_hash"] = create_job_hash(df)

    # Remove duplicates within same crawl
    df = (
        df.sort_values("created_at")
        .drop_duplicates(
            subset="job_hash",
            keep="last",
        )
        .reset_index(drop=True)
    )

    print("\nIncoming")
    print(len(df), "rows")

    # ----------------------------------------
    # First run
    # ----------------------------------------
    if not csv_path.exists():

        df.to_csv(
            csv_path,
            index=False,
        )

        return csv_path

    # ----------------------------------------
    # Load existing data
    # ----------------------------------------
    try:

        existing = pd.read_csv(
            csv_path,
            parse_dates=["created_at"],
        )

    except EmptyDataError:

        existing = pd.DataFrame(columns=df.columns)

    if len(existing):

        if "job_hash" not in existing.columns:

            existing["job_hash"] = create_job_hash(
                existing
            )

    print("Existing")
    print(len(existing), "rows")

    # ----------------------------------------
    # Merge
    # ----------------------------------------
    combined = pd.concat(
        [existing, df],
        ignore_index=True,
    )

    print("Merged")
    print(len(combined), "rows")

    # ----------------------------------------
    # Remove duplicates
    # ----------------------------------------
    combined = (
        combined.sort_values("created_at")
        .drop_duplicates(
            subset="job_hash",
            keep="last",
        )
        .reset_index(drop=True)
    )

    print("After dedup")
    print(len(combined), "rows")

    # ----------------------------------------
    # Keep latest version if source_id repeats
    # ----------------------------------------
    combined = (
        combined.sort_values("created_at")
        .drop_duplicates(
            subset="source_job_id",
            keep="last",
        )
        .reset_index(drop=True)
    )

    # ----------------------------------------
    # Optional: remove helper column
    # ----------------------------------------
    combined.drop(
        columns=["job_hash"],
        inplace=True,
        errors="ignore",
    )

    combined.to_csv(
        csv_path,
        index=False,
    )

    return csv_path