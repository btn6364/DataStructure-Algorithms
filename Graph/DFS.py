from Graph.graph_helper import buildAdjList, GraphVisualization


def DFSHelper(adj_list, source, target, visited):
    #base case
    if source is target:
        return True
    if source in visited: #already visited this position
        return False
    visited.add(source)
    for neighbor in adj_list[source]:
        if DFSHelper(adj_list, neighbor, target, visited):
            return True
    return False

def DFS(adj_list, source, target):
    visited = set()
    return DFSHelper(adj_list, source, target, visited)

if __name__ == '__main__':
    edges = [("A", "B"), ("D", "B"), ("C", "D"), ("E", "F"), ("F", "E"),
             ("G", "G"), ("B", "G"), ("C", "E"), ("A", "G"), ("G", "C")]

    #Visualize the map
    graphVisualizer = GraphVisualization(edges)
    graphVisualizer.visualize()

    #Init the adjacency list.
    adj_list = buildAdjList(edges)

    #Call BFS on some nodes.
    print(DFS(adj_list, "B", "F"))
    print(DFS(adj_list, "D", "F"))