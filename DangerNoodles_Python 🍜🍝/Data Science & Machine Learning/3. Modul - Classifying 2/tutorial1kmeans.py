import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans # This will be used for the algorithm

import matplotlib.pyplot as plt  # This will be use to plot the data
from sklearn import datasets   # This will be used to get a sample dataset - just to have some data


# we only take the first two features. We could avoid this ugly
# slicing by using a real two-dim dataset
# the iris-data is a multidimensional data so we slice the first
iris = datasets.load_iris()

X = iris.data[:, :2]
# Taking the first two columns - notation array[x,y] gives you the x-th row and the y-column
# if you want all values on the row i.e. an entire column use array[:,columnNr]
print(X) # just to print the data so we can see what we are dealing with

plt.figure() # creating a new figure
plt.scatter(X[:, 0], X[:, 1], color='black', s=20)  # plot x,y values using the color black and size = 20

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
plt.scatter(clusters[:, 0], clusters[:, 1], c='black', s=200, alpha=0.5); # s ændre på størrelse af cluster cirkel
plt.show()

#The important thing is that we could now predict which cluster a new point should belong to.
# Let's take the point (6,4) which we might expect to belong to the red cluster and (6,2)
# which should probably belong to the green cluster (look at the graph to verify this):

print(kmeans.predict([[5, 3], [7, 3]]))

# Verify that this is what we expected.
# 0 indicates the first cluster (red - numbering of clusters start at 0),
# 1 indicates that the second point belongs to the second cluster (green).
# So based on previous data, we have learned to how to cluster previously unseen new data.

#We can of course also decide we want more than 2 clusters -
# here you can see the code for k = 4 and the corresponding plot

k = 4
#running kmeans clustering into 4
kmeans = KMeans(n_clusters=k, random_state=0).fit(X)
# this will contain the labels for our predicted clusters (either 0,1,2, or 3)
labels = kmeans.labels_
#using the color map with index 2 - which has 4 colors if you go back in the coode
plt.scatter(X[:, 0], X[:, 1], c=labels, edgecolor='black', cmap=cmap_bold[2], s=20)

# the centers of the calculated clusters
clusters = kmeans.cluster_centers_
# printing our cluster centers - there will be 4 of them.
print(clusters)

print(kmeans.predict([[5, 3], [7, 3]]))
plt.scatter(clusters[:, 0], clusters[:, 1], c='black', s=200, alpha=0.5);
plt.show()



# Try again with even more kmeans clustering
k = 7
#running kmeans clustering into 4
kmeans = KMeans(n_clusters=k, random_state=0).fit(X)
# this will contain the labels for our predicted clusters (either 0,1,2, or 3)
labels = kmeans.labels_
#using the color map with index 5 - which has 7 colors if you go back in the coode
plt.scatter(X[:, 0], X[:, 1], c=labels, edgecolor='black', cmap=cmap_bold[5], s=20)

# the centers of the calculated clusters
clusters = kmeans.cluster_centers_
# printing our cluster centers - there will be 7 of them.
print(clusters)

print(kmeans.predict([[5, 3], [7, 3]]))
plt.scatter(clusters[:, 0], clusters[:, 1], c='black', s=200, alpha=0.5);
plt.show()