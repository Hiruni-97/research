import networkx as nx
import matplotlib.pyplot as plt
import json

# Create an undirected graph
G = nx.Graph()

with open('input.json', 'r') as f:
    data = json.load(f)

for node in data['nodes']:
    G.add_node(node['id'], label=node['label'])

for edge in data['edges']:
    G.add_edge(edge['source'], edge['target'])

# Assign attributes
G.nodes[1]['color'] = 'red'
G[1][2]['weight'] = 5

# Visualize the graph
nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray')
plt.show()
