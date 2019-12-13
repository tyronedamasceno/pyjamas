"""
Exemplo 2

Dado uma sequência não vazia de parênteses, colchetes e chaves,
verifique se é válida.

Exemplos válidos:

[], (), ((())), ([{}]), []{}(), [(){}]

Exemplos inválidos:

(, (], {[}], )(, {}}, ({[}]), (()
"""

from queue import LifoQueue
opens = ('(', '{', '[')
closes = (')', '}', ']')
matches = {o: c for o, c in zip(opens, closes)}

s = LifoQueue()

seq = input()

valid = True

for bracket in seq:
    if bracket in opens:
        s.put(bracket)
    else:
        top = s.get()
        if bracket != matches[top]:
            valid = False
            break

valid = valid and s.empty()

print('A sequência é valida' if valid else 'A sequência não é válida')
