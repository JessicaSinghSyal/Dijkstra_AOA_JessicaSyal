# DIJKSTRA ALGORITHM 
# Homework Submission: Problem 4, Problem Set 7 
# Jessica Singh Syal 
# UIN: 337001834


import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    previous = {node: None for node in graph}
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))
    return distances, previous

def get_path(previous, node):
    path = []
    while node is not None:
        path.insert(0, node)
        node = previous[node]
    return path

graph = {
    1: [(2,1), (11,1)],
    2: [(1,1), (3,1), (12,1)],
    3: [(2,1), (4,1)],
    4: [(3,1), (5,1)],
    5: [(4,1), (6,2)],
    6: [(5,2), (7,1)],
    7: [(6,1), (8,1)],
    8: [(7,1), (9,1)],
    9: [(8,1), (10,1)],
    10: [(9,1), (11,1)],
    11: [(1,1), (10,1), (12,1), (13,2)],
    12: [(2,1), (11,1), (13,1)],
    13: [(11,2), (12,1), (14,1)],
    14: [(13,1), (15,1)],
    15: [(14,1), (16,2)],
    16: [(15,2), (17,1), (22,1)],
    17: [(16,1), (18,1)],
    18: [(17,1), (19,1)],
    19: [(18,1), (20,1)],
    20: [(19,1), (21,1), (22,1)],
    21: [(20,1)],
    22: [(16,1), (20,1)]
}

print(f"Source Node: {source}\n")

print("Shortest Path Distances to Target Destinations:")
for t in targets:
    print(f"   → Destination Node {t:<3} | Shortest Path Length: {distances[t]}")

min_target = min(targets, key=lambda x: distances[x])
min_distance = distances[min_target]