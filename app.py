from flask import Flask, render_template
import json
import networkx as nx
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from analyzer import Analyzer

app = Flask(__name__)


def generate_graph():
    G = nx.Graph()
    with open('input.json', 'r') as f:
        data = json.load(f)

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
    buf.seek(0)
    return base64.b64encode(buf.read()).decode('utf-8')


@app.route('/')
def index():

    graph_image = generate_graph()
    return render_template('index.html', graph_image=graph_image)

if __name__ == '__main__':
    app.run(debug=True, port=8080)