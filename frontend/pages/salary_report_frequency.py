import streamlit as st
from components.data_fetcher import fetch_data
import pandas as pd


def main():
    st.title("Salary Report Frequency")
    frequency = fetch_data("salary-report-frequency")
    if frequency:
        df = pd.DataFrame(frequency)
        st.dataframe(df)


if __name__ == "__main__":
    main()
