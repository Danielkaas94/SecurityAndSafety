# Importing necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load dataset (example: Boston housing dataset)
# from sklearn.datasets import load_boston
# boston = load_boston()

from sklearn.datasets import fetch_california_housing
CaliforniaHousing = fetch_california_housing()
data = pd.DataFrame(CaliforniaHousing.data, columns=CaliforniaHousing.feature_names)
data['target'] = CaliforniaHousing.target

# Exploratory Data Analysis (EDA)
print(data.head())  # Display the first few rows of the dataset
print(data.describe())  # Summary statistics of the dataset

# Data Visualization
plt.figure(figsize=(10, 6))
sns.heatmap(data.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap')
plt.show()

# Splitting the dataset into training and testing sets
X = data.drop('target', axis=1)
y = data['target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model Training (Linear Regression)
model = LinearRegression()
model.fit(X_train, y_train)

# Model Evaluation
train_preds = model.predict(X_train)
test_preds = model.predict(X_test)
train_rmse = np.sqrt(mean_squared_error(y_train, train_preds))
test_rmse = np.sqrt(mean_squared_error(y_test, test_preds))
print("Train RMSE:", train_rmse)
print("Test RMSE:", test_rmse)
