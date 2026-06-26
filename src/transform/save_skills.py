from pathlib import Path


def save_skills(df):

    processed_dir = Path("data/processed")

    processed_dir.mkdir(
        parents=True,
        exist_ok=True,
    )

    latest_file = (
        processed_dir /
        "latest_skills.csv"
    )

    df.to_csv(
        latest_file,
        index=False,
    )

    return latest_file