# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 21:16:37 2018

@author: sila
"""

from sklearn.datasets import make_moons;
from sklearn.cluster import KMeans # This will be used for the algorithm
import matplotlib.pyplot as plt 

# generate 2d classification dataset
X, y = make_moons(n_samples=100, noise=0.1)

from matplotlib import pyplot
from pandas import DataFrame
# generate 2d classification dataset
# X, y = make_moons(n_samples=100, noise=0.1)
X, y = make_moons(n_samples=1000, noise=0.1)
# scatter plot, dots colored by class value
df = DataFrame(dict(x=X[:,0], y=X[:,1], label=y))
colors = {0:'red', 1:'blue'}
fig, ax = pyplot.subplots()
grouped = df.groupby('label')
for key, group in grouped:
    group.plot(ax=ax, kind='scatter', x='x', y='y', label=key, color=colors[key])

pyplot.show()


k = 2 
#running kmeans clustering into two
kmeans = KMeans(n_clusters=k, random_state=0).fit(X)  
# the random state is optionlly, here it is specified so we get determistic clusters.
# this will contain the labels for our predicted clusters (either 0 or 1)   
labels = kmeans.labels_
# the centers of the calculated clusters
clusters = kmeans.cluster_centers_
# printing our cluster centers - there will be 2 of them.
print(clusters)

# need a new import
from matplotlib.colors import ListedColormap

# we define color lists to use with K values from 2 till 5
# the color values are simply RGB values, so the colormap for k = 2, will give red ($FF0000) and green ($00FF00) colors
cmap_bold = [ListedColormap(['#FF0000', '#00FF00']),
             ListedColormap(['#FF0000', '#00FF00', '#0000FF']),
             ListedColormap(['#FF0000', '#00FF00', '#0000FF', '#FFFF00']),
             ListedColormap(['#FF0000', '#00FF00', '#0000FF', '#FFFF00','#00FFFF']),
             ListedColormap(['#FF0000', '#00FF00', '#0000FF', '#FFFF00','#00FFFF', '#FF00FF']),
             ListedColormap(['#FF0000', '#00FF00', '#0000FF', '#FFFF00','#00FFFF', '#FF00FF', '#FF8000'])]

# now plot the same points, but this time assigning the colors to indicate the clusters

plt.scatter(X[:, 0], X[:, 1], c=labels, edgecolor='black', cmap=cmap_bold[0], s=20)
plt.scatter(clusters[:, 0], clusters[:, 1], c='black', s=200, alpha=0.5);
print(kmeans.predict([[-0.5, 0.5], [1.5, -0.25], [0, 0.25]]))

plt.show()




# Seven Cluster k = 7


k = 7
#running kmeans clustering into two
kmeans = KMeans(n_clusters=k, random_state=0).fit(X)  
# the random state is optionlly, here it is specified so we get determistic clusters.
# this will contain the labels for our predicted clusters (either 0 or 1)   
labels = kmeans.labels_
# the centers of the calculated clusters
clusters = kmeans.cluster_centers_
# printing our cluster centers - there will be 2 of them.
print(clusters)

# now plot the same points, but this time assigning the colors to indicate the clusters

plt.scatter(X[:, 0], X[:, 1], c=labels, edgecolor='black', cmap=cmap_bold[5], s=20)
plt.scatter(clusters[:, 0], clusters[:, 1], c='black', s=200, alpha=0.5);
print(kmeans.predict([[-0.5, 0.5], [1.5, -0.25], [0, 0.25]]))

plt.show()


'''
     _____  ____   _____  _____          _   _ 
    |  __ \|  _ \ / ____|/ ____|   /\   | \ | |
    | |  | | |_) | (___ | |       /  \  |  \| |
    | |  | |  _ < \___ \| |      / /\ \ | . ` |
    | |__| | |_) |____) | |____ / ____ \| |\  |
    |_____/|____/|_____/ \_____/_/    \_\_| \_|


  _____                 _ _                ____                     _    _____             _   _       _    _____ _           _            _                      __                        _ _           _   _                            _ _   _       _   _       _          
 |  __ \               (_) |              |  _ \                   | |  / ____|           | | (_)     | |  / ____| |         | |          (_)                    / _|     /\               | (_)         | | (_)                          (_) | | |     | \ | |     (_)         
 | |  | | ___ _ __  ___ _| |_ _   _ ______| |_) | __ _ ___  ___  __| | | (___  _ __   __ _| |_ _  __ _| | | |    | |_   _ ___| |_ ___ _ __ _ _ __   __ _    ___ | |_     /  \   _ __  _ __ | |_  ___ __ _| |_ _  ___  _ __  ___  __      ___| |_| |__   |  \| | ___  _ ___  ___ 
 | |  | |/ _ \ '_ \/ __| | __| | | |______|  _ < / _` / __|/ _ \/ _` |  \___ \| '_ \ / _` | __| |/ _` | | | |    | | | | / __| __/ _ \ '__| | '_ \ / _` |  / _ \|  _|   / /\ \ | '_ \| '_ \| | |/ __/ _` | __| |/ _ \| '_ \/ __| \ \ /\ / / | __| '_ \  | . ` |/ _ \| / __|/ _ \
 | |__| |  __/ | | \__ \ | |_| |_| |      | |_) | (_| \__ \  __/ (_| |  ____) | |_) | (_| | |_| | (_| | | | |____| | |_| \__ \ ||  __/ |  | | | | | (_| | | (_) | |    / ____ \| |_) | |_) | | | (_| (_| | |_| | (_) | | | \__ \  \ V  V /| | |_| | | | | |\  | (_) | \__ \  __/
 |_____/ \___|_| |_|___/_|\__|\__, |      |____/ \__,_|___/\___|\__,_| |_____/| .__/ \__,_|\__|_|\__,_|_|  \_____|_|\__,_|___/\__\___|_|  |_|_| |_|\__, |  \___/|_|   /_/    \_\ .__/| .__/|_|_|\___\__,_|\__|_|\___/|_| |_|___/   \_/\_/ |_|\__|_| |_| |_| \_|\___/|_|___/\___|
                               __/ |                                          | |                                                                   __/ |                      | |   | |                                                                                        
                              |___/                                           |_|                                                                  |___/                       |_|   |_|                                                                                        


'''
from sklearn.cluster import DBSCAN

# DBSCAN clustering
# dbscan = DBSCAN(eps=0.2, min_samples=5)
dbscan = DBSCAN(eps=0.2, min_samples=20)
labels = dbscan.fit_predict(X)
# Number of clusters in labels, ignoring noise if present.
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
print(f"Number of clusters: {n_clusters_}")

# Plotting the clusters
plt.scatter(X[:, 0], X[:, 1], c=labels, edgecolor='black', cmap='viridis', s=20)
plt.show()



'''
In the DBSCAN (Density-Based Spatial Clustering of Applications with Noise) algorithm, `eps` and `min_samples` are two critical parameters that directly affect the clustering results:

1. **eps (epsilon)**:
   - `eps` is the maximum distance between two samples for one to be considered as in the neighborhood of the other. In simpler terms, it determines the radius of the neighborhood around each point.
   - Points within the same neighborhood are considered as part of the same cluster.
   - Increasing `eps` means that more points will be included in each cluster, potentially resulting in fewer clusters.
   - Decreasing `eps` results in smaller, denser clusters because it requires points to be closer together to be considered part of the same cluster.

2. **min_samples**:
   - `min_samples` is the number of samples in a neighborhood for a point to be considered as a core point. Core points are points that have at least `min_samples` points (including themselves) within their `eps` neighborhood.
   - Points that do not meet the `min_samples` criterion but are within the `eps` neighborhood of a core point are considered border points.
   - Points that are not core points and do not have enough neighbors to be considered border points are labeled as noise points.
   - Increasing `min_samples` requires denser regions to form a cluster, resulting in more points being labeled as noise or belonging to smaller clusters.
   - Decreasing `min_samples` allows for more points to be core points, potentially leading to larger clusters and fewer noise points.

In summary, adjusting `eps` and `min_samples` allows you to control the density and size of the clusters identified by DBSCAN. It's often necessary to experiment with different values to find the optimal parameters for your specific dataset and clustering objectives.

'''