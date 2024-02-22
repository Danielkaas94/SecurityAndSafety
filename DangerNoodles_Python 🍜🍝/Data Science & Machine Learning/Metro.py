import matplotlib.pyplot as plt
import networkx as nx

# Sample data representing metro stations and connections
metro_data = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'E'],
    'D': ['B', 'E'],
    'E': ['C', 'D']
}

# Create a graph
G = nx.Graph(metro_data)

# Define positions for stations (you may need actual coordinates)
positions = {
    'A': (0, 0),
    'B': (1, 0),
    'C': (0, 1),
    'D': (1, 1),
    'E': (2, 1)
}

# Draw the graph
nx.draw(G, pos=positions, with_labels=True, node_size=1000, node_color='lightblue', font_size=12, font_weight='bold')

# Customize the plot to make it look like a metro map
plt.title('Metro Map')
plt.grid(False)
plt.show()
