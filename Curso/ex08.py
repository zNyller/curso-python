# Exercíciossss

import random
from time import sleep

print("Suas opções: \n[ 0 ] PEDRA \n[ 1 ] PAPEL\n[ 2 ] TESOURA")
jogador = int(input("Qual é sua jogada? "))
computador = random.randint(0, 3)
resultado = ''

if jogador == 0:
    jogador = 'Pedra'
    if computador == 0:
        computador = 'Pedra'
        resultado = 'EMPATE!'
    elif computador == 1:
        computador = 'Papel'
        resultado = 'Você Perdeu!'
    else:
        computador = 'Tesoura'
        resultado = 'Você venceu!'
elif jogador == 1:
    jogador = 'Papel'
    if computador == 0:
        computador = 'Pedra'
        resultado = 'Você venceu!'
    elif computador == 1:
        computador = 'Papel'
        resultado = 'EMPATE!'
    else:
        computador = 'Tesoura'
        resultado = 'Você perdeu!'
elif jogador == 2:
    jogador = 'Tesoura'
    if computador == 0:
        computador = 'Pedra'
        resultado = 'Você perdeu!'
    elif computador == 1:
        computador = 'Papel'
        resultado = 'Você venceu!'
    else:
        computador = 'Tesoura'
        resultado = 'EMPATE!'

print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PÔ!!!")
sleep(1)

print('-=' * 10)
print(f"Computador jogou {computador}")
print(f"Jogador jogou {jogador}")
print(resultado)
print('-=' * 10)