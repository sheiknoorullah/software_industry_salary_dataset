import streamlit as st
from components.data_fetcher import fetch_data
import pandas as pd


def main():
    st.title("Salary Trends by Location")
    trends = fetch_data("salary-trends-by-location")
    if trends:
        df = pd.DataFrame(trends)
        st.dataframe(df)


if __name__ == "__main__":
    main()
