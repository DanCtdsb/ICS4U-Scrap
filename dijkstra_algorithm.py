import heapq

def dijkstra_algorithm(graph, start, end):
    dist = {node: float('inf') for node in graph}
    dist[start] = 0

    pq = []
    heapq.heappush(pq, [0, start])

    while pq:
        current_dist, node = heapq.heappop(pq)
        if current_dist > dist[node]:
            continue

        for neighbour, weight in graph[node]:
            new_dist = current_dist + weight

            if new_dist < dist[neighbour]:
                dist[neighbour] = new_dist
                heapq.heappush(pq, [new_dist, neighbour])
    return dist[end] 


graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2)],
    'C': []
}

print(dijkstra_algorithm(graph, list(graph.keys())[0], list(graph.keys())[-1]))