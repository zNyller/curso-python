# Mega-Sena
from random import randint
from time import sleep

lista = []
jogos = []

vezes = int(input("Quantos vezes você quer que eu sorteie? "))
total = 1

while total <= vezes:
    cont = 0
    while True:
        num = randint(0, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1

print(f"-=" *3," SORTEANDO {vezes} JOGOS ", "-=" *3)

for i, l in enumerate(jogos):
    print(f"Jogo {i+1}: {l}")
    sleep(1)