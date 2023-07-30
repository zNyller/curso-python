# Boletins

ficha = []

while True:
    nome = input("Nome: ")
    nota_1 = float(input("Nota 1: "))
    nota_2 = float(input("Nota 2: "))
    media = (nota_1 + nota_2) / 2
    ficha.append([nome, [nota_1, nota_2], media])
    next = input("Quer continuar? [S]im/[N]ão: ").upper()
    while next not in 'SN':
        print("Opção inválida!")
        next = input("Quer continuar? [S]im/[N]ão: ").upper()
    if next == 'N':
        break

print(ficha)