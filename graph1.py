"""
Exemplo 1

Implementação de um grafo simples
"""

from collections import defaultdict

def find_with_dfs(graph, st, tgt):
    visited = set()
    def _dfs(cur, tgt):
        for neighbor in graph.graph[cur]:
            visited.add(neighbor[0])
            _dfs(neighbor[0], tgt)
    _dfs(st, tgt)
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
