import logging

from src.extract.adzuna import fetch_jobs
from src.extract.save_raw import save_raw

from src.transform.clean_jobs import clean_jobs
from src.transform.save_processed import save_processed
from src.transform.extract_skills import extract_skills
from src.transform.save_skills import save_skills

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

    try:
        # -------------------------
        # Extract
        # -------------------------
        logging.info("Fetching jobs from Adzuna API")

        data = fetch_jobs()

        logging.info(
            "Fetched %d jobs",
            len(data["results"])
        )

        raw_path = save_raw(data)

        logging.info(
            "Raw data saved to %s",
            raw_path
        )

        print(f"Saved raw file: {raw_path}")

        # -------------------------
        # Transform
        # -------------------------
        logging.info("Cleaning job data")

        df = clean_jobs(data)

        print(f"Rows processed: {len(df)}")

        print(
            f"Columns: {', '.join(df.columns)}"
        )

        logging.info(
            "Processed %d rows",
            len(df)
        )

        logging.info("Running data quality checks")

        run_quality_checks(df)

        logging.info("Saving processed dataset")

        processed_path = save_processed(df)

        print(
            f"\nProcessed file saved: "
            f"{processed_path}"
        )

        logging.info(
            "Processed dataset saved to %s",
            processed_path
        )

        logging.info("Extracting skills")

        skills_df = extract_skills(df)

        logging.info(
            "Extracted %d unique skills",
            len(skills_df)
        )

        logging.info("Saving skills CSV")

        save_skills(skills_df)

        # -------------------------
        # Load
        # -------------------------
        logging.info("Loading jobs into MySQL")

        inserted_jobs = load_jobs(df)

        logging.info(
            "Inserted %d new jobs",
            inserted_jobs
        )

        logging.info("Loading skills into MySQL")

        loaded_skills = load_skills(skills_df)

        logging.info(
            "Loaded %d skills",
            loaded_skills
        )

        logging.info("Pipeline completed successfully")

    except Exception:
        logging.exception("Pipeline failed")
        raise


if __name__ == "__main__":
    main()