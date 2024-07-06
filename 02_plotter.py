import networkx as nx
import matplotlib.pyplot as plt
import json

from analyzer import Analyzer

# Create an undirected graph
G = nx.Graph()

with open('input.json', 'r') as f:
    data = json.load(f)

for node in data['nodes']:
    G.add_node(node['id'], label=node['label'])

for edge in data['edges']:
    G.add_edge(edge['source'], edge['target'])

analyzer = Analyzer(G)
colors = analyzer.get_colors()

# Visualize the graph
nx.draw(G, with_labels=True, node_color=colors, edge_color='gray')
plt.show()
