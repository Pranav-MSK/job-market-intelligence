import pandas as pd


def clean_jobs(raw_data):
    rows = []

    for job in raw_data["results"]:
        rows.append(
            {
                "source_job_id": job.get("id"),
                "title": job.get("title"),
                "company": job.get(
                    "company", {}
                ).get("display_name"),
                "location": job.get(
                    "location", {}
                ).get("display_name"),
                "created_at": job.get("created"),
                "description": job.get("description"),
            }
        )

    df = pd.DataFrame(rows)

    return df