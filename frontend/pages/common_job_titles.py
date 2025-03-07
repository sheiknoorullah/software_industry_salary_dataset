import streamlit as st
from components.data_fetcher import fetch_data
import pandas as pd


def main():
    st.title("Most Common Job Titles")
    job_titles = fetch_data("common-job-titles")
    if job_titles:
        df = pd.DataFrame(job_titles)
        st.dataframe(df)


if __name__ == "__main__":
    main()
