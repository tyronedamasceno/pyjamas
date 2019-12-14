"""
Exemplo 1

Implementação de um grafo simples
"""

from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, from_, to):
        self.graph[from_].append(to)
        self.graph[to]

    def show_graph(self):
        for node, neighbors in self.graph.items():
            print(f'{node}:  {neighbors}')
