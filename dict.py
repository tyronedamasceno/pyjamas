""""
Exemplo de Dicionários
"""

d1 = dict()
d2 = {}
d3 = {'py': 'jamas'}

s1 = set()
# s2 = {} 
s2 = {1, 2}

print('Criando um dict de pares números e seu valor ao quadrado\n')

dict_squares = {
    v: v**2 for v in range(-3, 4)
}

for k, v in dict_squares.items():
    print(f'{k}: {v}')

print(f'\nEste dicionário possui {len(dict_squares)} pares\n')
