from dotenv import load_dotenv
import os

load_dotenv()

ADZUNA_APP_ID = os.getenv("ADZUNA_APP_ID")
ADZUNA_APP_KEY = os.getenv("ADZUNA_APP_KEY")

COUNTRY = "in"
JOB_QUERY = "software engineer"

RESULTS_PER_PAGE = 50
DEFAULT_PAGE = 1

MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_PORT = os.getenv("MYSQL_PORT")
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")

USE_SQL = False # Set to True to use data_loader_sql.py (development), False to use data_loader_csv.py (production/streamlit deployment)