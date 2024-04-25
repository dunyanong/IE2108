def dfs(adj, start):
    global index
    seq[index] = start
    index += 1
    print(start, end=' ')
    for neighbor in adj[start]:
        if neighbor not in seq:
            dfs(adj, neighbor)

# Example usage:
adj = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 4],
    3: [1],
    4: [1, 2]
}

num_nodes = len(adj)
seq = [None] * num_nodes
index = 0

dfs(adj, 0)

print("\nSequence of visited vertices:")
for i in range(num_nodes):
    print(seq[i], end=' ')
