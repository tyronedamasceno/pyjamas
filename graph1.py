"""
Exemplo 1

Implementação de um grafo simples
"""
from collections import defaultdict
from queue import Queue


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, from_, to, weight=1):
        self.graph[from_].append((to, weight))
        self.graph[to]

    def show_graph(self):
        for node, neighbors in self.graph.items():
            print(f'{node}:  {neighbors}')        

    def bfs(self, st, tgt):
        visited = set()
        q = Queue()
        q.put(st)
        while not q.empty():
            cur = q.get()
            visited.add(cur)
            for neighbor, _ in self.graph[cur]:
                if neighbor not in visited:
                    q.put(neighbor)

        return tgt in visited

    def dfs(self, st, tgt):
        visited = set()
        def _dfs(cur):
            visited.add(cur)
            for neighbor, _ in self.graph[cur]:
                if neighbor not in visited:
                    _dfs(neighbor)
        _dfs(st)
        return tgt in visited


my_graph = Graph()
my_graph.add_edge(1, 2)
my_graph.add_edge(1, 3)
my_graph.add_edge(2, 4)
my_graph.add_edge(2, 5)
my_graph.add_edge(3, 6)
