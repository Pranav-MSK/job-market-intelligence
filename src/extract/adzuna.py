import requests

from src.config.settings import (
    ADZUNA_APP_ID,
    ADZUNA_APP_KEY,
    COUNTRY,
    JOB_QUERY,
)

BASE_URL = "https://api.adzuna.com/v1/api/jobs"


def fetch_jobs(
    country=COUNTRY,
    query=JOB_QUERY,
    page=1,
    results_per_page=50
):
    url = (
        f"{BASE_URL}/{country}/search/{page}"
        f"?app_id={ADZUNA_APP_ID}"
        f"&app_key={ADZUNA_APP_KEY}"
        f"&what={query}"
        f"&results_per_page={results_per_page}"
    )

    response = requests.get(url, timeout=30)

    response.raise_for_status()

    return response.json()