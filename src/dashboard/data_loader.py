import pandas as pd

from src.load.db import get_engine


def get_top_companies():
    query = """
    SELECT
        company,
        COUNT(*) AS total_jobs
    FROM jobs
    GROUP BY company
    ORDER BY total_jobs DESC
    LIMIT 10
    """

    engine = get_engine()

    return pd.read_sql(query, engine)


def get_top_cities():
    query = """
    SELECT
        city,
        COUNT(*) AS total_jobs
    FROM jobs
    WHERE city IS NOT NULL
    GROUP BY city
    ORDER BY total_jobs DESC, city ASC
    LIMIT 10
    """

    engine = get_engine()

    return pd.read_sql(query, engine)


def get_jobs_by_day():
    query = """
    SELECT
        DATE(created_at) AS posting_date,
        COUNT(*) AS total_jobs
    FROM jobs
    GROUP BY posting_date
    ORDER BY posting_date
    """

    engine = get_engine()

    return pd.read_sql(query, engine)