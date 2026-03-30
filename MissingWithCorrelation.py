import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans

# -------------------------------
# LOAD DATA
# -------------------------------
df = pd.read_csv("data.csv")

print("Dataset Preview:\n", df.head())
print("\nMissing Values Before:\n", df.isnull().sum())

# -------------------------------
# HANDLE MISSING VALUES
# -------------------------------
num_cols = ['Age', 'Salary']
cat_cols = ['Gender', 'Department']

for col in num_cols:
    df[col].fillna(df[col].median(), inplace=True)

for col in cat_cols:
    df[col].fillna(df[col].mode()[0], inplace=True)

print("\nMissing Values After:\n", df.isnull().sum())

# -------------------------------
# OUTLIER FUNCTION
# -------------------------------
def get_outliers(data, col):
    Q1, Q3 = data[col].quantile([0.25, 0.75])
    IQR = Q3 - Q1
    low, high = Q1 - 1.5*IQR, Q3 + 1.5*IQR
    return data[(data[col] < low) | (data[col] > high)]

print("\nAge Outliers:\n", get_outliers(df, 'Age'))
print("\nSalary Outliers:\n", get_outliers(df, 'Salary'))

# -------------------------------
# BASIC VISUALS
# -------------------------------

# Bar
df['Department'].value_counts().plot(kind='bar', title="Department Count")
plt.show()

# Pie
df['Gender'].value_counts().plot(kind='pie', autopct='%1.1f%%', title="Gender Distribution")
plt.ylabel("")
plt.show()

# Boxplot
sns.boxplot(data=df[num_cols])
plt.title("Boxplot")
plt.show()

# -------------------------------
# CORRELATION + SCATTER
# -------------------------------
corr = df['Age'].corr(df['Salary'])
print(f"\nCorrelation: {corr:.2f}")

sns.scatterplot(x='Age', y='Salary', data=df)
plt.title("Scatter Plot")
plt.show()

# -------------------------------
# K-MEANS CLUSTERING
# -------------------------------
kmeans = KMeans(n_clusters=3, random_state=42)
df['Cluster'] = kmeans.fit_predict(df[['Age', 'Salary']])

sns.scatterplot(x='Age', y='Salary', hue='Cluster', data=df)
plt.title("Clusters")
plt.show()

# -------------------------------
# REGRESSION LINE
# -------------------------------
sns.regplot(x='Age', y='Salary', data=df)
plt.title("Regression Line")
plt.show()

# -------------------------------
# SAVE FILE
# -------------------------------
df.to_csv("cleaned_data.csv", index=False)
print("\n Cleaned dataset saved!")