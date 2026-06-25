from src.load.db import get_engine


def load_jobs(df):

    engine = get_engine()

    df.to_sql(
        name="jobs",
        con=engine,
        if_exists="append",
        index=False,
    )

    print(
        f"Loaded {len(df)} rows into jobs table."
    )