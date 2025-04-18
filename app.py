
import streamlit as st
import numpy as np

st.title("Employee Burnout Predictor")

fatigue = st.slider("Mental Fatigue Score", 0.0, 10.0, 5.0)
resources = st.slider("Resource Allocation", 1, 10, 5)
designation = st.selectbox("Designation Level", [0, 1, 2, 3, 4, 5])
wfh = st.selectbox("WFH Setup Available", ["Yes", "No"])
company_type = st.selectbox("Company Type", ["Product", "Service"])
gender = st.selectbox("Gender", ["Male", "Female"])
years = st.slider("Years in Current Company", 0.0, 20.0, 5.0)

burn_rate = 0.1 + 0.03 * resources + 0.07 * fatigue + 0.009 * designation
if wfh == "No":
    burn_rate += 0.02
if gender == "Male":
    burn_rate += 0.005

# Cap burn rate between 0 and 1
burn_rate = min(max(burn_rate, 0), 1)

st.subheader(f"Predicted Burn Rate: {round(burn_rate, 2)}")
