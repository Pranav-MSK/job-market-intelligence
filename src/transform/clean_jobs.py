import pandas as pd


def parse_location(location_str):
    if not location_str:
        return None, None, "India"

    parts = [part.strip() for part in location_str.split(",")]

    city = None
    state = None
    country = "India"

    if len(parts) == 3:
        city = parts[0]
        state = parts[1]
        country = parts[2]

    elif len(parts) == 2:
        # State, Country
        if parts[1].lower() == "india":
            state = parts[0]
            country = parts[1]

        # City, State
        else:
            city = parts[0]
            state = parts[1]

    elif len(parts) == 1:
        country = parts[0]

    # Validation
    if city == state:
        city = None

    if city == country:
        city = None

    if state == country:
        state = None

    return city, state, country


def clean_jobs(raw_data):
    rows = []

    for job in raw_data["results"]:

        location = (
            job.get("location", {})
            .get("display_name")
        )

        city, state, country = parse_location(location)

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