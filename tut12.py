import heapq

graph = {
    1: {
        2: 2,
        3: 10,
        4: 7
    },
    2: {
        1: 2,
        4: 3
    },
    3: {
        1: 10,
        4: 4,
        5: 1
    },
    4: {
        1: 7,
        2: 3,
        3: 4,
        5: 9
    },
    5: {
        1: 12,
        3: 1,
        4: 9
    }
}

def dijkstra(graph, src):
    distances = {node: float('inf') for node in graph}
    distances[src] = 0
    priority_queue = [(0, src)]
    parent = {node: -1 for node in graph}  # parent node in the shortest path
    visited = set()  # visited nodes
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        print("current_distance: ", current_distance)
        if current_node in visited:
            continue
        visited.add(current_node)
        print("current_node: ", current_node)
        for neighbor, weight in graph[current_node].items():
            if neighbor not in visited:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    parent[neighbor] = current_node
                    
                    heapq.heappush(priority_queue, (distance, neighbor))
                    print("distances[current_node]: ", distances[current_node])
                    print("parent[current_node]: ", parent[current_node])
    return distances, parent

# Example usage:
src_node = 1
distances, parent = dijkstra(graph, src_node)
print("Distances from source node:", distances)
print("Parent nodes:", parent)