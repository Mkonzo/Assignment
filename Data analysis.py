# data_analysis.py

import pandas as pd
import matplotlib.pyplot as plt

# 1. Load dataset
# You can change this to your dataset path
data = pd.read_csv('sample_data.csv')

# 2. Basic Exploration
print("First 5 rows:")
print(data.head())

print("\nSummary Statistics:")
print(data.describe())

print("\nMissing Values:")
print(data.isnull().sum())

# 3. Basic Analysis
# Example: Count of unique values in a column (adjust as needed)
print("\nValue counts for 'Category' column:")
if 'Category' in data.columns:
    print(data['Category'].value_counts())

# 4. Visualizations

# Histogram
data.hist(figsize=(10, 6))
plt.suptitle('Histogram of Numeric Features')
plt.tight_layout()
plt.show()

# Bar chart (if 'Category' column exists)
if 'Category' in data.columns:
    data['Category'].value_counts().plot(kind='bar')
    plt.title('Distribution of Categories')
    plt.xlabel('Category')
    plt.ylabel('Count')
    plt.show()

# 5. Observations
print("\nObservations:")
print("- Dataset has", data.shape[0], "rows and", data.shape[1], "columns.")
print("- Check for skewed distributions or outliers in histograms.")
print("- Categorical variable distributions visualized.")

