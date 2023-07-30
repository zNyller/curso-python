from random import randint
from time import sleep

def sorteia(lista):
    print(f'Sorteando 5 valores da lista: ', end='')
    for cont in range(0, 5):
        num = randint(1, 10)
        numeros.append(num)
        print(f'{num} ', end='', flush=True)
        sleep(0.3)
    print('PRONTO!')

def somaPar(numeros_sorteados):
    total_pares = 0
    for n in numeros_sorteados:
        if n % 2 == 0:
            total_pares += n
    print(f'Somando os valores pares de {numeros_sorteados}, temos {total_pares}!')

numeros = []
sorteia(numeros)
somaPar(numeros)