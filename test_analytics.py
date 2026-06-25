from src.analytics.analytics import run_query

print("\nTop Companies\n")

print(
    run_query(
        "sql/top_companies.sql"
    )
)

print("\nTop Cities\n")

print(
    run_query(
        "sql/top_cities.sql"
    )
)