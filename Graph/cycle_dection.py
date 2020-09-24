from Graph.graph_helper import buildAdjList, GraphVisualization

def detectCycle(adj_list):
    visited = set()
    for node in adj_list:
        if node not in visited:
            if DFS(adj_list, node, set(), visited):
                return True
    return False

def DFS(adj_list, node, cur_path, visited):
    #if node in the cur_path, found a cycle, return True
    if node in cur_path:
        return True
    #if node in visited, already checked this node, not found a cycle
    if node in visited:
        return False

    cur_path.add(node)
    visited.add(node)
    for neighbor in adj_list[node]:
        if DFS(adj_list, neighbor, cur_path, visited):
            return True
    #backtrack the current path
    cur_path.remove(node)
    return False



if __name__ == '__main__':
    edges = [("A", "B"), ("D", "B"), ("C", "D"), ("E", "F"), ("B", "G"),
             ("G", "G"), ("C", "E"), ("A", "G"), ("G", "C")]

    #Visualize the map
    graphVisualizer = GraphVisualization(edges)
    graphVisualizer.visualize()

    #Init the adjacency list.
    adj_list = buildAdjList(edges)

    #Detect if can find a cycle.
    print(detectCycle(adj_list))