# Caixa eletrônico

cedula = 50
total = total_cedula = 0

value = input("Qual valor você quer sacar? R$")

try:
    value_int = int(value)
    total = value_int
except ValueError:
    print("Digite um número inteiro válido!")

while True:
    if total >= cedula:
        total -= cedula
        total_cedula += 1
    else:
        if total_cedula > 0:
            print(f'Total de {total_cedula} cédulas de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        total_cedula = 0
        if total == 0:
            break
