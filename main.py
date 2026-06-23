import logging

from src.extract.adzuna import fetch_jobs
from src.extract.save_raw import save_raw
from src.transform.clean_jobs import clean_jobs
from src.transform.save_processed import save_processed


logging.basicConfig(
    filename="logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def main():
    logging.info("Pipeline started")

    data = fetch_jobs()

    raw_path = save_raw(data)

    print(f"Saved raw file: {raw_path}")

    df = clean_jobs(data)

    print("\nData Preview:")
    print(df.head())

    print("\nData Info:")
    print(df.info())

    processed_path = save_processed(df)

    print(
        f"\nProcessed file saved: "
        f"{processed_path}"
    )

    logging.info(
        f"Fetched {len(data['results'])} jobs"
    )

    logging.info(
        f"Raw data saved to {raw_path}"
    )

    logging.info(
        f"Processed data saved to "
        f"{processed_path}"
    )

    logging.info("Pipeline completed")


if __name__ == "__main__":
    main()