from src.load.db import get_engine

def load_skills(df):

    engine = get_engine()

    df.to_sql(
        "skills",
        con=engine,
        if_exists="replace",
        index=False
    )

    print(
        f"Loaded {len(df)} skills."
    )

    return len(df)