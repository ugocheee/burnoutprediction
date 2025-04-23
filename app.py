import streamlit as st
import numpy as np

st.markdown("""
    <style>
    /* Target the filled track of the slider */
    div[data-baseweb="slider"] .rc-slider-track {
        background-color: #1f77b4 !important;
    }

    /* Target the slider handle */
    div[data-baseweb="slider"] .rc-slider-handle {
        background-color: #1f77b4 !important;
        border: 2px solid #1f77b4 !important;
    }

    /* Target the unfilled track */
    div[data-baseweb="slider"] .rc-slider-rail {
        background-color: #e0f0ff !important;
    }
    </style>
""", unsafe_allow_html=True)


st.title("Jaguar is here to help")
st.subheader("Enter team member information")

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


st.subheader("Jaguar by Ugochi")
