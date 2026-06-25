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

def get_total_jobs():
    query = """
    SELECT COUNT(*) AS total_jobs
    FROM jobs
    """

    return pd.read_sql(
        query,
        get_engine()
    ).iloc[0]["total_jobs"]

def get_total_cities():
    query = """
    SELECT COUNT(DISTINCT city) AS total_cities
    FROM jobs
    WHERE city IS NOT NULL
    """

    return pd.read_sql(
        query,
        get_engine()
    ).iloc[0]["total_cities"]

def get_total_companies():
    query = """
    SELECT COUNT(DISTINCT company)
    AS total_companies
    FROM jobs
    """

    return pd.read_sql(
        query,
        get_engine()
    ).iloc[0]["total_companies"]

def get_latest_posting():
    query = """
    SELECT MAX(created_at)
    AS latest_posting
    FROM jobs
    """

    return pd.read_sql(
        query,
        get_engine()
    ).iloc[0]["latest_posting"]

def get_average_jobs_per_day():
    query = """
    SELECT
        ROUND(COUNT(*) / COUNT(DISTINCT DATE(created_at)), 2)
        AS avg_jobs_per_day
    FROM jobs
    """

    engine = get_engine()

    return pd.read_sql(query, engine)

def get_recent_jobs():
    query = """
    SELECT
        title,
        company,
        city,
        DATE(created_at) AS posted_date
    FROM jobs
    ORDER BY created_at DESC
    LIMIT 10
    """

    engine = get_engine()

    return pd.read_sql(query, engine)

def get_data_quality_metrics():
    query = """
    SELECT
        COUNT(*) AS total_jobs,
        SUM(city IS NULL) AS missing_city,
        SUM(state IS NULL) AS missing_state,
        COUNT(DISTINCT source_job_id) AS unique_jobs
    FROM jobs
    """

    engine = get_engine()

    return pd.read_sql(query, engine)