from sqlalchemy import create_engine
from urllib.parse import quote_plus

from src.config.settings import (
    MYSQL_HOST,
    MYSQL_PORT,
    MYSQL_DATABASE,
    MYSQL_USER,
    MYSQL_PASSWORD,
)


def get_engine():

    encoded_password = quote_plus(MYSQL_PASSWORD)

    connection_string = (
        f"mysql+pymysql://"
        f"{MYSQL_USER}:{encoded_password}"
        f"@{MYSQL_HOST}:{MYSQL_PORT}"
        f"/{MYSQL_DATABASE}"
    )

    return create_engine(connection_string)