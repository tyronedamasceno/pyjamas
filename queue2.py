"""
Exemplo 2

Dada uma pilha de n cartas enumeradas de 1 até n com a carta 1 no topo
e a carta n na base. 
A seguinte operação é ralizada enquanto tiver 2 ou mais cartas na pilha.

Jogue fora a carta do topo e mova a próxima carta (a que ficou no topo)
para a base da pilha.

Sua tarefa é encontrar a sequência de cartas descartadas e a última carta
remanescente.

Cada linha de entrada (com exceção da última) contém um número n ≤ 50. 
A última linha contém 0 e não deve ser processada. Cada número de entrada
produz duas linhas de saída. A primeira linha apresenta a sequência de cartas
descartadas e a segunda linha apresenta a carta remanescente.

https://www.urionlinejudge.com.br/judge/pt/problems/view/1110
"""

from queue import Queue

q = Queue()
n = int(input())

for i in range(n):
    q.put(i+1)

discards = []
while q.qsize() > 1:
    discards.append(str(q.get()))
    q.put(q.get())

discards = ', '.join(discards)
print(f'Discarded cards: {discards}')
print(f'Remaining card: {q.get()}')
