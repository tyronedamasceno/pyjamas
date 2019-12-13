"""
Exemplo 1

Uma pilha simples
"""

from queue import LifoQueue

p = LifoQueue()

p.put(1)
p.put(2)
p.put(3)
p.put(4)

print(f'Esta é a nossa pilha: {p.queue}')

print(f'Primeira remoção: {p.get()}')
print(f'Segunda remoção: {p.get()}')

print(f'Esta é a nossa pilha pós remoção: {p.queue}')
