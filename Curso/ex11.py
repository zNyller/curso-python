# Baribilring

temp = []
atletas = []
maior_peso = menor_peso = 0
mais_pesado = mais_leve = ''

while True:
    temp.append(input("Nome: "))
    temp.append(int(input("Peso: ")))
    if len(atletas) == 0:
        maior_peso = menor_peso = temp[1]
        mais_pesado = mais_leve = temp[0]

    else:
        if temp[1] >= maior_peso:
            maior_peso = temp[1]
            mais_pesado = temp[0]
        if temp[1] <= menor_peso:
            menor_peso = temp[1]
            mais_leve = temp[0]
    atletas.append(temp[:])
    temp.clear()

    next = input("Deseja continuar? [S]im/[N]ão: ").upper()
    while next not in 'SN':
        print("Opção inválida!")
        next = input("Deseja continuar? [S]im/[N]ão: ")
    if next == 'N':
        break

print(f"Ao todo, você cadastrou {len(atletas)} atletas.")
print(f"O maior peso foi de {maior_peso}kg. Peso de {mais_pesado}")
print(f"O menor peso foi de {menor_peso}kg. Peso de {mais_leve}")