
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

st.write("Enter customer details below:")

# Customer input fields
age = st.number_input("Age", min_value=18, max_value=100, value=35)

type_of_contact = st.selectbox(
    "Type of Contact",
    ["Self Enquiry", "Company Invited"]
)

city_tier = st.selectbox("City Tier", [1, 2, 3])

duration_of_pitch = st.number_input(
    "Duration of Pitch",
    min_value=0.0,
    value=15.0
)

occupation = st.selectbox(
    "Occupation",
    ["Salaried", "Small Business", "Large Business", "Free Lancer"]
)

gender = st.selectbox("Gender", ["Male", "Female"])

number_of_person_visiting = st.number_input(
    "Number of Persons Visiting",
    min_value=1,
    value=2
)

number_of_followups = st.number_input(
    "Number of Follow-ups",
    min_value=0.0,
    value=3.0
)

product_pitched = st.selectbox(
    "Product Pitched",
    ["Basic", "Deluxe", "Standard", "Super Deluxe", "King"]
)

preferred_property_star = st.number_input(
    "Preferred Property Star",
    min_value=1.0,
    max_value=5.0,
    value=3.0
)

marital_status = st.selectbox(
    "Marital Status",
    ["Married", "Unmarried", "Divorced"]
)

number_of_trips = st.number_input(
    "Number of Trips",
    min_value=0.0,
    value=3.0
)

passport = st.selectbox("Passport", [0, 1])

pitch_satisfaction_score = st.number_input(
    "Pitch Satisfaction Score",
    min_value=1,
    max_value=5,
    value=3
)

own_car = st.selectbox("Own Car", [0, 1])

number_of_children_visiting = st.number_input(
    "Number of Children Visiting",
    min_value=0.0,
    value=1.0
)

designation = st.selectbox(
    "Designation",
    ["Executive", "Manager", "Senior Manager", "AVP", "VP"]
)

monthly_income = st.number_input(
    "Monthly Income",
    min_value=0.0,
    value=20000.0
)

# Store user inputs in a DataFrame
input_data = pd.DataFrame({
    "Age": [age],
    "TypeofContact": [type_of_contact],
    "CityTier": [city_tier],
    "DurationOfPitch": [duration_of_pitch],
    "Occupation": [occupation],
    "Gender": [gender],
    "NumberOfPersonVisiting": [number_of_person_visiting],
    "NumberOfFollowups": [number_of_followups],
    "ProductPitched": [product_pitched],
    "PreferredPropertyStar": [preferred_property_star],
    "MaritalStatus": [marital_status],
    "NumberOfTrips": [number_of_trips],
    "Passport": [passport],
    "PitchSatisfactionScore": [pitch_satisfaction_score],
    "OwnCar": [own_car],
    "NumberOfChildrenVisiting": [number_of_children_visiting],
    "Designation": [designation],
    "MonthlyIncome": [monthly_income]
})

st.write("Customer input data:")
st.dataframe(input_data)
