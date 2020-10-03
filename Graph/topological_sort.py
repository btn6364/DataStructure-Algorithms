from Graph.graph_helper import buildDiGraph, GraphVisualization


def topologicalSort(graph):
    #O(E + V) runtime | O(V) space
    visited = set()
    stack = []
    for node in graph:
        if node in visited:
            continue
        _topologicalSort(graph, node, visited, stack)
    return stack

def _topologicalSort(graph, node, visited, stack):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor in visited:
            continue
        _topologicalSort(graph, neighbor, visited, stack)
    stack.append(node)


if __name__ == '__main__':
    edges = [("A", "C"), ("B", "C"), ("B", "D"), ("C", "E"), ("E", "H"),
             ("E", "F"), ("F", "G"), ("D", "F")]

    # Build the graph
    graph = buildDiGraph(edges)
    print(graph)
    print(topologicalSort(graph))

    # Visualize the map
    graphVisualizer = GraphVisualization(edges)
    graphVisualizer.visualize()