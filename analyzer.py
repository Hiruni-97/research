class Analyzer:
    '''
    Generate critical nodes array
    '''
    def __init__(self, graph):
        self.graph = graph
        self.colors = []
        self.analyze()
    
    def get_colors(self):
        return self.colors

    def analyze(self):
        for node in self.graph.nodes():
            degree = self.graph.degree[node]
            color = 'lightblue'
            if degree > 3:
                color = 'orange'
            if degree > 5:
                color = 'red'
            self.colors.append(color)

