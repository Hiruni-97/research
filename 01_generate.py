import networkx as nx
import json
import random

G = nx.gnm_random_graph(50, 100)

graph_json = {
    'nodes': [],
    'edges': []
}
for node in G.nodes():
    node_data = {
        'id': node,
        'label': f'Node {node}'
    }
    graph_json['nodes'].append(node_data)

for edge in G.edges():
    edge_data = {
        'source': edge[0],
        'target': edge[1]
    }
    graph_json['edges'].append(edge_data)

json_string = json.dumps(graph_json, indent=4)
print(json_string)
with open('input.json', 'w') as f:
    f.write(json_string)

