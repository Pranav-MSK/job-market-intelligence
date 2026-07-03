import re
from collections import Counter

import pandas as pd


SKILL_PATTERNS = {

    # Languages
    "Python": r"\bpython\b",
    "Java": r"\bjava\b(?!script)",
    "JavaScript": r"\bjavascript\b|\bjs\b",
    "TypeScript": r"\btypescript\b|\bts\b",
    "C": r"\bc\b",
    "C++": r"\bc\+\+|cpp\b",
    "C#": r"\bc#|csharp\b",
    "Go": r"\bgo(lang)?\b",
    "Rust": r"\brust\b",
    "PHP": r"\bphp\b",
    "Ruby": r"\bruby\b",
    "Scala": r"\bscala\b",
    "Kotlin": r"\bkotlin\b",
    "Swift": r"\bswift\b",

    # Frontend
    "React": r"\breact(js)?\b",
    "Angular": r"\bangular\b",
    "Vue": r"\bvue(js)?\b",
    "HTML": r"\bhtml5?\b",
    "CSS": r"\bcss3?\b",
    "Bootstrap": r"\bbootstrap\b",
    "Tailwind CSS": r"\btailwind\b",

    # Backend
    "Node.js": r"\bnode\.?js\b",
    "Express.js": r"\bexpress\b",
    "Django": r"\bdjango\b",
    "Flask": r"\bflask\b",
    "FastAPI": r"\bfastapi\b",
    "Spring Boot": r"\bspring(\s*boot)?\b",
    ".NET": r"\.net|dotnet",
    "ASP.NET": r"\basp\.?net\b",

    # Databases
    "SQL": r"\bsql\b",
    "MySQL": r"\bmysql\b",
    "PostgreSQL": r"\bpostgres(ql)?\b",
    "MongoDB": r"\bmongodb\b",
    "Redis": r"\bredis\b",
    "Oracle": r"\boracle\b",

    # Cloud
    "AWS": r"\baws\b|amazon web services",
    "Azure": r"\bazure\b",
    "GCP": r"\bgcp\b|google cloud",

    # DevOps
    "Docker": r"\bdocker\b",
    "Kubernetes": r"\bkubernetes\b|\bk8s\b",
    "Jenkins": r"\bjenkins\b",
    "Git": r"\bgit\b",
    "GitHub": r"\bgithub\b",
    "GitLab": r"\bgitlab\b",
    "CI/CD": r"\bci\/cd\b|\bcontinuous integration\b",
    "Linux": r"\blinux\b",

    # Data
    "Pandas": r"\bpandas\b",
    "NumPy": r"\bnumpy\b",
    "PySpark": r"\bpyspark\b",
    "Spark": r"\bspark\b",
    "Hadoop": r"\bhadoop\b",
    "Airflow": r"\bairflow\b",

    # AI / ML
    "Machine Learning": r"\bmachine learning\b",
    "Deep Learning": r"\bdeep learning\b",
    "TensorFlow": r"\btensorflow\b",
    "PyTorch": r"\bpytorch\b",
    "Scikit-learn": r"\bscikit[- ]?learn\b|\bsklearn\b",
    "LLM": r"\bllm\b|large language model",
    "OpenAI": r"\bopenai\b",
    "LangChain": r"\blangchain\b",
    "RAG": r"\brag\b|retrieval augmented generation",

    # BI
    "Power BI": r"\bpower\s?bi\b",
    "Tableau": r"\btableau\b",
    "Excel": r"\bexcel\b",

}


def extract_skills(df):

    counter = Counter()

    descriptions = (
        df["description"]
        .fillna("")
        .astype(str)
        .str.lower()
    )

    for text in descriptions:

        found = set()

        for skill, pattern in SKILL_PATTERNS.items():

            if re.search(pattern, text, re.IGNORECASE):

                found.add(skill)

        for skill in found:
            counter[skill] += 1

    skills_df = (
        pd.DataFrame(
            counter.items(),
            columns=[
                "skill",
                "total_jobs",
            ],
        )
        .sort_values(
            "total_jobs",
            ascending=False,
        )
        .reset_index(drop=True)
    )

    return skills_df