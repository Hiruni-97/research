# Research

## Setup Environment
```
pip 21.0.1
Python 3.10
Visual Studio Code - latest
```

* Run `pip install -r requirements.txt` to install Python dependencies.

## Configuration

* First run 01_generator.py to generate the network, You can configure nodes and edges by  ``` G = nx.gnm_random_graph(num_of_nodes, num_of_edges) ```
JSON format 
```
{
    "nodes": [
        {"id": 1, "label": "Node 1"},
        {"id": 2, "label": "Node 2"},
        {"id": 3, "label": "Node 3"}
    ],
    "edges": [
        {"source": 1, "target": 2},
        {"source": 2, "target": 3},
        {"source": 3, "target": 1}
    ]
}
```
* Next run 02_plotter.py to plot the network
* Nodes in red color are highly critical. Nodes in orange color are less crtitcal.

## How to run web app

* Click on debug button in VSCode

* Browse `http://127.0.0.1:8080/` to visualize.

![Logo](img/image.png)
