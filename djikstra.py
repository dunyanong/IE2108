import heapq

# list down all of the distances to all nodes
def dijkstra(graph, start):
    # setup the graph
    distances = {}
    for node in graph:
        distances[node] = float("inf")
        
    distances[start] = 0
    
    priority_queue = [(distances[start], start)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if distances[current_node] < current_distance:
            continue
        
        for neighbour, weight in graph[current_node].items():
            sum_distance = current_distance + weight
            
            if sum_distance < distances[neighbour]:
                distances[neighbour] = sum_distance
                heapq.heappush(priority_queue, (sum_distance ,neighbour))
    
    return distances
        

        

graph = {
    'A': {'B': 2, 'C': 5},
    'B': {'A': 2, 'C': 1, 'D': 7},
    'C': {'A': 5, 'B': 1, 'D': 3},
    'D': {'B': 7, 'C': 3}
}

start_node = 'A'
print("Shortest distances from node", start_node, "to other nodes:")
print(dijkstra(graph, start_node))