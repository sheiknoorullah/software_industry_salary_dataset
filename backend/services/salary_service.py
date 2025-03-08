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


def get_salary_trends_by_location():
    """
    Retrieves salary trends by location.
    """
    df = load_dataframe()

    if df is None:
        return {}

    # Calculate the average salary for each location
    location_salaries = df.groupby('Location')['Salary'].mean().reset_index()
    location_salaries.columns = ["Location", "Average Salary"]

    return location_salaries.to_dict(orient='records')


def get_salary_by_company_rating():
    """
    Retrieves the average salary for each company rating.
    """
    df = load_dataframe()

    if df is None:
        return {}

    salary_by_rating = (
        df.groupby("Rating")["Salary"]
        .mean()
        .reset_index()
    )
    salary_by_rating.columns = ["Company Rating", "Average Salary"]

    return salary_by_rating.to_dict(orient='records')


def get_salary_distribution_by_job_title(limit: int = 10):
    """
    Retrieves the salary distribution by job title.
    """
    df = load_dataframe()

    if df is None:
        return {}

    # Calculate the average salary for each job title
    salary_by_job_title = (
        df.groupby("Job Title")["Salary"]
        .mean().sort_values(ascending=False).head(limit)
        .reset_index()
    )
    salary_by_job_title.columns = ["Job Title", "Average Salary"]

    return salary_by_job_title.to_dict(orient='records')


def get_employment_status_and_salary():
    """
    Retrieves the relationship between employment status and salary.
    """
    df = load_dataframe()

    if df is None:
        return {}

    # Calculate the average salary for each employment status
    salary_by_employment_status = (
        df.groupby("Employment Status")["Salary"]
        .mean()
        .reset_index()
    )
    salary_by_employment_status.columns = [
        "Employment Status", "Average Salary"]

    return salary_by_employment_status.to_dict(orient='records')


def get_salary_report_frequency():
    """
    Retrieves the most frequently reported salary values.
    """
    df = load_dataframe()

    if df is None:
        return {}

    # Calculate the frequency of each salary value
    salary_frequency = df["Salary"].value_counts().reset_index()
    salary_frequency.columns = ["Salary", "Frequency"]

    return salary_frequency.to_dict(orient='records')
