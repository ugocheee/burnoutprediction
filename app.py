import streamlit as st
import numpy as np

# Page Config
st.set_page_config(page_title="Jaguar by Ugochi", page_icon="🐆", layout="centered")

# Custom CSS Styling
st.markdown("""
    <style>
    .main {
        background-color: #f7f9fb;
        padding: 2rem;
        border-radius: 10px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }
    .stSlider > div[data-baseweb="slider"] {
        color: #e63946;
    }
    h1 {
        text-align: center;
        color: #264653;
        font-family: 'Trebuchet MS', sans-serif;
    }
    h3 {
        color: #1d3557;
        margin-top: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1>🐆 Jaguar by Ugochi</h1>", unsafe_allow_html=True)

# Input Form Layout
with st.container():
    fatigue = st.slider("🧠 Mental Fatigue Score", 0.0, 10.0, 5.0)
    resources = st.slider("📊 Resource Allocation", 1, 10, 5)
    designation = st.selectbox("🎓 Designation Level", [0, 1, 2, 3, 4, 5])
    wfh = st.selectbox("🏡 WFH Setup Available", ["Yes", "No"])
    company_type = st.selectbox("🏢 Company Type", ["Product", "Service"])
    gender = st.selectbox("🧍 Gender", ["Male", "Female"])
    years = st.slider("📅 Years in Current Company", 0.0, 20.0, 5.0)

# Burnout Prediction Logic
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
burn_rate = min(max(burn_rate, 0), 1)

# Output Result
st.markdown(f"<h3>🔥 Predicted Burn Rate: <span style='color:#e63946'>{round(burn_rate, 2)}</span></h3>", unsafe_allow_html=True)
