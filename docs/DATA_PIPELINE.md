# Data Pipeline

This document describes the end-to-end ETL pipeline used in the Job Market Intelligence Platform.

---

# Pipeline Overview

```text
                Adzuna Jobs API
                       │
                       ▼
              Extract Raw JSON
                       │
                       ▼
            Store Timestamped JSON
                       │
                       ▼
              Transform & Clean Data
                       │
        ┌──────────────┴──────────────┐
        ▼                             ▼
  Extract Skills              Data Quality Checks
        │                             │
        └──────────────┬──────────────┘
                       ▼
           Save Processed CSV Dataset
                       │
             ┌─────────┴─────────┐
             ▼                   ▼
        Load into MySQL      Dashboard (CSV)
```

---

# Step 1 — Data Extraction

The pipeline retrieves software engineering job postings from the Adzuna Jobs API.

Each execution requests the latest available jobs and saves the complete API response as a timestamped JSON file.

Example:

```
data/raw/jobs_20260626_194600.json
```

Keeping raw snapshots makes the pipeline reproducible and allows inspection of the original source data.

---

# Step 2 — Data Transformation

The raw API response contains nested JSON objects that are flattened into an analytics-friendly table.

The transformation process performs:

- flattening nested JSON
- extracting company names
- parsing location fields
- separating location into:
  - city
  - state
  - country
- converting timestamps to UTC datetime
- standardizing column names

The resulting dataset contains:

| Column | Description |
|---------|-------------|
| source_job_id | Adzuna job identifier |
| title | Job title |
| company | Hiring company |
| city | City |
| state | State |
| country | Country |
| created_at | Posting timestamp |
| description | Full job description |

---

# Step 3 — Skill Extraction

The pipeline scans every job description and searches for predefined technical skills.

Examples include:

- Python
- SQL
- Java
- JavaScript
- React
- Docker
- Kubernetes
- AWS
- Azure
- Pandas
- NumPy
- Git
- Linux

Each detected skill increments a counter.

The output is a skills dataset containing:

| skill | total_jobs |
|--------|------------|
| python | 18 |
| sql | 15 |
| docker | 10 |

This dataset is loaded into the `skills` table in MySQL for dashboard visualizations.

---

# Step 4 — Data Quality Validation

Before loading the data, the pipeline performs several validation checks.

Current metrics include:

- Total rows
- Duplicate job IDs
- Missing titles
- Missing companies
- Missing cities
- Missing states

Example output:

```text
--- Data Quality Report ---

total_rows: 50
duplicate_job_ids: 0
missing_titles: 0
missing_companies: 0
missing_cities: 14
missing_states: 14
```

These checks help detect malformed or incomplete API responses before data is loaded.

---

# Step 5 — Processed Dataset

After validation, the cleaned dataset is written to CSV.

Rather than creating a new CSV for every run, the pipeline maintains a cumulative dataset.

```
data/processed/latest_jobs.csv
```

Behavior:

- append only new jobs
- ignore duplicate job IDs
- maintain historical records
- serve as the dashboard's data source when running in CSV mode

This file is committed to GitHub so deployed dashboards can display updated data without requiring a live database.

---

# Step 6 — Database Loading

For local development, the cleaned dataset is also loaded into MySQL.

The loading process is incremental.

Duplicate records are prevented by checking the existing `source_job_id` values before inserting new rows.

Two tables are maintained:

## jobs

Stores cleaned job postings.

## skills

Stores aggregated skill counts extracted from job descriptions.

---

# Step 7 — Dashboard

The Streamlit dashboard supports two data sources.

## SQL Mode

```
MySQL Database
        │
        ▼
data_loader_sql.py
        │
        ▼
 Dashboard
```

Used during local development.

---

## CSV Mode

```
latest_jobs.csv
       │
       ▼
data_loader_csv.py
       │
       ▼
 Dashboard
```

Used for deployment on Streamlit Community Cloud, where a local MySQL server is unavailable.

A simple flag in `app.py` determines which loader is used.

```python
USE_SQL = False
```

---

# Incremental Loading Strategy

The pipeline is designed to preserve historical data.

Each execution:

1. fetches the newest jobs
2. transforms the data
3. validates the dataset
4. extracts skills
5. appends only unseen jobs
6. updates the cumulative CSV
7. inserts only new records into MySQL

This prevents duplicate entries while allowing the dataset to grow over time.

---

# Current Pipeline Status

| Component | Status |
|-----------|--------|
| API Extraction | ✅ |
| Raw JSON Storage | ✅ |
| Data Cleaning | ✅ |
| Location Parsing | ✅ |
| Skill Extraction | ✅ |
| Data Quality Checks | ✅ |
| Processed CSV Generation | ✅ |
| Incremental MySQL Loading | ✅ |
| CSV Dashboard Support | ✅ |
| Streamlit Dashboard | ✅ |
| GitHub Actions Automation | Planned |