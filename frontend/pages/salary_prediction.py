import streamlit as st
import requests
import pandas as pd


def main():
    st.title("Salary Prediction")

    # Input form
    with st.form("prediction_form"):
        rating = st.number_input(
            "Company Rating", min_value=1.0, max_value=5.0, step=0.1)
        job_title = st.text_input("Job Title")
        location = st.text_input("Location")
        employment_status = st.selectbox(
            "Employment Status", ["Full-time", "Part-time"])
        model_choice = st.radio("Prediction Model", [
                                "Linear Regression", "Logistic Regression"])
        submit_button = st.form_submit_button("Predict Salary")

    if submit_button:
        # Prepare input data
        input_data = {
            "Rating": rating,
            "Job_Title": job_title,
            "Location": location,
            "Employment_Status": employment_status
        }

        # Make API call
        if model_choice == "Linear Regression":
            response = requests.post(
                "http://localhost:8000/predict_salary_linear", json=input_data)
        else:
            response = requests.post(
                "http://localhost:8000/predict_salary_logistic", json=input_data)

        # Display results
        if response.status_code == 200:
            result = response.json()
            if model_choice == "Linear Regression":
                st.success(
                    f"Predicted Salary: ₹{result['predicted_salary']:.2f}")
            else:
                st.success(
                    f"Predicted Salary Category: {result['predicted_category']}")
        else:
            st.error(f"Error: {response.status_code} - {response.text}")


if __name__ == "__main__":
    main()


    
# def main():
#     st.title("Salary Prediction")

#     # Input form
#     with st.form("prediction_form"):
#         rating = st.number_input(
#             "Company Rating", min_value=1.0, max_value=5.0, step=0.1)
#         job_title = st.text_input("Job Title")
#         location = st.text_input("Location")
#         employment_status = st.selectbox(
#             "Employment Status", ["Full-time", "Part-time"])
#         model_choice = st.radio("Prediction Model", [
#                                 "Linear Regression", "Logistic Regression"])
#         submit_button = st.form_submit_button("Predict Salary")

#     if submit_button:
#         # Placeholder for API call and prediction display
#         st.write("Prediction in progress...")


# if __name__ == "__main__":
#     main()
