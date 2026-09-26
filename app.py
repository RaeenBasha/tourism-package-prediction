
import streamlit as st
import pandas as pd
import joblib
import os

# Page configuration
st.set_page_config(
    page_title="Tourism Package Prediction",
    page_icon="🌴",
    layout="centered"
)

st.title("🌴 Tourism Package Prediction")
st.write(
    "Predict whether a customer is likely to purchase the Wellness Tourism Package."
)

# Load the trained model committed to the repository
MODEL_PATH = os.path.join(
    os.path.dirname(__file__),
    "model_building",
    "best_tourism_package_model.pkl"
)

@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)

model = load_model()

st.success("Trained XGBoost model loaded successfully.")

st.write("The trained model is ready for customer purchase prediction.")
