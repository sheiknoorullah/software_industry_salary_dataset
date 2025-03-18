import pandas as pd
import os


def load_dataframe(filepath=None):
    """Loads the software industry salary dataset."""
    if filepath is None:
        # Construct the absolute path to the dataset
        # This works regardless of the current working directory
        dataset_path = os.path.join(os.path.dirname(
            # Path to data_loader.py's directory
            os.path.dirname(os.path.abspath(__file__))
            ),  # Go up one level to the backend directory
            'data',
            'software_industry_salary_dataset.csv'
        )
    else:
        dataset_path = filepath  # Use the provided filepath if given

    df = None
    try:
        df = pd.read_csv(dataset_path)
        # print("Dataset loaded successfully")  # Debugging print
        return df
    except FileNotFoundError:
        # Debugging print
        print(f"Error: Dataset file not found at {dataset_path}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")  # Debugging print
        return None