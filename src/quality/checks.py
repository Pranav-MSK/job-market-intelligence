def run_quality_checks(df):
    report = {
        "total_rows": len(df),
        "duplicate_job_ids": df["source_job_id"].duplicated().sum(),
        "missing_titles": df["title"].isna().sum(),
        "missing_companies": df["company"].isna().sum(),
        "missing_locations": df["location"].isna().sum(),
    }

    print("\n--- Data Quality Report ---")

    for key, value in report.items():
        print(f"{key}: {value}")

    return report