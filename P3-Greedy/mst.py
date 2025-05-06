class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def add_edge(self, u, v, weight):
        self.graph[u][v] = weight
        self.graph[v][u] = weight

    def min_key(self, keys, mst_set):
        min_val = float('inf')
        min_index = None

        for v in range(self.vertices):
            if keys[v] < min_val and not mst_set[v]:
                min_val = keys[v]
                min_index = v

        return min_index
    

    def prim_mst(self):
        keys = [float('inf')] * self.vertices
        parents = [None] * self.vertices  
        keys[0] = 0  
        mst_set = [False] * self.vertices

        parents[0] = -1 

        for _ in range(self.vertices):
            u = self.min_key(keys, mst_set)  

            mst_set[u] = True  

            for v in range(self.vertices):
                if self.graph[u][v] > 0 and not mst_set[v] and keys[v] > self.graph[u][v]:
                    keys[v] = self.graph[u][v]
                    parents[v] = u

        print("Edge \tWeight")
        for i in range(1, self.vertices):
            print(parents[i], "-", i, "\t", self.graph[i][parents[i]])


# Example usage:
g = Graph(5)
g.add_edge(0, 1, 2)
g.add_edge(0, 3, 6)
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 8)
g.add_edge(1, 4, 5)
g.add_edge(2, 4, 7)
g.add_edge(3, 4, 9)

g.prim_mst()
