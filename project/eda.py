import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------------
# 1. Load Dataset
# -----------------------------------

df = pd.read_csv("manufacturing_dataset_1000_samples.csv")

print("First 5 rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nDataset Information:")
print(df.info())

# -----------------------------------
# 2. Check Missing Values
# -----------------------------------

print("\nMissing Values:")
print(df.isnull().sum())

# -----------------------------------
# 3. Statistical Summary
# -----------------------------------

print("\nStatistical Summary:")
print(df.describe())

# -----------------------------------
# 4. Process Timestamp
# -----------------------------------

df["Timestamp"] = pd.to_datetime(df["Timestamp"])

df["Hour"] = df["Timestamp"].dt.hour
df["Day"] = df["Timestamp"].dt.day
df["Month"] = df["Timestamp"].dt.month

# Remove original timestamp
df = df.drop("Timestamp", axis=1)

print("\nAfter Timestamp Processing:")
print(df.head())

# -----------------------------------
# 5. Handle Missing Values
# -----------------------------------

numeric_columns = df.select_dtypes(
    include=["int64", "float64"]
).columns

categorical_columns = df.select_dtypes(
    include=["object"]
).columns

# Numerical → Median
for column in numeric_columns:
    df[column] = df[column].fillna(df[column].median())

# Categorical → Mode
for column in categorical_columns:
    df[column] = df[column].fillna(df[column].mode()[0])

print("\nMissing Values After Processing:")
print(df.isnull().sum())

# -----------------------------------
# 6. Target Distribution
# -----------------------------------

plt.figure(figsize=(8, 5))

sns.histplot(
    df["Parts_Per_Hour"],
    kde=True
)

plt.title("Distribution of Parts Per Hour")
plt.xlabel("Parts Per Hour")
plt.ylabel("Frequency")

plt.show()

# -----------------------------------
# 7. Correlation Heatmap
# -----------------------------------

plt.figure(figsize=(12, 8))

correlation = df.select_dtypes(
    include=["int64", "float64"]
).corr()

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm"
)

plt.title("Feature Correlation Heatmap")

plt.show()

# -----------------------------------
# 8. Important Feature Relationships
# -----------------------------------

features = [
    "Injection_Temperature",
    "Injection_Pressure",
    "Cycle_Time",
    "Cooling_Time",
    "Efficiency_Score",
    "Machine_Utilization"
]

for feature in features:

    plt.figure(figsize=(7, 5))

    sns.scatterplot(
        x=df[feature],
        y=df["Parts_Per_Hour"]
    )

    plt.title(
        feature + " vs Parts Per Hour"
    )

    plt.xlabel(feature)
    plt.ylabel("Parts Per Hour")

    plt.show()

# -----------------------------------
# Save Processed Dataset
# -----------------------------------

df.to_csv(
    "processed_manufacturing_dataset.csv",
    index=False
)

print("\nProcessed dataset saved successfully!")