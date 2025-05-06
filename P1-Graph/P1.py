from collections import defaultdict, Counter

class Graph:
    def __innit__(self):
        self.adj = defaultdict(list)

    def add_edge(self,u, v, bidir = True):
        self.adj[u].append(v)
        if bidir:
            self.adj[v].append(u)

    def print_graph(self):
        for u, vs in self.adj.items():
            print(f"{u} -> {'->'.join(vs)}")

    def dfs(self, start):
        def _dfs(u):
            print(u, end = " ")
            for v in self.adj[u]:
                if v not in vis:
                    vis.add(v)
                    _dfs(v)

        vis = {start}
        _dfs(start)

    def bfs(self, start):
        def _bfs(queue, vis):
            if not queue:
                return
            next_queue = []
            for u in queue:
                print(u, end = " ")
                for v in self.adj[u]:
                    if v not in vis:
                        vis.add(v)
                        next_queue.append(v)
            _bfs(next_queue, vis)
        vis = {start}
        _bfs([start], vis)
