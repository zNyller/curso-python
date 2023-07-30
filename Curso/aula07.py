# def is_leap(year):
#     leap = False
    
#     # Write your logic here
#     if year % 4 == 0:
#         leap = True
#     if year % 100 == 0:
#         leap = False
#     if year % 400 == 0:
#         leap = True

#     return leap

# year = int(input())
# print(is_leap(year))

# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Seus valores serão sempre únicos;
# - Não aceitam valores mutáveis;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)
# l1 = [1, 2, 3, 3, 3, 3, 3, 1]
# s1 = set(l1)
# print(s1)
# l2 = list(s1)
# s1 = {1, 2, 3}
# print(3 not in s1)
# for numero in s1:
#     print(numero)

# Métodos úteis:
# add, update, clear, discard
# s1 = set()
# s1.add('Luiz')
# s1.add(1)
# s1.update(('Olá mundo', 1, 2, 3, 4))
# # s1.clear()
# s1.discard('Olá mundo')
# s1.discard('Luiz')
# print(s1)

# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos
# s1 = {1, 2, 3}
# s2 = {2, 3, 4}
# #s3 = s1 | s2
# #s3 = s1 & s2
# #s3 = s2 - s1
# s3 = s1 ^ s2
# print(s3)

# Exemplo de uso dos sets
letras = set()
while True:
    letra = input('Digite: ')
    letras.add(letra.lower())

    if 'z' in letras:
        print('PARABÉNS')
        break

    print(letras)