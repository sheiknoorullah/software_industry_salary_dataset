import streamlit as st
from components.data_fetcher import fetch_data
import pandas as pd


def main():
    st.title("Employment Status and Salary")
    relationship = fetch_data("employment-status-and-salary")
    if relationship:
        df = pd.DataFrame(relationship)
        st.dataframe(df)


if __name__ == "__main__":
    main()
