# Depth First Search
graph = {
    1:[2, 4],
    2:[1, 3, 5],
    3:[2, 6],
    4:[1, 5, 7],
    5:[2, 4, 6, 8],
    6:[3, 5, 9],
    7:[4, 8],
    8:[5, 7, 9],
    9:[6, 8]
}
visited = {}

for vertex in graph:
    visited[vertex] = False

def dfs(graph, vertex, visited):
    if not visited[vertex]:
        visited[vertex] = True
        print(vertex, end=" ")
        
        for neighbor in graph[vertex]:
            if not visited[neighbor]:
                dfs(graph, neighbor, visited)
                

dfs(graph, 1, visited)     





