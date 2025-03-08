import streamlit as st
from components.data_fetcher import fetch_data
import pandas as pd
import plotly.express as px


def main():
    st.title("Employment Status and Salary")
    relationship = fetch_data("employment-status-and-salary")
    if relationship:
        df = pd.DataFrame(relationship)
        st.dataframe(df)
        fig = px.bar(df, x="Employment Status", y="Average Salary")
        st.plotly_chart(fig)


if __name__ == "__main__":
    main()
