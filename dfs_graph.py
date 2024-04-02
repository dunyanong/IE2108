graph = {
    1: [3],
    2: [3, 6],
    3: [1, 2, 4, 7],
    4: [3, 8],
    5: [6],
    6: [2, 5, 7, 10],
    7: [3, 6, 8, 11],
    8: [4, 7, 9, 12],
    9: [8],
    10: [6, 11],
    11: [7, 10, 12, 13],
    12: [8, 11],
    13: [11]
}

def dfs(start, graph):
    visited = set()
    stack = [start]
    
    res = []
    
    while stack:
        current = stack.pop()
        
        if (current not in visited):
            visited.add(current)
            res.append(current)
            
            for neighbour in graph[current]:
                if neighbour not in visited:
                    stack.append(neighbour)     
            
    return res

print(dfs(1, graph))


