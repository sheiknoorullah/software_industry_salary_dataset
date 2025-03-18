import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pandas as pd
from utils.data_loader import load_dataframe
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score, precision_score, recall_score, f1_score
import pickle
import numpy as np


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


def prepare_data_for_prediction():
    """
    Prepares the data for salary prediction by performing feature engineering.
    """
    df = load_dataframe()
    df.rename(columns={'Job Title': 'Job_Title',
              'Employment Status': 'Employment_Status'}, inplace=True)


    if df is None:
        return None

    # Company Ratings: Convert to numerical
    df['Rating'] = pd.to_numeric(df['Rating'], errors='coerce')

    # Define categorical and numerical features
    categorical_features = ['Job_Title', 'Location', 'Employment_Status']
    numerical_features = ['Rating']

    # Create transformers for preprocessing
    numeric_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='mean')),
        ('scaler', StandardScaler())
    ])

    categorical_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('onehot', OneHotEncoder(handle_unknown='ignore'))
    ])

    # Create preprocessor
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numeric_transformer, numerical_features),
            ('cat', categorical_transformer, categorical_features)
        ])

    # Separate features and target variable
    X = df.drop("Salary", axis=1)
    y = df["Salary"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42)

    # Preprocess the data
    X_train_processed = preprocessor.fit_transform(X_train)
    X_test_processed = preprocessor.transform(X_test)


    return X_train_processed, X_test_processed, y_train, y_test, preprocessor


def train_and_evaluate_models():
    """
    Trains Linear Regression and Logistic Regression models and evaluates their performance.
    """
    X_train, X_test, y_train, y_test, preprocessor = prepare_data_for_prediction()

    if X_train is None:
        return None

    # --- Linear Regression ---
    linear_model = LinearRegression()
    linear_model.fit(X_train, y_train)
    y_pred_linear = linear_model.predict(X_test)
 
    rmse_linear = np.sqrt(mean_squared_error(y_test, y_pred_linear))
    r2_linear = r2_score(y_test, y_pred_linear)
    print("--- Linear Regression ---")
    print(f"RMSE: {rmse_linear}")
    print(f"R-squared: {r2_linear}")

    
    # Save the models and preprocessor
    models = {
        'linear_model': linear_model,
    }

    with open('salary_prediction_models.pkl', 'wb') as file:
        pickle.dump(models, file)
    with open('salary_prediction_preprocessor.pkl', 'wb') as file:
        pickle.dump(preprocessor, file)

    return models, preprocessor


def get_predict_salary_linear(input_data, preprocessor, linear_model):
    """Predicts salary using Linear Regression."""
    try:
        input_df = pd.DataFrame([input_data])
        processed_input = preprocessor.transform(input_df)
        print(input_df)
        prediction = linear_model.predict(processed_input)[0]
        return {"predicted_salary": prediction}
    except Exception as e:
        print(e)
        raise Exception(str(e))


if __name__ == "__main__":
    train_and_evaluate_models()
