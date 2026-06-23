import pandas as pd


def parse_location(location_str):
    if not location_str:
        return None, None, "India"

    parts = [
        part.strip()
        for part in location_str.split(",")
    ]

    if len(parts) == 1:
        return None, None, parts[0]

    if len(parts) == 2:
        return parts[0], parts[1], "India"

    return (
        parts[0],
        parts[1],
        parts[-1],
    )


def clean_jobs(raw_data):
    rows = []

    for job in raw_data["results"]:

        location = (
            job.get("location", {})
            .get("display_name")
        )

        city, state, country = (
            parse_location(location)
        )

        rows.append(
            {
                "source_job_id": job.get("id"),
                "title": job.get("title"),
                "company": (
                    job.get("company", {})
                    .get("display_name")
                ),
                "city": city,
                "state": state,
                "country": country,
                "created_at": pd.to_datetime(
                    job.get("created"),
                    utc=True,
                ),
                "description": job.get(
                    "description"
                ),
            }
        )

    return pd.DataFrame(rows)