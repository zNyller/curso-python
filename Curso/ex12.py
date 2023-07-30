temp = 0
numeros = [[], []]

for x in range(0, 7):
    temp = int(input(f"Digite o {x+1}° número: "))
    if temp % 2 == 0:
        numeros[0].append(temp)
    else:
        numeros[1].append(temp)

print(f'Números pares: {numeros[0]}')
print(f'Números ímpares: {numeros[1]}')