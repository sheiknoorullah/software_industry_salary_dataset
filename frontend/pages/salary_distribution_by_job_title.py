import streamlit as st
from components.data_fetcher import fetch_data
import pandas as pd


def main():
    st.title("Salary Distribution by Job Title")
    distribution = fetch_data("salary-distribution-by-job-title")
    if distribution:
        df = pd.DataFrame(distribution)
        st.dataframe(df)


if __name__ == "__main__":
    main()
