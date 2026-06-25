import streamlit as st
import plotly.express as px

from src.dashboard.data_loader import (
    get_top_companies,
    get_top_cities,
    get_jobs_by_day,
    get_total_jobs,
    get_total_cities,
    get_total_companies,
    get_latest_posting,
    get_average_jobs_per_day,
    get_recent_jobs,
    get_data_quality_metrics,
)

st.set_page_config(
    page_title="Job Market Intelligence",
    layout="wide"
)

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

companies = get_top_companies()
cities = get_top_cities()
jobs_by_day = get_jobs_by_day()
recent_jobs = get_recent_jobs()
quality = get_data_quality_metrics()
avg_jobs = get_average_jobs_per_day()

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
    "Latest Job",
    str(get_latest_posting())[:10]
)

col5.metric(
    "Avg Jobs / Day",
    round(avg_jobs.iloc[0]["avg_jobs_per_day"],2)
)

st.divider()

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
        orientation="h",
        title="Top Hiring Companies"
    )
    st.plotly_chart(
        fig,
        width="stretch"
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
        orientation="h",
        title="Top Hiring Cities"
    )
    st.plotly_chart(
        fig,
        width="stretch"
    )

st.subheader("Jobs Posted Over Time")

fig = px.line(
    jobs_by_day,
    x="posting_date",
    y="total_jobs",
    title="Jobs Posted Over Time",
)

st.plotly_chart(
    fig,
    width="stretch",
)

st.subheader("Most Recent Job Postings")

st.dataframe(
    recent_jobs,
    width="stretch",
)

st.subheader("Data Quality Metrics")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Jobs",
    int(quality.iloc[0]["total_jobs"])
)

col2.metric(
    "Unique Jobs",
    int(quality.iloc[0]["unique_jobs"])
)

col3.metric(
    "Missing City",
    int(quality.iloc[0]["missing_city"])
)

col4.metric(
    "Missing State",
    int(quality.iloc[0]["missing_state"])
)