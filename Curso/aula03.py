# Rascunhos e tal

# Usando o randint - gerar números aleatórios
from random import randint

numeros = []
numeros_pares = []
numeros_impares = []

while True:
    numero = input("Digite um número: ")
    try:
        numero_int = int(numero)
    except ValueError:
        print("Digite um número válido!")
        continue
    numeros.append(numero_int)

    numeros_pares.append(numero) if numero_int % 2 == 0 else numeros_impares.append(numero)

    next = input("Deseja continuar? [S]im / [N]ão: ").upper()
    while next not in "SN":
        print("Opção inválida!")
        next = input("Deseja continuar? [S]im / [N]ão: ").upper()
    if next == 'N':
        break

print(f"Lista de números: {numeros}")
print(f"{len(numeros)} números digitados.")
numero_em_ordem = sorted(numeros, reverse=True)
print(f"Lista de números em ordem decrescente: {numero_em_ordem}")
print('-='*30)
print(f"O maior número é o {max(numeros)}\nO menor número é o {min(numeros)}")
print("O número 5 faz parte da lista!")if 5 in numeros else print("O número 5 não aparece na lista!")
print(f"Números pares: {numeros_pares}")
print(f"Números ímpares: {numeros_impares}")
