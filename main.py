import logging
from src.extract.adzuna import fetch_jobs
from src.extract.save_raw import save_raw

data = fetch_jobs()

path = save_raw(data)

print(f"Saved to {path}")

logging.basicConfig(
    filename="logs/pipeline.log",
    level=logging.INFO,
)

logging.info(
    f"Fetched {data['count']} jobs"
)
