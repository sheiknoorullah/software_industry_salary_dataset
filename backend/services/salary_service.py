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


def get_most_common_job_titles(limit: int = 10):
    """
    Retrieves the most common job titles.
    """
    df = load_dataframe()

    if df is None:
        return {}

    # Count the occurrences of each job title
    job_title_counts = df['Job Title'].value_counts().reset_index().head(limit)
    job_title_counts.columns = ["Job Title", "Count"]

    return job_title_counts.to_dict(orient='records')
