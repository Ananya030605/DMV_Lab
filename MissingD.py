import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------------
# 1. Load Dataset
# -------------------------------
df = pd.read_csv("data.csv", sep=",")

print("Original Dataset:\n", df.head())
print(df.columns)
# -------------------------------
# 2. Missing Values Detection
# -------------------------------
print("\nMissing Values Before:\n")
print(df.isnull().sum())

# -------------------------------
# 3. Handle Missing Values
# -------------------------------

# Numerical columns → median
df['Age'].fillna(df['Age'].median(), inplace=True)
df['Salary'].fillna(df['Salary'].median(), inplace=True)

# Categorical columns → mode
df['Gender'].fillna(df['Gender'].mode()[0], inplace=True)
df['Department'].fillna(df['Department'].mode()[0], inplace=True)

print("\nMissing Values After:\n")
print(df.isnull().sum())

# -------------------------------
# 4. Outlier Detection (IQR)
# -------------------------------
def detect_outliers(column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    outliers = df[(df[column] < lower) | (df[column] > upper)]
    return outliers

print("\nOutliers in Age:\n", detect_outliers("Age"))
print("\nOutliers in Salary:\n", detect_outliers("Salary"))

# -------------------------------
# 5. BAR CHART (Department)
# -------------------------------
plt.figure(figsize=(6,4))
df['Department'].value_counts().plot(kind='bar', color='skyblue')
plt.title("Employee Count by Department")
plt.xlabel("Department")
plt.ylabel("Count")
plt.show()

# -------------------------------
# 6. PIE CHART (Gender)
# -------------------------------
plt.figure(figsize=(5,5))
df['Gender'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title("Gender Distribution")
plt.ylabel("")
plt.show()

# -------------------------------
# 7. STEP / STAIR CHART (Salary)
# -------------------------------
plt.figure(figsize=(8,4))
sorted_salary = df['Salary'].sort_values()
plt.step(range(len(sorted_salary)), sorted_salary, where='mid')
plt.title("Step Chart of Salary")
plt.xlabel("Index")
plt.ylabel("Salary")
plt.show()

# -------------------------------
# 8. BOXPLOT (Outliers Visualization)
# -------------------------------
plt.figure(figsize=(6,4))
sns.boxplot(data=df[['Age','Salary']])
plt.title("Boxplot for Outliers")
plt.show()

df.to_csv("cleaned_data.csv", index=False)

print("\n✅ Cleaned dataset saved as 'cleaned_data.csv'")
