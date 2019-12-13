"""
Exemplo 1

Uma fila simples
"""

from queue import Queue

q = Queue()

q.put(1)
q.put(2)
q.put(3)
q.put(4)

print(f'Esta é a nossa fila: {q.queue}')

print(f'Primeira remoção: {q.get()}')
print(f'Segunda remoção: {q.get()}')

print(f'Esta é a nossa fila pós remoção: {q.queue}')
