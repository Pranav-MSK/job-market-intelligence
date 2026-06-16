from dotenv import load_dotenv
import os

load_dotenv()

ADZUNA_APP_ID = os.getenv("ADZUNA_APP_ID")
ADZUNA_APP_KEY = os.getenv("ADZUNA_APP_KEY")

COUNTRY = "in"
JOB_QUERY = "software engineer"

RESULTS_PER_PAGE = 50
DEFAULT_PAGE = 1