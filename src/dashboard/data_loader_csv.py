import pandas as pd

JOBS_FILE = "data/processed/latest_jobs.csv"
SKILLS_FILE = "data/processed/latest_skills.csv"


def load_jobs():
    return pd.read_csv(
        JOBS_FILE,
        parse_dates=["created_at"]
    )


def load_skills():
    return pd.read_csv(
        SKILLS_FILE
    )


def get_top_companies():
    df = load_jobs()

    return (
        df.groupby("company")
        .size()
        .reset_index(name="total_jobs")
        .sort_values(
            "total_jobs",
            ascending=False
        )
        .head(10)
    )


def get_top_cities():
    df = load_jobs()

    return (
        df.dropna(subset=["city"])
        .groupby("city")
        .size()
        .reset_index(name="total_jobs")
        .sort_values(
            ["total_jobs", "city"],
            ascending=[False, True]
        )
        .head(10)
    )


def get_jobs_by_day():
    df = load_jobs()

    df["posting_date"] = (
        df["created_at"]
        .dt.date
    )

    return (
        df.groupby("posting_date")
        .size()
        .reset_index(name="total_jobs")
    )


def get_total_jobs():
    return len(load_jobs())


def get_total_cities():
    return (
        load_jobs()["city"]
        .dropna()
        .nunique()
    )


def get_total_companies():
    return (
        load_jobs()["company"]
        .nunique()
    )


def get_latest_posting():
    return (
        load_jobs()["created_at"]
        .max()
    )


def get_average_jobs_per_day():

    df = load_jobs()

    avg = round(
        len(df) /
        df["created_at"].dt.date.nunique(),
        2
    )

    return pd.DataFrame(
        {
            "avg_jobs_per_day": [avg]
        }
    )


def get_recent_jobs():

    df = load_jobs()

    return (
        df.sort_values(
            "created_at",
            ascending=False
        )[[
            "title",
            "company",
            "city",
            "created_at"
        ]]
        .rename(
            columns={
                "created_at": "posted_date"
            }
        )
        .head(10)
    )


def get_data_quality_metrics():

    df = load_jobs()

    return pd.DataFrame({
        "total_jobs": [len(df)],
        "unique_jobs": [
            df["source_job_id"].nunique()
        ],
        "missing_city": [
            df["city"].isna().sum()
        ],
        "missing_state": [
            df["state"].isna().sum()
        ]
    })


def get_top_states():

    df = load_jobs()

    return (
        df.dropna(subset=["state"])
        .groupby("state")
        .size()
        .reset_index(name="total_jobs")
        .sort_values(
            "total_jobs",
            ascending=False
        )
    )


def get_company_city_data():

    df = load_jobs()

    return (
        df.dropna(subset=["city"])
        .groupby(
            ["city", "company"]
        )
        .size()
        .reset_index(name="total_jobs")
        .sort_values(
            ["city", "total_jobs"],
            ascending=[True, False]
        )
    )


def get_company_posting_trend():

    df = load_jobs()

    df["posting_date"] = (
        df["created_at"]
        .dt.date
    )

    return (
        df.groupby(
            ["posting_date", "company"]
        )
        .size()
        .reset_index(name="total_jobs")
    )


def get_top_skills():

    df = load_skills()

    return df.sort_values(
        "total_jobs",
        ascending=False
    )