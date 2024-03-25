# Kruskal algorithm
graph = {
    1: {
       2: 5,
       5: 7,
       6: 14 
    },
    2: {
        1: 5,
        3: 7,
        5: 1,
        7: 2
    },
    3: {
        2: 7,
        4: 10,
        7: 6,
        8: 6
    },
    4: {
        3: 10,
        8: 4
    },
    5: {
        1: 7,
        2: 1,
        6: 4,
        9: 4
    },
    6: {
        1: 14,
        5: 4,
        7: 8,
        10: 6,
        15: 1
    },
    7: {
        2: 2,
        3: 6,
        8: 7,
        11: 4
    },
    8: {
        3: 6, 
        4: 4, 
        7: 7, 
        12: 1
    },
    9: {
        5: 4,
        10: 4,
        13: 7
    },
    10: {
        6: 6,
        9: 4,
        13: 2,
        14: 8
    },
    11: {
        7: 4, 
        12: 11, 
        14: 6, 
        15: 13
    },
    12: {
        8: 1, 
        11: 11, 
        16: 2
    },
    13: {
        9: 7,
        10: 2
    },
    14: {
        10: 8, 
        11: 6, 
        15: 9
    },
    15: {
        6: 1,
        11: 13,
        14: 9,
        16: 5
    },
    16: {
        12: 2,
        15: 5
    }
}
def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

def union(parent, rank, x, y):
    x_root = find(parent, x)
    y_root = find(parent, y)

    if rank[x_root] < rank[y_root]:
        parent[x_root] = y_root
    elif rank[x_root] > rank[y_root]:
        parent[y_root] = x_root
    else:
        parent[y_root] = x_root
        rank[x_root] += 1

def kruskal(graph):
    edges = []
    for u in graph:
        for v in graph[u]:
            edges.append((u, v, graph[u][v]))

    edges.sort(key=lambda x: x[2]) # sort them based on weight of edges

    parent = {}
    rank = {}

    for node in graph:
        parent[node] = node
        rank[node] = 0

    minimum_spanning_tree = []

    for edge in edges:
        u, v, weight = edge
        
        # uses the find and union functions to determine the connected components and merge them as necessary.
        u_root = find(parent, u) 
        v_root = find(parent, v)
        if u_root != v_root:
            minimum_spanning_tree.append((u, v, weight))
            union(parent, rank, u_root, v_root)

    return minimum_spanning_tree

minimum_spanning_tree = kruskal(graph)
print("Vertex A, Vertex B, Weight")
for edge in minimum_spanning_tree:
    print(edge)

