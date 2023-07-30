# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.

# lista = []
# for numero in range(10):
#     lista.append(numero)
# print(lista)

# lista = [numero for numero in range(10)]
# print(lista)

# lista = [
#     numero * 2
#     for numero in range(10)
# ]
# print(lista)

# Mapeamento de dados em list comprehension
# produtos = [
#     {'nome': 'p1', 'preco': 20},
#     {'nome': 'p2', 'preco': 10},
#     {'nome': 'p3', 'preco': 30},
# ]
# novos_produtos = [
#     {**produto, 'preco': produto['preco'] * 1.05} # Aqui está sendo criado um novo dicionário {} que está desempacotando os dicionários da List Comprehension. E Alterando a chave 'preço' do produto com um aumento de 5%.
#     if produto['preco'] > 20 else {**produto} # Aqui um if ternário para aumentar o preço apenas se o preço antigo for maior que 20.
#     for produto in produtos
# ]

# print(*produtos)
# print(*novos_produtos, sep='\n')

# # Dictionary Comprehension e Set Comprehension
# produto = {
#     'nome': 'Caneta Azul',
#     'preco': 2.5,
#     'categoria': 'Escritório',
# }

# dc = {
#     chave: valor.upper()
#     if isinstance(valor, str) else valor
#     for chave, valor
#     in produto.items()
#     if chave != 'categoria'
# }

# lista = [
#     ('a', 'valor a'),
#     ('b', 'valor a'),
#     ('b', 'valor a'),
# ]
# dc = {
#     chave: valor
#     for chave, valor in lista
# }

# s1 = {2 ** i for i in range(10)}
# print(s1)

# lista = [
#     'a', 1, 1.1, True, [0, 1, 2], (1, 2),
#     {0, 1}, {'nome': 'Luiz'},
# ]

# for item in lista:
#     if isinstance(item, set):
#         print('SET')
#         item.add(5)
#         print(item, isinstance(item, set))

#     elif isinstance(item, str):
#         print('STR')
#         print(item.upper())

#     elif isinstance(item, (int, float)):
#         print('NUM')
#         print(item, item * 2)
#     else:
#         print('OUTRO')
#         print(item)

#Check if the "Person" object has the "age" property:

class Person:
  name = "John"
  age = 36
  country = "Norway"

x = hasattr(Person, 'age')
print(x)

import sys

lista = [n for n in range(1000)]
generator = (n for n in range(1000))

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

print(generator)

for n in generator:
    print(n)

def generator(n=0, maximum=10):
    while True:
        yield n
        n += 1

        if n >= maximum:
            return


gen = generator(maximum=1000000)
for n in gen:
    print(n)