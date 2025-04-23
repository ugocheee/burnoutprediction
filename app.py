import streamlit as st
import numpy as np

# Add this near the top of your Streamlit script (after imports)
st.markdown("""
    <style>
    /* Change slider color */
    .stSlider > div[data-baseweb="slider"] .css-14g5kz0 {
        background: #1f77b4;  /* Blue track color */
    }
    .stSlider > div[data-baseweb="slider"] .css-1lv4goc {
        background-color: #1f77b4 !important; /* Blue handle */
    }
    .stSlider > div[data-baseweb="slider"] .css-1r6slb0 {
        background-color: #1f77b4; /* Active range */
    }
    </style>
""", unsafe_allow_html=True)

st.title("Jaguar by Ugochi")

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

# Scale to 0–10 range for easier interpretation
burn_score = round(burn_rate * 10, 2)

# Display appropriate message
if burn_score <= 4.5:
    message = f"🔥 Predicted Burn Rate: {burn_score}\n\n✅ You should be good. No signs of burnout."
elif 4.5 < burn_score <= 6.5:
    message = f"🔥 Predicted Burn Rate: {burn_score}\n\n⚠️ Watch out. This employee may be at risk. Take action soon."
else:
    message = f"🔥 Predicted Burn Rate: {burn_score}\n\n🚨 Take action today. This employee is burned out!"

st.subheader(message)
