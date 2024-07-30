from flask import Flask, render_template,request
import json
import networkx as nx
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from analyzer import Analyzer
from graph_generator import Generator

app = Flask(__name__)


def generate_random_graph(nodes_count, edges_count):
    G = nx.Graph()
    generator = Generator(nodes_count, edges_count)
    data = generator.get_graph()

    for node in data['nodes']:
        G.add_node(node['id'], label=node['label'])

    for edge in data['edges']:
        G.add_edge(edge['source'], edge['target'])

    pos = nx.spring_layout(G)
    analyzer = Analyzer(G)
    colors = analyzer.get_colors()
    nx.draw(G,pos, with_labels=True, node_color=colors, edge_color='gray')
    buf = BytesIO()
    plt.savefig(buf, format='png')
    plt.close()
    buf.seek(0)
    return base64.b64encode(buf.read()).decode('utf-8')


@app.route('/')
def index():
    '''
    Landing page
    '''
    return render_template('index.html')

@app.route('/graph',  methods=['POST'])
def graph():
    '''
    Generate Graph
    '''
    nodes_count = request.form['nodes']
    edges_count = request.form['edges']

    graph_image = generate_random_graph(nodes_count, edges_count)
    return render_template('graph.html', graph_image=graph_image)

if __name__ == '__main__':
    app.run(debug=True, port=8080)