# DocStrings

def contador(s, e, st):
    """
    -> Realiza uma contagem e mostra na tela.
    :parâm. s: início da contagem
    :parâm. e: final da contagem
    :parâm. s: passo da contagem
    :return: sem retorno
    Função criada por Nyller.
    """
    c = s
    while c <= e:
        print(f'{c}', end='')
        c += st
    print('FIM!')

help(contador)
