# Ex
'''As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores 
e lhe contraram para desenvolver o programa que calculará os reajustes.

Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, 
baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% 
Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.'''

def filter():
    while True:
        try:
            salary = int(input('Digite um salário: R$'))
            if salary <= 0:
                print('Por favor, insira um salário positivo!')
            else:
                return salary
        except(ValueError, TypeError):
            print('Salário inválido! Por favor, digite um número válido!')

def adjustment(salary):
    if salary < 280:
        percentual = 20

    elif salary < 700:
        percentual = 15

    elif salary < 1500:
        percentual = 10
    else:
        percentual = 5

    adjust = salary * (1 + percentual / 100)
    value = adjust - salary

    return salary, percentual, value, adjust

salary_input = filter()
inform = adjustment(salary_input)

print(f'Salary before adjustment: R${inform[0]}')
print(f'Percentual added: {inform[1]}%')
print(f'Value raised: R${inform[2]:.2f}')
print(f'New Salary: R${inform[3]:.2f}')