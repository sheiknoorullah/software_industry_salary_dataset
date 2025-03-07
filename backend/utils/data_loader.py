import pandas as pd


def load_dataframe(filepath="data/software_industry_salary_dataset.csv"):
    df = None
    try:
        df = pd.read_csv(filepath)
        return df
    except FileNotFoundError:
        return df