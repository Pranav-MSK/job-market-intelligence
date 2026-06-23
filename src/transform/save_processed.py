from pathlib import Path
from datetime import datetime


def save_processed(df):

    Path(
        "data/processed"
    ).mkdir(
        parents=True,
        exist_ok=True,
    )

    timestamp = (
        datetime.now()
        .strftime("%Y%m%d_%H%M%S")
    )

    filename = (
        f"data/processed/"
        f"jobs_clean_{timestamp}.csv"
    )

    df.to_csv(
        filename,
        index=False,
    )

    return filename