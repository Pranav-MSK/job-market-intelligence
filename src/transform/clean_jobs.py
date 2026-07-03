import pandas as pd


VALID_TITLES = [
    "software engineer",
    "software developer",
    "developer",
    "backend",
    "frontend",
    "front end",
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
    "doctor",
    "nurse",
    "customer support",
    "customer service",
    "business development",
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
    "chandigarh",
    "ladakh",
    "jammu and kashmir",
    "andaman and nicobar islands",
    "dadra and nagar haveli",
    "daman and diu",
    "lakshadweep",
    "puducherry",
}


MAJOR_CITIES = {
    "bangalore",
    "bengaluru",
    "hyderabad",
    "chennai",
    "mumbai",
    "pune",
    "gurgaon",
    "gurugram",
    "noida",
    "ghaziabad",
    "delhi",
    "new delhi",
    "kolkata",
    "ahmedabad",
    "rajkot",
    "lucknow",
    "kochi",
    "coimbatore",
    "jaipur",
    "indore",
    "bhopal",
    "mysore",
    "surat",
    "vadodara",
    "visakhapatnam",
    "nagpur",
    "thane",
    "navi mumbai",
    "faridabad",
    "sonipat",
    "dehradun",
    "trivandrum",
}


def keep_job(title):

    title = str(title).lower()

    if any(x in title for x in INVALID_TITLES):
        return False

    if any(x in title for x in VALID_TITLES):
        return True

    return False


def parse_location(location):

    if not location:
        return None, None, "India"

    parts = [p.strip() for p in location.split(",") if p.strip()]

    city = None
    state = None
    country = "India"

    # remove country if present
    if parts and parts[-1].lower() == "india":
        parts = parts[:-1]

    # find state
    for p in parts:
        if p.lower() in INDIAN_STATES:
            state = p
            break

    # find city
    for p in reversed(parts):

        if p == state:
            continue

        if p.lower() in MAJOR_CITIES:
            city = p
            break

    # locality, city
    if city is None and len(parts) >= 2:

        city = parts[-1]

    # only one location token
    if city is None and len(parts) == 1:

        token = parts[0]

        if token.lower() not in INDIAN_STATES:
            city = token

    if city == state:
        city = None

    return city, state, country


def clean_jobs(raw_data):

    rows = []

    seen = set()

    for job in raw_data["results"]:

        job_id = str(job.get("id"))

        if job_id in seen:
            continue

        seen.add(job_id)

        title = job.get("title", "")

        if not keep_job(title):
            continue

        location = (
            job.get("location", {})
            .get("display_name")
        )

        city, state, country = parse_location(location)

        rows.append(
            {
                "source_job_id": job_id,
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

    if df.empty:
        return df

    df = (
        df.sort_values("created_at")
        .drop_duplicates(
            subset="source_job_id",
            keep="last",
        )
        .reset_index(drop=True)
    )

    return df