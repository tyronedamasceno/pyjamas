"""
Exemplo 1

Implementação de um grafo simples
"""
from collections import defaultdict
from queue import Queue


def find_with_dfs(graph, st, tgt):
    visited = set()
    def _dfs(cur):
        visited.add(cur)
        for neighbor, _ in graph.graph[cur]:
            if neighbor not in visited:
                _dfs(neighbor)
    _dfs(st, tgt)
    return tgt in visited


def find_with_bfs(graph, st, tgt):
    visited = set()
    q = Queue()
    q.put(st)

    while not q.empty():
        cur = q.get()
        visited.add(cur)
        for neighbor, _ in graph.graph[cur]:
            if neighbor not in visited:
                q.put(neighbor)

    return tgt in visited


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, from_, to, weight=1):
        self.graph[from_].append((to, weight))
        self.graph[to]

    def show_graph(self):
        for node, neighbors in self.graph.items():
            print(f'{node}:  {neighbors}')        

my_graph = Graph()
my_graph.add_edge(1, 2)
my_graph.add_edge(1, 3)
my_graph.add_edge(2, 4)
my_graph.add_edge(2, 5)
my_graph.add_edge(3, 6)
