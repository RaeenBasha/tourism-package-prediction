import os
import pandas as pd
from sklearn.model_selection import train_test_split

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(PROJECT_DIR, "data", "tourism.csv")

data = pd.read_csv(DATA_PATH)

# Remove unnecessary identifier/index columns
data = data.drop(columns=["Unnamed: 0", "CustomerID"], errors="ignore")

# Standardize inconsistent gender value
if "Gender" in data.columns:
    data["Gender"] = data["Gender"].replace({"Fe Male": "Female"})

# Separate features and target
X = data.drop(columns=["ProdTaken"])
y = data["ProdTaken"]

# Create train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# Save train/test datasets
X_train.to_csv("Xtrain.csv", index=False)
X_test.to_csv("Xtest.csv", index=False)
y_train.to_csv("ytrain.csv", index=False)
y_test.to_csv("ytest.csv", index=False)

print("Data preparation completed successfully.")
print(f"Training records: {len(X_train)}")
print(f"Testing records: {len(X_test)}")
print("Train/test files created successfully.")
