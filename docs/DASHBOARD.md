# Dashboard Guide

The Job Market Intelligence Dashboard is an interactive Streamlit application built on top of the ETL pipeline. It visualizes hiring activity, demand trends, company distribution, geographic distribution, and technology demand extracted from software engineering job postings.

The dashboard is intended for exploratory analysis rather than static reporting, allowing users to quickly identify hiring patterns across companies, locations, and technologies.

---

# Running the Dashboard

## Local Development (MySQL)

The dashboard can query the local MySQL database during development.

Configure the flag inside `src/dashboard/app.py`:

```python
USE_SQL = True
```

Start the application:

```bash
python -m streamlit run src/dashboard/app.py
```

---

## Deployment (CSV)

For Streamlit Community Cloud, the dashboard reads from processed CSV files instead of MySQL.

Change the flag before deployment:

```python
USE_SQL = False
```

The dashboard will automatically load:

```
data/processed/latest_jobs.csv
data/processed/skills_skills.csv
```

No database is required in production.

---

# Dashboard Sections

## Summary Metrics

The top section displays high-level statistics.

Current metrics include:

* Total Jobs
* Companies
* Cities
* Latest Posting Date
* Average Jobs per Day

These provide a quick overview of the current dataset.

---

## Top Hiring Companies

Displays the companies with the largest number of software engineering openings.

Visualization:

* Horizontal bar chart

Purpose:

* Identify major hiring organizations.
* Compare hiring volume across companies.

---

## Top Hiring Cities

Displays cities ranked by the number of available job postings.

Visualization:

* Horizontal bar chart

Purpose:

* Identify geographic hiring hotspots.
* Compare demand across cities.

---

## Top Hiring States

Displays state-level hiring demand.

Visualization:

* Horizontal bar chart

Purpose:

* Compare hiring activity across Indian states.

---

## Skills in Demand

Shows the most frequently requested technical skills extracted from job descriptions.

Examples include:

* Python
* SQL
* Java
* JavaScript
* React
* AWS
* Docker
* Kubernetes
* Pandas
* Machine Learning

Visualization:

* Horizontal bar chart

Purpose:

* Identify technologies currently in demand.
* Understand employer skill requirements.

---

## Companies Hiring by City

Displays companies hiring within each city.

Visualization:

* Interactive table

Purpose:

* Explore which organizations are actively recruiting in specific locations.

---

## Jobs Posted Over Time

Displays posting activity by date.

Visualization:

* Line chart with markers

Purpose:

* Observe changes in hiring activity over time.
* Detect spikes or periods of increased recruitment.

Future improvements may include:

* Weekly aggregation
* Monthly aggregation
* Rolling averages
* Date range filters

---

## Recent Job Postings

Displays the latest jobs collected by the pipeline.

Columns include:

* Job Title
* Company
* City
* Posting Date

Purpose:

* Quickly inspect the newest data ingested into the system.

---

## Data Quality Metrics

The dashboard includes operational quality checks for the dataset.

Current metrics:

* Total Jobs
* Unique Job IDs
* Missing City Values
* Missing State Values

Purpose:

* Monitor pipeline health.
* Detect data quality issues after ingestion.

---

# Data Sources

Depending on the selected mode, the dashboard reads from one of two sources.

## SQL Mode

```
MySQL
```

Used during local development.

Queries are executed directly against the relational database.

---

## CSV Mode

```
jobs_latest.csv
skills_latest.csv
```

Used for deployment on Streamlit Community Cloud.

This mode removes the dependency on MySQL while preserving the same dashboard functionality.

---

# Current Features

The dashboard currently supports:

* Summary KPI cards
* Interactive Plotly charts
* Company analysis
* City analysis
* State analysis
* Hiring timeline
* Skills analysis
* Recent jobs table
* Data quality metrics

---

# Planned Enhancements

The following features are planned for future iterations:

* Remote vs On-site job analysis
* Weekly and monthly hiring trends
* Company hiring trends over time
* Interactive dashboard filters
* Search by company
* Search by city
* Search by skill

---

# Design Principles

The dashboard is designed with the following goals:

* Clean, uncluttered layout
* Interactive visualizations
* Lightweight deployment
* Consistent metrics between SQL and CSV modes
* Easy extensibility as additional analytics are added

The separation of SQL and CSV data loaders ensures that development and deployment workflows remain independent while sharing the same user interface.
