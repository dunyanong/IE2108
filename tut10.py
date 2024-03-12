# Question 4: Breadth First Search

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

def bfs(graph, source):
    visited = set()
    queue = [source]
    visited.add(source)
    while len(queue) > 0:
        current = queue.pop(0)
        print(current)
        for neighbour in graph[current]:
            if neighbour not in visited:
                queue.append(neighbour)
                visited.add(neighbour)

bfs(graph, 1)
