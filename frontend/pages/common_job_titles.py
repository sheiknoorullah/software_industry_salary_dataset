import streamlit as st
from components.data_fetcher import fetch_data
import pandas as pd
import plotly.express as px


def main():
    st.title("Most Common Job Titles")
    job_titles = fetch_data("common-job-titles")
    if job_titles:
        df = pd.DataFrame(job_titles)
        st.dataframe(df)
        fig = px.bar(df, x="Job Title", y="Count")
        st.plotly_chart(fig)


if __name__ == "__main__":
    main()
