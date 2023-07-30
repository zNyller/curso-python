"""
Calculo do primeiro dígito do CPF
Colete o total dos 9 primeiros dígitos do CPF multiplicando 
cada um dos valores por uma contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

total todos os resultado_1s: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado_1 anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado_1 anterior for maior que 9:
    resultado_1 é 0
contrário disso:
    resultado_1 é o valor da conta

O primeiro dígito do CPF é 7
"""
import random

cpf_9_digitos = ''

for i in range(9):
    cpf_9_digitos += str(random.randint(0, 9))

print(f"CPF 9 Dígitos: {cpf_9_digitos}")

resultado_1 = 0
resultado_2 = 0 
multiplicador_1 = 10

for digito in cpf_9_digitos:
    resultado_1 += int(digito) * multiplicador_1
    multiplicador_1 -= 1

digito_1 = (resultado_1 * 10) % 11

cpf_10_digitos = cpf_9_digitos + str(digito_1)
multiplicador_2 = 11

for digito2 in cpf_10_digitos:
    resultado_2 += int(digito2) * multiplicador_2
    multiplicador_2 -= 1

digito2 = (resultado_2 * 10) % 11

print(f"{resultado_1}, Dígito inválido!") if digito_1 > 9 else print(f"O resultado 1 é: {digito_1}")

print(f"{resultado_2}, Digito inválido!") if digito2 > 9 else print(f"O resultado 2 é: {digito2}")

print(f"CPF gerado pelo cálculo: {cpf_10_digitos}{digito2}")