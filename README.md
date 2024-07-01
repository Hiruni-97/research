# research

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

* First run 01_generator.py to generate the network, You can configure nodes and edges by  ``` G = nx.gnm_random_graph(num_of_nodes, num_of_edges) ```
* Next run 02_plotter.py to plot the network
