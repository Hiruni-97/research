import networkx as nx
import matplotlib.pyplot as plt
import json

# Create an undirected graph
G = nx.Graph()

# Add nodes
G.add_node(1)
G.add_nodes_from([2, 3, 4])

# Add edges
G.add_edge(1, 2)
G.add_edges_from([(2, 3), (3, 4), (4, 1)])

# Assign attributes
G.nodes[1]['color'] = 'red'
G[1][2]['weight'] = 5

# Visualize the graph
nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray')
plt.show()
