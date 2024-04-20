class DisjointSet:
    def __init__(self, vertices):
        self.parent = [-1] * (vertices + 1)
        
    def find(self, node):
        if self.parent[node] == -1:
            return node
        return self.find(self.parent[node])    
        
    def union(self, x, y):
        x_parent = self.find(x)
        y_parent = self.find(y)
        
        if x_parent != y_parent:
            self.parent[x_parent] = y_parent 

class Graph:
    def __init__(self, vertices):
        self.V = vertices + 1
        self.adjacency_list = []
        
    def add_edge(self, u, v, weight):
        self.adjacency_list.append((u, v, weight))
        
    def kruskal(self):
        self.adjacency_list.sort(key=lambda x:x[2])
        disjoint_set = DisjointSet(self.V)
        mst = []
        
        for edge in self.adjacency_list:
            u, v, weight = edge
            u_parent = disjoint_set.find(u)
            v_parent = disjoint_set.find(v)
            
            if u_parent != v_parent:
                mst.append((u, v, weight))
                disjoint_set.union(u_parent, v_parent)
                
        return mst
                
g = Graph(4)

# Add edges to the graph
g.add_edge(1, 2, 10)
g.add_edge(1, 3, 15)
g.add_edge(1, 4, 20)
g.add_edge(2, 3, 35)
g.add_edge(2, 4, 5)
g.add_edge(3, 4, 30)

mst = g.kruskal()

print("Min Spanning Tree: ")
for edge in mst:
    print(edge)