
import pandas as pd
import os

DATA_PATH = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "data",
    "tourism.csv"
)

EXPECTED_COLUMNS = [
    "CustomerID",
    "ProdTaken",
    "Age",
    "TypeofContact",
    "CityTier",
    "Occupation",
    "Gender",
    "NumberOfPersonVisiting",
    "PreferredPropertyStar",
    "MaritalStatus",
    "NumberOfTrips",
    "Passport",
    "OwnCar",
    "NumberOfChildrenVisiting",
    "Designation",
    "MonthlyIncome",
    "PitchSatisfactionScore",
    "ProductPitched",
    "NumberOfFollowups",
    "DurationOfPitch",
    "Unnamed: 0"
]

data = pd.read_csv(DATA_PATH)

missing_columns = [
    col for col in EXPECTED_COLUMNS
    if col not in data.columns
]

unexpected_columns = [
    col for col in data.columns
    if col not in EXPECTED_COLUMNS
]

validation_passed = (
    len(missing_columns) == 0
    and len(unexpected_columns) == 0
)

print("========== DATASET VALIDATION ==========")
print(f"Dataset path       : {DATA_PATH}")
print(f"Validation status  : {"PASSED" if validation_passed else "FAILED"}")

print("\n========== DATASET SUMMARY ==========")
print(f"Rows               : {data.shape[0]}")
print(f"Columns            : {data.shape[1]}")
print(f"Duplicate rows     : {data.duplicated().sum()}")

print("\n========== COLUMN VALIDATION ==========")
print(f"Expected columns   : {len(EXPECTED_COLUMNS)}")
print(f"Actual columns     : {len(data.columns)}")
print(f"Missing columns    : {missing_columns if missing_columns else 'None'}")
print(f"Unexpected columns : {unexpected_columns if unexpected_columns else 'None'}")

print("\n========== MISSING VALUE SUMMARY ==========")
print(f"Total missing values: {data.isnull().sum().sum()}")

print("\n========== TARGET DISTRIBUTION ==========")
print(data["ProdTaken"].value_counts())
print("\nTarget percentage:")
print((data["ProdTaken"].value_counts(normalize=True) * 100).round(2))

if not validation_passed:
    raise ValueError("Dataset validation failed. Please review the column differences above.")

print("\nDataset validation completed successfully.")
