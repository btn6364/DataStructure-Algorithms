#pip install networkx
import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict

def buildAdjList(edges):
    adj_list = defaultdict(list)
    for source, target in edges:
        adj_list[source].append(target)
    return adj_list

def buildDiGraph(edges):
    adj_list = dict()
    for source, target in edges:
        if source not in adj_list:
            adj_list[source] = []
        if target not in adj_list:
            adj_list[target] = []
        adj_list[source].append(target)
    return adj_list

class GraphVisualization:
    def __init__(self, edges):
        self.edges = edges
        self.options = {
            'node_color': 'yellow',
            'node_size': 1000,
            'width': 3,
            'arrowstyle': '->',
            'arrowsize': 12,
        }
    def visualize(self):
        graph = nx.DiGraph(directed=True)
        graph.add_edges_from(self.edges)
        nx.draw_networkx(graph, arrows=True, **self.options)
        plt.show()

