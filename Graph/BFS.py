from Graph.graph_helper import buildAdjList, prettyPrint
from collections import deque

def BFS(adj_list, source, target):
    queue = deque()
    queue.append(source)
    visited = set()
    while queue:
        node = queue.popleft()
        if node == target:
            return True
        if node not in visited:
            visited.add(node)
            for neighbor in adj_list[node]:
                queue.append(neighbor)
    return False



if __name__ == '__main__':
    love_connections = [("Hermia", "Lysander"), ("Demetrius", "Lysander"),
                        ("Helena", "Demetrius"), ("Titania", "Oberon"), ("Oberon", "Titania"),
                        ("Puck", "Puck"), ("Lysander", "Puck"), ("Helena", "Titania"), ("Hermia", "Puck"), ("Puck", "Helena")]

    #directed adjacency list
    adj_list = buildAdjList(love_connections)

    #Lysander: [Helena, Puck]
    #Hermia: [Lysander]
    #Demetrius: [Lysander]
    #Helena: [Demetrius, Titania]
    #Titania: [Oberon]
    #Oberon: [Titania]
    #Puck: [Puck]

    #visited: Hermia, Puck, Lysander, Helena, Titania, Demetrius

    #0 Hermia
    #1 Puck, Lysander
    #2 Helena
    #3 Titania, Demetrius
    #4 Oberon

    print(BFS(adj_list, "Hermia", "Oberon"))

    # prettyPrint(love_connections)