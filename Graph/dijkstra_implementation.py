"""
Dijkstra's algorithm:
- Given a directed weighted graph (positive weight). Find the shortest path from the starting node to all other
positions in the graph. If this couldn't be found, output[i] = -1.
"""

import heapq
from collections import defaultdict

def dijkstras(start, graph):
    num_vertices = len(graph.keys())

    # Initialize the min_distances hash table and min_dist_heap
    # to keep track of the current smallest distances to each node from start.
    min_distances = defaultdict(int)
    min_dist_heap = []
    for node in graph:
        init_distance = 0 if node == start else float("inf")
        min_distances[node] = init_distance
        min_dist_heap.append((init_distance, node))

    # Initialize the min heap
    heapq.heapify(min_dist_heap)

    # Keep track of visited nodes.
    visited = set()

    # Visit every single node in the graph
    while len(visited) < num_vertices:
        min_dist, node = heapq.heappop(min_dist_heap)

        # If the unvisited node with minimum distance is inf, meaning it's impossible to get to the rest of the nodes
        # from the start position, stop the algorithm here.

        if min_dist == float("inf"):
            break

        visited.add(node)
        for destination, distToDestination in graph[node]:
            cur_distance = min_dist + distToDestination

            # Prevents visit the same node twice.
            if destination in visited:
                continue

            # If the current distance to the destination is smaller than the current shortest path,
            # update the shortest path.
            if cur_distance <= min_distances[destination]:
                min_distances[destination] = cur_distance
                heapq.heappush(min_dist_heap, (cur_distance, destination))

    printResult(start, min_distances)

def printResult(start, min_distances):
    for node in min_distances:
        if min_distances[node] == float("inf"):
            print(f"No shortest path from {start} to {node}.")
        else:
            print(f"Shortest path from {start} to {node} costs: {min_distances[node]} units.")

if __name__ == '__main__':
    start1 = 'A'
    start2 = 'D'
    graph = {
        'A': [('B', 2)],
        'B': [('C', 1), ('D', 5), ('E', 13)],
        'C': [('D', 3)],
        'D': [('E', 16), ('B', 2)],
        'E': [],
        'F': []
    }
    print("----------------------TEST 1: START AT A--------------------------")
    dijkstras(start1, graph)

    print("\n")
    print("----------------------TEST 1: START AT D--------------------------")
    dijkstras(start2, graph)