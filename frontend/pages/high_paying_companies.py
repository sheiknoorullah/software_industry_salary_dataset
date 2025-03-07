import streamlit as st
from components.data_fetcher import fetch_data

def main():
    st.title("Most High-Paying Companies")
    companies = fetch_data("high-paying-companies")
    if companies:
        st.table(companies)
        print((companies))

if __name__ == "__main__":
    main()