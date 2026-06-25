from collections import Counter

SKILLS = [
    "python",
    "sql",
    "aws",
    "azure",
    "gcp",
    "java",
    "javascript",
    "react",
    "spark",
    "airflow",
    "docker",
    "kubernetes",
    "tableau",
    "power bi",
    "snowflake",
    "pandas",
    "numpy",
]

def extract_skills(df):

    skill_counter = Counter()

    for description in df["description"]:

        text = str(description).lower()

        for skill in SKILLS:

            if skill in text:
                skill_counter[skill] += 1

    return skill_counter