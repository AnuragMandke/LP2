from collections import defaultdict, Counter, deque

# Graph implementation with adjacency list and traversal methods
class Graph:
    # Initialize the graph with empty adjacency list
    def __init__(self):
        self.adj = defaultdict(list)

    # Add an edge from u to v; if bidir, add reverse edge as well
    def add_edge(self, u, v, bidir=True):
        self.adj[u].append(v)
        if bidir:
            self.adj[v].append(u)

    # Print the adjacency list representation of the graph
    def print_graph(self):
        for u, vs in self.adj.items():
            print(f"{u} -> {' -> '.join(vs)}")

    # Compute and print in-degree and out-degree for each node
    def print_degrees(self):
        indeg = Counter()
        # Count in-degrees by iterating through adjacency lists
        for u, vs in self.adj.items():
            for v in vs:
                indeg[v] += 1
        print("Node : In : Out")
        for u, vs in self.adj.items():
            print(f"{u} : {indeg[u]} : {len(vs)}")



    # Perform depth-first search starting from 'start' using recursion
    def dfs(self, start):
        def _dfs(u):
            print(u, end=" ")
            # recurse on each unvisited neighbor
            for v in self.adj[u]:
                if v not in vis:
                    vis.add(v)
                    _dfs(v)
        vis = {start}      # initialize visited set
        _dfs(start)
        print()

    # Perform breadth-first search recursively starting from 'start'
    def bfs_recursive(self, start):
        def _bfs(queue, vis):
            if not queue:
                return
            next_queue = []
            for u in queue:
                print(u, end=" ")
                for v in self.adj[u]:
                    if v not in vis:
                        vis.add(v)
                        next_queue.append(v)
            _bfs(next_queue, vis)
        vis = {start}
        _bfs([start], vis)
        print()
1

if __name__ == "__main__":
    g = Graph()
    # build a graph with branching and cross‐links
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('B', 'D')
    g.add_edge('B', 'E')
    g.add_edge('C', 'F')
    g.add_edge('E', 'F')
    g.add_edge('D', 'G')
    g.add_edge('F', 'H')
    g.add_edge('G', 'H')

    print("Adjacency list:")
    g.print_graph()

    print("\nBFS starting at A:")
    g.bfs('A')

    print("DFS starting at A:")
    g.dfs('A')

    print("\nRecursive BFS starting at A:")
    g.bfs_recursive('A')
    print("Iterative DFS starting at A:")
    g.dfs_iterative('A')