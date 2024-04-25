import heapq

def djikstra(graph, start):
    distances = {}
    for node in graph:
        distances[node] = float("inf")
    
    distances[start] = 0
    
    priority_queue = [(start, distances[start])]
    
    while priority_queue:
        current_node, current_distance = heapq.heappop(priority_queue)
        
        if distances[current_node] < current_distance:
            continue
        
        for neighbour, weight in graph[current_node].items():
            total_weight = weight + current_distance
            
            if total_weight < distances[neighbour]:
                distances[neighbour] = total_weight
                heapq.heappush(priority_queue, (neighbour, total_weight))

    return distances["D"]
    
    
graph = {
    "A": {"B": 2, "C": 5 },
    "B": {"A": 2, "C": 1, "D": 7},
    "C": {"A": 5, "B": 1, "D": 3},
    "D": {"B": 7, "C": 3}
}

print(djikstra(graph, "A"))