def bfs(start, target, graph):
    visited = set()
    queue = [start]
    
    while queue:
        current = queue.pop(0)
        visited.add(current)
        if current ==  target:
            return True
        
        for node in graph[current]:
            if node not in visited:
                queue.append(node)
                visited.add(node)
                
    return False

# Example usage:
graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"]
}


print(bfs("A", "F", graph))
