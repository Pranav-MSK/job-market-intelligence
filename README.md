# Job Market Intelligence Platform

An end-to-end Data Engineering and Analytics project that collects software engineering job postings from the Adzuna API, transforms and stores them in a relational database, and exposes hiring insights through an analytics dashboard.

## Project Overview

The goal of this project is to build an automated pipeline that tracks labor market trends by collecting job postings and converting them into actionable insights.

The platform is designed to answer questions such as:

* Which companies are hiring the most software engineers?
* Which cities have the highest demand for technical talent?
* What technologies and skills are most frequently requested?
* How are hiring trends changing over time?
* What proportion of roles are remote versus location-based?

This project demonstrates the complete data lifecycle:

* Data Extraction
* Data Transformation
* Data Validation
* Database Loading
* Pipeline Automation
* Analytics & Visualization

---

## Architecture

```text
                Adzuna API
                     │
                     ▼
              Extract Layer
                     │
                     ▼
              Raw JSON Files
              (data/raw/)
                     │
                     ▼
            Transform Layer
                     │
                     ▼
             Clean Dataset
          (data/processed/)
                     │
                     ▼
              MySQL Database
                     │
                     ▼
            Analytics Queries
                     │
                     ▼
                Dashboard
```

---

## Tech Stack

### Programming

* Python 3.11+

### Data Processing

* Pandas

### API Integration

* Requests

### Database

* MySQL
* SQLAlchemy

### Configuration

* python-dotenv

### Dashboard

* Streamlit
* Plotly

### Testing

* Pytest

### Version Control

* Git
* GitHub

---

## Project Structure

```text
job-market-intelligence/

├── data/
│   ├── raw/
│   └── processed/
│
├── logs/
│
├── sql/
│
├── src/
│   ├── config/
│   │   └── settings.py
│   │
│   ├── extract/
│   │   ├── adzuna.py
│   │   ├── save_raw.py
│   │   └── explore.py
│   │
│   ├── transform/
│   │
│   ├── load/
│   │
│   ├── quality/
│   │
│   └── dashboard/
│
├── tests/
│
├── .env
├── .gitignore
├── main.py
├── requirements.txt
└── README.md
```

---

## Data Pipeline

### Extract

The pipeline retrieves software engineering job postings from the Adzuna API.

Example fields:

* Job ID
* Title
* Company
* Location
* Description
* Created Date

Raw responses are stored as timestamped JSON snapshots.

Example:

```text
data/raw/jobs_20260616_183755.json
```

---

### Transform

The transformation layer:

* Flattens nested JSON structures
* Standardizes field names
* Parses location information
* Removes duplicates
* Performs validation checks

Output:

```text
data/processed/jobs_clean.csv
```

---

### Load

Cleaned data is loaded into MySQL.

Primary table:

```sql
jobs
```

Key columns:

```text
source_job_id
title
company
city
state
country
created_at
description
```

---

## Environment Variables

Create a `.env` file in the project root:

```env
ADZUNA_APP_ID=your_app_id
ADZUNA_APP_KEY=your_app_key

MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_DATABASE=job_market
MYSQL_USER=root
MYSQL_PASSWORD=your_password
```

Do not commit this file to GitHub.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/job-market-intelligence.git

cd job-market-intelligence
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate:

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Pipeline

Run the ETL pipeline:

```bash
python main.py
```

Expected output:

```text
Saved to data/raw/jobs_YYYYMMDD_HHMMSS.json
```

---

## Data Quality Checks

The pipeline validates:

* Row counts
* Duplicate job IDs
* Missing critical fields
* Schema consistency

Examples:

```text
Rows Processed
Duplicate Records
Missing Companies
Missing Titles
```

---

## Learning Objectives

This project was built to practice:

* Data Engineering
* ETL Development
* API Integration
* Data Modeling
* SQL
* Analytics Engineering
* Dashboard Development
* Workflow Automation

---

## Project Status

Current Phase:

```text
Phase 1: Data Extraction
```

Roadmap:
```
[x] Project Setup
[x] API Integration
[x] Raw Data Storage
[x] Data Transformation
[ ] Database Loading
[ ] Data Quality Framework
[ ] Automation
[ ] Dashboard Development
```

---

## License

This project is for educational and portfolio purposes.
