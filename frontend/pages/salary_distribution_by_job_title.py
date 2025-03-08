import streamlit as st
from components.data_fetcher import fetch_data
import pandas as pd
import plotly.express as px


def main():
    st.title("Salary Distribution by Job Title")
    distribution = fetch_data("salary-distribution-by-job-title")
    if distribution:
        df = pd.DataFrame(distribution)
        st.dataframe(df)
        fig = px.bar(df, x="Job Title", y="Average Salary")
        st.plotly_chart(fig)


if __name__ == "__main__":
    main()
