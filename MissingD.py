import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans

# Load dataset
df = pd.read_csv("data.csv", sep=",")

print("Original Dataset:\n", df.head())
print(df.columns)

print("\nMissing Values Before:\n")
print(df.isnull().sum())

# Handling missing values
df['Age'] = df['Age'].fillna(df['Age'].median())
df['Salary'] = df['Salary'].fillna(df['Salary'].median())

df['Gender'] = df['Gender'].fillna(df['Gender'].mode()[0])
df['Department'] = df['Department'].fillna(df['Department'].mode()[0])

print("\nMissing Values After:\n")
print(df.isnull().sum())

# -------------------------------
# OUTLIER DETECTION FUNCTION
# -------------------------------
def detect_outliers(data, column):
    Q1 = data[column].quantile(0.25)
    Q3 = data[column].quantile(0.75)
    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    return data[(data[column] < lower) | (data[column] > upper)]

print("\nOutliers in Age:\n", detect_outliers(df, "Age"))
print("\nOutliers in Salary:\n", detect_outliers(df, "Salary"))

# -------------------------------
# BASIC VISUALIZATIONS
# -------------------------------

# Bar chart
plt.figure(figsize=(6,4))
df['Department'].value_counts().plot(kind='bar', color='skyblue')
plt.title("Employee Count by Department")
plt.xlabel("Department")
plt.ylabel("Count")
plt.show()

# Pie chart
plt.figure(figsize=(5,5))
df['Gender'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title("Gender Distribution")
plt.ylabel("")
plt.show()

# Step chart
plt.figure(figsize=(8,4))
sorted_salary = df['Salary'].sort_values()
plt.step(range(len(sorted_salary)), sorted_salary, where='mid')
plt.title("Step Chart of Salary")
plt.xlabel("Index")
plt.ylabel("Salary")
plt.show()

# Boxplot
plt.figure(figsize=(6,4))
sns.boxplot(data=df[['Age','Salary']])
plt.title("Boxplot for Outliers")
plt.show()

# =====================================================
# 🔥 NEW SECTION: SCATTER PLOT (OUTLIERS + CLUSTERS + CORRELATION)
# =====================================================

# Correlation
corr = df['Age'].corr(df['Salary'])
print(f"\nCorrelation between Age and Salary: {corr:.2f}")

# Function to get bounds
def get_bounds(data, column):
    Q1 = data[column].quantile(0.25)
    Q3 = data[column].quantile(0.75)
    IQR = Q3 - Q1
    return Q1 - 1.5 * IQR, Q3 + 1.5 * IQR

age_lower, age_upper = get_bounds(df, 'Age')
sal_lower, sal_upper = get_bounds(df, 'Salary')

# Identify outliers
outliers = df[
    (df['Age'] < age_lower) | (df['Age'] > age_upper) |
    (df['Salary'] < sal_lower) | (df['Salary'] > sal_upper)
]

normal = df.drop(outliers.index)

# Scatter plot with outliers
plt.figure(figsize=(7,5))

plt.scatter(normal['Age'], normal['Salary'],
            color='blue', label='Normal', alpha=0.6)

plt.scatter(outliers['Age'], outliers['Salary'],
            color='red', label='Outliers', alpha=0.8)

plt.title("Scatter Plot (Outliers Highlighted)")
plt.xlabel("Age")
plt.ylabel("Salary")
plt.legend()
plt.show()

# -------------------------------
# CLUSTERING (K-Means)
# -------------------------------
X = df[['Age', 'Salary']]

kmeans = KMeans(n_clusters=3, random_state=42)
df['Cluster'] = kmeans.fit_predict(X)

plt.figure(figsize=(7,5))
sns.scatterplot(x='Age', y='Salary', hue='Cluster', palette='Set1', data=df)

plt.title("Scatter Plot with Clusters")
plt.show()

# -------------------------------
# REGRESSION LINE (CORRELATION VISUAL)
# -------------------------------
plt.figure(figsize=(7,5))
sns.regplot(x='Age', y='Salary', data=df)
plt.title("Scatter Plot with Regression Line")
plt.show()

# =====================================================

# Save cleaned dataset
df.to_csv("cleaned_data.csv", index=False)

print("\n✅ Cleaned dataset saved as 'cleaned_data.csv'")