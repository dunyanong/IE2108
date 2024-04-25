class DisjointSet:
    def __init__(self, vertices):
        self.parent = [-1] * (vertices + 1)
        
    def find(self, node):
        if self.parent[node] == -1:
            return node
        return self.find(self.parent[node])
    
    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        
        if x_root != y_root:
            self.parent[x_root] = y_root
            
class Graph:
    def __init__(self, vertices):
        self.V = vertices + 1
        self.adjacency_list = []
        
    def add_edge(self, u, v, weight):
        self.adjacency_list.append((u, v, weight))
        
    def kruskal(self):
        mst = []
        self.adjacency_list.sort(key=lambda weight: weight[2])
        disjoinset = DisjointSet(self.V)
        
        for u, v, weight in self.adjacency_list: # could be bugged with .items()
            u_parent = disjoinset.find(u)
            v_parent = disjoinset.find(v)
            
            if u_parent != v_parent:

                disjoinset.union(u_parent, v_parent)
                mst.append((u, v, weight))
        
        return mst
    
g = Graph(4)

# Add edges to the graph
g.add_edge(0, 1, 2)
g.add_edge(1, 3, 1)
g.add_edge(0, 2, 3)
g.add_edge(2, 3, 4)
g.add_edge(2, 4, 10)
g.add_edge(3, 4, 2)

mst = g.kruskal()

print(mst)