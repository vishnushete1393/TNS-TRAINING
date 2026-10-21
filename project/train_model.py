import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import (
    OneHotEncoder,
    StandardScaler
)
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression

# -----------------------------------
# 1. Load Dataset
# -----------------------------------

df = pd.read_csv(
    "manufacturing_dataset_1000_samples.csv"
)

# -----------------------------------
# 2. Process Timestamp
# -----------------------------------

df["Timestamp"] = pd.to_datetime(
    df["Timestamp"],
    errors="coerce"
)

df["Hour"] = df["Timestamp"].dt.hour
df["Day"] = df["Timestamp"].dt.day
df["Month"] = df["Timestamp"].dt.month

df = df.drop(
    "Timestamp",
    axis=1
)

# -----------------------------------
# 3. Define Target
# -----------------------------------

X = df.drop(
    "Parts_Per_Hour",
    axis=1
)

y = df["Parts_Per_Hour"]

# -----------------------------------
# 4. Identify Columns
# -----------------------------------

categorical_columns = [
    "Shift",
    "Machine_Type",
    "Material_Grade",
    "Day_of_Week"
]

numerical_columns = [
    column
    for column in X.columns
    if column not in categorical_columns
]

print("Numerical Columns:")
print(numerical_columns)

print("\nCategorical Columns:")
print(categorical_columns)

# -----------------------------------
# 5. Numerical Pipeline
# -----------------------------------

numerical_pipeline = Pipeline(
    steps=[
        (
            "imputer",
            SimpleImputer(
                strategy="median"
            )
        ),
        (
            "scaler",
            StandardScaler()
        )
    ]
)

# -----------------------------------
# 6. Categorical Pipeline
# -----------------------------------

categorical_pipeline = Pipeline(
    steps=[
        (
            "imputer",
            SimpleImputer(
                strategy="most_frequent"
            )
        ),
        (
            "encoder",
            OneHotEncoder(
                handle_unknown="ignore"
            )
        )
    ]
)

# -----------------------------------
# 7. Preprocessor
# -----------------------------------

preprocessor = ColumnTransformer(
    transformers=[
        (
            "numerical",
            numerical_pipeline,
            numerical_columns
        ),
        (
            "categorical",
            categorical_pipeline,
            categorical_columns
        )
    ]
)

# -----------------------------------
# 8. Linear Regression Model
# -----------------------------------

model = Pipeline(
    steps=[
        (
            "preprocessor",
            preprocessor
        ),
        (
            "regression",
            LinearRegression()
        )
    ]
)

# -----------------------------------
# 9. Train-Test Split
# -----------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

print("\nTraining Records:", len(X_train))
print("Testing Records:", len(X_test))

# -----------------------------------
# 10. Train Model
# -----------------------------------

model.fit(
    X_train,
    y_train
)

print("\nModel trained successfully!")

# -----------------------------------
# 11. Predictions
# -----------------------------------

predictions = model.predict(
    X_test
)

print("\nFirst 10 Predictions:")

for actual, predicted in zip(
    y_test[:10],
    predictions[:10]
):
    print(
        "Actual:",
        round(actual, 2),
        "Predicted:",
        round(predicted, 2)
    )

# -----------------------------------
# 12. Save Model
# -----------------------------------

joblib.dump(
    model,
    "manufacturing_linear_regression.joblib"
)

print(
    "\nModel saved as "
    "manufacturing_linear_regression.joblib"
)