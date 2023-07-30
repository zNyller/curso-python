from time import sleep

def bigger(*num):
    print('-=' * 30)
    print('Analisando os valores passados...')
    for n in num:
        print(f'{n} ', end='', flush=True)
        sleep(0.3)
    if len(num) == 0:
        print('Foram informados 0 valores ao todo.')
        print(f'O maior valor informado foi 0.')
        return
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {max(num)}.')
    sleep(1)

bigger(2, 9, 4, 5, 7, 1)
bigger(4, 7, 0)
bigger(1, 2)
bigger(6)
bigger()