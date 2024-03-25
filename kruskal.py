def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

## To avoid cycles
def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)

    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1

def kruskal(graph):
    edges = []
    result = []

    for u in graph:
        for v, w in graph[u]:
            edges.append((w, u, v))

    edges.sort()

    parent = {}
    rank = {}

    for u in graph:
        parent[u] = u
        rank[u] = 0

    for edge in edges:
        w, u, v = edge
        x = find(parent, u)
        y = find(parent, v)

        if x != y:
            result.append((u, v, w))
            union(parent, rank, x, y)

    return result

graph = {
    "A": [("B", 2), ("D", 5)],
    "B": [("A", 2), ("C", 1), ("D", 3)],
    "C": [("B", 1), ("D", 4)],
    "D": [("A", 5), ("B", 3), ("C", 4)]
}

minimum_spanning_tree = kruskal(graph)
print("Minimum Spanning Tree:")
for u, v, w in minimum_spanning_tree:
    print(f"{u} - {v}: {w}")