from Graph.graph_helper import buildAdjList, GraphVisualization


def helper(adj_list, source, target, visited):
    #base case
    if source == target:
        return True
    if source in visited:
        return False
    visited.add(source)
    for neighbor in adj_list[source]:
        if helper(adj_list, neighbor, target, visited):
            return True
    return False

def DFS(adj_list, source, target):
    visited = set()
    return helper(adj_list, source, target, visited)



if __name__ == '__main__':
    love_connections = [("Lysander", "Helena"), ("Hermia", "Lysander"), ("Demetrius", "Lysander"),
                        ("Helena", "Demetrius"), ("Titania", "Oberon"), ("Oberon", "Titania"),
                        ("Puck", "Puck"), ("Lysander", "Puck"), ("Helena", "Titania")]

    #directed adjacency list
    adj_list = buildAdjList(love_connections)

    #source 0
    #N+1
    edges = []
    N = 5
    for i in range(N):
        for j in range(N):
            edges.append((i,j))
    edges.append((N+1,N+1))
    # prettyPrint(edges)


    #graph_repr = prettyPrint(love_connections)
    print(DFS(adj_list, "Hermia", "Oberon"))