import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))

import streamlit as st
import plotly.express as px
from src.config.settings import USE_SQL

if USE_SQL:
    from src.dashboard.data_loader_sql import *
else:
    from src.dashboard.data_loader_csv import *

st.set_page_config(
    page_title="Job Market Intelligence",
    layout="wide"
)

# --------------------------------------------------
# Header
# --------------------------------------------------

st.markdown(
    """
    <h1 style='text-align:center;'>
        📊 Job Market Intelligence Dashboard
    </h1>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <p style='text-align:center; font-size:18px;'>
        Analytics dashboard built from Adzuna job market data.
    </p>
    """,
    unsafe_allow_html=True
)

st.divider()

# --------------------------------------------------
# Load Data
# --------------------------------------------------

companies = get_top_companies()
cities = get_top_cities()
jobs_by_day = get_jobs_by_day()
recent_jobs = get_recent_jobs()
quality = get_data_quality_metrics()
avg_jobs = get_average_jobs_per_day()
states = get_top_states()
company_city = get_company_city_data()
company_trend = get_company_posting_trend()
skills = get_top_skills()

# --------------------------------------------------
# KPI Row
# --------------------------------------------------

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric(
    "Total Jobs",
    get_total_jobs()
)

col2.metric(
    "Cities",
    get_total_cities()
)

col3.metric(
    "Companies",
    get_total_companies()
)

col4.metric(
    "Latest Posting",
    str(get_latest_posting())[:10]
)

col5.metric(
    "Average Jobs/Day",
    round(
        avg_jobs.iloc[0]["avg_jobs_per_day"],
        2
    )
)

st.divider()

# --------------------------------------------------
# Top Companies / Top Cities
# --------------------------------------------------

col6, col7 = st.columns(2)

with col6:

    st.subheader("Top Hiring Companies")

    companies = companies.sort_values(
        "total_jobs",
        ascending=True
    )

    fig = px.bar(
        companies,
        x="total_jobs",
        y="company",
        orientation="h"
    )

    fig.update_layout(
        height=450
    )

    st.plotly_chart(
        fig,
        width="stretch",
        config={
            "displayModeBar": False
        }
    )

with col7:

    st.subheader("Top Hiring Cities")

    fig = px.bar(
        cities.sort_values(
            "total_jobs",
            ascending=True
        ),
        x="total_jobs",
        y="city",
        orientation="h"
    )

    fig.update_layout(
        height=450
    )

    st.plotly_chart(
        fig,
        width="stretch",
        config={
            "displayModeBar": False
        }
    )

col8, col9 = st.columns(2)

with col8:
    st.subheader("Top Hiring States")

    fig = px.bar(
        states.sort_values(
            "total_jobs",
            ascending=True
        ),
        x="total_jobs",
        y="state",
        orientation="h"
    )

    st.plotly_chart(
        fig,
        width="stretch",
        config={
            "displayModeBar": False
        }
    )

with col9:
    selected_city = st.selectbox(
        "Select City",
        sorted(company_city["city"].unique())
    )

    filtered = company_city[
        company_city["city"] == selected_city
    ]

    st.dataframe(
        filtered,
        width="stretch"
    )

# --------------------------------------------------
# Hiring Trend
# --------------------------------------------------

st.subheader("Jobs Posted Over Time")

fig = px.line(
    jobs_by_day,
    x="posting_date",
    y="total_jobs",
    markers=True
)

fig.update_layout(
    height=500
)

st.plotly_chart(
    fig,
    width="stretch",
    config={
        "displayModeBar": False
    }
)

st.subheader("Company Hiring Trends")

fig = px.line(
    company_trend,
    x="posting_date",
    y="total_jobs",
    color="company"
)

st.plotly_chart(
    fig,
    width="stretch",
    config={
        "displayModeBar": False
    }
)

# --------------------------------------------------
# Recent Jobs
# --------------------------------------------------

st.subheader("Most Recent Job Postings")

st.dataframe(
    recent_jobs,
    width="stretch"
)

# --------------------------------------------------
# Top Skills
# --------------------------------------------------

st.subheader("Top Requested Skills")

fig = px.bar(
    skills.sort_values("total_jobs",ascending=True),
    x="total_jobs",
    y="skill",
    orientation="h",
)

st.plotly_chart(
    fig,
    width="stretch",
    config={
        "displayModeBar": False
    }
)

# --------------------------------------------------
# Data Quality Metrics
# --------------------------------------------------

st.subheader("Data Quality Metrics")

total_jobs = int(
    quality.iloc[0]["total_jobs"]
)

unique_jobs = int(
    quality.iloc[0]["unique_jobs"]
)

missing_city = int(
    quality.iloc[0]["missing_city"]
)

missing_state = int(
    quality.iloc[0]["missing_state"]
)

duplicate_jobs = (
    total_jobs - unique_jobs
)

completeness = round(((total_jobs * 2 - missing_city - missing_state)/ (total_jobs * 2))* 100,2)

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Duplicate Jobs",
    duplicate_jobs
)

col2.metric(
    "Missing City",
    missing_city
)

col3.metric(
    "Missing State",
    missing_state
)

col4.metric(
    "Data Completeness %",
    completeness
)

# --------------------------------------------------
# Footer
# --------------------------------------------------

st.divider()

st.caption(
    """
    <p style='text-align:center; font-size:14px;'>
        Data source: Adzuna API | 
        Updated via ETL pipeline | 
        Built with Streamlit <br>
        <a href="https://github.com/Pranav-MSK/job-market-intelligence" target="_blank" style="text-decoration:none; color:#1f77b4;">GitHub Repo</a> | 
        <a href="https://www.linkedin.com/in/pranav-m-s-krishnan-25b5982a9" target="_blank" style="text-decoration:none; color:#1f77b4;">LinkedIn Profile</a>
    </p>
    """,
    unsafe_allow_html=True
)