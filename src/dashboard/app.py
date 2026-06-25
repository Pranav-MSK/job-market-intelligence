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
)

col1, col2, col3, col4 = st.columns(4)

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

st.set_page_config(
    page_title="Job Market Intelligence",
    layout="wide",
)

st.title("📊 Job Market Intelligence Dashboard")

st.markdown(
    "Analytics dashboard built from Adzuna job market data."
)

companies = get_top_companies()
cities = get_top_cities()
jobs_by_day = get_jobs_by_day()

st.subheader("Top Hiring Companies")

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

st.subheader("Top Hiring Cities")

fig = px.bar(
    cities,
    x="city",
    y="total_jobs",
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