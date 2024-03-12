# Given directed graph
digraph = {
    1: [],
    2: [1],
    3: [2],
    4: [5],
    5: [],
    6: [1, 7],
    7: [2, 3]
}

outdegrees = {node: len(neighbours) for node, neighbours in digraph.items()}
indegrees = {node: 0 for node, neighbours in digraph.items()}

print("outdegrees")
print(outdegrees)


for node, neighbours in digraph.items():
    for neighbour in neighbours:
        if (neighbour): indegrees[neighbour] += 1

print("indegrees")
print(indegrees)


