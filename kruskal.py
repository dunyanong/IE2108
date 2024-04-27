class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adjacency_list = []
        
    def add_edge(self, u, v, weight):
        self.adjacency_list.append((u, v, weight))
        
    def kruskal(self):
        mst = []
        disjoint_set = DisjointSet(len(self.adjacency_list))
        self.adjacency_list.sort(key=lambda x: x[2])
        
        for u , v, weight in self.adjacency_list:
            u_root = disjoint_set.find(u)
            v_root = disjoint_set.find(v)
            
            if u_root != v_root:
                disjoint_set.union(u, v)
                mst.append((u , v, weight))
        return mst

class DisjointSet:
    def __init__(self, vertices):
        self.parents = [-1] * (vertices)
        
    def find(self, node):
        if self.parents[node] == -1:
            return node
        return self.find(self.parents[node])
        
    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        
        if (x_root != y_root):
            self.parents[x_root] = y_root
    
g = Graph(6)

# Add edges to the graph
g.add_edge("A", "C", 1)
g.add_edge("A", "B", 2)
g.add_edge("A", "F", 3)
g.add_edge("B", "F", 1)
g.add_edge("B", "D", 3)
g.add_edge("B", "E", 4)
g.add_edge("E", "F", 2)

mst = g.kruskal()

print(mst)