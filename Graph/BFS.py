from Graph.graph_helper import buildAdjList, GraphVisualization
from collections import deque

def BFS(adj_list, source, target):
    queue = deque([source])
    visited = set()
    while queue:
        node = queue.popleft()
        if node in visited:
            continue
        if node is target:
            return True
        visited.add(node)
        for neighbor in adj_list[node]:
            queue.append(neighbor)
    return False

if __name__ == '__main__':
    edges = [("A", "B"), ("D", "B"), ("C", "D"), ("E", "F"), ("F", "E"),
             ("G", "G"), ("B", "G"), ("C", "E"), ("A", "G"), ("G", "C")]

    #Visualize the map
    graphVisualizer = GraphVisualization(edges)
    graphVisualizer.visualize()

    #Init the adjacency list.
    adj_list = buildAdjList(edges)

    #Call BFS on some nodes.
    print(BFS(adj_list, "B", "F"))
    print(BFS(adj_list, "D", "F"))

