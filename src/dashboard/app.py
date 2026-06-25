import streamlit as st
import plotly.express as px

from src.dashboard.data_loader import (
    get_top_companies,
    get_top_cities,
    get_jobs_by_day,
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

st.dataframe(
    companies,
    width="stretch",
)

st.subheader("Top Hiring Cities")

st.dataframe(
    cities,
    width="stretch",
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