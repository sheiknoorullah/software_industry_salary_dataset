import requests
import streamlit as st
from utils.config import BACKEND_URL


def fetch_data(endpoint):
    """Fetches data from the FastAPI backend."""
    try:
        response = requests.get(f"{BACKEND_URL}/{endpoint}")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching data: {e}")
        return None