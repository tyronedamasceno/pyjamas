""""
Exemplo de Conjuntos
"""

s1 = set()
# s2 = {} 
s2 = {1, 2}

print('Criando um conjunto de números ao quadrado\n')

set_squares = {
    v**2 for v in range(-3, 4)
}

for k in set_squares:
    print(k)

print(f'\nEste conjunto possui {len(set_squares)} elementos\n')
