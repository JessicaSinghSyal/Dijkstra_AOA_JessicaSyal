# DIJKSTRA ALGORITHM 
# Homework Submission: Problem 4, Problem Set 7 
# Jessica Singh Syal 
# UIN: 337001834


import heapq

def dijkstra_shortest_paths(graph, source):
    
    # Initialization
    distances = {vertex: float('inf') for vertex in graph}
    predecessors = {vertex: None for vertex in graph}
    distances[source] = 0
    
    # Min-Priority Queue (Binary Heap): stores (distance, vertex)
    # The heap only stores the tentative distance and the vertex.
    priority_queue = [(0, source)]

    while priority_queue:
        # EXTRACT-MIN: Get the vertex u with the smallest current distance
        current_distance, u = heapq.heappop(priority_queue)

        # Check for "stale" entries (where a shorter path to u 
        # was already processed)
        if current_distance > distances[u]:
            continue

        # Relaxation Step: For each neighbor v of u
        for v, weight in graph.get(u, []):
            new_distance = current_distance + weight
            
            # Relax the edge (u, v)
            if new_distance < distances[v]:
                distances[v] = new_distance
                predecessors[v] = u
                
                # DECREASE-KEY: Handled by inserting the new, shorter distance.
                heapq.heappush(priority_queue, (new_distance, v))
                
    return distances, predecessors

# --- Example Usage (Map data will be provided later) ---
# Example graph where streets 1 are desirable (low weight) and 2 less so.
example_map = {
    'Bookstore': [('Alley_A', 1), ('Texas_Ave_N', 2)],
    'Alley_A': [('Hideout_1', 1)],
    'Texas_Ave_N': [('Residential_B', 2), ('Hideout_1', 1)],
    'Residential_B': [('Highway_Access', 2)],
    'Hideout_1': [],
    'Highway_Access': []
}

# distances, paths = dijkstra_shortest_paths(example_map, 'Bookstore')
# print(f"Distances: {distances}")
# print(f"Predecessors: {paths}")

