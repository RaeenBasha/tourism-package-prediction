import os
import pandas as pd

# Locate the project directory relative to this script
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_PATH = os.path.join(
    PROJECT_DIR,
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

print("Starting dataset registration and validation...")
print(f"Dataset path: {DATA_PATH}")

if not os.path.exists(DATA_PATH):
    raise FileNotFoundError(
        f"Dataset not found at: {DATA_PATH}"
    )

data = pd.read_csv(DATA_PATH)

actual_columns = data.columns.tolist()

missing_columns = [
    column for column in EXPECTED_COLUMNS
    if column not in actual_columns
]

unexpected_columns = [
    column for column in actual_columns
    if column not in EXPECTED_COLUMNS
]

validation_passed = (
    len(missing_columns) == 0
    and len(unexpected_columns) == 0
)

print(f"Rows: {data.shape[0]}")
print(f"Columns: {data.shape[1]}")
print(f"Duplicate rows: {data.duplicated().sum()}")
print(f"Expected columns: {len(EXPECTED_COLUMNS)}")
print(f"Actual columns: {len(actual_columns)}")
print(f"Missing columns: {missing_columns if missing_columns else 'None'}")
print(f"Unexpected columns: {unexpected_columns if unexpected_columns else 'None'}")
print(f"Total missing values: {data.isnull().sum().sum()}")

print("\nProdTaken distribution:")
print(data["ProdTaken"].value_counts())

print("\nProdTaken percentage:")
print((data["ProdTaken"].value_counts(normalize=True) * 100).round(2))

if validation_passed:
    print("\nValidation status: PASSED")
else:
    print("\nValidation status: FAILED")
    raise ValueError(
        "Dataset validation failed. Please review the missing or unexpected columns."
    )

print("Dataset registration validation completed successfully.")
