# Local Setup Guide

This guide explains how to set up the Job Market Intelligence Platform for local development.

---

# Prerequisites

Install the following software before starting:

* Python 3.11 or later
* Git
* MySQL 8.0+
* A code editor (VS Code recommended)

---

# 1. Clone the Repository

```bash
git clone https://github.com/Pranav-MSK/job-market-intelligence.git

cd job-market-intelligence
```

---

# 2. Create a Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

# 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 4. Configure Environment Variables

Create a `.env` file in the project root.

You can copy the provided example:

```bash
cp .env.example .env
```

(or create it manually on Windows)

Populate the file with your credentials:

```env
ADZUNA_APP_ID=your_app_id
ADZUNA_APP_KEY=your_app_key

MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_DATABASE=job_market_intelligence
MYSQL_USER=root
MYSQL_PASSWORD=your_password
```

---

# 5. Create the Database

Open MySQL and create the project database.

```sql
CREATE DATABASE job_market_intelligence;

-- 1. Create the master jobs table
CREATE TABLE jobs (
    source_job_id VARCHAR(50) PRIMARY KEY,
    title VARCHAR(255),
    company VARCHAR(255),
    city VARCHAR(100),
    state VARCHAR(100),
    country VARCHAR(100),
    created_at DATETIME,
    description TEXT,
    inserted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 2. Create the skills dimension table 
CREATE TABLE skills (
    skill VARCHAR(100) NOT NULL,
    total_jobs BIGINT DEFAULT 0,
);
```

---

# 6. Run the ETL Pipeline

Execute:

```bash
python main.py
```

The pipeline performs the following steps:

1. Fetches software engineering jobs from the Adzuna API.
2. Saves the raw API response as JSON.
3. Cleans and transforms the data.
4. Extracts commonly requested technical skills.
5. Performs data quality checks.
6. Updates the processed CSV dataset.
7. Loads new jobs into MySQL.
8. Updates the skills table.

Example output:

```text
Saved raw file: data/raw/jobs_20260627_145500.json
Rows processed: 50
Columns: source_job_id, title, company, city, state, country, created_at, description

--- Data Quality Report ---
total_rows: 50
duplicate_job_ids: 0
missing_titles: 0
missing_companies: 0
missing_cities: 15
missing_states: 14

Processed file saved: data\processed\latest_jobs.csv
No new records found. Skipping load.
Loaded 17 skills.
```

---

# 7. Launch the Dashboard

The dashboard supports two data sources:

## SQL Mode (Local Development)

In `src/dashboard/app.py`:

```python
USE_SQL = True
```

Start Streamlit:

```bash
python -m streamlit run src/dashboard/app.py
```

---

## CSV Mode (Deployment)

Switch:

```python
USE_SQL = False
```

Run the same command:

```bash
python -m streamlit run src/dashboard/app.py
```

In CSV mode, the dashboard reads directly from:

```text
data/processed/latest_jobs.csv
```

No MySQL server is required.

---

# Project Modes

## Local Development

* ETL Pipeline
* MySQL Database
* Dashboard (SQL)

Recommended while developing new features.

---

## Deployment

* ETL Pipeline (optional)
* CSV Dataset
* Dashboard (CSV)

Recommended for Streamlit Community Cloud deployment.

---

# Updating the Dashboard

Whenever new data is fetched, simply run:

```bash
python main.py
```

This updates:

```text
data/processed/latest_jobs.csv
```

If the dashboard is running in CSV mode, refreshing the browser will display the latest data.

---

# Troubleshooting

## ModuleNotFoundError: No module named 'src'

Run Streamlit using:

```bash
python -m streamlit run src/dashboard/app.py
```

instead of:

```bash
streamlit run src/dashboard/app.py
```

---

## Database Connection Error

Verify:

* MySQL is running.
* Credentials in `.env` are correct.
* The database exists.

---

## Dashboard Shows No Data

Ensure:

* `latest_jobs.csv` exists in `data/processed/`.
* The pipeline has been executed successfully.
* `USE_SQL` matches the intended data source.

---

# Development Workflow

A typical development cycle is:

```text
Modify Code
      ↓
Run main.py
      ↓
Verify MySQL / CSV
      ↓
Launch Dashboard
      ↓
Validate Results
      ↓
Commit Changes
```
