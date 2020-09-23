from Graph.graph_helper import buildAdjList, prettyPrint

def detectCycle(adj_list):
    visited = set()
    for node in adj_list:
        if node not in visited:
            if DFS(node, set(), visited, adj_list):
                return True
    return False


def DFS(cur_node, cur_path, visited, adj_list):
    #base case
    if cur_node in cur_path: #found a cycle
        return True
    if cur_node in visited: # cur_node has already been checked and doesn't have cycle
        return False

    cur_path.add(cur_node)
    visited.add(cur_node)
    for neighbor in adj_list[cur_node]:
        if neighbor == cur_node:
            continue
        if DFS(neighbor, cur_path, visited, adj_list):
            return True

    #backtrack
    cur_path.remove(cur_node)
    return False




if __name__ == '__main__':
    love_connections = [("Hermia", "Lysander"), ("Demetrius", "Lysander"), ("Oberon", "Titania"),
                        ("Puck", "Puck"), ("Lysander", "Puck"), ("Helena", "Titania"), ("Hermia", "Puck"), ("Puck", "Helena"),
                        ("Titania", "Titania"), ("Helena", "Hermia")]

    #start Hermia
    #cur path: Hermia, Lysander, Puck, Demetrius
    #directed adjacency list
    adj_list = buildAdjList(love_connections)

    # prettyPrint(love_connections)
    print(detectCycle(adj_list))