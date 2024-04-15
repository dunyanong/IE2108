def convert_to_2_hop(graph):
    two_hop_adjacency_list = {vertex: [] for vertex in graph}
    
    for node in graph:
        for vertex in graph[node]:
            for second_hopped_vertex in graph[vertex]:
                if vertex != second_hopped_vertex:
                    if second_hopped_vertex not in two_hop_adjacency_list[node]:
                        two_hop_adjacency_list[node].append(second_hopped_vertex)

    return two_hop_adjacency_list

# Example 1-hop adjacency list
adjacency_list_1_hop = {
    1: [2, 3],
    2: [1],
    3: [1, 4],
    4: [3]
}

# Convert to 2-hop adjacency list
adjacency_list_2_hop = convert_to_2_hop(adjacency_list_1_hop)
print(adjacency_list_2_hop)