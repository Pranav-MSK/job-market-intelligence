import requests

from src.config.settings import (
    ADZUNA_APP_ID,
    ADZUNA_APP_KEY,
    COUNTRY,
    JOB_QUERY,
    RESULTS_PER_PAGE,
    DEFAULT_PAGE,
)

BASE_URL = "https://api.adzuna.com/v1/api/jobs"


def fetch_jobs(
    country=COUNTRY,
    query=JOB_QUERY,
    page=DEFAULT_PAGE,
    results_per_page=RESULTS_PER_PAGE,
):
    url = (
        f"{BASE_URL}/{country}/search/{page}"
        f"?app_id={ADZUNA_APP_ID}"
        f"&app_key={ADZUNA_APP_KEY}"
        f"&what={query}"
        f"&results_per_page={results_per_page}"
        f"&max_days_old=14"
    )

    response = requests.get(url, timeout=30,)

    if response.status_code != 200:
        print(
            f"API Error: "
            f"{response.status_code}"
        )
        print(response.text)

    response.raise_for_status()

    return response.json()