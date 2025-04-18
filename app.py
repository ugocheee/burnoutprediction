
import streamlit as st
import numpy as np

st.title("Employee Burnout Predictor (Real Model)")

fatigue = st.slider("Mental Fatigue Score", 0.0, 10.0, 5.0)
resources = st.slider("Resource Allocation", 1, 10, 5)
designation = st.selectbox("Designation Level", [0, 1, 2, 3, 4, 5])
wfh = st.selectbox("WFH Setup Available", ["Yes", "No"])
company_type = st.selectbox("Company Type", ["Product", "Service"])
gender = st.selectbox("Gender", ["Male", "Female"])
years = st.slider("Years in Current Company", 0.0, 20.0, 5.0)

# Burnout prediction using real model coefficients from R
burn_rate = (
    -0.1031
    + 0.0068 * (1 if gender == "Male" else 0)
    + 0.00003 * (1 if company_type == "Service" else 0)
    - 0.0171 * (1 if wfh == "Yes" else 0)
    + 0.00896 * designation
    + 0.0309 * resources
    + 0.0672 * fatigue
    + 0.00108 * years
)

# Cap prediction between 0 and 1
burn_rate = min(max(burn_rate, 0), 1)

st.subheader(f"Predicted Burn Rate: {round(burn_rate, 2)}")
