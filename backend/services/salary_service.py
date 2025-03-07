import pandas as pd
from utils.data_loader import load_dataframe


def get_high_paying_companies(limit):
    """
    Retrieves the companies with the highest average salaries.
    """
    df = load_dataframe()

    # Group by company and calculate the mean salary
    if df is None:
        return {}

    company_salaries = df.groupby('Company Name')[
        'Salary'].mean().sort_values(ascending=False).reset_index().head(limit)
    company_salaries.columns = [
        "Company Name", "Average Salary"]

    # Convert to a dictionary for easy API response
    high_paying_companies = company_salaries.to_dict(orient="records")
    return high_paying_companies
