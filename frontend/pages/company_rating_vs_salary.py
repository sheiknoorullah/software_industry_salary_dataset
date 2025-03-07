import streamlit as st
from components.data_fetcher import fetch_data
import pandas as pd


def main():
    st.title("Company Rating vs. Salary")
    results = fetch_data("salary-by-company-rating")
    if results:
        df = pd.DataFrame(results)
        st.dataframe(df)


if __name__ == "__main__":
    main()
