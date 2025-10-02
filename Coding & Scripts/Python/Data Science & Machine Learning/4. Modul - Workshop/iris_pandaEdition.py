import pandas as pd
import matplotlib.pyplot as plt

# Load the Iris dataset from a URL
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
# Define column names for the dataset
column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
# Read the dataset into a pandas DataFrame
iris_df = pd.read_csv(url, names=column_names)

# Display the first few rows of the dataset
print("First 5 rows of the Iris dataset:")
print(iris_df.head())

# Display basic information about the dataset
print("\nInformation about the Iris dataset:")
print(iris_df.info())

# Display descriptive statistics of the dataset
print("\nDescriptive statistics of the Iris dataset:")
print(iris_df.describe())

# Group by class and calculate the mean of each feature
print("\nMean of each feature by class:")
print(iris_df.groupby('class').mean())

# Plotting
# Pairplot to visualize the relationships between features
import seaborn as sns

sns.pairplot(iris_df, hue='class', markers=['o', 's', 'D'])
plt.title('Pairplot of Iris Dataset')
plt.show()

# Boxplot to visualize the distribution of each feature by class
plt.figure(figsize=(10, 6))
for i, column in enumerate(iris_df.columns[:-1]):
    plt.subplot(2, 2, i+1)
    sns.boxplot(x='class', y=column, data=iris_df)
    plt.title(f'{column} distribution by class')
plt.tight_layout()
plt.show()
