# Função de contador
from time import sleep

def counter(start, end, step):
    total = start
    step = abs(step)
    if step == 0:
        step = 1
    print('-=' * 30)
    print(f'Contagem de {start} até {end} de {step} em {step}')
    if start < end:
        while total <= end:
            print(f'{total} ', end='', flush=True)
            sleep(0.3)
            total += step
    else:
        while total >= end:
            print(f'{total} ', end='', flush=True)
            sleep(0.3)
            total -= step
    print('FIM!')

counter(10, 100, 8)
counter(10, 0, 2)
print('Agora é a sua vez de personalizar a contagem!')
start = int(input('Início: '))
end = int(input('Fim: '))
step = int(input('Passo: '))
counter(start, end, step)