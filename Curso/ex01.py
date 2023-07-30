"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

# Ex01
num = input("Digite um número inteiro: ")

if num.isdigit():
    num_int = int(num)
    par_impar = num_int % 2 == 0
    par_impar_texto = "ímpar"
    if par_impar:
        par_impar_texto = "par"
    print(f"O número {num} é {par_impar_texto}!")

else:
    print("Isso não é um número inteiro!")

# Ex02
time = input("Que horas são? ")

time = int(time)

if time >= 0 and time < 12:
    print(f"São {time} horas! Bom dia! :)")

elif time >= 12 and time < 18:
    print(f"São {time} horas! Boa tarde! :)")
else:
    print(f"São {time} horas! Boa noite! :)")

#Ex03
name = input("Digite seu nome: ")

if len(name) <= 4:
    print("Seu nome é curto!")

elif len(name) > 4 and len(name) <= 6:
    print("Seu nome é médio!")
else:
    print("Seu nome é grande!")