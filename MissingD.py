import pandas as pd
import numpy as np

# Load dataset
data = pd.read_csv("data.csv")

# Check missing values
print("Missing values in each column:")
print(data.isnull().sum())

# Fill missing numerical values with mean
data["Age"].fillna(data["Age"].mean(), inplace=True)

# Fill missing categorical values with mode
data["Gender"].fillna(data["Gender"].mode()[0], inplace=True)

# Replace missing values with a constant
data["City"].fillna("Unknown", inplace=True)

# Drop rows with missing values
data = data.dropna()

print("\nDataset after handling missing values:")
print(data.head())