frase = "O Python é uma linguagem de programação"

indice = 0

maior_qtd = 0
letra_que_mais_apareceu = ''

while indice < len(frase):
    letra_atual = frase[indice]
    maior_qtd_atual = frase.count(letra_atual)

    if letra_atual == ' ':
        indice += 1
        continue

    if maior_qtd < maior_qtd_atual:
        maior_qtd = maior_qtd_atual
        letra_que_mais_apareceu = letra_atual

    indice += 1

print(f"A letra que mais apareceu foi '{letra_que_mais_apareceu}', que apareceu {maior_qtd}x")