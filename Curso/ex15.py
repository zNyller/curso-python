# Área

def somarArea(width, length):
    return f'A área de um terreno {width}x{length} é de {width * length}m²'


print(' CONTROLE DE TERRENOS ')
print('======================')
width = float(input('Largura (m): '))
length = float(input('Comprimento (m): '))
area_total = somarArea(width, length)
print(area_total)

def write(msg):
    length = len(msg) + 4
    print('-' * length)
    print(f'  {msg}')
    print('-' * length)


write('Curso em Vídeo')
write('Furia')
write('Domingão de programação no Pythonzão')