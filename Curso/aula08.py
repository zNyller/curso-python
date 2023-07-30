# Introdução à função lambda (função anônima de uma linha)
# A função lambda é uma função como qualquer outra em Python. Porém, são funções anônimas
# que contém apenas uma linha. Ou seja, tudo deve ser contido dentro de uma única expressão.

# lista = [
#     {'nome': 'Luiz', 'sobrenome': 'miranda'},
#     {'nome': 'Maria', 'sobrenome': 'Oliveira'},
#     {'nome': 'Daniel', 'sobrenome': 'Silva'},
#     {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
#     {'nome': 'Aline', 'sobrenome': 'Souza'},
# ]

# l1 = sorted(lista, key=lambda item: item['nome'])
# l2 = sorted(lista, key=lambda item: item['sobrenome'])

# def ordena(item):
#     return item['nome']

# def exibir(lista):
#     for item in lista:
#         print(item)
#     print()


# exibir(l1)
# exibir(l2)

# def executa(funcao, *args):
#     return funcao(*args)

# print(
#     executa(
#         lambda x, y: x + y,
#         2, 3
#     )
# )

# # Que seria o mesmo que:
# def soma(x, y):
#     return x + y
# print(executa(soma, 2, 3))


# pessoa = {
#     'nome': 'Aline',
#     'sobrenome': 'Souza',
# }

# dados_pessoa = {
#     'idade': 16,
#     'altura': 1.6,
# }

# pessoas_completa = {**pessoa, **dados_pessoa}

# def mostrar_argumentos_nomeados(*args, **kwargs):
#     print('NÃO NOMEADOS:', args)

#     for chave, valor in kwargs.items():
#         print(chave, valor)

# mostrar_argumentos_nomeados(1, 2, nome='Joana', qlq=123)

# configuracoes = {
#     'arg1': 1,
#     'arg2': 2,
#     'arg3': 3,
#     'arg4': 4,
# }
# mostrar_argumentos_nomeados(**configuracoes)

