import logging

from src.extract.adzuna import fetch_jobs
from src.extract.save_raw import save_raw

from src.transform.clean_jobs import clean_jobs
from src.transform.save_processed import save_processed
from src.transform.extract_skills import extract_skills

from src.quality.checks import run_quality_checks

from src.load.load_jobs import load_jobs
from src.load.load_skills import load_skills

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
    print(df[["city", "state", "country"]].drop_duplicates().head(20))

    print(f"Rows processed: {len(df)}")

    print(
        f"Columns: "
        f"{', '.join(df.columns)}"
    )

    run_quality_checks(df)

    processed_path = save_processed(df)

    load_jobs(df)

    print(
        f"\nProcessed file saved: "
        f"{processed_path}"
    )
    
    skills_df = extract_skills(df)

    load_skills(skills_df)

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