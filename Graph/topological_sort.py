from Graph.graph_helper import buildDiGraph, GraphVisualization

#########################################
# Recursion version of Top sort.
#########################################
def topologicalSortRecursion(graph):
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


###########################################
# Iterative version of Top Sort.
###########################################
from collections import deque, defaultdict
def countPreq(graph):
    preqs = defaultdict(int)
    for node in graph:
        for neighbor in graph[node]:
            preqs[neighbor] += 1
    return preqs

def topologicalSortIterative(graph):
    #Count the number of preq for each node.
    preqs = countPreq(graph)

    print(preqs)
    #Init the queue with all nodes with 0 prerequisite.
    queue = deque()
    for node in graph:
        if preqs[node] == 0:
            queue.append(node)

    #Start top sort.
    result = []
    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor in graph[node]:
            preqs[neighbor] -= 1
            if preqs[neighbor] == 0:
                queue.append(neighbor)
    return result


if __name__ == '__main__':
    edges = [("A", "B"), ("C", "D"), ("B", "E"), ("D", "E")]

    # Build the graph
    # graph = buildDiGraph(edges)
    graph = buildDiGraph(edges)
    #Top sort recursion
    print(topologicalSortRecursion(graph))

    #Top sort iteration
    print(topologicalSortIterative(graph))

    # Visualize the map
    graphVisualizer = GraphVisualization(edges)
    graphVisualizer.visualize()