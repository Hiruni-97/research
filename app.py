import networkx as nx
import matplotlib.pyplot as plt
import json

# Create an undirected graph
G = nx.Graph()

# Assign attributes
G.nodes[1]['color'] = 'red'
G[1][2]['weight'] = 5

# Visualize the graph
nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray')
plt.show()
