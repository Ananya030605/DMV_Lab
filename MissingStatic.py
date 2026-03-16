import pandas as pd

# Create dataset with missing values
data = {
    "Name": ["Ananya", "Rahul", "Priya", "Amit", "Riya"],
    "Age": [21, 23, None, 24, 22],
    "Gender": ["Female", "Male", "Female", None, "Female"],
    "City": ["Mumbai", "Delhi", "Kolkata", "Mumbai", None]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

# Fill missing numerical values with mean
df["Age"].fillna(df["Age"].mean(), inplace=True)

# Fill missing categorical values with mode
df["Gender"].fillna(df["Gender"].mode()[0], inplace=True)

# Fill missing city with constant value
df["City"].fillna("Unknown", inplace=True)

print("\nData after handling missing values:")
print(df)