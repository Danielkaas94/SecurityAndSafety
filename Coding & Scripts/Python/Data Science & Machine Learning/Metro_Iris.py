import matplotlib.pyplot as plt
import networkx as nx
from sklearn.datasets import load_iris
from sklearn.metrics.pairwise import euclidean_distances

# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Compute pairwise Euclidean distances between samples
distances = euclidean_distances(X)

# Threshold for defining connections
threshold = 1.5

# Create a graph
G = nx.Graph()

# Add nodes representing samples
for i in range(len(X)):
    G.add_node(i, label=f'Sample {i}\n({iris.target_names[y[i]]})')

# Add edges representing connections based on similarity
for i in range(len(X)):
    for j in range(i + 1, len(X)):
        if distances[i, j] <= threshold:
            G.add_edge(i, j)

# Define positions for samples using a spring layout
positions = nx.spring_layout(G, scale=10, iterations=10, fixed=None)

# Draw nodes
nx.draw_networkx_nodes(G, pos=positions, node_size=300, node_color='lightblue')

# Draw edge, scale=100, iterations=100s
nx.draw_networkx_edges(G, pos=positions, width=1.0, alpha=0.5)

# Draw labels
labels = nx.get_node_attributes(G, 'label')
nx.draw_networkx_labels(G, pos=positions, labels=labels, font_size=8, font_weight='bold')

# Customize the plot
plt.title('Metro Map using Iris Dataset')
plt.grid(False)
plt.axis('off')
plt.show()
