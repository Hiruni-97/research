import networkx as nx
class Generator:
    '''
    Generate graph
    '''
    def __init__(self,nodes,edges):
        self.graph = self.generate_random_graph(nodes, edges)

    def generate_random_graph(self, nodes, edges):
        '''
        Generate a random graph based on given nodes and edges count
        '''
        G = nx.gnm_random_graph(int(nodes), int(edges))

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
        return graph_json

    def get_graph(self):
        '''
        Get generated graph
        '''
        return self.graph
