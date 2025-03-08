import streamlit as st
from components.data_fetcher import fetch_data
import pandas as pd
import plotly.express as px


def main():
    st.title("Salary Trends by Location")
    trends = fetch_data("salary-trends-by-location")
    if trends:
        df = pd.DataFrame(trends)
        st.dataframe(df)
        fig = px.bar(df, x="Location", y="Average Salary")
        st.plotly_chart(fig)


if __name__ == "__main__":
    main()
