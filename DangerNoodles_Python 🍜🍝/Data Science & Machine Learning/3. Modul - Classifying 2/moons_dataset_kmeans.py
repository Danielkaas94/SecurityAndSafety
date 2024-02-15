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