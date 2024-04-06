import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from statsmodels.tsa.seasonal import seasonal_decompose

# Load your data
train_data = pd.read_csv("KDDTrain+.txt")
test_data = pd.read_csv("KDDTest+.txt")

# Preprocess your data (e.g., handle missing values, encode categorical variables)
# For clustering, you might need to encode categorical variables if present and handle missing values.

# Perform clustering
X_train = train_data.drop(columns=["label"])  # Assuming "label" is the target variable
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)

# Choose the number of clusters
k = 5
kmeans = KMeans(n_clusters=k, random_state=42)
clusters = kmeans.fit_predict(X_train_scaled)

# Perform dimensionality reduction for visualization
pca = PCA(n_components=2)
X_train_pca = pca.fit_transform(X_train_scaled)

# Visualize clusters
plt.scatter(X_train_pca[:, 0], X_train_pca[:, 1], c=clusters, cmap='viridis')
plt.title("Cluster Visualization")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.colorbar(label="Cluster")
plt.show()

# Perform time series analysis (assuming you have time series data)
# For example, you can decompose the time series into trend, seasonal, and residual components
time_series_data = train_data[['timestamp', 'value_column']]  # Adjust column names accordingly
time_series_data['timestamp'] = pd.to_datetime(time_series_data['timestamp'])
time_series_data.set_index('timestamp', inplace=True)

# Decompose the time series
decomposition = seasonal_decompose(time_series_data['value_column'], model='additive', period=12)  # Adjust the period as needed
trend = decomposition.trend
seasonal = decomposition.seasonal
residual = decomposition.resid

# Plot the decomposed components
plt.figure(figsize=(10, 8))
plt.subplot(411)
plt.plot(time_series_data, label='Original', color='blue')
plt.legend(loc='best')
plt.subplot(412)
plt.plot(trend, label='Trend', color='blue')
plt.legend(loc='best')
plt.subplot(413)
plt.plot(seasonal, label='Seasonality', color='blue')
plt.legend(loc='best')
plt.subplot(414)
plt.plot(residual, label='Residuals', color='blue')
plt.legend(loc='best')
plt.tight_layout()
plt.show()
