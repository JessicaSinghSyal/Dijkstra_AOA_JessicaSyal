# DIJKSTRA ALGORITHM 
# Homework Submission: Problem 4, Problem Set 7 
# Jessica Singh Syal 
# UIN: 337001834


import heapq

def dijkstra_shortest_paths(graph, source):
    """
    Implements Dijkstra's algorithm using a Binary Min-Heap (heapq).
    Finds the lowest-cost escape routes from the source (bookstore).
    """
    
    # Initialization
    distances = {node: float('inf') for node in graph}
    predecessors = {node: None for node in graph}
    distances[source] = 0
    
    # Priority Queue (Min-Heap) stores (distance, node)
    priority_queue = [(0, source)]

    while priority_queue:
        current_distance, u = heapq.heappop(priority_queue)

        # Skip if a shorter path has already been found for u (stale entry)
        if current_distance > distances[u]:
            continue

        # Relaxation step
        for v, weight in graph.get(u, []):
            new_distance = current_distance + weight
            
            # Relax the edge (u, v)
            if new_distance < distances[v]:
                distances[v] = new_distance
                predecessors[v] = u
                
                # DECREASE-KEY: Handled by inserting the new, shorter distance entry.
                heapq.heappush(priority_queue, (new_distance, v))
                
    return distances, predecessors

# --- Graph Data Derived from the Map (Source 1) ---
# Edge Weight 1: Entirely Green (Fast) [cite: 15]
# Edge Weight 2: Any part Orange/Yellow (Slow) [cite: 15]
graph_data = {
    1: [(2, 1), (11, 1), (12, 2), (10, 1)],
    2: [(1, 1), (3, 1)],
    3: [(2, 1), (4, 1)],
    4: [(3, 1), (5, 1)],
    5: [(4, 1), (6, 2), (21, 1), (7, 2)],
    6: [(5, 2), (7, 1)],
    7: [(6, 1), (5, 2)],
    8: [(9, 1), (10, 1)],
    9: [(8, 1), (10, 1), (19, 1)],
    10: [(1, 1), (8, 1), (9, 1), (11, 2)],
    11: [(1, 1), (10, 2), (12, 2), (17, 1)],
    12: [(1, 2), (11, 2), (13, 1), (21, 1)],
    13: [(12, 1), (14, 1)],
    14: [(13, 1), (15, 1)],
    15: [(14, 1), (16, 1)],
    16: [(15, 1), (17, 1)],
    17: [(11, 1), (16, 1), (18, 1)],
    18: [(17, 1), (19, 1)],
    19: [(9, 1), (18, 1)],
    21: [(5, 1), (12, 1), (22, 1)],
    22: [(21, 1)]
    # Nodes 20 and 23-26 do not exist/are not connected waypoints.
}

# Source node for Dijkstra's
source_node = 1

# The required target destinations [cite: 18, 19, 20]
destinations = [6, 8, 9, 15, 16, 22] 

# Run the algorithm
distances, predecessors = dijkstra_shortest_paths(graph_data, source_node)

# --- Path Reconstruction Utility (Not required in the final output, but useful) ---
def reconstruct_path(predecessors, target):
    path = []
    curr = target
    while curr is not None:
        path.append(curr)
        curr = predecessors.get(curr)
    return path[::-1]

# Display the required result for the homework table
print("\n--- Shortest Path Results (for Homework Table) ---")
for dest in destinations:
    dist = distances[dest] if dest in distances else float('inf')
    path = reconstruct_path(predecessors, dest)
    print(f"Destination {dest}: Distance {dist}, Path {path}")