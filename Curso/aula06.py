# Dicionários

pessoa = {
    'nome': 'Edu',
    'sobrenome': 'Sampaio',
    'idade': 20,
    'altura': 1.65,
    'endereços': [
        {'rua': 'tal tal', 'número': 123},
        {'rua': 'outra rua', 'número': 321},
    ]
}

print(pessoa['nome'])
print(pessoa['sobrenome'])

print()

pessoa.update(nome='Sam', sobrenome='Sepi0l')
print(pessoa)

# print()

# for chave in pessoa:
#     print(chave, pessoa[chave])

# print()

# print(pessoa.items())
# print(pessoa.values())
# print(pessoa.keys())

# print()

# for k, v in pessoa.items():
#     print(f'O {k} é {v}')

# estado = {}
# brasil = []
# for count in range(0, 3):
#     estado['uf'] = str(input('Unidade Federativa: '))
#     estado['sigla'] = str(input('Sigla do Estado: '))
#     brasil.append(estado.copy())
# for e in brasil:
#     for v in e.values():
#         print(v, end=' ')
#     print()