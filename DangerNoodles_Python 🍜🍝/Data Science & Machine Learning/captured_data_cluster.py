import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Read the captured file into a DataFrame
# Replace 'captured_data.csv' with the path to your captured file
df = pd.read_csv('captured_data.csv')

# Assuming your data has columns including 'Timestamp' and 'Protocol'
# Adjust column names accordingly
data = df[['Timestamp', 'Protocol']]

# Convert protocol types to numerical values using one-hot encoding
data_encoded = pd.get_dummies(data)

# Perform K-means clustering
kmeans = KMeans(n_clusters=3)  # You can adjust the number of clusters as needed
kmeans.fit(data_encoded)

# Add cluster labels to the DataFrame
data['Cluster'] = kmeans.labels_

# Plot clusters
plt.scatter(data['Timestamp'], data['Protocol'], c=data['Cluster'], cmap='viridis')
plt.xlabel('Timestamp')
plt.ylabel('Protocol')
plt.title('Clustering based on Protocol Type')
plt.show()