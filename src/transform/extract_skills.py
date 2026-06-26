from collections import Counter
import pandas as pd

SKILLS = [
    "python",
    "sql",
    "mysql",
    "postgresql",
    "java",
    "c++",
    "c#",
    "javascript",
    "typescript",
    "react",
    "angular",
    "vue",
    "django",
    "flask",
    "fastapi",
    "spring",
    "docker",
    "kubernetes",
    "aws",
    "azure",
    "gcp",
    "airflow",
    "spark",
    "hadoop",
    "tableau",
    "power bi",
    "excel",
    "git",
    "github",
    "linux",
    "machine learning",
    "deep learning",
    "tensorflow",
    "pytorch",
    "pandas",
    "numpy"
]

def extract_skills(df):
    counter = Counter()

    for description in df["description"]:
        text = str(description).lower()
        for skill in SKILLS:
            if skill in text:
                counter[skill] += 1

    skills_df = pd.DataFrame(
        counter.items(),
        columns=[
            "skill",
            "total_jobs"
        ]
    )

    skills_df = skills_df.sort_values(
        "total_jobs",
        ascending=False
    )
    
    return skills_df