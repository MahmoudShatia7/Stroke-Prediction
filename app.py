import streamlit as st
import pandas as pd
import numpy as np
from joblib import load  
from sklearn.preprocessing import LabelEncoder

# Function to load the model (without caching decorator for troubleshooting)
def load_model():
    return load("best_model.joblib")  # Ensure the model file is in the same directory

# Load the model
model = load_model()

# Streamlit app title
st.title("Stroke Prediction App")
st.write("This app predicts the likelihood of a stroke based on user inputs.")

# Sidebar for user input features
st.sidebar.header("User Input Features")

def get_user_input():
    """
    Capture user inputs via the Streamlit sidebar and return a structured dictionary.
    """
    gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
    age = st.sidebar.slider("Age", 0, 120, 30)
    hypertension = st.sidebar.selectbox("Hypertension (1 = Yes, 0 = No)", [0, 1])
    heart_disease = st.sidebar.selectbox("Heart Disease (1 = Yes, 0 = No)", [0, 1])
    ever_married = st.sidebar.selectbox("Ever Married", ["Yes", "No"])
    work_type = st.sidebar.selectbox(
        "Work Type", 
        ["Private", "Self-employed", "Govt_job", "Children", "Never_worked"]
    )
    residence_type = st.sidebar.selectbox("Residence Type", ["Urban", "Rural"])
    avg_glucose_level = st.sidebar.slider("Average Glucose Level", 50.0, 300.0, 100.0)
    bmi = st.sidebar.slider("BMI", 10.0, 100.0, 20.0)
    smoking_status = st.sidebar.selectbox(
        "Smoking Status", ["never smoked", "formerly smoked", "smokes", "Unknown"]
    )

    def categorize_age(age):
        if age < 12:
            return "Child"
        elif 12 <= age < 19:
            return "Teenager"
        elif 19 <= age < 35:
            return "Young Adult"
        elif 35 <= age < 50:
            return "Middle-aged Adult"
        else:
            return "Senior"

    def categorize_glucose_level(glucose_level):
        if glucose_level < 70:
            return "Low"
        elif 70 <= glucose_level <= 99:
            return "Normal"
        elif 100 <= glucose_level <= 125:
            return "Prediabetes"
        else:
            return "Diabetes"

    age_category = categorize_age(age)
    glucose_level_category = categorize_glucose_level(avg_glucose_level)
    has_diabetes = 1 if glucose_level_category == "Diabetes" else 0

    input_data = {
        "gender": gender,
        "age": age,
        "hypertension": hypertension,
        "heart_disease": heart_disease,
        "ever_married": ever_married,
        "work_type": work_type,
        "Residence_type": residence_type,
        "bmi": bmi,
        "smoking_status": smoking_status,
        "age_category": age_category,
        "glucose_level_category": glucose_level_category,
        "has_diabetes": has_diabetes,
    }

    return input_data

# Get user input
user_input = get_user_input()
input_df = pd.DataFrame([user_input])

# Display user input
st.subheader("User Input:")
st.write(input_df)

# Preprocessing: Encode categorical variables if necessary
def preprocess_input_data(input_df):
    # Initialize LabelEncoder for categorical variables
    le = LabelEncoder()

    input_df['gender'] = le.fit_transform(input_df['gender'])
    input_df['ever_married'] = le.fit_transform(input_df['ever_married'])
    input_df['work_type'] = le.fit_transform(input_df['work_type'])
    input_df['Residence_type'] = le.fit_transform(input_df['Residence_type'])
    input_df['smoking_status'] = le.fit_transform(input_df['smoking_status'])
    input_df['age_category'] = le.fit_transform(input_df['age_category'])
    input_df['glucose_level_category'] = le.fit_transform(input_df['glucose_level_category'])

    return input_df

# Apply preprocessing
input_df = preprocess_input_data(input_df)

# Prediction logic
if st.button("Predict"):
    prediction = model.predict(input_df)
    prediction_proba = model.predict_proba(input_df)

    st.subheader("Prediction")
    st.write("Stroke" if prediction[0] == 1 else "No Stroke")

    st.subheader("Prediction Probability")
    st.write(f"Probability of Stroke: {prediction_proba[0][1]:.2f}")
    st.write(f"Probability of No Stroke: {prediction_proba[0][0]:.2f}")
