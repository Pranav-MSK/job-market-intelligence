import pandas as pd

from src.load.db import get_engine

def run_query(sql_file):
    with open(sql_file, "r") as f:
        query = f.read()

    engine = get_engine()

    return pd.read_sql(query, engine)