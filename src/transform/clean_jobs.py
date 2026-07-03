import re
import pandas as pd


VALID_TITLES = [
    "software engineer",
    "software developer",
    "developer",
    "backend",
    "front end",
    "frontend",
    "front-end",
    "full stack",
    "fullstack",
    "web developer",
    "python developer",
    "java developer",
    "react developer",
    "node",
    ".net",
    "data engineer",
    "machine learning",
    "ml engineer",
    "ai engineer",
    "artificial intelligence",
    "devops",
    "cloud engineer",
    "platform engineer",
    "site reliability",
    "sre",
    "qa engineer",
    "test engineer",
    "automation engineer",
    "application developer",
    "software architect",
]


INVALID_TITLES = [
    "assistant professor",
    "associate professor",
    "professor",
    "lecturer",
    "teacher",
    "faculty",
    "trainer",
    "principal",
    "vice principal",
    "headmaster",
    "sales",
    "marketing",
    "accountant",
    "finance",
    "civil engineer",
    "mechanical engineer",
    "electrical engineer",
    "chemical engineer",
    "nurse",
    "doctor",
    "receptionist",
    "telecaller",
    "customer support",
    "customer service",
    "business development",
    "hr",
    "human resources",
]


INDIAN_STATES = {
    "andhra pradesh",
    "arunachal pradesh",
    "assam",
    "bihar",
    "chhattisgarh",
    "goa",
    "gujarat",
    "haryana",
    "himachal pradesh",
    "jharkhand",
    "karnataka",
    "kerala",
    "madhya pradesh",
    "maharashtra",
    "manipur",
    "meghalaya",
    "mizoram",
    "nagaland",
    "odisha",
    "punjab",
    "rajasthan",
    "sikkim",
    "tamil nadu",
    "telangana",
    "tripura",
    "uttar pradesh",
    "uttarakhand",
    "west bengal",
    "delhi",
    "jammu and kashmir",
    "ladakh",
    "chandigarh",
    "dadra and nagar haveli",
    "daman and diu",
    "lakshadweep",
    "puducherry",
    "andaman and nicobar islands",
}


def parse_location(location_str):

    if not location_str:
        return None, None, "India"

    parts = [x.strip() for x in location_str.split(",")]

    city = None
    state = None
    country = "India"

    if len(parts) >= 3:
        city = parts[0]
        state = parts[1]
        country = parts[-1]

    elif len(parts) == 2:

        first = parts[0].lower()
        second = parts[1].lower()

        if second == "india":
            state = parts[0]
            country = parts[1]

        else:
            city = parts[0]
            state = parts[1]

    elif len(parts) == 1:

        first = parts[0].lower()

        if first in INDIAN_STATES:
            state = parts[0]
        else:
            country = parts[0]

    if city and city.lower() in INDIAN_STATES:
        state = city
        city = None

    return city, state, country


def keep_job(title):

    title = str(title).lower()

    if any(word in title for word in INVALID_TITLES):
        return False

    if any(word in title for word in VALID_TITLES):
        return True

    return False


def clean_jobs(raw_data):

    rows = []

    for job in raw_data["results"]:

        title = job.get("title")

        if not keep_job(title):
            continue

        location = (
            job.get("location", {})
            .get("display_name")
        )

        city, state, country = parse_location(location)

        rows.append(
            {
                "source_job_id": job.get("id"),
                "title": title,
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
                "description": job.get("description"),
            }
        )

    df = pd.DataFrame(rows)

    return df